# Viết câu hỏi cho BA: đọc là hiểu, nghe như người nói

Người đọc có hai kiểu: **tester** cần kiểm tra từng dòng, và **BA** cần hình dung được rồi trả lời nhanh. Cả hai không cần biết mã nội bộ hay đọc lại tài liệu gốc. Đọc trước `memories/conventions/ba-question-wording.md` để lấy xưng hô và từ đã chốt.

## 1. Khuôn một câu hỏi (nhãn trường cố định, script đọc theo nhãn này)

**Phần A và B** (khối riêng cho mỗi câu):
```
## A1. <Tiêu đề là một câu hỏi nói thường>

**Người trả lời gợi ý:** BA | Dev | BA và Dev

<Kể tình huống thật có số: "Mình thử …". Có thể kèm một bảng nhỏ.>

**Hỏi:** Anh/chị cho mình hỏi: …?

**Mình đang hiểu:** … (nói rõ khi là đoán: "mình đoán", "mình chưa chắc")

**Vì sao hỏi:** … (một hai câu)

**Anh/chị chọn:**
- [ ] … 
- [ ] Khác: ______

**Câu trả lời của BA:** ______

*Mã cũ: CH-02, KN-05.*
```
**Phần C** (mình tự kiểm tra trước):
```
## C1. <Tiêu đề>

- **Cần xem:** (hoặc **Cần làm:**) việc mình làm trên hệ thống
- **Mình đang hiểu:** …
- **Nếu không tìm ra, hỏi BA:** …

*Mã cũ: KN-04.*
```
Dòng `*Mã cũ: …*` chỉ để tra chéo với mã trong bảng soát. Không đặt mã đó trong nội dung câu hỏi.

## 2. Giọng văn: nhắn tin cho đồng nghiệp
- **Số liệu trước, câu hỏi sau.** Kể điều mình thấy rồi mới hỏi.
- **Câu ngắn**, một ý một câu (khoảng 25 chữ trở xuống). Chủ ngữ rõ: "mình", "anh/chị", "màn hình", "hệ thống".
- Một câu hỏi một ý. Có nhiều ý thì tách thành các câu hỏi liền nhau, hoặc cho lựa chọn đánh dấu.
- **Gợi ý sẵn lựa chọn** để BA chỉ cần chọn.
- Nói thẳng chỗ mình chưa chắc. Không giả vờ biết.
- Xưng "mình", gọi BA "anh/chị" (chưa biết giới tính). Không dùng "người test".

## 3. Từ ngữ
- **Một từ cho một khái niệm** trong cả file. Lấy từ trong bảng "Từ đã chốt" của `ba-question-wording.md`. Từ mới thì hỏi người dùng rồi thêm vào bảng.
- **Chữ đang hiện trên màn hình** (tên khung, tên ô, nhãn, câu thông báo) giữ nguyên trong dấu ngoặc kép.
- Thuật ngữ của nghiệp vụ (LTV, DSR…) giải thích một lần ở đầu file, theo đúng lời của tài liệu gốc.
- **Tránh** các từ dịch máy: "tiến hành", "nhằm", "đối với", "dựa trên", "thực hiện việc", "kết quả mong đợi" (nói "kết quả đúng" hoặc "phải ra"), "phạm vi" (nói "phần mình cần test"), "ngưỡng" lẫn "hạn mức" lẫn "mức tối đa".
- **Tránh** danh từ hóa ("việc làm tròn", "sự hiển thị") khi có động từ ("làm tròn", "hiện").
- **Tránh** câu bị động dài và câu nhiều vế lồng nhau.
- Không viết tắt khó hiểu. Không để mã nội bộ (CH-02, M01, R05) làm nội dung chính.

## 4. Trước và sau (ví dụ thật)
**Trước** (nghe như dịch máy):
> Khi LTV hoặc DSR tính ra nhiều chữ số lẻ, hệ thống nên làm tròn thế nào, và nên so với hạn mức bằng số đã làm tròn hay số thật? Cách làm tròn này có áp dụng cả khi hiển thị trên màn hình không?

**Sau:**
> Mình thử vay 3.200.100.000 trên tài sản khai báo 4.000.000.000. Số thật là 80,0025%. Màn hình ghi 80,00% và vẫn Phê duyệt, trong khi mức tối đa là 80%. Nếu làm tròn lên thì ra 80,01%, tức là vượt, phải Từ chối.
> **Hỏi:** Anh/chị cho mình hỏi: hệ thống nên làm tròn kiểu nào, và có làm tròn cả số hiển thị không?
> **Mình đang hiểu:** Mình tạm chọn làm tròn lên, lấy 2 số sau dấu phẩy, cho cả số hiển thị và khi so với mức tối đa. Hệ thống hiện đang làm tròn gần nhất.

**Trước:**
> Khi thời hạn vay làm người vay quá 70 tuổi lúc hết hạn, khuyến nghị trên màn hình phải hiển thị thế nào?

**Sau:**
> Mình thử người vay sinh 15/5/1990, vay 40 năm, tức hết hạn lúc 76 tuổi, quá mức tối đa 70. Dữ liệu hệ thống trả về là Từ chối. Nhưng màn hình không hiện Từ chối: khung Thẩm định để trống, lại hiện dòng "Nhập đủ thông tin…" dù mình đã nhập đủ.
> **Hỏi:** Anh/chị cho mình hỏi: trường hợp này màn hình phải hiện gì ạ?

## 5. Bảng soát lấy câu hỏi từ đây
Cột "Câu hỏi gửi BA" trong bảng soát chép đúng chữ của **Hỏi** và **Mình đang hiểu** từ file câu hỏi (phần C: **Cần xem**, **Mình đang hiểu**, **Nếu không tìm ra, hỏi BA**). Sửa câu chữ thì sửa ở file câu hỏi trước rồi chép lại; `kiem-tra.py` báo nếu hai nơi lệch nhau.

## 6. Tự kiểm trước khi giao
- Đọc to ba bốn câu. Câu nào nghe lạ thì viết lại.
- Mỗi câu có số liệu hoặc tình huống cụ thể, không chỉ phát biểu chung.
- Phần "Mình đang hiểu" nói rõ chỗ nào là đoán.
- Không có mã nội bộ trong **Hỏi** và **Mình đang hiểu**. Chạy `kiem-tra.py` (nó cảnh báo từ dịch máy và mã nội bộ).
- Số trong ví dụ đã được tính lại bằng script.
- Một người chưa đọc tài liệu gốc vẫn hiểu câu hỏi.
