#!/usr/bin/env python3
"""Đổi tài liệu markdown (SRS, bảng soát, câu hỏi BA, checklist, test case, truy vết, nhật ký khám phá) sang trang HTML dễ xem
và sinh trang tổng `testing/<dự-án>/index.html`. Không dùng AI: chỉ là chương trình đổi định dạng và đọc số liệu có sẵn.

    python -X utf8 scripts/build_docs.py                 # dự án trong .du-an-hien-tai
    python -X utf8 scripts/build_docs.py --project banking-lite
    python -X utf8 scripts/build_docs.py --check         # chỉ báo trang HTML nào cũ hơn file md (thoát mã 1 nếu có)

File md là bản gốc: sửa md rồi chạy lại. HTML nằm cạnh file md, đừng sửa tay.
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_automation import config, docs_pages  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description="Sinh trang HTML cho tài liệu md và trang tổng của dự án")
    ap.add_argument("--project")
    ap.add_argument("--check", action="store_true", help="chỉ kiểm trang HTML có cũ hơn md không")
    args = ap.parse_args()
    try:
        project = args.project or config.current_project()
        if args.check:
            old = docs_pages.stale(project)
            index = config.ROOT / "testing" / project / "index.html"
            if not index.exists():
                old.append(index)
            if old:
                print(f"{len(old)} trang HTML chưa có hoặc cũ hơn file md. Chạy: python -X utf8 scripts/build_docs.py")
                for f in old[:8]:
                    print("  -", f.relative_to(config.ROOT))
                return 1
            print("Mọi trang HTML tài liệu còn mới.")
            return 0
        done, skipped, index = docs_pages.build_all(project)
        print(f"Đã sinh {len(done)} trang HTML tài liệu và trang tổng: {index.relative_to(config.ROOT)}")
        for s in skipped:
            print(f"  (bỏ qua, có file HTML làm tay trùng tên: {s.relative_to(config.ROOT)})")
    except config.ConfigError as error:
        print(error)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
