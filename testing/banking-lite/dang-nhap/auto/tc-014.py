"""Banking Lite · Đăng nhập · TC-014: sai liên tiếp 9 lần (cùng một tài khoản): lần thứ 9 vẫn báo câu chung, chưa bị chặn.

Bộ đếm trần 9 của thư viện: đăng nhập đúng không đưa bộ đếm về 0; ca chỉ chạy khi bộ đếm còn đủ 9 lần.
"""
import login_common as lc

CASE_INFO = {
    "code": "TC-014",
    "title": "Sai liên tiếp 9 lần: lần thứ 9 vẫn báo câu chung, chưa bị chặn",
    "accounts": [],
    "ready_account": "P100001",
    "wrong_attempts": 9,
}


WRONG_ROUNDS = 9


def _nine_wrong(ctx, first_step):
    """Cố ý nhập sai 9 lần liên tiếp (`Sai@Matkhau1`…`9`), mỗi lần kiểm khung lỗi; dừng sớm nếu bị chặn."""
    page = ctx.page
    statuses, generic, blocked = [], [], []
    for i in range(1, WRONG_ROUNDS + 1):
        status = ctx.submit_login("P100001", f"Sai@Matkhau{i}", expect_success=False)
        statuses.append(status)
        lc.wait_error_box(ctx)
        body = ctx.page_text()
        generic.append(page.get_by_text(lc.GENERIC_VN, exact=True).count() > 0)
        found = [m for m in lc.BLOCKED if m in body]
        blocked.append(found)
        if found or status in (None, 429):
            break
    ctx.screenshot("sau-lan-sai-thu-" + str(len(statuses)))
    return statuses, generic, blocked


def run(ctx):
    ctx.goto("/")
    lc.wait_form(ctx, ctx.page)
    statuses, generic, blocked = _nine_wrong(ctx, 3)
    done = len(statuses)
    ctx.precondition("gửi đủ 9 lần nhập sai (không bị dừng giữa chừng)", done == WRONG_ROUNDS or any(blocked))
    ctx.check_main("Bước 3-11: sau mỗi lần sai (1 đến 9), khung lỗi ghi `Mã nhân viên hoặc mật khẩu không đúng.`", all(generic),
                   f"mã máy chủ từng lần: {statuses}; lần có câu đúng: {[i + 1 for i, g in enumerate(generic) if g]}")
    last_blocked = blocked[-1] if blocked else []
    ctx.check_main("Bước 12: sau lần sai thứ 9 chưa bị chặn (không hiện `Đăng nhập sai quá nhiều lần. Thử lại sau 5 phút.`)", not any(blocked),
                   f"bị chặn ở lần thứ {done}" if any(blocked) else "", mark_text=last_blocked,
                   error_note=f"Lỗi ở bước {2 + done}: sau lần sai thứ {done}, hệ thống đã chặn (hiện `{last_blocked[0]}`), đáng ra chỉ chặn từ lần thứ 10." if last_blocked else "")
