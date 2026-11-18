#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Truy vết requirement <-> checklist/test case của một tính năng.

Dùng:
  python -X utf8 scripts/truy-vet.py kiem <dự-án> <tính-năng>
      So requirement hiện tại với mốc đã chốt lần trước, báo mã nào đổi và test case nào
      cần xem lại, ghi lại truy-vet.md và khối "Lịch sử thay đổi" trong checklist/test case.
      Không đổi mốc. Thoát mã 1 nếu có việc cần làm.
  python -X utf8 scripts/truy-vet.py chot <dự-án> <tính-năng> -m "đã làm gì" [--doi checklist,test-case,requirement]
      Chốt mốc mới: "test case hiện tại đã khớp requirement hiện tại". Ghi một dòng lịch sử.

Ví dụ: python -X utf8 scripts/truy-vet.py kiem banking-lite dang-nhap

Cần trong thư mục testing/<dự-án>/<tính-năng>/ file truy-vet-cau-hinh.json (đường dẫn, tiền tố mã,
tên ngắn của từng mã). File trạng thái truy-vet-trang-thai.json do script tự tạo; không sửa tay.
Cách tính "mã đổi": băm nội dung dòng của mã trong SRS (bỏ cột bằng chứng/nhãn) và dòng TL trong
bảng soát (chỉ cột mã + nội dung trả lời). Đổi link, đổi ngày không làm mã bị tính là đổi.
"""
import argparse
import datetime
import hashlib
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CODE = r"(?:S\d\d-AC\d\d|R\d\d|M\d\d|TL-\d\d)"
TOKEN = re.compile(r"(?<![\w-])(" + CODE + r")(?!\w)")
START = "<!-- LICH-SU:BAT-DAU (tự sinh bởi scripts/truy-vet.py, không sửa tay) -->"
END = "<!-- LICH-SU:KET-THUC -->"


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def h(parts):
    return hashlib.sha1("¦".join(norm(p) for p in parts).encode("utf-8")).hexdigest()[:12]


def cut(s, n=150):
    s = norm(s).replace("|", "¦")
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def read(p):
    return Path(p).read_text(encoding="utf-8")


def parse_srs(text, prefix):
    out = {}
    keep = {"S": 5, "R": 3, "M": 4}
    pat = re.compile(r"^\| `" + re.escape(prefix) + r"-(S\d\d-AC\d\d|R\d\d|M\d\d)` \|")
    for n, line in enumerate(text.splitlines(), 1):
        m = pat.match(line)
        if not m or m.group(1) in out:
            continue
        code = m.group(1)
        c = cells(line)
        k = keep[code[0]]
        nv = {"S": 4, "R": 2, "M": 2}[code[0]]
        out[code] = dict(hash=h(c[:k]), nghia=c[1] if len(c) > 1 else "", nguyen_van=c[nv] if len(c) > nv else "", dong=n)
    return out


def parse_tl(text):
    out = {}
    for n, line in enumerate(text.splitlines(), 1):
        m = re.match(r"^\| (TL-\d\d) \|", line)
        if not m or m.group(1) in out:
            continue
        c = cells(line)
        out[m.group(1)] = dict(hash=h(c[:2]), nghia="", nguyen_van=c[1] if len(c) > 1 else "", dong=n)
    return out


def parse_ba(text, prefix):
    """Gom, theo từng mã SRS, các dòng của bảng soát: điều BA trả lời, hệ thống hiện tại, chỗ còn mở."""
    out = {}
    pat = re.compile(r"^\| `" + re.escape(prefix) + r"-(S\d\d-AC\d\d|R\d\d|M\d\d)` \|")
    in5 = False
    for line in text.splitlines():
        if line.startswith("## "):
            in5 = line.startswith("## 5.") or line.startswith("## 6.")
        m = pat.match(line)
        if not in5 or not m:
            continue
        c = cells(line)
        if len(c) < 6:
            continue
        s, o = c[3], out.setdefault(m.group(1), dict(ba=[], hien_tai=[], chua_chot=[], khac=False))
        khac = "khác hệ thống" in s or "có thể khác" in s
        refs = sorted(set(re.findall(r"TL-\d\d", s)))
        if s.startswith("❓"):
            q = re.search(r"\*\*([ABC]\d+)\.", c[4])
            o["chua_chot"].append(q.group(1) if q else "?")
        elif "hành vi hiện tại" in s:
            o["hien_tai"].append(c[2])
        elif "Suy ra" in s or "theo TL" in s:
            o["ba"].append(dict(text=c[2], refs=refs, suy_ra="Suy ra" in s, stt=s))
            o["khac"] = o["khac"] or khac
    return out


def parse_tc(text, ncols):
    out = {}
    for line in text.splitlines():
        m = re.match(r"^\| (TC-\d+) \|", line)
        if not m:
            continue
        c = cells(line)
        if len(c) != ncols:
            sys.exit(f"{m.group(1)}: số cột {len(c)}, cần {ncols}")
        out[m.group(1)] = dict(tinh_huong=c[1], uu_tien=c[2] if ncols == 5 else "", nguon=c[-1],
                               ma=sorted(set(TOKEN.findall(c[-1]))), row=norm(line))
    return out


def date_in(text, label):
    m = re.search(re.escape(label) + r"[^0-9]{0,10}(\d{4}-\d\d-\d\d)", text)
    return m.group(1) if m else "?"


def rel(frm_dir, target):
    return os.path.relpath(target, frm_dir).replace("\\", "/")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("lenh", choices=["kiem", "chot"])
    ap.add_argument("du_an")
    ap.add_argument("tinh_nang")
    ap.add_argument("-m", "--mo-ta", default="")
    ap.add_argument("--doi", default="checklist,test-case")
    ap.add_argument("--ngay", default=datetime.date.today().isoformat())
    a = ap.parse_args()

    d = ROOT / "testing" / a.du_an / a.tinh_nang
    cfg_p = d / "truy-vet-cau-hinh.json"
    st_p = d / "truy-vet-trang-thai.json"
    if not cfg_p.exists():
        sys.exit(f"Chưa có {cfg_p}")
    cfg = json.loads(read(cfg_p))
    srs_t, bs_t = read(ROOT / cfg["srs"]), read(ROOT / cfg["bang_soat"])
    ck_t, tc_t = read(ROOT / cfg["checklist"]), read(ROOT / cfg["test_case"])

    cur = parse_srs(srs_t, cfg["tien_to"])
    tls = parse_tl(bs_t)
    ba = parse_ba(bs_t, cfg["tien_to"])
    for k, v in cur.items():
        if not k.startswith("TL"):
            v["ba_hash"] = h([x for e in ba.get(k, {}).get("ba", []) for x in (e["text"], e["stt"])])
    cur.update(tls)
    for k, v in cur.items():
        v["ten"] = cfg["ten_ngan"].get(k) or cut(v["nghia"] or v["nguyen_van"], 40)
    ck = parse_tc(ck_t, 5)
    tcs = parse_tc(tc_t, 7)

    state = json.loads(read(st_p)) if st_p.exists() else {"ma": {}, "tc": {}, "lich_su": [], "nguon_chot": {}}
    dua_tren = dict(srs=date_in(srs_t, "Cập nhật lần cuối"), bang_soat=date_in(bs_t, "Cập nhật gần nhất"),
                    tl_cuoi=max(tls, default="?"))

    problems = []
    # Checklist và test case phải khớp nhau
    if set(ck) != set(tcs):
        problems.append(f"Checklist và test case lệch mã TC: chỉ ở checklist {sorted(set(ck)-set(tcs))}, chỉ ở test case {sorted(set(tcs)-set(ck))}")
    for k in sorted(set(ck) & set(tcs)):
        if ck[k]["ma"] != tcs[k]["ma"]:
            problems.append(f"{k}: mã nguồn ở checklist {ck[k]['ma']} khác test case {tcs[k]['ma']}")
    # Mã requirement trạng thái
    def st_ma(code):
        base = state["ma"].get(code)
        if code not in cur:
            return "Đã bỏ khỏi nguồn" if base else None
        if base is None:
            return "Mới"
        return "Đã đổi" if why(code) else "Không đổi"

    def why(code):
        base, v = state["ma"].get(code), cur.get(code)
        if not base or not v:
            return []
        r = []
        if base["hash"] != v["hash"]:
            r.append("nội dung SRS" if not code.startswith("TL") else "nội dung câu trả lời")
        if "ba_hash" in base and base["ba_hash"] != v.get("ba_hash"):
            r.append("phần theo BA trong bảng soát")
        return r

    all_codes = sorted(set(cur) | set(state["ma"]), key=lambda c: (c.startswith("TL"), c))
    ma_st = {c: st_ma(c) for c in all_codes}
    tc_of = {c: [] for c in all_codes}
    for t in sorted(tcs):
        for c in tcs[t]["ma"]:
            tc_of.setdefault(c, []).append(t)
            ma_st.setdefault(c, "Không có trong nguồn")
    # Mã dùng trong TC mà không có trong SRS/bảng soát
    for c, v in ma_st.items():
        if v == "Không có trong nguồn":
            problems.append(f"Mã {c} được dùng ở test case nhưng không có trong SRS/bảng soát")
    srs_codes = [c for c in all_codes if not c.startswith("TL") and c in cur]
    chua_co_tc = [c for c in srs_codes if not tc_of.get(c)]

    def row_h(t):
        return h([ck.get(t, {}).get("row", ""), tcs.get(t, {}).get("row", "")])

    def st_tc(t):
        b = state["tc"].get(t)
        if b is None or b.get("da_bo"):
            return "Mới, chưa chốt"
        doi = [c for c in tcs[t]["ma"] if ma_st.get(c) in ("Đã đổi", "Đã bỏ khỏi nguồn")]
        sua = b["row_hash"] != row_h(t)
        if doi:
            return "Cần xem lại" + (" (đã sửa, chưa chốt)" if sua else "")
        if sua:
            return "Đã sửa, chưa chốt"
        return "Còn đúng"

    tc_st = {t: st_tc(t) for t in sorted(tcs)}
    tc_bo = sorted(t for t in state["tc"] if t not in tcs and not state["tc"][t].get("da_bo"))
    ma_doi = [c for c, v in ma_st.items() if v in ("Đã đổi", "Đã bỏ khỏi nguồn")]
    ma_moi = [c for c, v in ma_st.items() if v == "Mới"]

    today = a.ngay
    if a.lenh == "chot":
        if not a.mo_ta.strip():
            sys.exit('Cần -m "đã làm gì" để ghi vào lịch sử.')
        if problems:
            print("Chưa chốt được, còn vấn đề:")
            for p in problems:
                print(" -", p)
            sys.exit(1)
        tc_moi = [t for t in tcs if t not in state["tc"] or state["tc"][t].get("da_bo")]
        tc_sua = [t for t in tcs if t in state["tc"] and not state["tc"][t].get("da_bo") and state["tc"][t]["row_hash"] != row_h(t)]
        for c, v in cur.items():
            old = state["ma"].get(c)
            doi = not old or old["hash"] != v["hash"] or old.get("ba_hash") != v.get("ba_hash")
            state["ma"][c] = dict(hash=v["hash"], ba_hash=v.get("ba_hash"), ngay_chot=today if doi else old["ngay_chot"])
        for c in [c for c in state["ma"] if c not in cur]:
            del state["ma"][c]
        for t in tcs:
            old = state["tc"].get(t)
            if not old or old.get("da_bo"):
                state["tc"][t] = dict(tao=today, sua=today, row_hash=row_h(t), ma=tcs[t]["ma"])
            else:
                state["tc"][t] = dict(tao=old["tao"], sua=today if old["row_hash"] != row_h(t) else old["sua"], row_hash=row_h(t), ma=tcs[t]["ma"])
        for t in tc_bo:
            state["tc"][t]["da_bo"] = today
        state["lich_su"].append(dict(ngay=today, doi=[x.strip() for x in a.doi.split(",") if x.strip()], noi_dung=a.mo_ta.strip(),
                                     dua_tren=dua_tren, ma_doi=ma_doi, ma_moi=ma_moi, tc_moi=tc_moi, tc_sua=tc_sua, tc_bo=tc_bo))
        state["nguon_chot"] = dua_tren
        st_p.write_text(json.dumps(state, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        # tính lại sau chốt
        ma_st = {c: "Không đổi" for c in cur}
        for c in tc_of:
            ma_st.setdefault(c, "Không đổi")
        tc_st = {t: "Còn đúng" for t in tcs}
        ma_doi, ma_moi, tc_bo = [], [], []

    # ---------- sinh truy-vet.md ----------
    out_dir = d
    link = lambda p, n: f"[{Path(p).name} dòng {n}]({rel(out_dir, ROOT / p)}#L{n})"
    cnt = {}
    for v in tc_st.values():
        k = v.split(" (")[0]
        cnt[k] = cnt.get(k, 0) + 1
    L = []
    L.append(f"# Truy vết — {cfg['ten_tinh_nang']}\n")
    L.append("*File này do `scripts/truy-vet.py` tự sinh, đừng sửa tay. Muốn đổi thì sửa nguồn rồi chạy lại script.*\n")
    L.append("| | |\n|---|---|")
    L.append(f"| Lần chạy gần nhất | {today} ({'chốt mốc mới' if a.lenh == 'chot' else 'chỉ kiểm, chưa đổi mốc'}) |")
    L.append(f"| Requirement | {cfg['srs']} (cập nhật {dua_tren['srs']}); bảng soát (cập nhật {dua_tren['bang_soat']}), câu trả lời đến {dua_tren['tl_cuoi']} |")
    L.append(f"| Checklist, test case | [checklist.md]({rel(out_dir, ROOT / cfg['checklist'])}), [test-case.md]({rel(out_dir, ROOT / cfg['test_case'])}) |")
    nc = state.get("nguon_chot") or {}
    L.append(f"| Mốc đã chốt | {state['lich_su'][-1]['ngay'] if state['lich_su'] else 'chưa chốt lần nào'}" +
             (f" (khi đó: SRS {nc.get('srs')}, bảng soát {nc.get('bang_soat')}, TL đến {nc.get('tl_cuoi')})" if nc else "") + " |\n")
    L.append("## 1. Tóm tắt")
    L.append(f"- Mã requirement: {len(srs_codes)} trong SRS, {len([c for c in cur if c.startswith('TL')])} câu trả lời (TL). Test case: {len(tcs)}.")
    L.append("- Trạng thái test case: " + (", ".join(f"{k} {v}" for k, v in sorted(cnt.items())) or "chưa có"))
    L.append(f"- Mã requirement đã đổi so với mốc đã chốt: {', '.join(ma_doi) or 'không có'}; mã mới: {', '.join(ma_moi) or 'không có'}.")
    L.append(f"- Mã SRS chưa có test case nào: {', '.join(chua_co_tc) or 'không có'}.")
    L.append(f"- Test case đã bỏ khỏi file: {', '.join(tc_bo) or 'không có'}.")
    L.append("- Vấn đề khác: " + ("; ".join(problems) if problems else "không có") + "\n")
    L.append("## 2. Khi requirement đổi, làm gì")
    L.append(f"1. Sửa SRS hoặc ghi câu trả lời mới của BA vào bảng soát (như mọi lần).")
    L.append(f"2. Chạy `python -X utf8 scripts/truy-vet.py kiem {a.du_an} {a.tinh_nang}`. Script liệt kê mã đã đổi và các test case chuyển sang **Cần xem lại**.")
    L.append("3. Mở từng test case đó (bảng 6 dưới đây), sửa checklist và test case cho khớp.")
    L.append(f"4. Chạy `python -X utf8 scripts/truy-vet.py chot {a.du_an} {a.tinh_nang} -m \"đã làm gì, vì sao\"`. Script ghi một dòng lịch sử và chốt mốc mới.")
    L.append("5. Muốn xem từng chữ đã đổi, dùng lịch sử git (commit sau mỗi lần chốt).\n")
    L.append("## 3. Bảng tra mã")
    L.append("Mã trong cột Nguồn của checklist và test case bỏ tiền tố `" + cfg["tien_to"] + "-`. `S01-AC02` là story 1, tình huống 2; `R` là quy tắc; `M` là thông báo; `TL` là câu trả lời của BA (TL-12, TL-13 là điều suy ra, người dùng xác nhận).\n")
    L.append("| Mã | Tên ngắn | Nguyên văn (rút gọn) | Mở ở đâu |\n|---|---|---|---|")
    for c in all_codes:
        if c not in cur:
            continue
        v = cur[c]
        where = link(cfg["bang_soat"], v["dong"]) if c.startswith("TL") else link(cfg["srs"], v["dong"])
        L.append(f"| {c} | {v['ten']} | {cut(v['nguyen_van'])} | {where} |")
    L.append("")
    L.append("## 4. Yêu cầu theo BA của từng mã SRS")
    L.append("Gom từ bảng soát (mục 5, 6) để mỗi mã SRS có chỗ ghi điều BA trả lời, kể cả khi SRS (bản quan sát hệ thống 1.3.0) ghi khác. "
             "Test case viết theo cột \"Theo BA\"; chỗ có ⚠️ là nghi lỗi của hệ thống, chưa phải lỗi đã xác nhận. "
             "SRS không bị sửa.\n")
    L.append("| Mã | Tên ngắn | Theo BA (hoặc suy ra) | Hệ thống 1.3.0 hiện tại | Còn mở |\n|---|---|---|---|---|")
    for c in srs_codes:
        o = ba.get(c, dict(ba=[], hien_tai=[], chua_chot=[], khac=False))
        if o["ba"]:
            tb = "<br>".join(
                ("Suy ra: " if e["suy_ra"] else "") + cut(e["text"], 320) +
                (" (" + ", ".join(e["refs"]) + ")" if e["refs"] else " (suy ra từ SRS)" if e["suy_ra"] else "") for e in o["ba"])
        else:
            tb = "Chưa có câu trả lời riêng của BA; theo SRS"
        if o["khac"]:
            ht = "⚠️ Khác. " + ("<br>".join(cut(x, 260) for x in o["hien_tai"]) if o["hien_tai"] else "Xem dòng theo BA ở cột bên cạnh")
        else:
            ht = "Không có điểm khác đã biết"
        L.append(f"| {c} | {cur[c]['ten']} | {tb} | {ht} | {', '.join(sorted(set(o['chua_chot']))) or '—'} |")
    L.append("")
    L.append("## 5. Từ requirement tới test case")
    L.append("| Mã | Tên ngắn | Trạng thái requirement | Test case |\n|---|---|---|---|")
    for c in all_codes:
        ts = tc_of.get(c, [])
        stt = ma_st.get(c) or ""
        if c in cur:
            tname = cur[c]["ten"]
        else:
            tname = cfg["ten_ngan"].get(c, "")
        if not ts:
            tshow = "⚠️ chưa có test case" if (not c.startswith("TL") and c in cur) else "—"
        else:
            tshow = f"{len(ts)}: " + ", ".join(ts)
        L.append(f"| {c} | {tname} | {stt} | {tshow} |")
    L.append("")
    L.append("## 6. Từ test case tới requirement")
    L.append("| Mã | Tình huống | Ưu tiên | Mã requirement dùng | Trạng thái | Tạo | Sửa lần cuối |\n|---|---|---|---|---|---|---|")
    for t in sorted(tcs):
        b = state["tc"].get(t, {})
        ms = ", ".join(f"{c} ({cur[c]['ten']})" if c in cur else c for c in tcs[t]["ma"]) or "—"
        L.append(f"| {t} | {cut(tcs[t]['tinh_huong'], 90)} | {ck.get(t, {}).get('uu_tien', '')} | {cut(ms, 400)} | {tc_st[t]} | {b.get('tao', '—') if not b.get('da_bo') else '—'} | {b.get('sua', '—') if not b.get('da_bo') else '—'} |")
    L.append("")
    L.append("## 7. Lịch sử thay đổi")
    L.append("Ghi mỗi lần chạy `chot`. Cột \"Dựa trên\" là phiên bản requirement lúc chốt.\n")
    L.append("| Ngày | Đối tượng | Nội dung | Dựa trên | Mã requirement đổi | Test case mới / sửa / bỏ |\n|---|---|---|---|---|---|")
    for e in state["lich_su"]:
        dt = e.get("dua_tren", {})
        L.append(f"| {e['ngay']} | {', '.join(e['doi'])} | {cut(e['noi_dung'], 300)} | SRS {dt.get('srs')}; bảng soát {dt.get('bang_soat')}; TL đến {dt.get('tl_cuoi')} | "
                 f"{', '.join(e.get('ma_doi', []) + [x + ' (mới)' for x in e.get('ma_moi', [])]) or '—'} | "
                 f"mới {len(e.get('tc_moi', []))}; sửa {', '.join(e.get('tc_sua', [])) or 0}; bỏ {', '.join(e.get('tc_bo', [])) or 0} |")
    if not state["lich_su"]:
        L.append("| (chưa có) | | | | | |")
    (d / "truy-vet.md").write_text("\n".join(L) + "\n", encoding="utf-8")

    # ---------- chèn khối lịch sử vào checklist / test case ----------
    for kind, key in (("checklist", "checklist"), ("test-case", "test_case")):
        p = ROOT / cfg[key]
        t = read(p)
        B = [START, "## Lịch sử thay đổi",
             f"Dựa trên: SRS cập nhật {dua_tren['srs']}; bảng soát cập nhật {dua_tren['bang_soat']}; câu trả lời của BA đến {dua_tren['tl_cuoi']}. "
             f"Trạng thái truy vết (chạy ngày {today}): " + (", ".join(f"{k} {v}" for k, v in sorted(cnt.items())) or "chưa có") +
             ". Chi tiết từng test case và bảng tra mã: [truy-vet.md](truy-vet.md).", "",
             "| Ngày | Nội dung | Test case mới / sửa / bỏ |", "|---|---|---|"]
        rows = [e for e in state["lich_su"] if kind in e["doi"] or "requirement" in e["doi"]]
        for e in rows:
            B.append(f"| {e['ngay']} | {cut(e['noi_dung'], 300)} | mới {len(e.get('tc_moi', []))}; sửa {', '.join(e.get('tc_sua', [])) or 0}; bỏ {', '.join(e.get('tc_bo', [])) or 0} |")
        if not rows:
            B.append("| (chưa có) | | |")
        B.append(END)
        blk = "\n".join(B)
        if START in t and END in t:
            t = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda m: blk, t, flags=re.S)
        else:
            t = t.rstrip("\n") + "\n\n" + blk + "\n"
        p.write_text(t, encoding="utf-8")

    # ---------- in ra console ----------
    print(f"[{a.lenh}] {a.du_an}/{a.tinh_nang}  ngày {today}")
    print("  Trạng thái test case:", ", ".join(f"{k} {v}" for k, v in sorted(cnt.items())))
    if ma_doi:
        print("  Mã requirement đã đổi:", ", ".join(f"{c} ({'; '.join(why(c)) or 'đã bỏ khỏi nguồn'})" for c in ma_doi))
        for t in sorted(tcs):
            if tc_st.get(t, "").startswith("Cần xem lại"):
                print("   -", t, "xem lại vì:", ", ".join(c for c in tcs[t]["ma"] if ma_st.get(c) in ("Đã đổi", "Đã bỏ khỏi nguồn")))
    if ma_moi:
        print("  Mã requirement mới:", ", ".join(ma_moi))
    if chua_co_tc:
        print("  Mã SRS chưa có test case:", ", ".join(chua_co_tc))
    if tc_bo:
        print("  Test case đã bỏ khỏi file:", ", ".join(tc_bo))
    for p in problems:
        print("  VẤN ĐỀ:", p)
    print("  Đã ghi:", (d / "truy-vet.md").relative_to(ROOT))
    bad = ma_doi or chua_co_tc or tc_bo or problems or any(v != "Còn đúng" for v in tc_st.values())
    sys.exit(1 if bad and a.lenh == "kiem" else 0)


if __name__ == "__main__":
    main()
