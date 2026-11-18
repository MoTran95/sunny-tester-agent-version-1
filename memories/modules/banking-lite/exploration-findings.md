# Banking Lite — khám phá chung (hồ sơ vay, vai trò, vòng đời)
Đọc khi: làm feature Banking Lite cần biết luồng hồ sơ/vai trò/dữ liệu test. Báo cáo + ảnh: `evidence/banking-lite/bao-cao-kham-pha.md`, `screenshots/` (v1: 32 ảnh, 28 câu hỏi team).

## Hệ thống
- Ứng dụng xử lý hồ sơ vay mua nhà (`HL-xxxxxx`), 8 bước: Người vay → Khoản vay & tài sản → Tài chính → Định giá → Lãi suất → Kiểm tra & gửi → Quyết định tín dụng → Lịch sử. URL `/applications/<id>/{borrowers,loan,financials,valuation,pricing,review,decision,history}`.
- Tích hợp thấy trong nhật ký: VNeID, CIC, SMS (lỗi SMS không hủy quyết định); chưa biết giả lập hay thật. Người dùng: "chưa setup, tạm bỏ qua".
- Số: LTV tối đa 80% Mua nhà / 70% Xây-sửa nhà (luật đầy đủ ở `feature-khuyen-nghi-ltv-dsr.md`); cho thuê tính 70%; giảm biên độ tối đa 0,5 điểm %.

## Vai trò
| Tài khoản | Vai trò | Làm được |
|---|---|---|
| P100001 | Chuyên viên khách hàng | Tạo hồ sơ, yêu cầu định giá, Gửi thẩm định. P100002 cũng có (người tạo HL-000012) |
| P200001 | Chuyên viên định giá | Không có nút tạo hồ sơ; tab "Chờ định giá"/"Tất cả"; hồ sơ chỉ xem trừ form Định giá (Giá trị thị trường*, Ghi chú); trống → `validation.too_small (marketValue)` thô |
| P300001 | Chuyên viên thẩm định tín dụng | Menu **Tích hợp** (`/integrations`: trạng thái + nhật ký 200 lần gọi, che CCCD/SĐT), nút Tải báo cáo (CSV, **chưa tải**, cần người dùng đồng ý), tab "Chờ quyết định", form quyết định |

## Vòng đời hồ sơ (đã chạy hết 2026-11-17)
- Nháp → Đã gửi → {Phê duyệt | Từ chối | Trả lại → Đã gửi lại}. "Tạo hồ sơ mới" tạo nháp ngay; bước chưa mở báo "Bước này mở sau khi hoàn thành: …".
- Form lưu CCCD/SĐT sai định dạng vẫn báo "Đã lưu."; VNeID chỉ chạy khi nhập đủ hợp lệ.
- Thẩm định xem trước ở bước Tài chính (LTV>80 Từ chối; DSR>50 Chuyển cấp trên — bản đủ ở file RECO). Lãi sau ưu đãi 9,80% (LTV 50%) vs 10,30% (LTV 85%).
- **Gửi thẩm định** khóa tới khi định giá xong; Đã gửi → hồ sơ khóa, tự lấy CIC ("A1: nhóm nợ 1, trả nợ 0") và chạy thẩm định chính thức. Hồ sơ khuyến nghị Từ chối (LTV 85%) vẫn gửi được.
- Định giá cho tài sản đã định giá trong 90 ngày → hoàn thành ngay "Dùng lại từ hồ sơ HL-xxxxxx".
- "Tạo từ hồ sơ có sẵn": tìm khách hàng (CCCD/họ tên) + tài sản (GCN/địa chỉ) → "Dùng" → Tạo; có sẵn người vay (VNeID xong) + tài sản; tiền vay/tài chính trống. Nhanh để tới bước Tài chính (Tester Mot + CT 100019).
- Quyết định (P300001): Phê duyệt bắt buộc tick đủ 4 mục kiểm tra ("Đánh dấu đủ danh mục kiểm tra trước khi phê duyệt."); Từ chối/Trả lại bắt buộc ghi chú, không cần tick; Từ chối thủ công trái khuyến nghị vẫn được. Từ chối → khóa + SMS khách; Trả lại → banner ghi chú, **không** SMS; Phê duyệt → SMS. Sau Phê duyệt "Không thể thay đổi nữa".
- Hồ sơ bị trả lại: P100001 sửa, lưu, Gửi lại → banner mất, Khuyến nghị cập nhật; giữa chừng ô Khuyến nghị đầu trang bị cũ (vẫn "Từ chối" dù LTV 50%).
- English UI: `2,000,000,000`, ngày `17/11/2026, 07:26`, nhãn đổi hết.

## Dữ liệu test mình tạo (2026-11-17; HL-000013…18 không phải của người dùng, không dùng)
| Hồ sơ | Trạng thái | id |
|---|---|---|
| HL-000019 | Đã phê duyệt (4 tỷ) | `db5f18e6-7a49-4d61-b307-0a485c8ab20d` |
| HL-000020 | Bị từ chối | `e32cdb49-26da-4d7d-90dc-cb564fcaca36` |
| HL-000021 | Đã gửi, chờ P300001 (để nguyên) | `9af2ec62-ca19-4968-a780-103c27c56421` |
SMS phê duyệt "Đã gửi" tới 091****678 (số test mình nhập). Người dùng xác nhận được tạo hồ sơ test.
- Chưa thử: tải CSV, hủy yêu cầu định giá, Thêm người vay, đường SMS lỗi.

## Bẫy thao tác trình duyệt
- Phần tử ngoài màn hình không hiện trong `read_page`: cuộn rồi đọc. Điền form bằng `form_input` theo ref; nút ngoài màn hình có thể `.click()` bằng JS.
- Trang "Đang tải…" 3–5 giây: luôn chờ rồi đọc/chụp. Click link trong danh sách có thể chỉ cuộn; dùng URL trực tiếp `/applications/<id>/...`.
- Ảnh chụp tự lưu ở thư mục tool-results của phiên: copy sang `evidence/` để giữ.
- Claude **không gõ mật khẩu**; người dùng đăng nhập từng tài khoản. Tài khoản test trong `.env` (đã `.gitignore`); không chép mật khẩu vào bộ nhớ.
