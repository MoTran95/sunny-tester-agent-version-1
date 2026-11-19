"""Banking Lite · Đăng nhập · TC-011: nhập sai rồi nhìn lại form: ô Mật khẩu phải trống, ô Mã nhân viên giữ chữ đã gõ.
"""
import login_common as lc

CASE_INFO = {
    "code": "TC-011",
    "title": "Sau khi báo lỗi: ô Mật khẩu trống, ô Mã nhân viên giữ chữ",
    "accounts": [],
    "ready_account": "P100001",
    "wrong_attempts": 1,
}


def run(ctx):
    page = ctx.page
    ctx.goto("/")
    lc.wait_form(ctx, page)
    status = ctx.submit_login("P100001", "Sai@Matkhau1", expect_success=False)
    ctx.precondition("form gửi được yêu cầu đăng nhập", status is not None)
    lc.wait_error_box(ctx)
    ctx.screenshot("sau-nhap-sai")
    body = ctx.page_text()
    ctx.check_main("Bước 5: hiện khung lỗi đỏ `Mã nhân viên hoặc mật khẩu không đúng.`", page.get_by_text(lc.GENERIC_VN, exact=True).count() > 0,
                   f"khung lỗi đang ghi: {lc.actual_error_line(body)}")
    id_value = page.get_by_label(lc.re.compile(r"^Mã nhân viên")).first.input_value()
    password_length = len(page.locator("input[type=password]").first.input_value())
    ctx.check_main("Bước 6: ô `Mã nhân viên *` còn nguyên `P100001`", id_value == "P100001", f"ô đang chứa {len(id_value)} ký tự")
    ctx.check_main("Bước 7: ô `Mật khẩu *` trống, không còn chấm hay ký tự nào", password_length == 0, f"ô Mật khẩu còn {password_length} ký tự",
                   error_note=f"Lỗi ở bước 7: sau khi báo lỗi, ô Mật khẩu vẫn còn {password_length} ký tự (chữ đã gõ không bị xóa)." if password_length else "")
