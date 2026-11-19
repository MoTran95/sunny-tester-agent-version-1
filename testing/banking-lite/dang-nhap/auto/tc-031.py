"""Banking Lite · Đăng nhập · TC-031: nhấn Enter ở ô Mật khẩu rồi ở ô Mã nhân viên → form được gửi như bấm nút.

Mật khẩu đúng lấy từ `.env` trong thư viện (script không thấy).
"""
import login_common as lc

CASE_INFO = {
    "code": "TC-031",
    "title": "Nhấn Enter ở ô Mật khẩu và ở ô Mã nhân viên: form được gửi như bấm Đăng nhập",
    "accounts": [],
    "ready_account": "P100001",
    "wrong_attempts": 1,
}


def run(ctx):
    page = ctx.page
    ctx.goto("/")
    lc.wait_form(ctx, page)
    status = ctx.submit_login("P100001", password_of="P100001", expect_success=True, via="enter_in_password")   # bước 2-4
    ctx.precondition("Enter ở ô Mật khẩu gửi được yêu cầu đăng nhập", status is not None)
    lc.check_logged_in_as(ctx, "bước 5")
    lc.click_sign_out(page)                                                                                       # bước 6
    ctx.check_main("Bước 6: về form `Đăng nhập`", lc.wait_form(ctx, page))
    status = ctx.submit_login("P100001", password_of="P100001", expect_success=True, via="enter_in_id")           # bước 7-9
    ctx.precondition("Enter ở ô Mã nhân viên gửi được yêu cầu đăng nhập", status is not None)
    lc.check_logged_in_as(ctx, "bước 10")
