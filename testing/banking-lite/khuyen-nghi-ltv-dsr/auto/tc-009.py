"""Banking Lite · Khuyến nghị LTV/DSR · TC-009 (smoke #5): thặng dư thiếu 1 đồng (2.999.999) → Từ chối + lý do.

Chỉ nhập số, KHÔNG bấm Lưu. Cần hồ sơ nháp `draft_application` trong auto-data.json.
"""
import reco_common as rc

CASE_INFO = {
    "code": "TC-009",
    "title": "Hiển thị Từ chối kèm lý do khi thặng dư thiếu 1 đồng (2.999.999)",
    "accounts": ["P100001"],
}


def run(ctx):
    rc.open_financials(ctx)
    rc.fill_field(ctx, "Lương hằng tháng", 100000000)
    rc.fill_field(ctx, "Chi phí sinh hoạt hằng tháng", 56200001)
    panel = rc.stable_panel(ctx)
    ctx.screenshot("khung-tham-dinh")

    ctx.check_main("Thặng dư `2.999.999 VND` (bước 6)", "2.999.999 VND" in panel)
    ctx.check_main("Nhãn `Từ chối` (bước 6)", rc.recommendation_label(panel) == "Từ chối", f"thấy: {rc.recommendation_label(panel)}")
    ctx.check_main("Lý do `Từ chối: Thặng dư hằng tháng 2.999.999 VND thấp hơn 3.000.000 VND.`",
                   "Từ chối: Thặng dư hằng tháng 2.999.999 VND thấp hơn 3.000.000 VND." in panel)
