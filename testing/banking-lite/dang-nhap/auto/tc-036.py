"""Banking Lite · Đăng nhập · TC-036: bản English, sai mật khẩu → `Employee ID or password is incorrect.`
"""
import login_common as lc

CASE_INFO = {
    "code": "TC-036",
    "title": "Bản English sai mật khẩu: câu lỗi bằng English",
    "accounts": [],
    "ready_account": "P100001",
    "wrong_attempts": 1,
}


def run(ctx):
    lc.single_wrong_attempt(ctx, "P100001", "Sai@Matkhau1", step="bước 6", expected=lc.GENERIC_EN, language="English")
