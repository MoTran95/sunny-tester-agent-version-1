"""Banking Lite · Đăng nhập · TC-039: bấm English → vai trò `Banker`, số tiền kiểu English (dấu phẩy ngăn nghìn).

Đăng nhập bằng `ctx.sign_in("P100001")`. Số tiền hiện ở đâu còn CẦN XÁC NHẬN (câu 3 gửi BA): script quét
toàn trang, nên ý số tiền là ý phụ (chỉ ghi nhận), không làm Không đạt cả ca.
"""
import re

import login_common as lc

CASE_INFO = {
    "code": "TC-039",
    "title": "Bấm English: vai trò đổi thành Banker, số tiền hiện kiểu English",
    "accounts": [],
}

ENGLISH_AMOUNT = re.compile(r"\b\d{1,3}(?:,\d{3})+\b")
VIETNAMESE_AMOUNT = re.compile(r"\b\d{1,3}(?:\.\d{3})+\b")


def _nav_bar(ctx):
    header = ctx.page.locator("header")
    return header.first.inner_text() if header.count() else ctx.page_text()[:400]


def run(ctx):
    page = ctx.page
    ctx.goto("/")
    lc.wait_form(ctx, page)
    ctx.sign_in("P100001")                                  # bước 2-4
    ctx.wait_text("Danh sách việc")
    page.wait_for_timeout(1000)
    ctx.check_main("Bước 5: thanh điều hướng hiện vai trò `Chuyên viên khách hàng`", "Chuyên viên khách hàng" in _nav_bar(ctx))

    lc.click_language(page, "English")                      # bước 6
    ctx.wait_text("Sign out")
    page.wait_for_timeout(1500)
    nav = _nav_bar(ctx)
    body = ctx.page_text()
    ctx.screenshot("english")
    ctx.check_main("Bước 7: thanh điều hướng hiện vai trò `Banker`", "Banker" in nav,
                   "thanh điều hướng: " + " | ".join(s.strip() for s in nav.splitlines() if s.strip()))
    ctx.check_main("Bước 7: không còn `Chuyên viên khách hàng`", "Chuyên viên khách hàng" not in nav, mark_text="Chuyên viên khách hàng",
                   error_note="Lỗi ở bước 7: đã bấm English nhưng thanh điều hướng vẫn hiện `Chuyên viên khách hàng`.")
    english = ENGLISH_AMOUNT.findall(body)
    vietnamese = VIETNAMESE_AMOUNT.findall(body)
    ctx.precondition("trang có ít nhất một số tiền để đối chiếu (số tiền hiện ở đâu còn chờ BA, câu 3)", english or vietnamese)
    ctx.check_minor("Bước 8: số tiền hiện kiểu English (dấu phẩy ngăn hàng nghìn), không có kiểu dấu chấm",
                    bool(english) and not vietnamese, f"kiểu English: {english[:3]}; kiểu dấu chấm: {vietnamese[:3]}",
                    mark_text=vietnamese[:3], error_note="Lỗi ở bước 8: sau khi bấm English, số tiền này vẫn hiện kiểu dấu chấm." if vietnamese else "")
