"""Banking Lite · Đăng nhập · TC-029: mã có dấu cách ở cuối + mật khẩu đúng → đăng nhập được (tự cắt khoảng trắng).

Mật khẩu đúng lấy từ `.env` trong thư viện (script không thấy). Nếu hệ thống từ chối, đó là một lần sai được bộ đếm ghi lại.
"""
import login_common as lc

CASE_INFO = {
    "code": "TC-029",
    "title": "Mã thừa dấu cách ở cuối + mật khẩu đúng: đăng nhập được",
    "accounts": [],
    "ready_account": "P100001",
    "wrong_attempts": 1,
}


def run(ctx):
    page = ctx.page
    ctx.goto("/")
    lc.wait_form(ctx, page)
    status = ctx.submit_login('P100001 ', password_of="P100001", expect_success=True)       # bước 2-4 (dấu cách ở cuối)
    ctx.precondition("form gửi được yêu cầu đăng nhập", status is not None)
    ctx.check_main("Bước 4: máy chủ nhận đăng nhập (200)", status == 200, f"mã trả về: {status}")
    lc.check_logged_in_as(ctx, "bước 5")
