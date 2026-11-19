"""Banking Lite · Khuyến nghị LTV/DSR · TC-002 (smoke #3): lương 100 triệu → khuyến nghị Phê duyệt.

Chỉ nhập số, KHÔNG bấm Lưu (không đổi dữ liệu hồ sơ). Cần hồ sơ nháp `draft_application` trong auto-data.json.
"""
import reco_common as rc

CASE_INFO = {
    "code": "TC-002",
    "title": "Hiển thị khuyến nghị Phê duyệt khi nhập lương 100 triệu",
    "accounts": ["P100001"],
}


def run(ctx):
    rc.open_financials(ctx)
    rc.fill_field(ctx, "Lương hằng tháng", 100000000)
    panel = rc.stable_panel(ctx)
    ctx.screenshot("khung-tham-dinh")

    ctx.check_main("Khung Thẩm định đổi ngay khi nhập, không cần Lưu (bước 5)", rc.recommendation_label(panel) is not None)
    ctx.check_main("Nhãn `Phê duyệt`", rc.recommendation_label(panel) == "Phê duyệt", f"thấy: {rc.recommendation_label(panel)}")
    ctx.check_main("DSR `40,80%`", "40,80%" in panel)
    ctx.check_main("Thặng dư `54.700.000 VND`", "54.700.000 VND" in panel)
    ctx.check_main("Lý do `Đáp ứng mọi quy tắc tín dụng.`", "Đáp ứng mọi quy tắc tín dụng." in panel)
    ctx.check_minor("Dòng nhỏ `Xem trước: thẩm định chính thức chạy khi gửi, có dữ liệu CIC.`",
                 "Xem trước: thẩm định chính thức chạy khi gửi, có dữ liệu CIC." in panel)
    ctx.check_minor("Khoản trả mới `40.800.000 VND`", "40.800.000 VND" in panel)
    ctx.check_minor("Thu nhập được tính `100.000.000 VND`", "100.000.000 VND" in panel)
    ctx.check_minor("Chi phí được tính `4.500.000 VND`", "4.500.000 VND" in panel)
