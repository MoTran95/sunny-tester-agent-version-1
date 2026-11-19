"""Banking Lite · Đăng nhập · TC-025: hai tab cùng trình duyệt, đăng xuất ở tab 2 → tab 1 khi thao tác cần tải dữ liệu thì về form, không báo gì.

Tự đăng nhập P100001 bằng `ctx.sign_in` ở tab 1; tab 2 là tab mới cùng một context (chung cookie đăng nhập).
"""
import login_common as lc

CASE_INFO = {
    "code": "TC-025",
    "title": "Hai tab: đăng xuất ở tab 2, tab 1 thao tác thì chuyển về form đăng nhập",
    "accounts": [],
}


def run(ctx):
    tab1 = ctx.page
    ctx.goto("/")
    lc.wait_form(ctx, tab1)
    ctx.sign_in("P100001")
    ctx.wait_text("Danh sách việc")

    tab2 = tab1.context.new_page()                          # bước 1
    tab2.goto(ctx.cfg.url + "/", wait_until="domcontentloaded")
    shown2 = ctx.poll_until(lambda: "Danh sách việc" in tab2.inner_text("body"), seconds=15)
    ctx.precondition("tab 2 vào thẳng Danh sách việc (dùng chung phiên)", shown2)

    lc.click_sign_out(tab2)                                 # bước 2
    ctx.check_main("Bước 2: tab 2 về form Đăng nhập", lc.wait_form(ctx, tab2))

    tab1.bring_to_front()                                   # bước 3-4
    ctx.check_minor("Bước 4: tab 1 chưa tự thay đổi, vẫn hiện Danh sách việc",
                    "Danh sách việc" in ctx.page_text() and not lc.form_visible(tab1))

    tab1.get_by_text("Tất cả hồ sơ", exact=True).first.click()   # bước 5
    form1 = lc.wait_form(ctx, tab1)
    body = ctx.page_text()
    ctx.screenshot("tab-1-sau-thao-tac")
    ctx.check_main("Bước 6: tab 1 chuyển sang form Đăng nhập", form1)
    ctx.check_main("Bước 6: không hiện thông báo nào (không có `Vui lòng đăng nhập.`)", "Vui lòng đăng nhập" not in body,
                   mark_text="Vui lòng đăng nhập", error_note="Lỗi ở bước 6: tab 1 hiện thông báo `Vui lòng đăng nhập.`, đáng ra không có thông báo.")
