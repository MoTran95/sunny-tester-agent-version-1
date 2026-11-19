"""Hàm dùng chung cho script ca Đăng nhập (Banking Lite)."""
import re
from urllib.parse import urlparse

SIGN_OUT = re.compile(r"^(Đăng xuất|Sign out)$")


def path_of(page):
    """Phần đường dẫn của địa chỉ hiện tại (không gồm tên miền)."""
    return urlparse(page.url).path


def form_visible(page):
    return page.locator("input[type=password]").count() > 0


def wait_form(ctx, page, seconds=12):
    """Chờ form đăng nhập hiện; trả True/False (không ném lỗi, để script tự kết luận)."""
    return bool(ctx.poll_until(lambda: form_visible(page), seconds=seconds))


def click_sign_out(page):
    page.get_by_role("button", name=SIGN_OUT).or_(page.get_by_role("link", name=SIGN_OUT)).first.click()


def click_language(page, name):
    """Bấm `English` hoặc `Tiếng Việt` trên thanh điều hướng."""
    page.get_by_role("button", name=name, exact=True).or_(page.get_by_role("link", name=name, exact=True)).first.click()


def has_label(page, pattern):
    return page.get_by_label(re.compile(pattern)).count() > 0


# --- nhập sai: kiểm khung lỗi ---
GENERIC_VN = "Mã nhân viên hoặc mật khẩu không đúng."
GENERIC_EN = "Employee ID or password is incorrect."
TECHNICAL = ("Một số giá trị không hợp lệ", "Some values are not valid", "validation.")
BLOCKED = ("Đăng nhập sai quá nhiều lần", "Too many failed attempts")
ERROR_KEYWORDS = ("không đúng", "không hợp lệ", "incorrect", "not valid", "quá nhiều", "too many", "validation")


def actual_error_line(body):
    """Dòng chữ giống khung lỗi nhất trên trang (để ghi vào ghi chú và tô đỏ); None nếu không thấy."""
    for line in body.splitlines():
        if any(k in line.lower() for k in ERROR_KEYWORDS):
            return line.strip()
    return None


def wait_error_box(ctx, seconds=8):
    ctx.poll_until(lambda: actual_error_line(ctx.page_text()) is not None, seconds=seconds)
    ctx.page.wait_for_timeout(300)


def check_error_box(ctx, step, expected=GENERIC_VN, check_form=True):
    """Kiểm khung lỗi sau một lần nhập sai: đúng câu chung, không câu/mã kỹ thuật, không cụm `Mã không gian`, vẫn ở form."""
    page = ctx.page
    wait_error_box(ctx)
    body = ctx.page_text()
    exact = page.get_by_text(expected, exact=True).count() > 0
    actual = actual_error_line(body)
    note = f"khung lỗi đang ghi: {actual}" if actual else "không thấy khung lỗi"
    ctx.check_main(f"{step}: khung lỗi đỏ ghi đúng câu `{expected}`", exact, note,
                   mark_text=expected if exact else actual,   # đúng: khung xanh quanh câu; sai: khung đỏ quanh câu đang hiện
                   error_note=f"Lỗi ở {step}: khung lỗi ghi `{actual}`, đáng ra phải ghi `{expected}`." if (actual and not exact) else "")
    technical = [t for t in TECHNICAL if t in body]
    ctx.check_main(f"{step}: không hiện câu hay mã kỹ thuật (`Một số giá trị không hợp lệ.`, `validation…`)", not technical,
                   "thấy: " + ", ".join(technical) if technical else "", mark_text=technical,
                   error_note=f"Lỗi ở {step}: trang hiện `{technical[0]}`, đáng ra chỉ có câu chung." if technical else "")
    ctx.check_main(f"{step}: câu lỗi không có cụm `Mã không gian`/`Workspace`", "không gian" not in body.lower() and "workspace" not in body.lower(),
                   mark_text=actual if ("không gian" in body.lower() or "workspace" in body.lower()) else None,
                   error_note=f"Lỗi ở {step}: câu lỗi còn nhắc mã không gian: `{actual}`." if ("không gian" in body.lower() or "workspace" in body.lower()) else "")
    if check_form:
        ctx.check_main(f"{step}: vẫn ở màn hình đăng nhập, thanh địa chỉ không đổi", form_visible(page) and path_of(page) == "/", f"địa chỉ: {path_of(page)}")
    return body


def single_wrong_attempt(ctx, username, password="", password_of=None, variant="as_is", step="bước 5", expected=GENERIC_VN, language=None):
    """Mở `/`, (tuỳ chọn bấm ngôn ngữ), gửi form sai đúng một lần, kiểm khung lỗi. Trả mã máy chủ."""
    page = ctx.page
    ctx.goto("/")
    wait_form(ctx, page)
    if language:
        click_language(page, language)
        page.wait_for_timeout(500)
    status = ctx.submit_login(username, password, expect_success=False, password_of=password_of, variant=variant)
    ctx.precondition("form gửi được yêu cầu đăng nhập (không bị trình duyệt chặn trước)", status is not None)
    ctx.screenshot("sau-nhap-sai")
    check_error_box(ctx, step, expected)
    return status


def check_logged_in_as(ctx, step, code="P100001"):
    """Sau khi gửi form đúng: vào Danh sách việc và thanh trên cùng hiện mã."""
    logged = ctx.poll_until(lambda: "Danh sách việc" in ctx.page_text() and not form_visible(ctx.page), seconds=15)
    ctx.screenshot("sau-dang-nhap")
    ctx.check_main(f"{step}: đăng nhập thành công, vào Danh sách việc", bool(logged), mark_text="Danh sách việc")
    if logged:
        header = ctx.page.locator("header")
        nav = header.first.inner_text() if header.count() else ctx.page_text()[:400]
        ctx.check_main(f"{step}: thanh trên cùng hiện `{code}`", code in nav, "thanh điều hướng: " + " | ".join(s.strip() for s in nav.splitlines() if s.strip()), mark_text=code)
