#!/usr/bin/env python3
"""Banking Lite · chuẩn bị dữ liệu: tạo hồ sơ nháp đúng điều kiện trước của các ca Khuyến nghị LTV/DSR.

TẠO DỮ LIỆU THẬT trên hệ thống đang test (mỗi lần chạy tạo đúng `--count` hồ sơ nháp của P100001):
  người vay Tester Mot + tài sản CT 100019 (qua `Tạo từ hồ sơ có sẵn`), rồi đặt khoản vay:
  Mua nhà · sản phẩm 12 tháng cố định 6,00% · vay 3.200.000.000 · 20 năm · Gốc đều · giá trị khai báo 4.000.000.000
  (LTV 80%, khoản trả mới 40.800.000/tháng). Bước Tài chính để trống thu nhập.
Hồ sơ đầu ghi vào `draft_application`, hồ sơ thứ hai (nếu có) ghi vào `draft_application_for_tc_022` trong auto-data.json.
Không có mật khẩu: dùng phiên đã lưu của P100001 (`auto_login.py P100001 --headless`).

    python -X utf8 testing/banking-lite/auto/create_draft_application.py --count 2
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
sys.stdout.reconfigure(encoding="utf-8")

from test_automation import config, session  # noqa: E402
from test_automation.results import CaseResult  # noqa: E402
from test_automation.context import Context  # noqa: E402

CUSTOMER_QUERY = "Tester Mot"
COLLATERAL_QUERY = "CT 100019"
PRODUCT = "Vay mua nhà, cố định 6,00% trong 12 tháng"
REPAYMENT_METHOD = "Gốc đều (số tiền trả giảm dần)"
KEYS = ["draft_application", "draft_application_for_tc_022"]


def create_one(ctx):
    page = ctx.page
    ctx.goto("/")
    ctx.wait_text("Danh sách việc")
    page.get_by_role("button", name="Tạo từ hồ sơ có sẵn").click()
    for search_name, keyword in (("Tìm khách hàng có sẵn", CUSTOMER_QUERY), ("Tìm tài sản có sẵn", COLLATERAL_QUERY)):
        panel = page.get_by_role("search", name=search_name)
        panel.get_by_role("searchbox").fill(keyword)
        panel.get_by_role("button", name="Tìm").click()
        panel.get_by_role("button", name="Dùng").first.wait_for(state="visible", timeout=20000)
        panel.get_by_role("button", name="Dùng").first.click()
    create_button = page.get_by_role("button", name="Tạo hồ sơ", exact=True)
    create_button.wait_for(state="visible", timeout=10000)
    create_button.click()
    page.wait_for_url(re.compile(r"/applications/[0-9a-f-]{36}"), timeout=30000)
    application_id = re.search(r"/applications/([0-9a-f-]{36})", page.url).group(1)

    ctx.goto(f"/applications/{application_id}/loan")
    ctx.wait_text("Số tiền vay (VND)")
    page.get_by_label("Mục đích").select_option(label="Mua nhà")
    page.get_by_label("Sản phẩm").select_option(label=PRODUCT)
    page.get_by_label("Số tiền vay (VND)").fill("3200000000")
    page.get_by_label("Thời hạn (năm)").fill("20")
    page.get_by_label("Phương thức trả nợ").select_option(label=REPAYMENT_METHOD)
    page.get_by_label("Giá trị khai báo (VND)").fill("4000000000")
    page.get_by_role("button", name=re.compile(r"^Lưu$")).first.click()
    ctx.wait_text("Đã lưu.")
    ltv = ctx.poll_until(lambda: re.search(r"80,00%", ctx.page_text()) is not None, seconds=15)
    return application_id, bool(ltv)


def main():
    ap = argparse.ArgumentParser(description="Tạo hồ sơ nháp đúng điều kiện trước cho ca Khuyến nghị LTV/DSR")
    ap.add_argument("--count", type=int, default=2, choices=[1, 2])
    ap.add_argument("--overwrite", action="store_true", help="cho phép ghi đè id đang có trong auto-data.json")
    ap.add_argument("--tc-022-only", action="store_true",
                    help="chỉ tạo 1 hồ sơ mới cho draft_application_for_tc_022 (ca TC-022 dùng hết hồ sơ mỗi lần chạy), không đụng draft_application")
    args = ap.parse_args()
    needed_keys = KEYS[1:] if args.tc_022_only else KEYS[: args.count]

    cfg = config.load("banking-lite")
    data_file = cfg.project_dir / "auto-data.json"
    data = json.loads(data_file.read_text(encoding="utf-8"))
    already_set = [k for k in needed_keys if data.get(k)]
    if already_set and not args.overwrite:
        print(f"auto-data.json đã có {', '.join(already_set)}. Thêm --overwrite nếu muốn tạo hồ sơ mới thay thế.")
        return 2

    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = session.launch_browser(p, headless=True)
        if session.session_status(browser, cfg, "P100001") != "ok":
            print("Phiên P100001 chưa có hoặc hết hạn. Chạy: python -X utf8 scripts\\auto_login.py P100001 --headless")
            browser.close()
            return 3
        pairs = 0
        for key in needed_keys:
            ctx = Context(cfg, browser, {"accounts": ["P100001"]}, CaseResult(case_id="chuan-bi"), "chuan-bi")
            try:
                application_id, ltv_ok = create_one(ctx)
            except Exception as error:  # noqa: BLE001
                print(f"Tạo hồ sơ cho {key} không thành công: {type(error).__name__}: {(str(error).splitlines() or [''])[0]}")
                pairs = 1
                break
            finally:
                ctx.line()
            data[key] = application_id
            data_file.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(f"{key}: {application_id} (LTV 80,00% {'đúng' if ltv_ok else 'CHƯA THẤY, kiểm lại hồ sơ'})")
        browser.close()
    return pairs


if __name__ == "__main__":
    sys.exit(main())
