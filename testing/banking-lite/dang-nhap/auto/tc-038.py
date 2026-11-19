"""Banking Lite · Đăng nhập · TC-038: chọn English, tải lại trang, đăng nhập rồi đăng xuất → vẫn English.

Đăng nhập bằng `ctx.sign_in("P100001")` (form đang bằng English, thư viện nhận cả nhãn `Employee ID` và nút `Sign in`).
"""
import login_common as lc

CASE_INFO = {
    "code": "TC-038",
    "title": "Chọn English, tải lại, đăng nhập rồi đăng xuất: vẫn đúng ngôn ngữ đã chọn",
    "accounts": [],
}


def _english_form(page):
    return (lc.has_label(page, r"^Employee ID") and lc.has_label(page, r"^Password")
            and page.get_by_role("button", name="Sign in", exact=True).count() > 0)


def run(ctx):
    page = ctx.page
    ctx.goto("/")                                           # bước 1
    lc.wait_form(ctx, page)
    lc.click_language(page, "English")                      # bước 2
    page.reload(wait_until="domcontentloaded")              # bước 3
    lc.wait_form(ctx, page)
    page.wait_for_timeout(800)
    ctx.screenshot("sau-tai-lai-english")
    ctx.check_main("Bước 4: form vẫn bằng English (`Employee ID *`, `Password *`, `Sign in`)", _english_form(page))

    ctx.sign_in("P100001")                                  # bước 5-7
    ctx.wait_text("Sign out")
    ctx.check_main("Bước 7: vào Danh sách việc (thanh điều hướng có `Sign out`)", page.get_by_text("Sign out").count() > 0)
    lc.click_sign_out(page)                                 # bước 8
    form = lc.wait_form(ctx, page)
    page.wait_for_timeout(800)
    ctx.screenshot("sau-dang-xuat-english")
    ctx.check_main("Bước 9: về form đăng nhập", form)
    ctx.check_main("Bước 9: form vẫn bằng English", _english_form(page))
