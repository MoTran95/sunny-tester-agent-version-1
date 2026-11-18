# Truy vết — Khuyến nghị thẩm định xem trước LTV/DSR (Banking Lite)

*File này do `scripts/truy-vet.py` tự sinh, đừng sửa tay. Muốn đổi thì sửa nguồn rồi chạy lại script.*

| | |
|---|---|
| Lần chạy gần nhất | 2026-11-18 19:52:42 (+07:00) (chỉ kiểm, chưa đổi mốc) |
| Requirement | srs/banking-lite/khuyen-nghi-ltv-dsr.md (cập nhật 2026-11-17); bảng soát (cập nhật ?), câu trả lời đến TL-02 |
| Test case (đã gồm checklist) | [test-case.md](test-case.md) |
| Mốc đã chốt | 2026-11-18 19:04:01 (+07:00) (khi đó: SRS 2026-11-17, bảng soát ?, TL đến TL-02) |

## 1. Tóm tắt
- Mã requirement: 61 trong SRS, 2 câu trả lời (TL). Test case: 38.
- Trạng thái test case: Còn đúng 38
- Mã requirement đã đổi so với mốc đã chốt: không có; mã mới: không có.
- Mã SRS chưa có test case nào: M09, M10, R12, S03-AC11, S04-AC01, S04-AC04, S05-AC02.
- Test case đã bỏ khỏi file: không có.
- Vấn đề khác: không có

## 2. Khi requirement đổi, làm gì
1. Sửa SRS hoặc ghi câu trả lời mới của BA vào bảng soát (như mọi lần).
2. Chạy `python -X utf8 scripts/truy-vet.py kiem banking-lite khuyen-nghi-ltv-dsr`. Script liệt kê mã đã đổi và các test case chuyển sang **Cần xem lại**.
3. Mở từng test case đó (bảng 6 dưới đây), sửa test case cho khớp (checklist nằm chung bảng).
4. Chạy `python -X utf8 scripts/truy-vet.py chot banking-lite khuyen-nghi-ltv-dsr -m "đã làm gì, vì sao"`. Script ghi một dòng lịch sử và chốt mốc mới.
5. Muốn xem từng chữ đã đổi, dùng lịch sử git (commit sau mỗi lần chốt).

## 3. Bảng tra mã
Mã trong cột Nguồn của checklist và test case bỏ tiền tố `RECO-`. `S01-AC02` là story 1, tình huống 2; `R` là quy tắc; `M` là thông báo; `TL` là câu trả lời của BA (TL-12, TL-13 là điều suy ra, người dùng xác nhận).

| Mã | Tên ngắn | Nguyên văn (rút gọn) | Mở ở đâu |
|---|---|---|---|
| M01 | Thông báo chưa đủ thông tin | `Nhập đủ thông tin người vay, khoản vay, tài sản và thu nhập để xem khuyến nghị.` | [khuyen-nghi-ltv-dsr.md dòng 146](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L146) |
| M02 | Không có lý do | `Đáp ứng mọi quy tắc tín dụng.` | [khuyen-nghi-ltv-dsr.md dòng 147](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L147) |
| M03 | Dòng xem trước | `Xem trước: thẩm định chính thức chạy khi gửi, có dữ liệu CIC.` | [khuyen-nghi-ltv-dsr.md dòng 148](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L148) |
| M04 | LTV vượt tối đa | `LTV {ltv}% vượt mức tối đa {max}%.` — ví dụ `Từ chối: LTV 81% vượt mức tối đa 80%.` | [khuyen-nghi-ltv-dsr.md dòng 149](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L149) |
| M05 | DSR vượt tối đa | `DSR {dsr}% vượt mức tối đa {max}%.` — ví dụ `Từ chối: DSR 70,34% vượt mức tối đa 70%.` | [khuyen-nghi-ltv-dsr.md dòng 150](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L150) |
| M06 | DSR trên 50% | `DSR {dsr}% vượt {max}%; chuyển cấp trên xem xét.` — ví dụ `Chuyển cấp trên: DSR 50,37% vượt 50%; chuyển cấp trên xem xét.` | [khuyen-nghi-ltv-dsr.md dòng 151](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L151) |
| M07 | Thặng dư thấp | `Thặng dư hằng tháng {surplus} VND thấp hơn {min} VND.` — ví dụ `Từ chối: Thặng dư hằng tháng 2.999.999 VND thấp hơn 3.000.000 VND.` | [khuyen-nghi-ltv-dsr.md dòng 152](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L152) |
| M08 | Quá tuổi | `Có người vay {age} tuổi khi đáo hạn; tối đa {max}.` | [khuyen-nghi-ltv-dsr.md dòng 153](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L153) |
| M09 | Định giá thấp hơn giá khai báo — **chưa… | `Giá định giá thấp hơn giá khai báo {shortfall}% (quá {max}%).` | [khuyen-nghi-ltv-dsr.md dòng 154](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L154) |
| M10 | CIC báo nhóm nợ — **chưa thấy** (chỉ tr… | `CIC báo người vay {borrower} thuộc nhóm nợ {group}.` | [khuyen-nghi-ltv-dsr.md dòng 155](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L155) |
| M11 | Đã lưu | `Đã lưu.` | [khuyen-nghi-ltv-dsr.md dòng 156](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L156) |
| M12 | Nhãn khuyến nghị | `Phê duyệt` · `Chuyển cấp trên` · `Từ chối` | [khuyen-nghi-ltv-dsr.md dòng 157](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L157) |
| R01 | LTV tối đa | **Mua nhà: 80%**; **Xây/sửa nhà: 70%** (`maxLtv` 80 hoặc 70). Vượt mức → `Từ chối`. Nhận biết "vượt" theo số hiển thị 2 chữ số thập phân: 80,0025% (h… | [khuyen-nghi-ltv-dsr.md dòng 130](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L130) |
| R02 | DSR | Từ `0` đến **50,00%**: không ảnh hưởng. Trên 50% đến **70,00%**: `Chuyển cấp trên`. Trên 70%: `Từ chối`. DSR đúng 50,00% và đúng 70,00% thuộc nhóm th… | [khuyen-nghi-ltv-dsr.md dòng 131](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L131) |
| R03 | Thặng dư tối thiểu | Tối thiểu **3.000.000 VND**; thấp hơn (kể cả 2.999.999) → `Từ chối`. So theo số đồng nguyên. | [khuyen-nghi-ltv-dsr.md dòng 132](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L132) |
| R04 | Tuổi lúc đáo hạn | Tuổi cao nhất của các người vay khi hết thời hạn phải **≤ 70**; 71 trở lên → `Từ chối` (thấy qua API; màn hình không hiện, xem S04-AC04). | [khuyen-nghi-ltv-dsr.md dòng 133](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L133) |
| R05 | LTV theo giá khai báo | Khi tài sản chưa có kết quả định giá: **số tiền vay ÷ giá trị khai báo** (ví dụ 3,2 tỷ ÷ 5 tỷ = 64%). Khi đã định giá: chưa kiểm tra. | [khuyen-nghi-ltv-dsr.md dòng 134](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L134) |
| R06 | Thu nhập cho thuê | Chỉ **70%** được tính vào thu nhập (dòng giải thích dưới ô). Thu nhập được tính = lương + 70% × thu nhập cho thuê. | [khuyen-nghi-ltv-dsr.md dòng 135](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L135) |
| R07 | Chi phí được tính | Để trống / không người phụ thuộc: `4.500.000`. Quan sát với người phụ thuộc 2, 5, 20: `4.500.000 + 2.000.000 × số người phụ thuộc` (8,5 / 14,5 / 44,5… | [khuyen-nghi-ltv-dsr.md dòng 136](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L136) |
| R08 | Khoản trả mới | Phụ thuộc số tiền vay, thời hạn, phương thức trả nợ, ân hạn, lãi suất thẩm định. Số đã thấy: Gốc đều 3,2 tỷ/20 năm/10,30% = `40.800.000`; 40 năm = `3… | [khuyen-nghi-ltv-dsr.md dòng 137](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L137) |
| R09 | Lãi suất thẩm định | Đổi theo LTV và theo sản phẩm. Mua nhà, sản phẩm 12 tháng: LTV 32%/40% → `9,80%`; 53,33% → `9,90%`; 64% → `10,05%`; 80% và trên → `10,30%`. Sản phẩm… | [khuyen-nghi-ltv-dsr.md dòng 138](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L138) |
| R10 | Công thức DSR và thặng dư | **DSR** = (khoản trả mới + nợ hiện có) ÷ thu nhập được tính. **Thặng dư** = thu nhập được tính − chi phí được tính − khoản trả mới − nợ hiện có. Thu… | [khuyen-nghi-ltv-dsr.md dòng 139](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L139) |
| R11 | Ô nhập tiền | Chỉ nhận chữ số: chữ và dấu trừ bị bỏ khi điền. Dưới ô hiện số có dấu chấm ngăn nghìn. | [khuyen-nghi-ltv-dsr.md dòng 140](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L140) |
| R12 | Ngưỡng cố định hay cấu hình | `GET /api/settings` trả `{"release":"1.3.0","settings":{}}` — không chứa ngưỡng nào. | [khuyen-nghi-ltv-dsr.md dòng 141](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L141) |
| S01-AC01 | Chưa nhập thu nhập | Khung `Thẩm định` **không có nhãn khuyến nghị** và **không có mục `Lý do`**. Có thông báo xanh `Nhập đủ thông tin người vay, khoản vay, tài sản và th… | [khuyen-nghi-ltv-dsr.md dòng 50](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L50) |
| S01-AC02 | Đạt mọi quy tắc | Nhãn `Phê duyệt`. Dòng nhỏ `Xem trước: thẩm định chính thức chạy khi gửi, có dữ liệu CIC.` (`RECO-M03`). DSR `40,80%`; thặng dư `54.700.000 VND`. Mục… | [khuyen-nghi-ltv-dsr.md dòng 51](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L51) |
| S01-AC03 | DSR trên 50% | Nhãn `Chuyển cấp trên`. DSR `50,37%`. Lý do: `Chuyển cấp trên: DSR 50,37% vượt 50%; chuyển cấp trên xem xét.` (`RECO-M06`). Cùng kết quả với lương `7… | [khuyen-nghi-ltv-dsr.md dòng 52](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L52) |
| S01-AC04 | DSR trên 70% | Nhãn `Từ chối`. DSR `70,34%`. Lý do: `Từ chối: DSR 70,34% vượt mức tối đa 70%.` (`RECO-M05`). Thặng dư `12.700.000 VND` (không phải lý do) | [khuyen-nghi-ltv-dsr.md dòng 53](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L53) |
| S01-AC05 | DSR đúng 50% | DSR `50,00%`; nhãn `Phê duyệt` (không phải Chuyển cấp trên); thặng dư `36.300.000 VND` | [khuyen-nghi-ltv-dsr.md dòng 54](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L54) |
| S01-AC06 | DSR đúng 70% | DSR `70,00%`; nhãn `Chuyển cấp trên`; lý do `Chuyển cấp trên: DSR 70% vượt 50%; chuyển cấp trên xem xét.` | [khuyen-nghi-ltv-dsr.md dòng 55](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L55) |
| S01-AC07 | DSR sát 50% | DSR hiện `50,00%`; nhãn `Phê duyệt` | [khuyen-nghi-ltv-dsr.md dòng 56](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L56) |
| S01-AC08 | Thặng dư đúng 3 triệu | Thặng dư `3.000.000 VND`; nhãn `Phê duyệt`; `Đáp ứng mọi quy tắc tín dụng.` | [khuyen-nghi-ltv-dsr.md dòng 57](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L57) |
| S01-AC09 | Thặng dư thiếu 1 đồng | Thặng dư `2.999.999 VND`; nhãn `Từ chối`; lý do `Từ chối: Thặng dư hằng tháng 2.999.999 VND thấp hơn 3.000.000 VND.` (`RECO-M07`). Với chi phí `58000… | [khuyen-nghi-ltv-dsr.md dòng 58](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L58) |
| S01-AC10 | Nhiều lý do cùng lúc | Nhãn `Từ chối`; mục `Lý do` liệt kê **ba dòng**: `Từ chối: LTV 81% vượt mức tối đa 80%.` · `Từ chối: DSR 77,18% vượt mức tối đa 70%.` · `Từ chối: Thặ… | [khuyen-nghi-ltv-dsr.md dòng 59](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L59) |
| S02-AC01 | LTV đúng 80% | Khung ghi `80,00% (LTV tối đa 80,00%)`; đầu trang LTV `80,00%`; Khuyến nghị `Phê duyệt` | [khuyen-nghi-ltv-dsr.md dòng 68](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L68) |
| S02-AC02 | LTV sát 80% | Đầu trang LTV `80,00%`; Khuyến nghị `Phê duyệt` | [khuyen-nghi-ltv-dsr.md dòng 69](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L69) |
| S02-AC03 | LTV 80,01% | Đầu trang LTV `80,01%`; Khuyến nghị `Từ chối` | [khuyen-nghi-ltv-dsr.md dòng 70](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L70) |
| S02-AC04 | LTV 81% | Đầu trang LTV `81,00%`, Khuyến nghị `Từ chối`. Khung Thẩm định: `81,00% (LTV tối đa 80,00%)`; lý do `Từ chối: LTV 81% vượt mức tối đa 80%.` (`RECO-M0… | [khuyen-nghi-ltv-dsr.md dòng 71](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L71) |
| S02-AC05 | LTV theo giá khai báo | LTV `64,00%` (Khuyến nghị `Phê duyệt`) rồi `106,67%` (Khuyến nghị `Từ chối`, lý do `ltvAboveMax`) | [khuyen-nghi-ltv-dsr.md dòng 72](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L72) |
| S02-AC06 | Lãi suất theo LTV | LTV → lãi suất thẩm định: `32%` → `9,80%`; `40%` → `9,80%`; `53,33%` → `9,90%`; `64%` → `10,05%`; `80%` → `10,30%` (và `106,67%` → `10,30%`) | [khuyen-nghi-ltv-dsr.md dòng 73](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L73) |
| S02-AC07 | Xây/sửa nhà | Đầu trang LTV `76,19%`, Khuyến nghị `Từ chối`. Khung: `76,19% (LTV tối đa 70,00%)`; lý do `Từ chối: LTV 76,19% vượt mức tối đa 70%.` Ô `Sản phẩm` tự… | [khuyen-nghi-ltv-dsr.md dòng 74](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L74) |
| S03-AC01 | DSR và thặng dư cơ bản | Khoản trả mới `40.800.000 VND`; thu nhập được tính `100.000.000 VND`; chi phí được tính `4.500.000 VND`; DSR `40,80%` (= 40.800.000 / 100.000.000); t… | [khuyen-nghi-ltv-dsr.md dòng 83](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L83) |
| S03-AC02 | Thu nhập cho thuê 70% | Thu nhập được tính `85.000.000 VND` (50 triệu + 70% × 50 triệu); DSR `48,00%`; nhãn `Phê duyệt`. Dưới ô cho thuê có dòng `Tính 70% thu nhập cho thuê… | [khuyen-nghi-ltv-dsr.md dòng 84](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L84) |
| S03-AC03 | Nợ hiện có | `Khoản trả nợ hiện có` `5.000.000 VND`; DSR `45,80%` (= (40.800.000 + 5.000.000) / 100.000.000); thặng dư `44.200.000 VND` | [khuyen-nghi-ltv-dsr.md dòng 85](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L85) |
| S03-AC04 | Chi phí nhập cao | `Chi phí được tính` `10.000.000 VND`; thặng dư `49.200.000 VND` | [khuyen-nghi-ltv-dsr.md dòng 86](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L86) |
| S03-AC05 | Chi phí để trống | `Chi phí được tính` `4.500.000 VND` | [khuyen-nghi-ltv-dsr.md dòng 87](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L87) |
| S03-AC06 | Người phụ thuộc | Người phụ thuộc 2: `Chi phí được tính` `8.500.000 VND` dù nhập 1.000.000 hoặc để trống; 5: `14.500.000 VND`; 20: `44.500.000 VND`. DSR không đổi. Nhậ… | [khuyen-nghi-ltv-dsr.md dòng 88](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L88) |
| S03-AC07 | Thời hạn vay | Khoản trả mới theo lãi suất thẩm định giảm từ `40.800.000` xuống `34.133.333 VND`; DSR `34,13%` (lương 100 triệu). Tuổi cao nhất khi đáo hạn tăng lên… | [khuyen-nghi-ltv-dsr.md dòng 89](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L89) |
| S03-AC08 | Phương thức trả nợ | Khoản trả mới `40.133.333` (Gốc đều) → `30.986.775 VND` (Niên kim); DSR `30,99%`; thặng dư `64.513.225 VND` | [khuyen-nghi-ltv-dsr.md dòng 90](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L90) |
| S03-AC09 | Ân hạn | Khoản trả mới tăng từ `30.986.775` lên `31.504.846 VND`; DSR `31,5%` | [khuyen-nghi-ltv-dsr.md dòng 91](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L91) |
| S03-AC10 | Sản phẩm | Lãi suất thẩm định `9,55%` (sản phẩm 12 tháng: `10,05%`); khoản trả mới `30.465.933 VND`; DSR `30,47%` | [khuyen-nghi-ltv-dsr.md dòng 92](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L92) |
| S03-AC11 | Số rất lớn không gây lỗi | Thu nhập được tính `99.999.999.999.999 VND`; DSR `0,00%`; thặng dư `99.999.915.366.666 VND`; nhãn `Phê duyệt`; không có thông báo lỗi | [khuyen-nghi-ltv-dsr.md dòng 93](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L93) |
| S04-AC01 | Thời hạn 20 năm | `Tuổi cao nhất khi đáo hạn` `56` | [khuyen-nghi-ltv-dsr.md dòng 102](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L102) |
| S04-AC02 | Tuổi 70 vẫn đạt | `assessment.recommendation` = `APPROVE`; `maxAgeAtMaturity` = `70`; `reasons` rỗng | [khuyen-nghi-ltv-dsr.md dòng 103](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L103) |
| S04-AC03 | Tuổi 71 bị từ chối | `recommendation` = `DECLINE`; lý do `assessment.ageAtMaturity` với `age` 71, `max` 70 (nghĩa: `Có người vay 71 tuổi khi đáo hạn; tối đa 70.`, `RECO-M… | [khuyen-nghi-ltv-dsr.md dòng 104](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L104) |
| S04-AC04 | Quá tuổi nhưng màn hình không báo | `Tuổi cao nhất khi đáo hạn` `76`. Khung Thẩm định **không có nhãn khuyến nghị và không có lý do**, lại hiện thông báo `RECO-M01` dù đã nhập đủ; đầu t… | [khuyen-nghi-ltv-dsr.md dòng 105](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L105) |
| S05-AC01 | Đầu trang sau khi lưu | Phản hồi chậm vài giây (4 giây sau vẫn `—`); sau đó ô Khuyến nghị thành `Phê duyệt`; bước `Tài chính` ghi `Đã xong`; ô `Lương hằng tháng` giữ giá trị… | [khuyen-nghi-ltv-dsr.md dòng 114](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L114) |
| S05-AC02 | Chưa lưu thì đầu trang giữ kết quả cũ | Khung Thẩm định ghi `Chuyển cấp trên` nhưng đầu trang vẫn `Phê duyệt` cho tới khi bấm `Lưu` | [khuyen-nghi-ltv-dsr.md dòng 115](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L115) |
| S05-AC03 | Lưu khi trống | `Đã lưu.` (`RECO-M11`); đầu trang Khuyến nghị về `—` | [khuyen-nghi-ltv-dsr.md dòng 116](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L116) |
| S05-AC04 | Ô tiền chỉ nhận chữ số | `abc` → ô để trống, quay về thông báo `RECO-M01`; `-5000000` → ô giữ `5000000` (dấu trừ bị bỏ), DSR `816,00%`, nhãn `Từ chối` với hai lý do (DSR và t… | [khuyen-nghi-ltv-dsr.md dòng 117](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L117) |
| S06-AC01 | Giao diện English | Khung tên `Assessment`, nhãn `Refer`; `Loan-to-value` `64.00% (Maximum LTV 80.00%)`; `Debt service ratio` `53.51%`; mục `Reasons`: `Refer: DSR 53.51%… | [khuyen-nghi-ltv-dsr.md dòng 124](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L124) |
| TL-01 | Làm tròn LTV và DSR đến 2 chữ số thập p… | Làm tròn LTV và DSR đến 2 chữ số thập phân, theo cách làm tròn gần nhất | [bang-soat-requirement.md dòng 47](bang-soat-requirement.md#L47) |
| TL-02 | Làm tròn LTV và DSR đến **2 chữ số thập… | Làm tròn LTV và DSR đến **2 chữ số thập phân** theo hướng **làm tròn lên** (về phía bất lợi cho người vay), rồi so với ngưỡng (LTV 80% và 70%, DSR 50… | [bang-soat-requirement.md dòng 48](bang-soat-requirement.md#L48) |

## 4. Yêu cầu theo BA của từng mã SRS
Gom từ bảng soát (mục 5, 6) để mỗi mã SRS có chỗ ghi điều BA trả lời, kể cả khi SRS (bản quan sát hệ thống 1.3.0) ghi khác. Test case viết theo cột "Theo BA"; chỗ có ⚠️ là nghi lỗi của hệ thống, chưa phải lỗi đã xác nhận. SRS không bị sửa.

| Mã | Tên ngắn | Theo BA (hoặc suy ra) | Hệ thống 1.3.0 hiện tại | Còn mở |
|---|---|---|---|---|
| M01 | Thông báo chưa đủ thông tin | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| M02 | Không có lý do | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| M03 | Dòng xem trước | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| M04 | LTV vượt tối đa | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| M05 | DSR vượt tối đa | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| M06 | DSR trên 50% | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| M07 | Thặng dư thấp | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| M08 | Quá tuổi | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| M09 | Định giá thấp hơn giá khai báo — **chưa… | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| M10 | CIC báo nhóm nợ — **chưa thấy** (chỉ tr… | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| M11 | Đã lưu | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| M12 | Nhãn khuyến nghị | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| R01 | LTV tối đa | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| R02 | DSR | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| R03 | Thặng dư tối thiểu | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| R04 | Tuổi lúc đáo hạn | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| R05 | LTV theo giá khai báo | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| R06 | Thu nhập cho thuê | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| R07 | Chi phí được tính | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| R08 | Khoản trả mới | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| R09 | Lãi suất thẩm định | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| R10 | Công thức DSR và thặng dư | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| R11 | Ô nhập tiền | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| R12 | Ngưỡng cố định hay cấu hình | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S01-AC01 | Chưa nhập thu nhập | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S01-AC02 | Đạt mọi quy tắc | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S01-AC03 | DSR trên 50% | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S01-AC04 | DSR trên 70% | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S01-AC05 | DSR đúng 50% | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S01-AC06 | DSR đúng 70% | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S01-AC07 | DSR sát 50% | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S01-AC08 | Thặng dư đúng 3 triệu | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S01-AC09 | Thặng dư thiếu 1 đồng | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S01-AC10 | Nhiều lý do cùng lúc | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S02-AC01 | LTV đúng 80% | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S02-AC02 | LTV sát 80% | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S02-AC03 | LTV 80,01% | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S02-AC04 | LTV 81% | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S02-AC05 | LTV theo giá khai báo | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S02-AC06 | Lãi suất theo LTV | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S02-AC07 | Xây/sửa nhà | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S03-AC01 | DSR và thặng dư cơ bản | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S03-AC02 | Thu nhập cho thuê 70% | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S03-AC03 | Nợ hiện có | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S03-AC04 | Chi phí nhập cao | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S03-AC05 | Chi phí để trống | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S03-AC06 | Người phụ thuộc | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S03-AC07 | Thời hạn vay | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S03-AC08 | Phương thức trả nợ | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S03-AC09 | Ân hạn | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S03-AC10 | Sản phẩm | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S03-AC11 | Số rất lớn không gây lỗi | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S04-AC01 | Thời hạn 20 năm | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S04-AC02 | Tuổi 70 vẫn đạt | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S04-AC03 | Tuổi 71 bị từ chối | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S04-AC04 | Quá tuổi nhưng màn hình không báo | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S05-AC01 | Đầu trang sau khi lưu | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S05-AC02 | Chưa lưu thì đầu trang giữ kết quả cũ | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S05-AC03 | Lưu khi trống | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S05-AC04 | Ô tiền chỉ nhận chữ số | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S06-AC01 | Giao diện English | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |

## 5. Từ requirement tới test case
| Mã | Tên ngắn | Trạng thái requirement | Test case |
|---|---|---|---|
| M01 | Thông báo chưa đủ thông tin | Không đổi | 1: TC-001 |
| M02 | Không có lý do | Không đổi | 2: TC-002, TC-008 |
| M03 | Dòng xem trước | Không đổi | 1: TC-002 |
| M04 | LTV vượt tối đa | Không đổi | 3: TC-010, TC-014, TC-016 |
| M05 | DSR vượt tối đa | Không đổi | 2: TC-007, TC-010 |
| M06 | DSR trên 50% | Không đổi | 2: TC-004, TC-036 |
| M07 | Thặng dư thấp | Không đổi | 2: TC-009, TC-010 |
| M08 | Quá tuổi | Không đổi | 1: TC-021 |
| M09 | Định giá thấp hơn giá khai báo — **chưa… | Không đổi | ⚠️ chưa có test case |
| M10 | CIC báo nhóm nợ — **chưa thấy** (chỉ tr… | Không đổi | ⚠️ chưa có test case |
| M11 | Đã lưu | Không đổi | 2: TC-022, TC-035 |
| M12 | Nhãn khuyến nghị | Không đổi | 1: TC-036 |
| R01 | LTV tối đa | Không đổi | 6: TC-011, TC-012, TC-013, TC-016, TC-017, TC-025 |
| R02 | DSR | Không đổi | 6: TC-003, TC-004, TC-005, TC-006, TC-007, TC-023 |
| R03 | Thặng dư tối thiểu | Không đổi | 2: TC-008, TC-009 |
| R04 | Tuổi lúc đáo hạn | Không đổi | 2: TC-020, TC-021 |
| R05 | LTV theo giá khai báo | Không đổi | 2: TC-015, TC-024 |
| R06 | Thu nhập cho thuê | Không đổi | 1: TC-018 |
| R07 | Chi phí được tính | Không đổi | 4: TC-027, TC-028, TC-029, TC-030 |
| R08 | Khoản trả mới | Không đổi | 3: TC-031, TC-032, TC-033 |
| R09 | Lãi suất thẩm định | Không đổi | 2: TC-026, TC-034 |
| R10 | Công thức DSR và thặng dư | Không đổi | 2: TC-001, TC-019 |
| R11 | Ô nhập tiền | Không đổi | 2: TC-037, TC-038 |
| R12 | Ngưỡng cố định hay cấu hình | Không đổi | ⚠️ chưa có test case |
| S01-AC01 | Chưa nhập thu nhập | Không đổi | 1: TC-001 |
| S01-AC02 | Đạt mọi quy tắc | Không đổi | 1: TC-002 |
| S01-AC03 | DSR trên 50% | Không đổi | 2: TC-004, TC-023 |
| S01-AC04 | DSR trên 70% | Không đổi | 1: TC-007 |
| S01-AC05 | DSR đúng 50% | Không đổi | 1: TC-003 |
| S01-AC06 | DSR đúng 70% | Không đổi | 1: TC-006 |
| S01-AC07 | DSR sát 50% | Không đổi | 1: TC-005 |
| S01-AC08 | Thặng dư đúng 3 triệu | Không đổi | 1: TC-008 |
| S01-AC09 | Thặng dư thiếu 1 đồng | Không đổi | 1: TC-009 |
| S01-AC10 | Nhiều lý do cùng lúc | Không đổi | 1: TC-010 |
| S02-AC01 | LTV đúng 80% | Không đổi | 1: TC-011 |
| S02-AC02 | LTV sát 80% | Không đổi | 1: TC-012 |
| S02-AC03 | LTV 80,01% | Không đổi | 1: TC-013 |
| S02-AC04 | LTV 81% | Không đổi | 1: TC-014 |
| S02-AC05 | LTV theo giá khai báo | Không đổi | 2: TC-015, TC-024 |
| S02-AC06 | Lãi suất theo LTV | Không đổi | 1: TC-026 |
| S02-AC07 | Xây/sửa nhà | Không đổi | 1: TC-016 |
| S03-AC01 | DSR và thặng dư cơ bản | Không đổi | 1: TC-002 |
| S03-AC02 | Thu nhập cho thuê 70% | Không đổi | 1: TC-018 |
| S03-AC03 | Nợ hiện có | Không đổi | 1: TC-019 |
| S03-AC04 | Chi phí nhập cao | Không đổi | 1: TC-027 |
| S03-AC05 | Chi phí để trống | Không đổi | 1: TC-028 |
| S03-AC06 | Người phụ thuộc | Không đổi | 2: TC-029, TC-030 |
| S03-AC07 | Thời hạn vay | Không đổi | 1: TC-031 |
| S03-AC08 | Phương thức trả nợ | Không đổi | 1: TC-032 |
| S03-AC09 | Ân hạn | Không đổi | 1: TC-033 |
| S03-AC10 | Sản phẩm | Không đổi | 1: TC-034 |
| S03-AC11 | Số rất lớn không gây lỗi | Không đổi | ⚠️ chưa có test case |
| S04-AC01 | Thời hạn 20 năm | Không đổi | ⚠️ chưa có test case |
| S04-AC02 | Tuổi 70 vẫn đạt | Không đổi | 1: TC-020 |
| S04-AC03 | Tuổi 71 bị từ chối | Không đổi | 1: TC-021 |
| S04-AC04 | Quá tuổi nhưng màn hình không báo | Không đổi | ⚠️ chưa có test case |
| S05-AC01 | Đầu trang sau khi lưu | Không đổi | 1: TC-022 |
| S05-AC02 | Chưa lưu thì đầu trang giữ kết quả cũ | Không đổi | ⚠️ chưa có test case |
| S05-AC03 | Lưu khi trống | Không đổi | 1: TC-035 |
| S05-AC04 | Ô tiền chỉ nhận chữ số | Không đổi | 2: TC-037, TC-038 |
| S06-AC01 | Giao diện English | Không đổi | 1: TC-036 |
| TL-01 | Làm tròn LTV và DSR đến 2 chữ số thập p… | Không đổi | — |
| TL-02 | Làm tròn LTV và DSR đến **2 chữ số thập… | Không đổi | 10: TC-004, TC-005, TC-006, TC-007, TC-010, TC-012, TC-016, TC-031, TC-033, TC-036 |

## 6. Từ test case tới requirement
| Mã | Tình huống | Ưu tiên | Mã requirement dùng | Trạng thái | Tạo | Sửa lần cuối | Tự động hóa |
|---|---|---|---|---|---|---|---|
| TC-001 | Không hiển thị khuyến nghị mà báo cần nhập đủ thông tin khi chưa nhập thu nhập | Cao | M01 (Thông báo chưa đủ thông tin), R10 (Công thức DSR và thặng dư), S01-AC01 (Chưa nhập thu nhập) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-002 | Hiển thị khuyến nghị Phê duyệt khi nhập lương 100 triệu và đạt mọi quy tắc | Cao | M02 (Không có lý do), M03 (Dòng xem trước), S01-AC02 (Đạt mọi quy tắc), S03-AC01 (DSR và thặng dư cơ bản) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-003 | Vẫn hiển thị Phê duyệt khi DSR đúng bằng mức 50% | Cao | R02 (DSR), S01-AC05 (DSR đúng 50%) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-004 | Hiển thị Chuyển cấp trên khi DSR vượt 50% một chút (50,38%) | Cao | M06 (DSR trên 50%), R02 (DSR), S01-AC03 (DSR trên 50%), TL-02 (Làm tròn LTV và DSR đến **2 chữ số thập…) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-005 | Hiển thị Chuyển cấp trên khi DSR chỉ hơn 50% rất ít (50,0006%) | Cao | R02 (DSR), S01-AC07 (DSR sát 50%), TL-02 (Làm tròn LTV và DSR đến **2 chữ số thập…) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-006 | Hiển thị Từ chối khi DSR chỉ hơn 70% rất ít (70,0000003%) | Cao | R02 (DSR), S01-AC06 (DSR đúng 70%), TL-02 (Làm tròn LTV và DSR đến **2 chữ số thập…) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-007 | Hiển thị Từ chối kèm lý do khi DSR vượt 70% (70,35%) | Cao | M05 (DSR vượt tối đa), R02 (DSR), S01-AC04 (DSR trên 70%), TL-02 (Làm tròn LTV và DSR đến **2 chữ số thập…) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-008 | Vẫn hiển thị Phê duyệt khi thặng dư hằng tháng đúng bằng mức tối thiểu 3.000.000 | Cao | M02 (Không có lý do), R03 (Thặng dư tối thiểu), S01-AC08 (Thặng dư đúng 3 triệu) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-009 | Hiển thị Từ chối kèm lý do khi thặng dư thiếu 1 đồng so với mức tối thiểu (2.999.999) | Cao | M07 (Thặng dư thấp), R03 (Thặng dư tối thiểu), S01-AC09 (Thặng dư thiếu 1 đồng) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-010 | Hiển thị Từ chối và liệt kê đủ ba lý do khi hồ sơ vi phạm cả LTV, DSR và thặng dư | Cao | M04 (LTV vượt tối đa), M05 (DSR vượt tối đa), M07 (Thặng dư thấp), S01-AC10 (Nhiều lý do cùng lúc), TL-02 (Làm tròn LTV và DSR đến **2 chữ số thập…) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-011 | Hiển thị Phê duyệt khi LTV của hồ sơ Mua nhà đúng bằng mức tối đa 80% | Cao | R01 (LTV tối đa), S02-AC01 (LTV đúng 80%) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-012 | Hiển thị Từ chối khi LTV chỉ hơn 80% rất ít (80,0025%) | Cao | R01 (LTV tối đa), S02-AC02 (LTV sát 80%), TL-02 (Làm tròn LTV và DSR đến **2 chữ số thập…) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-013 | Hiển thị Từ chối khi LTV là 80,01% | Cao | R01 (LTV tối đa), S02-AC03 (LTV 80,01%) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-014 | Hiển thị Từ chối kèm lý do LTV vượt mức khi LTV là 81% | Cao | M04 (LTV vượt tối đa), S02-AC04 (LTV 81%) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-015 | Hiển thị Từ chối khi giá trị khai báo 3 tỷ làm LTV lên 106,67% | Cao | R05 (LTV theo giá khai báo), S02-AC05 (LTV theo giá khai báo) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-016 | Hiển thị Từ chối theo mức tối đa 70% khi hồ sơ Xây/sửa nhà có LTV 76,20% | Cao | M04 (LTV vượt tối đa), R01 (LTV tối đa), S02-AC07 (Xây/sửa nhà), TL-02 (Làm tròn LTV và DSR đến **2 chữ số thập…) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-017 | Hiển thị Từ chối khi hồ sơ Xây/sửa nhà có LTV chỉ hơn 70% một chút (70,01%) | Cao | R01 (LTV tối đa) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-018 | Chỉ tính 70% thu nhập cho thuê vào thu nhập khi nhập cả lương và thu nhập cho thuê | Cao | R06 (Thu nhập cho thuê), S03-AC02 (Thu nhập cho thuê 70%) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-019 | Cộng khoản nợ hiện có vào DSR khi nhập nợ hiện có hằng tháng | Cao | R10 (Công thức DSR và thặng dư), S03-AC03 (Nợ hiện có) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-020 | Vẫn đạt (API trả APPROVE) khi thời hạn 34 năm khiến người vay 70 tuổi lúc đáo hạn | Cao | R04 (Tuổi lúc đáo hạn), S04-AC02 (Tuổi 70 vẫn đạt) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-021 | Bị từ chối (API trả DECLINE) khi thời hạn 35 năm khiến người vay 71 tuổi lúc đáo hạn | Cao | M08 (Quá tuổi), R04 (Tuổi lúc đáo hạn), S04-AC03 (Tuổi 71 bị từ chối) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-022 | Cập nhật khuyến nghị ở đầu trang hồ sơ sau vài giây khi nhập lương rồi bấm Lưu | Cao | M11 (Đã lưu), S05-AC01 (Đầu trang sau khi lưu) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-023 | Hiển thị Chuyển cấp trên khi DSR 54,40% (nằm giữa 50% và 70%) | Trung bình | R02 (DSR), S01-AC03 (DSR trên 50%) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-024 | Hiển thị Phê duyệt khi giá trị khai báo 5 tỷ cho LTV 64,00% | Trung bình | R05 (LTV theo giá khai báo), S02-AC05 (LTV theo giá khai báo) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-025 | Không bị loại vì LTV khi hồ sơ Xây/sửa nhà có LTV đúng bằng mức tối đa 70% | Trung bình | R01 (LTV tối đa) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-026 | Lãi suất thẩm định là 10,05% (xem ở API) khi LTV là 64% | Trung bình | R09 (Lãi suất thẩm định), S02-AC06 (Lãi suất theo LTV) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-027 | Dùng số chi phí đã nhập khi chi phí nhập cao hơn mức tối thiểu | Trung bình | R07 (Chi phí được tính), S03-AC04 (Chi phí nhập cao) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-028 | Tính chi phí mặc định 4.500.000 khi để trống chi phí và số người phụ thuộc | Trung bình | R07 (Chi phí được tính), S03-AC05 (Chi phí để trống) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-029 | Nâng chi phí lên 8.500.000 khi có 2 người phụ thuộc mà chi phí nhập thấp hơn mức tối thiểu | Trung bình | R07 (Chi phí được tính), S03-AC06 (Người phụ thuộc) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-030 | Giữ chi phí đã nhập khi có 2 người phụ thuộc và chi phí nhập cao hơn mức tối thiểu | Trung bình | R07 (Chi phí được tính), S03-AC06 (Người phụ thuộc) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-031 | Khoản trả mới giảm còn 34.133.333 khi đổi thời hạn vay từ 20 lên 40 năm | Trung bình | R08 (Khoản trả mới), S03-AC07 (Thời hạn vay), TL-02 (Làm tròn LTV và DSR đến **2 chữ số thập…) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-032 | Khoản trả mới là 30.986.775 khi đổi phương thức trả nợ sang Niên kim | Trung bình | R08 (Khoản trả mới), S03-AC08 (Phương thức trả nợ) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-033 | Khoản trả mới là 31.504.846 khi Niên kim có thêm ân hạn 12 tháng | Trung bình | R08 (Khoản trả mới), S03-AC09 (Ân hạn), TL-02 (Làm tròn LTV và DSR đến **2 chữ số thập…) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-034 | Lãi suất thẩm định đổi thành 9,55% khi chọn sản phẩm cố định 36 tháng | Trung bình | R09 (Lãi suất thẩm định), S03-AC10 (Sản phẩm) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-035 | Khuyến nghị ở đầu trang về “—” khi bấm Lưu lúc mọi ô tài chính để trống | Trung bình | M11 (Đã lưu), S05-AC03 (Lưu khi trống) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-036 | Khung thẩm định đổi sang tiếng Anh khi chọn giao diện English | Trung bình | M06 (DSR trên 50%), M12 (Nhãn khuyến nghị), S06-AC01 (Giao diện English), TL-02 (Làm tròn LTV và DSR đến **2 chữ số thập…) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-037 | Ô lương bị để trống khi gõ chữ “abc” vào ô lương | Thấp | R11 (Ô nhập tiền), S05-AC04 (Ô tiền chỉ nhận chữ số) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |
| TC-038 | Dấu trừ bị bỏ và ô lương giữ 5000000 khi gõ “-5000000” vào ô lương | Thấp | R11 (Ô nhập tiền), S05-AC04 (Ô tiền chỉ nhận chữ số) | Còn đúng | 2026-11-18 | 2026-11-18 | Chưa có |

## 7. Lịch sử thay đổi
Ghi mỗi lần chạy `chot`. **Thời điểm chốt** là giờ máy lúc bấm chốt (kèm múi giờ), không phải giờ BA trả lời hay giờ requirement đổi; mốc cũ chỉ có ngày thì ghi "không rõ giờ". **Commit gốc** là commit đang đứng lúc chốt ("+ sửa chưa commit" nghĩa là còn thay đổi chưa commit); muốn xem từng chữ đã đổi, dùng git. **Ngày BA trả lời** chỉ ghi khi biết.

| Thời điểm chốt (giờ máy) | Commit gốc | Ngày BA trả lời | Đối tượng | Nội dung | Dựa trên | Mã requirement đổi | Test case mới / sửa / bỏ |
|---|---|---|---|---|---|---|---|
| 2026-11-18 18:35:05 (+07:00) | `736f701` + sửa chưa commit | — | checklist, test-case | Lần đầu: 38 test case (file gộp), 7 mã SRS còn ❓ chưa có test case theo bảng soát | SRS 2026-11-17; bảng soát ?; TL đến TL-02 | M01 (mới), M02 (mới), M03 (mới), M04 (mới), M05 (mới), M06 (mới), M07 (mới), M08 (mới), M09 (mới), M10 (mới), M11 (mới), M12 (mới), R01 (mới), R02 (mới), R03 (mới), R04 (mới), R05 (mới), R06 (mới), R07 (mới), R08 (mới), R09 (mới), R10 (mới), R11 (mới), R12 (mới), S01-AC01 (mới), S01-AC02 (mới), S01-AC03 (mới), S01-AC04 (mới), S01-AC05 (mới), S01-AC06 (mới), S01-AC07 (mới), S01-AC08 (mới), S01-AC09 (mới), S01-AC10 (mới), S02-AC01 (mới), S02-AC02 (mới), S02-AC03 (mới), S02-AC04 (mới), S02-AC05 (mới), S02-AC06 (mới), S02-AC07 (mới), S03-AC01 (mới), S03-AC02 (mới), S03-AC03 (mới), S03-AC04 (mới), S03-AC05 (mới), S03-AC06 (mới), S03-AC07 (mới), S03-AC08 (mới), S03-AC09 (mới), S03-AC10 (mới), S03-AC11 (mới), S04-AC01 (mới), S04-AC02 (mới), S04-AC03 (mới), S04-AC04 (mới), S05-AC01 (mới), S05-AC02 (mới), S05-AC03 (mới), S05-AC04 (mới), S06-AC01 (mới), TL-01 (mới), TL-02 (mới) | mới 38; sửa 0; bỏ 0 |
| 2026-11-18 18:41:10 (+07:00) | `736f701` + sửa chưa commit | — | checklist, test-case | Viết lại cột Tình huống thành tên test case ngắn (điều kiện: kết quả); nội dung bước và kết quả không đổi | SRS 2026-11-17; bảng soát ?; TL đến TL-02 | — | mới 0; sửa TC-001, TC-002, TC-003, TC-004, TC-005, TC-006, TC-007, TC-008, TC-009, TC-010, TC-011, TC-012, TC-013, TC-014, TC-015, TC-016, TC-017, TC-018, TC-019, TC-020, TC-021, TC-022, TC-023, TC-024, TC-025, TC-026, TC-027, TC-028, TC-029, TC-030, TC-031, TC-032, TC-033, TC-034, TC-035, TC-036, TC-037, TC-038; bỏ 0 |
| 2026-11-18 18:43:00 (+07:00) | `736f701` + sửa chưa commit | — | checklist, test-case | Viết lại tên test case (cột Tình huống) thành câu đầy đủ dạng: kết quả khi điều kiện; bước và kết quả không đổi | SRS 2026-11-17; bảng soát ?; TL đến TL-02 | — | mới 0; sửa TC-001, TC-002, TC-003, TC-004, TC-005, TC-006, TC-007, TC-008, TC-009, TC-010, TC-011, TC-012, TC-013, TC-014, TC-015, TC-016, TC-017, TC-018, TC-019, TC-020, TC-021, TC-022, TC-023, TC-024, TC-025, TC-026, TC-027, TC-028, TC-029, TC-030, TC-031, TC-032, TC-033, TC-034, TC-035, TC-036, TC-037, TC-038; bỏ 0 |
| 2026-11-18 18:44:43 (+07:00) | `736f701` + sửa chưa commit | — | checklist, test-case | Viết Điều kiện trước thành danh sách gạch đầu dòng ngắn; nội dung điều kiện không đổi | SRS 2026-11-17; bảng soát ?; TL đến TL-02 | — | mới 0; sửa TC-001, TC-002, TC-003, TC-004, TC-005, TC-006, TC-007, TC-008, TC-009, TC-010, TC-011, TC-012, TC-013, TC-014, TC-015, TC-016, TC-017, TC-018, TC-019, TC-020, TC-021, TC-022, TC-023, TC-024, TC-025, TC-026, TC-027, TC-028, TC-029, TC-030, TC-031, TC-032, TC-033, TC-034, TC-035, TC-036, TC-037, TC-038; bỏ 0 |
| 2026-11-18 18:44:57 (+07:00) | `736f701` + sửa chưa commit | — | checklist, test-case | Điều kiện trước còn 4 gạch đầu dòng ngắn; nội dung điều kiện không đổi | SRS 2026-11-17; bảng soát ?; TL đến TL-02 | — | mới 0; sửa TC-001, TC-002, TC-003, TC-004, TC-005, TC-006, TC-007, TC-008, TC-009, TC-010, TC-011, TC-012, TC-013, TC-014, TC-015, TC-016, TC-017, TC-018, TC-019, TC-020, TC-021, TC-022, TC-023, TC-024, TC-025, TC-026, TC-027, TC-028, TC-029, TC-030, TC-031, TC-032, TC-033, TC-034, TC-035, TC-036, TC-037, TC-038; bỏ 0 |
| 2026-11-18 18:46:12 (+07:00) | `736f701` + sửa chưa commit | — | checklist, test-case | Điều kiện trước rút còn 2 gạch + gạch riêng; hồ sơ nền định nghĩa một lần ở đầu file | SRS 2026-11-17; bảng soát ?; TL đến TL-02 | — | mới 0; sửa 0; bỏ 0 |
| 2026-11-18 18:46:31 (+07:00) | `736f701` + sửa chưa commit | — | checklist, test-case | Điều kiện trước rút còn 2 gạch chung + gạch riêng của ca; hồ sơ nền định nghĩa một lần ở đầu file | SRS 2026-11-17; bảng soát ?; TL đến TL-02 | — | mới 0; sửa 0; bỏ 0 |
| 2026-11-18 18:46:48 (+07:00) | `736f701` + sửa chưa commit | — | checklist, test-case | Điều kiện trước rút còn 2 gạch chung + gạch riêng của ca; hồ sơ nền định nghĩa một lần ở đầu file (hai lần chốt trước cùng lượt chưa đổi nội dung) | SRS 2026-11-17; bảng soát ?; TL đến TL-02 | — | mới 0; sửa TC-001, TC-002, TC-003, TC-004, TC-005, TC-006, TC-007, TC-008, TC-009, TC-010, TC-011, TC-012, TC-013, TC-014, TC-015, TC-016, TC-017, TC-018, TC-019, TC-020, TC-021, TC-022, TC-023, TC-024, TC-025, TC-026, TC-027, TC-028, TC-029, TC-030, TC-031, TC-032, TC-033, TC-034, TC-035, TC-036, TC-037, TC-038; bỏ 0 |
| 2026-11-18 18:47:09 (+07:00) | `736f701` + sửa chưa commit | — | checklist, test-case | Hồ sơ nền định nghĩa một lần ở đầu file; Điều kiện trước còn 2 gạch chung + gạch riêng; nội dung điều kiện không đổi | SRS 2026-11-17; bảng soát ?; TL đến TL-02 | — | mới 0; sửa 0; bỏ 0 |
| 2026-11-18 18:51:05 (+07:00) | `736f701` + sửa chưa commit | — | checklist, test-case | Điều kiện trước chỉ ghi dữ kiện cần cho từng ca (bỏ đăng nhập, bỏ mục hồ sơ nền ở đầu file); bỏ chữ tự nhập mật khẩu ở bước 1 | SRS 2026-11-17; bảng soát ?; TL đến TL-02 | — | mới 0; sửa TC-001, TC-002, TC-003, TC-004, TC-005, TC-006, TC-007, TC-008, TC-009, TC-010, TC-011, TC-012, TC-013, TC-014, TC-015, TC-016, TC-017, TC-018, TC-019, TC-020, TC-021, TC-022, TC-023, TC-024, TC-025, TC-026, TC-027, TC-028, TC-029, TC-030, TC-031, TC-032, TC-033, TC-034, TC-035, TC-036, TC-037, TC-038; bỏ 0 |
| 2026-11-18 18:59:51 (+07:00) | `0534aba` + sửa chưa commit | — | checklist, test-case | Viết lại cột Nguồn thành câu thường + link tới dòng SRS (neo thêm vào SRS, truy-vet.py bỏ thẻ neo khi băm); mã và nội dung requirement không đổi | SRS 2026-11-17; bảng soát ?; TL đến TL-02 | — | mới 0; sửa TC-001, TC-002, TC-003, TC-004, TC-005, TC-006, TC-007, TC-008, TC-009, TC-010, TC-011, TC-012, TC-013, TC-014, TC-015, TC-016, TC-017, TC-018, TC-019, TC-020, TC-021, TC-022, TC-023, TC-024, TC-025, TC-026, TC-027, TC-028, TC-029, TC-030, TC-031, TC-032, TC-033, TC-034, TC-035, TC-036, TC-037, TC-038; bỏ 0 |
| 2026-11-18 19:04:01 (+07:00) | `a042890` + sửa chưa commit | — | checklist, test-case | Thêm điều kiện người vay Tester Mot cho ca tuổi lúc đáo hạn và tài sản chưa định giá cho các ca LTV; đối chiếu số liệu bằng script, khớp hết | SRS 2026-11-17; bảng soát ?; TL đến TL-02 | — | mới 0; sửa TC-011, TC-012, TC-013, TC-014, TC-016, TC-017, TC-020, TC-021, TC-025; bỏ 0 |
