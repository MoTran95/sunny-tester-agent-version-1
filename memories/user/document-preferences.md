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
- **Cột `Tình huống` của test case = tên test case, câu ĐẦY ĐỦ rõ nghĩa** (2026-11-18: bản câu dài lộn xộn bị chê khó hiểu; bản rút ngắn `điều kiện: kết quả` cũng bị chê, người dùng muốn như "Đăng nhập thành công khi nhập đúng tên và mật khẩu"): dạng `<Hệ thống làm gì/hiển thị gì> khi <người dùng làm gì/điều kiện>`, ví dụ `Vẫn hiển thị Phê duyệt khi DSR đúng bằng mức 50%`; số liệu chi tiết để cột Dữ liệu test. Đã áp dụng cho `RECO` (38 TC) và ghi vào skill (quy tắc 13); `LOGIN` chưa đổi.
- **Cột `Điều kiện trước` viết gạch đầu dòng** (`- …` mỗi ý một dòng, ngắn; 2026-11-18 người dùng chê đoạn văn dài dòng): trong JSON mỗi phần tử `dieu_kien` là một dòng đã có `- ` ở đầu (script nối bằng `<br>`). **Điều kiện trước chỉ ghi dữ kiện QUAN TRỌNG để vào kiểm tra ca đó** (người dùng chốt 2026-11-18, sau 3 vòng sửa): KHÔNG ghi "đã đăng nhập" (đã nằm ở bước 1; bỏ luôn chữ "tự nhập mật khẩu" ở bước 1), KHÔNG định nghĩa hồ sơ nền ở đầu file. Mỗi ca 2–4 gạch ngắn: cách có hồ sơ + trạng thái hồ sơ liên quan kết quả của ca (vay, thời hạn, LTV, khoản trả mới…) + trạng thái đặc biệt nếu có (đầu trang đang `—`, tài sản chưa định giá). Bản 4–5 gạch lặp mọi ca bị chê rối. Muốn đổi phần đầu file thì xóa file rồi sinh lại (`sinh-bang.py` chỉ thay bảng giữa hai dấu; chỉ làm được khi chưa có cột ghi khi chạy). Đã ghi vào skill `tao-checklist-test-case` (quy tắc 5, 13; mẫu `mau-du-lieu-gop.json`); `LOGIN` giữ cách cũ.
- **Cột `Nguồn` của file gộp viết bằng câu thường + link** (2026-11-18, người dùng chê "mã + tên ngắn" khó hiểu, khó truy vết): dòng 1 căn cứ chính `Có trong tài liệu: <câu> (<link "SRS, S01-AC03" trỏ tới neo reco-s01-ac03>).`; dòng 2 câu trả lời chi phối (TL-02) nếu có; dòng 3 `⚠️ Hệ thống đang hiện …` nếu có; dòng 4 `Tra thêm: quy tắc R02; thông báo M06.` (không link, để script tính phủ). Link cần thẻ neo `<a id="reco-s01-ac03"></a>` ở ô đầu mỗi dòng mã SRS: **đã thêm 68 neo vào SRS `RECO`**; SRS khác/mới chưa có (khuôn `srs/_template.md` + skill `srs-from-website` chưa thêm neo, việc nên làm). Đã ghi vào skill; `LOGIN` giữ `mã (tên ngắn)`.
- Có cột ưu tiên + lý do cần nhiều TC/câu hỏi.
- Test case có cột ghi khi chạy: Ưu tiên, Kết quả thực tế, Trạng thái, Người viết (mặc định Sunny Tran), Tự động hóa (lưu script chạy lại cho đỡ token) — khuôn của `tao-checklist-test-case`: từ 2026-11-18 **một bảng gộp 13 cột** (có cả Kỹ thuật, không `checklist.md` riêng) cho feature mới; `LOGIN` giữ hai file 12 cột.

## Câu hỏi BA
Xưng hô, từ đã chốt, khuôn: `conventions/ba-question-wording.md` (bài học "câu chữ máy móc như dịch tiếng Anh").
