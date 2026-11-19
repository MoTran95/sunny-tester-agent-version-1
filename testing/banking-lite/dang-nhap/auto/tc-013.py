"""Banking Lite · Đăng nhập · TC-013: Mật khẩu đúng + 1 dấu cách ở cuối → không đăng nhập, câu chung.

Mật khẩu lấy từ `.env` trong thư viện, script không thấy.
"""
import login_common as lc

CASE_INFO = {
    "code": "TC-013",
    "title": "Mật khẩu thừa dấu cách cuối: không đăng nhập, câu chung",
    "accounts": [],
    "ready_account": "P100001",
    "wrong_attempts": 1,
}


def run(ctx):
    lc.single_wrong_attempt(ctx, "P100001", password_of="P100001", variant="trailing_space", step="bước 5")
