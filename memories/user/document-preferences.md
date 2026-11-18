# Người dùng muốn tài liệu viết thế nào (chi tiết)
Đọc khi: viết báo cáo, SRS, bảng soát, checklist, câu hỏi BA.

## Báo cáo khám phá
- MD: sơ đồ Mermaid, ảnh bằng chứng, luồng end-to-end như người dùng thật; không bịa, chưa rõ thì hỏi.
- HTML: giải thích vai trò cho người mới chưa biết lĩnh vực; ảnh khoanh nút đánh số; sơ đồ luồng đánh số bước; đường end-to-end; điểm mơ hồ có lý do + bằng chứng.
- **Giao diện HTML giữ nguyên ở mọi máy, mọi dự án** (font, màu, kiểu sơ đồ) — người dùng báo khi Mac đổi font. Cách làm: `decisions/decision-log.md`, skill `feature-exploration-report` `references/so-do.md`.
- Phải mở được trong khung xem trước của app (≤512 KiB): `modules/banking-lite/report-v2-html.md`.
- Từ bị chê: "giải phẫu", "dây chuyền", "tick" (script skill chặn). Thuật ngữ IT đúng ngữ cảnh.

## SRS
- Truy nguồn được (ID thống nhất, bằng chứng có link), kiểu story + AC, không tách nhiều bảng khó đọc.
- Khám phá đầy đủ, chỉ tránh đổi dữ liệu người khác/khóa hệ thống; không "bỏ ngõ" vì rủi ro nhỏ (`project/srs-process.md`).

## Bảng gửi người dùng/BA (bài học bảng soát `RECO`)
Bản đầu quá cô đọng ("thiếu (Dữ liệu)", "KN-02", "M01", "DSR" không giải thích) nên người dùng không hiểu. Quy tắc:
- Mỗi dòng có **cột Tình huống** (làm gì, dữ liệu cụ thể), nội dung **câu đủ ý**.
- Chép **nội dung thông báo** thay vì mã M01…; giải thích LTV/DSR/thặng dư/"hồ sơ nền" ở bảng thuật ngữ đầu file.
- Mã nội bộ (KN-02, CH-03) chỉ để tra chéo, không làm nội dung chính; nhãn chữ thường ("Hỏi BA ngay", "Tự kiểm tra trên hệ thống trước") thay tên riêng của sách.
- Gộp cột phụ cho gọn (6 cột). Cột "Câu hỏi gửi BA" ghi luôn câu BA đã trả lời.
- **Một mã nhiều dòng thì không chép lại ô** (chốt 2026-11-18, người dùng chê "duplicate" ở AC09): dòng thứ hai trở đi ô Tình huống ghi ngắn "Phần … của dòng trên", ô trích ghi `—`; mã câu hỏi (B15…) kèm link "mở câu" tới file câu hỏi. `kiem-tra.py` mục 8 báo lỗi nếu chép lại. Khi thêm dòng mới vào bảng soát/SRS phải tự áp dụng, không đợi bị nhắc.

## Checklist / test case
- Câu hỏi BA dựa kinh nghiệm (không dấu vết trong nguồn) → tách riêng, hỏi khi cần.
- **Requirement ghi rõ thì suy luận tiếp, ghi chưa rõ thì hỏi** (chốt 2026-11-18 sau khi chê A7, A8, B14 là "vô tri"). Ghi "suy ra từ <mã/TL>" kèm lý do. Lý do bảo mật dùng để suy hành vi chức năng, không tự đặt ca test bảo mật. Không hỏi độ dài mã ở đăng nhập (chỉ báo đúng/sai) và A6 (suy từ "10 lần liên tiếp"; hệ thống làm khác = nghi lỗi). Skill `phan-tich-requirement` quy tắc 1b.
- Có cột ưu tiên + lý do cần nhiều TC/câu hỏi.
- Test case có cột ghi khi chạy: Ưu tiên, Kết quả thực tế, Trạng thái, Người viết (mặc định Sunny Tran), Tự động hóa (lưu script chạy lại cho đỡ token) — khuôn 12 cột của `tao-checklist-test-case`.

## Câu hỏi BA
Xưng hô, từ đã chốt, khuôn: `conventions/ba-question-wording.md` (bài học "câu chữ máy móc như dịch tiếng Anh").
