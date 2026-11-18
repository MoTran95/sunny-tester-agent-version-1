# Quy trình khám phá → SRS → bảng soát → checklist (cho AI đọc)
Đọc khi: làm/sửa SRS, hoặc cần biết vì sao khuôn hiện tại như vậy. Quy trình đầy đủ nằm trong `SKILL.md` của từng skill; đây chỉ là quyết định + bẫy.

## Phạm vi
- Người dùng làm **từng bước nhỏ rồi ghép**. Chuỗi: khám phá → SRS → bảng soát/câu hỏi BA → checklist → test case. Bước sau chưa được yêu cầu thì **không làm trước**: chạy test, bug, retest, báo cáo, Jira chưa lên kế hoạch.
- Khám phá **đầy đủ**; chỉ tránh đổi dữ liệu người khác/khóa hệ thống. Không chừa trống vì "hơi rủi ro". Mật khẩu người dùng gõ.

## Quyết định đã chốt
| Chủ đề | Quyết định |
|---|---|
| SRS | Sống: mỗi feature 1 file, sửa tại chỗ + "Lịch sử thay đổi"; ID không đổi/không dùng lại; bỏ yêu cầu → nhãn `đã bỏ`. Khám phá/ảnh/báo cáo = ảnh chụp theo ngày, tạo mới, không sửa |
| Nhãn | `đã thấy` / `chưa rõ` / `đã bỏ`; chỉ BA/dev xác nhận mới nâng cấp. Từ 2026-11-18 `LOGIN` là yêu cầu theo BA (xem `feature-dang-nhap.md`) |
| Định dạng | Markdown trong repo; bug nháp MD trước, Jira sau |
| Khuôn v2 | Story + luồng + AC; cột `Tình huống | Bối cảnh | Người dùng làm | Hệ thống phản hồi | Nhãn·Bằng chứng·Liên quan`; chép nguyên văn thông báo vào ô phản hồi. Bỏ Cho trước/Khi/Thì (người dùng không hiểu). Quy tắc dữ liệu/thông báo chỉ là bảng tra phụ. Khuôn: `srs/_template.md`; ID + nguồn: `srs/id-and-source-rules.md` (đọc trước khi viết SRS) |
| ID | `LOGIN-S01-AC01`, `-R01` quy tắc, `-M01` thông báo, `-Q01` câu hỏi, `-E01` bằng chứng; mã feature = chữ HOA tiếng Anh ngắn; AC = đơn vị gắn test case |
| Ghi nguồn | Mỗi AC trỏ `-Exx`; bảng Bằng chứng có link tệp + "Cách kiểm lại"; bằng chứng không ảnh (Network, localStorage) ghi rõ "không có ảnh". Khuôn v1 (FR/BR, `NK#n`…) bỏ vì không truy được |
| Bảng checklist v3 | `ID | Tên checklist | Nguồn` (+ Ưu tiên, Lý do viết riêng); tên dạng "Kiểm tra <đối tượng> <hành vi> khi <điều kiện + dữ liệu>"; mỗi TC một mục tiêu, một dữ liệu, không gộp; chỉ functional. Nay thay bằng skill `tao-checklist-test-case` (5 cột) |
| Câu hỏi BA | Khuôn khối, không bảng: Vấn đề → Ví dụ số thật → Mình đang hiểu → Vì sao hỏi → ô trả lời. Nhóm A hỏi ngay / B hỏi sau / C tự kiểm tra. `CH` = có dấu vết trong SRS, `KN` = kinh nghiệm (chỉ hỏi khi cần). Nguồn câu chữ duy nhất = `cau-hoi-cho-ba.md` |
| Trả lời BA | Mã `TL-xx`, ghi ai nói + ngày; SRS chỉ sửa khi BA/team xác nhận |
| Luật test case | Mỗi TC tự đứng được (không "như TC-xxx"), đủ điều kiện trước + bước + dữ liệu + kết quả; giữ nguyên số lượng/mã TC đã xác nhận, thấy trùng/thiếu thì ghi riêng, không tự gộp/xóa/thêm; nguồn thiếu → `CẦN XÁC NHẬN` + câu hỏi BA |

## Pilot
- `LOGIN`: 18 ảnh, 4 story, 24 AC. `RECO`: khám phá 38 hàng/10 ảnh, SRS 37 AC, `check-srs.py` 0 lỗi. Chi tiết trong file feature của dự án.
- Ứng viên feature chưa làm: trang Tích hợp `/integrations` (P300001, chỉ đọc, che CCCD/SĐT); đổi ngôn ngữ VI/EN.
- Bài học: **trí nhớ** về khám phá cũ có thể thiếu luật (bản cũ 2 luật, thực tế ≥5) → lần khám phá ĐẦU phải làm bằng thao tác thật + đọc API/tệp giao diện cho đủ. Feature "nhỏ" có thể ra 37 AC.
- **Từ 2026-11-18: đã khám phá (có `bao-cao.md` + ảnh) thì không khám phá lại**, trừ khi người dùng nói rõ "khám phá lại"/"feature đã đổi" (chỉ phần đổi). Thiếu gì trong nhật ký → ghi chưa rõ + hỏi người dùng, không tự mở trình duyệt. Lý do: người dùng hết token.
- Phân tích `RECO` bằng script: kiểm mọi trích dẫn bằng `in` trên file SRS (74/74) và **tính lại số học từng AC** → lộ chỗ SRS tự lệch.
- Cùng AC vừa đủ căn cứ vừa mơ hồ → **tách**: phần đủ vào bảng 1, phần mơ hồ vào bảng 2. Mã Req = AC + R + M (S là nhóm, Q/E không phải Req).
- `RECO` bảng soát 37 AC: sau TL-02 17 AC chỉ ✅, 16 cả hai, 4 chỉ ❓. Câu hỏi: 3 đã trả lời, còn Hỏi ngay 4 / Gom sau 12 / Tự tìm 15. Chưa gửi BA.

## Sách Sunny (nguồn chiến lược)
- Notion "Nền Tảng Tester Thời AI – Version 2". Đã đọc ~1/3 (Phần 1, 2, 5, 6, 7, 8). Tóm tắt: `testing/chien-luoc-phan-tich-requirement.md`.
- Ý chính: Tách–Xoay 6 nút–Lọc; bảng soát đã rõ/cần hỏi; 3 nhóm câu hỏi; ba nhãn nguồn; checklist trước chi tiết sau.
- Sách cho gộp TC khi chỉ khác dữ liệu, **trái luật "không gộp"** của người dùng → đã nêu để người dùng quyết; các skill hiện giữ "không gộp".
- `notion-fetch` trang lớn bị lưu ra file: trích `text` từ JSON bằng script, đọc theo khoảng dòng.

## Bẫy
- Sinh bảng MD bằng script: escape `|` **từng ô**, không escape cả dòng. Kiểm số cột từng dòng bằng file script (không heredoc `python -`, regex bị méo).
- Phối hợp mật khẩu: mình điền ô Mã nhân viên, người dùng gõ mật khẩu + bấm, báo "xong", mình đọc bằng screenshot + Network.

## Từ người dùng nói lệch
"SRS" = bước ngay sau khám phá. "Thiết khai" có thể là "thiết kế (test)". "Queue" chưa rõ, hỏi trước khi dùng.
