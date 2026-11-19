"""Banking Lite · Đăng nhập · TC-009: Để trống ô Mật khẩu → câu chung, không còn `Một số giá trị không hợp lệ.` và `validation.too_small (password)`.

"""
import login_common as lc

CASE_INFO = {
    "code": "TC-009",
    "title": "Trống ô Mật khẩu: câu chung, không câu kỹ thuật",
    "accounts": [],
    "ready_account": "P100001",
    "wrong_attempts": 1,
}


def run(ctx):
    lc.single_wrong_attempt(ctx, "P100001", "", step="bước 5")
