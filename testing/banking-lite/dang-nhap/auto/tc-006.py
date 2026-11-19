"""Banking Lite · Đăng nhập · TC-006: Mã có thật + sai mật khẩu → câu chung, không đăng nhập.

P100001, mật khẩu giả `Sai@Matkhau1`
"""
import login_common as lc

CASE_INFO = {
    "code": "TC-006",
    "title": "Mã có thật + sai mật khẩu: không đăng nhập, câu chung",
    "accounts": [],
    "ready_account": "P100001",
    "wrong_attempts": 1,
}


def run(ctx):
    lc.single_wrong_attempt(ctx, "P100001", "Sai@Matkhau1", step="bước 5")
