"""Banking Lite · Đăng nhập · TC-041: form đăng nhập không có ô chọn Workspace, quên mật khẩu, đăng ký, ghi nhớ đăng nhập.

Không đăng nhập, không có mật khẩu.
"""
import re

CASE_INFO = {
    "code": "TC-041",
    "title": "Form đăng nhập không có Workspace, quên mật khẩu, đăng ký, ghi nhớ đăng nhập",
    "accounts": [],
}

EXTRAS = ("Workspace", "Không gian", "Quên mật khẩu", "Đăng ký", "Ghi nhớ", "Nhớ đăng nhập")


def run(ctx):
    page = ctx.page
    ctx.goto("/")
    ctx.wait_text("Đăng nhập")
    page.get_by_label(re.compile(r"^Mã nhân viên")).first.wait_for(state="visible", timeout=20000)
    ctx.screenshot("form-dang-nhap")
    body = ctx.page_text()
    fields = page.locator("form input:visible, form select:visible, form textarea:visible").count() or page.locator("input:visible, select:visible").count()
    buttons = [b.strip() for b in page.locator("form button:visible").all_inner_texts()] or [b.strip() for b in page.locator("main button:visible").all_inner_texts()]
    ctx.check_main("Bước 2: form chỉ có 2 ô nhập (Mã nhân viên, Mật khẩu)", fields == 2, f"số ô nhập: {fields}")
    ctx.check_main("Bước 2: form có nút `Đăng nhập`", "Đăng nhập" in buttons, f"nút trong form: {buttons}")
    found = [t for t in EXTRAS if t.lower() in body.lower()]
    ctx.check_main("Bước 3: không có Workspace, quên mật khẩu, đăng ký, ghi nhớ đăng nhập", not found, "thấy: " + ", ".join(found) if found else "",
                   mark_text=found, error_note=f"Lỗi ở bước 3: form đăng nhập có `{found[0]}`, đáng ra không có." if found else "")
    ctx.check_main("Bước 3: không có ô tích chọn nào", page.locator("input[type=checkbox]").count() == 0)
