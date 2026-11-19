"""Banking Lite · Đăng nhập · TC-003: chưa đăng nhập mở link hồ sơ → form đăng nhập giữ link; đăng nhập đúng thì mở thẳng hồ sơ.

Bước nhập mã + mật khẩu + bấm Đăng nhập do `ctx.sign_in("P100001")` làm (đọc `.env`, một lần bấm).
Cần `application_hl_000019` trong auto-data.json.
"""
import login_common as lc

CASE_INFO = {
    "code": "TC-003",
    "title": "Chưa đăng nhập mở link hồ sơ: form giữ link, đăng nhập đúng mở thẳng hồ sơ",
    "accounts": [],
}


def run(ctx):
    application_path = "/applications/" + ctx.test_data("application_hl_000019")
    page = ctx.page
    ctx.goto(application_path)
    form = lc.wait_form(ctx, page)
    ctx.screenshot("link-ho-so-chua-dang-nhap")
    ctx.check_main("Bước 2: hiện form Đăng nhập", form)
    ctx.check_main("Bước 2: thanh địa chỉ vẫn là link hồ sơ", lc.path_of(page) == application_path, f"địa chỉ: {lc.path_of(page)}")

    ctx.sign_in("P100001")
    shown = ctx.poll_until(lambda: "HL-000019" in ctx.page_text(), seconds=15)
    ctx.screenshot("sau-dang-nhap")
    ctx.check_main("Bước 6: mở thẳng hồ sơ HL-000019", bool(shown), "không thấy mã HL-000019 sau khi đăng nhập" if not shown else "", mark_text="HL-000019")
    ctx.check_main("Bước 6: không về Danh sách việc (địa chỉ vẫn là link hồ sơ)", lc.path_of(page) == application_path,
                   f"địa chỉ: {lc.path_of(page)}")
