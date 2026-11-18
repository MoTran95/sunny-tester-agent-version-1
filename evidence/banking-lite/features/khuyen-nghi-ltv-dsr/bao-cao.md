# Khuyến nghị thẩm định xem trước (LTV/DSR) — nhật ký khám phá

Ngày: 2026-11-17 · Hệ thống: https://banking-lite.vercel.app/ · Phiên bản (chân trang): 1.3.0
Khung nhìn: 752×845 (ảnh chụp thu nhỏ 0,6). Ảnh: `screenshots/NN-…jpg`.
Tài khoản: P100001 (Chuyên viên khách hàng) — người dùng tự gõ mật khẩu; mình chỉ điền sẵn mã nhân viên.
Quy tắc: không tự gõ mật khẩu; chỉ thao tác trên hồ sơ nháp do mình tạo; không gửi thẩm định, không đụng hồ sơ của người khác.

**Dữ liệu test mình tạo trong lượt này**
- HL-000024 (id `172396e6-7d1e-4579-9666-c9e057eb8a62`): hồ sơ nháp rỗng, tạo bằng nút `Tạo hồ sơ mới`, bỏ không dùng.
- HL-000025 (id `38d4fdef-efd5-4f59-8c7e-6f29084975b0`): tạo từ khách `Tester Mot` + tài sản `CT 100019`. Trạng thái cuối: Nháp; vay 3.200.000.000; thời hạn 20 năm; mục đích Xây/sửa nhà; Niên kim; ân hạn 12 tháng; giá trị khai báo **4.200.000.000** (đã đổi nhiều lần, xem hàng 27 và 34–38); lương 100.000.000, các ô tài chính khác để trống; chưa yêu cầu định giá.

Cách đọc số liệu: phần lớn hàng dưới đây đọc bằng **công cụ đọc chữ trên trang** (không có ảnh) — mở lại bằng cách làm đúng thao tác ghi ở cột 2 rồi nhìn khung `Thẩm định` ở bước Tài chính.

## 1. Đã thấy (có thao tác thật)
| # | Thao tác | Kết quả quan sát (nguyên văn khi có) | Ảnh |
|---|---|---|---|
| 1 | `Tạo hồ sơ mới` rồi mở thẳng `/applications/<id>/financials` | Hồ sơ HL-000024 (Nháp). Bước Tài chính: `Bước này mở sau khi hoàn thành:` `Người vay` — chưa có form | — (không chụp) |
| 2 | `Tạo từ hồ sơ có sẵn`: tìm khách `Tester Mot`, tìm tài sản `100019`, bấm `Dùng` hai lần, `Tạo hồ sơ` | Hồ sơ HL-000025; bước Người vay `Đã xong` (`VNeID: khớp`); bước Tài chính mở được, ghi `Còn thiếu thông tin` | — |
| 3 | Bước `Khoản vay và tài sản`: số tiền vay `3200000000`, `Lưu` | `Đã lưu.` Ước tính trả nợ: LTV `80,00%`, lãi sau ưu đãi `10,30%`, kỳ trả đầu `29.333.333 VND`. Đầu trang hồ sơ: Số tiền vay `3.200.000.000 VND`, LTV `80,00%`, Khuyến nghị `—` (chưa nhập tài chính) | — |
| 4 | Bước Tài chính, chưa nhập gì | Khung `Thẩm định` không có nhãn khuyến nghị; thông báo xanh `Nhập đủ thông tin người vay, khoản vay, tài sản và thu nhập để xem khuyến nghị.`; `Khoản trả mới theo lãi suất thẩm định` `40.800.000 VND`; `Thu nhập được tính` `0 VND`; `Chi phí được tính` `4.500.000 VND`; `Tỷ lệ trả nợ trên thu nhập (DSR)` `—`; `Thặng dư hằng tháng` `-45.300.000 VND`; `Tuổi cao nhất khi đáo hạn` `56` | 08 |
| 5 | Lương `100000000` (LTV 80%) | Nhãn `Phê duyệt`; dòng `Xem trước: thẩm định chính thức chạy khi gửi, có dữ liệu CIC.`; DSR `40,80%`; thặng dư `54.700.000 VND`; `Lý do`: `Đáp ứng mọi quy tắc tín dụng.`. Đầu trang Khuyến nghị vẫn `—` (chưa lưu) | 01 |
| 6 | Lương `81600000` | DSR `50,00%` (đúng 50%); nhãn `Phê duyệt`; thặng dư `36.300.000 VND` | — |
| 7 | Lương `81599000` | DSR hiện `50,00%` (giá trị thật khoảng 50,0006%); nhãn `Phê duyệt` | — |
| 8 | Lương `81000000` | DSR `50,37%`; nhãn `Chuyển cấp trên`; lý do `Chuyển cấp trên: DSR 50,37% vượt 50%; chuyển cấp trên xem xét.` | 02 |
| 9 | Lương `75000000` (nợ hiện có trống) | DSR `54,40%`; `Chuyển cấp trên`; lý do `Chuyển cấp trên: DSR 54,4% vượt 50%; chuyển cấp trên xem xét.` | — |
| 10 | Lương `58285714` | DSR `70,00%`; `Chuyển cấp trên`; lý do `Chuyển cấp trên: DSR 70% vượt 50%; chuyển cấp trên xem xét.` | — |
| 11 | Lương `58000000` | DSR `70,34%`; nhãn `Từ chối`; lý do `Từ chối: DSR 70,34% vượt mức tối đa 70%.`; thặng dư `12.700.000 VND` | — |
| 12 | Lương `50000000` + Thu nhập cho thuê `50000000` | `Thu nhập được tính` `85.000.000 VND` (50 tr + 70% × 50 tr); DSR `48,00%`; `Phê duyệt`. Dưới ô cho thuê có dòng `Tính 70% thu nhập cho thuê vào khả năng trả nợ.` | 03 |
| 13 | Lương `100000000`, Chi phí sinh hoạt `10000000` (số người phụ thuộc trống) | `Chi phí được tính` `10.000.000 VND`; thặng dư `49.200.000 VND`; DSR `40,80%` | — |
| 14 | Thêm Khoản trả nợ hiện có `5000000` | `Khoản trả nợ hiện có` `5.000.000 VND`; DSR `45,80%` (= (40.800.000 + 5.000.000) / 100.000.000); thặng dư `44.200.000 VND` | — |
| 15 | Số người phụ thuộc `2`, Chi phí `1000000` | `Chi phí được tính` `8.500.000 VND` (không phải 1.000.000) | — |
| 16 | Xóa Chi phí; người phụ thuộc `2` rồi `5` | `Chi phí được tính` `8.500.000` rồi `14.500.000 VND`. (Với người phụ thuộc trống: `4.500.000`.) DSR không đổi | — |
| 17 | `Lưu` ở bước Tài chính (lương 100 tr, nợ 5 tr, phụ thuộc 5) | Phản hồi chậm vài giây (4 giây sau chưa đổi). Sau đó đầu trang Khuyến nghị đổi từ `—` sang `Phê duyệt`; bước Tài chính `Đã xong`. Mở lại bước Tài chính sau khi lưu: các ô vẫn giữ giá trị (đọc ô: `100000000`, trống, trống, `5000000`, `5`) | 04 |
| 18 | Bước Khoản vay: số tiền `3200100000`, `Lưu` | Đầu trang LTV `80,00%`; Khuyến nghị `Phê duyệt` (LTV thật khoảng 80,0025%) | — |
| 19 | Số tiền `3200400000`, `Lưu` | LTV `80,01%`; Khuyến nghị `Từ chối` | — |
| 20 | Số tiền `3240000000`, `Lưu` | LTV `81,00%`; Khuyến nghị `Từ chối`; lý do trong khung Tài chính: `Từ chối: LTV 81% vượt mức tối đa 80%.` | 05 |
| 21 | LTV 81% + lương `60000000` (chưa lưu) | Nhãn `Từ chối`, danh sách 3 lý do: `Từ chối: LTV 81% vượt mức tối đa 80%.` · `Từ chối: DSR 77,18% vượt mức tối đa 70%.` · `Từ chối: Thặng dư hằng tháng -810.000 VND thấp hơn 3.000.000 VND.` (DSR hiện 77,18%, thặng dư `-810.000 VND`) | 06 |
| 22 | Đưa số tiền vay về `3200000000`; lương `100000000`; Chi phí `56200000` / `56200001` / `58000000` | Thặng dư `3.000.000 VND` → `Phê duyệt`; `2.999.999 VND` → `Từ chối`, lý do `Từ chối: Thặng dư hằng tháng 2.999.999 VND thấp hơn 3.000.000 VND.`; `1.200.000 VND` → `Từ chối` | 07 |
| 23 | Ô lương: điền `abc`, rồi `-5000000`, rồi để trống (điền bằng công cụ) | `abc` → ô trống (chữ bị bỏ); `-5000000` → ô giữ `5000000` (dấu trừ bị bỏ; DSR `816,00%`, hai lý do Từ chối); để trống → quay về thông báo `Nhập đủ thông tin…` | 08 |
| 24 | `Lưu` khi mọi ô tài chính trống | `Đã lưu.`; đầu trang Khuyến nghị về `—` | — |
| 25 | Bước Khoản vay: Thời hạn `40` năm, `Lưu`; mở lại bước Tài chính (lương 100 tr) | `Tuổi cao nhất khi đáo hạn` `76`; khung `Thẩm định` **không** có nhãn, hiện lại thông báo `Nhập đủ thông tin…`; đầu trang Khuyến nghị `—`; chân bước `Lãi suất` ghi `Chưa mở`. Nhưng `GET /api/applications/<id>` trả `assessment.recommendation = "DECLINE"` với lý do `assessment.ageAtMaturity` (`age` 76, `max` 70) | 09 |
| 26 | Thời hạn `35` rồi `34` năm, `Lưu`, đọc `GET /api/applications/<id>` | 35 năm: `DECLINE`, `ageAtMaturity` (age 71, max 70). 34 năm: `APPROVE`, `maxAgeAtMaturity` 70, không có lý do. Quay lại 20 năm: `APPROVE`, tuổi 56 | — |
| 27 | Giá trị khai báo (cùng bước Khoản vay) `10`, `8`, `6`, `5`, `4`, `3` tỷ với số tiền vay 3,2 tỷ, đọc `assessment.metrics` | LTV / lãi suất thẩm định: 32% / 9,80%; 40% / 9,80%; 53,33% / 9,90%; 64% / 10,05%; 80% / 10,30%; 106,67% / 10,30% (kèm `Từ chối`, lý do `ltvAboveMax`). Đầu trang Khuyến nghị theo đó: 64% `Phê duyệt`, 106,67% `Từ chối` | — |
| 28 | Lương `75000000` rồi chưa lưu (đầu trang đang `Phê duyệt` từ lần lưu trước) | Khung `Thẩm định` đã `Chuyển cấp trên` nhưng đầu trang vẫn `Phê duyệt` cho tới khi bấm `Lưu` (cũng thấy ở hàng 5 và hàng 8) | — |
| 29 | Bấm `English`, mở bước Tài chính, lương `75000000` | Nhãn: `Assessment: Refer`, `Loan-to-value` `64.00% (Maximum LTV 80.00%)`, `Assessment rate`, `New repayment at assessment rate`, `Assessed income`, `Debt service ratio` `53.51%`, `Monthly surplus`, `Oldest age at maturity`, `Reasons`; lý do `Refer: DSR 53.51% is above 50%; refer to a senior assessor.`; số viết `40,133,333 VND`; đầu trang `Recommendation` `Approve`. Sau đó bấm lại `Tiếng Việt` | 10 |
| 30 | Tải tệp giao diện `/assets/main.99595f2e.js`, tìm chuỗi `assessment.` và `recommendation.` | Có 7 mã lý do: `ltvAboveMax`, `dsrAboveMax`, `dsrAboveApprove`, `surplusBelowBuffer`, `ageAtMaturity`, `valuationShortfall`, `cicDebtGroup`, kèm câu tiếng Việt và English (xem SRS mục 4.2). Nhãn khuyến nghị: `APPROVE`=`Phê duyệt`/`Approve`, `REFER`=`Chuyển cấp trên`/`Refer`, `DECLINE`=`Từ chối`/`Decline`. Cũng có câu của bước quyết định: `Không thể phê duyệt hồ sơ được khuyến nghị từ chối.` và `Ghi rõ lý do phê duyệt hồ sơ được khuyến nghị chuyển cấp trên.` | — |
| 31 | `GET /api/settings` | `{"release":"1.3.0","settings":{}}` — không chứa ngưỡng nào | — |
| 32 | Bước `Định giá` của HL-000025: bấm `Yêu cầu định giá` (định dùng lại kết quả định giá 4 tỷ của cùng tài sản) | **Không thực hiện được**: thao tác bị hệ thống chặn (từ chối quyền), mình không làm đường vòng. Trang chỉ hiện `Trạng thái` `Chưa yêu cầu`, giá trị khai báo `5.000.000.000 VND` | — |

| 33 | Bước Tài chính (chưa lưu): Số người phụ thuộc `20`; rồi lương `99999999999999` | Người phụ thuộc 20: `Chi phí được tính` `44.500.000 VND` (= 4.500.000 + 2.000.000 × 20). Lương 99.999.999.999.999: `Thu nhập được tính` `99.999.999.999.999 VND`, DSR `0,00%`, thặng dư `99.999.915.366.666 VND`, `Phê duyệt` — không báo lỗi. Sau đó đặt lại lương 100 tr, xóa người phụ thuộc (chưa lưu) | — |
| 34 | Bước Khoản vay: `Phương thức trả nợ` đổi sang `Niên kim (số tiền trả đều)`, `Lưu`, đọc `GET /api/applications/<id>` | `assessment.metrics.newRepayment` `30986775` (lãi suất thẩm định 10,05%, vay 3,2 tỷ, 20 năm; lúc `Gốc đều` là `40133333`); DSR `30,99%`; thặng dư `64513225`; `Phê duyệt`. Đầu trang `Kỳ trả đầu tiên` `22.925.794 VND` | — |
| 35 | `Thời gian ân hạn (tháng)` `12` (đang Niên kim), `Lưu`, đọc API | `newRepayment` `31504846` (cao hơn 30.986.775 khi không ân hạn), DSR `31,5%`, `APPROVE` | — |
| 36 | Bước Khoản vay: `Sản phẩm` đổi sang `Vay mua nhà, cố định 7,80% trong 36 tháng`, `Lưu`, đọc API (LTV 64%, Niên kim, ân hạn 12) | `assessmentRate` `9.55` (sản phẩm 12 tháng cùng LTV 64%: `10.05`); `newRepayment` `30465933`; DSR `30,47%`; `APPROVE` | — |
| 37 | `Mục đích` đổi từ `Mua nhà` sang `Xây/sửa nhà`, `Lưu`, đọc API | `maxLtv` **70** (Mua nhà: 80); `productCode` quay về `HL_PROMO12` (sản phẩm 12 tháng) dù trước đó chọn 36 tháng | — |
| 38 | Mục đích `Xây/sửa nhà`, Giá trị khai báo `4200000000` (LTV 76,19%), `Lưu`; mở bước Tài chính | Đầu trang LTV `76,19%`, Khuyến nghị `Từ chối`; khung `Thẩm định`: `76,19% (LTV tối đa 70,00%)`, lãi suất thẩm định `10,30%`, lý do `Từ chối: LTV 76,19% vượt mức tối đa 70%.` | — |

- Hàng 34–38: hồ sơ HL-000025 kết thúc ở trạng thái Xây/sửa nhà · sản phẩm 12 tháng · Niên kim · ân hạn 12 tháng · giá trị khai báo 4,2 tỷ (không đưa về giá trị ban đầu).
- Hàng 27 đo ở **Mua nhà · sản phẩm 12 tháng · Gốc đều · không ân hạn**.
- Cột "Ảnh": số ảnh trong `screenshots/`; `—` là quan sát bằng công cụ đọc chữ trang / API / tệp giao diện, mở lại bằng F12 (Network, Console) hoặc làm lại thao tác.
- Hàng 25, 26, 27 đọc thêm thân phản hồi **GET** `/api/applications/<id>` (đọc được); không đọc thân yêu cầu nào có mật khẩu.

## 2. Cần người dùng làm (vì phải gõ mật khẩu) — kết quả
- A. Đăng nhập P100001: người dùng gõ mật khẩu, báo "xong" → vào được Danh sách việc (thấy HL-000023 trở xuống). Mình xác nhận bằng ảnh.

## 3. Chưa thử / không kiểm tra được
- Quy tắc `valuationShortfall` (định giá thấp hơn giá khai báo) và `cicDebtGroup` (nhóm nợ CIC): chỉ gặp khi đã có kết quả định giá / báo cáo CIC. Yêu cầu định giá bị chặn (hàng 32); cách khác là `Gửi thẩm định`, thao tác này khóa hồ sơ và tự lấy CIC → cần hỏi người dùng trước.
- Tác động của khuyến nghị lên quyết định của P300001 (chỉ thấy câu trong tệp giao diện): cần đăng nhập P300001 (người dùng gõ mật khẩu) và một hồ sơ đã gửi.
- Khung `Thẩm định` với tài khoản P200001/P300001 (họ xem được hồ sơ): cần người dùng gõ mật khẩu từng tài khoản.
- Hồ sơ nhiều người vay (`Thêm người vay`): chưa thử vì bước này nằm ngoài khung Tài chính hiện có và cần nhập thêm danh tính người vay (VNeID chạy khi lưu) — ghi để hỏi người dùng có muốn khám phá không.
- Sản phẩm lãi suất 24 tháng (7,00%): chưa chọn (đã thử 12 và 36 tháng). Chưa đo `assessmentRate` ở mục đích Xây/sửa nhà với nhiều mức LTV.
- Khung `Thẩm định` khi tài sản đã có kết quả định giá: cùng lý do với dòng đầu tiên (cần yêu cầu định giá, đang bị chặn).

## 4. Điểm chưa rõ (ứng viên cho mục câu hỏi của SRS)
1. Ngưỡng so sánh dùng số làm tròn 2 chữ số thập phân hay số thật (DSR 50,0006% → Phê duyệt; LTV 80,0025% → Phê duyệt; nhưng thặng dư 2.999.999 → Từ chối).
2. Khi tuổi lúc đáo hạn > 70, máy chủ trả Từ chối nhưng màn hình không hiện khuyến nghị lẫn lý do.
3. Công thức `Chi phí được tính` (4.500.000 + 2.000.000 × số người phụ thuộc, lấy mức lớn hơn khi nhập tay?) — chỉ suy ra từ vài điểm.
4. Quy tắc lãi suất thẩm định theo LTV và theo sản phẩm (12 tháng: 10,05%, 36 tháng: 9,55% cùng LTV 64%); LTV tối đa phụ thuộc mục đích (Mua nhà 80%, Xây/sửa nhà 70%).
5. Đầu trang hồ sơ chỉ cập nhật Khuyến nghị sau khi `Lưu` — chủ ý hay chưa kịp đồng bộ.
6. Ngưỡng 50%, 70%, 3.000.000, tuổi 70, LTV 80% là cố định hay cấu hình (`/api/settings` trống).
7. Khuyến nghị `Từ chối` có chặn P300001 phê duyệt không (câu trong tệp giao diện) — nhật ký cũ chỉ ghi Từ chối thủ công trái khuyến nghị vẫn được.
