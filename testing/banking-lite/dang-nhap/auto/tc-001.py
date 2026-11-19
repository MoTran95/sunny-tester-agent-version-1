"""Banking Lite · Đăng nhập · TC-001 (smoke #2): đăng nhập đúng P100001 vào Danh sách việc.

Script KHÔNG chứa và KHÔNG đọc mật khẩu. Bước 2-4 (nhập mã + mật khẩu + bấm Đăng nhập) do
`scripts/auto_login.py P100001 --headless` làm trước và lưu phiên; script này dùng lại phiên đó
rồi kiểm phần KẾT QUẢ (bước 4-5).

Chạy: python -X utf8 scripts/run_tests.py --case-id dang-nhap/tc-001
"""
import re

CASE_INFO = {
    "code": "TC-001",
    "title": "Đăng nhập đúng P100001 vào Danh sách việc",
    "accounts": ["P100001"],
}

ACCOUNT_ID = "P100001"
ROLE_NAME = "Chuyên viên khách hàng"


def run(ctx):
    ctx.goto("/")
    ctx.wait_text("Danh sách việc")
    page = ctx.page
    page.wait_for_timeout(1000)

    header = page.locator("header")
    nav_bar = header.first.inner_text() if header.count() else ctx.page_text()[:400]
    body = ctx.page_text()
    ctx.screenshot("danh-sach-viec")

    ctx.check_main("Vào Danh sách việc (bước 4)", "Danh sách việc" in body)
    ctx.check_main(f"Thanh điều hướng hiện mã {ACCOUNT_ID} (bước 5)", ACCOUNT_ID in nav_bar, f"thanh điều hướng: {' | '.join(s.strip() for s in nav_bar.splitlines() if s.strip())}")
    ctx.check_main(f"Thanh điều hướng hiện vai trò {ROLE_NAME} (bước 5)", ROLE_NAME in nav_bar)
    ctx.check_minor("Không có chữ DEFAULT trên thanh điều hướng (bước 5, TL-07)", re.search(r"\bDEFAULT\b", nav_bar) is None, mark_text="DEFAULT",
                 error_note="Lỗi ở bước 5 (nhìn thanh điều hướng sau khi đăng nhập): thanh điều hướng hiện chữ DEFAULT sau mã và vai trò, đáng ra không có chữ này.")
    ctx.check_minor("Không có thông báo đăng nhập thành công (bước 4)",
                 re.search(r"đăng nhập thành công|signed in successfully", body, re.I) is None)
