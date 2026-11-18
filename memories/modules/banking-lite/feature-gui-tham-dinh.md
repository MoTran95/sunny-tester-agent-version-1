# Feature “Gửi thẩm định” — kết quả khám phá
Cập nhật: 2026-11-17 · Liên quan: [exploration-findings.md](exploration-findings.md), [report-v2-html.md](report-v2-html.md), [../../project/skills.md](../../project/skills.md)

Báo cáo đầy đủ: `evidence/banking-lite/features/gui-tham-dinh/gui-tham-dinh.html` (nguồn `_src/`, nhật ký gốc `bao-cao.md`, 14 ảnh). Tạo bằng skill `feature-exploration-report`. Đây là báo cáo feature đầu tiên theo skill.

## Điều học được (chỉ điều đã thấy)
- Nút ở cuối bước 6 “Kiểm tra và gửi”, trên “Tiếp tục →”. **Bật** khi hồ sơ đủ: thông báo xanh “Hồ sơ đã đầy đủ và sẵn sàng gửi.” **Vô hiệu hóa** (`disabled=true`) khi thiếu: khung “Cần hoàn thiện các mục sau trước khi gửi:” gồm tối đa **12 mục**, mỗi mục có liên kết “Đến bước …”.
- Quy tắc mới thấy trong danh sách đó: **số tiền vay 100.000.000 – 20.000.000.000 VND**; “A1: danh tính phải khớp VNeID”; “Ít nhất một người vay phải có thu nhập”; “Kết quả định giá đã hoàn thành”.
- Hồ sơ rỗng: thẩm định hiện “Chi phí được tính 4.500.000 VND” dù chưa nhập (quy tắc ❓).
- Bấm gửi: phản hồi chậm vài giây; sau đó nút biến mất, thay bằng chữ “Đã gửi”; Trạng thái Đã gửi + banner khóa; bước 7 “Đang chờ xử lý”; P100001 thấy Thẩm định chính thức + báo cáo CIC nhưng không có form quyết định. Lịch sử: “Nhận báo cáo CIC” rồi “Gửi thẩm định — Phê duyệt”; VNeID chạy lúc **tạo hồ sơ từ khách hàng có sẵn**.
- Bước 6 vẫn ghi “Còn thiếu thông tin” dù đã “sẵn sàng gửi” (chưa rõ chủ ý). P200001 không có nút.

## Dữ liệu test tạo trong lượt này
- **HL-000022** (id `bf76d6c5-0850-4dc4-91e5-c4105882ed7f`): từ khách Tester Mot + tài sản CT 100019, vay 2 tỷ, **Đã gửi, chờ P300001** (chưa quyết định).
- **HL-000023** (id `796d1e22-74e9-4310-b4eb-e9ab2615fcda`): nháp rỗng, để xem nút bị vô hiệu hóa.

## Việc còn lại
Chưa thử: VNeID không khớp có chặn gửi không, biên số tiền vay, bấm hai lần, CIC nhóm nợ xấu lúc gửi, English UI, nút với P300001/P100002. Chờ người dùng quyết: có đăng nhập P300001 để xử lý HL-000022 và kiểm tra nút của P300001 không.
