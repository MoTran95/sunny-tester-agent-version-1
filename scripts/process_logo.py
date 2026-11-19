#!/usr/bin/env python3
"""Tạo bản logo nền trong suốt, nhỏ gọn, để nhúng vào trang kết quả (smoke-ket-qua.html).

    python -X utf8 scripts/process_logo.py            # đọc docs/thuong-hieu/logo-sunny-nhan-ra.png
    python -X utf8 scripts/process_logo.py --rong 420 # đổi chiều rộng (mặc định 420 px)

Nền trắng chuyển thành trong suốt (để đặt lên nền kem không bị hộp trắng), màu logo giữ nguyên.
Chạy một lần khi đổi logo, cần Pillow (`pip install Pillow`).
"""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "docs" / "thuong-hieu" / "logo-sunny-nhan-ra.png"
DEST = ROOT / "docs" / "thuong-hieu" / "logo-sunny-nhan-ra-nen-trong.png"


def process(src, dest, width=420):
    from PIL import Image, ImageChops

    im = Image.open(src).convert("RGB")
    im = im.resize((width, max(1, round(im.height * width / im.width))), Image.LANCZOS)
    r, g, b = im.split()
    darkest = ImageChops.darker(ImageChops.darker(r, g), b)  # kênh tối nhất mỗi điểm; 255 = trắng tinh
    alpha = darkest.point(lambda v: min(255, (255 - v) * 255 // 40))  # gần trắng → trong suốt, đủ đậm → giữ nguyên
    im.putalpha(alpha)
    dest.parent.mkdir(parents=True, exist_ok=True)
    im.save(dest, "PNG", optimize=True)
    return im.size


def main():
    ap = argparse.ArgumentParser(description="Tạo logo nền trong suốt cho trang kết quả")
    ap.add_argument("--width", type=int, default=420)
    args = ap.parse_args()
    if not SOURCE.exists():
        print(f"Chưa có logo gốc. Đặt file vào {SOURCE.relative_to(ROOT)} rồi chạy lại.")
        return 2
    size = process(SOURCE, DEST, args.width)
    print(f"Đã tạo {DEST.relative_to(ROOT)} {size[0]}x{size[1]}. Chạy `scripts/build_report.py build` để cập nhật trang.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
