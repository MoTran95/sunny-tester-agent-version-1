# Bảng soát requirement — <tên feature> (<hệ thống>)

| | |
|---|---|
| Nguồn requirement | [<đường dẫn file>](<liên kết tương đối>) (mã `<MÃ>`, tình trạng <nháp / chính thức>, <phiên bản hệ thống nếu có>) |
| Ngày lập | <YYYY-MM-DD> |
| Cách làm | Tách, Xoay, Lọc (skill `phan-tich-requirement`) |
| Phạm vi | <số> đơn vị (AC, quy tắc, thông báo), cộng phụ lục cho chủ đề chung. Chỉ **functional**. Chưa viết checklist hay test case |
| Câu hỏi gửi BA | [cau-hoi-cho-ba.md](cau-hoi-cho-ba.md) |

## 1. Cách đọc
**Mỗi dòng trả lời ba câu:** (1) người dùng làm gì, (2) requirement cho biết gì hoặc chỗ nào chưa rõ, (3) cần hỏi BA câu gì.

**Cách đọc mã:** <giải thích cấu trúc mã của tài liệu, ví dụ `RECO` là tên feature, `S01` là story số 1, `AC01` là tiêu chí số 1>.

**Cột Trạng thái:**
- **✅ Đã rõ:** requirement trả lời đủ để biết thế nào là đúng. <Nếu tài liệu là bản nháp: nói rõ chưa phải xác nhận chính thức.>
- **❓ + loại vấn đề:** Thiếu thông tin, Chưa rõ nghĩa, Hai chỗ nói khác nhau, Số liệu không chính xác, hoặc Trình bày không thống nhất.

**Cách xử lý câu hỏi** (in đậm đầu mỗi câu hỏi):
- **🚨 Hỏi BA ngay:** hiểu sai thì kết quả đúng đổi.
- **📋 Hỏi BA sau (gom lại):** câu chữ, hiển thị, hoặc phần ngoài phần đang test.
- **🔍 Tự kiểm tra trên hệ thống trước:** xem hệ thống đang chạy để tìm câu trả lời. Chỉ cho biết hệ thống đang làm gì, không chứng minh là đúng.

**Cột "Câu hỏi gửi BA":** ghi số câu (A1, B3, C5…) trong `cau-hoi-cho-ba.md`, cách xử lý, câu hỏi và cách mình đang hiểu.

## 2. Giải thích thuật ngữ (theo requirement)
| Thuật ngữ | Nghĩa |
|---|---|
| <thuật ngữ> | <nghĩa, lấy theo lời của tài liệu> |

## 3. Câu trả lời đã nhận
| Mã | Nội dung trả lời | Nguồn | Áp dụng cho | Còn lại |
|---|---|---|---|---|
| TL-01 | <đúng ý người trả lời> | <ai nói, ngày, ở đâu; nếu là tester tự chốt thì ghi "chưa có xác nhận của BA"> | <mã câu hỏi, mã requirement> | <chỗ chưa trả lời, người cần xác nhận, hệ quả> |

(Chưa có câu trả lời nào thì ghi một dòng: "Chưa có câu trả lời nào.")

## 4. Tổng kết
| Chỉ số | Số lượng |
|---|---|
| Đơn vị chỉ có phần ✅ | <n> |
| Đơn vị có cả ✅ và ❓ | <n> |
| Đơn vị chỉ có ❓ | <n> |
| Tổng | <n> |
| Câu hỏi: 🚨 / 📋 / 🔍 | <a> / <b> / <c> |

## 5. Bảng soát theo từng story (hoặc theo nhóm requirement)

### <Tên nhóm 1> (<mã nhóm>)

| Mã | Tình huống (người dùng làm gì) | Requirement cho biết gì, hoặc chỗ chưa rõ | Trạng thái | Câu hỏi gửi BA | Trích nguyên văn |
|---|---|---|---|---|---|
| <MÃ-S01-AC01> | Ở hồ sơ nền, nhập lương 100.000.000 VND. | Nhãn là Phê duyệt. Mục Lý do ghi "Đáp ứng mọi quy tắc tín dụng." | ✅ Đã rõ | — | “<đoạn chép đúng nguyên văn từ requirement>” |
| <MÃ-S01-AC02> | Ở hồ sơ nền, nhập lương 58.285.714 VND. | Requirement gọi đây là "DSR đúng 70,00%", nhưng tính lại ra hơn 70% một chút. | ❓ Số liệu không chính xác | **A1. <Tiêu đề>** (🚨 Hỏi BA ngay)<br>**Hỏi:** <chép đúng từ file câu hỏi><br>**Mình đang hiểu:** <chép đúng từ file câu hỏi> | “<đoạn chép đúng nguyên văn>” |

Quy tắc chép vào cột câu hỏi: đúng khuôn `**<số câu>. <tiêu đề>** (<nhóm>)<br>**Hỏi:** …<br>**Mình đang hiểu:** …`. Câu phần C: `**C1. <tiêu đề>** (<nhóm>)<br>**Cần xem:** …<br>**Mình đang hiểu:** …<br>**Nếu không tìm ra, hỏi BA:** …`. Đơn vị rõ một nửa thì có một dòng ✅ và các dòng ❓ cùng mã.

## 6. Phụ lục: chủ đề chung, quy tắc và thông báo không gắn với một tiêu chí
| Mã | Tình huống | Requirement cho biết gì, hoặc chỗ chưa rõ | Trạng thái | Câu hỏi gửi BA | Trích nguyên văn |
|---|---|---|---|---|---|

## 7. Nhóm 🚨 Hỏi BA ngay
Nội dung đầy đủ ở Phần A của [cau-hoi-cho-ba.md](cau-hoi-cho-ba.md). Danh sách và mã liên quan:
- **A1. <Tiêu đề>** (liên quan <mã>)

## 8. Tự kiểm
- Đủ <n> đơn vị: mọi mã xuất hiện ít nhất một dòng.
- Mọi câu hỏi xuất hiện ít nhất một lần.
- Trích dẫn đã so từng chuỗi với requirement bằng `kiem-tra.py` (lỗi: 0).

## 9. Lịch sử thay đổi
| Ngày | Thay đổi |
|---|---|
| <YYYY-MM-DD> | Tạo mới |
