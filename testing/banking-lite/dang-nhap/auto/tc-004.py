"""Banking Lite · Đăng nhập · TC-004: nhập sai một lần rồi sửa lại cho đúng và đăng nhập: vào Danh sách việc.

Mật khẩu đúng lấy từ `.env` trong thư viện (script không thấy).
"""
import login_common as lc

CASE_INFO = {
    "code": "TC-004",
    "title": "Nhập sai một lần rồi sửa lại cho đúng: vào Danh sách việc",
    "accounts": [],
    "ready_account": "P100001",
    "wrong_attempts": 1,
}


def run(ctx):
    page = ctx.page
    ctx.goto("/")
    lc.wait_form(ctx, page)
    status = ctx.submit_login("P100001", "Sai@Matkhau1", expect_success=False)          # bước 2-4
    ctx.precondition("form gửi được yêu cầu đăng nhập", status is not None)
    lc.check_error_box(ctx, "bước 4-5")
    ctx.screenshot("sau-nhap-sai")
    status = ctx.submit_login("P100001", password_of="P100001", expect_success=True)    # bước 6-8
    ctx.check_main("Bước 8: lần nhập đúng được máy chủ nhận (200)", status == 200, f"mã trả về: {status}")
    lc.check_logged_in_as(ctx, "bước 9")
