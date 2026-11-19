# Quy tắc đã chốt với người dùng (chạy test tự động)

Mỗi dòng là điều người dùng đã xác nhận hoặc bài học đã trả giá. Không đổi khi chưa hỏi.

## 1. Chọn ca và an toàn hệ thống
- Chỉ **bỏ qua ca mà chính bước làm gây chặn hệ thống** (lần sai thứ 10, nhập khi đang bị chặn, chờ hết chặn…), để tester tự làm: trạng thái `Bỏ qua`, cột Tự động hóa `Không tự động được: <lý do>`. Ca **chạm sát ngưỡng nhưng kết quả mong đợi là KHÔNG chặn** vẫn làm.
- **Trần nhập sai 9 lần, tính cộng dồn** (đăng nhập đúng xen giữa KHÔNG đưa về 0: đã quan sát khác quy định BA). Bộ đếm `failure_counter` từ chối vượt trần hoặc khi đang chặn; về 0 khi hết thời gian chặn hoặc `run_tests.py --reset-failure-counter` (chỉ khi chắc hệ thống đã về 0). Ca có nhập sai khai `ready_account` và `wrong_attempts`; xếp ca ít sai trước; gặp mã 429 thì dừng ngay, ghi `Không kết luận` (không phải Không đạt).
- Tạo dữ liệu thật (hồ sơ nháp…) chỉ khi người dùng cho phép rõ; công cụ chặn nếu chưa hỏi. Mỗi ca bấm Lưu dùng hết một hồ sơ: ghi `auto-data.json`.
- Tải file (ffmpeg, font) cần người dùng đồng ý, nêu tên file, nguồn, dung lượng.

## 2. Đăng nhập và mật khẩu
- Chỉ nhập tài khoản test của dự án vào địa chỉ **do người dùng nêu và có nhãn môi trường thử** (staging, dev, test, qa, sandbox, preview). Địa chỉ khác → không nhập, nhờ người dùng tự chạy `auto_login.py`.
- Mật khẩu chỉ nằm trong `.env`; chỉ thư viện đọc. Script ca, kết quả, ảnh, bug, chat **không bao giờ** chứa mật khẩu; mật khẩu sai dùng chữ giả (`Sai@Matkhau1`). `ctx.sign_in(tài khoản)` và `ctx.submit_login(..., password_of=…, variant=…)` để script không thấy mật khẩu.
- Phiên sống ngắn (Banking Lite 10 phút): runner kiểm phiên đầu lượt (thoát mã 3 nếu hết). Đăng xuất làm mất phiên phía máy chủ → khai `invalidates_sessions` hoặc dùng `ctx.sign_in` riêng cho ca đó (mỗi lần đăng nhập là phiên riêng).

## 3. Kết luận từng ca
- Giá trị: `Đạt`, `Đạt kèm ý phụ sai`, `Không đạt`, `Không kết luận`, `Chưa có script`. `Đạt kèm lỗi đã biết` chỉ ở smoke và chỉ cho ý được miễn trong tiêu chí trả build.
- Ý chính sai → Không đạt; ý phụ sai → chỉ ghi nhận. Trang kết quả theo tính năng: ca còn lỗi đã biết ghi `Không đạt` kèm bug (khác smoke).
- Chờ phần tử bằng `wait_text`/`poll_until` (trang hay ở "Đang tải…" vài giây), không chờ giây cố định; không `except: pass`.
- Trạng thái test case: `Chưa chạy`, `Đạt`, `Không đạt`, `Bị chặn` (chưa test được vì **bug của case khác**; ghi link bug ở Kết quả thực tế), `Bỏ qua`.

## 4. Bằng chứng
- `check_main/check_minor(..., mark_text="chữ", error_note="Lỗi ở bước N (…): thấy <gì>, đáng ra <gì>.")`: ý sai → ảnh `-loi.png` (chỉ khung đỏ, dùng cho bug); có ý đạt khai `mark_text` → ảnh `-kiem.png` (khung xanh đạt, đỏ sai) hiện ở cột Evidence.
- Video quay mọi ca, **chỉ giữ ca Không đạt / Đạt kèm ý phụ sai** (`evidence/<dự-án>/chay-test/video/`, không vào git, người dùng đính tay vào bug). Cần ffmpeg của Playwright (`python -m playwright install ffmpeg`, xin phép); chưa có thì chạy tiếp không quay.
- Ảnh khoanh tay cho vùng nhiều dòng: `scripts/mark_error.py <ảnh> --box x1,y1,x2,y2`.

## 5. Ghi lượt và trang kết quả
- Dữ liệu gốc `testing/<dự-án>/run-results/<bộ>.json` (chỉ thêm lượt, không sửa tay); trang `smoke-ket-qua.*` (bộ smoke) hoặc `<tính-năng>/ket-qua-test-case.*`. Cột: ID, Test case, Các bước, Kết quả mong đợi, Status, Evidence, Bug, Số lần chạy (không có cột Kết quả thực tế vì đã có Status).
- Ca không test được vì bug khác: `--status "N=Bị chặn" --blocked-by "N=BUG-nnn"`; ca bỏ qua: `--status "N=Bỏ qua"`.
- **Kết luận và rủi ro** (`--conclusion-file` JSON: `headline`, `passed[]`, `not_tested[{cases,status,reason}]`, `risks[{title,detail}]`, `suggestion`) bắt buộc cho lượt theo tính năng. Viết để người test **đánh giá được**: số liệu cụ thể; mỗi rủi ro nói **chuyện gì xảy ra với người dùng** và đã/chưa kiểm; ca chưa có kết quả nói rõ vì sao; đề xuất ghi là đề xuất, quyết nhận/trả build là của người test hoặc PO. Cấm câu chung chung ("còn một số lỗi") và viết tắt khó hiểu. Ghi chú lượt viết câu đầy đủ (môi trường, bản, ngày, số ca đã/chưa có kết quả).
- Lượt tổng theo tính năng: `Đạt toàn bộ` / `Có case không đạt` / `Chưa chạy hết`; smoke: `Nhận build` / `Trả build` / `Chưa đủ kết luận`.

## 6. Bug từ lượt chạy
- Mỗi nguyên nhân một bug. **Chỉ gộp khi người dùng hoặc Dev xác nhận cùng chỗ sửa** (ví dụ câu báo lỗi tiếng Việt và English cùng sửa một chỗ → một bug). Mã `BUG-nnn` không dùng lại số đã bỏ.
- Đính ảnh `-loi` (tô đỏ như trang test case) và video `.webm` trong mục Đính kèm; suy luận (ví dụ cách hệ thống đếm) gắn nhãn Giả định, câu hỏi cho Dev nêu đủ nghĩa. Chi tiết nội dung bug: skill `tao-bug-report`.
- Ca Không kết luận do lỗi của mình (bộ đếm, script) **không phải bug** và không ghi Không đạt.

## 7. Trang HTML luôn khớp nguồn, giao diện thống nhất
- `build_docs.py --all` sinh mọi trang: tài liệu md (SRS, bảng soát, câu hỏi BA, checklist, test case, truy vết, nhật ký khám phá, hướng dẫn), kết quả, bug, trang tổng `testing/<dự-án>/index.html`. `--check` so nội dung (không dựa giờ sửa file). Bốn lớp chặn cũ: `CLAUDE.md` bước 5, `kiem-tra-bo-nho.py`, hook `.githooks/pre-commit` (`git config core.hooksPath .githooks` một lần mỗi clone), selftest.
- Link kiểu `file.md#L66` nhảy đúng dòng; mã requirement, TL, câu hỏi BA, TC tự thành link tới dòng định nghĩa. Muốn link đúng thì md theo quy ước: mã nằm ở **ô đầu** của dòng bảng, TL ở ô đầu dòng của bảng soát, câu hỏi BA có `<a id="a1"></a>`, test case có `<a id="tc-001"></a>`.
- Giao diện (màu, font, bảng rộng, chế độ tối, logo ở góc trái) duy nhất ở `scripts/test_automation/theme.py`; font cục bộ `docs/thuong-hieu/fonts/`; thương hiệu cấu hình ở `docs/thuong-hieu/brand.json` (riêng dự án: `testing/<dự-án>/brand.json`). Muốn đổi giao diện: sửa `theme.py`, không sửa từng trang.

## 8. Bẫy môi trường
- Windows: chạy Python kèm `-X utf8`; Git Bash đổi `/duong-dan` thành `C:/Program Files/Git/…` (dùng PowerShell hoặc `MSYS_NO_PATHCONV=1`); heredoc làm méo dấu `\` (viết file bằng công cụ Write).
- Đổi tên hàng loạt: chạy selftest (từng bắt lỗi tên dùng dạng chuỗi, tham số che tên hàm, cờ lệnh lệch tên).
- Hệ thống mới có thể đổi địa chỉ/bản: kiểm `/api/health` và số bản ở `auto-data.json` trước khi chạy.
