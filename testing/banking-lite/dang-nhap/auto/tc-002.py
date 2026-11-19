"""Banking Lite · Đăng nhập · TC-002 (smoke #7): đăng nhập đúng P200001 và P300001, đúng vai trò.

Không có mật khẩu: dùng phiên đã lưu của hai tài khoản (`auto_login.py P200001 P300001 --headless`).
Bước 6 (Đăng xuất P200001) làm mất phiên P200001 ở máy chủ nên khai `invalidates_sessions`; xếp ca này CUỐI bộ.
Bước nhập mã + mật khẩu + bấm Đăng nhập (2-4, 7-9) do script đăng nhập làm, script này kiểm kết quả.
"""
import re

CASE_INFO = {
    "code": "TC-002",
    "title": "Đăng nhập đúng P200001 và P300001, đúng Danh sách việc và vai trò",
    "accounts": ["P200001", "P300001"],
    "invalidates_sessions": ["P200001"],
}


def _nav_bar(ctx, account):
    ctx.goto("/", account=account)
    ctx.wait_text("Danh sách việc", account=account)
    ctx.page_for(account).wait_for_timeout(1000)
    header = ctx.page_for(account).locator("header")
    return header.first.inner_text() if header.count() else ctx.page_text(account)[:400]


def run(ctx):
    # --- P200001 (bước 4, 5, 6) ---
    nav_text = _nav_bar(ctx, "P200001")
    ctx.screenshot("p200001-danh-sach-viec", account="P200001")
    ctx.check_main("P200001: vào Danh sách việc (bước 4)", "Danh sách việc" in ctx.page_text("P200001"))
    ctx.check_main("P200001: thanh điều hướng hiện mã P200001 (bước 5)", "P200001" in nav_text,
                   "thanh điều hướng: " + " | ".join(s.strip() for s in nav_text.splitlines() if s.strip()))
    ctx.check_main("P200001: thanh điều hướng hiện vai trò Chuyên viên định giá (bước 5)", "Chuyên viên định giá" in nav_text)

    ctx.page_for("P200001").get_by_role("button", name=re.compile(r"^Đăng xuất$")).or_(
        ctx.page_for("P200001").get_by_role("link", name=re.compile(r"^Đăng xuất$"))).first.click()
    back_to_form = ctx.poll_until(
        lambda: ctx.page_for("P200001").get_by_label(re.compile(r"^Mã nhân viên")).count() > 0, seconds=10, account="P200001")
    ctx.check_minor("P200001: bấm Đăng xuất về form Đăng nhập (bước 6)", bool(back_to_form))

    # --- P300001 (bước 9, 10) ---
    nav_text = _nav_bar(ctx, "P300001")
    ctx.screenshot("p300001-danh-sach-viec", account="P300001")
    ctx.check_main("P300001: vào Danh sách việc (bước 9)", "Danh sách việc" in ctx.page_text("P300001"))
    ctx.check_main("P300001: thanh điều hướng hiện mã P300001 (bước 10)", "P300001" in nav_text,
                   "thanh điều hướng: " + " | ".join(s.strip() for s in nav_text.splitlines() if s.strip()))
    ctx.check_main("P300001: thanh điều hướng hiện vai trò Chuyên viên thẩm định tín dụng (bước 10)",
                   "Chuyên viên thẩm định tín dụng" in nav_text)
