"""Banking Lite · Đăng nhập · TC-034: đã đăng nhập, mở địa chỉ không có thật → Danh sách việc, giữ địa chỉ, không có trang "không tìm thấy".

Dùng phiên đã lưu của P100001. Không làm mất phiên.
"""
import login_common as lc

CASE_INFO = {
    "code": "TC-034",
    "title": "Đã đăng nhập mở địa chỉ không có thật: hiện Danh sách việc, không có trang không tìm thấy",
    "accounts": ["P100001"],
}

NOT_FOUND = ("không tìm thấy", "Not found", "404")


def run(ctx):
    page = ctx.page
    ctx.goto("/khong-ton-tai-xyz")                          # bước 1
    ctx.wait_text("Danh sách việc")
    ctx.screenshot("dia-chi-khong-co-that")
    body = ctx.page_text()
    found = [m for m in NOT_FOUND if m.lower() in body.lower()]
    ctx.check_main("Bước 2: hiện Danh sách việc", "Danh sách việc" in body, mark_text="Danh sách việc")
    ctx.check_main("Bước 2: thanh địa chỉ giữ nguyên `/khong-ton-tai-xyz`", lc.path_of(page) == "/khong-ton-tai-xyz", f"địa chỉ: {lc.path_of(page)}")
    ctx.check_main("Bước 2: không có trang `không tìm thấy`", not found, "thấy: " + ", ".join(found) if found else "", mark_text=found,
                   error_note=f"Lỗi ở bước 2: hiện chữ `{found[0]}`, đáng ra hiện Danh sách việc." if found else "")
