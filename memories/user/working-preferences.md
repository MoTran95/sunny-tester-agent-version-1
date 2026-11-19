# Sở thích làm việc của người dùng (LUÔN ĐỌC)
Chi tiết viết tài liệu: `document-preferences.md`.

- Tiếng Việt. Người dùng là **tester**. Nói bằng giọng nói nên có từ lệch ("thiết khai", "sự khoai mạnh") → hỏi lại, không đoán.
- **Từng bước nhỏ rồi ghép**; chưa rõ thì **hỏi, không suy diễn, không bịa**. Chỉ test **functional** (không tự suy diễn bảo mật/hiệu năng).
- **Cách đặt câu hỏi cho người dùng (dặn 2026-11-19):** viết câu **đủ ngữ cảnh, từ ngữ rõ ràng**, người đọc không cần lật lại chat cũng hiểu mình đang hỏi gì và vì sao; khi có thể thì **đưa các lựa chọn theo logic** (kèm hệ quả ngắn của từng lựa chọn, có một đề xuất) để họ chọn, dùng công cụ hỏi có nút chọn khi có. **Không hỏi lại điều đã có câu trả lời** (trong chat, `memories/`, skill, tài liệu dự án): tra trước, chỉ hỏi cái còn thiếu thật sự.
- **Quyết định 2026-11-19 (người dùng, áp dụng mọi dự án):** Claude được chạy cả ca đăng nhập và nhập sai bằng runner tự động; script đọc `.env`; **bỏ qua** (để người dùng tự làm) mọi ca mà chính bước làm có thể chặn hệ thống; **tên hàm/biến/khóa JSON trong code dùng tiếng Anh** (thông báo, tài liệu, trạng thái Đạt/Không đạt vẫn tiếng Việt). Chỉ nhập tài khoản test vào địa chỉ do người dùng nêu và có nhãn môi trường thử (staging…); mật khẩu chỉ script đọc, Claude không đọc ra, không ghi lại, không nhập sang địa chỉ khác. **Số lần nhập sai cho phép và thời gian chặn không có số mặc định: lấy từ requirement của dự án hoặc hỏi người test** (`project/tu-dong-hoa-test.md`). Địa chỉ test và số liệu riêng từng dự án chỉ nằm ở `modules/<slug>/`.
- **Không gõ mật khẩu** (kể cả sai): mình điền ô tên đăng nhập, người dùng gõ. Tài khoản test ở `.env` gốc repo (`.gitignore`, khóa có tiền tố theo dự án); không chép mật khẩu ra nơi khác.
- Ngoại lệ đã chốt 2026-11-18: script `scripts/auto_login.py` đọc `.env` để đăng nhập; từ 2026-11-19 Claude được chạy luôn script này khi địa chỉ do người dùng nêu và có nhãn thử; địa chỉ không có nhãn thử thì không chạy, nhờ người dùng tự chạy. Chi tiết `project/tu-dong-hoa-test.md`.
- **Nhiều dự án:** máy mới hỏi dự án (ghi `.du-an-hien-tai`); chỉ dùng kiến thức dự án hiện tại: `conventions/nhieu-du-an.md`.
- **An toàn hệ thống đang test:** không khóa hệ thống/tài khoản, không đổi dữ liệu người khác, không kích hoạt giới hạn. Số lần nhập sai cho phép do requirement hoặc người test chốt, **không tự đặt con số**; chưa biết thì hỏi. Thao tác có thể lặp gây khóa → làm tay từng lần rồi dừng hỏi; runner tự động đếm cộng dồn và từ chối vượt trần đã khai (chưa khai thì từ chối mọi lần nhập sai); không tự nâng ngưỡng; dữ liệu giả không phải lý do an toàn; lỡ kích hoạt báo ngay (`pitfalls/dont-trigger-lockouts.md`).
- **Đã khám phá rồi thì không khám phá lại** (tốn token, người dùng không đủ chạy lại); chỉ khi người dùng nói rõ feature đã đổi/khám phá lại, và chỉ phần đổi: `project/srs-process.md`.
- **Commit/push chỉ khi người dùng nhờ** (kể cả sau tạo dự án/sửa bộ nhớ).
- Đọc Word/PPT/HTML/PDF chữ/nhiều file → đổi sang Markdown bằng MarkItDown (ra thư mục tạm) rồi đọc; không dùng cho .txt/.md, Excel lớn, PDF scan: `project/cong-cu-markitdown.md`.
- Tài liệu **đọc là hiểu**: tiếng Việt thường, câu đủ ý, thuật ngữ IT đúng; không dùng Given/When/Then, FR/BR, NK#… hay mã nội bộ làm tên cột/nhãn/nội dung chính.
- Kết quả dài → **lưu file trong repo**, chat chỉ tóm tắt + link; không dán cả bảng vào chat.
- Connector/plugin không dùng cho kiểm thử: mặc định tắt, **hỏi trước khi bật** (`connectors-and-plugins.md`).
- Notion lưu hành trình làm việc (để dạy người mới, làm content); có feedback/lỗi lớn mới thì bổ sung nếu được nhờ: `project/notion-journey-page.md`.
- Bộ nhớ này chỉ cho AI đọc; tài liệu cho người đọc (srs/, testing/, evidence/, docs/, báo cáo HTML) giữ nguyên dạng đầy đủ.
