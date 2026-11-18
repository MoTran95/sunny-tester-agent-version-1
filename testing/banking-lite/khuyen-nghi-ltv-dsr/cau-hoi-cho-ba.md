# Câu hỏi cho BA — Khuyến nghị thẩm định xem trước LTV/DSR (Banking Lite)

| | |
|---|---|
| Ngày soạn | 2026-11-17 |
| Dùng để | Gửi BA. Mỗi câu có tình huống thật, câu hỏi, cách mình đang hiểu và lý do hỏi |
| Nguồn | [SRS nháp](../../../srs/banking-lite/khuyen-nghi-ltv-dsr.md) (hệ thống 1.3.0) và [bảng soát](bang-soat-requirement.md). Mã cũ (CH-xx, KN-xx) ghi ở cuối mỗi câu để tra chéo |
| Cách dùng | Gửi **Phần A** trước. **Phần B** gom hỏi một lần sau. **Phần C** là việc mình tự kiểm tra trên hệ thống, chưa cần hỏi BA |
| Tình trạng | Chưa gửi BA. Chưa có câu trả lời nào |

## Đọc trước 1 phút

Tính năng này giúp chuyên viên khách hàng biết sớm hồ sơ vay có khả năng được duyệt không. Khi nhập số liệu cho hồ sơ vay mua hoặc xây sửa nhà, hệ thống tính ngay một **khuyến nghị**: **Phê duyệt**, **Chuyển cấp trên** hoặc **Từ chối**, kèm các chỉ số và lý do. Đây là bản **xem trước**. Thẩm định chính thức chạy khi gửi hồ sơ, lúc đó mới có dữ liệu CIC.

| Từ hay dùng | Nghĩa |
|---|---|
| LTV | Số tiền vay chia giá trị tài sản, tính bằng % |
| DSR | Tiền trả nợ mỗi tháng chia thu nhập mỗi tháng, tính bằng % |
| Thặng dư | Tiền còn lại mỗi tháng sau khi trừ chi phí và các khoản trả nợ |
| Khoản trả mới | Số tiền phải trả mỗi tháng cho khoản vay đang xét |
| Khung Thẩm định | Khung ở bước Tài chính, hiện khuyến nghị, chỉ số và lý do. Đổi ngay khi nhập số |
| Đầu trang hồ sơ | Ô Khuyến nghị ở đầu trang hồ sơ. Chỉ đổi sau khi bấm Lưu |
| Hồ sơ nền | Hồ sơ mẫu mình dùng trong các ví dụ: mua nhà, vay 3.200.000.000, 20 năm, tài sản khai báo 4.000.000.000, trả Gốc đều. Khoản trả mới khi đó là 40.800.000 một tháng |

**Các mức tối đa hệ thống đang dùng** (mình quan sát được, chưa có tài liệu chính thức):

- DSR trên 50% đến 70% thì Chuyển cấp trên. DSR trên 70% thì Từ chối.
- Thặng dư tối thiểu 3.000.000. Thấp hơn thì Từ chối.
- LTV tối đa 80% (mua nhà) hoặc 70% (xây/sửa nhà). Vượt thì Từ chối.
- Tuổi cao nhất của người vay lúc hết hạn vay tối đa 70. Từ 71 trở lên thì Từ chối.

**Quy ước từ ngữ trong file này:** "mức tối đa" cho các giới hạn, "hết hạn vay" cho lúc kết thúc khoản vay. Chữ nào đang hiện trên màn hình thì mình để trong dấu ngoặc kép. Nếu team dùng từ khác, báo mình đổi.

---

# Phần A. Hỏi ngay (5 câu)

Các câu này làm đổi kết quả khuyến nghị, nên cần trả lời sớm.

## A1. Hệ thống làm tròn tỷ lệ LTV, DSR như thế nào?

**Người trả lời gợi ý:** BA (Dev xác nhận cách đang cài)

Mình thử vay 3.200.100.000 trên tài sản khai báo 4.000.000.000. Số thật là 80,0025%. Màn hình ghi 80,00% và vẫn Phê duyệt, trong khi mức tối đa là 80%. Nếu làm tròn lên thì ra 80,01%, tức là vượt, phải Từ chối. Mình thử thêm vài ca sát mức tối đa:

| Ca | Số thật | Màn hình đang ghi | Nếu làm tròn lên |
|---|---|---|---|
| Vay 3.200.100.000, tài sản 4.000.000.000 (LTV, mức tối đa 80%) | 80,0025% | 80,00%, Phê duyệt | 80,01%, Từ chối |
| Lương 81.599.000, khoản trả mới 40.800.000 (DSR, mức 50%) | 50,0006% | 50,00%, Phê duyệt | 50,01%, Chuyển cấp trên |
| Lương 58.285.714, khoản trả mới 40.800.000 (DSR, mức 70%) | 70,0000003% | 70,00%, Chuyển cấp trên | 70,01%, Từ chối |
| Lương 81.000.000, khoản trả mới 40.800.000 (chỉ khác số hiển thị) | 50,3703…% | 50,37% | 50,38% |

**Hỏi:** Anh/chị cho mình hỏi: hệ thống nên làm tròn kiểu nào, và có làm tròn cả số hiển thị không?

**Mình đang hiểu:** Mình tạm chọn làm tròn lên, lấy 2 số sau dấu phẩy, cho cả số hiển thị và khi so với mức tối đa (chưa phải BA chốt). Hệ thống hiện đang làm tròn gần nhất. Nếu mình hiểu đúng thì 11 chỗ trong tài liệu đang cho kết quả khác. Thặng dư vẫn so theo số đồng nguyên.

**Vì sao hỏi:** Hai cách cho kết quả khác nhau ở các hồ sơ sát mức tối đa. Nếu không hỏi, mình có thể báo lỗi sai hoặc bỏ sót lỗi thật.

**Anh/chị chọn:**

- [ ] 1. Làm tròn lên 2 số sau dấu phẩy, cho cả số hiển thị và khi so với mức tối đa (cách mình đang hiểu)
- [ ] 2. Làm tròn gần nhất 2 số sau dấu phẩy (như hệ thống hiện tại). Khi phần lẻ đúng ở giữa, ví dụ 80,005%, thì làm tròn lên hay xuống?
- [ ] 3. So với mức tối đa bằng số thật, chỉ làm tròn khi hiển thị
- [ ] 4. Khác: ______

**Câu trả lời của BA:** ______

*Mã cũ: CH-02, CH-03, KN-05 (đã có quyết định tạm của mình, cần BA xác nhận).*

## A2. Người vay quá 70 tuổi thì màn hình phải hiện gì?

**Người trả lời gợi ý:** BA (Dev nếu là lỗi hiển thị)

Mình thử người vay sinh 15/5/1990, vay 3,2 tỷ trong 40 năm, tức hết hạn lúc 76 tuổi, quá mức tối đa 70. Dữ liệu hệ thống trả về là Từ chối, lý do "Có người vay 76 tuổi khi đáo hạn; tối đa 70." Nhưng màn hình không hiện Từ chối. Dòng "Tuổi cao nhất khi đáo hạn" ghi 76, còn khung Thẩm định để trống, lại hiện câu "Nhập đủ thông tin người vay, khoản vay, tài sản và thu nhập để xem khuyến nghị." dù mình đã nhập đủ. Ô Khuyến nghị ở đầu trang ghi "—". Mình chưa thử trên màn hình với vay 35 năm (71 tuổi).

**Hỏi:** Anh/chị cho mình hỏi: trường hợp này màn hình phải hiện gì ạ? Và các chỉ số khác như DSR, khoản trả mới có còn hiện không?

**Mình đang hiểu:** Phải hiện Từ chối kèm lý do quá tuổi, giống các luật khác (LTV, DSR, thặng dư), và hiện tại là lỗi hiển thị. Mình chưa chắc vì tài liệu không nói.

**Vì sao hỏi:** Nếu là lỗi thì mình báo lỗi. Nếu chủ ý thì phải ghi vào tài liệu để test đúng theo. Hiện người dùng thấy câu "Nhập đủ thông tin…" dù đã nhập đủ, dễ hiểu nhầm.

**Anh/chị chọn:**

- [ ] a. Phải hiện Từ chối kèm lý do quá tuổi (hiện tại là lỗi)
- [ ] b. Giữ như hiện tại (chủ ý). Nếu vậy, vì sao?
- [ ] c. Khác: ______

**Câu trả lời của BA:** ______

*Mã cũ: CH-04.*

## A3. Hồ sơ vừa "Chuyển cấp trên" vừa dính luật "Từ chối" thì ra kết quả gì?

**Người trả lời gợi ý:** BA

Mình lấy hồ sơ nền, lương 75.000.000, chi phí sinh hoạt 31.500.000 (số này mình tính theo công thức, chưa thử trên hệ thống). DSR là 40.800.000 ÷ 75.000.000 = 54,40%, nằm giữa 50% và 70% nên là Chuyển cấp trên. Thặng dư là 75.000.000 − 31.500.000 − 40.800.000 = 2.700.000, thấp hơn mức tối thiểu 3.000.000 nên là Từ chối. Mình mới thấy một ví dụ gần giống: hồ sơ vi phạm cả ba luật (LTV, DSR trên 70%, thặng dư) đều ra Từ chối, và mục Lý do ghi đủ ba dòng, mỗi luật một dòng, theo thứ tự LTV, DSR, thặng dư.

**Hỏi:** Anh/chị cho mình hỏi: với hồ sơ như trên, nhãn cuối là gì? Mục Lý do có ghi cả hai dòng không, và theo thứ tự nào?

**Mình đang hiểu:** Nhãn cuối là Từ chối (mức nặng nhất), mục Lý do ghi cả hai dòng, thứ tự giống ví dụ ba lý do. Đây là mình đoán từ ví dụ, chưa có tài liệu.

**Vì sao hỏi:** Tổ hợp này chưa có ví dụ nào mà hồ sơ thật rất dễ gặp. Mình cần biết kết quả đúng để viết test.

**Anh/chị chọn:**

- [ ] Đúng như mình đang hiểu
- [ ] Khác: nhãn cuối là ______; mục Lý do ghi ______

**Câu trả lời của BA:** ______

*Mã cũ: KN-01.*

## A4. Tuổi lúc hết hạn vay được tính thế nào?

**Người trả lời gợi ý:** BA

Người vay trong ví dụ có ngày sinh đang hiện là "15/5/90" (mình hiểu là 15/5/1990). Hôm mình thử là 17/11/2026. Dòng "Tuổi cao nhất khi đáo hạn" ghi như sau:

| Vay trong | Màn hình ghi | Kết quả |
|---|---|---|
| 20 năm | 56 | Hồ sơ nền |
| 34 năm | 70 | Đạt |
| 35 năm | 71 | Từ chối |

**Hỏi:** Anh/chị cho mình hỏi: tuổi tính từ ngày nào (hôm nay, ngày tạo hồ sơ hay ngày giải ngân), và tính tròn năm hay lấy năm hết hạn trừ năm sinh? Ngày sinh lấy từ đâu, hồ sơ khách hàng hay VNeID?

**Mình đang hiểu:** Tuổi tròn năm tại ngày hết hạn, tính từ ngày thao tác (hôm nay) cộng số năm vay. Ba số trên khớp cách hiểu này. Nhưng chúng cũng khớp cách "năm hết hạn trừ năm sinh", vì sinh nhật 15/5 đã qua trong năm 2026, nên mình chưa phân biệt được.

**Vì sao hỏi:** Kết quả ở ranh giới 70 và 71 đổi theo ngày mình chạy test. Mình cần biết cách tính để chọn dữ liệu cho kết quả ổn định. Nếu quy tắc là tính từ ngày giải ngân thì hệ thống có thể đang sai.

**Anh/chị chọn:**

- Tính từ ngày: [ ] hôm nay [ ] ngày tạo hồ sơ [ ] ngày giải ngân dự kiến [ ] khác: ______
- Cách tính tuổi: [ ] tuổi tròn năm tại ngày hết hạn [ ] năm hết hạn trừ năm sinh [ ] khác: ______
- Ngày sinh lấy từ: ______

**Câu trả lời của BA:** ______

*Mã cũ: KN-03.*

## A5. Có tài liệu yêu cầu chính thức của tính năng này không?

**Người trả lời gợi ý:** BA

Tài liệu mình đang có là do mình ghi lại từ hệ thống phiên bản 1.3.0. Nó còn là bản nháp, chưa team nào xác nhận. Mình không có tài liệu yêu cầu hay chính sách tín dụng nào để đối chiếu.

**Hỏi:** Anh/chị cho mình hỏi: có tài liệu yêu cầu, ticket hay chính sách tín dụng cho tính năng này không? Nếu có, anh/chị gửi giúp mình. Nếu không, anh/chị xác nhận giúp các mức tối đa, ba nhãn khuyến nghị và các câu thông báo ở đầu file là đúng yêu cầu.

**Mình đang hiểu:** Mình đang coi hành vi hệ thống hiện tại là đúng, trừ chỗ tự mâu thuẫn hoặc BA nói khác.

**Vì sao hỏi:** Nếu một hành vi hiện tại thật ra sai mà không ai biết, mình sẽ coi lỗi là "đạt".

**Câu trả lời của BA:** ______

*Mã cũ: CH-01.*

---

# Phần B. Hỏi sau, gom một lần (12 câu)

Các câu này chủ yếu về hiển thị, câu chữ, hoặc phần mình chưa test được. Gom lại hỏi trong một buổi.

## B1. Các mức tối đa trong hệ thống là cố định hay chỉnh được?

**Người trả lời gợi ý:** BA và Dev

Hệ thống đang dùng các mức sau: DSR 50% và 70%, thặng dư tối thiểu 3.000.000, tuổi tối đa 70, LTV tối đa 80% (mua nhà) và 70% (xây/sửa nhà). Mình xem danh sách thiết lập của hệ thống thì thấy trống, không có mức nào trong đó.

**Hỏi:** Anh/chị cho mình hỏi: các mức này cố định hay chỉnh được? Nếu chỉnh được thì ai chỉnh?

**Mình đang hiểu:** Cố định trong hệ thống, không chỉnh được trên giao diện.

**Vì sao hỏi:** Nếu chỉnh được thì mình phải biết cách đặt giá trị trước khi test. Hiện mình dùng thẳng các con số trên.

**Câu trả lời của BA:** ______

*Mã cũ: CH-16.*

## B2. Ô Khuyến nghị đầu trang chỉ đổi sau khi bấm Lưu, có đúng ý không?

**Người trả lời gợi ý:** BA

Đầu trang đang là Phê duyệt (đã lưu). Mình đổi lương xuống 75.000.000 nhưng chưa bấm Lưu. Khung Thẩm định đổi ngay sang Chuyển cấp trên, còn đầu trang vẫn Phê duyệt. Bấm Lưu xong, chờ vài giây thì đầu trang mới đổi.

**Hỏi:** Anh/chị cho mình hỏi: đầu trang chỉ đổi sau khi lưu là chủ ý đúng không, và có cần ghi chú cho người dùng không?

**Mình đang hiểu:** Chủ ý, vì đầu trang là kết quả của bản đã lưu.

**Vì sao hỏi:** Nếu đây là lỗi thì người dùng nhìn đầu trang sẽ tưởng hồ sơ vẫn được phê duyệt.

**Câu trả lời của BA:** ______

*Mã cũ: CH-14.*

## B3. Hồ sơ có nhiều người vay thì tính thế nào?

**Người trả lời gợi ý:** BA

Quy tắc tuổi lấy tuổi cao nhất trong các người vay, và câu thông báo ghi "Có người vay … tuổi khi đáo hạn". Nhưng mình mới thử hồ sơ một người vay.

**Hỏi:** Anh/chị cho mình hỏi: hồ sơ nhiều người vay có nằm trong phần mình cần test không? Nếu có thì thu nhập, nợ hiện có và tuổi lấy theo người nào, hay cộng lại?

**Mình đang hiểu:** Tuổi lấy người lớn tuổi nhất. Còn thu nhập và nợ thì mình chưa có cách hiểu nào vì tài liệu không nói.

**Vì sao hỏi:** Không biết cách tính thì mình không viết được test cho nhiều người vay.

**Câu trả lời của BA:** ______

*Mã cũ: CH-05.*

## B4. Tài sản đã định giá thì LTV tính theo giá nào?

**Người trả lời gợi ý:** BA

Khi tài sản chưa định giá, LTV bằng số tiền vay chia giá trị khai báo. Ví dụ vay 3,2 tỷ trên tài sản khai báo 5 tỷ thì LTV là 64%. Hệ thống có sẵn câu "Giá định giá thấp hơn giá khai báo {shortfall}% (quá {max}%)." nhưng mình chưa thấy câu này trên màn hình, cũng không biết mức {max} là bao nhiêu. Mình chưa thử được vì phần định giá cần chuyên viên định giá làm.

**Hỏi:** Anh/chị cho mình hỏi: khi đã có giá định giá thì LTV tính theo giá định giá hay giá khai báo? Giá định giá thấp hơn giá khai báo bao nhiêu phần trăm thì bị tính là quá mức, và khi đó kết quả là nhãn nào?

**Mình đang hiểu:** LTV dùng giá định giá, và có thêm một lý do nếu giá định giá thấp hơn giá khai báo quá mức cho phép. Đây là mình đoán, chưa thử.

**Vì sao hỏi:** Chưa có cách nào test hồ sơ đã định giá nếu không biết quy tắc này.

**Câu trả lời của BA:** ______

*Mã cũ: CH-06.*

## B5. Câu thông báo về nhóm nợ CIC xuất hiện khi nào?

**Người trả lời gợi ý:** BA

Hệ thống có sẵn câu "CIC báo người vay {borrower} thuộc nhóm nợ {group}." nhưng mình chưa thấy câu này trên màn hình. Bản xem trước có dòng ghi "thẩm định chính thức chạy khi gửi, có dữ liệu CIC".

**Hỏi:** Anh/chị cho mình hỏi: nhóm nợ nào thì hồ sơ bị Từ chối, nhóm nào thì Chuyển cấp trên? Câu này có hiện ở bản xem trước không?

**Mình đang hiểu:** Câu này chỉ hiện khi thẩm định chính thức, bản xem trước thì không có.

**Vì sao hỏi:** Mình không viết được test cho câu này nếu không biết nhóm nợ nào làm nó xuất hiện.

**Câu trả lời của BA:** ______

*Mã cũ: CH-07.*

## B6. Bản xem trước và bản thẩm định chính thức có khớp nhau không?

**Người trả lời gợi ý:** BA

Trong mã nguồn giao diện mình thấy hai câu của bước quyết định: "Không thể phê duyệt hồ sơ được khuyến nghị từ chối." và "Ghi rõ lý do phê duyệt hồ sơ được khuyến nghị chuyển cấp trên." Mình chưa thấy chúng trên màn hình.

**Hỏi:** Anh/chị cho mình hỏi: với cùng số liệu thì bản xem trước và bản chính thức có cho cùng kết quả không? Khuyến nghị Từ chối có chặn việc phê duyệt không? Chuyển cấp trên có bắt người duyệt ghi lý do không?

**Mình đang hiểu:** Bản chính thức dùng cùng quy tắc, chỉ thêm kiểm tra định giá và CIC. Hai câu trên cho thấy Từ chối thì chặn phê duyệt, còn Chuyển cấp trên thì phải ghi lý do.

**Vì sao hỏi:** Phần này chưa thuộc phần mình đang test, nhưng nó quyết định có dùng khuyến nghị xem trước làm chuẩn cho các bước sau được không.

**Câu trả lời của BA:** ______

*Mã cũ: CH-08.*

## B7. Các câu thông báo tiếng Anh có đúng không?

**Người trả lời gợi ý:** BA

Các câu tiếng Anh dưới đây mình chỉ thấy trong mã nguồn giao diện, chưa thấy trên màn hình:

| Thông báo | Tiếng Việt | Tiếng Anh (trong mã nguồn) |
|---|---|---|
| Chưa đủ thông tin | Nhập đủ thông tin người vay, khoản vay, tài sản và thu nhập để xem khuyến nghị. | Enter the borrower, loan, property and income details to see a recommendation. |
| Đạt mọi quy tắc | Đáp ứng mọi quy tắc tín dụng. | All credit rules are met. |
| LTV vượt | LTV {ltv}% vượt mức tối đa {max}%. | LTV {ltv}% is above the maximum {max}%. |
| DSR vượt | DSR {dsr}% vượt mức tối đa {max}%. | DSR {dsr}% is above the maximum {max}%. |
| Thặng dư thấp | Thặng dư hằng tháng {surplus} VND thấp hơn {min} VND. | Monthly surplus {surplus} VND is below {min} VND. |
| Quá tuổi | Có người vay {age} tuổi khi đáo hạn; tối đa {max}. | A borrower would be {age} at maturity; the maximum is {max}. |
| Định giá thấp | Giá định giá thấp hơn giá khai báo {shortfall}% (quá {max}%). | Valuation is {shortfall}% below the declared value (more than {max}%). |
| Nhóm nợ CIC | CIC báo người vay {borrower} thuộc nhóm nợ {group}. | CIC reports debt group {group} for borrower {borrower}. |

Câu "Đã lưu." khi lưu thành công thì mình chưa thấy bản tiếng Anh.

**Hỏi:** Anh/chị xem giúp mình các câu tiếng Anh này có đúng không, câu nào cần sửa?

**Mình đang hiểu:** Các câu trong mã nguồn là bản chính thức. Mình chưa kiểm được trên màn hình.

**Vì sao hỏi:** Mình chỉ viết được test tiếng Anh cho những câu đã thấy trên màn hình.

**Câu trả lời của BA:** ______

*Mã cũ: CH-17.*

## B8. Số phần trăm hiển thị theo quy tắc nào?

**Người trả lời gợi ý:** BA

Khung Thẩm định ghi "81,00% (LTV tối đa 80,00%)", tức 2 số sau dấu phẩy. Nhưng câu lý do lại ghi "LTV 81% vượt mức tối đa 80%.", bỏ số 0 ở cuối. Trong tài liệu còn một chỗ ghi DSR "31,5%". Với LTV 106,67% thì mình chỉ thấy mã lý do ltvAboveMax, chưa thấy câu hiển thị.

**Hỏi:** Anh/chị cho mình hỏi: số phần trăm trong chỉ số và trong câu lý do viết theo quy tắc nào? Với LTV 106,67%, câu lý do trên màn hình là gì?

**Mình đang hiểu:** Chỉ số luôn ghi 2 số sau dấu phẩy. Trong câu lý do thì bỏ số 0 thừa ở cuối. Với LTV 106,67%, mình đoán câu là "LTV 106,67% vượt mức tối đa 80%." theo mẫu câu.

**Vì sao hỏi:** Để mình viết đúng từng chữ khi so sánh kết quả.

**Câu trả lời của BA:** ______

*Mã cũ: CH-18.*

## B9. Khoản trả mới mỗi tháng tính bằng công thức nào?

**Người trả lời gợi ý:** BA

Mình thấy hệ thống ghi các khoản trả mới như bảng dưới, với khoản vay 3,2 tỷ:

| Tình huống | Khoản trả mới hệ thống ghi |
|---|---|
| Gốc đều, 20 năm, lãi suất thẩm định 10,30% | 40.800.000 |
| Gốc đều, 40 năm, lãi suất 10,30% | 34.133.333 |
| Gốc đều, 20 năm, lãi suất 10,05% | 40.133.333 |
| Niên kim (trả đều), 20 năm, lãi suất 10,05% | 30.986.775 |
| Niên kim, ân hạn 12 tháng, lãi suất 10,05% | 31.504.846 |
| Niên kim, ân hạn 12 tháng, lãi suất 9,55% (sản phẩm 36 tháng) | 30.465.933 |

**Hỏi:** Anh/chị cho mình hỏi: công thức tính khoản trả mới cho Gốc đều, Niên kim và khi có ân hạn là gì? Tiền lẻ làm tròn thế nào?

**Mình đang hiểu:**

- **Gốc đều:** lấy tiền vay chia số tháng, cộng tiền vay nhân lãi suất chia 12, tức là khoản của tháng đầu tiên. Ví dụ 3.200.000.000 ÷ 240 + 3.200.000.000 × 10,30% ÷ 12 = 40.800.000.
- **Niên kim:** trả đều mỗi tháng theo công thức trả góp đều. Có ân hạn 12 tháng thì trả đều trong 228 tháng còn lại.
- **Làm tròn** đến đồng gần nhất.

Mình đã tính lại: cả 6 số trên khớp cách hiểu này, sai lệch dưới 1 đồng.

**Vì sao hỏi:** Có công thức thì mình mới tính được kết quả đúng cho các số liệu khác.

**Anh/chị chọn:**

- [ ] Đúng như mình đang hiểu
- [ ] Khác: ______

**Câu trả lời của BA:** ______

*Mã cũ: KN-04.*

## B10. Hồ sơ đã gửi thẩm định thì còn hiện khuyến nghị không?

**Người trả lời gợi ý:** BA

Mình mới thử hồ sơ nháp. Bấm Gửi thẩm định thì hồ sơ bị khóa và hệ thống gọi CIC, nên mình chưa thử.

**Hỏi:** Anh/chị cho mình hỏi: hồ sơ ở trạng thái nào thì còn hiện bản xem trước khuyến nghị? Sau khi gửi thẩm định, hồ sơ bị khóa thì khuyến nghị có còn hiện và có còn tính lại không?

**Mình đang hiểu:** Sau khi gửi thì hồ sơ chỉ xem được, khuyến nghị xem trước không đổi nữa. Mình đoán.

**Vì sao hỏi:** Mình đang thiếu test cho các trạng thái hồ sơ khác ngoài hồ sơ nháp.

**Câu trả lời của BA:** ______

*Mã cũ: KN-13.*

## B11. Mở lại hồ sơ đã lưu thì khuyến nghị là kết quả cũ hay tính lại?

**Người trả lời gợi ý:** BA hoặc Dev

Mình chưa biết khi mở lại một hồ sơ đã lưu thì khuyến nghị là kết quả đã lưu từ lần trước hay được tính lại từ số liệu hiện tại.

**Hỏi:** Anh/chị cho mình hỏi: khuyến nghị được lưu cùng hồ sơ hay tính lại mỗi lần mở?

**Mình đang hiểu:** Tính lại mỗi lần mở. Mình chưa chắc.

**Vì sao hỏi:** Biết cách này mình mới chọn đúng dữ liệu để kiểm sau khi đổi số liệu hoặc đổi mức tối đa.

**Câu trả lời của BA:** ______

*Mã cũ: KN-14.*

## B12. Dữ liệu API của khuyến nghị có cần test không?

**Người trả lời gợi ý:** Dev

Một số kết quả, như trường hợp quá tuổi, mình chỉ thấy được qua dữ liệu API của hồ sơ. Dữ liệu đó có phần khuyến nghị với các giá trị như APPROVE, DECLINE, mã lý do ageAtMaturity và ltvAboveMax, cùng các chỉ số như tuổi tối đa khi hết hạn vay.

**Hỏi:** Anh/chị cho mình hỏi: những trường và giá trị này có nằm trong phần mình cần test không, và tên chính thức là gì?

**Mình đang hiểu:** Đây là dữ liệu bên trong để màn hình hiển thị. Mình chỉ dùng để kiểm tra thêm, không coi là giao diện chính thức.

**Vì sao hỏi:** Nếu tên hoặc giá trị đổi mà màn hình không đổi thì test chỉ dựa vào màn hình sẽ không phát hiện.

**Câu trả lời:** ______

*Mã cũ: KN-16.*

---

# Phần C. Mình tự kiểm tra trên hệ thống trước (14 mục)

Theo sách: câu nào xem hệ thống đang chạy là tìm được câu trả lời thì mình tự làm trước, chỉ hỏi BA khi không tìm ra. Lưu ý: xem hệ thống chỉ cho biết hệ thống **đang làm gì**, không chứng minh là **đúng**. Mình chỉ dùng hồ sơ nháp của mình, không đổi dữ liệu của người khác.

## C1. Lãi suất thẩm định tính theo quy tắc nào?

- **Cần xem:** Mình thử thêm các mức LTV khác (ví dụ 45% và 70%) và sản phẩm khác (sản phẩm 24 tháng 7,00% mình chưa thử), rồi ghi lãi suất thẩm định. Mình cũng xem con số này hiện trên màn hình hay chỉ có trong dữ liệu API.
- **Mình đang hiểu:** Lãi suất thẩm định tăng khi LTV cao hơn (từ 9,80% đến 10,30% với sản phẩm 12 tháng), và thấp hơn với sản phẩm 36 tháng (9,55% ở LTV 64%). Mình chưa biết ranh giới giữa các mức.
- **Nếu không tìm ra, hỏi BA:** Lãi suất thẩm định được tính theo quy tắc nào: theo LTV, theo sản phẩm hay theo mục đích vay?

*Mã cũ: CH-09.*

## C2. Chi phí sinh hoạt tối thiểu tính thế nào khi có người phụ thuộc?

- **Cần xem:** Mình thử 1, 3 và 4 người phụ thuộc, với chi phí nhập thấp và để trống, rồi ghi dòng "Chi phí được tính".
- **Mình đang hiểu:** Chi phí được tính là số lớn hơn giữa chi phí mình nhập và (4.500.000 + 2.000.000 × số người phụ thuộc). Công thức này khớp với 2, 5 và 20 người phụ thuộc mình đã thử.
- **Nếu không tìm ra, hỏi BA:** Công thức chi phí tối thiểu chính thức là gì? Hệ thống tự nâng chi phí nhập thấp lên mức tối thiểu mà không báo người dùng, vậy có đúng ý không?

*Mã cũ: CH-10.*

## C3. Ba ca khoản trả mới, ân hạn, sản phẩm thiếu điều kiện

- **Cần làm:** Mình chạy lại ba ca này và ghi rõ lương, chi phí, nợ hiện có, số người phụ thuộc, vì tài liệu không ghi. Việc này của mình, không cần hỏi BA.
- **Mình đang hiểu:** Các kết quả DSR 30,99%, 31,5% và 30,47% khớp với lương 100.000.000 và không có nợ.

*Mã cũ: CH-11.*

## C4. Ca số rất lớn (lương 99.999.999.999.999)

- **Cần làm:** Mình chạy lại ở hồ sơ nền, không đổi ô nào khác, rồi ghi thặng dư. Tài liệu ghi 99.999.915.366.666 nhưng theo công thức phải ra 99.999.954.699.999 (lệch 39.333.333). Việc này của mình, không cần hỏi BA.

*Mã cũ: CH-12.*

## C5. Gõ phím thật và dán vào ô tiền

- **Cần xem:** Mình gõ từng phím và dán vào từng ô tiền và ô số, thử chữ, dấu trừ, dấu phẩy, dấu chấm, khoảng trắng, số 0 đầu. Trước đây mình chỉ điền bằng công cụ.
- **Mình đang hiểu:** Ô chỉ nhận chữ số. Dấu trừ bị bỏ (nhập -5000000 thành 5.000.000). Dưới ô hiện số có dấu chấm ngăn nghìn.
- **Nếu không tìm ra, hỏi BA:** Ô tiền chỉ nhận chữ số có đúng quy tắc không? Bỏ dấu trừ để thành 5.000.000 có chủ ý không?

*Mã cũ: CH-13, KN-10.*

## C6. Hai tài khoản khác xem khung Thẩm định thế nào?

- **Cần làm:** Mình đăng nhập P200001 (chuyên viên định giá) và P300001 (chuyên viên thẩm định tín dụng), mở một hồ sơ rồi xem khung Thẩm định và ô Khuyến nghị. **Cần bạn gõ mật khẩu.**
- **Mình đang hiểu:** Hai vai trò này thấy khuyến nghị giống chuyên viên khách hàng nhưng không sửa được số liệu. Mình đoán, chưa thử.
- **Nếu không tìm ra, hỏi BA:** Hai vai trò này có thấy khung Thẩm định và ô Khuyến nghị không, và hiển thị thế nào?

*Mã cũ: CH-15.*

## C7. Thu nhập "bằng 0" và các ô còn thiếu

- **Cần xem:** Mình thử để trống lương, gõ 0, chỉ nhập thu nhập cho thuê, và xóa số tiền vay, thời hạn hoặc giá trị khai báo (mỗi lần một ô), rồi xem màn hình hiện gì.
- **Mình đang hiểu:** Khi thiếu thu nhập, khung Thẩm định không hiện nhãn mà hiện câu "Nhập đủ thông tin…". Các trường hợp còn lại mình chưa biết.
- **Nếu không tìm ra, hỏi BA:** Thu nhập được coi là "bằng 0" trong những trường hợp nào? Thiếu số tiền vay, thời hạn hoặc giá trị tài sản thì màn hình hiện gì?

*Mã cũ: KN-02.*

## C8. Ô Mục đích có những lựa chọn nào?

- **Cần xem:** Mình mở ô Mục đích xem có những lựa chọn nào.
- **Mình đang hiểu:** Chỉ có Mua nhà (LTV tối đa 80%) và Xây/sửa nhà (70%).
- **Nếu có mục đích khác, hỏi BA:** LTV tối đa của từng mục đích là bao nhiêu?

*Mã cũ: KN-06.*

## C9. Vì sao ô Sản phẩm tự quay về sản phẩm 12 tháng?

- **Cần xem:** Mình đổi mục đích qua lại, xem danh sách sản phẩm của từng mục đích và lúc nào ô Sản phẩm tự đổi.
- **Mình đang hiểu:** Danh sách sản phẩm phụ thuộc vào mục đích, nên ô tự về mặc định khi sản phẩm cũ không còn hợp. Mình đoán.
- **Nếu không tìm ra, hỏi BA:** Quy tắc tự đặt lại sản phẩm là gì? Sản phẩm nào đi với mục đích nào?

*Mã cũ: KN-07.*

## C10. Số người phụ thuộc nhập được trong khoảng nào?

- **Cần xem:** Mình thử 0, 1, 3, 4, một số rất lớn, số âm, số lẻ, và ca 5, 20 người phụ thuộc khi ô chi phí để trống.
- **Mình đang hiểu:** Số nguyên không âm, chi phí được tính tăng theo số người.
- **Nếu không tìm ra, hỏi BA:** Số người phụ thuộc nhập được trong khoảng nào?

*Mã cũ: KN-08.*

## C11. Ô tiền có giá trị tối đa không?

- **Cần xem:** Mình nhập một số rất lớn (như 99.999.999.999.999) và bấm Lưu trên hồ sơ nháp của mình, xem có lỗi không.
- **Mình đang hiểu:** Chưa thấy giới hạn. Mình đã nhập 99.999.999.999.999 vào ô lương (chưa lưu) và không có lỗi.
- **Nếu không tìm ra, hỏi BA:** Ô tiền có giới hạn giá trị tối đa hoặc độ dài không?

*Mã cũ: KN-09.*

## C12. Thời hạn vay và ân hạn nhập được trong khoảng nào?

- **Cần xem:** Mình thử thời hạn 0, 1 và một số rất lớn, ân hạn 0, bằng thời hạn và lớn hơn thời hạn.
- **Mình đang hiểu:** Mình đã lưu được các thời hạn 20, 34, 35, 40 năm và ân hạn 12 tháng.
- **Nếu không tìm ra, hỏi BA:** Thời hạn vay và ân hạn nhập được trong khoảng nào? Ân hạn có bị giới hạn bởi thời hạn không?

*Mã cũ: KN-11.*

## C13. Nhãn trạng thái của bước đổi theo quy tắc nào?

- **Cần xem:** Mình xem nhãn trạng thái của từng bước sau khi lưu đủ, lưu thiếu và lưu khi để trống.
- **Mình đang hiểu:** Bước Tài chính chỉ mở sau khi xong bước Người vay. Bước ghi "Đã xong" sau khi lưu đủ thông tin. Bước Lãi suất ghi "Chưa mở" khi chưa có khuyến nghị. Phần cuối mình chưa chắc.
- **Nếu không tìm ra, hỏi BA:** Các nhãn trạng thái của bước đổi theo quy tắc nào? Khi nào bước Lãi suất được mở?

*Mã cũ: KN-12.*

## C14. Ngôn ngữ đã chọn có được nhớ khi mở lại không?

- **Cần xem:** Mình chọn English, đóng rồi mở lại trang.
- **Mình đang hiểu:** Ngôn ngữ được nhớ. Mình chưa thử.
- **Nếu không tìm ra, hỏi BA:** Ngôn ngữ người dùng đã chọn có được lưu lại không?

*Mã cũ: KN-15.*

---

## Đối chiếu mã cũ và mã mới

| Mã mới | Mã cũ | Nhóm |
|---|---|---|
| A1 | CH-02, CH-03, KN-05 | Hỏi ngay |
| A2 | CH-04 | Hỏi ngay |
| A3 | KN-01 | Hỏi ngay |
| A4 | KN-03 | Hỏi ngay |
| A5 | CH-01 | Hỏi ngay |
| B1 đến B12 | CH-16, CH-14, CH-05, CH-06, CH-07, CH-08, CH-17, CH-18, KN-04, KN-13, KN-14, KN-16 | Hỏi sau |
| C1 đến C14 | CH-09, CH-10, CH-11, CH-12, CH-13 và KN-10, CH-15, KN-02, KN-06, KN-07, KN-08, KN-09, KN-11, KN-12, KN-15 | Tự kiểm tra trước |

Đủ 34 mã cũ: 18 CH và 16 KN đều có mặt.

## Lịch sử thay đổi

| Ngày | Thay đổi |
|---|---|
| 2026-11-17 | Tạo mới: viết lại câu hỏi BA thành dạng đọc là hiểu |
| 2026-11-17 | Viết lại toàn bộ 31 câu theo giọng nói chuyện với đồng nghiệp: kể tình huống thật trước, hỏi sau, xưng "mình", gọi BA là "anh/chị"; thống nhất từ "mức tối đa" và "hết hạn vay" |
