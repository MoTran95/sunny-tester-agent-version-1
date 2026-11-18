#!/usr/bin/env python3
"""Tạo thư mục cho một dự án mới (hệ thống đang test) theo cấu trúc chung của repo.

Chạy từ gốc repo:
    python -X utf8 scripts/tao-du-an.py <slug> "<Tên dự án>" [<URL>]

Tạo:  memories/modules/<slug>/overview.md, srs/<slug>/, testing/<slug>/, evidence/<slug>/ (kèm .gitkeep),
      thêm dòng vào bảng "Các dự án" trong memories/project/overview.md, ghi slug vào .du-an-hien-tai.
Không ghi đè file đã có. Không đụng tới thư mục của dự án khác.
"""
import datetime
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    slug, ten = sys.argv[1].strip(), sys.argv[2].strip()
    url = sys.argv[3].strip() if len(sys.argv) > 3 else ""
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        print("LỖI: slug phải là kebab-case, chữ thường không dấu, ví dụ shop-online")
        return 2
    today = datetime.date.today().isoformat()
    env_prefix = slug.upper().replace("-", "_") + "_"

    for d in ("srs", "testing", "evidence"):
        p = os.path.join(ROOT, d, slug)
        os.makedirs(p, exist_ok=True)
        keep = os.path.join(p, ".gitkeep")
        if not os.listdir(p):
            io.open(keep, "w", encoding="utf-8").close()
        print("thư mục:", os.path.relpath(p, ROOT))

    mem_dir = os.path.join(ROOT, "memories", "modules", slug)
    os.makedirs(mem_dir, exist_ok=True)
    ov = os.path.join(mem_dir, "overview.md")
    if os.path.exists(ov):
        print("đã có, giữ nguyên:", os.path.relpath(ov, ROOT))
    else:
        io.open(ov, "w", encoding="utf-8", newline="\n").write(f"""# Dự án {ten} — tổng quan
Cập nhật: {today}

Slug dự án: `{slug}`. Chỉ đọc file này khi dự án hiện tại là {ten} (xem `memories/conventions/nhieu-du-an.md`).

## Hệ thống
- URL: {url or "_chưa có, hỏi người dùng_"}
- Tài khoản test: _chưa biết_ (mật khẩu trong `.env`, khóa bắt đầu bằng `{env_prefix}`).

## Bối cảnh
_Chưa có. Chỉ ghi điều người dùng nói hoặc đã thấy trên hệ thống này; không suy từ dự án khác._

## Thư mục của dự án
| Loại | Đường dẫn |
|---|---|
| Bộ nhớ | `memories/modules/{slug}/` |
| SRS | `srs/{slug}/` |
| Phân tích requirement | `testing/{slug}/` |
| Bằng chứng, báo cáo HTML | `evidence/{slug}/` |

## Việc cần làm tiếp
_Điền khi có._
""")
        print("tạo:", os.path.relpath(ov, ROOT))

    pov = os.path.join(ROOT, "memories", "project", "overview.md")
    text = io.open(pov, encoding="utf-8").read()
    if f"| `{slug}` |" not in text:
        row = f"| `{slug}` | {ten} | [../modules/{slug}/overview.md](../modules/{slug}/overview.md) |"
        lines = text.split("\n")
        idx = max(i for i, l in enumerate(lines) if l.startswith("| `"))
        lines.insert(idx + 1, row)
        io.open(pov, "w", encoding="utf-8", newline="\n").write("\n".join(lines))
        print("thêm dòng vào bảng dự án:", os.path.relpath(pov, ROOT))

    io.open(os.path.join(ROOT, ".du-an-hien-tai"), "w", encoding="utf-8", newline="\n").write(slug + "\n")
    print("dự án hiện tại trên máy này:", slug)
    print(f"\nViệc còn lại: thêm dòng cho dự án vào memories/MEMORY.md; người dùng tự thêm tài khoản vào .env với tiền tố {env_prefix}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
