# SRS — Khuyến nghị thẩm định xem trước: LTV và DSR (Banking Lite)

| | |
|---|---|
| Mã feature | `RECO` (quy tắc ID: [id-and-source-rules.md](../id-and-source-rules.md)) |
| Phiên bản hệ thống đã quan sát | 1.3.0 (https://banking-lite.vercel.app/) |
| Cập nhật lần cuối | 2026-11-17 |
| Tình trạng | **nháp** — chỉ ghi hành vi quan sát được, chưa xác nhận với team |
| Nhật ký khám phá gốc | [bao-cao.md](../../evidence/banking-lite/features/khuyen-nghi-ltv-dsr/bao-cao.md) (38 hàng, theo thứ tự thời gian) |

## 1. Mục đích, phạm vi, vai trò
- **Mục đích:** khi chuyên viên khách hàng nhập số liệu cho hồ sơ vay mua/xây sửa nhà, hệ thống **tính ngay** một khuyến nghị — `Phê duyệt`, `Chuyển cấp trên` hoặc `Từ chối` — kèm các chỉ số và lý do. Khuyến nghị hiện ở khung **Thẩm định** của bước **Tài chính**, và ở ô **Khuyến nghị** trên đầu trang hồ sơ (sau khi lưu). Đây là bản **xem trước**: dòng chữ trên màn hình nói `thẩm định chính thức chạy khi gửi, có dữ liệu CIC` (`RECO-M03`).
- **Giải thích thuật ngữ cho người mới:**
  - **LTV** (Tỷ lệ cho vay/giá trị): số tiền vay chia giá trị tài sản bảo đảm, tính bằng %.
  - **DSR** (Tỷ lệ trả nợ trên thu nhập): tiền phải trả nợ mỗi tháng chia thu nhập mỗi tháng, tính bằng %.
  - **Thặng dư hằng tháng:** tiền còn lại mỗi tháng sau khi trừ chi phí và các khoản trả nợ.
  - **CIC:** báo cáo tín dụng của khách hàng, hệ thống lấy khi gửi thẩm định chính thức.
- **Ngoài phạm vi / chưa thấy trên màn hình:** thẩm định **chính thức** lúc `Gửi thẩm định` (có CIC, có kết quả định giá); tác động của khuyến nghị lên quyết định của người thẩm định tín dụng; hồ sơ nhiều người vay (xem mục 6.2).
- **Vai trò:**

| Tài khoản | Vai trò hiển thị | Đã thử với feature này |
|---|---|---|
| P100001 | Chuyên viên khách hàng | Tất cả các ca ở mục 3 |
| P200001 | Chuyên viên định giá | Chưa thử (cần người dùng gõ mật khẩu) |
| P300001 | Chuyên viên thẩm định tín dụng | Chưa thử (cần người dùng gõ mật khẩu) |

## 2. Điều kiện tiên quyết
- Đăng nhập P100001 (người dùng gõ mật khẩu; mật khẩu **không** ghi trong tài liệu).
- Có một **hồ sơ nháp** của mình. Bước `Tài chính` chỉ mở **sau khi hoàn thành bước `Người vay`**: hồ sơ vừa tạo bằng `Tạo hồ sơ mới` hiện `Bước này mở sau khi hoàn thành: Người vay` ([E20](#e20)). Cách nhanh nhất: `Tạo từ hồ sơ có sẵn` (chọn một khách hàng và một tài sản) — hồ sơ mới có sẵn người vay (đã qua VNeID) và tài sản.
- Để có khuyến nghị cần đủ: người vay, **số tiền vay và thời hạn** (bước `Khoản vay và tài sản`), **tài sản có giá trị khai báo**, và **thu nhập** (bước `Tài chính`).

## 3. User story và tiêu chí chấp nhận

**Cách đọc các bảng dưới đây.** Mỗi dòng là **một tình huống có thể đem đi test**, đọc từ trái sang phải như một câu chuyện:
1. **Bối cảnh** — hệ thống/người dùng đang ở tình trạng nào *trước khi* làm.
2. **Người dùng làm** — thao tác cụ thể: nhập gì, bấm gì, mở gì.
3. **Hệ thống phản hồi** — điều đã **nhìn thấy** sau thao tác đó. Chữ trong dấu `…` là câu nguyên văn trên màn hình.

Cột cuối ghi nhãn (`đã thấy` = mình đã tự nhìn thấy; `chưa rõ` = còn thiếu/không chắc), bằng chứng (bấm số `E..` để xem ảnh/cách kiểm lại ở mục 6.1) và quy tắc/thông báo liên quan (tra ở mục 4). *(Trong tài liệu kiểm thử, ba cột đầu thường được gọi là Given – When – Then; mỗi dòng gọi là một "tiêu chí chấp nhận", viết tắt AC.)*

**Mọi ví dụ dưới đây dùng cùng một hồ sơ nền** (trừ khi ghi khác): mục đích `Mua nhà`, sản phẩm 12 tháng, trả `Gốc đều`, vay `3.200.000.000 VND`, thời hạn `20` năm, giá trị khai báo `4.000.000.000 VND` (LTV `80,00%`), người vay `Tester Mot` (cao nhất khi đáo hạn `56` tuổi), không có thu nhập cho thuê, nợ hiện có, chi phí hay người phụ thuộc. Khoản trả mới theo lãi suất thẩm định khi đó là `40.800.000 VND` mỗi tháng.

### `RECO-S01` — Biết khuyến nghị và lý do ngay khi nhập thu nhập
**Là** chuyên viên khách hàng, **tôi muốn** thấy ngay khuyến nghị và lý do khi nhập số liệu ở bước Tài chính **để** biết hồ sơ có khả năng được duyệt trước khi gửi.

**Luồng:** (1) mở hồ sơ nháp có người vay, khoản vay, tài sản → (2) vào bước `Tài chính` → (3) nhập `Lương hằng tháng` (và các ô khác nếu có) → (4) khung `Thẩm định` đổi ngay, không cần bấm lưu → (5) bấm `Lưu` để ô `Khuyến nghị` ở đầu trang cập nhật (→ `RECO-S05`); rẽ nhánh: chưa đủ thông tin (→ `RECO-S01-AC01`), vượt ngưỡng (→ `RECO-S01-AC03`, `AC04`, `AC09`).

| ID | Tình huống | Bối cảnh | Người dùng làm | Hệ thống phản hồi | Nhãn · Bằng chứng · Liên quan |
|---|---|---|---|---|---|
| <a id="reco-s01-ac01"></a>`RECO-S01-AC01` | Chưa nhập thu nhập | Hồ sơ nền, bước Tài chính chưa nhập gì | Mở bước `Tài chính` | Khung `Thẩm định` **không có nhãn khuyến nghị** và **không có mục `Lý do`**. Có thông báo xanh `Nhập đủ thông tin người vay, khoản vay, tài sản và thu nhập để xem khuyến nghị.` (`RECO-M01`). Các chỉ số vẫn hiện: LTV `80,00% (LTV tối đa 80,00%)`; khoản trả mới `40.800.000 VND`; thu nhập được tính `0 VND`; chi phí được tính `4.500.000 VND`; DSR `—`; thặng dư `-45.300.000 VND`; tuổi cao nhất khi đáo hạn `56` | đã thấy · [E08](#e08) · Liên quan: `RECO-M01`, `RECO-R10` |
| <a id="reco-s01-ac02"></a>`RECO-S01-AC02` | Đạt mọi quy tắc → Phê duyệt | Hồ sơ nền | Nhập `Lương hằng tháng` = `100000000` | Nhãn `Phê duyệt`. Dòng nhỏ `Xem trước: thẩm định chính thức chạy khi gửi, có dữ liệu CIC.` (`RECO-M03`). DSR `40,80%`; thặng dư `54.700.000 VND`. Mục `Lý do`: `Đáp ứng mọi quy tắc tín dụng.` (`RECO-M02`) | đã thấy · [E01](#e01) · Liên quan: `RECO-M02`, `RECO-M03`, `RECO-R02` |
| <a id="reco-s01-ac03"></a>`RECO-S01-AC03` | DSR trên 50% đến 70% → Chuyển cấp trên | Hồ sơ nền | Nhập lương `81000000` | Nhãn `Chuyển cấp trên`. DSR `50,37%`. Lý do: `Chuyển cấp trên: DSR 50,37% vượt 50%; chuyển cấp trên xem xét.` (`RECO-M06`). Cùng kết quả với lương `75000000` (DSR `54,40%`) | đã thấy · [E02](#e02) [E11](#e11) · Liên quan: `RECO-R02`, `RECO-M06` |
| <a id="reco-s01-ac04"></a>`RECO-S01-AC04` | DSR trên 70% → Từ chối | Hồ sơ nền | Nhập lương `58000000` | Nhãn `Từ chối`. DSR `70,34%`. Lý do: `Từ chối: DSR 70,34% vượt mức tối đa 70%.` (`RECO-M05`). Thặng dư `12.700.000 VND` (không phải lý do) | đã thấy · [E11](#e11) · Liên quan: `RECO-R02`, `RECO-M05` |
| <a id="reco-s01-ac05"></a>`RECO-S01-AC05` | DSR đúng 50,00% vẫn Phê duyệt | Hồ sơ nền | Nhập lương `81600000` | DSR `50,00%`; nhãn `Phê duyệt` (không phải Chuyển cấp trên); thặng dư `36.300.000 VND` | đã thấy · [E11](#e11) · Liên quan: `RECO-R02` |
| <a id="reco-s01-ac06"></a>`RECO-S01-AC06` | DSR đúng 70,00% là Chuyển cấp trên, chưa phải Từ chối | Hồ sơ nền | Nhập lương `58285714` | DSR `70,00%`; nhãn `Chuyển cấp trên`; lý do `Chuyển cấp trên: DSR 70% vượt 50%; chuyển cấp trên xem xét.` | đã thấy · [E11](#e11) · Liên quan: `RECO-R02`, `RECO-M06` |
| <a id="reco-s01-ac07"></a>`RECO-S01-AC07` | DSR thật hơn 50% một chút nhưng hiện 50,00% | Hồ sơ nền | Nhập lương `81599000` (DSR thật khoảng 50,0006%) | DSR hiện `50,00%`; nhãn `Phê duyệt` | chưa rõ (so bằng số làm tròn hay số thật?) · [E11](#e11) · Liên quan: `RECO-Q01`, `RECO-R02` |
| <a id="reco-s01-ac08"></a>`RECO-S01-AC08` | Thặng dư đúng 3.000.000 vẫn đạt | Hồ sơ nền; lương `100000000` | Nhập `Chi phí sinh hoạt hằng tháng` = `56200000` | Thặng dư `3.000.000 VND`; nhãn `Phê duyệt`; `Đáp ứng mọi quy tắc tín dụng.` | đã thấy · [E07](#e07) · Liên quan: `RECO-R03`, `RECO-M02` |
| <a id="reco-s01-ac09"></a>`RECO-S01-AC09` | Thặng dư thiếu 1 đồng → Từ chối | Như AC08 | Đổi chi phí thành `56200001` (rồi thử `58000000`) | Thặng dư `2.999.999 VND`; nhãn `Từ chối`; lý do `Từ chối: Thặng dư hằng tháng 2.999.999 VND thấp hơn 3.000.000 VND.` (`RECO-M07`). Với chi phí `58000000`: thặng dư `1.200.000 VND`, cũng `Từ chối` | đã thấy · [E07](#e07) · Liên quan: `RECO-R03`, `RECO-M07` |
| <a id="reco-s01-ac10"></a>`RECO-S01-AC10` | Nhiều lý do cùng lúc | Vay `3.240.000.000` (LTV 81%); nợ hiện có `5000000`; người phụ thuộc `5` | Nhập lương `60000000` | Nhãn `Từ chối`; mục `Lý do` liệt kê **ba dòng**: `Từ chối: LTV 81% vượt mức tối đa 80%.` · `Từ chối: DSR 77,18% vượt mức tối đa 70%.` · `Từ chối: Thặng dư hằng tháng -810.000 VND thấp hơn 3.000.000 VND.` | đã thấy · [E06](#e06) · Liên quan: `RECO-M04`, `RECO-M05`, `RECO-M07` |

### `RECO-S02` — Biết khoản vay có vượt mức tối đa so với giá trị tài sản không (LTV)
**Là** chuyên viên khách hàng, **tôi muốn** thấy LTV và mức tối đa cho phép **để** chỉnh số tiền vay trước khi gửi.

**Luồng:** (1) bước `Khoản vay và tài sản`: nhập số tiền vay, giá trị khai báo → (2) bấm `Lưu` → (3) đầu trang hồ sơ hiện LTV và Khuyến nghị; bước `Tài chính` hiện `LTV … (LTV tối đa …)`. Giá trị khai báo và số tiền vay cho ra LTV; chưa thử khi tài sản đã được định giá (→ mục 6.2).

| ID | Tình huống | Bối cảnh | Người dùng làm | Hệ thống phản hồi | Nhãn · Bằng chứng · Liên quan |
|---|---|---|---|---|---|
| <a id="reco-s02-ac01"></a>`RECO-S02-AC01` | LTV đúng 80,00% (mua nhà) | Hồ sơ nền, lương `100000000` đã lưu | Xem khung Thẩm định và đầu trang | Khung ghi `80,00% (LTV tối đa 80,00%)`; đầu trang LTV `80,00%`; Khuyến nghị `Phê duyệt` | đã thấy · [E01](#e01) [E13](#e13) · Liên quan: `RECO-R01`, `RECO-R12` |
| <a id="reco-s02-ac02"></a>`RECO-S02-AC02` | LTV thật hơn 80% rất ít nhưng hiện 80,00% | Như AC01 | Đổi số tiền vay thành `3200100000`, bấm `Lưu` | Đầu trang LTV `80,00%`; Khuyến nghị `Phê duyệt` | chưa rõ (so bằng số làm tròn?) · [E13](#e13) · Liên quan: `RECO-Q01`, `RECO-R01` |
| <a id="reco-s02-ac03"></a>`RECO-S02-AC03` | LTV 80,01% → Từ chối | Như AC01 | Đổi số tiền vay thành `3200400000`, bấm `Lưu` | Đầu trang LTV `80,01%`; Khuyến nghị `Từ chối` | đã thấy · [E13](#e13) · Liên quan: `RECO-R01` |
| <a id="reco-s02-ac04"></a>`RECO-S02-AC04` | LTV 81% có lý do | Như AC01 | Đổi số tiền vay thành `3240000000`, bấm `Lưu`, mở bước Tài chính | Đầu trang LTV `81,00%`, Khuyến nghị `Từ chối`. Khung Thẩm định: `81,00% (LTV tối đa 80,00%)`; lý do `Từ chối: LTV 81% vượt mức tối đa 80%.` (`RECO-M04`) | đã thấy · [E05](#e05) [E06](#e06) [E13](#e13) · Liên quan: `RECO-M04` |
| <a id="reco-s02-ac05"></a>`RECO-S02-AC05` | LTV tính theo giá trị khai báo | Vay `3200000000`; tài sản **chưa** có kết quả định giá | Đổi `Giá trị khai báo` lần lượt `5000000000` và `3000000000`, `Lưu` | LTV `64,00%` (Khuyến nghị `Phê duyệt`) rồi `106,67%` (Khuyến nghị `Từ chối`, lý do `ltvAboveMax`) | đã thấy · [E15](#e15) · Liên quan: `RECO-R05` |
| <a id="reco-s02-ac06"></a>`RECO-S02-AC06` | Lãi suất thẩm định đổi theo LTV | Mua nhà, sản phẩm 12 tháng, Gốc đều, vay `3200000000` | Đổi giá trị khai báo `10`, `8`, `6`, `5`, `4` tỷ | LTV → lãi suất thẩm định: `32%` → `9,80%`; `40%` → `9,80%`; `53,33%` → `9,90%`; `64%` → `10,05%`; `80%` → `10,30%` (và `106,67%` → `10,30%`) | đã thấy (số liệu) · chưa rõ (quy tắc) · [E15](#e15) · Liên quan: `RECO-Q04`, `RECO-R09` |
| <a id="reco-s02-ac07"></a>`RECO-S02-AC07` | Xây/sửa nhà có mức tối đa thấp hơn | Hồ sơ nền, đã lưu lương `100000000` | Bước Khoản vay: `Mục đích` = `Xây/sửa nhà`, giá trị khai báo `4200000000` (LTV 76,19%), `Lưu`, mở bước Tài chính | Đầu trang LTV `76,19%`, Khuyến nghị `Từ chối`. Khung: `76,19% (LTV tối đa 70,00%)`; lý do `Từ chối: LTV 76,19% vượt mức tối đa 70%.` Ô `Sản phẩm` tự quay về sản phẩm 12 tháng khi đổi mục đích | đã thấy · [E22](#e22) · Liên quan: `RECO-R01`, `RECO-M04` |

### `RECO-S03` — Thu nhập, chi phí và các khoản trả nợ ảnh hưởng thế nào đến DSR và thặng dư
**Là** chuyên viên khách hàng, **tôi muốn** hiểu số nào được tính vào DSR và thặng dư **để** nhập đúng số liệu của khách.

**Luồng:** (1) nhập 5 ô ở bước `Tài chính`: `Lương hằng tháng`, `Thu nhập cho thuê hằng tháng`, `Chi phí sinh hoạt hằng tháng`, `Khoản trả nợ hiện có hằng tháng`, `Số người phụ thuộc` → (2) khung `Thẩm định` tính lại các dòng `Thu nhập được tính`, `Chi phí được tính`, `Khoản trả nợ hiện có`, `DSR`, `Thặng dư hằng tháng`.

| ID | Tình huống | Bối cảnh | Người dùng làm | Hệ thống phản hồi | Nhãn · Bằng chứng · Liên quan |
|---|---|---|---|---|---|
| <a id="reco-s03-ac01"></a>`RECO-S03-AC01` | DSR và thặng dư cơ bản | Hồ sơ nền | Nhập lương `100000000` | Khoản trả mới `40.800.000 VND`; thu nhập được tính `100.000.000 VND`; chi phí được tính `4.500.000 VND`; DSR `40,80%` (= 40.800.000 / 100.000.000); thặng dư `54.700.000 VND` (= 100.000.000 − 4.500.000 − 40.800.000) | đã thấy · [E01](#e01) · Liên quan: `RECO-R10` |
| <a id="reco-s03-ac02"></a>`RECO-S03-AC02` | Thu nhập cho thuê chỉ tính 70% | Hồ sơ nền | Nhập lương `50000000` và `Thu nhập cho thuê hằng tháng` `50000000` | Thu nhập được tính `85.000.000 VND` (50 triệu + 70% × 50 triệu); DSR `48,00%`; nhãn `Phê duyệt`. Dưới ô cho thuê có dòng `Tính 70% thu nhập cho thuê vào khả năng trả nợ.` | đã thấy · [E03](#e03) · Liên quan: `RECO-R06` |
| <a id="reco-s03-ac03"></a>`RECO-S03-AC03` | Nợ hiện có cộng vào DSR | Lương `100000000`, chi phí `10000000` | Nhập `Khoản trả nợ hiện có hằng tháng` = `5000000` | `Khoản trả nợ hiện có` `5.000.000 VND`; DSR `45,80%` (= (40.800.000 + 5.000.000) / 100.000.000); thặng dư `44.200.000 VND` | đã thấy · [E12](#e12) · Liên quan: `RECO-R10` |
| <a id="reco-s03-ac04"></a>`RECO-S03-AC04` | Chi phí nhập cao hơn mức tối thiểu thì dùng số nhập | Lương `100000000`, người phụ thuộc trống | Nhập chi phí `10000000` | `Chi phí được tính` `10.000.000 VND`; thặng dư `49.200.000 VND` | đã thấy · [E12](#e12) · Liên quan: `RECO-R07` |
| <a id="reco-s03-ac05"></a>`RECO-S03-AC05` | Chi phí để trống có mức mặc định | Lương `100000000` | Để trống ô chi phí và người phụ thuộc | `Chi phí được tính` `4.500.000 VND` | đã thấy · [E08](#e08) [E01](#e01) · Liên quan: `RECO-R07` |
| <a id="reco-s03-ac06"></a>`RECO-S03-AC06` | Người phụ thuộc làm tăng mức chi phí tối thiểu | Lương `100000000` | Nhập `Số người phụ thuộc` = `2`, chi phí `1000000` (rồi để trống chi phí; rồi người phụ thuộc `5`, `20`) | Người phụ thuộc 2: `Chi phí được tính` `8.500.000 VND` dù nhập 1.000.000 hoặc để trống; 5: `14.500.000 VND`; 20: `44.500.000 VND`. DSR không đổi. Nhập chi phí `10000000` + người phụ thuộc 2 thì vẫn `10.000.000 VND` | đã thấy · chưa rõ (công thức: Q03) · [E12](#e12) · Liên quan: `RECO-R07`, `RECO-Q03` |
| <a id="reco-s03-ac07"></a>`RECO-S03-AC07` | Thời hạn vay đổi khoản trả mới | Hồ sơ nền (Gốc đều, LTV 80%, lãi suất thẩm định 10,30%) | Bước Khoản vay: đổi `Thời hạn (năm)` từ `20` thành `40`, `Lưu` | Khoản trả mới theo lãi suất thẩm định giảm từ `40.800.000` xuống `34.133.333 VND`; DSR `34,13%` (lương 100 triệu). Tuổi cao nhất khi đáo hạn tăng lên `76` (→ `RECO-S04`) | đã thấy · [E14](#e14) · Liên quan: `RECO-R08` |
| <a id="reco-s03-ac08"></a>`RECO-S03-AC08` | Phương thức trả nợ đổi khoản trả mới | Vay `3200000000`, 20 năm, LTV 64% (lãi suất thẩm định 10,05%) | Bước Khoản vay: `Phương thức trả nợ` đổi từ `Gốc đều` sang `Niên kim (số tiền trả đều)`, `Lưu` | Khoản trả mới `40.133.333` (Gốc đều) → `30.986.775 VND` (Niên kim); DSR `30,99%`; thặng dư `64.513.225 VND` | đã thấy · [E21](#e21) · Liên quan: `RECO-R08` |
| <a id="reco-s03-ac09"></a>`RECO-S03-AC09` | Thời gian ân hạn đổi khoản trả mới | Như AC08 (đang Niên kim) | Nhập `Thời gian ân hạn (tháng)` = `12`, `Lưu` | Khoản trả mới tăng từ `30.986.775` lên `31.504.846 VND`; DSR `31,5%` | đã thấy · [E21](#e21) · Liên quan: `RECO-R08` |
| <a id="reco-s03-ac10"></a>`RECO-S03-AC10` | Sản phẩm đổi lãi suất thẩm định | Mua nhà, LTV 64%, Niên kim, ân hạn 12 tháng | Chọn sản phẩm `Vay mua nhà, cố định 7,80% trong 36 tháng` thay cho sản phẩm 12 tháng, `Lưu` | Lãi suất thẩm định `9,55%` (sản phẩm 12 tháng: `10,05%`); khoản trả mới `30.465.933 VND`; DSR `30,47%` | đã thấy · chưa rõ (quy tắc: Q04) · [E22](#e22) · Liên quan: `RECO-R09`, `RECO-Q04` |
| <a id="reco-s03-ac11"></a>`RECO-S03-AC11` | Số rất lớn không gây lỗi | Hồ sơ nền | Nhập lương `99999999999999` (chưa lưu) | Thu nhập được tính `99.999.999.999.999 VND`; DSR `0,00%`; thặng dư `99.999.915.366.666 VND`; nhãn `Phê duyệt`; không có thông báo lỗi | đã thấy · [E12](#e12) · Liên quan: `RECO-R10` |

### `RECO-S04` — Bị loại khi người vay quá tuổi lúc đáo hạn
**Là** chuyên viên khách hàng, **tôi muốn** biết thời hạn vay có làm người vay quá tuổi cho phép không **để** chọn thời hạn phù hợp.

**Luồng:** (1) chọn `Thời hạn (năm)` ở bước Khoản vay → (2) bước Tài chính hiện dòng `Tuổi cao nhất khi đáo hạn` → (3) nếu vượt mức tối đa thì máy chủ trả `Từ chối` (`RECO-S04-AC03`), nhưng màn hình **không hiện** khuyến nghị (`RECO-S04-AC04`).

| ID | Tình huống | Bối cảnh | Người dùng làm | Hệ thống phản hồi | Nhãn · Bằng chứng · Liên quan |
|---|---|---|---|---|---|
| <a id="reco-s04-ac01"></a>`RECO-S04-AC01` | Thời hạn 20 năm | Hồ sơ nền (kết quả tìm khách ghi ngày sinh `15/5/90`) | Mở bước Tài chính | `Tuổi cao nhất khi đáo hạn` `56` | đã thấy · [E08](#e08) [E14](#e14) · Liên quan: `RECO-R04` |
| <a id="reco-s04-ac02"></a>`RECO-S04-AC02` | Thời hạn 34 năm vẫn đạt | Hồ sơ nền, lương `100000000` | Đổi `Thời hạn (năm)` thành `34`, `Lưu`; đọc phản hồi `GET /api/applications/<id>` | `assessment.recommendation` = `APPROVE`; `maxAgeAtMaturity` = `70`; `reasons` rỗng | đã thấy (qua API) · [E14](#e14) · Liên quan: `RECO-R04` |
| <a id="reco-s04-ac03"></a>`RECO-S04-AC03` | Thời hạn 35 năm bị từ chối | Như AC02 | Đổi thời hạn thành `35`, `Lưu`; đọc API | `recommendation` = `DECLINE`; lý do `assessment.ageAtMaturity` với `age` 71, `max` 70 (nghĩa: `Có người vay 71 tuổi khi đáo hạn; tối đa 70.`, `RECO-M08`) | đã thấy (qua API) · [E14](#e14) · Liên quan: `RECO-R04`, `RECO-M08` |
| <a id="reco-s04-ac04"></a>`RECO-S04-AC04` | Quá tuổi nhưng màn hình không báo | Như AC02 | Đổi thời hạn thành `40`, `Lưu`, mở bước Tài chính | `Tuổi cao nhất khi đáo hạn` `76`. Khung Thẩm định **không có nhãn khuyến nghị và không có lý do**, lại hiện thông báo `RECO-M01` dù đã nhập đủ; đầu trang Khuyến nghị `—`; bước `Lãi suất` ghi `Chưa mở`. Trong khi đó API trả `DECLINE` + `ageAtMaturity` (age 76, max 70) | chưa rõ (thiết kế hay lỗi hiển thị?) · [E09](#e09) [E14](#e14) · Liên quan: `RECO-Q02`, `RECO-M01`, `RECO-M08` |

### `RECO-S05` — Khuyến nghị ở đầu trang hồ sơ và lưu dữ liệu
**Là** chuyên viên khách hàng, **tôi muốn** thấy khuyến nghị trên đầu hồ sơ **để** nhìn nhanh mà không cần mở từng bước.

**Luồng:** (1) nhập số ở bước Tài chính → (2) khung `Thẩm định` đổi ngay → (3) bấm `Lưu` → (4) sau vài giây ô `Khuyến nghị` đầu trang đổi theo.

| ID | Tình huống | Bối cảnh | Người dùng làm | Hệ thống phản hồi | Nhãn · Bằng chứng · Liên quan |
|---|---|---|---|---|---|
| <a id="reco-s05-ac01"></a>`RECO-S05-AC01` | Đầu trang cập nhật sau khi lưu | Vay `3200000000`, đầu trang Khuyến nghị `—` | Nhập lương `100000000`, nợ hiện có `5000000`, người phụ thuộc `5`, bấm `Lưu` | Phản hồi chậm vài giây (4 giây sau vẫn `—`); sau đó ô Khuyến nghị thành `Phê duyệt`; bước `Tài chính` ghi `Đã xong`; ô `Lương hằng tháng` giữ giá trị khi mở lại | đã thấy · [E04](#e04) · Liên quan: `RECO-M11` |
| <a id="reco-s05-ac02"></a>`RECO-S05-AC02` | Chưa lưu thì đầu trang giữ kết quả cũ | Đầu trang Khuyến nghị đang `Phê duyệt` (đã lưu) | Đổi lương thành `75000000`, **chưa** bấm `Lưu` | Khung Thẩm định ghi `Chuyển cấp trên` nhưng đầu trang vẫn `Phê duyệt` cho tới khi bấm `Lưu` | đã thấy · [E19](#e19) [E02](#e02) · Liên quan: `RECO-Q05` |
| <a id="reco-s05-ac03"></a>`RECO-S05-AC03` | Lưu khi để trống | Mọi ô tài chính trống | Bấm `Lưu` | `Đã lưu.` (`RECO-M11`); đầu trang Khuyến nghị về `—` | đã thấy · [E17](#e17) · Liên quan: `RECO-M11` |
| <a id="reco-s05-ac04"></a>`RECO-S05-AC04` | Ô tiền chỉ nhận chữ số | Bước Tài chính | Điền (bằng công cụ) `abc` rồi `-5000000` vào ô lương | `abc` → ô để trống, quay về thông báo `RECO-M01`; `-5000000` → ô giữ `5000000` (dấu trừ bị bỏ), DSR `816,00%`, nhãn `Từ chối` với hai lý do (DSR và thặng dư) | đã thấy (điền bằng công cụ, chưa gõ từng phím) · [E08](#e08) [E17](#e17) · Liên quan: `RECO-R11` |

### `RECO-S06` — Xem khuyến nghị bằng tiếng Anh
**Là** người dùng chọn English, **tôi muốn** khung thẩm định đổi hết sang tiếng Anh **để** dùng hệ thống bằng ngôn ngữ của mình.

| ID | Tình huống | Bối cảnh | Người dùng làm | Hệ thống phản hồi | Nhãn · Bằng chứng · Liên quan |
|---|---|---|---|---|---|
| <a id="reco-s06-ac01"></a>`RECO-S06-AC01` | Giao diện English | Bước Tài chính, vay 3,2 tỷ, LTV 64% | Bấm `English`, nhập lương `75000000` | Khung tên `Assessment`, nhãn `Refer`; `Loan-to-value` `64.00% (Maximum LTV 80.00%)`; `Debt service ratio` `53.51%`; mục `Reasons`: `Refer: DSR 53.51% is above 50%; refer to a senior assessor.`. Số viết `40,133,333 VND` (dấu phẩy ngăn nghìn, dấu chấm thập phân). Đầu trang: `Recommendation` `Approve` | đã thấy · [E10](#e10) [E16](#e16) · Liên quan: `RECO-M04`..`RECO-M07`, `RECO-M12` |

## 4. Bảng tra cứu
### 4.1 Quy tắc dữ liệu
| ID | Trường | Quy tắc quan sát được | Nhãn | Bằng chứng |
|---|---|---|---|---|
| <a id="reco-r01"></a>`RECO-R01` | LTV tối đa | **Mua nhà: 80%**; **Xây/sửa nhà: 70%** (`maxLtv` 80 hoặc 70). Vượt mức → `Từ chối`. Nhận biết "vượt" theo số hiển thị 2 chữ số thập phân: 80,0025% (hiện `80,00%`) vẫn đạt, 80,01% bị từ chối. | đã thấy; chưa rõ (làm tròn: Q01) | [E13](#e13), [E22](#e22), [E06](#e06) |
| <a id="reco-r02"></a>`RECO-R02` | DSR | Từ `0` đến **50,00%**: không ảnh hưởng. Trên 50% đến **70,00%**: `Chuyển cấp trên`. Trên 70%: `Từ chối`. DSR đúng 50,00% và đúng 70,00% thuộc nhóm thấp hơn. | đã thấy; chưa rõ (làm tròn: Q01) | [E11](#e11), [E02](#e02) |
| <a id="reco-r03"></a>`RECO-R03` | Thặng dư hằng tháng | Tối thiểu **3.000.000 VND**; thấp hơn (kể cả 2.999.999) → `Từ chối`. So theo số đồng nguyên. | đã thấy | [E07](#e07) |
| <a id="reco-r04"></a>`RECO-R04` | Tuổi lúc đáo hạn | Tuổi cao nhất của các người vay khi hết thời hạn phải **≤ 70**; 71 trở lên → `Từ chối` (thấy qua API; màn hình không hiện, xem S04-AC04). | đã thấy (API); chưa rõ (hiển thị: Q02) | [E14](#e14), [E09](#e09) |
| <a id="reco-r05"></a>`RECO-R05` | LTV | Khi tài sản chưa có kết quả định giá: **số tiền vay ÷ giá trị khai báo** (ví dụ 3,2 tỷ ÷ 5 tỷ = 64%). Khi đã định giá: chưa kiểm tra. | đã thấy (chưa định giá); chưa kiểm (đã định giá) | [E15](#e15) |
| <a id="reco-r06"></a>`RECO-R06` | Thu nhập cho thuê | Chỉ **70%** được tính vào thu nhập (dòng giải thích dưới ô). Thu nhập được tính = lương + 70% × thu nhập cho thuê. | đã thấy | [E03](#e03) |
| <a id="reco-r07"></a>`RECO-R07` | Chi phí được tính | Để trống / không người phụ thuộc: `4.500.000`. Quan sát với người phụ thuộc 2, 5, 20: `4.500.000 + 2.000.000 × số người phụ thuộc` (8,5 / 14,5 / 44,5 triệu), kể cả khi nhập chi phí thấp hơn. Chi phí nhập cao hơn mức đó thì dùng số nhập. | đã thấy (số liệu); chưa rõ (công thức: Q03) | [E12](#e12) |
| <a id="reco-r08"></a>`RECO-R08` | Khoản trả mới theo lãi suất thẩm định | Phụ thuộc số tiền vay, thời hạn, phương thức trả nợ, ân hạn, lãi suất thẩm định. Số đã thấy: Gốc đều 3,2 tỷ/20 năm/10,30% = `40.800.000`; 40 năm = `34.133.333`; Niên kim 10,05%/20 năm = `30.986.775`; thêm ân hạn 12 tháng = `31.504.846`. | đã thấy (số liệu) | [E14](#e14), [E21](#e21) |
| <a id="reco-r09"></a>`RECO-R09` | Lãi suất thẩm định | Đổi theo LTV và theo sản phẩm. Mua nhà, sản phẩm 12 tháng: LTV 32%/40% → `9,80%`; 53,33% → `9,90%`; 64% → `10,05%`; 80% và trên → `10,30%`. Sản phẩm 36 tháng ở LTV 64%: `9,55%`. Xây/sửa nhà ở LTV 76,19%: `10,30%`. | đã thấy (số liệu); chưa rõ (quy tắc: Q04) | [E15](#e15), [E22](#e22) |
| <a id="reco-r10"></a>`RECO-R10` | Công thức DSR, thặng dư và điều kiện hiện khuyến nghị | **DSR** = (khoản trả mới + nợ hiện có) ÷ thu nhập được tính. **Thặng dư** = thu nhập được tính − chi phí được tính − khoản trả mới − nợ hiện có. Thu nhập `0`: DSR `—` và không có nhãn khuyến nghị. | đã thấy (đối chiếu số) | [E01](#e01), [E12](#e12), [E08](#e08) |
| <a id="reco-r11"></a>`RECO-R11` | Ô nhập tiền/số | Chỉ nhận chữ số: chữ và dấu trừ bị bỏ khi điền. Dưới ô hiện số có dấu chấm ngăn nghìn. | đã thấy (điền bằng công cụ) | [E17](#e17) |
| <a id="reco-r12"></a>`RECO-R12` | Ngưỡng cố định hay cấu hình | `GET /api/settings` trả `{"release":"1.3.0","settings":{}}` — không chứa ngưỡng nào. | đã thấy | [E18](#e18) |

### 4.2 Thông báo hệ thống (nguyên văn)
| ID | Khi nào | Tiếng Việt | English | Bằng chứng |
|---|---|---|---|---|
| <a id="reco-m01"></a>`RECO-M01` | Chưa đủ thông tin để có khuyến nghị (cũng hiện khi thời hạn quá dài, xem S04-AC04) | `Nhập đủ thông tin người vay, khoản vay, tài sản và thu nhập để xem khuyến nghị.` | `Enter the borrower, loan, property and income details to see a recommendation.` (chỉ thấy trong tệp giao diện) | [E08](#e08), [E16](#e16) |
| <a id="reco-m02"></a>`RECO-M02` | Không có lý do nào | `Đáp ứng mọi quy tắc tín dụng.` | `All credit rules are met.` (chỉ thấy trong tệp giao diện) | [E01](#e01), [E16](#e16) |
| <a id="reco-m03"></a>`RECO-M03` | Dòng nhỏ dưới nhãn khuyến nghị | `Xem trước: thẩm định chính thức chạy khi gửi, có dữ liệu CIC.` | `Preview: final assessment runs at submission with CIC data.` | [E01](#e01), [E10](#e10) |
| <a id="reco-m04"></a>`RECO-M04` | LTV vượt tối đa (`Từ chối`) | `LTV {ltv}% vượt mức tối đa {max}%.` — ví dụ `Từ chối: LTV 81% vượt mức tối đa 80%.` | `LTV {ltv}% is above the maximum {max}%.` (chỉ thấy trong tệp giao diện) | [E06](#e06), [E16](#e16) |
| <a id="reco-m05"></a>`RECO-M05` | DSR vượt tối đa (`Từ chối`) | `DSR {dsr}% vượt mức tối đa {max}%.` — ví dụ `Từ chối: DSR 70,34% vượt mức tối đa 70%.` | `DSR {dsr}% is above the maximum {max}%.` (chỉ thấy trong tệp giao diện) | [E11](#e11), [E16](#e16) |
| <a id="reco-m06"></a>`RECO-M06` | DSR trên 50% (`Chuyển cấp trên`) | `DSR {dsr}% vượt {max}%; chuyển cấp trên xem xét.` — ví dụ `Chuyển cấp trên: DSR 50,37% vượt 50%; chuyển cấp trên xem xét.` | `DSR {dsr}% is above {max}%; refer to a senior assessor.` — thấy: `Refer: DSR 53.51% is above 50%; refer to a senior assessor.` | [E02](#e02), [E10](#e10) |
| <a id="reco-m07"></a>`RECO-M07` | Thặng dư thấp (`Từ chối`) | `Thặng dư hằng tháng {surplus} VND thấp hơn {min} VND.` — ví dụ `Từ chối: Thặng dư hằng tháng 2.999.999 VND thấp hơn 3.000.000 VND.` | `Monthly surplus {surplus} VND is below {min} VND.` (chỉ thấy trong tệp giao diện) | [E07](#e07), [E16](#e16) |
| <a id="reco-m08"></a>`RECO-M08` | Quá tuổi lúc đáo hạn (`Từ chối`) — **chưa thấy trên màn hình** | `Có người vay {age} tuổi khi đáo hạn; tối đa {max}.` | `A borrower would be {age} at maturity; the maximum is {max}.` | [E16](#e16), [E14](#e14) |
| <a id="reco-m09"></a>`RECO-M09` | Định giá thấp hơn giá khai báo — **chưa thấy** (chỉ trong tệp giao diện) | `Giá định giá thấp hơn giá khai báo {shortfall}% (quá {max}%).` | `Valuation is {shortfall}% below the declared value (more than {max}%).` | [E16](#e16) |
| <a id="reco-m10"></a>`RECO-M10` | CIC báo nhóm nợ — **chưa thấy** (chỉ trong tệp giao diện) | `CIC báo người vay {borrower} thuộc nhóm nợ {group}.` | `CIC reports debt group {group} for borrower {borrower}.` | [E16](#e16) |
| <a id="reco-m11"></a>`RECO-M11` | Lưu thành công | `Đã lưu.` | chưa thấy bản English | [E04](#e04), [E17](#e17) |
| <a id="reco-m12"></a>`RECO-M12` | Nhãn khuyến nghị (tiền tố ở dòng lý do giống nhãn) | `Phê duyệt` · `Chuyển cấp trên` · `Từ chối` | `Approve` · `Refer` · `Decline` | [E10](#e10), [E16](#e16) |

## 5. Điểm chưa rõ và câu hỏi cho team
| ID | Đã thấy | Vì sao chưa rõ | Câu hỏi | Liên quan | Trạng thái |
|---|---|---|---|---|---|
| <a id="reco-q01"></a>`RECO-Q01` | DSR thật 50,0006% hiện `50,00%` → Phê duyệt; LTV thật 80,0025% hiện `80,00%` → Phê duyệt; nhưng thặng dư 2.999.999 → Từ chối | Không rõ ngưỡng so sánh dùng số đã làm tròn 2 chữ số hay số thật | So ngưỡng LTV, DSR theo số làm tròn hay số thật? | S01-AC07, S02-AC02, R01, R02 | mở |
| <a id="reco-q02"></a>`RECO-Q02` | Tuổi lúc đáo hạn > 70: API trả `DECLINE` + lý do, nhưng màn hình không hiện nhãn, không hiện lý do, lại hiện câu "Nhập đủ thông tin…"; đầu trang `—`; bước `Lãi suất` `Chưa mở` | Không rõ do thiết kế hay lỗi hiển thị | Quá tuổi 70 phải hiện `Từ chối` kèm lý do `RECO-M08` trên màn hình? | S04-AC04, M01, M08 | mở |
| <a id="reco-q03"></a>`RECO-Q03` | `Chi phí được tính` khớp `4.500.000 + 2.000.000 × số người phụ thuộc` ở 3 điểm; chi phí nhập thấp hơn bị nâng lên | Công thức chỉ suy ra từ số liệu | Công thức chi phí tối thiểu chính thức? Nhập chi phí thấp hơn mức tối thiểu thì hệ thống nâng lên có chủ ý không (người dùng không được báo)? | S03-AC06, R07 | mở |
| <a id="reco-q04"></a>`RECO-Q04` | Lãi suất thẩm định đổi theo LTV (9,80% → 10,30%) và theo sản phẩm (36 tháng thấp hơn 0,5 điểm % so với 12 tháng ở cùng LTV 64%); Xây/sửa nhà LTV tối đa 70% | Chưa thấy tài liệu quy tắc | Quy tắc tính lãi suất thẩm định (theo LTV, sản phẩm, mục đích) và vì sao LTV tối đa của Xây/sửa nhà là 70%? | S02-AC06, S02-AC07, S03-AC10, R09 | mở |
| <a id="reco-q05"></a>`RECO-Q05` | Ô Khuyến nghị đầu trang chỉ đổi sau `Lưu`, và cập nhật chậm vài giây; khung Thẩm định đổi ngay | Có thể chủ ý (đầu trang là bản đã lưu) nhưng dễ gây hiểu nhầm | Đầu trang chỉ phản ánh bản đã lưu — chủ ý? Có cần chú thích? | S05-AC01, S05-AC02 | mở |
| <a id="reco-q06"></a>`RECO-Q06` | Ngưỡng 50%, 70%, 3.000.000, tuổi 70, LTV 80%/70% hiện hằng số; `/api/settings` trả danh sách rỗng | Không rõ có chỉnh được không, ai chỉnh | Các ngưỡng này cố định hay cấu hình? Ai được đổi? | R01, R02, R03, R04, R12 | mở |
| <a id="reco-q07"></a>`RECO-Q07` | Tệp giao diện có hai câu của bước quyết định: `Không thể phê duyệt hồ sơ được khuyến nghị từ chối.` và `Ghi rõ lý do phê duyệt hồ sơ được khuyến nghị chuyển cấp trên.` | Chưa thấy trên màn hình (cần P300001); nhật ký cũ ghi Từ chối thủ công trái khuyến nghị vẫn được | Khuyến nghị `Từ chối` có chặn phê duyệt không, `Chuyển cấp trên` có buộc ghi lý do không? | RECO (ngoài phạm vi) | mở |

## 6. Bằng chứng và chưa khám phá
Cách gọi tên: **Ảnh NN** = ảnh trong `evidence/banking-lite/features/khuyen-nghi-ltv-dsr/screenshots/` (đánh số NN). **Nhật ký, hàng N** = hàng N trong bảng ở mục 1 của [bao-cao.md](../../evidence/banking-lite/features/khuyen-nghi-ltv-dsr/bao-cao.md). Mọi ngày đều **2026-11-17**, phiên bản hệ thống **1.3.0**, tài khoản **P100001**, hồ sơ test **HL-000025** (xem đầu nhật ký).

### 6.1 Bằng chứng
Loại: **ảnh** · **quan sát** (đọc chữ trên trang, API `GET`, **không có ảnh**) · **tệp giao diện** (đọc mã công khai của trang, không phải hành vi trên màn hình).

| ID | Loại | Thao tác đã làm | Tệp | Cách kiểm lại |
|---|---|---|---|---|
| <a id="e01"></a>`RECO-E01` | ảnh · P100001 | Lương 100 triệu, hồ sơ nền → Phê duyệt | [Ảnh 01](../../evidence/banking-lite/features/khuyen-nghi-ltv-dsr/screenshots/01-p100001-tai-chinh-luong-100tr-phe-duyet.jpg) | Mở bước Tài chính của hồ sơ nền, nhập lương `100000000`, nhìn khung Thẩm định |
| <a id="e02"></a>`RECO-E02` | ảnh · P100001 | Lương 81 triệu → DSR 50,37% Chuyển cấp trên | [Ảnh 02](../../evidence/banking-lite/features/khuyen-nghi-ltv-dsr/screenshots/02-p100001-tai-chinh-luong-81tr-chuyen-cap-tren.jpg) | Như E01 nhưng lương `81000000` |
| <a id="e03"></a>`RECO-E03` | ảnh · P100001 | Lương 50 tr + thu nhập cho thuê 50 tr | [Ảnh 03](../../evidence/banking-lite/features/khuyen-nghi-ltv-dsr/screenshots/03-p100001-tai-chinh-thu-nhap-cho-thue-50tr.jpg) | Nhập lương `50000000` và cho thuê `50000000`; xem thu nhập được tính |
| <a id="e04"></a>`RECO-E04` | ảnh · P100001 | Sau `Lưu`, đầu trang Khuyến nghị đổi thành Phê duyệt | [Ảnh 04](../../evidence/banking-lite/features/khuyen-nghi-ltv-dsr/screenshots/04-p100001-dau-trang-khuyen-nghi-sau-khi-luu.jpg) | Nhập lương, bấm `Lưu`, chờ vài giây, nhìn đầu trang |
| <a id="e05"></a>`RECO-E05` | ảnh · P100001 | Bước Khoản vay với số tiền vay 3,24 tỷ | [Ảnh 05](../../evidence/banking-lite/features/khuyen-nghi-ltv-dsr/screenshots/05-p100001-khoan-vay-3-24-ty.jpg) | Bước Khoản vay, nhập `3240000000`, `Lưu` |
| <a id="e06"></a>`RECO-E06` | ảnh · P100001 | LTV 81% + DSR 77% + thặng dư âm: ba lý do | [Ảnh 06](../../evidence/banking-lite/features/khuyen-nghi-ltv-dsr/screenshots/06-p100001-tai-chinh-ltv-81-dsr-77-tu-choi-nhieu-ly-do.jpg) | Vay 3,24 tỷ (đã lưu), nợ hiện có 5 triệu, người phụ thuộc 5, lương `60000000`; cuộn tới `Lý do` |
| <a id="e07"></a>`RECO-E07` | ảnh · P100001 | Thặng dư 1,2 triệu → Từ chối (và biên 3.000.000 / 2.999.999) | [Ảnh 07](../../evidence/banking-lite/features/khuyen-nghi-ltv-dsr/screenshots/07-p100001-tai-chinh-thang-du-1-2tr-tu-choi.jpg) · [Nhật ký, hàng 22](../../evidence/banking-lite/features/khuyen-nghi-ltv-dsr/bao-cao.md) | Lương `100000000`; chi phí `56200000`, `56200001`, `58000000` |
| <a id="e08"></a>`RECO-E08` | ảnh · P100001 | Chưa nhập thu nhập: thông báo "Nhập đủ thông tin…" | [Ảnh 08](../../evidence/banking-lite/features/khuyen-nghi-ltv-dsr/screenshots/08-p100001-tai-chinh-de-trong-chua-co-khuyen-nghi.jpg) | Mở bước Tài chính khi mọi ô trống |
| <a id="e09"></a>`RECO-E09` | ảnh · P100001 | Thời hạn 40 năm: không hiện khuyến nghị | [Ảnh 09](../../evidence/banking-lite/features/khuyen-nghi-ltv-dsr/screenshots/09-p100001-tai-chinh-thoi-han-40-nam-khong-hien-khuyen-nghi.jpg) | Bước Khoản vay: thời hạn `40`, `Lưu`; mở bước Tài chính (lương 100 triệu đã lưu) |
| <a id="e10"></a>`RECO-E10` | ảnh · P100001 | Giao diện English, nhãn Refer | [Ảnh 10](../../evidence/banking-lite/features/khuyen-nghi-ltv-dsr/screenshots/10-p100001-tai-chinh-english-refer.jpg) | Bấm `English`, mở bước Tài chính, lương `75000000` |
| <a id="e11"></a>`RECO-E11` | quan sát · P100001 | Biên DSR 50% / 70% (lương 81.600.000, 81.599.000, 81.000.000, 75.000.000, 58.285.714, 58.000.000) | [Nhật ký, hàng 6, 7, 9, 10, 11](../../evidence/banking-lite/features/khuyen-nghi-ltv-dsr/bao-cao.md) | Hồ sơ nền, nhập lần lượt các lương, đọc DSR + nhãn + lý do trong khung Thẩm định (không có ảnh riêng; ca 81 triệu có Ảnh 02) |
| <a id="e12"></a>`RECO-E12` | quan sát · P100001 | Chi phí, người phụ thuộc, nợ hiện có, số rất lớn | [Nhật ký, hàng 13–16 và 33](../../evidence/banking-lite/features/khuyen-nghi-ltv-dsr/bao-cao.md) | Nhập từng ô theo hàng nhật ký, đọc dòng `Chi phí được tính`, `DSR`, `Thặng dư` (không có ảnh) |
| <a id="e13"></a>`RECO-E13` | quan sát · P100001 | Biên LTV: vay 3.200.100.000 / 3.200.400.000 / 3.240.000.000 | [Nhật ký, hàng 18–20](../../evidence/banking-lite/features/khuyen-nghi-ltv-dsr/bao-cao.md) | Bước Khoản vay: đổi số tiền, `Lưu`, đọc ô LTV và Khuyến nghị đầu trang (không có ảnh) |
| <a id="e14"></a>`RECO-E14` | quan sát · P100001 | Thời hạn 20/34/35/40 năm; phản hồi `GET /api/applications/<id>` | [Nhật ký, hàng 25, 26](../../evidence/banking-lite/features/khuyen-nghi-ltv-dsr/bao-cao.md) | Đổi thời hạn, `Lưu`, F12 → Network → `/api/applications/<id>` → Response → `assessment` (có `recommendation`, `reasons`, `metrics.maxAgeAtMaturity`) |
| <a id="e15"></a>`RECO-E15` | quan sát · P100001 | Giá trị khai báo 3–10 tỷ → LTV và lãi suất thẩm định | [Nhật ký, hàng 27](../../evidence/banking-lite/features/khuyen-nghi-ltv-dsr/bao-cao.md) | Đổi giá trị khai báo, `Lưu`, đọc `assessment.metrics.ltv`, `assessmentRate` trong phản hồi API |
| <a id="e16"></a>`RECO-E16` | tệp giao diện | Bảng thông báo VI/EN, mã lý do, nhãn khuyến nghị trong `/assets/main.99595f2e.js` | [Nhật ký, hàng 30](../../evidence/banking-lite/features/khuyen-nghi-ltv-dsr/bao-cao.md) | F12 → Sources/Network mở tệp, tìm `assessment.ltvAboveMax`, `assessment.ageAtMaturity`, `recommendation.REFER` (tên tệp có thể đổi theo bản phát hành) |
| <a id="e17"></a>`RECO-E17` | quan sát · P100001 | Điền `abc` / `-5000000`; `Lưu` khi mọi ô trống | [Nhật ký, hàng 23, 24](../../evidence/banking-lite/features/khuyen-nghi-ltv-dsr/bao-cao.md) | Điền vào ô lương, đọc giá trị ô; để trống rồi `Lưu`, đọc `Đã lưu.` và đầu trang (không có ảnh riêng; Ảnh 08 cho trạng thái trống) |
| <a id="e18"></a>`RECO-E18` | quan sát · P100001 | `GET /api/settings` | [Nhật ký, hàng 31](../../evidence/banking-lite/features/khuyen-nghi-ltv-dsr/bao-cao.md) | F12 → Network → `/api/settings` → Response |
| <a id="e19"></a>`RECO-E19` | quan sát · P100001 | Khung Thẩm định đổi ngay còn đầu trang giữ bản cũ | [Nhật ký, hàng 28](../../evidence/banking-lite/features/khuyen-nghi-ltv-dsr/bao-cao.md) | Lưu lương 100 triệu, rồi đổi lương `75000000` **không** bấm Lưu; so khung Thẩm định với đầu trang |
| <a id="e20"></a>`RECO-E20` | quan sát · P100001 | Hồ sơ mới tạo: bước Tài chính chưa mở | [Nhật ký, hàng 1, 2](../../evidence/banking-lite/features/khuyen-nghi-ltv-dsr/bao-cao.md) | `Tạo hồ sơ mới`, mở `/applications/<id>/financials` (không có ảnh) |
| <a id="e21"></a>`RECO-E21` | quan sát · P100001 | Phương thức Niên kim và ân hạn 12 tháng | [Nhật ký, hàng 34, 35](../../evidence/banking-lite/features/khuyen-nghi-ltv-dsr/bao-cao.md) | Bước Khoản vay: đổi phương thức/ân hạn, `Lưu`, đọc `assessment.metrics.newRepayment` (không có ảnh) |
| <a id="e22"></a>`RECO-E22` | quan sát · P100001 | Sản phẩm 36 tháng; mục đích Xây/sửa nhà, LTV tối đa 70% | [Nhật ký, hàng 36–38](../../evidence/banking-lite/features/khuyen-nghi-ltv-dsr/bao-cao.md) | Đổi sản phẩm/mục đích, `Lưu`, đọc `maxLtv`, `assessmentRate`; mở bước Tài chính đọc `(LTV tối đa 70,00%)` (không có ảnh) |

### 6.2 Chưa khám phá
- **Quy tắc `RECO-M09` (định giá thấp hơn giá khai báo) và `RECO-M10` (nhóm nợ CIC):** cần tài sản đã có kết quả định giá hoặc hồ sơ đã gửi thẩm định chính thức. Bấm `Yêu cầu định giá` bị hệ thống chặn (nhật ký hàng 32); `Gửi thẩm định` khóa hồ sơ và gọi CIC nên cần người dùng đồng ý trước.
- **LTV khi tài sản đã được định giá** (dùng giá định giá hay giá khai báo): cùng lý do trên.
- **Khung Thẩm định với P200001 và P300001, và tác động lên quyết định của P300001** (`RECO-Q07`): cần người dùng gõ mật khẩu từng tài khoản.
- **Hồ sơ nhiều người vay** (`Thêm người vay`): cần nhập thêm danh tính người vay và chạy VNeID; chưa hỏi người dùng có muốn thử không.
- **Sản phẩm 24 tháng (7,00%)** và lãi suất thẩm định của Xây/sửa nhà ở nhiều mức LTV: chưa đổi sang, ghi để lượt sau.

## 7. Lịch sử thay đổi
| Ngày | Phiên bản hệ thống | Thay đổi | Lý do |
|---|---|---|---|
| 2026-11-17 | 1.3.0 | Tạo mới: 6 story, 37 tiêu chí chấp nhận (AC), 12 quy tắc, 12 thông báo, 7 câu hỏi, 22 bằng chứng | Lượt thử đầu tiên chạy skill `srs-from-website` trên feature mới "Khuyến nghị LTV/DSR" |
