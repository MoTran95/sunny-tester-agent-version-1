# Banking Lite — Gửi thẩm định
Đọc khi: làm feature nút Gửi thẩm định. Báo cáo: `evidence/banking-lite/features/gui-tham-dinh/gui-tham-dinh.html` (nguồn `_src/`, nhật ký `bao-cao.md`, 14 ảnh), tạo bằng skill `feature-exploration-report`.

- Nút ở cuối bước 6 "Kiểm tra và gửi", trên "Tiếp tục →". **Bật** khi đủ ("Hồ sơ đã đầy đủ và sẵn sàng gửi."); **disabled** khi thiếu: khung "Cần hoàn thiện các mục sau trước khi gửi:" tối đa **12 mục**, mỗi mục có link "Đến bước …".
- Quy tắc thấy trong danh sách: **số tiền vay 100.000.000 – 20.000.000.000 VND**; "A1: danh tính phải khớp VNeID"; "Ít nhất một người vay phải có thu nhập"; "Kết quả định giá đã hoàn thành".
- Hồ sơ rỗng: thẩm định hiện "Chi phí được tính 4.500.000 VND" dù chưa nhập (❓).
- Bấm gửi: chậm vài giây; nút → chữ "Đã gửi"; trạng thái Đã gửi + banner khóa; bước 7 "Đang chờ xử lý"; P100001 thấy Thẩm định chính thức + báo cáo CIC, không có form quyết định. Lịch sử: "Nhận báo cáo CIC" rồi "Gửi thẩm định — Phê duyệt"; VNeID chạy lúc **tạo hồ sơ từ khách hàng có sẵn**.
- Bước 6 vẫn ghi "Còn thiếu thông tin" dù "sẵn sàng gửi" (chưa rõ chủ ý). P200001 không có nút.
- Dữ liệu test: **HL-000022** (`bf76d6c5-0850-4dc4-91e5-c4105882ed7f`, Tester Mot + CT 100019, vay 2 tỷ, Đã gửi, chờ P300001); **HL-000023** (`796d1e22-74e9-4310-b4eb-e9ab2615fcda`, nháp rỗng, xem nút disabled).
- Chưa thử: VNeID không khớp có chặn gửi không, biên số tiền vay, bấm hai lần, CIC nhóm nợ xấu, English UI, nút với P300001/P100002. Chờ người dùng quyết: đăng nhập P300001 xử lý HL-000022 + kiểm nút của P300001.
