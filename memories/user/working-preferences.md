# Sở thích làm việc của người dùng (cốt lõi, đọc ở mọi yêu cầu)
Cập nhật: 2026-11-18 · Chi tiết về cách viết tài liệu: [document-preferences.md](document-preferences.md)

- Giao tiếp bằng **tiếng Việt**. Người dùng là **tester**.
- Người dùng nói bằng giọng nói nên có từ nghe lệch (“thiết khai”, “sự khoai mạnh”) → hỏi lại nghĩa, không đoán.
- Làm **từng bước nhỏ rồi ghép lại**, không dựng cả quy trình một lúc. Chỗ nào chưa rõ thì **hỏi, không tự suy diễn**, không bịa.
- **Không gõ mật khẩu** (kể cả mật khẩu sai): mình điền sẵn ô tên đăng nhập, người dùng tự gõ, rồi mình đọc kết quả. Tài khoản test nằm trong `.env` ở gốc repo (đã `.gitignore`, khóa có tiền tố theo dự án), không chép mật khẩu ra nơi khác.
- **Nhiều dự án:** máy mới thì hỏi đang làm dự án nào (một lần mỗi máy, ghi ở `.du-an-hien-tai`); chỉ dùng kiến thức của dự án hiện tại, không lẫn sang dự án khác: [../conventions/nhieu-du-an.md](../conventions/nhieu-du-an.md).
- **An toàn trên hệ thống đang test:** không khóa hệ thống/tài khoản, không đổi dữ liệu của người khác, không kích hoạt giới hạn. Thao tác có thể lặp gây khóa → tối đa **3 lần**, kiểm tra từng lần (không chạy lô), rồi **dừng và hỏi**; không tự nâng ngưỡng; dữ liệu giả không có nghĩa là an toàn. Lỡ kích hoạt thì báo ngay. Người dùng đã phải nhắc hai lần: [../pitfalls/dont-trigger-lockouts.md](../pitfalls/dont-trigger-lockouts.md).
- Chỉ test **functional**, không tự suy diễn bảo mật/hiệu năng.
- Tài liệu phải **đọc là hiểu**: tiếng Việt thường, câu đủ ý, thuật ngữ IT đúng ngữ cảnh; không dùng thuật ngữ kiểm thử/viết tắt khó (Given/When/Then, FR/BR, NK#…) hay mã nội bộ làm tên cột, nhãn, nội dung chính.
- Kết quả dài thì **lưu thành file trong repo**, chat chỉ tóm tắt + link, không dán cả bảng vào chat.
- Connector/plugin không dùng cho kiểm thử: mặc định tắt, **hỏi trước khi bật** ([connectors-and-plugins.md](connectors-and-plugins.md)).
- Người dùng lưu hành trình làm việc trên Notion (nhật ký, feedback trước/sau, lỗi + cách giải quyết) để dạy người mới và làm content; khi có feedback/lỗi lớn mới thì bổ sung nếu được nhờ: [../project/notion-journey-page.md](../project/notion-journey-page.md).

**Why:** người dùng muốn ngữ cảnh được giữ bền vững qua các phiên và không bị sót.
**How to apply:** luôn theo quy trình trong `CLAUDE.md`; sở thích cốt lõi mới ghi vào file này, chi tiết về tài liệu ghi vào `document-preferences.md`.
