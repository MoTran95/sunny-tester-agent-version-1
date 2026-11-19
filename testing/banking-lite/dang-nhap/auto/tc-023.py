"""Banking Lite · Đăng nhập · TC-023: đăng xuất khi đang đăng nhập → form đăng nhập, địa chỉ `/`, ngôn ngữ giữ nguyên (English).

Tự đăng nhập P100001 bằng `ctx.sign_in` trên trang riêng của ca (không dùng và không làm mất phiên đã lưu).
"""
import login_common as lc

CASE_INFO = {
    "code": "TC-023",
    "title": "Đăng xuất: về form đăng nhập, địa chỉ /, ngôn ngữ đã chọn giữ nguyên",
    "accounts": [],
}


def run(ctx):
    page = ctx.page
    ctx.goto("/")
    lc.wait_form(ctx, page)
    ctx.sign_in("P100001")
    ctx.wait_text("Danh sách việc")
    lc.click_language(page, "English")                      # bước 1
    ctx.wait_text("Sign out")
    lc.click_sign_out(page)                                 # bước 2
    form = lc.wait_form(ctx, page)
    ctx.screenshot("sau-dang-xuat")
    ctx.check_main("Bước 2: về form đăng nhập", form)
    ctx.check_main("Bước 3: thanh địa chỉ là `/`", lc.path_of(page) == "/", f"địa chỉ: {lc.path_of(page)}")
    ctx.check_main("Bước 3: form bằng English (`Employee ID`, `Password`, nút `Sign in`)",
                   lc.has_label(page, r"^Employee ID") and lc.has_label(page, r"^Password")
                   and page.get_by_role("button", name="Sign in", exact=True).count() > 0)
    ctx.check_minor("Bước 3: ngôn ngữ lưu vẫn là English (localStorage bl.locale)",
                    page.evaluate("() => localStorage.getItem('bl.locale')") == "en")
