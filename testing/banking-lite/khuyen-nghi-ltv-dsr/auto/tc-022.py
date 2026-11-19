"""Banking Lite · Khuyến nghị LTV/DSR · TC-022 (smoke #6): nhập lương rồi Lưu → đầu trang cập nhật sau vài giây.

CÓ BẤM LƯU nên ca này DÙNG HẾT một hồ sơ nháp: cần hồ sơ MỚI mỗi lần chạy, điền vào `draft_application_for_tc_022`
trong auto-data.json. Chạy lần hai với hồ sơ cũ sẽ báo 'Không kết luận' (điều kiện trước không còn).
"""
import re

import reco_common as rc

CASE_INFO = {
    "code": "TC-022",
    "title": "Cập nhật khuyến nghị ở đầu trang sau vài giây khi nhập lương rồi bấm Lưu",
    "accounts": ["P100001"],
}

HEADER_LABEL_PATTERN = re.compile(r"Khuyến nghị[^\n]*\n?\s*(Phê duyệt|Chuyển cấp trên|Từ chối|—)")


def _header_recommendation(ctx):
    m = HEADER_LABEL_PATTERN.search(ctx.page_text())
    return m.group(1) if m else None


def run(ctx):
    panel = rc.open_financials(ctx, "draft_application_for_tc_022")
    ctx.precondition("Hồ sơ chưa nhập thu nhập (khung còn thông báo `Nhập đủ thông tin…`); ca này dùng hết một hồ sơ nháp",
                  "Nhập đủ thông tin" in panel)

    rc.fill_field(ctx, "Lương hằng tháng", 100000000)
    rc.fill_field(ctx, "Khoản trả nợ hiện có hằng tháng", 5000000)
    rc.fill_field(ctx, "Số người phụ thuộc", 5)
    ctx.page.get_by_role("button", name=re.compile(r"^Lưu$")).first.click()

    ctx.wait_text("Đã lưu.")
    ctx.check_main("Hiện thông báo `Đã lưu.` (bước 5)", True)

    # Bước 6: phản hồi chậm vài giây; chờ tối đa 25 giây cho tới khi đầu trang không còn `—`
    header_value = ctx.poll_until(lambda: (lambda v: v if v and v != "—" else None)(_header_recommendation(ctx)), seconds=25)
    ctx.check_main("Sau vài giây ô Khuyến nghị đầu trang thành `Phê duyệt` (bước 6)", header_value == "Phê duyệt",
                   f"thấy: {header_value or _header_recommendation(ctx)}")

    body = ctx.page_text()
    ctx.check_main("Bước `Tài chính` ghi `Đã xong` (bước 7)", re.search(r"Tài chính[\s\S]{0,60}Đã xong", body) is not None)

    # Bước 8: tải lại, ô Lương vẫn còn giá trị
    ctx.page.reload(wait_until="domcontentloaded")
    o = rc.field_input(ctx, "Lương hằng tháng")
    o.wait_for(state="visible", timeout=20000)
    ctx.page.wait_for_timeout(1000)
    ctx.check_main("Tải lại trang, ô `Lương hằng tháng` vẫn `100000000` (bước 8)", o.input_value() == "100000000",
                   f"thấy: {o.input_value()}")
    ctx.screenshot("sau-khi-luu")
