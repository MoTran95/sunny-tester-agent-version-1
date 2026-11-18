# Sở thích làm việc của người dùng (LUÔN ĐỌC)
Chi tiết viết tài liệu: `document-preferences.md`.

- Tiếng Việt. Người dùng là **tester**. Nói bằng giọng nói nên có từ lệch ("thiết khai", "sự khoai mạnh") → hỏi lại, không đoán.
- **Từng bước nhỏ rồi ghép**; chưa rõ thì **hỏi, không suy diễn, không bịa**. Chỉ test **functional** (không tự suy diễn bảo mật/hiệu năng).
- **Không gõ mật khẩu** (kể cả sai): mình điền ô tên đăng nhập, người dùng gõ. Tài khoản test ở `.env` gốc repo (`.gitignore`, khóa có tiền tố theo dự án); không chép mật khẩu ra nơi khác.
- **Nhiều dự án:** máy mới hỏi dự án (ghi `.du-an-hien-tai`); chỉ dùng kiến thức dự án hiện tại: `conventions/nhieu-du-an.md`.
- **An toàn hệ thống đang test:** không khóa hệ thống/tài khoản, không đổi dữ liệu người khác, không kích hoạt giới hạn. Thao tác có thể lặp gây khóa → tối đa **3 lần**, từng lần, rồi **dừng hỏi**; không tự nâng ngưỡng; dữ liệu giả không phải lý do an toàn; lỡ kích hoạt báo ngay (`pitfalls/dont-trigger-lockouts.md`, đã nhắc hai lần).
- **Đã khám phá rồi thì không khám phá lại** (tốn token, người dùng không đủ chạy lại); chỉ khi người dùng nói rõ feature đã đổi/khám phá lại, và chỉ phần đổi: `project/srs-process.md`.
- **Commit/push chỉ khi người dùng nhờ** (kể cả sau tạo dự án/sửa bộ nhớ).
- Đọc Word/PPT/HTML/PDF chữ/nhiều file → đổi sang Markdown bằng MarkItDown (ra thư mục tạm) rồi đọc; không dùng cho .txt/.md, Excel lớn, PDF scan: `project/cong-cu-markitdown.md`.
- Tài liệu **đọc là hiểu**: tiếng Việt thường, câu đủ ý, thuật ngữ IT đúng; không dùng Given/When/Then, FR/BR, NK#… hay mã nội bộ làm tên cột/nhãn/nội dung chính.
- Kết quả dài → **lưu file trong repo**, chat chỉ tóm tắt + link; không dán cả bảng vào chat.
- Connector/plugin không dùng cho kiểm thử: mặc định tắt, **hỏi trước khi bật** (`connectors-and-plugins.md`).
- Notion lưu hành trình làm việc (để dạy người mới, làm content); có feedback/lỗi lớn mới thì bổ sung nếu được nhờ: `project/notion-journey-page.md`.
- Bộ nhớ này chỉ cho AI đọc; tài liệu cho người đọc (srs/, testing/, evidence/, docs/, báo cáo HTML) giữ nguyên dạng đầy đủ.
