"""Banking Lite · Đăng nhập · TC-040: Mã 210 ký tự → câu chung, không còn `validation.too_big (employeeId)`.

"""
import login_common as lc

CASE_INFO = {
    "code": "TC-040",
    "title": "Mã 210 ký tự: câu chung, không câu kỹ thuật",
    "accounts": [],
    "ready_account": "P100001",
    "wrong_attempts": 1,
}


def run(ctx):
    lc.single_wrong_attempt(ctx, "P" + "1" * 209, "Sai@Matkhau1", step="bước 5")
