"""Banking Lite · Đăng nhập · TC-026: chưa đăng nhập, mở `/integrations` (và một địa chỉ không có thật) → form đăng nhập, giữ địa chỉ, không thông báo.

Không đăng nhập, không có mật khẩu.
"""
import login_common as lc

CASE_INFO = {
    "code": "TC-026",
    "title": "Chưa đăng nhập mở /integrations hoặc địa chỉ không có thật: form đăng nhập, giữ địa chỉ, không thông báo",
    "accounts": [],
}

MESSAGES = ("cần đăng nhập", "Vui lòng đăng nhập", "không tìm thấy", "Not found", "404")


def _check(ctx, path, step):
    page = ctx.page
    ctx.goto(path)
    form = lc.wait_form(ctx, page)
    body = ctx.page_text()
    found = [m for m in MESSAGES if m.lower() in body.lower()]
    ctx.check_main(f"{path}: hiện form Đăng nhập ({step})", form)
    ctx.check_main(f"{path}: thanh địa chỉ giữ nguyên ({step})", lc.path_of(page) == path, f"địa chỉ: {lc.path_of(page)}")
    ctx.check_main(f"{path}: không có thông báo `cần đăng nhập` hay trang `không tìm thấy` ({step})", not found,
                   "thấy: " + ", ".join(found) if found else "", mark_text=found,
                   error_note=f"Lỗi ở {step}: mở {path} khi chưa đăng nhập, trang hiện chữ `{found[0]}`, đáng ra chỉ hiện form đăng nhập." if found else "")


def run(ctx):
    _check(ctx, "/integrations", "bước 2")
    ctx.screenshot("integrations")
    _check(ctx, "/khong-ton-tai-xyz", "bước 2 (địa chỉ không có thật)")
