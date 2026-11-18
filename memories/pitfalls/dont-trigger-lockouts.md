# Bẫy: tự kích hoạt khóa/giới hạn khi test
Đọc khi: trước thao tác lặp có thể gây khóa/chặn.

- Đã xảy ra (Banking Lite `LOGIN`, 2026-11-17): người dùng dặn không làm việc có thể khóa; mình vẫn gửi liên tiếp 10 lần đăng nhập sai (nhiều biến thể mã nhân viên) → lần 11 bị **chặn 5 phút** (429).
- Sai ở đâu: nghĩ "mã không tồn tại thì không đụng tài khoản thật" (bỏ qua giới hạn theo nguồn/toàn hệ thống; không có bằng chứng hệ thống không giới hạn); không đặt ngưỡng dừng, chạy theo lô 4 lần; không hỏi dù đã được cảnh báo.
- Làm đúng: tối đa **3 lần**, kiểm từng lần, dừng và hỏi; lỡ kích hoạt báo ngay (quy tắc ở `user/working-preferences.md`). Muốn biết có giới hạn không mà không kích hoạt: đọc tệp giao diện công khai (tìm `auth.locked`) hoặc hỏi team. Nếu có giới hạn: chờ hết hạn rồi thử lại **một** lần để biết có tự hết không.
