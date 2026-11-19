"""Banking Lite · Khuyến nghị LTV/DSR · TC-023 (smoke #4): lương 75 triệu → DSR 54,40%, Chuyển cấp trên.

Chỉ nhập số, KHÔNG bấm Lưu. Cần hồ sơ nháp `draft_application` trong auto-data.json.
"""
import reco_common as rc

CASE_INFO = {
    "code": "TC-023",
    "title": "Hiển thị Chuyển cấp trên khi DSR 54,40% (lương 75 triệu)",
    "accounts": ["P100001"],
}


def run(ctx):
    rc.open_financials(ctx)
    rc.fill_field(ctx, "Lương hằng tháng", 75000000)
    panel = rc.stable_panel(ctx)
    ctx.screenshot("khung-tham-dinh")

    ctx.check_main("DSR `54,40%` (bước 5)", "54,40%" in panel)
    ctx.check_main("Nhãn `Chuyển cấp trên` (bước 5)", rc.recommendation_label(panel) == "Chuyển cấp trên",
                   f"thấy: {rc.recommendation_label(panel)}")
