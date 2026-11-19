"""Banking Lite · Đăng nhập · TC-010: Để trống cả hai ô → câu chung, không câu kỹ thuật.

"""
import login_common as lc

CASE_INFO = {
    "code": "TC-010",
    "title": "Trống cả hai ô: câu chung",
    "accounts": [],
    "ready_account": "P100001",
    "wrong_attempts": 1,
}


def run(ctx):
    lc.single_wrong_attempt(ctx, "", "", step="bước 4")
