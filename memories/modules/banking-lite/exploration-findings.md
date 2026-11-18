# Banking Lite — kết quả khám phá
Cập nhật: 2026-11-17 · Liên quan: [project/overview.md](../../project/overview.md)

Báo cáo đầy đủ + ảnh: `evidence/banking-lite/bao-cao-kham-pha.md` và `evidence/banking-lite/screenshots/`. File này chỉ giữ điểm cần nhớ.

- Hệ thống: ứng dụng xử lý **hồ sơ vay mua nhà** (mã `HL-xxxxxx`), 8 bước: Người vay → Khoản vay & tài sản → Tài chính → Định giá → Lãi suất → Kiểm tra & gửi → Quyết định tín dụng → Lịch sử. URL bước: `/applications/<id>/{borrowers,loan,financials,valuation,pricing,review,decision,history}`.
- Tài khoản test: P100001 = Chuyên viên khách hàng (đã xác nhận trên giao diện). P200001 = nhiều khả năng định giá, P300001 = nhiều khả năng phê duyệt (suy từ nhật ký HL-000011, **chưa xác nhận bằng đăng nhập**). Có thêm P100002 (người tạo HL-000012).
- Tích hợp thấy trong nhật ký: VNeID (kiểm tra danh tính), CIC (báo cáo tín dụng), SMS khách hàng (lỗi gửi SMS không hủy quyết định). Chưa biết là giả lập hay thật.
- Số liệu hiển thị: LTV tối đa 80% (**Mua nhà; Xây/sửa nhà là 70%** — xem [feature-khuyen-nghi-ltv-dsr.md](feature-khuyen-nghi-ltv-dsr.md), có cả luật DSR>70, thặng dư ≥3 triệu, tuổi ≤70); thu nhập cho thuê tính 70%; giảm biên độ tối đa 0,5 điểm %.

## Quy tắc/hành vi đã quan sát khi tạo hồ sơ (HL-000019, 2026-11-17)
- "Tạo hồ sơ mới" tạo bản ghi nháp ngay lập tức. Các bước mở dần; bước chưa mở báo "Bước này mở sau khi hoàn thành: …".
- Form lưu được CCCD/SĐT sai định dạng, báo "Đã lưu." không có lỗi; VNeID chỉ chạy khi nhập đủ hợp lệ ("VNeID: khớp").
- Thẩm định xem trước ở bước Tài chính: LTV > 80% → Từ chối; DSR > 50% → Chuyển cấp trên. Lãi sau ưu đãi 9,80% (LTV 50%) vs 10,30% (LTV 85%).
- "Gửi thẩm định" bị khóa đến khi định giá hoàn thành (người định giá, nhiều khả năng P200001, phải làm ở tài khoản của họ).
- Đã làm xong phía P100001 đến "Yêu cầu định giá" cho HL-000019 (id `db5f18e6-7a49-4d61-b307-0a485c8ab20d`); việc tiếp: đăng nhập P200001 hoàn thành định giá → P100001 gửi thẩm định → P300001 quyết định.
- Người dùng xác nhận (2026-11-17): được tạo hồ sơ test; HL-000013…18 không phải của họ nên không dùng lại; tích hợp "chưa setup, tạm bỏ qua". Chưa có tài liệu nghiệp vụ → danh sách câu hỏi cho team ở mục 7 của báo cáo.

## P200001 = Chuyên viên định giá (xác nhận 2026-11-17)
- Không có nút tạo hồ sơ; có tab "Chờ định giá" + "Tất cả hồ sơ". Mở hồ sơ: "Bạn được xem nhưng không được sửa hồ sơ này"; chỉ form Định giá (Giá trị thị trường*, Ghi chú) sửa được; không có nút Gửi thẩm định.
- Form định giá để trống → hiện mã lỗi thô `validation.too_small (marketValue)` (chưa dịch).
- Đã hoàn thành định giá HL-000019 (4 tỷ). Việc tiếp: P100001 gửi thẩm định → P300001 quyết định.

## Gửi thẩm định HL-000019 (2026-11-17)
- Sau khi định giá xong, P100001 bấm "Gửi thẩm định": trạng thái → Đã gửi, hồ sơ bị khóa; hệ thống tự lấy CIC ("A1: nhóm nợ 1, trả nợ 0") và chạy thẩm định chính thức (Phê duyệt). Lịch sử ghi "Nhận báo cáo CIC" + "Gửi thẩm định — Phê duyệt".
- Việc tiếp: đăng nhập P300001 để quyết định HL-000019 (chờ ở bước Quyết định tín dụng).

## P300001 = Chuyên viên thẩm định tín dụng + E2E hoàn tất (2026-11-17)
- Có thêm menu **Tích hợp** (`/integrations`: trạng thái VNeID/CIC/SMS + nhật ký 200 lần gọi, che CCCD/SĐT) và nút **Tải báo cáo (CSV)** (chưa tải, cần người dùng đồng ý trước khi tải file). Tab "Chờ quyết định".
- Form quyết định: 4 ô danh mục kiểm tra + radio Phê duyệt/Từ chối/Trả lại chuyên viên KH + ghi chú. Phê duyệt khi chưa tick đủ → lỗi "Đánh dấu đủ danh mục kiểm tra trước khi phê duyệt."
- HL-000019 đã Phê duyệt → "Không thể thay đổi nữa", SMS phê duyệt "Đã gửi" tới 091****678 (số test mình nhập; chưa biết SMS giả lập hay thật).
- Chưa thử: Từ chối, Trả lại, tải CSV, hủy yêu cầu định giá, thêm người vay, "Tạo từ hồ sơ có sẵn", tìm khách hàng/tài sản có sẵn, English UI.
- Báo cáo v1 hoàn chỉnh ở `evidence/banking-lite/bao-cao-kham-pha.md` (32 ảnh, 28 câu hỏi cho team).

## Vòng thử 2 (2026-11-17): Tạo từ hồ sơ có sẵn
- "Tạo từ hồ sơ có sẵn": tìm khách hàng (CCCD/họ tên) + tài sản (GCN/địa chỉ) → "Dùng" → Tạo hồ sơ. Hồ sơ mới có sẵn người vay (VNeID đã xong) + tài sản; số tiền vay và tài chính để trống.
- Yêu cầu định giá cho tài sản đã định giá trong 90 ngày → hoàn thành ngay "Dùng lại từ hồ sơ HL-xxxxxx", không cần P200001.
- Hồ sơ khuyến nghị Từ chối (LTV 85%) vẫn gửi thẩm định được (nút không khóa).
- Đã gửi: HL-000020 (id `e32cdb49-26da-4d7d-90dc-cb564fcaca36`, LTV 50%, để P300001 thử Từ chối) và HL-000021 (id `9af2ec62-ca19-4968-a780-103c27c56421`, LTV 85%, để thử Trả lại). Chờ P300001 quyết định, rồi P100001 xem hồ sơ bị trả lại.
- Giao diện English: số `2,000,000,000`, ngày `17/11/2026, 07:26`; nhãn đổi hết.

## Nhánh quyết định (P300001, 2026-11-17)
- Phê duyệt: bắt buộc tick đủ 4 mục kiểm tra. Từ chối / Trả lại: bắt buộc ghi chú, KHÔNG cần tick mục kiểm tra. Từ chối thủ công trái khuyến nghị vẫn được.
- Từ chối → "Bị từ chối, không thể thay đổi nữa" + SMS khách. Trả lại → "Bị trả lại" + banner ghi chú, KHÔNG gửi SMS. Phê duyệt → SMS.
- HL-000020 = Bị từ chối (khóa). HL-000021 = bị trả lại → P100001 sửa (hồ sơ mở khóa), lưu, "Gửi thẩm định" lại → Đã gửi, banner trả lại mất, Khuyến nghị cập nhật. Giữa chừng ô Khuyến nghị đầu trang bị cũ (vẫn "Từ chối" dù LTV 50%). HL-000021 hiện **Đã gửi, chờ P300001** (để nguyên).
- Vòng đời đã chạy hết: Nháp → Đã gửi → {Đã phê duyệt | Bị từ chối | Bị trả lại → Đã gửi}.
- Dữ liệu test mình tạo: HL-000019 (Đã phê duyệt), HL-000020 (Bị từ chối), HL-000021 (Đã gửi). Chưa thử: tải CSV, hủy yêu cầu định giá, Thêm người vay, đường SMS lỗi.

## Bẫy khi thao tác bằng browser
- Phần tử ngoài màn hình không hiện trong read_page; cuộn xuống rồi mới đọc. Điền form dùng form_input theo ref; bấm nút ngoài màn hình có thể dùng JS `.click()`.
- Trang tải chậm (hiện "Đang tải…" 3–5 giây): luôn chờ rồi mới đọc/chụp.
- Click link trong danh sách có thể chỉ cuộn trang; dùng URL trực tiếp `/applications/<id>/...` ổn định hơn.
- Ảnh chụp từ browser tự lưu ở thư mục tool-results của phiên; copy sang `evidence/` để giữ lâu dài.
- Claude **không được tự gõ mật khẩu**; người dùng tự đăng nhập từng tài khoản trong pane Browser. `.env` ở gốc repo giữ tài khoản test (đã `.gitignore`), không chép mật khẩu vào bộ nhớ.
