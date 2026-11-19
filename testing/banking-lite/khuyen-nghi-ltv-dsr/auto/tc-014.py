"""Banking Lite · Khuyến nghị LTV/DSR · TC-014 (Tầng 1 regression): LTV 81% → Từ chối kèm lý do LTV vượt mức.

CÓ BẤM LƯU HAI LẦN (lương, rồi số tiền vay) nên ca này DÙNG HẾT một hồ sơ nháp: cần hồ sơ MỚI mỗi lần chạy, điền vào
`draft_application_for_tc_014` trong auto-data.json (tạo bằng create_draft_application.py --keys draft_application_for_tc_014 --overwrite).
"""
import re

import reco_common as rc

CASE_INFO = {
    "code": "TC-014",
    "title": "Hiển thị Từ chối kèm lý do LTV vượt mức khi LTV là 81%",
    "accounts": ["P100001"],
}

KEY = "draft_application_for_tc_014"


def run(ctx):
    panel = rc.open_financials(ctx, KEY)
    ctx.precondition("Hồ sơ chưa nhập thu nhập (ô `Lương hằng tháng` còn trống); ca này dùng hết một hồ sơ nháp",
                     rc.field_input(ctx, "Lương hằng tháng").input_value() == "")

    rc.fill_field(ctx, "Lương hằng tháng", 100000000)
    rc.save_and_wait(ctx)
    ctx.poll_until(lambda: (lambda v: v if v and v != "—" else None)(rc.header_recommendation(ctx)), seconds=25)

    application_id = ctx.test_data(KEY)
    ctx.goto(f"/applications/{application_id}/loan")
    ctx.wait_text("Số tiền vay (VND)")
    ctx.page.get_by_label("Số tiền vay (VND)").fill("3240000000")
    rc.save_and_wait(ctx)
    # đầu trang cập nhật chậm vài giây: chờ tới khi LTV đầu trang là 81,00%
    ctx.poll_until(lambda: "81,00%" in ctx.page_text() or None, seconds=25)

    ctx.goto(f"/applications/{application_id}/financials")
    ctx.wait_text("Lương hằng tháng")
    panel = ctx.poll_until(lambda: (lambda p: p if "81,00%" in p and rc.recommendation_label(p) else None)(rc.read_panel(ctx)), seconds=25) or rc.read_panel(ctx)
    header = ctx.poll_until(lambda: (lambda v: v if v == "Từ chối" else None)(rc.header_recommendation(ctx)), seconds=25) or rc.header_recommendation(ctx)
    ctx.screenshot("sau-khi-luu")

    ctx.check_main("Đầu trang LTV `81,00%` (bước 8)", "81,00%" in ctx.page_text())
    ctx.check_main("Đầu trang Khuyến nghị `Từ chối` (bước 8)", header == "Từ chối", f"thấy: {header}", mark_text="Từ chối")
    ctx.check_main("Khung `Thẩm định` ghi `81,00% (LTV tối đa 80,00%)` (bước 8)", "81,00% (LTV tối đa 80,00%)" in panel, f"thấy khung: {panel[:200]}")
    ctx.check_main("Lý do `Từ chối: LTV 81% vượt mức tối đa 80%.` (bước 8)", "Từ chối: LTV 81% vượt mức tối đa 80%." in panel)
