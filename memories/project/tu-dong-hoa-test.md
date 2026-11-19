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
API ca: `CASE_INFO{code,title,accounts,invalidates_sessions,ready_account,wrong_attempts}`; `ctx.goto/wait_text/poll_until/page_text/screenshot/page_for/test_data/precondition/check_main/check_minor(mark_text,error_note)/sign_in/submit_login/verify_account_ready`. `.env`: `<TIỀN_TỐ>_URL`, `_<MÃ>_USER`, `_<MÃ>_PASSWORD`. Venv: `.venv` trong repo (do `scripts/cai-dat-may-moi.py` tạo; máy này còn `~/.venvs/playwright`); `scripts/_venv.py` làm `run_tests/auto_login/inspect_page/selftest` tự chạy lại bằng venv nếu Python hệ thống thiếu Playwright (nên gõ `python -X utf8 …` được). Playwright 1.65.2, Chrome có sẵn, ffmpeg-1013 đã cài.
Dự án mới: `scripts/tao-du-an.py` sinh khuôn `auto-config.json` (chỗ `<…>`, `config.load` từ chối chạy khi chưa điền), `auto-data.json`, `ten-tinh-nang.json` (tên hiển thị tính năng theo dự án, thay cho `FEATURE_NAMES` cũ trong `report.py`). Trang bug luôn nhúng video dù file không có trên máy (video bị gitignore; trước đây máy khác sinh lại là mất khung video và báo trang cũ). `.gitattributes` ép LF cho md/json/py/html/css. Trang dùng chung (`docs/*.md`, `testing/*.md`) sinh trong lượt của từng dự án: link tới md đổi sang html theo MỌI dự án (`render_all` dùng `projects()`), nếu không trang đổi theo dự án hiện tại và `--check` báo cũ mãi khi có từ 2 dự án.
**Máy khác và kiểm tự động (2026-11-19, người dùng yêu cầu chạy Windows + Mac, không lẫn dự án, kết quả đúng như dự án đầu):** `scripts/cai-dat-may-moi.py` (đa nền tảng, thay bản PowerShell) tạo `.venv`; `kiem-tra-may-moi.py` biết đường dẫn trình duyệt/ffmpeg của Windows, Mac, Linux; chưa chạy thử trên Mac thật. `kiem-tra-lan-du-an.py` (dấu hiệu mỗi dự án: slug, tiền tố `.env`, tên miền, tên hiển thị, mã tài khoản) bắt thông tin lẫn vào skill hoặc dự án khác; `kiem-tra-ro-mat-khau.py` dò mật khẩu `.env` trong file văn bản (chỉ in tên khóa); `tao-bug-report/scripts/kiem-tra-bug.py` kiểm khuôn bug; `report.validate_conclusion` làm `add-run` từ chối kết luận thiếu, chung chung hoặc bỏ sót ca chưa có kết quả; tất cả (trừ add-run) nằm trong `kiem-tra-bo-nho.py`. Trần nhập sai và `block_minutes` KHÔNG có mặc định (`failure_counter.py`: chưa khai thì từ chối nhập sai). `login.mode = "manual"` + `auto_login.py --manual` cho SSO/OTP/captcha (người test tự đăng nhập, script chỉ chờ). Mỗi lần chạy in dòng "Dự án: … · địa chỉ: …" và cảnh báo nếu khác `.du-an-hien-tai`.

## Bẫy đã gặp (lý do thiết kế)
- Kết luận Đạt/Không đạt chỉ khi script chạy trọn (từng báo Không đạt giả vì chụp lúc còn "Đang tải…", vì `except: pass` nuốt lỗi); số bản chân trang hiện sau vài giây → `poll_until`.
- Đăng xuất làm mất phiên máy chủ; mỗi lần đăng nhập là một phiên riêng (đăng xuất phiên này không làm chết phiên đã lưu).
- Đổi tên hàng loạt từng gây lỗi chuỗi/tham số/cờ lệnh: selftest bắt được; chạy selftest sau mọi lần sửa thư viện (`RESULT: ALL OK`).
- Windows: `-X utf8`; Git Bash đổi `/đường-dẫn`; heredoc làm méo `\` (viết file bằng Write); máy chủ giả dừng bằng `Get-NetTCPConnection -State Listen`.
- Công cụ chặn tạo dữ liệu thật/tải file nếu chưa được người dùng cho phép rõ.
- Bộ đếm nhập sai: không tin con số hay quy tắc đếm của BA khi thiết kế cơ chế an toàn, chỉ tin điều đã quan sát; trần và thời gian chặn do requirement hoặc người test chốt (không có mặc định). Chi tiết lần sai ở Banking Lite: `modules/banking-lite/tu-dong-hoa.md`.

## Trạng thái từng dự án
Nằm ở `memories/modules/<slug>/tu-dong-hoa.md` (số bản, kết quả lượt, quyết định riêng), không ghi ở file chung này.

## Thiết kế trang và thương hiệu (người dùng chốt, 2026-11-18 đến 19)
Chi tiết ở `docs/thuong-hieu/README.md`. Điểm không suy ra từ code: màu nền chốt `#E8DFD0` (bản sáng đầu tiên chói mắt), có chế độ tối tự theo hệ điều hành; trang rộng gần hết màn hình, bảng có thanh kéo ngang luôn hiện + cột cố định; logo ở góc trái (không để giữa) và cấu hình được (`brand.json`) vì người khác dùng bộ công cụ; font tải về repo để giống hệt khi không có mạng; link truy vết phải nhảy đúng dòng; trang HTML phải luôn khớp md (4 lớp chặn). Màu cam logo (`#E8832A`) hơi khác vàng giao diện (`#D9902A`), chưa chỉnh.
