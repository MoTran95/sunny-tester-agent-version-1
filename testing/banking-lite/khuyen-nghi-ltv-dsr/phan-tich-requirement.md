# Phân tích requirement — Khuyến nghị thẩm định xem trước LTV/DSR (Banking Lite)

| | |
|---|---|
| Nguồn requirement | [srs/banking-lite/khuyen-nghi-ltv-dsr.md](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md) (mã `RECO`, tình trạng **nháp**, hệ thống 1.3.0) |
| Ngày phân tích | 2026-11-17 |
| Mục đích file | Lưu kết quả phân tích để **viết test case chi tiết** sau này; không cần mở lại cuộc trò chuyện |
| Phạm vi | Chỉ kiểm thử **chức năng (functional)**. Không suy diễn bảo mật, hiệu năng |
| Quy mô | 62 mục checklist (TC), 18 câu hỏi cho BA (CH), 16 câu hỏi dựa trên kinh nghiệm (KN) |
| Tình trạng | Checklist **chưa được xác nhận**. Chưa viết test case chi tiết |
| Câu hỏi gửi BA | Bản đọc là hiểu, có ví dụ và cách đang hiểu: [cau-hoi-cho-ba.md](cau-hoi-cho-ba.md). Các câu hỏi CH và KN trong file này là bản ghi gốc, dùng để tra chéo |

## 1. Cách đọc file
- **TC-xx**: một mục checklist = một test case sau này. Mỗi TC chỉ có **một mục tiêu và một dữ liệu**; không gộp, kể cả khi chỉ khác dữ liệu.
- Cột **Nguồn** = mã requirement (mã sẵn có của SRS, không gán mã mới) kèm **trích nguyên văn** từ SRS. Kết quả mong đợi nằm trong phần trích này.
- **CẦN XÁC NHẬN → CH-xx / KN-xx**: nguồn chưa đủ để viết cụ thể phần đó; câu hỏi tương ứng nằm ở mục 5 hoặc 6. Khi viết test case, ghi "CẦN XÁC NHẬN" ở phần liên quan, không tự điền.
- **CH-xx**: câu hỏi có dấu vết ngay trong SRS (SRS ghi `chưa rõ`, tự mâu thuẫn, hoặc ghi `chưa kiểm/chưa thấy`). Hỏi BA sớm.
- **KN-xx**: câu hỏi dựa trên kinh nghiệm kiểm thử, SRS không có dấu vết. Để riêng, **chỉ hỏi khi cần**.

### Quy ước ưu tiên
| Mức | TC | CH / KN |
|---|---|---|
| **Cao** | Nếu sai thì nhãn khuyến nghị sai, hoặc việc có/không có khuyến nghị sai, hoặc mất dữ liệu đã nhập | Chặn việc viết hoặc chạy TC mức Cao, hoặc có thể đảo kết luận đạt/không đạt |
| **Trung bình** | Nếu sai thì số liệu, lý do hoặc trạng thái hiển thị sai nhưng nhãn có thể vẫn đúng | Ảnh hưởng TC mức Trung bình hoặc phạm vi test |
| **Thấp** | Nội dung phụ trợ: dòng giải thích, dòng nhỏ, định dạng, ngôn ngữ | Hiển thị phụ hoặc ngoài phạm vi hiện tại |

Cơ sở của mức ưu tiên lấy từ mục đích của feature trong SRS: hệ thống tính một khuyến nghị `Phê duyệt`, `Chuyển cấp trên` hoặc `Từ chối`.

## 2. Vì sao có nhiều test case và nhiều câu hỏi
**Vì sao 62 TC** (Cao 22, Trung bình 34, Thấp 6):
1. **Luật "một mục tiêu, một dữ liệu"**: 30 tiêu chí chấp nhận (AC) được đưa vào checklist, nhưng nhiều AC chứa nhiều kết quả hoặc nhiều dữ liệu (ví dụ S02-AC06 có 6 điểm LTV, S03-AC06 có 3 tổ hợp chi phí). Tách theo luật nên ra 62 TC.
2. **Mỗi ngưỡng cần ca biên**: LTV 80,00% / 80,01% (R01), DSR đúng 50,00% (R02), thặng dư 3.000.000 / 2.999.999 (R03), tuổi 70 / 71 (R04). Sai một ngưỡng là kết luận sai.
3. **Mỗi nhãn kết quả cần ca riêng**: Phê duyệt, Chuyển cấp trên, Từ chối; Từ chối đến từ nhiều luật (LTV, DSR, thặng dư, tuổi) nên mỗi luật có ca riêng.
4. **Mỗi thông báo cần ít nhất một ca**: M01 đến M07, M11, M12 (M08 chỉ kiểm qua API; M09, M10 chưa kiểm được).
5. **Mỗi công thức tính cần ca riêng**: DSR, thặng dư, 70% thu nhập cho thuê, chi phí tối thiểu, khoản trả mới (đổi theo thời hạn, phương thức, ân hạn, sản phẩm), lãi suất thẩm định.
6. **Hiển thị ở hai nơi**: khung Thẩm định (đổi ngay) và đầu trang hồ sơ (chỉ đổi sau khi Lưu) cần kiểm riêng.

**Vì sao 18 câu hỏi CH**: SRS tự ghi 7 điểm `chưa rõ` (Q01 đến Q07), ghi phần `chưa khám phá` ở mục 6.2, và có hai chỗ số liệu tự lệch (S01-AC06, S03-AC11) mà TC không thể dựa vào. Mỗi câu hỏi là một chỗ mà nếu viết kết quả mong đợi thì phải tự đoán.

**Vì sao 16 câu hỏi KN**: do kinh nghiệm kiểm thử (tổ hợp luật, danh sách giá trị, khoảng hợp lệ, trạng thái, cách nhập thật). SRS không có dấu vết nên **không hỏi ngay**; chỉ hỏi khi cần viết TC cho phần đó.

**Đã loại vì ngoài phạm vi functional**: câu hỏi về độ trễ khi cập nhật đầu trang sau Lưu (hiệu năng). Không có TC hay câu hỏi về bảo mật.

## 3. Dữ liệu nền và điều kiện tiên quyết (trích nguyên văn SRS)
Đây là bối cảnh mà phần lớn TC dùng; mỗi test case chi tiết phải chép đầy đủ vào phần điều kiện trước của mình, không viết "như hồ sơ nền".

> **Mọi ví dụ dưới đây dùng cùng một hồ sơ nền** (trừ khi ghi khác): mục đích `Mua nhà`, sản phẩm 12 tháng, trả `Gốc đều`, vay `3.200.000.000 VND`, thời hạn `20` năm, giá trị khai báo `4.000.000.000 VND` (LTV `80,00%`), người vay `Tester Mot` (cao nhất khi đáo hạn `56` tuổi), không có thu nhập cho thuê, nợ hiện có, chi phí hay người phụ thuộc. Khoản trả mới theo lãi suất thẩm định khi đó là `40.800.000 VND` mỗi tháng.

> - Đăng nhập P100001 (người dùng gõ mật khẩu; mật khẩu **không** ghi trong tài liệu).
> - Có một **hồ sơ nháp** của mình. Bước `Tài chính` chỉ mở **sau khi hoàn thành bước `Người vay`**: hồ sơ vừa tạo bằng `Tạo hồ sơ mới` hiện `Bước này mở sau khi hoàn thành: Người vay` ([E20](#e20)). Cách nhanh nhất: `Tạo từ hồ sơ có sẵn` (chọn một khách hàng và một tài sản) — hồ sơ mới có sẵn người vay (đã qua VNeID) và tài sản.
> - Để có khuyến nghị cần đủ: người vay, **số tiền vay và thời hạn** (bước `Khoản vay và tài sản`), **tài sản có giá trị khai báo**, và **thu nhập** (bước `Tài chính`).

Thuật ngữ (trích nguyên văn SRS mục 1):

> - **LTV** (Tỷ lệ cho vay/giá trị): số tiền vay chia giá trị tài sản bảo đảm, tính bằng %.
> - **DSR** (Tỷ lệ trả nợ trên thu nhập): tiền phải trả nợ mỗi tháng chia thu nhập mỗi tháng, tính bằng %.
> - **Thặng dư hằng tháng:** tiền còn lại mỗi tháng sau khi trừ chi phí và các khoản trả nợ.
> - **CIC:** báo cáo tín dụng của khách hàng, hệ thống lấy khi gửi thẩm định chính thức.

## 4. Checklist test (Bảng 1)

### RECO-S01 — Biết khuyến nghị và lý do ngay khi nhập thu nhập

| ID | Tên checklist | Ưu tiên | Lý do viết riêng | Nguồn |
|---|---|---|---|---|
| TC-01 | Kiểm tra khung Thẩm định không hiện nhãn khuyến nghị và mục Lý do, mà hiện thông báo yêu cầu nhập đủ thông tin, khi chưa nhập thu nhập | Cao | Nhánh không có khuyến nghị khi thiếu thu nhập: kiểm nhãn, mục Lý do và thông báo M01. | RECO-S01-AC01; RECO-M01; RECO-R10 — “Khung `Thẩm định` **không có nhãn khuyến nghị** và **không có mục `Lý do`**. Có thông báo xanh `Nhập đủ thông tin người vay, khoản vay, tài sản và thu nhập để xem khuyến nghị.` (`RECO-M01`).” · **CẦN XÁC NHẬN** → KN-02 |
| TC-02 | Kiểm tra các chỉ số LTV, khoản trả mới, thu nhập được tính, chi phí được tính, DSR, thặng dư, tuổi đáo hạn vẫn hiện khi chưa nhập thu nhập | Trung bình | Mục tiêu khác với việc kiểm thông báo: ở đây kiểm giá trị 7 chỉ số vẫn được tính khi thu nhập bằng 0. | RECO-S01-AC01; RECO-R10 — “Các chỉ số vẫn hiện: LTV `80,00% (LTV tối đa 80,00%)`; khoản trả mới `40.800.000 VND`; thu nhập được tính `0 VND`; chi phí được tính `4.500.000 VND`; DSR `—`; thặng dư `-45.300.000 VND`; tuổi cao nhất khi đáo hạn `56`” · **CẦN XÁC NHẬN** → KN-02, KN-03 |
| TC-03 | Kiểm tra nhãn khuyến nghị là Phê duyệt khi lương 100.000.000 VND và đạt mọi quy tắc | Cao | Nhánh Phê duyệt: kết quả cuối của hồ sơ đạt mọi quy tắc. | RECO-S01-AC02; RECO-R02; RECO-M12 — “Nhãn `Phê duyệt`.” |
| TC-04 | Kiểm tra dòng nhỏ "Xem trước…" hiện dưới nhãn khi khuyến nghị là Phê duyệt (lương 100.000.000 VND) | Thấp | Dòng nhỏ M03 là thông báo riêng, không quyết định nhãn. | RECO-S01-AC02; RECO-M03 — “Dòng nhỏ `Xem trước: thẩm định chính thức chạy khi gửi, có dữ liệu CIC.` (`RECO-M03`).” |
| TC-05 | Kiểm tra mục Lý do hiện câu "Đáp ứng mọi quy tắc tín dụng." khi không vi phạm quy tắc nào (lương 100.000.000 VND) | Trung bình | Thông báo M02 chỉ xuất hiện khi không có lý do nào; là một thông báo riêng. | RECO-S01-AC02; RECO-M02 — “Mục `Lý do`: `Đáp ứng mọi quy tắc tín dụng.` (`RECO-M02`)” |
| TC-06 | Kiểm tra nhãn Chuyển cấp trên và lý do M06 khi lương 81.000.000 VND (DSR 50,38% sau làm tròn lên) | Cao | Nhánh Chuyển cấp trên (DSR trên 50% đến 70%) và câu lý do M06. | RECO-S01-AC03; RECO-R02; RECO-M06; RECO-M12 — “Nhãn `Chuyển cấp trên`. DSR `50,37%`. Lý do: `Chuyển cấp trên: DSR 50,37% vượt 50%; chuyển cấp trên xem xét.` (`RECO-M06`).” · **ĐỔI THEO TL-02:** DSR hiển thị đúng phải là 50,38% (SRS ghi 50,37%); lý do “Chuyển cấp trên: DSR 50,38% vượt 50%; chuyển cấp trên xem xét.” |
| TC-07 | Kiểm tra nhãn Chuyển cấp trên khi lương 75.000.000 VND (DSR 54,40%) | Cao | Cùng nhánh với một dữ liệu khác (DSR 54,40%); luật không gộp nên tách riêng theo dữ liệu. | RECO-S01-AC03; RECO-R02 — “Cùng kết quả với lương `75000000` (DSR `54,40%`)” |
| TC-08 | Kiểm tra nhãn Từ chối và lý do M05 khi lương 58.000.000 VND (DSR 70,35% sau làm tròn lên) | Cao | Nhánh Từ chối do DSR trên 70% và câu lý do M05. | RECO-S01-AC04; RECO-R02; RECO-M05 — “Nhãn `Từ chối`. DSR `70,34%`. Lý do: `Từ chối: DSR 70,34% vượt mức tối đa 70%.` (`RECO-M05`).” · **ĐỔI THEO TL-02:** DSR hiển thị đúng phải là 70,35% (SRS ghi 70,34%); lý do “Từ chối: DSR 70,35% vượt mức tối đa 70%.” |
| TC-09 | Kiểm tra nhãn vẫn là Phê duyệt (không phải Chuyển cấp trên) khi DSR đúng 50,00% (lương 81.600.000 VND) | Cao | Ngưỡng biên DSR đúng 50,00%: phân biệt Phê duyệt với Chuyển cấp trên. | RECO-S01-AC05; RECO-R02 — “DSR `50,00%`; nhãn `Phê duyệt` (không phải Chuyển cấp trên); thặng dư `36.300.000 VND`” |
| TC-10 | Kiểm tra nhãn Phê duyệt khi thặng dư đúng 3.000.000 VND (lương 100.000.000, chi phí sinh hoạt 56.200.000) | Cao | Ngưỡng biên thặng dư đúng 3.000.000: còn đạt. | RECO-S01-AC08; RECO-R03; RECO-M02 — “Thặng dư `3.000.000 VND`; nhãn `Phê duyệt`; `Đáp ứng mọi quy tắc tín dụng.`” |
| TC-11 | Kiểm tra nhãn Từ chối và lý do M07 khi thặng dư 2.999.999 VND (lương 100.000.000, chi phí sinh hoạt 56.200.001) | Cao | Ngưỡng biên thặng dư thiếu 1 đồng: Từ chối và câu lý do M07. | RECO-S01-AC09; RECO-R03; RECO-M07 — “Thặng dư `2.999.999 VND`; nhãn `Từ chối`; lý do `Từ chối: Thặng dư hằng tháng 2.999.999 VND thấp hơn 3.000.000 VND.` (`RECO-M07`).” |
| TC-12 | Kiểm tra nhãn Từ chối khi thặng dư 1.200.000 VND (lương 100.000.000, chi phí sinh hoạt 58.000.000) | Trung bình | Điểm xa ngưỡng thặng dư; dữ liệu khác nên tách riêng. Rủi ro thấp hơn ca biên vì ca biên đã có TC. | RECO-S01-AC09; RECO-R03 — “Với chi phí `58000000`: thặng dư `1.200.000 VND`, cũng `Từ chối`” |
| TC-13 | Kiểm tra mục Lý do liệt kê ba dòng LTV, DSR, thặng dư khi vay 3.240.000.000, nợ hiện có 5.000.000, 5 người phụ thuộc, lương 60.000.000 | Cao | Nhiều luật vi phạm cùng lúc: kiểm cả nhãn và danh sách ba dòng lý do. | RECO-S01-AC10; RECO-M04; RECO-M05; RECO-M07 — “Nhãn `Từ chối`; mục `Lý do` liệt kê **ba dòng**: `Từ chối: LTV 81% vượt mức tối đa 80%.` · `Từ chối: DSR 77,18% vượt mức tối đa 70%.` · `Từ chối: Thặng dư hằng tháng -810.000 VND thấp hơn 3.000.000 VND.`” · **ĐỔI THEO TL-02:** DSR trong dòng lý do phải là 77,19% (SRS ghi 77,18%) · **CẦN XÁC NHẬN** → KN-01 |

### RECO-S02 — Biết khoản vay có vượt mức tối đa so với giá trị tài sản không (LTV)

| ID | Tên checklist | Ưu tiên | Lý do viết riêng | Nguồn |
|---|---|---|---|---|
| TC-14 | Kiểm tra khung Thẩm định ghi "80,00% (LTV tối đa 80,00%)" khi mua nhà, vay 3,2 tỷ, giá trị khai báo 4 tỷ | Trung bình | Khung Thẩm định (hiện ngay) khác nơi hiển thị với đầu trang hồ sơ (sau khi Lưu). | RECO-S02-AC01; RECO-R01 — “Khung ghi `80,00% (LTV tối đa 80,00%)`” |
| TC-15 | Kiểm tra đầu trang hồ sơ hiện LTV 80,00% và Khuyến nghị Phê duyệt khi vay 3,2 tỷ, giá trị khai báo 4 tỷ, lương 100.000.000 đã lưu | Cao | Ngưỡng biên LTV đúng 80,00% (mua nhà): còn đạt. | RECO-S02-AC01; RECO-R01 — “đầu trang LTV `80,00%`; Khuyến nghị `Phê duyệt`” |
| TC-16 | Kiểm tra đầu trang hồ sơ hiện LTV 80,01% và Khuyến nghị Từ chối khi vay 3.200.400.000, giá trị khai báo 4 tỷ | Cao | Ngưỡng biên LTV 80,01%: vượt mức tối đa. | RECO-S02-AC03; RECO-R01 — “Đầu trang LTV `80,01%`; Khuyến nghị `Từ chối`” |
| TC-17 | Kiểm tra đầu trang hồ sơ hiện LTV 81,00% và Khuyến nghị Từ chối khi vay 3.240.000.000, giá trị khai báo 4 tỷ | Cao | LTV vượt tối đa: kiểm kết quả ở đầu trang. | RECO-S02-AC04; RECO-R01 — “Đầu trang LTV `81,00%`, Khuyến nghị `Từ chối`.” |
| TC-18 | Kiểm tra khung Thẩm định ghi "81,00% (LTV tối đa 80,00%)" và lý do M04 khi vay 3.240.000.000, giá trị khai báo 4 tỷ | Trung bình | Nơi hiển thị khác đầu trang: kiểm khung Thẩm định và câu lý do M04. | RECO-S02-AC04; RECO-M04 — “Khung Thẩm định: `81,00% (LTV tối đa 80,00%)`; lý do `Từ chối: LTV 81% vượt mức tối đa 80%.` (`RECO-M04`)” |
| TC-19 | Kiểm tra LTV 64,00% và Khuyến nghị Phê duyệt, tính theo giá trị khai báo, khi tài sản chưa định giá, vay 3,2 tỷ, giá trị khai báo 5 tỷ | Cao | R05: cách tính LTV khi chưa định giá (nhánh Phê duyệt). | RECO-S02-AC05; RECO-R05 — “LTV `64,00%` (Khuyến nghị `Phê duyệt`)” · **CẦN XÁC NHẬN** → CH-06 |
| TC-20 | Kiểm tra LTV 106,67% và Khuyến nghị Từ chối khi tài sản chưa định giá, vay 3,2 tỷ, giá trị khai báo 3 tỷ | Trung bình | R05 với dữ liệu khác (LTV trên 100%, nhánh Từ chối); dữ liệu khác nên tách riêng. | RECO-S02-AC05; RECO-R05 — “`106,67%` (Khuyến nghị `Từ chối`, lý do `ltvAboveMax`)” · **CẦN XÁC NHẬN** → CH-06, CH-18 |
| TC-21 | Kiểm tra lãi suất thẩm định là 9,80% khi LTV 32% (mua nhà, sản phẩm 12 tháng, vay 3,2 tỷ, giá trị khai báo 10 tỷ) | Trung bình | R09: mỗi điểm LTV đã đo là một dữ liệu riêng; lãi suất thẩm định quyết định khoản trả mới rồi DSR. | RECO-S02-AC06; RECO-R09 — “`32%` → `9,80%`” · **CẦN XÁC NHẬN** → CH-09 |
| TC-22 | Kiểm tra lãi suất thẩm định là 9,80% khi LTV 40% (mua nhà, sản phẩm 12 tháng, vay 3,2 tỷ, giá trị khai báo 8 tỷ) | Trung bình | R09: mỗi điểm LTV đã đo là một dữ liệu riêng; lãi suất thẩm định quyết định khoản trả mới rồi DSR. | RECO-S02-AC06; RECO-R09 — “`40%` → `9,80%`” · **CẦN XÁC NHẬN** → CH-09 |
| TC-23 | Kiểm tra lãi suất thẩm định là 9,90% khi LTV 53,34% (53,333…% làm tròn lên) (mua nhà, sản phẩm 12 tháng, vay 3,2 tỷ, giá trị khai báo 6 tỷ) | Trung bình | R09: mỗi điểm LTV đã đo là một dữ liệu riêng; lãi suất thẩm định quyết định khoản trả mới rồi DSR. | RECO-S02-AC06; RECO-R09 — “`53,33%` → `9,90%`” · **ĐỔI THEO TL-02:** LTV hiển thị đúng phải là 53,34% (SRS ghi 53,33%) · **CẦN XÁC NHẬN** → CH-09 |
| TC-24 | Kiểm tra lãi suất thẩm định là 10,05% khi LTV 64% (mua nhà, sản phẩm 12 tháng, vay 3,2 tỷ, giá trị khai báo 5 tỷ) | Trung bình | R09: mỗi điểm LTV đã đo là một dữ liệu riêng; lãi suất thẩm định quyết định khoản trả mới rồi DSR. | RECO-S02-AC06; RECO-R09 — “`64%` → `10,05%`” · **CẦN XÁC NHẬN** → CH-09 |
| TC-25 | Kiểm tra lãi suất thẩm định là 10,30% khi LTV 80% (mua nhà, sản phẩm 12 tháng, vay 3,2 tỷ, giá trị khai báo 4 tỷ) | Trung bình | R09: mỗi điểm LTV đã đo là một dữ liệu riêng; lãi suất thẩm định quyết định khoản trả mới rồi DSR. | RECO-S02-AC06; RECO-R09 — “`80%` → `10,30%`” · **CẦN XÁC NHẬN** → CH-09 |
| TC-26 | Kiểm tra lãi suất thẩm định là 10,30% khi LTV 106,67% (mua nhà, sản phẩm 12 tháng, vay 3,2 tỷ, giá trị khai báo 3 tỷ) | Thấp | R09: mỗi điểm LTV đã đo là một dữ liệu riêng; lãi suất thẩm định quyết định khoản trả mới rồi DSR. | RECO-S02-AC06; RECO-R09 — “(và `106,67%` → `10,30%`)” · **CẦN XÁC NHẬN** → CH-09 |
| TC-27 | Kiểm tra đầu trang hồ sơ hiện LTV 76,20% và Khuyến nghị Từ chối khi mục đích Xây/sửa nhà, giá trị khai báo 4,2 tỷ | Cao | R01: mục đích Xây/sửa nhà có LTV tối đa khác (70%). | RECO-S02-AC07; RECO-R01 — “Đầu trang LTV `76,19%`, Khuyến nghị `Từ chối`.” · **ĐỔI THEO TL-02:** LTV hiển thị đúng phải là 76,20% (SRS ghi 76,19%) · **CẦN XÁC NHẬN** → KN-06, KN-07 |
| TC-28 | Kiểm tra khung Thẩm định ghi "76,20% (LTV tối đa 70,00%)" và lý do M04 khi mục đích Xây/sửa nhà, giá trị khai báo 4,2 tỷ | Trung bình | Nơi hiển thị khác đầu trang: kiểm mức tối đa 70% và câu lý do M04. | RECO-S02-AC07; RECO-R01; RECO-M04 — “Khung: `76,19% (LTV tối đa 70,00%)`; lý do `Từ chối: LTV 76,19% vượt mức tối đa 70%.`” · **ĐỔI THEO TL-02:** khung ghi “76,20% (LTV tối đa 70,00%)”, lý do “Từ chối: LTV 76,20% vượt mức tối đa 70%.” (SRS ghi 76,19%) · **CẦN XÁC NHẬN** → KN-06, KN-07 |

### RECO-S03 — Thu nhập, chi phí và các khoản trả nợ ảnh hưởng thế nào đến DSR và thặng dư

| ID | Tên checklist | Ưu tiên | Lý do viết riêng | Nguồn |
|---|---|---|---|---|
| TC-29 | Kiểm tra DSR là 40,80% khi lương 100.000.000 VND (hồ sơ nền, khoản trả mới 40.800.000) | Cao | Công thức DSR là đầu vào quyết định của nhãn. | RECO-S03-AC01; RECO-R10 — “DSR `40,80%` (= 40.800.000 / 100.000.000)” |
| TC-30 | Kiểm tra thặng dư hằng tháng là 54.700.000 VND khi lương 100.000.000 VND (hồ sơ nền) | Cao | Công thức thặng dư là đầu vào quyết định của nhãn; khác công thức DSR nên tách riêng. | RECO-S03-AC01; RECO-R10 — “thặng dư `54.700.000 VND` (= 100.000.000 − 4.500.000 − 40.800.000)” |
| TC-31 | Kiểm tra thu nhập được tính là 85.000.000 VND (chỉ tính 70% thu nhập cho thuê) khi lương 50.000.000 và thu nhập cho thuê 50.000.000 | Cao | R06: tỷ lệ 70% thu nhập cho thuê làm thay đổi thu nhập và DSR. | RECO-S03-AC02; RECO-R06 — “Thu nhập được tính `85.000.000 VND` (50 triệu + 70% × 50 triệu); DSR `48,00%`; nhãn `Phê duyệt`.” · **CẦN XÁC NHẬN** → KN-04 |
| TC-32 | Kiểm tra dòng giải thích 70% hiện dưới ô Thu nhập cho thuê hằng tháng | Thấp | Nội dung giải thích hiển thị riêng, không ảnh hưởng kết quả tính. | RECO-S03-AC02; RECO-R06 — “Dưới ô cho thuê có dòng `Tính 70% thu nhập cho thuê vào khả năng trả nợ.`” |
| TC-33 | Kiểm tra DSR là 45,80% khi lương 100.000.000, chi phí 10.000.000, khoản trả nợ hiện có 5.000.000 | Cao | Nợ hiện có cộng vào tử số của DSR. | RECO-S03-AC03; RECO-R10 — “`Khoản trả nợ hiện có` `5.000.000 VND`; DSR `45,80%` (= (40.800.000 + 5.000.000) / 100.000.000)” |
| TC-34 | Kiểm tra thặng dư là 44.200.000 VND khi lương 100.000.000, chi phí 10.000.000, khoản trả nợ hiện có 5.000.000 | Trung bình | Nợ hiện có trừ vào thặng dư: công thức khác với DSR nên kiểm riêng. | RECO-S03-AC03; RECO-R10 — “thặng dư `44.200.000 VND`” |
| TC-35 | Kiểm tra chi phí được tính là 10.000.000 và thặng dư 49.200.000 khi lương 100.000.000, chi phí nhập 10.000.000, không có người phụ thuộc | Trung bình | R07: chi phí nhập cao hơn mức tối thiểu thì dùng số nhập. | RECO-S03-AC04; RECO-R07 — “`Chi phí được tính` `10.000.000 VND`; thặng dư `49.200.000 VND`” |
| TC-36 | Kiểm tra chi phí được tính là 4.500.000 khi lương 100.000.000, ô chi phí và người phụ thuộc để trống | Trung bình | R07: nhánh chi phí để trống dùng mức mặc định. | RECO-S03-AC05; RECO-R07 — “`Chi phí được tính` `4.500.000 VND`” |
| TC-37 | Kiểm tra chi phí được tính là 8.500.000 khi 2 người phụ thuộc và chi phí nhập 1.000.000 | Trung bình | R07: người phụ thuộc nâng mức chi phí tối thiểu khi chi phí nhập thấp hơn. | RECO-S03-AC06; RECO-R07 — “Người phụ thuộc 2: `Chi phí được tính` `8.500.000 VND` dù nhập 1.000.000 hoặc để trống” · **CẦN XÁC NHẬN** → CH-10, KN-08 |
| TC-38 | Kiểm tra chi phí được tính là 8.500.000 khi 2 người phụ thuộc và ô chi phí để trống | Trung bình | R07: cùng quy tắc nhưng ô chi phí trống; dữ liệu khác nên tách riêng. | RECO-S03-AC06; RECO-R07 — “Người phụ thuộc 2: `Chi phí được tính` `8.500.000 VND` dù nhập 1.000.000 hoặc để trống” · **CẦN XÁC NHẬN** → CH-10, KN-08 |
| TC-39 | Kiểm tra chi phí được tính vẫn là 10.000.000 khi 2 người phụ thuộc và chi phí nhập 10.000.000 | Trung bình | R07: chi phí nhập cao hơn mức tối thiểu của 2 người phụ thuộc thì dùng số nhập. | RECO-S03-AC06; RECO-R07 — “Nhập chi phí `10000000` + người phụ thuộc 2 thì vẫn `10.000.000 VND`” · **CẦN XÁC NHẬN** → CH-10, KN-08 |
| TC-40 | Kiểm tra khoản trả mới giảm còn 34.133.333 VND khi đổi thời hạn vay từ 20 năm sang 40 năm (Gốc đều, vay 3,2 tỷ) | Trung bình | R08: thời hạn làm đổi khoản trả mới. | RECO-S03-AC07; RECO-R08 — “Khoản trả mới theo lãi suất thẩm định giảm từ `40.800.000` xuống `34.133.333 VND`” · **CẦN XÁC NHẬN** → CH-04, KN-04 |
| TC-41 | Kiểm tra DSR là 34,14% khi thời hạn vay 40 năm và lương 100.000.000 | Trung bình | DSR đổi theo khoản trả mới; kiểm riêng với giá trị khoản trả mới. | RECO-S03-AC07; RECO-R08 — “DSR `34,13%` (lương 100 triệu)” · **ĐỔI THEO TL-02:** DSR hiển thị đúng phải là 34,14% (SRS ghi 34,13%) · **CẦN XÁC NHẬN** → CH-04, KN-04 |
| TC-42 | Kiểm tra tuổi cao nhất khi đáo hạn là 76 khi thời hạn vay 40 năm | Trung bình | Tuổi đáo hạn đổi theo thời hạn vay. | RECO-S03-AC07; RECO-R04 — “Tuổi cao nhất khi đáo hạn tăng lên `76`” · **CẦN XÁC NHẬN** → KN-03 |
| TC-43 | Kiểm tra khoản trả mới là 40.133.333 VND khi phương thức Gốc đều, vay 3,2 tỷ, 20 năm, LTV 64% | Trung bình | R08: giá trị mốc của phương thức Gốc đều. | RECO-S03-AC08; RECO-R08 — “Khoản trả mới `40.133.333` (Gốc đều)” · **CẦN XÁC NHẬN** → KN-04 |
| TC-44 | Kiểm tra khoản trả mới là 30.986.775 VND khi đổi sang Niên kim (số tiền trả đều), vay 3,2 tỷ, 20 năm, LTV 64% | Trung bình | R08: phương thức trả nợ làm đổi khoản trả mới. | RECO-S03-AC08; RECO-R08 — “`30.986.775 VND` (Niên kim)” · **CẦN XÁC NHẬN** → KN-04 |
| TC-45 | Kiểm tra khoản trả mới tăng lên 31.504.846 VND khi nhập thời gian ân hạn 12 tháng (Niên kim, vay 3,2 tỷ, 20 năm, LTV 64%) | Trung bình | R08: ân hạn làm đổi khoản trả mới. | RECO-S03-AC09; RECO-R08 — “Khoản trả mới tăng từ `30.986.775` lên `31.504.846 VND`” · **CẦN XÁC NHẬN** → KN-04 |
| TC-46 | Kiểm tra lãi suất thẩm định là 9,55% khi chọn sản phẩm "Vay mua nhà, cố định 7,80% trong 36 tháng" (LTV 64%, Niên kim, ân hạn 12 tháng) | Trung bình | R09: sản phẩm làm đổi lãi suất thẩm định. | RECO-S03-AC10; RECO-R09 — “Lãi suất thẩm định `9,55%` (sản phẩm 12 tháng: `10,05%`)” · **CẦN XÁC NHẬN** → CH-09 |
| TC-47 | Kiểm tra khoản trả mới là 30.465.933 VND khi chọn sản phẩm "Vay mua nhà, cố định 7,80% trong 36 tháng" (LTV 64%, Niên kim, ân hạn 12 tháng) | Trung bình | Sản phẩm làm đổi khoản trả mới; khác mục tiêu với việc kiểm lãi suất thẩm định. | RECO-S03-AC10; RECO-R08 — “khoản trả mới `30.465.933 VND`” · **CẦN XÁC NHẬN** → CH-09, KN-04 |

### RECO-S04 — Bị loại khi người vay quá tuổi lúc đáo hạn

| ID | Tên checklist | Ưu tiên | Lý do viết riêng | Nguồn |
|---|---|---|---|---|
| TC-48 | Kiểm tra API trả APPROVE, tuổi tối đa 70, không có lý do khi tuổi cao nhất lúc đáo hạn là 70 (thời hạn 34 năm, lương 100.000.000) | Cao | R04: ngưỡng biên tuổi 70 — còn đạt. | RECO-S04-AC02; RECO-R04 — “`assessment.recommendation` = `APPROVE`; `maxAgeAtMaturity` = `70`; `reasons` rỗng” · **CẦN XÁC NHẬN** → KN-03, KN-16 |
| TC-49 | Kiểm tra API trả DECLINE kèm lý do quá tuổi khi tuổi cao nhất lúc đáo hạn là 71 (thời hạn 35 năm, lương 100.000.000) | Cao | R04: ngưỡng biên tuổi 71 — bị Từ chối. | RECO-S04-AC03; RECO-R04; RECO-M08 — “`recommendation` = `DECLINE`; lý do `assessment.ageAtMaturity` với `age` 71, `max` 70 (nghĩa: `Có người vay 71 tuổi khi đáo hạn; tối đa 70.`, `RECO-M08`)” · **CẦN XÁC NHẬN** → CH-04, KN-03, KN-16 |

### RECO-S05 — Khuyến nghị ở đầu trang hồ sơ và lưu dữ liệu

| ID | Tên checklist | Ưu tiên | Lý do viết riêng | Nguồn |
|---|---|---|---|---|
| TC-50 | Kiểm tra ô Khuyến nghị đầu trang đổi thành Phê duyệt khi nhập lương 100.000.000, nợ hiện có 5.000.000, 5 người phụ thuộc rồi bấm Lưu | Cao | Đầu trang chỉ đổi sau khi Lưu: kiểm kết quả hiển thị cuối cùng ở nơi người dùng nhìn nhanh nhất. | RECO-S05-AC01; RECO-M11 — “sau đó ô Khuyến nghị thành `Phê duyệt`” |
| TC-51 | Kiểm tra bước Tài chính ghi "Đã xong" sau khi nhập lương 100.000.000, nợ 5.000.000, 5 người phụ thuộc và bấm Lưu | Trung bình | Trạng thái bước là kết quả hiển thị riêng sau Lưu. | RECO-S05-AC01 — “bước `Tài chính` ghi `Đã xong`” · **CẦN XÁC NHẬN** → KN-12 |
| TC-52 | Kiểm tra ô Lương hằng tháng giữ giá trị khi mở lại hồ sơ sau khi lưu lương 100.000.000 | Cao | Dữ liệu đã nhập phải còn sau khi Lưu và mở lại; mất dữ liệu là lỗi nặng. | RECO-S05-AC01 — “ô `Lương hằng tháng` giữ giá trị khi mở lại” |
| TC-53 | Kiểm tra hiện thông báo "Đã lưu." khi bấm Lưu lúc mọi ô tài chính để trống | Trung bình | Thông báo M11 là thông báo riêng của nhánh lưu khi trống. | RECO-S05-AC03; RECO-M11 — “`Đã lưu.` (`RECO-M11`)” |
| TC-54 | Kiểm tra ô Khuyến nghị đầu trang về "—" khi bấm Lưu lúc mọi ô tài chính để trống | Trung bình | Kết quả hiển thị khác với kiểm thông báo; nhánh lưu khi trống khác nhánh lưu có dữ liệu. | RECO-S05-AC03 — “đầu trang Khuyến nghị về `—`” · **CẦN XÁC NHẬN** → KN-12 |
| TC-55 | Kiểm tra ô Lương hằng tháng để trống và quay về thông báo M01 khi điền "abc" (điền bằng công cụ) | Trung bình | R11: một giá trị không hợp lệ (chữ). | RECO-S05-AC04; RECO-R11; RECO-M01 — “`abc` → ô để trống, quay về thông báo `RECO-M01`” · **CẦN XÁC NHẬN** → CH-13, KN-10 |
| TC-56 | Kiểm tra ô Lương hằng tháng giữ 5.000.000 (bỏ dấu trừ), DSR 816,00% và nhãn Từ chối khi điền "-5000000" (điền bằng công cụ) | Trung bình | R11: một giá trị không hợp lệ khác (dấu trừ); kết quả khác hẳn nên tách riêng. | RECO-S05-AC04; RECO-R11 — “`-5000000` → ô giữ `5000000` (dấu trừ bị bỏ), DSR `816,00%`, nhãn `Từ chối` với hai lý do (DSR và thặng dư)” · **CẦN XÁC NHẬN** → CH-13, KN-10 |

### RECO-S06 — Xem khuyến nghị bằng tiếng Anh

| ID | Tên checklist | Ưu tiên | Lý do viết riêng | Nguồn |
|---|---|---|---|---|
| TC-57 | Kiểm tra khung tên "Assessment" và nhãn "Refer" khi giao diện English, vay 3,2 tỷ, LTV 64%, lương 75.000.000 | Thấp | Ngôn ngữ English: mỗi thành phần hiển thị là một kiểm tra riêng (khung tên và nhãn). | RECO-S06-AC01; RECO-M12 — “Khung tên `Assessment`, nhãn `Refer`” |
| TC-58 | Kiểm tra dòng "Loan-to-value" ghi "64.00% (Maximum LTV 80.00%)" khi giao diện English, vay 3,2 tỷ, LTV 64%, lương 75.000.000 | Trung bình | Ngôn ngữ English: nhãn và định dạng số của LTV. | RECO-S06-AC01 — “`Loan-to-value` `64.00% (Maximum LTV 80.00%)`” |
| TC-59 | Kiểm tra dòng "Debt service ratio" ghi "53.52%" khi giao diện English, vay 3,2 tỷ, LTV 64%, lương 75.000.000 | Trung bình | Ngôn ngữ English: nhãn và giá trị DSR. | RECO-S06-AC01 — “`Debt service ratio` `53.51%`” · **ĐỔI THEO TL-02:** giá trị đúng phải là 53.52% (SRS ghi 53.51%) |
| TC-60 | Kiểm tra mục Reasons hiện câu "Refer: DSR 53.52% is above 50%; refer to a senior assessor." khi giao diện English, lương 75.000.000 | Trung bình | Ngôn ngữ English: câu lý do M06. | RECO-S06-AC01; RECO-M06 — “mục `Reasons`: `Refer: DSR 53.51% is above 50%; refer to a senior assessor.`” · **ĐỔI THEO TL-02:** câu đúng phải là “Refer: DSR 53.52% is above 50%; refer to a senior assessor.” (SRS ghi 53.51%) |
| TC-61 | Kiểm tra số tiền viết "40,133,333 VND" (dấu phẩy ngăn nghìn, dấu chấm thập phân) khi giao diện English | Thấp | Ngôn ngữ English: quy tắc viết số khác tiếng Việt. | RECO-S06-AC01 — “Số viết `40,133,333 VND` (dấu phẩy ngăn nghìn, dấu chấm thập phân)” · **CẦN XÁC NHẬN** → CH-17 |
| TC-62 | Kiểm tra đầu trang hồ sơ ghi "Recommendation: Approve" khi giao diện English, hồ sơ đã lưu Phê duyệt | Thấp | Ngôn ngữ English: nhãn đầu trang hồ sơ. | RECO-S06-AC01; RECO-M12 — “Đầu trang: `Recommendation` `Approve`” · **CẦN XÁC NHẬN** → CH-17 |

### Ghi nhận riêng (không gộp, không xóa)
Các TC dưới đây trùng một phần dữ liệu hoặc kết quả. Số lượng và mã TC được giữ nguyên.
- TC-03 đến TC-05 (lương 100.000.000) trùng điều kiện với TC-29 và TC-30; cùng một lần chạy cho cả hai nhóm nhưng mục tiêu kiểm tra khác nhau.
- TC-02 và TC-36 cùng thấy chi phí được tính 4.500.000 khi chưa nhập chi phí.
- TC-13 trùng điều kiện LTV 81% với TC-17 và TC-18; khác ở việc có thêm DSR và thặng dư vi phạm.
- TC-43 (40.133.333) và TC-61 (`40,133,333`) là cùng một giá trị, khác ngôn ngữ giao diện.
- TC-37 và TC-38 có cùng nguồn; khác nhau ở việc chi phí nhập 1.000.000 hay để trống.

### Có thể bổ sung TC (chờ bạn xác nhận, chưa thêm)
Sau TL-02 (làm tròn lên 2 chữ số thập phân), ba ca biên trước đây chưa có TC đã đủ căn cứ. Theo luật giữ nguyên số lượng và mã TC, mình **chưa thêm**; nếu bạn đồng ý sẽ thêm ở cuối với mã mới, không đổi mã cũ. **Hệ thống hiện tại cho kết quả khác** ở cả ba ca (nghi lỗi nếu BA xác nhận TL-02):
- Lương 58.285.714 VND (DSR thật 70,0000003%, làm tròn lên 70,01%): kết quả mong đợi **Từ chối**; hệ thống hiện tại cho Chuyển cấp trên. Nguồn: RECO-S01-AC06, RECO-R02.
- Lương 81.599.000 VND (DSR thật 50,0006%, làm tròn lên 50,01%): kết quả mong đợi **Chuyển cấp trên**; hệ thống hiện tại cho Phê duyệt. Nguồn: RECO-S01-AC07, RECO-R02.
- Số tiền vay 3.200.100.000 VND (LTV thật 80,0025%, làm tròn lên 80,01%): kết quả mong đợi **Từ chối**; hệ thống hiện tại cho Phê duyệt. Nguồn: RECO-S02-AC02, RECO-R01.

### TC đã đổi theo TL-02 (làm tròn lên áp dụng cả khi hiển thị)
Tên và cột Nguồn của các TC sau đã đổi số hiển thị cho đúng TL-02 (cột Nguồn ghi **ĐỔI THEO TL-02**; trích nguyên văn vẫn là số hệ thống đang hiển thị): TC-06 (50,38%), TC-08 (70,35%), TC-13 (77,19%), TC-23 (53,34%), TC-27 và TC-28 (76,20%), TC-41 (34,14%), TC-59 và TC-60 (53,52%). Mã và số lượng TC không đổi. Các TC ca biên (TC-09, TC-15, TC-16) không bị ảnh hưởng vì số đã chính xác.

## 5. Câu hỏi cho BA (Bảng 2) — có dấu vết trong SRS

### 5.1 Câu trả lời đã nhận
| Mã | Nội dung trả lời | Nguồn | Áp dụng cho | Còn lại |
|---|---|---|---|---|
| TL-01 | Làm tròn LTV và DSR đến 2 chữ số thập phân, theo cách làm tròn gần nhất | Bạn (tester) ngày 2026-11-17: “làm tròn 2 số thập phân và làm tròn theo gần nhất” | CH-02, CH-03, KN-05 | **Đã bị thay thế bởi TL-02** cùng ngày |
| TL-02 | Làm tròn LTV và DSR đến **2 chữ số thập phân** theo hướng **làm tròn lên** (về phía bất lợi cho người vay), rồi so với ngưỡng | Bạn (tester) chọn phương án C ngày 2026-11-17, thay cho TL-01. Chưa có xác nhận của BA | CH-02, CH-03, KN-05 (các AC S01-AC06, S01-AC07, S02-AC02) | Thặng dư vẫn so theo số đồng nguyên. **Phạm vi:** áp dụng **cả khi hiển thị** (bạn chốt cùng ngày). **Hệ thống hiện tại làm tròn gần nhất** nên khác kết quả mong đợi ở ba ca biên và ở các số % hiển thị (nghi lỗi nếu BA xác nhận TL-02). Nên có BA hoặc PO xác nhận trước khi cập nhật SRS |

### 5.2 Danh sách câu hỏi

| ID | Vấn đề | Câu hỏi | Ưu tiên | Lý do phải hỏi (ảnh hưởng nếu không hỏi) | TC liên quan | Nguồn |
|---|---|---|---|---|---|---|
| CH-01 | **[Căn cứ]** Tài liệu ở tình trạng nháp: kết quả chỉ là hành vi đã quan sát, chưa được xác nhận. | Có xác nhận các hành vi nhãn `đã thấy` là kết quả mong đợi chính thức không? | Cao | Test case viết theo hành vi hiện tại có thể coi lỗi thật là "đạt". | — | RECO (toàn tài liệu) — “**nháp** — chỉ ghi hành vi quan sát được, chưa xác nhận với team” |
| CH-02 | ✅ **Đã có trả lời (TL-02, xem mục 5.1).** **[Quy tắc xử lý, mâu thuẫn]** LTV và DSR hiện làm tròn 2 chữ số rồi vẫn đạt (80,0025% hiện 80,00%; DSR thật 50,0006% hiện 50,00%), nhưng thặng dư thì so từng đồng. R01 viết như một quy tắc, còn Q01 ghi chưa rõ. | So ngưỡng LTV và DSR theo số làm tròn hay số thật? | Cao | Hai ca biên (S01-AC07, S02-AC02) chưa có TC vì chưa biết kết quả đạt hay không đạt. | — | RECO-S01-AC07; RECO-S02-AC02; RECO-R01; RECO-R02 (Q01) — “DSR thật 50,0006% hiện `50,00%` → Phê duyệt; LTV thật 80,0025% hiện `80,00%` → Phê duyệt; nhưng thặng dư 2.999.999 → Từ chối” · “Nhận biết "vượt" theo số hiển thị 2 chữ số thập phân” |
| CH-03 | ✅ **Đã có trả lời (TL-02, xem mục 5.1).** **[Dữ liệu, mâu thuẫn số liệu]** AC gọi là "DSR đúng 70,00%". Tính lại từ số trong tài liệu: 40.800.000 ÷ 58.285.714 ≈ 70,0000003%, tức trên 70% theo số thật, mà kết quả vẫn là Chuyển cấp trên. Chỉ lương 81.600.000 mới cho DSR đúng 50%. | Lương nào là ca biên 70% chuẩn? Kết quả Chuyển cấp trên ở đây có phải do làm tròn trước khi so không? | Cao | Ca biên 70% lấy từ AC này có thể sai; chưa có TC cho biên 70%. | — | RECO-S01-AC06; RECO-R02 — “DSR đúng 70,00% là Chuyển cấp trên, chưa phải Từ chối” |
| CH-04 | **[Hiển thị, mâu thuẫn]** API trả Từ chối khi quá tuổi, nhưng màn hình không hiện nhãn hay lý do, lại hiện thông báo M01 dù đã nhập đủ. Chỉ thử 40 năm trên màn hình, chưa thử 35 năm (71 tuổi). | Quá tuổi 70 có phải hiện Từ chối kèm M08 trên màn hình? Các chỉ số (DSR, khoản trả mới) có còn hiện không? | Cao | Không biết kết quả đúng trên màn hình; có thể bỏ lọt một lỗi thật. | TC-40, TC-41, TC-49 | RECO-S04-AC04; RECO-R04; RECO-M01; RECO-M08 (Q02) — “Khung Thẩm định **không có nhãn khuyến nghị và không có lý do**, lại hiện thông báo `RECO-M01` dù đã nhập đủ” |
| CH-05 | **[Người dùng, dữ liệu]** Quy tắc nhắc nhiều người vay, nhưng tài liệu ghi hồ sơ nhiều người vay là ngoài phạm vi. | Hồ sơ nhiều người vay có thuộc phạm vi test không? Thu nhập, nợ và tuổi lấy theo người nào? | Trung bình | Không thiết kế được test cho R04, M08, M10 với nhiều người vay. | — | RECO-R04; RECO-M08; RECO-M10 — “hồ sơ nhiều người vay (xem mục 6.2)” · “`Có người vay {age} tuổi khi đáo hạn; tối đa {max}.`” |
| CH-06 | **[Tích hợp, quy tắc]** LTV khi tài sản đã định giá chưa được kiểm tra. M09 chưa có ngưỡng `{max}` và chưa biết nhãn kết quả. | Đã định giá thì LTV dùng giá nào? Ngưỡng chênh lệch tối đa là bao nhiêu và kết quả là nhãn nào? | Trung bình | Không có kết quả mong đợi cho hồ sơ đã định giá; TC-19 và TC-20 chỉ đúng cho tài sản chưa định giá. | TC-19, TC-20 | RECO-R05; RECO-M09 — “Khi đã định giá: chưa kiểm tra.” · “`Giá định giá thấp hơn giá khai báo {shortfall}% (quá {max}%).`” |
| CH-07 | **[Tích hợp CIC]** Chưa biết nhóm nợ nào kích hoạt M10, nhãn kết quả là gì, và M10 có hiện ở bản xem trước hay chỉ ở bản chính thức. | Nhóm nợ nào gây Từ chối hoặc Chuyển cấp trên? M10 có xuất hiện ở bản xem trước không? | Trung bình | Không viết được test cho thông báo M10. | — | RECO-M10 — “`CIC báo người vay {borrower} thuộc nhóm nợ {group}.`” |
| CH-08 | **[Quy tắc xử lý, trạng thái]** Bản xem trước khác bản chính thức thế nào chưa rõ. Hai câu của bước quyết định chưa thấy trên màn hình. | Cùng số liệu thì bản xem trước và bản chính thức có khớp không? Từ chối có chặn phê duyệt không? Chuyển cấp trên có buộc ghi lý do không? | Thấp | Tài liệu xếp phần này ngoài phạm vi; chỉ ảnh hưởng khi mở rộng test sang bước quyết định. | — | RECO-M03; RECO-Q07 — “Đây là bản **xem trước**: dòng chữ trên màn hình nói `thẩm định chính thức chạy khi gửi, có dữ liệu CIC`” · “`Không thể phê duyệt hồ sơ được khuyến nghị từ chối.` và `Ghi rõ lý do phê duyệt hồ sơ được khuyến nghị chuyển cấp trên.`” |
| CH-09 | **[Quy tắc xử lý, hiển thị]** Lãi suất thẩm định chỉ có các điểm đo. Khoảng giữa các điểm (40–53,33%, 64–80%), tác động của sản phẩm và mục đích chưa rõ. Chưa rõ lãi suất này hiện trên màn hình hay chỉ trong API. | Quy tắc tính lãi suất thẩm định theo LTV, sản phẩm, mục đích? Giá trị này hiển thị ở đâu? | Trung bình | Chỉ test được đúng các điểm đã đo (TC-21 đến TC-26, TC-46, TC-47). | TC-21, TC-22, TC-23, TC-24, TC-25, TC-26, TC-46, TC-47 | RECO-R09; RECO-S02-AC06; RECO-S03-AC10 (Q04) — “Đổi theo LTV và theo sản phẩm.” |
| CH-10 | **[Quy tắc xử lý]** Công thức chi phí tối thiểu chỉ suy từ 3 điểm (2, 5, 20 người phụ thuộc). Chi phí nhập thấp hơn bị nâng lên mà người dùng không được báo. | Công thức chính thức của chi phí tối thiểu? Việc nâng chi phí nhập thấp lên có chủ ý không? | Trung bình | Sai kết quả ở các điểm chưa đo (người phụ thuộc 1, 3, 4…). | TC-37, TC-38, TC-39 | RECO-R07; RECO-S03-AC05; RECO-S03-AC06 (Q03) — “`4.500.000 + 2.000.000 × số người phụ thuộc` (8,5 / 14,5 / 44,5 triệu), kể cả khi nhập chi phí thấp hơn” |
| CH-11 | **[Dữ liệu đầu vào]** Bối cảnh của ba AC không ghi lương, nợ, người phụ thuộc, nhưng kết quả có DSR và thặng dư (30,99%, 64.513.225, 30,47%). | Điều kiện đầy đủ (lương, chi phí, nợ) của ba ca này là gì? | Trung bình | Phần DSR và thặng dư của ba AC chưa dùng được; checklist chỉ giữ phần khoản trả mới và lãi suất. | — | RECO-S03-AC08; RECO-S03-AC09; RECO-S03-AC10 — “Vay `3200000000`, 20 năm, LTV 64% (lãi suất thẩm định 10,05%)” |
| CH-12 | **[Dữ liệu, mâu thuẫn số liệu]** Với hồ sơ nền, thặng dư phải là 99.999.954.699.999 (= thu nhập − 4.500.000 − 40.800.000), nhưng tài liệu ghi lệch 39.333.333. Hiệu số 84.633.333 khớp chi phí 44.500.000 (20 người phụ thuộc) cộng khoản trả mới 40.133.333 (có thể là trạng thái dư của lượt thử trước, cần xác nhận). | Số đúng là bao nhiêu và trạng thái hồ sơ khi thử là gì? | Trung bình | Kết quả mong đợi của ca số rất lớn có thể sai; chưa có TC cho ca này. | — | RECO-S03-AC11; RECO-R10; RECO-R11 — “Nhập lương `99999999999999` (chưa lưu)” · “thặng dư `99.999.915.366.666 VND`” |
| CH-13 | **[Dữ liệu đầu vào]** Ô tiền chỉ được thử bằng công cụ điền, chưa gõ từng phím. `-5000000` trở thành 5.000.000 (bỏ dấu trừ). | Ô tiền chỉ nhận chữ số là quy tắc chính thức? Việc bỏ dấu trừ thành 5.000.000 có chủ ý không? | Trung bình | TC-55 và TC-56 chỉ phản ánh cách điền bằng công cụ. | TC-55, TC-56 | RECO-R11; RECO-S05-AC04 — “đã thấy (điền bằng công cụ, chưa gõ từng phím)” |
| CH-14 | **[Hiển thị, trạng thái]** Chưa lưu thì đầu trang giữ kết quả cũ. Có thể là chủ ý hoặc là lỗi hiển thị. | Đầu trang chỉ phản ánh bản đã lưu là chủ ý không? Có cần chú thích không? | Trung bình | Không biết nên ghi "đạt" hay "lỗi"; chưa có TC cho ca này. | — | RECO-S05-AC02; RECO-Q05 — “Đầu trang chỉ phản ánh bản đã lưu — chủ ý? Có cần chú thích?” · “Khung Thẩm định ghi `Chuyển cấp trên` nhưng đầu trang vẫn `Phê duyệt` cho tới khi bấm `Lưu`” |
| CH-15 | **[Người dùng và vai trò]** P200001 và P300001 chưa được thử với feature này. | P200001 và P300001 có thấy khung Thẩm định và ô Khuyến nghị không, hiển thị thế nào? | Trung bình | Không có ca cho hai vai trò này. | — | RECO mục 1 (vai trò) — “Chưa thử (cần người dùng gõ mật khẩu)” |
| CH-16 | **[Quy tắc xử lý]** Ngưỡng 50%, 70%, 3.000.000, tuổi 70, LTV 80/70 hiện là hằng số; `/api/settings` trả danh sách rỗng. | Các ngưỡng này cố định hay cấu hình được? Ai được đổi? | Trung bình | Nếu cấu hình được thì TC dùng ngưỡng cứng sẽ sai khi cấu hình đổi. | — | RECO-R12 (Q06) — “`GET /api/settings` trả `{"release":"1.3.0","settings":{}}` — không chứa ngưỡng nào.” |
| CH-17 | **[Thông báo]** Bản English của M01, M02, M04, M05, M07, M08, M09, M10 chỉ thấy trong tệp giao diện, chưa thấy trên màn hình. M11 chưa thấy bản English. | Văn bản English chính thức của các thông báo này là gì? | Thấp | TC tiếng Anh chỉ gồm phần đã thấy trên màn hình (S06-AC01). | TC-61, TC-62 | RECO-M01; RECO-M02; RECO-M04; RECO-M05; RECO-M07; RECO-M08; RECO-M09; RECO-M10; RECO-M11; RECO-S06-AC01 — “`Enter the borrower, loan, property and income details to see a recommendation.` (chỉ thấy trong tệp giao diện)” · “chưa thấy bản English” |
| CH-18 | **[Hiển thị]** Chỉ số hiện 2 chữ số thập phân (`81,00%`), lý do bỏ số 0 cuối (`81%`), AC09 ghi `31,5%`. Ca LTV 106,67% chỉ có mã `ltvAboveMax`, không có câu hiển thị trên màn hình. | Quy tắc định dạng số trong chỉ số và trong lý do là gì? Câu lý do hiển thị ở ca LTV 106,67% là gì? | Thấp | Dễ so sai chuỗi hiển thị khi viết kết quả mong đợi. | TC-20 | RECO-M04; RECO-M05; RECO-M06; RECO-S02-AC05; RECO-S03-AC09 — “`81,00% (LTV tối đa 80,00%)`; lý do `Từ chối: LTV 81% vượt mức tối đa 80%.`” · “DSR `31,5%`” |

## 6. Câu hỏi dựa trên kinh nghiệm — để riêng, hỏi sau khi cần

Những câu này **không** xuất phát từ chỗ SRS mơ hồ hay mâu thuẫn. Chúng đến từ kinh nghiệm kiểm thử về cách một chức năng thường cần được kiểm. Không đưa vào hàng đợi hỏi BA cho đến khi cần viết TC cho phần liên quan.

| ID | Vấn đề | Câu hỏi | Ưu tiên | Căn cứ kinh nghiệm | TC liên quan | Dấu vết trong SRS |
|---|---|---|---|---|---|---|
| KN-01 | **[Quy tắc xử lý]** Tài liệu chỉ có ví dụ ba lý do cùng là Từ chối. Chưa có ví dụ khi vừa có Chuyển cấp trên (DSR 50–70%) vừa có Từ chối (LTV, thặng dư, tuổi). | Khi vừa có điều kiện Chuyển cấp trên vừa có điều kiện Từ chối thì nhãn cuối là gì? Mục Lý do có liệt kê cả dòng Chuyển cấp trên không? Các dòng xếp theo thứ tự nào? | Cao | Khi thiết kế bảng quyết định cho luật nhiều điều kiện thì cần đủ tổ hợp; nguồn không có ví dụ cho tổ hợp này. | TC-13 | RECO-S01-AC10; RECO-R01; RECO-R02; RECO-R03; RECO-R04 — “mục `Lý do` liệt kê **ba dòng**” |
| KN-02 | **[Quy tắc xử lý, hiển thị]** "Đủ thông tin" chỉ được định nghĩa cho thu nhập bằng 0. Chưa nói khi thiếu số tiền vay, thời hạn hoặc giá trị khai báo thì hiển thị gì. | Thu nhập "0" gồm để trống, gõ 0, chỉ có thu nhập cho thuê? Thiếu hoặc bằng 0 ở từng ô còn lại thì hiện gì (M01 hay thông báo khác)? | Cao | Kinh nghiệm: ca thiếu từng trường bắt buộc thường cần kiểm riêng; nguồn chỉ có một ca (thiếu thu nhập). | TC-01, TC-02 | RECO-R10; RECO-M01; RECO-S01-AC01 — “Thu nhập `0`: DSR `—` và không có nhãn khuyến nghị.” · “Để có khuyến nghị cần đủ: người vay, **số tiền vay và thời hạn** (bước `Khoản vay và tài sản`), **tài sản có giá trị khai báo**, và **thu nhập** (bước `Tài chính`).” |
| KN-03 | **[Quy tắc xử lý, dữ liệu]** Cách tính tuổi lúc đáo hạn chưa được ghi: mốc ngày (hôm nay, ngày tạo hồ sơ, ngày giải ngân), có tính tròn năm không, ngày sinh lấy từ đâu. Các giá trị 56, 70, 71 chỉ chắc đúng ở ngày đã quan sát. | Quy tắc tính tuổi là gì? Nên dùng khách hàng có ngày sinh nào làm dữ liệu test? | Cao | Kinh nghiệm: kết quả phụ thuộc ngày chạy thì test lặp lại ở ngày khác có thể cho kết quả khác. | TC-02, TC-42, TC-48, TC-49 | RECO-R04; RECO-S04-AC01; RECO-S04-AC02; RECO-S04-AC03 — “Hồ sơ nền (kết quả tìm khách ghi ngày sinh `15/5/90`)” · “Tuổi cao nhất của các người vay khi hết thời hạn phải **≤ 70**; 71 trở lên → `Từ chối`” |
| KN-04 | **[Quy tắc xử lý]** Không có công thức "khoản trả mới" cho từng phương thức và ân hạn, và không nói dùng khoản của kỳ nào. Không nói cách làm tròn tiền (khoản trả mới, 70% thu nhập cho thuê). | Công thức và cách làm tròn chính thức? | Trung bình | Kinh nghiệm: có công thức mới dựng được kết quả mong đợi cho dữ liệu chưa đo. | TC-31, TC-40, TC-41, TC-43, TC-44, TC-45, TC-47 | RECO-R08; RECO-R06 — “Phụ thuộc số tiền vay, thời hạn, phương thức trả nợ, ân hạn, lãi suất thẩm định.” |
| KN-05 | ✅ **Đã có trả lời (TL-02, xem mục 5.1).** **[Quy tắc xử lý]** Nếu LTV và DSR so theo số làm tròn thì chưa biết cách làm tròn (cắt bỏ hay làm tròn nửa). | Cách làm tròn là gì (ví dụ LTV 80,005% hiện 80,00% hay 80,01%)? Hỏi sau khi CH-02 có câu trả lời. | Trung bình | Kinh nghiệm: ca biên của số làm tròn cần biết quy tắc làm tròn cụ thể. | — | RECO-R01; RECO-R02 — “Nhận biết "vượt" theo số hiển thị 2 chữ số thập phân” |
| KN-06 | **[Dữ liệu đầu vào]** Tài liệu chỉ nêu hai mục đích vay. | Còn mục đích vay nào khác, và LTV tối đa của từng mục đích? | Trung bình | Kinh nghiệm: danh sách giá trị của một ô chọn cần được kiểm hết. | TC-27, TC-28 | RECO-R01; RECO-S02-AC07 — “**Mua nhà: 80%**; **Xây/sửa nhà: 70%** (`maxLtv` 80 hoặc 70)” |
| KN-07 | **[Trạng thái]** Ô Sản phẩm tự quay về sản phẩm 12 tháng khi đổi mục đích; quy tắc không được giải thích. | Quy tắc tự đặt lại sản phẩm là gì? Sản phẩm nào hợp với mục đích nào? | Trung bình | Kinh nghiệm: ô tự đổi theo ô khác có thể làm DSR đổi ngoài ý người dùng. | TC-27, TC-28 | RECO-S02-AC07 — “Ô `Sản phẩm` tự quay về sản phẩm 12 tháng khi đổi mục đích” |
| KN-08 | **[Dữ liệu đầu vào]** Số người phụ thuộc chỉ được thử ở 2, 5, 20. Ca 5 và 20 không ghi ô chi phí nhập hay để trống. | Số người phụ thuộc hợp lệ là bao nhiêu? Ca 5 và 20 được thử với chi phí nhập hay để trống? | Thấp | Kinh nghiệm: ô số nguyên cần biết khoảng hợp lệ. | TC-37, TC-38, TC-39 | RECO-R07; RECO-S03-AC06 — “`4.500.000 + 2.000.000 × số người phụ thuộc` (8,5 / 14,5 / 44,5 triệu), kể cả khi nhập chi phí thấp hơn” |
| KN-09 | **[Dữ liệu đầu vào]** Chưa có giá trị tối đa của ô tiền (đã thử lương 99.999.999.999.999 chưa lưu). | Ô tiền có giới hạn độ dài hoặc giá trị tối đa không? Lưu giá trị rất lớn có lỗi không? | Thấp | Kinh nghiệm: ô số cần biết giá trị biên trên. | — | RECO-S03-AC11; RECO-R11 — “Nhập lương `99999999999999` (chưa lưu)” |
| KN-10 | **[Dữ liệu đầu vào]** Mới thử bằng công cụ điền. Chưa thử dán, ký tự thập phân (`,` `.`), khoảng trắng, số 0 đầu. Chưa rõ quy tắc áp dụng cho ô nào ngoài lương. | Quy tắc nhập chính thức cho từng ô tiền và số? | Trung bình | Kinh nghiệm: cách nhập thật (gõ, dán) thường cho kết quả khác cách điền bằng công cụ. | TC-55, TC-56 | RECO-R11; RECO-S05-AC04 — “đã thấy (điền bằng công cụ, chưa gõ từng phím)” |
| KN-11 | **[Dữ liệu đầu vào]** Không có khoảng hợp lệ của `Thời hạn (năm)` và `Thời gian ân hạn (tháng)`. Thời hạn 40 năm vẫn lưu được. | Giá trị tối thiểu, tối đa của hai ô này, và ràng buộc giữa ân hạn với thời hạn? | Trung bình | Kinh nghiệm: ô số cần biết khoảng hợp lệ và ràng buộc giữa hai ô. | — | RECO-S03-AC07; RECO-S03-AC09 — “Bước Khoản vay: đổi `Thời hạn (năm)` từ `20` thành `40`, `Lưu`” · “Nhập `Thời gian ân hạn (tháng)` = `12`, `Lưu`” |
| KN-12 | **[Trạng thái]** Nhãn trạng thái bước (`Đã xong`, `Chưa mở`) chỉ thấy ở vài ca. Lưu khi để trống thì bước Tài chính ghi gì? Điều kiện mở bước Lãi suất là gì? | Quy tắc đổi trạng thái của từng bước? | Trung bình | Kinh nghiệm: trạng thái bước thường là kết quả kiểm tra riêng sau mỗi lần Lưu. | TC-51, TC-54 | RECO-S05-AC01; RECO-S05-AC03; RECO-S04-AC04 — “bước `Tài chính` ghi `Đã xong`” · “bước `Lãi suất` ghi `Chưa mở`” |
| KN-13 | **[Trạng thái]** Tài liệu chỉ nêu hồ sơ nháp. Hồ sơ đã gửi thẩm định bị khóa: chưa rõ khuyến nghị còn hiện hoặc được tính lại không. | Trạng thái hồ sơ nào có bản xem trước, trạng thái nào chỉ đọc? | Trung bình | Kinh nghiệm: một chức năng thường cần kiểm ở từng trạng thái của đối tượng. | — | RECO mục 2; RECO mục 6.2 — “`Gửi thẩm định` khóa hồ sơ và gọi CIC nên cần người dùng đồng ý trước.” · “Có một **hồ sơ nháp** của mình.” |
| KN-14 | **[Dữ liệu lưu]** Không nói khuyến nghị được lưu cùng hồ sơ hay tính lại mỗi lần mở. | Lưu kết quả đã tính hay tính lại khi mở hồ sơ? | Thấp | Kinh nghiệm: biết cách lưu giúp chọn đúng dữ liệu để kiểm sau khi thay đổi. | — | RECO-S05 (mục 1) — “ô **Khuyến nghị** trên đầu trang hồ sơ (sau khi lưu)” |
| KN-15 | **[Thông báo]** Chưa nói ngôn ngữ đã chọn có được nhớ giữa các lần mở không. | Ngôn ngữ đã chọn có được lưu lại không? | Thấp | Kinh nghiệm: lựa chọn ngôn ngữ thường cần kiểm khi mở lại. | — | RECO-S06-AC01 — “chưa thấy bản English” |
| KN-16 | **[Tích hợp]** Nhiều kết quả chỉ thấy qua API (`APPROVE`, `DECLINE`, `ageAtMaturity`, `ltvAboveMax`) mà không có mô tả giao diện API. | Các trường và mã này có thuộc phạm vi test không? Tên và giá trị chính thức? | Trung bình | Kinh nghiệm: nếu chỉ kiểm qua API thì cần biết tên trường chính thức. | TC-48, TC-49 | RECO-S04-AC02; RECO-S04-AC03; RECO-S02-AC05; RECO-S02-AC06; RECO-S03-AC07 — “đã thấy (qua API)” |

## 7. Luật viết test case chi tiết (bước sau)
- Mỗi test case tự đứng được: người khác cầm lên là chạy được, không cần mở requirement hay lật sang case khác. Viết đầy đủ từ bước đầu tiên, không ghi "như TC-xxx".
- Mỗi case một mục tiêu kiểm tra; chỉ thử một giá trị không hợp lệ hoặc một đường không được phép.
- Mỗi mã TC trong checklist tương ứng một test case riêng biệt; không gộp, kể cả khi chỉ khác dữ liệu.
- Mỗi test case có đủ điều kiện trước, các bước thực hiện, dữ liệu test và kết quả mong đợi; không tham chiếu sang test case khác.
- Giữ nguyên số lượng và mã TC trong checklist đã được xác nhận. Nếu phát hiện trùng lặp hoặc không đủ thông tin, ghi nhận riêng, không tự ý gộp, xóa hoặc bổ sung.
- Chỗ nào nguồn không đủ để viết cụ thể thì ghi "CẦN XÁC NHẬN", không tự điền, và đưa vào câu hỏi cho BA.

## 8. Tự kiểm
- Mã requirement trong SRS: 61 (AC, R, M). Thiếu ở cả checklist lẫn hai bảng câu hỏi: **không có**.
- Mã chỉ xuất hiện ở câu hỏi (chưa có TC): RECO-M09, RECO-M10, RECO-R12, RECO-S01-AC06, RECO-S01-AC07, RECO-S02-AC02, RECO-S03-AC11, RECO-S04-AC01, RECO-S04-AC04, RECO-S05-AC02.
- Trích dẫn: 109 nơi đặt trích nguyên văn, đã so từng chuỗi với file SRS bằng script (lỗi: 0).
- Số lượng TC: 62 (TC-01 đến TC-62, không trùng mã).

## 9. Lịch sử thay đổi
| Ngày | Thay đổi |
|---|---|
| 2026-11-17 | Tạo mới từ cuộc trao đổi phân tích requirement; thêm ưu tiên và lý do; tách câu hỏi kinh nghiệm; loại câu hỏi hiệu năng |
| 2026-11-17 | Nhận TL-01 (làm tròn 2 chữ số thập phân, gần nhất): CH-02, CH-03, KN-05 đã có trả lời; ghi chú ba TC có thể bổ sung |
| 2026-11-17 | Bạn chọn phương án C (TL-02, làm tròn lên) thay cho TL-01: kết quả mong đợi của ba TC có thể bổ sung đổi, hệ thống hiện tại khác; ghi chú TC có số % hiển thị có thể đổi |
| 2026-11-17 | Bạn chốt TL-02 áp dụng cả khi hiển thị: đổi tên và ghi chú 9 TC có số % hiển thị (TC-06, 08, 13, 23, 27, 28, 41, 59, 60); mã và số lượng TC giữ nguyên |
