"""Banking Lite · Đăng nhập · TC-033: đã đăng nhập, mở `/login` → Danh sách việc, địa chỉ vẫn là `/login`.

Dùng phiên đã lưu của P100001. Không làm mất phiên.
"""
import login_common as lc

CASE_INFO = {
    "code": "TC-033",
    "title": "Đã đăng nhập mở /login: hiện Danh sách việc, địa chỉ vẫn là /login",
    "accounts": ["P100001"],
}


def run(ctx):
    page = ctx.page
    ctx.goto("/login")                                      # bước 1
    ctx.wait_text("Danh sách việc")
    ctx.screenshot("mo-login")
    ctx.check_main("Bước 2: hiện Danh sách việc", "Danh sách việc" in ctx.page_text(), mark_text="Danh sách việc")
    ctx.check_main("Bước 2: không hiện form Đăng nhập", not lc.form_visible(page))
    ctx.check_main("Bước 2: thanh địa chỉ vẫn là `/login`", lc.path_of(page) == "/login", f"địa chỉ: {lc.path_of(page)}")
