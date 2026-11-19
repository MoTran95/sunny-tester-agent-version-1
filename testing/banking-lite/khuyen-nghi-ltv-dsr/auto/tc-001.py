"""Banking Lite · Khuyến nghị LTV/DSR · TC-001 (Tầng 1 regression): chưa nhập thu nhập → không có nhãn khuyến nghị, báo cần nhập đủ thông tin.

Chỉ đọc khung Thẩm định, KHÔNG nhập và KHÔNG bấm Lưu. Cần hồ sơ nháp `draft_application` trong auto-data.json (bước Tài chính còn trống).
"""
import reco_common as rc

CASE_INFO = {
    "code": "TC-001",
    "title": "Không hiển thị khuyến nghị mà báo cần nhập đủ thông tin khi chưa nhập thu nhập",
    "accounts": ["P100001"],
}

MESSAGE = "Nhập đủ thông tin người vay, khoản vay, tài sản và thu nhập để xem khuyến nghị."


def run(ctx):
    panel = rc.open_financials(ctx)
    panel = ctx.poll_until(lambda: (lambda p: p if MESSAGE in p else None)(rc.read_panel(ctx)), seconds=15) or panel
    ctx.screenshot("khung-tham-dinh")

    ctx.check_main("Khung `Thẩm định` không có nhãn khuyến nghị (bước 4)", rc.recommendation_label(panel) is None,
                   f"thấy nhãn: {rc.recommendation_label(panel)}")
    ctx.check_main("Khung `Thẩm định` không có mục `Lý do` (bước 4)", "Lý do" not in panel)
    ctx.check_main(f"Có thông báo `{MESSAGE}` (bước 4)", MESSAGE in panel, mark_text="Nhập đủ thông tin")
    ctx.check_main("LTV `80,00% (LTV tối đa 80,00%)` (bước 4)", "80,00% (LTV tối đa 80,00%)" in panel)
    ctx.check_main("Khoản trả mới `40.800.000 VND` (bước 4)", "40.800.000 VND" in panel)
    ctx.check_main("Thặng dư `-45.300.000 VND` (bước 4)", "-45.300.000 VND" in panel)
