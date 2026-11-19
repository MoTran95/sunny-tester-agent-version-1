"""Banking Lite · Đăng nhập · TC-005 (smoke #1): form đăng nhập đủ ô, nút và phiên bản ở chân trang.

Không cần đăng nhập, không gửi yêu cầu đăng nhập, không có mật khẩu thật (chỉ gõ chữ giả `abc123`
vào ô Mật khẩu để xem chữ hiện dạng chấm, không bấm nút).
Phiên bản mong đợi lấy từ `auto-data.json` khóa `version` (mặc định 1.3.0); build mới đổi số thì sửa ở đó.
"""
import re

CASE_INFO = {
    "code": "TC-005",
    "title": "Form đăng nhập đủ ô nhập, nút và phiên bản ở chân trang",
    "accounts": [],
}


def run(ctx):
    version = ctx.cfg.test_data.get("version", "1.3.0")
    ctx.goto("/")
    ctx.wait_text("Đăng nhập")
    page = ctx.page
    page.get_by_label(re.compile(r"Mã nhân viên")).first.wait_for(state="visible", timeout=20000)
    # Số phiên bản ở chân trang hiện sau vài giây (lần đầu chụp sớm chỉ thấy "Phiên bản" trống):
    # chờ tối đa 15 giây cho tới khi có số; quá hạn mà vẫn không có số thì mới coi là sai.
    version_pattern = re.compile(r"Banking Lite\s*·\s*Phiên bản\s*(\d\S*)")
    for _ in range(30):
        body = ctx.page_text()
        if version_pattern.search(body):
            break
        page.wait_for_timeout(500)

    id_input = page.get_by_label(re.compile(r"^Mã nhân viên")).count() > 0
    password_input = page.get_by_label(re.compile(r"^Mật khẩu")).count() > 0
    button = page.get_by_role("button", name=re.compile(r"^Đăng nhập$")).count() > 0
    m = version_pattern.search(body)
    seen_version = m.group(1) if m else None

    ctx.check_main("Có ô `Mã nhân viên *` (bước 2)", id_input)
    ctx.check_main("Có ô `Mật khẩu *` (bước 2)", password_input)
    ctx.check_main("Có nút `Đăng nhập` (bước 4)", button)
    ctx.check_main(f"Chân trang ghi `Banking Lite · Phiên bản {version}` (bước 5)", seen_version == version,
                   f"thấy: {seen_version or 'không thấy dòng phiên bản'}")
    ctx.check_minor("Có dòng gợi ý `Chữ P và 6 chữ số, ví dụ P100001.` (bước 3)",
                 "Chữ P và 6 chữ số, ví dụ P100001." in body)

    # Bước 6-7: gõ chữ giả (không bấm nút), ô phải là kiểu mật khẩu (hiện chấm)
    o = page.locator("input[type=password]").first
    o.fill("abc123")
    input_type = o.get_attribute("type")
    ctx.check_minor("Chữ gõ trong ô Mật khẩu hiện dạng chấm (bước 7)", input_type == "password" and o.input_value() == "abc123",
                 f"kiểu ô: {input_type}")
    ctx.screenshot("form-dang-nhap")
