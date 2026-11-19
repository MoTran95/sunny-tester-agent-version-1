"""Banking Lite · Đăng nhập · TC-021: sai 9 lần, đăng nhập đúng một lần, đăng xuất, rồi sai tiếp: không bị chặn (đăng nhập đúng đưa số lần sai về 0).

Bộ đếm trần 9 tính tổng số lần sai (đăng nhập đúng không đưa về 0), nên ca này (10 lần sai) cần người dùng đặt lại bộ đếm và đồng ý trước khi chạy. Mật khẩu đúng lấy từ `.env` trong thư viện.
"""
import login_common as lc

CASE_INFO = {
    "code": "TC-021",
    "title": "Sai 9 lần, đăng nhập đúng, sai tiếp: không bị chặn",
    "accounts": [],
    "ready_account": "P100001",
    "wrong_attempts": 10,
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
    page = ctx.page
    ctx.goto("/")
    lc.wait_form(ctx, page)
    statuses, generic, blocked = _nine_wrong(ctx, 3)
    ctx.precondition("gửi đủ 9 lần nhập sai trước khi đăng nhập đúng", len(statuses) == WRONG_ROUNDS and not any(blocked))
    ctx.check_main("Bước 3-11: 9 lần sai đều báo câu chung, chưa bị chặn", all(generic), f"mã máy chủ: {statuses}")

    status = ctx.submit_login("P100001", password_of="P100001", expect_success=True)         # bước 12-13
    ctx.check_main("Bước 13: đăng nhập đúng thành công (200) dù đã sai 9 lần", status == 200, f"mã trả về: {status}")
    lc.check_logged_in_as(ctx, "bước 13")
    lc.click_sign_out(page)                                                                     # bước 14
    ctx.check_main("Bước 14: về form `Đăng nhập`", lc.wait_form(ctx, page))

    status = ctx.submit_login("P100001", "Sai@Matkhau10", expect_success=False)              # bước 15-18
    ctx.precondition("lần sai sau khi đăng nhập đúng gửi được yêu cầu", status is not None)
    lc.wait_error_box(ctx)
    body = ctx.page_text()
    found = [m for m in lc.BLOCKED if m in body]
    ctx.screenshot("sau-lan-sai-tiep")
    ctx.check_main("Bước 18: khung lỗi ghi `Mã nhân viên hoặc mật khẩu không đúng.`", page.get_by_text(lc.GENERIC_VN, exact=True).count() > 0,
                   f"mã máy chủ: {status}")
    ctx.check_main("Bước 18: không bị chặn (không hiện `Đăng nhập sai quá nhiều lần. Thử lại sau 5 phút.`)", not found, mark_text=found,
                   error_note=f"Lỗi ở bước 18: sau 9 lần sai và một lần đăng nhập đúng, lần sai tiếp theo đã bị chặn (hiện `{found[0]}`)." if found else "")
