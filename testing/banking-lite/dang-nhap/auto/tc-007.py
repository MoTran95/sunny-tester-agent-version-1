"""Banking Lite · Đăng nhập · TC-007: Mã không tồn tại `P999999` → cùng câu chung như sai mật khẩu.

"""
import login_common as lc

CASE_INFO = {
    "code": "TC-007",
    "title": "Mã không tồn tại: cùng câu chung như sai mật khẩu",
    "accounts": [],
    "ready_account": "P100001",
    "wrong_attempts": 1,
}


def run(ctx):
    lc.single_wrong_attempt(ctx, "P999999", "Sai@Matkhau1", step="bước 5")
