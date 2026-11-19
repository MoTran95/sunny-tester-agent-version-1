"""Hàm dùng chung cho script test case Khuyến nghị LTV/DSR (bước Tài chính của hồ sơ nháp).

Chưa kiểm trên hệ thống thật (cần phiên P100001 và hồ sơ nháp trong auto-data.json):
cách tìm khung `Thẩm định` dựa vào chữ của các dòng chỉ số, không dựa vào cấu trúc HTML.
Nếu lần chạy đầu báo 'Không kết luận' ở bước đọc khung, dùng scripts/inspect_page.py để xem cấu trúc thật.
"""
import re

RECOMMENDATION_LABELS = re.compile(r"Phê duyệt|Chuyển cấp trên|Từ chối")

# Tìm phần tử nhỏ nhất chứa cả hai dòng chỉ số, rồi leo lên tới phần tử đầu tiên có nhãn khuyến nghị,
# 'Lý do' hoặc thông báo 'Nhập đủ thông tin' (= gốc của khung Thẩm định, chưa lẫn ô Khuyến nghị đầu trang).
_JS_PANEL = """() => {
  const a = 'Khoản trả mới theo lãi suất thẩm định', b = 'Thặng dư hằng tháng';
  let best = null;
  for (const el of document.querySelectorAll('body *')) {
    const t = el.innerText || '';
    if (t.includes(a) && t.includes(b) && (!best || t.length < best.innerText.length)) best = el;
  }
  if (!best) return '';
  const marks = ['Phê duyệt', 'Chuyển cấp trên', 'Từ chối', 'Lý do', 'Nhập đủ thông tin'];
  let el = best;
  while (el && el.parentElement && el.tagName !== 'BODY') {
    const t = el.innerText || '';
    if (marks.some(m => t.includes(m))) return t;
    el = el.parentElement;
  }
  return (el && el.innerText) || '';
}"""


def open_financials(ctx, application_key="draft_application"):
    """Mở bước Tài chính của hồ sơ nháp (id lấy từ auto-data.json) và chờ khung Thẩm định hiện."""
    application_id = ctx.test_data(application_key)
    ctx.goto(f"/applications/{application_id}/financials")
    ctx.wait_text("Lương hằng tháng")
    panel = ctx.poll_until(lambda: read_panel(ctx), seconds=15)
    ctx.precondition("Đọc được khung `Thẩm định` ở bước Tài chính (xem scripts/inspect_page.py nếu trang đổi cấu trúc)", bool(panel))
    ctx.precondition("Hồ sơ nháp đúng khoản vay của test case (khoản trả mới 40.800.000 VND)", "40.800.000 VND" in panel)
    return panel


def read_panel(ctx):
    return ctx.page.evaluate(_JS_PANEL) or ""


def field_input(ctx, label):
    return ctx.page.get_by_label(re.compile(rf"^{re.escape(label)}")).first


def fill_field(ctx, label, value):
    field_input(ctx, label).fill(str(value))


def stable_panel(ctx, seconds=15):
    """Chờ khung Thẩm định có nhãn khuyến nghị và không đổi trong 1,5 giây (khung tính lại sau mỗi lần nhập)."""
    old, same_count = None, 0
    for _ in range(int(seconds * 2) + 1):
        new_text = read_panel(ctx)
        same_count = same_count + 1 if (new_text and new_text == old) else 0
        old = new_text
        if same_count >= 3 and RECOMMENDATION_LABELS.search(new_text):
            return new_text
        ctx.page.wait_for_timeout(500)
    return old or ""


def recommendation_label(panel):
    m = RECOMMENDATION_LABELS.search(panel)
    return m.group(0) if m else None


HEADER_LABEL_PATTERN = re.compile(r"Khuyến nghị[^\n]*\n?\s*(Phê duyệt|Chuyển cấp trên|Từ chối|—)")


def header_recommendation(ctx):
    """Nhãn Khuyến nghị ở đầu trang hồ sơ (bản đã lưu): Phê duyệt / Chuyển cấp trên / Từ chối / —; None nếu chưa thấy."""
    m = HEADER_LABEL_PATTERN.search(ctx.page_text())
    return m.group(1) if m else None


def save_and_wait(ctx):
    """Bấm Lưu và chờ thông báo `Đã lưu.`."""
    ctx.page.get_by_role("button", name=re.compile(r"^Lưu$")).first.click()
    ctx.wait_text("Đã lưu.")
