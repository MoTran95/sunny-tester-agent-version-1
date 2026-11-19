# Thêm dự án mới hoặc máy mới vào bộ chạy test

## Máy mới (một lần)
1. Python 3 + `pip install -r scripts/requirements-tu-dong.txt` (Playwright; dùng Chrome hoặc Edge có sẵn, không tải trình duyệt). Chạy Python kèm `-X utf8`.
2. Video ca lỗi (tùy chọn, hỏi người dùng): `python -m playwright install ffmpeg` (~1,6 MiB).
3. `git config core.hooksPath .githooks` (hook sinh lại trang HTML trước mỗi commit).
4. `.env` (không commit): `<TIỀN_TỐ>_URL`, `<TIỀN_TỐ>_<MÃ>_USER`, `<TIỀN_TỐ>_<MÃ>_PASSWORD`; mẫu ở `.env.example`. Người dùng tự điền mật khẩu.
5. `python -X utf8 scripts/kiem-tra-may-moi.py` (kiểm tổng thể) và `python -X utf8 scripts/selftest/run_selftest.py` (`ALL OK`).

## Dự án mới (`<slug>`)
1. Tạo thư mục dự án: `scripts/tao-du-an.py` (xem `memories/conventions/nhieu-du-an.md`); ghi `.du-an-hien-tai`.
2. `testing/<slug>/auto-config.json`:
   `{"env_prefix": "...", "default_url": "https://<địa chỉ có nhãn staging/dev>", "login": {"id_labels": ["Mã nhân viên", "Employee ID"], "button_labels": ["Đăng nhập", "Sign in"], "login_api": "/api/auth/sign-in", "session_check_api": "/api/me", "session_minutes": 10, "max_consecutive_failures": 9}}`
   (nhãn ô và API lấy từ hệ thống thật bằng `scripts/inspect_page.py`; nhãn cả hai ngôn ngữ nếu có).
3. `testing/<slug>/auto-data.json`: `{"version": "<số bản ở chân trang>", …id dữ liệu test…}`; bản mới đổi số ở đây.
4. Test case theo `tao-checklist-test-case` (12 cột; cột Tự động hóa); script ca ở `testing/<slug>/<tính-năng>/auto/tc-xxx.py` dựng từ `assets/mau-ca-tu-dong.py`.
5. Bộ smoke theo `tao-smoke-test`; chạy `--smoke`; ghi lượt bằng `build_report.py add-run`.
6. Tên hiển thị tiếng Việt của tính năng: thêm vào `FEATURE_NAMES` trong `scripts/test_automation/report.py`.
7. `python -X utf8 scripts/build_docs.py --all` rồi mở `testing/<slug>/index.html`.

## Thương hiệu
Mặc định logo Sunny (`docs/thuong-hieu/brand.json`). Dự án của thương hiệu khác: tạo `testing/<slug>/brand.json` chỉ gồm khóa muốn đổi (`name`, `logo`, `logo_enabled`); đường dẫn tính từ gốc repo. Màu và font là giao diện chung ở `theme.py`.
