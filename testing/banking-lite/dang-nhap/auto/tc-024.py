"""Banking Lite · Đăng nhập · TC-024: đăng xuất ở trang hồ sơ rồi Back → chỉ hiện form, không hiện dữ liệu hồ sơ.

Tự đăng nhập P100001 bằng `ctx.sign_in` (không dùng phiên đã lưu). Cần `application_hl_000019` trong auto-data.json.
"""
import login_common as lc

CASE_INFO = {
    "code": "TC-024",
    "title": "Đăng xuất ở trang hồ sơ rồi bấm Back: chỉ hiện form đăng nhập, không lộ dữ liệu hồ sơ",
    "accounts": [],
}


def run(ctx):
    application_path = "/applications/" + ctx.test_data("application_hl_000019")
    page = ctx.page
    ctx.goto("/")
    lc.wait_form(ctx, page)
    ctx.sign_in("P100001")
    ctx.wait_text("Danh sách việc")
    ctx.goto(application_path)                              # bước 1
    shown = ctx.poll_until(lambda: "HL-000019" in ctx.page_text(), seconds=15)
    ctx.precondition("hồ sơ HL-000019 mở được khi đã đăng nhập", shown)
    ctx.check_main("Bước 2: hiện hồ sơ HL-000019", bool(shown))

    lc.click_sign_out(page)                                 # bước 3
    form = lc.wait_form(ctx, page)
    ctx.check_main("Bước 4: về form Đăng nhập", form)
    ctx.check_main("Bước 4: thanh địa chỉ là `/`", lc.path_of(page) == "/", f"địa chỉ: {lc.path_of(page)}")

    page.go_back()                                          # bước 5
    page.wait_for_timeout(2500)                             # cho trang vẽ lại sau Back
    ctx.screenshot("sau-back")
    body = ctx.page_text()
    ctx.check_main("Bước 6: thanh địa chỉ quay về link hồ sơ", lc.path_of(page) == application_path, f"địa chỉ: {lc.path_of(page)}")
    ctx.check_main("Bước 6: chỉ hiện form Đăng nhập", lc.form_visible(page))
    ctx.check_main("Bước 6: dữ liệu hồ sơ không hiện ra (không thấy HL-000019)", "HL-000019" not in body,
                   mark_text="HL-000019", error_note="Lỗi ở bước 6: sau khi đăng xuất bấm Back, trang vẫn hiện dữ liệu hồ sơ HL-000019.")
