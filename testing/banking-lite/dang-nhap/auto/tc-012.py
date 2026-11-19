"""Banking Lite · Đăng nhập · TC-012: Mật khẩu đúng nhưng đổi hoa/thường một chữ cái → không đăng nhập, câu chung.

Mật khẩu lấy từ `.env` trong thư viện, script không thấy.
"""
import login_common as lc

CASE_INFO = {
    "code": "TC-012",
    "title": "Mật khẩu đổi hoa/thường một chữ: không đăng nhập, câu chung",
    "accounts": [],
    "ready_account": "P100001",
    "wrong_attempts": 1,
}


def run(ctx):
    lc.single_wrong_attempt(ctx, "P100001", password_of="P100001", variant="swap_letter_case", step="bước 5")
