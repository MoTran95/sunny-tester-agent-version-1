# Ngữ cảnh Banking Lite (hệ thống đang test)

Đọc file này khi báo cáo là về **các feature của trang web Banking Lite**. Mọi thông tin dưới đây lấy từ lượt khám phá đã làm (nguồn: `evidence/banking-lite/bao-cao-kham-pha.md` và 41 ảnh trong `evidence/banking-lite/screenshots/`). Điều chưa kiểm chứng ghi ❓ — không bổ sung từ suy đoán.

## Hệ thống

- “Banking Lite — Vay mua nhà”: https://banking-lite.vercel.app/ , phiên bản 1.3.0 (ghi ở chân trang), giao diện Tiếng Việt / English.
- Xử lý **hồ sơ vay mua nhà**, mã `HL-xxxxxx`. Đăng nhập bằng **Mã nhân viên** (chữ P + 6 chữ số) + **Mật khẩu**.
- **Không tự gõ mật khẩu**: người dùng tự đăng nhập từng tài khoản trong cửa sổ trình duyệt. Mật khẩu test nằm ở `.env` ở gốc repo (đã `.gitignore`) — không chép vào báo cáo/bộ nhớ/chat.
- Tích hợp bên thứ ba đã thấy: VNeID, CIC, Cổng SMS (thật hay mô phỏng ❓ — xem M-06 trong báo cáo v2).
- Dữ liệu test do mình tạo: HL-000019 (Đã phê duyệt), HL-000020 (Bị từ chối), HL-000021 (Đã gửi, chờ P300001), **HL-000022 (Đã gửi 12:39 17/11/26, chờ P300001)**, **HL-000023 (nháp rỗng)**. HL-000013…018 không phải do người dùng tạo → không dùng lại.
- Trình duyệt tích hợp có thể **đã đăng nhập sẵn P100001** từ phiên trước (đã gặp 2026-11-17) — mở trang xem trước, đừng bắt người dùng đăng nhập lại nếu chưa cần. Đặt khung nhìn 606×845 để ảnh cùng kích thước với bộ ảnh cũ.

## Tài khoản

| Mã | Vai trò hiển thị trên giao diện | Đã đăng nhập |
|---|---|---|
| P100001 | Chuyên viên khách hàng | ✅ |
| P200001 | Chuyên viên định giá | ✅ |
| P300001 | Chuyên viên thẩm định tín dụng | ✅ |
| P100002 | ❓ chưa biết (chỉ thấy ở cột “Người tạo” của HL-000012) | ❌ |

## Bản đồ feature và độ phủ hiện tại

“Báo cáo v2” = `evidence/banking-lite/bao-cao-kham-pha-v2.html`. Chia feature theo **chức năng người dùng thấy trên giao diện**; mục “Còn thiếu” liệt kê điều chưa kiểm chứng.

| Feature | Tài khoản | Đã khám phá (ảnh) | Còn thiếu / chưa thử |
|---|---|---|---|
| Đăng nhập, chuyển ngôn ngữ | cả 3 | 01, 33 (English) + **bổ sung 2026-11-17** `evidence/banking-lite/features/dang-nhap/` (10 ảnh: đăng xuất, để trống, ID sai định dạng, sai mật khẩu, ID không tồn tại, link sâu, đăng nhập đúng) | Sai mật khẩu nhiều lần (khóa?), hết hạn phiên, chữ P thường, hai tab, P100002, định dạng số/ngày giữa 2 ngôn ngữ ❓ |
| Danh sách việc (tab, bảng) | cả 3 | 02, 19, 27 | Tab “Tất cả hồ sơ” của P100002; phân quyền xem hồ sơ người khác ❓ |
| Tạo hồ sơ mới | P100001 | 12, 13 | Hồ sơ nháp rỗng tồn đọng (M-05) |
| Tạo từ hồ sơ có sẵn (tìm khách hàng/tài sản) | P100001 | 34, 35 | Nguồn dữ liệu tìm kiếm; dữ liệu nào được sao chép ❓ |
| Người vay + VNeID | P100001 | 11, 14 | **Thêm người vay** (chưa bấm); VNeID “không khớp / không tìm thấy” |
| Khoản vay và tài sản | P100001 | 15 (05) | Giới hạn giá trị, thời hạn, ân hạn ❓ |
| Tài chính + Thẩm định xem trước | P100001 | 16 | Ngưỡng/quy tắc khác ngoài LTV > 80% và DSR > 50% ❓ |
| Định giá (yêu cầu / hoàn thành / dùng lại) | P100001, P200001 | 17, 18, 20, 22, 35 | **Hủy yêu cầu định giá**; giá thị trường lệch giá khai báo; giới hạn giá trị thị trường ❓ |
| Lãi suất (so sánh sản phẩm, giảm biên độ) | P100001 | 07 (chỉ đọc) | **Đổi “Giảm biên độ”, chọn sản phẩm khác** |
| Kiểm tra và gửi (Gửi thẩm định) | P100001 | **Đã có báo cáo riêng** `evidence/banking-lite/features/gui-tham-dinh/` (14 ảnh: nút bật/vô hiệu hóa, danh sách 12 mục còn thiếu, sau khi gửi, Lịch sử) | Chưa thử: VNeID không khớp, biên số tiền vay 100tr–20 tỷ, bấm hai lần, CIC nhóm nợ xấu lúc gửi, English UI, nút với P300001/P100002 |
| Hồ sơ bị trả lại → sửa → gửi lại | P100001 | 40, 41 | Ảnh khoảnh khắc “Khuyến nghị cũ” (M-04) |
| Quyết định tín dụng (Phê duyệt / Từ chối / Trả lại) | P300001 | 29, 30, 31, 37, 38, 39 | Phê duyệt trái khuyến nghị Từ chối; Phê duyệt với ghi chú trống; mở lại hồ sơ Từ chối ❓ |
| Lịch sử (nhật ký thao tác) | cả 3 | 10, 26, 32 | Giữ bao lâu, ghi những sự kiện nào ❓ |
| Tích hợp (trạng thái + nhật ký gọi) | P300001 | 28 | Nút “Làm mới”; lọc theo hệ thống; đường SMS gửi lỗi |
| Tải báo cáo (CSV) | P300001 | 27 (chỉ thấy nút) | **Chưa bấm — cần người dùng đồng ý tải file** |
| Phân quyền theo vai trò | cả 3 | bảng “Ai làm được gì” (báo cáo v2 mục 3) | Các ô ❓ của P300001; truy cập thẳng link bước khi chưa đủ quyền |

## Khi làm báo cáo cho **một feature** (thay vì cả hệ thống)

- Vị trí: `evidence/banking-lite/features/<ten-feature>/` gồm `bao-cao.md` (nhật ký gốc), `screenshots/`, `_src/<ten>.src.html`, `<ten>.html`. Ảnh đánh số lại từ 01 trong thư mục của feature.
- Rút gọn 7 mục cho vừa feature: mục 1 chỉ giải thích phần liên quan; mục 3 chỉ tài khoản chạm tới feature; mục 4 chỉ luồng đi qua feature. Vẫn giữ mục 5–7 đầy đủ.
- **Dùng lại, đừng chép lại**: thuật ngữ, thông báo nguyên văn, số ảnh đã có trong báo cáo v2 — tham chiếu bằng “xem báo cáo v2, ảnh NN” hoặc copy ảnh sang thư mục feature. Không viết thông tin mới khi chưa khám phá.
- Trước khi khám phá thêm: kiểm tra cột “Còn thiếu” ở bảng trên; nếu cần tạo dữ liệu test mới hoặc tải CSV, hỏi người dùng trước.
- Sau khi xong: cập nhật cột “Đã khám phá / Còn thiếu” trong bảng này và `memories/modules/banking-lite/`.
