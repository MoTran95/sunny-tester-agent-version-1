"""Banking Lite · Đăng nhập · TC-032: đã đăng nhập, tải lại trang (F5) → vẫn đăng nhập, ở Danh sách việc.

Dùng phiên đã lưu của P100001 (`auto_login.py P100001 --headless`). Không làm mất phiên.
"""
import login_common as lc

CASE_INFO = {
    "code": "TC-032",
    "title": "Tải lại trang khi đã đăng nhập: vẫn đăng nhập, không phải nhập lại",
    "accounts": ["P100001"],
}


def run(ctx):
    page = ctx.page
    ctx.goto("/")
    ctx.wait_text("Danh sách việc")
    page.reload(wait_until="domcontentloaded")              # bước 1
    shown = ctx.poll_until(lambda: "Danh sách việc" in ctx.page_text() or lc.form_visible(page), seconds=15)
    ctx.screenshot("sau-tai-lai")
    ctx.check_main("Bước 2: vẫn ở Danh sách việc", "Danh sách việc" in ctx.page_text(), "" if shown else "trang không hiện gì sau 15 giây", mark_text="Danh sách việc")
    ctx.check_main("Bước 2: không hiện form Đăng nhập", not lc.form_visible(page))
