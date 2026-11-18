# Bẫy: tự kích hoạt khóa/giới hạn khi test
Cập nhật: 2026-11-17 · Liên quan: [../user/working-preferences.md](../user/working-preferences.md), [../modules/banking-lite/feature-dang-nhap.md](../modules/banking-lite/feature-dang-nhap.md)

## Chuyện đã xảy ra
Người dùng dặn không làm việc có thể khóa hệ thống. Khi khám phá Đăng nhập, mình vẫn gửi liên tiếp 10 lần đăng nhập sai/không hợp lệ (nhiều biến thể mã nhân viên) → lần thứ 11 bị **chặn 5 phút** (429). Đã có sẵn dấu hiệu nguy cơ: mình từng chủ động hoãn ca “sai mật khẩu nhiều lần” vì sợ khóa.

## Vì sao sai
- Tự nhủ “dùng mã không tồn tại thì không đụng tài khoản thật” — chỉ nghĩ tới khóa theo từng tài khoản, bỏ qua giới hạn theo nguồn kết nối/toàn hệ thống. Không có bằng chứng nào cho thấy hệ thống không giới hạn.
- Không đặt ngưỡng dừng; chạy theo lô (4 lần/lô), không dừng lại sau lô đầu để cân nhắc.
- Không hỏi người dùng trước dù họ đã cảnh báo.

## Cách làm đúng
- Quy tắc cứng đã ghi ở `user/working-preferences.md`: tối đa 3 lần, kiểm tra phản hồi từng lần, dừng và hỏi; lỡ kích hoạt thì báo ngay.
- Muốn biết hệ thống có giới hạn không mà không phải kích hoạt: đọc tệp giao diện công khai (tìm thông báo kiểu `auth.locked`) hoặc hỏi team trước.
- Nếu hệ thống có giới hạn, một lần chờ hết hạn rồi thử lại **một** lần đủ để biết nó có tự hết không.
