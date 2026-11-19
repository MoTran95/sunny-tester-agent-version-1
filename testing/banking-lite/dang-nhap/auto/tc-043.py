"""Banking Lite · Đăng nhập · TC-043: đăng nhập, không thao tác 10 phút 30 giây rồi tải lại trang: phiên hết hạn.

Màn hình lúc hết hạn (form hay có thông báo) BA chưa trả lời (B15), nên script chỉ kết luận ý "không còn đăng nhập"
và ghi lại màn hình thực tế vào ảnh và ghi chú, không coi màn hình nào là sai.
Không nhập sai mật khẩu nên không chạm bộ đếm. Ca chạy khoảng 10 phút 50 giây.
"""
import time

import login_common as lc

CASE_INFO = {
    "code": "TC-043",
    "title": "Đăng nhập, chờ 10 phút 30 giây không thao tác, tải lại trang: phiên hết hạn",
    "accounts": [],
}

WAIT_SECONDS = 10 * 60 + 30


def run(ctx):
    page = ctx.page
    ctx.goto("/")
    ctx.precondition("mở trang thấy form Đăng nhập", lc.wait_form(ctx, page))
    ctx.sign_in("P100001")
    ctx.wait_text("Danh sách việc")                       # bước 1
    start = time.time()                                    # T0
    ctx.screenshot("luc-dang-nhap-xong")

    page.wait_for_timeout(max(0, int((start + WAIT_SECONDS - time.time()) * 1000)))   # bước 2

    page.reload(wait_until="domcontentloaded")             # bước 3: F5
    # Trang tải lại hay ở "Đang tải…" vài giây rồi mới biết còn đăng nhập hay không (lần chạy đầu kết luận sai vì chụp lúc đó):
    # chờ tới khi tải xong rồi mới kết luận.
    settled = ctx.poll_until(lambda: lc.form_visible(page) or ("Danh sách việc" in ctx.page_text() and "Đang tải" not in ctx.page_text()), seconds=30)
    ctx.precondition("trang tải lại xong (hết chữ Đang tải…) trong 30 giây", settled)
    body = ctx.page_text()
    waited = int(time.time() - start)
    ctx.screenshot("sau-10-phut-30-giay-tai-lai")
    still_logged_in = "Danh sách việc" in body and not lc.form_visible(page)
    screen = "form Đăng nhập" if lc.form_visible(page) else "màn hình khác (không phải form)"
    ctx.check_main(f"Bước 4: sau {waited} giây không còn đăng nhập (màn hình thực tế: {screen})", not still_logged_in,
                   "vẫn ở Danh sách việc", mark_text="Danh sách việc" if still_logged_in else None,
                   error_note="Lỗi ở bước 4 (nhìn trang sau khi tải lại): đã chờ quá 10 phút nhưng vẫn đăng nhập, đáng ra phiên đã hết hạn.")
