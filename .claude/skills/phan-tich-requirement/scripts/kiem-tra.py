#!/usr/bin/env python3
"""Soát đầu ra của skill phan-tich-requirement (bảng soát + file câu hỏi cho BA).

Cách chạy:
    python -X utf8 kiem-tra.py --nguon <requirement.md> --bang-soat <bang-soat.md> \
        [--cau-hoi <cau-hoi-cho-ba.md>] [--ma "<regex mã>"] [--tu-cam "tiến hành,nhằm"]

Kiểm:
  1. Mọi bảng Markdown: mỗi dòng có đúng số cột của dòng tiêu đề (bắt lỗi escape `|` sai).
  2. Cột cuối có tiêu đề chứa "Trích": mọi đoạn trong “…” phải có trong requirement, nguyên văn.
  3. --ma: mọi mã tìm thấy trong requirement phải có mặt trong bảng soát.
  4. File câu hỏi: mỗi khối `## A1.` có đủ trường (Hỏi, Mình đang hiểu; phần C: Cần xem/Cần làm, Mình đang hiểu).
  5. Bảng soát khớp file câu hỏi: câu hỏi nhúng trong bảng soát phải đúng chữ như ở file câu hỏi.
  6. Cảnh báo: từ dịch máy, mã nội bộ (CH-xx, KN-xx, Mxx, Rxx) lọt vào nội dung câu hỏi.
Thoát mã 1 nếu có lỗi; cảnh báo không làm thất bại.
"""
import argparse
import io
import re
import sys

SPLIT = re.compile(r"(?<!\\)\|")
SEP = re.compile(r"^\|\s*:?-{2,}")
DEFAULT_TU_CAM = ["tiến hành", "nhằm", "đối với", "dựa trên", "thực hiện việc", "kết quả mong đợi"]
INTERNAL_CODE = re.compile(r"\b(?:CH|KN)-\d\d\b|\bM\d\d\b|\bR\d\d\b")


def read(path):
    return io.open(path, encoding="utf-8").read()


def cells(line):
    parts = SPLIT.split(line.strip())
    return [c.strip().replace("\\|", "|") for c in parts[1:-1]]


def tables(text):
    lines = text.split("\n")
    out = []
    i = 0
    while i < len(lines):
        if lines[i].startswith("|") and i + 1 < len(lines) and SEP.match(lines[i + 1]):
            header = cells(lines[i])
            rows = []
            j = i + 2
            while j < len(lines) and lines[j].startswith("|"):
                rows.append((j + 1, cells(lines[j])))
                j += 1
            out.append((i + 1, header, rows))
            i = j
        else:
            i += 1
    return out


def clean(t):
    t = t.strip()
    t = re.sub(r"\n\s*\n- ", "; ", t)
    t = re.sub(r"\n- ", "; ", t)
    t = re.sub(r"\s*\n\s*", " ", t)
    return t


def parse_questions(text):
    """Trả về {id: {title, van, hieu, xem, hoi, raw}}."""
    out = {}
    for blk in re.split(r"\n(?=## [ABC]\d+\. )", text):
        m = re.match(r"## ([ABC]\d+)\. (.+)", blk)
        if not m:
            continue
        nid, title = m.group(1), m.group(2).strip()
        d = {"title": title, "raw": blk}
        if nid[0] in "AB":
            mm = re.search(r"\*\*Hỏi:\*\* (.*?)(?:\n\n|\Z)", blk, re.S)
            d["van"] = clean(mm.group(1)) if mm else ""
            mm = re.search(r"\*\*Mình đang hiểu:\*\*\s*(.*?)(?=\n\n\*\*|\n\n\*Mã cũ|\Z)", blk, re.S)
            d["hieu"] = clean(mm.group(1)) if mm else ""
        else:
            for key, lab in [("xem", "Cần xem|Cần làm"), ("hieu", "Mình đang hiểu"),
                             ("hoi", "Nếu [^:*]*?hỏi BA")]:
                mm = re.search(r"- \*\*(?:%s):\*\* (.*)" % lab, blk)
                d[key] = clean(mm.group(1)) if mm else ""
        out[nid] = d
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nguon", required=True)
    ap.add_argument("--bang-soat", required=True)
    ap.add_argument("--cau-hoi")
    ap.add_argument("--ma", help="regex của mã requirement cần phủ, ví dụ RECO-S\\d\\d-AC\\d\\d")
    ap.add_argument("--tu-cam", help="danh sách từ cảnh báo, cách nhau dấu phẩy (mặc định: từ dịch máy hay gặp)")
    a = ap.parse_args()

    errors, warns = [], []
    src = read(a.nguon)
    bs = read(a.bang_soat)
    ch_text = read(a.cau_hoi) if a.cau_hoi else None

    # 1. bảng
    for name, txt in [("bảng soát", bs)] + ([("câu hỏi", ch_text)] if ch_text else []):
        n_tab = 0
        for line_no, header, rows in tables(txt):
            n_tab += 1
            for ln, row in rows:
                if len(row) != len(header):
                    errors.append(f"[{name}] dòng {ln}: {len(row)} cột, tiêu đề có {len(header)} (kiểm dấu | trong ô)")
        print(f"- {name}: {n_tab} bảng")

    # 2. trích dẫn
    n_quote = 0
    for line_no, header, rows in tables(bs):
        if not header or "Trích" not in header[-1]:
            continue
        for ln, row in rows:
            cell = row[-1] if row else ""
            quotes = re.findall(r"“(.+?)”", cell)
            if not quotes and cell not in ("", "—"):
                warns.append(f"[bảng soát] dòng {ln}: cột trích không có đoạn nào trong “…”")
            for q in quotes:
                n_quote += 1
                if q not in src:
                    errors.append(f"[bảng soát] dòng {ln}: trích không khớp nguyên văn: “{q[:80]}…”")
    print(f"- trích dẫn đã so: {n_quote}")

    # 3. phủ mã
    if a.ma:
        codes = sorted(set(re.findall(a.ma, src)))
        missing = [c for c in codes if c not in bs]
        print(f"- mã trong requirement: {len(codes)}, thiếu trong bảng soát: {len(missing)}")
        for c in missing:
            errors.append(f"[phủ mã] chưa có trong bảng soát: {c}")

    # 4, 5, 6. câu hỏi
    if ch_text:
        qs = parse_questions(ch_text)
        groups = {"A": 0, "B": 0, "C": 0}
        for nid, d in qs.items():
            groups[nid[0]] += 1
            if nid[0] in "AB":
                if not d["van"]:
                    errors.append(f"[câu hỏi {nid}] thiếu trường **Hỏi:**")
                if not d["hieu"]:
                    errors.append(f"[câu hỏi {nid}] thiếu trường **Mình đang hiểu:**")
            else:
                if not d["xem"]:
                    errors.append(f"[câu hỏi {nid}] thiếu **Cần xem:** (hoặc **Cần làm:**)")
                if not d["hieu"]:
                    warns.append(f"[câu hỏi {nid}] chưa có **Mình đang hiểu:** (chấp nhận được nếu đây là việc mình tự làm, không cần đoán)")
        print(f"- câu hỏi: A {groups['A']}, B {groups['B']}, C {groups['C']}")

        # 5. khớp bảng soát
        seen = set()
        for line_no, header, rows in tables(bs):
            for ln, row in rows:
                for cell in row:
                    m = re.match(r"\*\*([ABC]\d+)\. ", cell)
                    if not m:
                        continue
                    nid = m.group(1)
                    seen.add(nid)
                    if nid not in qs:
                        errors.append(f"[bảng soát] dòng {ln}: câu {nid} không có trong file câu hỏi")
                        continue
                    d = qs[nid]
                    pairs = []
                    if nid[0] in "AB":
                        pairs = [("Hỏi", r"\*\*Hỏi:\*\* (.*?)(?:<br>|$)", d["van"]),
                                 ("Mình đang hiểu", r"\*\*Mình đang hiểu:\*\* (.*?)(?:<br>|$)", d["hieu"])]
                    else:
                        pairs = [("Cần xem", r"\*\*(?:Cần xem|Cần làm):\*\* (.*?)(?:<br>|$)", d["xem"]),
                                 ("Mình đang hiểu", r"\*\*Mình đang hiểu:\*\* (.*?)(?:<br>|$)", d["hieu"]),
                                 ("Hỏi BA", r"\*\*Nếu [^:*]*?hỏi BA:\*\* (.*?)(?:<br>|$)", d["hoi"])]
                    for label, pat, want in pairs:
                        mm = re.search(pat, cell)
                        got = mm.group(1).strip() if mm else ""
                        if want and got != want:
                            errors.append(f"[bảng soát] dòng {ln}: câu {nid}, trường '{label}' lệch file câu hỏi")
        print(f"- câu hỏi được nhúng trong bảng soát: {len(seen)}")

        # 6. cảnh báo giọng văn
        tu_cam = [t.strip() for t in a.tu_cam.split(",")] if a.tu_cam else DEFAULT_TU_CAM
        for nid, d in qs.items():
            body = " ".join(str(d.get(k, "")) for k in ("van", "hieu", "xem", "hoi"))
            raw_body = re.sub(r"\*Mã cũ:.*?\*", "", d["raw"])
            for t in tu_cam:
                if t and t in raw_body:
                    warns.append(f"[câu hỏi {nid}] có từ nghe dịch máy: '{t}'")
            if INTERNAL_CODE.search(body):
                warns.append(f"[câu hỏi {nid}] có mã nội bộ trong nội dung câu hỏi: {INTERNAL_CODE.search(body).group(0)}")

    print()
    for w in warns:
        print("CẢNH BÁO:", w)
    for e in errors:
        print("LỖI:", e)
    print(f"\nKết quả: {len(errors)} lỗi, {len(warns)} cảnh báo")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
