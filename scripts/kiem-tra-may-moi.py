#!/usr/bin/env python3
"""Kiểm máy mới đã sẵn sàng cho repo chưa, để phiên đầu tiên không mất thời gian dò lỗi.

Chạy từ gốc repo:
    python -X utf8 scripts/kiem-tra-may-moi.py

Không in giá trị nào trong .env (chỉ báo khóa nào còn trống). Không sửa file nào.
Thoát mã 1 nếu có mục THIẾU.
"""
import io
import json
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
thieu, canh_bao = [], []


def ok(msg):
    print("  OK     ", msg)


def miss(msg, cach_sua):
    thieu.append(msg)
    print("  THIẾU  ", msg, "\n          → " + cach_sua)


def warn(msg, cach_sua):
    canh_bao.append(msg)
    print("  LƯU Ý  ", msg, "\n          → " + cach_sua)


def run(args):
    try:
        r = subprocess.run(args, cwd=ROOT, capture_output=True, text=True, encoding="utf-8", timeout=60)
        return r.returncode, (r.stdout or "") + (r.stderr or "")
    except (OSError, subprocess.TimeoutExpired) as e:
        return 1, str(e)


def read_env(path):
    out = {}
    for line in io.open(path, encoding="utf-8"):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            out[k.strip()] = v.strip()
    return out


print("1. Python")
if sys.version_info >= (3, 8):
    ok(f"Python {sys.version.split()[0]}")
else:
    miss(f"Python {sys.version.split()[0]} quá cũ", "cài Python 3.10 trở lên từ python.org")
try:
    import PIL  # noqa: F401
    ok("Pillow (cần cho build báo cáo HTML)")
except ImportError:
    miss("chưa có Pillow (script build báo cáo HTML cần)", "chạy: python -m pip install pillow")
try:
    import fontTools  # noqa: F401
    import brotli  # noqa: F401
    ok("fonttools + brotli (cắt font nhúng vào báo cáo khám phá)")
except ImportError:
    warn("chưa có fonttools/brotli: báo cáo khám phá vẫn build được nhưng nhúng font nặng hơn", "chạy: python -m pip install fonttools brotli")

print("2. Git")
if shutil.which("git"):
    code, out = run(["git", "remote", "get-url", "origin"])
    ok("có remote origin") if code == 0 else warn("chưa có remote origin", "xem memories/project/git-remote.md")
    for key in ("user.name", "user.email"):
        code, out = run(["git", "config", key])
        ok(f"đã đặt git {key}") if code == 0 and out.strip() else warn(f"chưa đặt git {key}", f"git config --global {key} \"...\"")
else:
    miss("chưa cài Git", "cài Git for Windows từ git-scm.com")

print("3. Dự án hiện tại trên máy này (.du-an-hien-tai)")
slug = ""
cur = os.path.join(ROOT, ".du-an-hien-tai")
if os.path.exists(cur):
    slug = io.open(cur, encoding="utf-8").read().strip()
    if os.path.exists(os.path.join(ROOT, "memories", "modules", slug, "overview.md")):
        ok(f"dự án hiện tại: {slug}")
    else:
        miss(f"dự án '{slug}' chưa có memories/modules/{slug}/overview.md",
             f"tạo bằng: python -X utf8 scripts/tao-du-an.py {slug} \"<Tên dự án>\"")
else:
    warn("chưa chọn dự án trên máy này", "mở phiên Claude, Claude sẽ hỏi đang làm dự án nào (hoặc tạo dự án mới)")

print("4. Tài khoản test (.env) của dự án hiện tại")
env_path, mau_path = os.path.join(ROOT, ".env"), os.path.join(ROOT, ".env.example")
prefix = slug.upper().replace("-", "_") + "_" if slug else None
if not prefix:
    warn("bỏ qua vì chưa chọn dự án", "chọn dự án trước")
elif not os.path.exists(env_path):
    miss(".env chưa có", "chép .env.example thành .env rồi tự điền mật khẩu (không gửi qua chat)")
else:
    env = read_env(env_path)
    mau = {k: v for k, v in (read_env(mau_path) if os.path.exists(mau_path) else {}).items() if k.startswith(prefix)}
    co = [k for k in env if k.startswith(prefix)]
    thieu_khoa = [k for k in mau if k not in env]
    trong = [k for k in co if not env[k]]
    if not co:
        warn(f".env chưa có khóa nào bắt đầu bằng {prefix}", "người dùng tự thêm tài khoản test của dự án này")
    if thieu_khoa:
        miss(".env thiếu khóa: " + ", ".join(thieu_khoa), "thêm theo .env.example")
    if trong:
        warn(".env còn trống: " + ", ".join(trong), "tự điền giá trị")
    if co and not thieu_khoa and not trong:
        ok(f".env có {len(co)} khóa {prefix}… (không in giá trị)")

print("5. Cấu hình Claude trong repo")
for name in ("feature-exploration-report", "srs-from-website", "phan-tich-requirement", "tao-checklist-test-case", "tao-smoke-test", "tao-bug-report", "chay-test-tu-dong"):
    p = os.path.join(ROOT, ".claude", "skills", name, "SKILL.md")
    ok(f"skill {name}") if os.path.exists(p) else miss(f"thiếu skill {name}", "git pull lại repo")
sp = os.path.join(ROOT, ".claude", "settings.json")
try:
    n = len(json.load(io.open(sp, encoding="utf-8"))["permissions"]["allow"])
    ok(f".claude/settings.json hợp lệ, {n} quyền cho phép sẵn")
except (OSError, ValueError, KeyError) as e:
    miss(".claude/settings.json lỗi hoặc thiếu", f"git pull lại repo ({e})")

print("5b. Trang HTML luôn khớp file md (hook git, font)")
code, out = run(["git", "config", "--get", "core.hooksPath"])
ok("hook git pre-commit đã bật (.githooks)") if code == 0 and out.strip() == ".githooks" else miss(
    "chưa bật hook pre-commit sinh lại trang HTML", "git config core.hooksPath .githooks")
code, out = run([sys.executable, "-X", "utf8", "scripts/build_docs.py", "--all", "--check"])
last = [l for l in out.strip().splitlines() if l.strip()][-1:] or [""]
ok("trang HTML khớp file md và dữ liệu") if code == 0 else miss("có trang HTML cũ: " + last[0][:100], "python -X utf8 scripts/build_docs.py --all")
brand_file = os.path.join(ROOT, "docs", "thuong-hieu", "brand.json")
try:
    brand = json.load(io.open(brand_file, encoding="utf-8")) if os.path.exists(brand_file) else {}
except ValueError:
    brand = {}
logo_rel = brand.get("logo", "docs/thuong-hieu/logo-sunny-nhan-ra-nen-trong.png")
if brand.get("logo_enabled", True) is False:
    ok("logo tắt trong docs/thuong-hieu/brand.json")
elif os.path.exists(os.path.join(ROOT, logo_rel)):
    ok(f"logo thương hiệu: {logo_rel}")
else:
    warn(f"thiếu file logo {logo_rel} (trang vẫn sinh, không có logo)", "đặt file logo hoặc sửa docs/thuong-hieu/brand.json")
fonts_dir = os.path.join(ROOT, "docs", "thuong-hieu", "fonts")
if os.path.isdir(fonts_dir) and any(f.endswith(".woff2") for f in os.listdir(fonts_dir)):
    ok("font thương hiệu cục bộ (trang giống hệt khi không có mạng)")
else:
    warn("chưa có file font cục bộ: trang lấy font từ Google Fonts (cần mạng)", "xem docs/thuong-hieu/README.md")

print("6. Chạy thử script của skill")
checks = [
    ("check-srs.py trên SRS Đăng nhập",
     [sys.executable, "-X", "utf8", ".claude/skills/srs-from-website/scripts/check-srs.py", "srs/banking-lite/dang-nhap.md"]),
    ("kiem-tra.py trên bảng soát Đăng nhập",
     [sys.executable, "-X", "utf8", ".claude/skills/phan-tich-requirement/scripts/kiem-tra.py",
      "--nguon", "srs/banking-lite/dang-nhap.md",
      "--bang-soat", "testing/banking-lite/dang-nhap/bang-soat-requirement.md",
      "--cau-hoi", "testing/banking-lite/dang-nhap/cau-hoi-cho-ba.md"]),
]
for label, args in checks:
    code, out = run(args)
    last = [l for l in out.strip().splitlines() if l.strip()][-1:] or [""]
    ok(f"{label}: {last[0]}") if code == 0 else miss(f"{label} chạy lỗi: {last[0][:120]}", "xem lỗi ở trên, thường do thiếu Python/Pillow")

print()
print(f"Kết quả: {len(thieu)} mục THIẾU, {len(canh_bao)} mục LƯU Ý.")
print("Còn phải tự làm trong app (script không kiểm được): xem docs/cai-dat-may-moi.md mục 4.")
sys.exit(1 if thieu else 0)
