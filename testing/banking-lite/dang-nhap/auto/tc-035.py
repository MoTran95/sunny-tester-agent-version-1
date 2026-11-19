"""Banking Lite · Đăng nhập · TC-035: đang hiện khung lỗi, bấm English: nhãn đổi ngay, ô mã còn chữ, khung lỗi vẫn hiện bằng English.
"""
import login_common as lc

CASE_INFO = {
    "code": "TC-035",
    "title": "Đang có khung lỗi, đổi sang English giữa chừng: nhãn, ô mã và câu lỗi đổi đúng",
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
    ctx.check_main("Bước 5: khung lỗi đỏ ghi `Mã nhân viên hoặc mật khẩu không đúng.`", page.get_by_text(lc.GENERIC_VN, exact=True).count() > 0)
    lc.click_language(page, "English")                                                   # bước 6
    page.wait_for_timeout(1200)
    ctx.screenshot("sau-doi-english")
    body = ctx.page_text()
    actual = lc.actual_error_line(body)
    ctx.check_main("Bước 7: nhãn đổi ngay sang English (`Employee ID *`, `Password *`, nút `Sign in`)",
                   lc.has_label(page, r"^Employee ID") and lc.has_label(page, r"^Password") and page.get_by_role("button", name="Sign in", exact=True).count() > 0)
    ctx.check_main("Bước 7: ô Mã nhân viên còn `P100001`", page.get_by_label(lc.re.compile(r"^Employee ID")).first.input_value() == "P100001")
    english_ok = page.get_by_text(lc.GENERIC_EN, exact=True).count() > 0
    ctx.check_main("Bước 7: khung lỗi vẫn hiện, ghi `Employee ID or password is incorrect.`", english_ok, f"khung lỗi đang ghi: {actual or 'không thấy khung lỗi'}",
                   mark_text=actual if (actual and not english_ok) else None,
                   error_note=f"Lỗi ở bước 7: sau khi bấm English, khung lỗi ghi `{actual}`, đáng ra `{lc.GENERIC_EN}`." if (actual and not english_ok) else "")
    technical = [t for t in lc.TECHNICAL if t in body]
    ctx.check_main("Bước 7: không có dòng `validation…`", not technical, "thấy: " + ", ".join(technical) if technical else "", mark_text=technical,
                   error_note=f"Lỗi ở bước 7: trang hiện `{technical[0]}`." if technical else "")
