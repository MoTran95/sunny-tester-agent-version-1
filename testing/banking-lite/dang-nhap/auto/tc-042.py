"""Banking Lite · Đăng nhập · TC-042: đăng nhập, không thao tác khoảng 9 phút rồi tải lại trang: vẫn đăng nhập.

Đăng nhập bằng `ctx.sign_in("P100001")` (một phiên riêng của ca, script không thấy mật khẩu).
Không nhập sai mật khẩu nên không chạm bộ đếm. Ca chạy khoảng 9 phút 20 giây.
"""
import time

import login_common as lc

CASE_INFO = {
    "code": "TC-042",
    "title": "Đăng nhập, chờ 9 phút không thao tác, tải lại trang: vẫn đăng nhập",
    "accounts": [],
}

WAIT_SECONDS = 9 * 60


def run(ctx):
    page = ctx.page
    ctx.goto("/")
    ctx.precondition("mở trang thấy form Đăng nhập", lc.wait_form(ctx, page))
    ctx.sign_in("P100001")
    ctx.wait_text("Danh sách việc")                       # bước 1: vào tới Danh sách việc
    start = time.time()                                    # T0
    ctx.screenshot("luc-dang-nhap-xong")

    # Bước 2: không bấm, không gõ, không tải lại; chỉ chờ tới T0 + 9 phút.
    page.wait_for_timeout(max(0, int((start + WAIT_SECONDS - time.time()) * 1000)))

    page.reload(wait_until="domcontentloaded")             # bước 3: F5
    # Trang tải lại hay ở "Đang tải…" vài giây rồi mới biết còn đăng nhập hay không: chờ tới khi tải xong.
    settled = ctx.poll_until(lambda: lc.form_visible(page) or ("Danh sách việc" in ctx.page_text() and "Đang tải" not in ctx.page_text()), seconds=30)
    ctx.precondition("trang tải lại xong (hết chữ Đang tải…) trong 30 giây", settled)
    body = ctx.page_text()
    waited = int(time.time() - start)
    ctx.screenshot("sau-9-phut-tai-lai")
    ctx.check_main(f"Bước 4: sau {waited} giây vẫn ở Danh sách việc", "Danh sách việc" in body,
                   "trang hiện form Đăng nhập" if lc.form_visible(page) else "",
                   mark_text="Danh sách việc",
                   error_note="Lỗi ở bước 4 (nhìn trang sau khi tải lại): phiên đã hết hạn khi mới chờ 9 phút, đáng ra vẫn đăng nhập (thời hạn là 10 phút).")
    ctx.check_main("Bước 4: không hiện form Đăng nhập (không phải nhập lại)", not lc.form_visible(page))
