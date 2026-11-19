# Tự động hóa test case (Playwright dùng chung nhiều dự án)
Đọc khi: sửa thư viện `scripts/test_automation/`, thêm dự án, hoặc cần biết trạng thái Banking Lite. **Quy tắc đã chốt với người dùng nằm ở skill `chay-test-tu-dong`** (`references/quy-tac-da-chot.md`), không chép lại ở đây. Hướng dẫn cho người: `docs/chay-test-tu-dong.md`; giao diện: `docs/thuong-hieu/README.md`.

## Cấu trúc
| Đường dẫn | Việc |
|---|---|
| `scripts/test_automation/` | `config`, `session`, `context` (`ctx`), `results`, `runner`, `failure_counter`, `report` (bảng kết quả), `bug_page`, `docs_pages` (md→HTML + trang tổng), `theme` (màu, font, logo, brand) |
| `scripts/*.py` | `auto_login`, `run_tests`, `build_report` (`add-run`/`build`/`bug-pages`), `build_docs` (`--all/--check/--stage`), `inspect_page`, `mark_error`, `process_logo`, `tai-font`, `selftest/run_selftest.py` |
| `testing/<dự-án>/auto-config.json`, `auto-data.json` | cấu hình đăng nhập/URL; dữ liệu test (số bản, id hồ sơ) |
| `testing/<dự-án>/<tính-năng>/auto/tc-xxx.py` | `CASE_INFO` + `run(ctx)`; hàm chung ở `*_common.py` cùng thư mục |
| `testing/<dự-án>/run-results/<bộ>.json` | dữ liệu lượt chạy (chỉ thêm) → `smoke-ket-qua.*` hoặc `<tính-năng>/ket-qua-test-case.*` |
| `evidence/<dự-án>/chay-test/` | ảnh (`-kiem`, `-loi`), `result-*.json`, `video/` (gitignore) |
| `.phien-dang-nhap/<dự-án>/` | phiên đã lưu, `failure-counter.json` (gitignore) |
| `.githooks/pre-commit`, `docs/thuong-hieu/` | sinh lại HTML trước commit; `brand.json`, logo, `fonts/` |
API ca: `CASE_INFO{code,title,accounts,invalidates_sessions,ready_account,wrong_attempts}`; `ctx.goto/wait_text/poll_until/page_text/screenshot/page_for/test_data/precondition/check_main/check_minor(mark_text,error_note)/sign_in/submit_login/verify_account_ready`. `.env`: `<TIỀN_TỐ>_URL`, `_<MÃ>_USER`, `_<MÃ>_PASSWORD`. venv máy này `C:\Users\Admin\.venvs\playwright` (`playwright==1.65.2`, Chrome có sẵn; ffmpeg-1013 đã cài).

## Bẫy đã gặp (lý do thiết kế)
- Kết luận Đạt/Không đạt chỉ khi script chạy trọn (từng báo Không đạt giả vì chụp lúc còn "Đang tải…", vì `except: pass` nuốt lỗi); số bản chân trang hiện sau vài giây → `poll_until`.
- Đăng xuất làm mất phiên máy chủ; mỗi lần đăng nhập là một phiên riêng (đăng xuất phiên này không làm chết phiên đã lưu).
- Đổi tên hàng loạt từng gây lỗi chuỗi/tham số/cờ lệnh: selftest bắt được; chạy selftest sau mọi lần sửa thư viện (`RESULT: ALL OK`).
- Windows: `-X utf8`; Git Bash đổi `/đường-dẫn`; heredoc làm méo `\` (viết file bằng Write); máy chủ giả dừng bằng `Get-NetTCPConnection -State Listen`.
- Công cụ chặn tạo dữ liệu thật/tải file nếu chưa được người dùng cho phép rõ.
- Bộ đếm nhập sai: giả định "đăng nhập đúng đưa về 0" (TL-06 của BA) SAI, P100001 bị chặn 5 phút ở TC-014 (lần sai thứ 5 của ca, cộng dồn 11 lần 401 trong ngày; hết chặn thì có vẻ về 0). BUG-008.

## Banking Lite (cập nhật 2026-11-19)
- Địa chỉ test `https://staging-banking-lite.vercel.app/` (địa chỉ cũ đã gỡ; staging dùng chung dữ liệu: hồ sơ nháp cũ còn). Bản 1.3.0.
- Smoke (7 ca, lượt 2 trên staging): 5 Đạt, TC-001 Đạt kèm lỗi đã biết (`DEFAULT`, BUG-001), TC-022 RECO Không kết luận vì hồ sơ nháp riêng của ca đã dùng hết (cần hồ sơ mới: hỏi người dùng, `testing/banking-lite/auto/create_draft_application.py --tc-022-only --overwrite`).
- Đăng nhập 43 ca: đã chạy 31 (17 Đạt, 14 Không đạt); TC-014 và TC-021 Bị chặn bởi BUG-008; bỏ qua TC-015…020, 022, 037; TC-042, 043 chờ BA (B15). Bug: BUG-001 (`DEFAULT`), BUG-002 (câu báo sai còn `Mã không gian`/`Workspace`, gộp VN+EN), 004, 005, 006 (câu kỹ thuật khi trống/mã dài), 007 (ô Mật khẩu giữ chữ), 008 (bộ đếm). BUG-003 đã gộp vào 002. Mã bug của công cụ team do người dùng điền.
- RECO: 4 script (TC-002, 009, 022, 023) đã Đạt ở lượt đầu; `reco_common.py` tìm khung `Thẩm định` theo chữ.
- Trang tổng `testing/banking-lite/index.html`; hai tính năng `dang-nhap`, `khuyen-nghi-ltv-dsr`; `gui-tham-dinh` chỉ có khám phá.
- Chồng chéo chưa gộp: `truy-vet-smoke.py ghi-luot` (mục "Lượt chạy" trong smoke-test.md) vs `smoke-ket-qua.*` (bản chính).
- `feature-exploration-report` còn giao diện riêng (Open Sans, CSS riêng), chưa dùng `theme.py`; chưa hỏi người dùng có muốn thống nhất không.

## Thiết kế trang và thương hiệu (người dùng chốt, 2026-11-18 đến 19)
Chi tiết ở `docs/thuong-hieu/README.md`. Điểm không suy ra từ code: màu nền chốt `#E8DFD0` (bản sáng đầu tiên chói mắt), có chế độ tối tự theo hệ điều hành; trang rộng gần hết màn hình, bảng có thanh kéo ngang luôn hiện + cột cố định; logo ở góc trái (không để giữa) và cấu hình được (`brand.json`) vì người khác dùng bộ công cụ; font tải về repo để giống hệt khi không có mạng; link truy vết phải nhảy đúng dòng; trang HTML phải luôn khớp md (4 lớp chặn). Màu cam logo (`#E8832A`) hơi khác vàng giao diện (`#D9902A`), chưa chỉnh.
