# Nhật ký gốc — feature “Gửi thẩm định” (nút ở bước 6 “Kiểm tra và gửi”)

Cập nhật: 2026-11-17 · Hệ thống: https://banking-lite.vercel.app/ (Phiên bản 1.3.0) · Tài khoản thao tác: **P100001** (Chuyên viên khách hàng, đã đăng nhập sẵn trong trình duyệt tích hợp; mình không nhập mật khẩu).

> Nguyên tắc: chỉ ghi điều đã nhìn thấy. Điều chưa kiểm chứng ghi “❓”. Ảnh: thư mục [screenshots/](screenshots/). Ảnh 10–12 và 14 sao chép từ báo cáo v2 (ảnh gốc 36, 40, 41, 23).

## Dữ liệu test đã tạo hôm nay (được phép từ trước: tạo hồ sơ nháp test)

| Hồ sơ | Cách tạo | Trạng thái cuối |
|---|---|---|
| **HL-000022** | “Tạo từ hồ sơ có sẵn”: khách hàng Tester Mot + tài sản “Căn hộ Test 19, Tòa Mẫu, Phường Thử Nghiệm” (CT 100019); vay 2.000.000.000 VND; Tài chính: lương 64.100.000, chi phí 15.000.000, nợ hiện có 0, người phụ thuộc 1; Yêu cầu định giá → dùng lại kết quả của HL-000019 | **Đã gửi** lúc 12:39 17/11/26, chờ P300001 (mình **chưa** đăng nhập P300001, chưa quyết định) |
| **HL-000023** | “Tạo hồ sơ mới”, không nhập gì | Nháp rỗng (dùng để xem nút bị vô hiệu hóa); thêm 1 hồ sơ nháp rỗng vào danh sách |

## 1. Vị trí và hình dạng của nút (ảnh 03)

- Nút **“Gửi thẩm định”** (nền xanh đậm) nằm ở **cuối** bước 6 “Kiểm tra và gửi”, góc phải, **dưới** các phần “Ước tính trả nợ” và “Thẩm định”, **trên** đường kẻ và nút **“Tiếp tục →”**.
- Hồ sơ HL-000022 trước khi gửi: Trạng thái **Nháp**, Khuyến nghị **Phê duyệt**, các bước 1–5 “Đã xong”, bước 6 “Kiểm tra và gửi” hiện nhãn **“Còn thiếu thông tin”**, bước 7 “Còn thiếu thông tin” (ảnh 01).
- Đầu bước 6 có thông báo nền xanh lá: **“Hồ sơ đã đầy đủ và sẵn sàng gửi.”** (ảnh 02).

## 2. Khi nút bị vô hiệu hóa (HL-000023, hồ sơ rỗng) — ảnh 07, 08

- Nút hiện **mờ**; kiểm tra bằng mã trang: `disabled = true`.
- Thay cho thông báo xanh là khung **“Cần hoàn thiện các mục sau trước khi gửi:”** liệt kê 12 mục, mỗi mục có liên kết **“Đến bước …”**:
  1. A1: họ và tên. → Đến bước Người vay
  2. A1: số CCCD 12 chữ số. → Đến bước Người vay
  3. A1: ngày sinh. → Đến bước Người vay
  4. A1: số di động 10 chữ số. → Đến bước Người vay
  5. A1: tỉnh/thành phố. → Đến bước Người vay
  6. A1: danh tính phải khớp VNeID. → Đến bước Người vay
  7. Ít nhất một người vay phải có thu nhập. → Đến bước Tài chính
  8. **Số tiền vay từ 100.000.000 đến 20.000.000.000 VND.** → Đến bước Khoản vay và tài sản
  9. Tỉnh/thành phố của tài sản. → Đến bước Khoản vay và tài sản
  10. Địa chỉ tài sản. → Đến bước Khoản vay và tài sản
  11. Giá trị khai báo của tài sản. → Đến bước Khoản vay và tài sản
  12. Kết quả định giá đã hoàn thành. → Đến bước Định giá
- Phần “Ước tính trả nợ” hiện: “Nhập khoản vay và tài sản để xem ước tính.”
- Phần “Thẩm định” hiện thông báo xanh dương: “Nhập đủ thông tin người vay, khoản vay, tài sản và thu nhập để xem khuyến nghị.” Các số: LTV “— (LTV tối đa 80,00%)”, lãi suất thẩm định 9,80%, khoản trả mới 0 VND, khoản trả nợ hiện có 0 VND, thu nhập được tính 0 VND, **chi phí được tính 4.500.000 VND**, DSR “—”, thặng dư hằng tháng **-4.500.000 VND**, tuổi cao nhất khi đáo hạn “—”. (Hồ sơ này chưa nhập chi phí sinh hoạt hay người phụ thuộc nào.)
- Thanh bước của hồ sơ rỗng (ghi nhận từ nội dung trang, không có ảnh riêng): bước 1 “Còn thiếu thông tin”, bước 2–5 “Chưa mở”, bước 6 “Còn thiếu thông tin”, bước 7 “Chưa mở”.
- Báo cáo v2 đã ghi trường hợp chỉ thiếu định giá: “Cần hoàn thiện các mục sau trước khi gửi: Kết quả định giá đã hoàn thành. Đến bước Định giá” (HL-000019, ghi nhận trong báo cáo, không có ảnh).

## 3. Khi bấm “Gửi thẩm định” (HL-000022)

| # | Quan sát | Ảnh |
|---|---|---|
| 1 | Bấm nút. Ảnh chụp **ngay sau khi bấm** vẫn thấy trang nguyên trạng, nút vẫn hiện (ứng dụng phản hồi chậm vài giây) | 13 |
| 2 | Sau khoảng 4 giây: nút **biến mất**, thay bằng dòng chữ **“Đã gửi”** ở góc trái dưới; “Tiếp tục →” vẫn còn | 04 |
| 3 | Đầu trang: Trạng thái **Đã gửi**; thông báo **“Hồ sơ đã gửi và bị khóa trong khi chuyên viên thẩm định ra quyết định.”**; bước 6 “Đã xong” ✓; bước 7 “Quyết định tín dụng — Đang chờ xử lý”; Khuyến nghị vẫn “Phê duyệt” | 05 |
| 4 | Bước 7 (P100001 xem): hiện **Thẩm định** chính thức (Phê duyệt, LTV 50,00%, lãi thẩm định 9,80%, DSR 38,48%, thặng dư 24.433.333 VND, lý do “Đáp ứng mọi quy tắc tín dụng.”) và **Báo cáo tín dụng CIC: “A1: nhóm nợ 1, trả nợ 0 VND”**. P100001 không có form quyết định | 09 |
| 5 | Lịch sử có thêm (mới nhất ở trên): 12:39 “Gửi thẩm định · P100001 — Phê duyệt”; 12:39 “Nhận báo cáo CIC · P100001” | 06 |

Lịch sử đầy đủ của HL-000022 (ảnh 06), mới nhất trước: Gửi thẩm định — Phê duyệt (12:39) · Nhận báo cáo CIC (12:39) · Dùng lại kết quả định giá gần đây (12:38) · Lưu thông tin — “Người vay, Khoản vay và tài sản” (12:38) · Lưu thông tin — “Người vay, Khoản vay và tài sản” (12:38) · Kiểm tra danh tính với VNeID — “A1: VNeID: khớp” (12:37) · Tạo hồ sơ (12:37). Hai dòng “Lưu thông tin” ứng với 2 lần mình bấm “Lưu và tiếp tục” ở bước Khoản vay và bước Tài chính.

## 4. Gửi trong các tình huống đã làm ở báo cáo v2 (HL-000021, ghi nhận từ v2)

- Vay 3,4 tỷ → LTV 85%, Khuyến nghị **Từ chối**: nút “Gửi thẩm định” **không bị vô hiệu hóa**, hồ sơ gửi được (ảnh 10 chỉ chụp đầu trang; nút không có ảnh — **ghi nhận trong báo cáo**). P300001 sau đó thấy “Thẩm định: Từ chối”.
- Hồ sơ **Bị trả lại**: banner vàng ghi chú, hồ sơ mở khóa (ảnh 11). Sửa vay xuống 2 tỷ, Lưu, bấm “Gửi thẩm định” lần nữa → Đã gửi, banner trả lại biến mất, Khuyến nghị đổi thành Phê duyệt (ảnh 12). Không cần định giá lại.
- Giữa lúc sửa và gửi lại, ô Khuyến nghị ở đầu trang vẫn hiện “Từ chối” (ghi nhận trong báo cáo, không có ảnh).

## 5. Tài khoản khác

- **P200001**: không có nút “Gửi thẩm định” (bước Kiểm tra và gửi chỉ có “Tiếp tục →”), banner “Bạn được xem nhưng không được sửa hồ sơ này.” (ảnh 14, từ v2).
- **P300001**: ❓ chưa kiểm tra riêng có/không nút này.
- **P100002**: ❓ chưa đăng nhập.

## 6. Chưa thử

- Gửi khi VNeID “Thông tin không khớp / Không tìm thấy” (điều kiện “danh tính phải khớp VNeID” có trong danh sách mục còn thiếu, nhưng chưa tái hiện trường hợp không khớp).
- Số tiền vay đúng biên 100.000.000 / 20.000.000.000, dưới và trên biên.
- Bấm “Gửi thẩm định” hai lần liên tiếp, hoặc khi mất mạng.
- Hành vi khi CIC trả nhóm nợ xấu ngay lúc gửi (dữ liệu có sẵn HL-000012 chỉ xem được ở trang Tích hợp: CIC nhóm nợ 4 → hồ sơ Bị từ chối).
- Giao diện English của nút và danh sách mục còn thiếu.
- Nút có sẵn với P300001 / P100002 (xem mục 5).

## 7. Điểm cần làm rõ (chưa kết luận lỗi hay thiết kế)

- Nhãn bước 6 “Còn thiếu thông tin” trong khi thông báo ghi “Hồ sơ đã đầy đủ và sẵn sàng gửi.” (ảnh 01, 02).
- Không thấy chỉ báo “đang gửi” trong ảnh chụp ngay sau khi bấm; phản hồi chậm vài giây (ảnh 13, 04).
- “Chi phí được tính 4.500.000 VND” khi chưa nhập chi phí sinh hoạt/người phụ thuộc (ảnh 08) — quy tắc nào cho ra con số này?
- Giới hạn số tiền vay 100 triệu – 20 tỷ: chỉ thấy trong danh sách mục còn thiếu, chưa thấy ở bước Khoản vay.
- Hồ sơ khuyến nghị Từ chối vẫn gửi được (đã nêu ở M-03 báo cáo v2).
- Lịch sử ghi hai dòng “Lưu thông tin” cùng nhãn “Người vay, Khoản vay và tài sản” dù mình lưu hai bước khác nhau (ảnh 06).
- Tạo thêm hồ sơ nháp rỗng mỗi khi bấm “Tạo hồ sơ mới” (HL-000023) — vấn đề M-05 của báo cáo v2.
