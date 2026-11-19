"""Banking Lite · Đăng nhập · TC-008: Để trống ô Mã nhân viên → câu chung.

"""
import login_common as lc

CASE_INFO = {
    "code": "TC-008",
    "title": "Trống ô Mã nhân viên: câu chung",
    "accounts": [],
    "ready_account": "P100001",
    "wrong_attempts": 1,
}


def run(ctx):
    lc.single_wrong_attempt(ctx, "", "Sai@Matkhau1", step="bước 5")
