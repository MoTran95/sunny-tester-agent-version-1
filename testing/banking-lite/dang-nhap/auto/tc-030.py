"""Banking Lite · Đăng nhập · TC-030: Mã sai dạng `X999999` → câu chung, không có câu riêng `sai định dạng`. (Chỉ giá trị đầu; hai giá trị còn lại của checklist ghi nhận riêng.)

"""
import login_common as lc

CASE_INFO = {
    "code": "TC-030",
    "title": "Mã sai dạng X999999: câu chung, không câu sai định dạng",
    "accounts": [],
    "ready_account": "P100001",
    "wrong_attempts": 1,
}


def run(ctx):
    lc.single_wrong_attempt(ctx, "X999999", "Sai@Matkhau1", step="bước 5")
