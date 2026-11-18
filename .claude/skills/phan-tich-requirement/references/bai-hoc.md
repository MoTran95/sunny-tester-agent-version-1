# Bài học và bẫy đã gặp (lần làm thật trên `RECO`)

1. **Làm quá việc được giao.** Mình dựng checklist 62 test case, ưu tiên, lý do viết riêng khi người dùng chỉ cần phân tích và câu hỏi cho BA. Người dùng phải chặn lại. → Dừng đúng chỗ: bảng soát và câu hỏi.
2. **Bảng quá cô đọng, nhiều mã nội bộ.** Dòng kiểu "Thiếu (Dữ liệu)", "KN-02", "thông báo M01" không ai hiểu. → Mỗi dòng có cột Tình huống, nội dung bằng câu đủ ý, chép nội dung thông báo thay vì mã.
3. **Câu chữ như dịch máy.** Trộn nhãn gốc của hệ thống với từ tự đặt, câu dài, xưng hô lẫn. → Một từ một khái niệm, câu ngắn, xưng "mình", gọi BA "anh/chị"; xem `viet-cau-hoi-de-doc.md`.
4. **Hai nơi chứa cùng một câu hỏi.** Người dùng phải kiểm hai chỗ. → Một nguồn: viết ở file câu hỏi, bảng soát chép lại, script kiểm khớp.
5. **Escape `|` cả dòng làm hỏng bảng.** Escape cả dòng thì các dấu ngăn cột cũng bị escape và bảng không hiện. → Escape **từng ô**. Sau khi sinh file luôn chạy script đếm số cột từng dòng.
6. **Heredoc `python -` qua công cụ làm méo regex.** → Viết script ra tệp rồi chạy tệp đó.
7. **Đọc bằng mắt bỏ sót số lệch.** Hai chỗ tài liệu tự lệch chỉ lộ ra khi tính lại bằng script. → Luôn tính lại.
8. **Quyết định người dùng ngược với lời khuyên của mình.** Người dùng chọn làm tròn lên dù mình khuyên giữ làm tròn gần nhất. → Làm theo, nói rõ hệ quả (hệ thống khác ở 11 AC) và đưa lên cho BA xác nhận; đừng tranh luận lại.
9. **Câu trả lời từ người dùng không phải từ BA.** → Ghi nguồn là người dùng, đánh dấu chưa có BA xác nhận, không sửa SRS.
10. **Kết luận "lỗi" quá sớm.** Hệ thống khác quy tắc mới thì chỉ là nghi lỗi nếu BA xác nhận, và có thể chỉ là một nguyên nhân chung.
11. **Kết quả dài dán vào chat khó đọc.** → Lưu file, chat chỉ tóm tắt và link.
12. **Trang sách/Notion lớn.** Kết quả công cụ quá dài bị lưu ra tệp; trích trường `text` bằng script rồi đọc theo khoảng dòng, nói rõ đã đọc phần nào.
13. **Tạm chốt từ ngữ rồi vẫn phải hỏi.** Người dùng chưa nói team dùng từ nào; mặc định của mình có thể sai. → Ghi vào `ba-question-wording.md` và nói rõ đó là mặc định.
