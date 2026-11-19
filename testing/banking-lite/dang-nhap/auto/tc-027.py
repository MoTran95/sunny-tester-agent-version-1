"""Banking Lite · Đăng nhập · TC-027: mã bằng chữ thường `p100001` + mật khẩu đúng → đăng nhập được, thanh trên hiện `P100001`.

Mật khẩu đúng lấy từ `.env` trong thư viện (script không thấy). Nếu hệ thống từ chối, đó là một lần sai được bộ đếm ghi lại.
"""
import login_common as lc

CASE_INFO = {
    "code": "TC-027",
    "title": "Mã chữ thường p100001 + mật khẩu đúng: đăng nhập được",
    "accounts": [],
    "ready_account": "P100001",
    "wrong_attempts": 1,
}


def run(ctx):
    page = ctx.page
    ctx.goto("/")
    lc.wait_form(ctx, page)
    status = ctx.submit_login('p100001', password_of="P100001", expect_success=True)       # bước 2-4 (chữ p thường)
    ctx.precondition("form gửi được yêu cầu đăng nhập", status is not None)
    ctx.check_main("Bước 4: máy chủ nhận đăng nhập (200)", status == 200, f"mã trả về: {status}")
    lc.check_logged_in_as(ctx, "bước 5")
