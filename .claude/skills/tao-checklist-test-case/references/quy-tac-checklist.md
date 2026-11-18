# Quy tắc viết checklist

> **Từ 2026-11-18 (file gộp):** feature mới không có `checklist.md` riêng. Các quy tắc dưới đây vẫn áp dụng cho các cột `Tình huống`, `Ưu tiên`, `Kỹ thuật`, `Nguồn` của **bảng gộp 13 cột** trong `test-case.md` (`Mã | Tình huống | Ưu tiên | Kỹ thuật | Điều kiện trước | Các bước | Dữ liệu test | Kết quả mong đợi | Nguồn | Kết quả thực tế | Trạng thái | Người viết | Tự động hóa`). Mục "Chưa đưa vào" và "Câu hỏi cho BA" nằm cuối `test-case.md`. Bảng 5 cột dưới đây chỉ còn cho feature cũ có hai file (Đăng nhập).

## Khuôn bảng (5 cột, tiêu đề cố định để script đọc)
`| Mã | Tình huống | Ưu tiên | Kỹ thuật | Nguồn |`
- **Mã:** `TC-001`, `TC-002`… liên tục, không nhảy số, không dùng lại. Dòng **Cao xếp trước**, rồi Trung bình, rồi Thấp (script `sinh-bang.py` tự đánh mã sau khi xếp).
- **Tình huống (= tên test case):** câu đầy đủ rõ nghĩa dạng `<Hệ thống làm gì/hiển thị gì> khi <người dùng làm gì/điều kiện>`, ví dụ `Đăng nhập thành công khi nhập đúng tên và mật khẩu`. Không rút gọn kiểu `điều kiện: kết quả`, không dùng mã nội bộ; con số chi tiết để cột Dữ liệu test (trong tên chỉ giữ số làm nên ca, đặt trong ngoặc). Một mục tiêu một dòng, **một** giá trị không hợp lệ hoặc **một** đường không được phép.
- **Ưu tiên:** `Cao`, `Trung bình`, `Thấp` (tiêu chí trong `ky-thuat-thiet-ke.md`).
- **Kỹ thuật:** đúng một trong `EP`, `BVA`, `Bảng quyết định`, `Chuyển trạng thái`, `Use case`, `Đoán lỗi`.
- **Nguồn:** bắt đầu bằng nhãn.
  - `Có trong tài liệu: <mã> (<tên ngắn>), <mã> (<tên ngắn>)…` — mã requirement hoặc mã câu trả lời BA.
  - `Suy luận: <mã> (…) …, vì <một câu lý do>` — điểm xuất phát là điều nguồn đã ghi rõ.
  - Cần thêm: `· ⚠️ hệ thống hiện khác (<một câu>)` khi bản đang chạy làm khác điều requirement/BA (nghi lỗi, chưa phải lỗi đã xác nhận).
  - **Không có dòng `Giả định` trong bảng.**
  Tên ngắn lấy từ `truy-vet-cau-hinh.json` của feature (xem `memories/project/truy-vet-requirement.md`); tên ngắn giúp người đọc hiểu mã mà không phải mở requirement.

## Đầu file, sau bảng
- Đầu file: bảng nhỏ (Ngày lập, Hệ thống, Nguồn, "Chỉ làm: checklist, chưa viết bước chi tiết"), đoạn "Cách đọc cột Nguồn", lưu ý an toàn nếu có ca có thể gây khóa.
- Sau bảng: **Câu hỏi cho BA** (mỗi câu kèm mã requirement liên quan; xem dưới), **Chưa đưa vào** (phần chưa chốt), **Tự kiểm**.

## Câu hỏi cho BA và phần chưa chốt
- **Không có bảng soát:** mọi chỗ nguồn không nói thành `Giả định` → đưa vào "Câu hỏi cho BA", mỗi câu ghi mã requirement liên quan. Câu hỏi viết đọc là hiểu (tình huống thật, nêu cách mình đang hiểu); khuôn đầy đủ ở skill `phan-tich-requirement`.
- **Có bảng soát:** chỉ viết dòng đã rõ/đã chốt (✅). Phần ❓ không viết dòng, chỉ liệt kê ở "Chưa đưa vào" kèm mã câu hỏi sẵn có (ví dụ B4); không lập câu hỏi mới trùng.
- Điều requirement ghi rõ thì **suy luận tiếp** (ghi `Suy luận`), không hỏi. Chỗ nguồn **chưa ghi** (con số, cách hiển thị) thì hỏi, không lấp bằng kinh nghiệm.

## Tự kiểm trước khi trả lời (script `kiem-tra-tc.py` làm phần cơ học)
- Mỗi mã requirement (và mã câu trả lời đã chốt cần phủ) có ít nhất một dòng.
- Không trùng mã. Dòng nào cũng có nhãn nguồn. Không có dòng `Giả định` trong bảng.
- Kỹ thuật và ưu tiên đúng danh sách; Cao xếp trước.
- Mỗi dòng một giá trị không hợp lệ; chưa có dòng nào thêm quy tắc mà nguồn không nêu.
