# Sở thích làm việc của người dùng (LUÔN ĐỌC)
Chi tiết viết tài liệu: `document-preferences.md`.

- Tiếng Việt. Người dùng là **tester**. Nói bằng giọng nói nên có từ lệch ("thiết khai", "sự khoai mạnh") → hỏi lại, không đoán.
- **Từng bước nhỏ rồi ghép**; chưa rõ thì **hỏi, không suy diễn, không bịa**. Chỉ test **functional** (không tự suy diễn bảo mật/hiệu năng).
- **Quyết định 2026-11-19 (người dùng):** muốn bỏ quy tắc này và cho Claude chạy cả ca đăng nhập/nhập sai; đồng ý cho script đọc `.env`; **bỏ qua** (để người dùng tự làm) mọi ca có thể làm chặn hệ thống (LOGIN TC-014…022, 037); **tên hàm/biến/khóa JSON trong code dùng tiếng Anh** (thông báo, tài liệu, trạng thái Đạt/Không đạt vẫn tiếng Việt). **Địa chỉ test từ 2026-11-19: `https://staging-banking-lite.vercel.app/`** (người dùng nêu; địa chỉ cũ `banking-lite.vercel.app` đã bị gỡ, báo `DEPLOYMENT_NOT_FOUND`; staging cũng bản 1.3.0). Quy tắc an toàn của công cụ chỉ cho Claude nhập tài khoản test khi địa chỉ do người dùng nêu và có nhãn môi trường thử (staging…): đúng với địa chỉ này, nên script đọc `.env` để đăng nhập chạy được; mật khẩu chỉ script đọc, Claude không đọc ra, không ghi lại, không nhập sang địa chỉ khác. **Trần nhập sai 9 lần (người dùng chốt 2026-11-19)**, xem `project/tu-dong-hoa-test.md`.
- **Không gõ mật khẩu** (kể cả sai): mình điền ô tên đăng nhập, người dùng gõ. Tài khoản test ở `.env` gốc repo (`.gitignore`, khóa có tiền tố theo dự án); không chép mật khẩu ra nơi khác.
- Ngoại lệ đã chốt 2026-11-18: script `scripts/auto_login.py` đọc `.env` để đăng nhập. **Cập nhật 2026-11-19:** người dùng cho mình chạy luôn script này trên staging (đã chạy, 3 tài khoản thành công); trên địa chỉ không có nhãn thử vẫn không chạy. Chi tiết `project/tu-dong-hoa-test.md`.
- **Nhiều dự án:** máy mới hỏi dự án (ghi `.du-an-hien-tai`); chỉ dùng kiến thức dự án hiện tại: `conventions/nhieu-du-an.md`.
- **An toàn hệ thống đang test:** không khóa hệ thống/tài khoản, không đổi dữ liệu người khác, không kích hoạt giới hạn. Thao tác có thể lặp gây khóa → làm tay thì tối đa **3 lần**, từng lần, rồi **dừng hỏi**; riêng runner tự động: trần **9 lần sai (cộng dồn, đăng nhập đúng không đưa về 0)** do người dùng chốt 2026-11-19, runner đếm và từ chối vượt (đã từng sai vì tin TL-06, xem `project/tu-dong-hoa-test.md`); không tự nâng ngưỡng; dữ liệu giả không phải lý do an toàn; lỡ kích hoạt báo ngay (`pitfalls/dont-trigger-lockouts.md`, đã nhắc hai lần).
- **Đã khám phá rồi thì không khám phá lại** (tốn token, người dùng không đủ chạy lại); chỉ khi người dùng nói rõ feature đã đổi/khám phá lại, và chỉ phần đổi: `project/srs-process.md`.
- **Commit/push chỉ khi người dùng nhờ** (kể cả sau tạo dự án/sửa bộ nhớ).
- Đọc Word/PPT/HTML/PDF chữ/nhiều file → đổi sang Markdown bằng MarkItDown (ra thư mục tạm) rồi đọc; không dùng cho .txt/.md, Excel lớn, PDF scan: `project/cong-cu-markitdown.md`.
- Tài liệu **đọc là hiểu**: tiếng Việt thường, câu đủ ý, thuật ngữ IT đúng; không dùng Given/When/Then, FR/BR, NK#… hay mã nội bộ làm tên cột/nhãn/nội dung chính.
- Kết quả dài → **lưu file trong repo**, chat chỉ tóm tắt + link; không dán cả bảng vào chat.
- Connector/plugin không dùng cho kiểm thử: mặc định tắt, **hỏi trước khi bật** (`connectors-and-plugins.md`).
- Notion lưu hành trình làm việc (để dạy người mới, làm content); có feedback/lỗi lớn mới thì bổ sung nếu được nhờ: `project/notion-journey-page.md`.
- Bộ nhớ này chỉ cho AI đọc; tài liệu cho người đọc (srs/, testing/, evidence/, docs/, báo cáo HTML) giữ nguyên dạng đầy đủ.
