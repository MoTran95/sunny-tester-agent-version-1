#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Truy vết bộ smoke test (testing/<dự-án>/smoke-test.md) về test case gốc và requirement.

Dùng:
  python -X utf8 scripts/truy-vet-smoke.py kiem <dự-án>
      So test case gốc và requirement hiện tại với mốc smoke đã chốt. Báo smoke case nào "Cần xem lại"
      (requirement mà test case gốc dựa vào đã đổi), "Test case đã sửa", "Test case không còn".
      Ghi lại mục "Truy vết" trong smoke-test.md. Không đổi mốc. Thoát mã 1 nếu có việc cần làm.
  python -X utf8 scripts/truy-vet-smoke.py chot <dự-án> -m "đã làm gì" [--nguoi "Sunny Tran"]
      Chốt mốc mới: "bộ smoke hiện tại đã khớp test case và requirement hiện tại". Ghi một dòng
      "Lịch sử tạo và cập nhật". Chốt sau khi đã chốt truy vết của từng tính năng (scripts/truy-vet.py).

Ví dụ: python -X utf8 scripts/truy-vet-smoke.py kiem banking-lite

Nguồn sự thật: cột "Mã case gốc" của bảng 7 cột trong smoke-test.md. Mỗi ô phải có link dạng
[Tên module · TC-005](dang-nhap/test-case.md#tc-005); script đọc link để biết tính năng và test case.
Mỗi tính năng cần có truy-vet-cau-hinh.json (đã có khi làm truy vết tính năng). Mốc lưu ở
testing/<dự-án>/smoke-trang-thai.json do script tự tạo, không sửa tay. Cách tính "đổi" dùng lại hàm
của scripts/truy-vet.py nên đồng nhất với truy vết của từng tính năng.
"""
import argparse
import datetime
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("truy_vet", ROOT / "scripts" / "truy-vet.py")
tv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tv)

TV_START = "<!-- TRUY-VET:BAT-DAU (tự sinh bởi scripts/truy-vet-smoke.py, không sửa tay) -->"
TV_END = "<!-- TRUY-VET:KET-THUC -->"
LS_START = "<!-- LICH-SU:BAT-DAU (tự sinh bởi scripts/truy-vet-smoke.py, không sửa tay) -->"
LS_END = "<!-- LICH-SU:KET-THUC -->"
LINK = re.compile(r"\[([^\]]+)\]\(([^)#]+)#(tc-\d+)\)")
PHAN = ("Cố định", "Theo build")


def anchors(path):
    return set(re.findall(r'<a id="([^"]+)"></a>', tv.read(path)))


def load_feature(rel_dir, du_an_dir, cache):
    """Đọc requirement + test case của một tính năng (đồng nhất cách tính với truy-vet.py)."""
    if rel_dir in cache:
        return cache[rel_dir]
    d = du_an_dir / rel_dir
    cfg_p = d / "truy-vet-cau-hinh.json"
    if not cfg_p.exists():
        sys.exit(f"Chưa có {cfg_p}: tính năng này chưa làm truy vết")
    cfg = json.loads(tv.read(cfg_p))
    srs_t, bs_t = tv.read(ROOT / cfg["srs"]), tv.read(ROOT / cfg["bang_soat"])
    tc_t = tv.read(ROOT / cfg["test_case"])
    gop = not cfg.get("checklist")
    ck_t = tc_t if gop else tv.read(ROOT / cfg["checklist"])
    cur = tv.parse_srs(srs_t, cfg["tien_to"])
    ba = tv.parse_ba(bs_t, cfg["tien_to"])
    for k, v in cur.items():
        v["ba_hash"] = tv.h([x for e in ba.get(k, {}).get("ba", []) for x in (e["text"], e["stt"])])
    cur.update(tv.parse_tl(bs_t))
    for k, v in cur.items():
        v["ten"] = cfg["ten_ngan"].get(k) or tv.cut(v["nghia"] or v["nguyen_van"], 40)
    ck, tcs = tv.parse_tc(ck_t), tv.parse_tc(tc_t)
    f = dict(cfg=cfg, cur=cur, ck=ck, tcs=tcs, srs=ROOT / cfg["srs"], bs=ROOT / cfg["bang_soat"], tc=ROOT / cfg["test_case"],
             srs_ids=anchors(ROOT / cfg["srs"]), bs_ids=anchors(ROOT / cfg["bang_soat"]), tc_ids=anchors(ROOT / cfg["test_case"]))
    cache[rel_dir] = f
    return f


def row_hash(f, t):
    return tv.h([f["ck"].get(t, {}).get("row", ""), f["tcs"].get(t, {}).get("row", "")])


def parse_smoke(text, du_an_dir):
    """Đọc bảng 7 cột (tiêu đề bắt đầu '| # | Smoke case |') -> danh sách dòng."""
    rows, names, problems, tong = [], None, [], 0.0
    for line in text.splitlines():
        if names is None:
            if line.startswith("| # | Smoke case |"):
                names = tv.cells(line)
            continue
        if not re.match(r"^\| \d+ \|", line):
            if rows and not line.startswith("|"):
                break
            continue
        c = tv.cells(line)
        if len(c) != len(names):
            problems.append(f"Dòng {c[0]}: có {len(c)} ô, tiêu đề có {len(names)} cột")
            continue
        d = dict(zip(names, c))
        m = LINK.search(d["Mã case gốc"])
        if not m:
            problems.append(f"Dòng {d['#']}: cột Mã case gốc chưa có link dạng [Tên · TC-005](thư-mục/test-case.md#tc-005) (case mới thì ghi 'Case mới' và chưa truy vết được)")
            continue
        tc_path = (du_an_dir / m.group(2)).resolve()
        tm = re.search(r"([\d]+(?:[,.]\d+)?)\s*phút", d["Thời gian ước tính"])
        phut = float(tm.group(1).replace(",", ".")) if tm else None
        if phut is None:
            problems.append(f"Dòng {d['#']}: cột Thời gian ước tính chưa có số phút")
        else:
            tong += phut
        if d["Phần"] not in PHAN:
            problems.append(f"Dòng {d['#']}: cột Phần chỉ được ghi {PHAN}, hiện là '{d['Phần']}'")
        rows.append(dict(n=d["#"], ten=d["Smoke case"], rel_dir=str(tc_path.parent.relative_to(du_an_dir)).replace("\\", "/"), tc=m.group(3).upper(),
                         nhan=m.group(1), phan=d["Phần"], phut=phut, key=f"{tc_path.parent.relative_to(du_an_dir).as_posix()}/{m.group(3).upper()}"))
    if names is None:
        sys.exit("Không thấy bảng 7 cột (tiêu đề '| # | Smoke case |')")
    return rows, problems, tong


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("lenh", choices=["kiem", "chot"])
    ap.add_argument("du_an")
    ap.add_argument("-m", "--mo-ta", default="")
    ap.add_argument("--nguoi", default="Sunny Tran")
    ap.add_argument("--ngay", default=None, help="chỉ dùng khi thử: ép ngày, không ghi giờ")
    a = ap.parse_args()

    du_an_dir = ROOT / "testing" / a.du_an
    sm_p = du_an_dir / "smoke-test.md"
    st_p = du_an_dir / "smoke-trang-thai.json"
    text = tv.read(sm_p)
    rows, problems, tong = parse_smoke(text, du_an_dir)
    state = json.loads(tv.read(st_p)) if st_p.exists() else {"case": {}, "lich_su": []}
    cache = {}

    mx = re.search(r"Thời gian tối đa[^|]*\|\s*\*{0,2}(\d+(?:[,.]\d+)?)\s*phút", text)
    if mx and tong > float(mx.group(1).replace(",", ".")):
        problems.append(f"Tổng thời gian các case {tong:g} phút vượt mức tối đa {mx.group(1)} phút (chưa kể chuẩn bị chung)")
    keys = [r["key"] for r in rows]
    for k in {k for k in keys if keys.count(k) > 1}:
        problems.append(f"Test case {k} xuất hiện hai lần trong smoke")

    info = {}
    for r in rows:
        f = load_feature(r["rel_dir"], du_an_dir, cache)
        t = r["tc"]
        if t.lower() not in f["tc_ids"]:
            problems.append(f"Dòng {r['n']}: link tới #{t.lower()} nhưng test-case.md không có thẻ neo này")
        if t not in f["tcs"]:
            info[r["key"]] = dict(st="Test case không còn", doi=[], ma=[])
            continue
        ma = f["tcs"][t]["ma"]
        base = state["case"].get(r["key"])
        if base is None:
            info[r["key"]] = dict(st="Mới, chưa chốt", doi=[], ma=ma)
            continue
        doi = []
        for c in sorted(set(ma) | set(base["ma"])):
            cu, b = f["cur"].get(c), base["ma"].get(c)
            if cu is None or b is None:
                if cu is None and b is not None:
                    doi.append(f"{c} (đã bỏ khỏi nguồn)")
                elif b is None:
                    doi.append(f"{c} (mã mới ở test case)")
            elif cu["hash"] != b["hash"] or cu.get("ba_hash") != b.get("ba_hash"):
                doi.append(c)
        sua = base["row_hash"] != row_hash(f, t)
        st = "Cần xem lại" if doi else ("Test case đã sửa" if sua else "Còn đúng")
        if doi and sua:
            st = "Cần xem lại (test case cũng đã sửa)"
        info[r["key"]] = dict(st=st, doi=doi, ma=ma)
    bo = [k for k in state["case"] if k not in keys and not state["case"][k].get("da_bo")]

    now = None if a.ngay else datetime.datetime.now().astimezone()
    now_iso = now.isoformat(timespec="seconds") if now else None
    today = a.ngay or now.date().isoformat()

    if a.lenh == "chot":
        if not a.mo_ta.strip():
            sys.exit('Cần -m "đã làm gì" để ghi vào lịch sử.')
        if problems:
            print("Chưa chốt được, còn vấn đề:")
            for p in problems:
                print(" -", p)
            sys.exit(1)
        moi = [k for k in keys if k not in state["case"] or state["case"][k].get("da_bo")]
        doi_ds = [k for k in keys if info[k]["st"].startswith(("Cần xem lại", "Test case đã sửa"))]
        for r in rows:
            f = cache[r["rel_dir"]]
            old = state["case"].get(r["key"])
            ma_h = {c: dict(hash=f["cur"][c]["hash"], ba_hash=f["cur"][c].get("ba_hash")) for c in f["tcs"][r["tc"]]["ma"] if c in f["cur"]}
            state["case"][r["key"]] = dict(tao=old["tao"] if old and not old.get("da_bo") else today, sua=today if (not old or old.get("da_bo") or r["key"] in doi_ds) else old["sua"],
                                           row_hash=row_hash(f, r["tc"]), ma=ma_h)
        for k in bo:
            state["case"][k]["da_bo"] = today
        state["lich_su"].append(dict(ngay=today, thoi_diem=now_iso, commit_goc=tv.git("rev-parse", "--short", "HEAD") or None,
                                     chua_commit=bool(tv.git("status", "--porcelain")), nguoi=a.nguoi, noi_dung=a.mo_ta.strip(),
                                     loai="Tạo" if not state["lich_su"] else "Cập nhật", case_moi=moi, case_xem_lai=doi_ds, case_bo=bo,
                                     tong_phut=tong, so_case=len(rows)))
        st_p.write_text(json.dumps(state, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        for k in info:
            info[k] = dict(st="Còn đúng", doi=[], ma=info[k]["ma"])
        bo = []

    # ---- mục Truy vết ----
    def link_code(f, c, out_dir):
        v = f["cur"].get(c)
        ten = f" {v['ten']}" if v else ""
        low = f"{f['cfg']['tien_to'].lower()}-{c.lower()}"
        if c.startswith("TL-") and c.lower() in f["bs_ids"]:
            return f"[{c}]({tv.rel(out_dir, f['bs'])}#{c.lower()}){ten}"
        if low in f["srs_ids"]:
            return f"[{c}]({tv.rel(out_dir, f['srs'])}#{low}){ten}"
        return f"{c}{ten}"

    out_dir = du_an_dir
    T = ["| # | Smoke case | Test case gốc | Requirement mà test case dựa vào | Truy vết |", "|---|---|---|---|---|"]
    for r in rows:
        f = cache[r["rel_dir"]]
        i = info[r["key"]]
        codes = "<br>".join(link_code(f, c, out_dir) for c in i["ma"]) or "—"
        tcl = f"[{r['nhan']}]({r['rel_dir']}/test-case.md#{r['tc'].lower()})"
        st = i["st"] + (": đổi " + ", ".join(i["doi"]) if i["doi"] else "")
        T.append(f"| {r['n']} | {tv.cut(r['ten'], 90)} | {tcl} | {codes} | {st} |")
    for k in bo:
        T.append(f"| — | (đã bỏ khỏi smoke) | {k} | — | Đã bỏ khỏi smoke |")
    cnt = {}
    for i in info.values():
        k = i["st"].split(" (")[0]
        cnt[k] = cnt.get(k, 0) + 1
    last = state["lich_su"][-1] if state["lich_su"] else None
    tom = ", ".join(f"{k} {v}" for k, v in sorted(cnt.items()))
    tv_block = [TV_START, f"Lần kiểm gần nhất: {tv.fmt_dt(now_iso, today)} ({'chốt mốc mới' if a.lenh == 'chot' else 'chỉ kiểm, chưa đổi mốc'}). Mốc đã chốt: "
                f"{tv.fmt_dt(last.get('thoi_diem'), last['ngay']) if last else 'chưa chốt lần nào'}. Kết quả: {tom}.", ""] + T + [TV_END]

    # ---- mục Lịch sử ----
    H = ["| Thời điểm | Việc | Người | Nội dung | Số case · tổng phút (ước lượng) | Commit |", "|---|---|---|---|---|---|"]
    for e in reversed(state["lich_su"]):
        ghi = []
        if e.get("case_moi") and e["loai"] != "Tạo":
            ghi.append("thêm " + ", ".join(e["case_moi"]))
        if e.get("case_xem_lai"):
            ghi.append("xem lại/sửa " + ", ".join(e["case_xem_lai"]))
        if e.get("case_bo"):
            ghi.append("bỏ " + ", ".join(e["case_bo"]))
        nd = e["noi_dung"] + (f" ({'; '.join(ghi)})" if ghi else "")
        H.append(f"| {tv.fmt_dt(e.get('thoi_diem'), e['ngay'])} | {e['loai']} | {e.get('nguoi', '—')} | {nd} | {e['so_case']} case · {e['tong_phut']:g} phút | {tv.fmt_commit(e)} |")
    ls_block = [LS_START] + (H if state["lich_su"] else ["Chưa chốt lần nào."]) + [LS_END]

    new = text
    for s, e, blk in ((TV_START, TV_END, tv_block), (LS_START, LS_END, ls_block)):
        if s not in new or e not in new:
            sys.exit(f"smoke-test.md thiếu dấu {s[:20]}…{e}: thêm cặp dấu vào file rồi chạy lại")
        new = re.sub(re.escape(s) + r".*?" + re.escape(e), lambda m, b=blk: "\n".join(b), new, flags=re.S)
    if last:
        cap = f"| Cập nhật lần cuối | {tv.fmt_dt(last.get('thoi_diem'), last['ngay'])} ({last['loai'].lower()}: {last['noi_dung']}) |"
        if re.search(r"^\| Cập nhật lần cuối \|.*$", new, flags=re.M):
            new = re.sub(r"^\| Cập nhật lần cuối \|.*$", lambda m: cap, new, flags=re.M)
        else:
            new = re.sub(r"^(\| Ngày lập \|.*)$", lambda m: m.group(1) + "\n" + cap, new, count=1, flags=re.M)
    sm_p.write_text(new, encoding="utf-8")

    print(f"[{a.lenh}] {a.du_an}/smoke-test.md  {tv.fmt_dt(now_iso, today)}")
    print(f"  {len(rows)} smoke case, tổng {tong:g} phút (ước lượng, chưa kể chuẩn bị chung); trạng thái: {tom}")
    viec = [r for r in rows if info[r['key']]['st'] != "Còn đúng"]
    for r in viec:
        i = info[r["key"]]
        print(f"  - Dòng {r['n']} ({r['key']}): {i['st']}" + (f" — đổi {', '.join(i['doi'])}" if i["doi"] else ""))
    for k in bo:
        print(f"  - {k}: đã bỏ khỏi smoke")
    for p in problems:
        print("  ! ", p)
    if a.lenh == "kiem" and (viec or bo or problems):
        sys.exit(1)


if __name__ == "__main__":
    main()
