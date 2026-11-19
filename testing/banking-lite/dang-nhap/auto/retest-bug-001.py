"""Banking Lite · Re-test BUG-001: thanh điều hướng không còn chữ `DEFAULT` sau mã và vai trò.

Kế hoạch: testing/banking-lite/dang-nhap/retest/BUG-001-ke-hoach-retest.md
- Ý chính (điều kiện đóng bug): đủ 3 tài khoản trong Phạm vi ảnh hưởng, bước 1-5 của TC-001.
- Ý phụ (biến thể, không tính vào điều kiện đóng): `/api/me` không còn `workspace`; bấm English; tải lại trang (F5).
  Biến thể "mở một màn hình khác" chưa làm vì chưa có đường dẫn đã biết (làm tay hoặc bổ sung sau).

Không có mật khẩu: dùng phiên đã lưu (`auto_login.py P100001 P200001 P300001 --headless`, chạy NGAY trước, phiên ~10 phút).
Chạy: python -X utf8 scripts/run_tests.py --case-id dang-nhap/retest-bug-001
(Tên không bắt đầu bằng `tc-` nên `--feature dang-nhap` không chạy kèm ca này.)
"""
import re

CASE_INFO = {
    "code": "RT-BUG-001",
    "title": "Re-test BUG-001: không còn chữ DEFAULT trên thanh điều hướng (P100001, P200001, P300001)",
    "accounts": ["P100001", "P200001", "P300001"],
}

ACCOUNTS = [
    ("P100001", "Chuyên viên khách hàng", "Banker"),
    ("P200001", "Chuyên viên định giá", None),
    ("P300001", "Chuyên viên thẩm định tín dụng", None),
]
DEFAULT_RE = re.compile(r"\bDEFAULT\b")
ERROR_NOTE = ("Lỗi ở bước 5 (nhìn thanh điều hướng sau khi đăng nhập): thanh điều hướng vẫn hiện chữ DEFAULT "
              "sau mã và vai trò, đáng ra không có chữ này.")


def _nav(ctx, account):
    page = ctx.page_for(account)
    header = page.locator("header")
    return header.first.inner_text() if header.count() else ctx.page_text(account)[:400]


def _line(nav_text):
    return "thanh điều hướng: " + " | ".join(s.strip() for s in nav_text.splitlines() if s.strip())


def _variant(ctx, title, fn):
    """Biến thể không được làm hỏng kết luận ý chính: lỗi script ở biến thể thì ghi 'chưa kiểm được', không im lặng."""
    try:
        fn()
    except Exception as error:  # noqa: BLE001
        first_line = (str(error).splitlines() or [""])[0]
        ctx.check_minor(title, False, f"Chưa kiểm được biến thể này (lỗi script {type(error).__name__}: {first_line}); làm tay")


def run(ctx):
    # --- Ý chính: từng tài khoản trong Phạm vi ảnh hưởng (bước 1-5 của TC-001) ---
    for account, role, _ in ACCOUNTS:
        ctx.goto("/", account=account)
        ctx.wait_text("Danh sách việc", account=account)
        ctx.page_for(account).wait_for_timeout(1000)
        nav_text = _nav(ctx, account)
        ctx.screenshot(f"{account.lower()}-danh-sach-viec", account=account)
        ctx.check_main(f"{account}: vào Danh sách việc (bước 4)", "Danh sách việc" in ctx.page_text(account), account=account)
        ctx.check_main(f"{account}: thanh điều hướng hiện mã {account} và vai trò {role} (bước 5)",
                       account in nav_text and role in nav_text, _line(nav_text), account=account)
        ctx.check_main(f"{account}: thanh điều hướng không còn chữ DEFAULT (bước 5)", DEFAULT_RE.search(nav_text) is None,
                       _line(nav_text), mark_text="DEFAULT", account=account, error_note=ERROR_NOTE)
    ctx.check_main("P300001: vẫn còn menu Tích hợp", "Tích hợp" in _nav(ctx, "P300001"), account="P300001")

    page = ctx.page_for("P100001")
    ctx.goto("/", account="P100001")
    ctx.wait_text("Danh sách việc", account="P100001")

    # --- Biến thể 1: /api/me không còn trường workspace (chỉ GET; không in nội dung trả về) ---
    def api_me():
        found = page.evaluate(
            """async () => { const r = await fetch('/api/me', {credentials: 'same-origin'}); const t = await r.text();
                return {status: r.status, has: /"workspace"\\s*:/.test(t)}; }""")
        ctx.check_minor("Biến thể 1: /api/me không còn trường workspace", found["status"] == 200 and not found["has"],
                        f"/api/me trả {found['status']}, " + ("còn trường workspace" if found["has"] else "không có trường workspace"))
    _variant(ctx, "Biến thể 1: /api/me không còn trường workspace", api_me)

    # --- Biến thể 2: bấm English rồi quay lại Tiếng Việt ---
    def english():
        page.get_by_role("button", name=re.compile(r"^English$")).or_(page.get_by_role("link", name=re.compile(r"^English$"))).first.click()
        ok = ctx.poll_until(lambda: "Sign out" in _nav(ctx, "P100001"), seconds=10, account="P100001")
        nav_en = _nav(ctx, "P100001")
        ctx.check_minor("Biến thể 2: bản English không còn chữ DEFAULT", bool(ok) and DEFAULT_RE.search(nav_en) is None,
                        _line(nav_en), mark_text="DEFAULT", account="P100001", error_note=ERROR_NOTE.replace("bước 5", "biến thể 2"))
        page.get_by_role("button", name=re.compile(r"^Tiếng Việt$")).or_(page.get_by_role("link", name=re.compile(r"^Tiếng Việt$"))).first.click()
        ctx.poll_until(lambda: "Đăng xuất" in _nav(ctx, "P100001"), seconds=10, account="P100001")
    _variant(ctx, "Biến thể 2: bản English không còn chữ DEFAULT", english)

    # --- Biến thể 3: tải lại trang (F5) khi đang đăng nhập ---
    def reload_page():
        page.reload(wait_until="domcontentloaded")
        ctx.wait_text("Danh sách việc", account="P100001")
        page.wait_for_timeout(1000)
        nav_text = _nav(ctx, "P100001")
        ctx.check_minor("Biến thể 3: sau khi tải lại trang (F5) vẫn không có chữ DEFAULT", DEFAULT_RE.search(nav_text) is None,
                        _line(nav_text), mark_text="DEFAULT", account="P100001", error_note=ERROR_NOTE.replace("bước 5", "biến thể 3"))
    _variant(ctx, "Biến thể 3: sau khi tải lại trang (F5) vẫn không có chữ DEFAULT", reload_page)
