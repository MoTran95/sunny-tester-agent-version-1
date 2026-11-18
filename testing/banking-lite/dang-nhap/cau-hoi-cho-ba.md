# Câu hỏi cho BA — Đăng nhập (Banking Lite)

| | |
|---|---|
| Ngày soạn | 2026-11-17 |
| Dùng để | Gửi BA. Mỗi câu có tình huống thật, câu hỏi, cách mình đang hiểu và lý do hỏi |
| Nguồn | [SRS Đăng nhập](../../../srs/banking-lite/dang-nhap.md) và [bảng soát](bang-soat-requirement.md). Mã cũ ghi ở cuối mỗi câu để tra chéo |
| Cách dùng | Gửi **Phần A** trước. **Phần B** gom hỏi một lần sau. **Phần C** là việc mình tự kiểm tra trên hệ thống, chưa cần hỏi BA |
| Tình trạng | A1–A6, B1, B3, B12, B13 đã được BA trả lời ngày 2026-11-18 (người dùng chuyển lại trong chat). Các câu còn lại chưa hỏi BA. C6 không cần làm nữa |

## Đọc trước 1 phút
Đăng nhập là cổng vào hệ thống: nhân viên nhập **Mã nhân viên** và **Mật khẩu** để vào "Danh sách việc". Phần này cũng có đăng xuất, đổi ngôn ngữ ngay ở màn hình đăng nhập, và chặn khi đăng nhập sai nhiều lần.

**Một điều quan trọng:** SRS mình đang đọc là bản nháp, viết lại từ việc xem hệ thống banking-lite bản 1.3.0 đang chạy. Nó chưa phải tài liệu yêu cầu của BA. Nên mọi chỗ ghi "đã rõ" chỉ có nghĩa là "hệ thống đang làm vậy", chưa chắc là đúng. Nếu anh/chị có tài liệu yêu cầu chính thức của Đăng nhập, cho mình xin. Nhiều câu dưới đây sẽ tự có đáp án.

| Từ | Nghĩa trong file này |
|---|---|
| Lỗi 400 | Hệ thống báo dữ liệu nhập không hợp lệ (ô trống, mã quá dài). Mình thấy qua công cụ đọc mạng của trình duyệt |
| Lỗi 401 | Hệ thống báo thông tin đăng nhập không đúng |
| Lỗi 429 | Hệ thống chặn vì đăng nhập sai quá nhiều lần |
| "Mã không gian" | Chữ đang hiện trong câu báo sai thông tin. Bản English ghi "Workspace". Theo câu trả lời A5: đã bị bỏ |

**Các mức hệ thống đang dùng** (mình quan sát được, chưa có tài liệu chính thức): bị chặn 5 phút sau nhiều lần đăng nhập sai; mã nhân viên 210 ký tự bị từ chối; mật khẩu 3 ký tự không bị báo "quá ngắn".

**Quy ước từ ngữ trong file này:** "mức tối đa", "mức tối thiểu"; "bị chặn" (không dùng "bị khóa"); chữ đang hiện trên màn hình để trong dấu ngoặc kép.

---

# Phần A. Hỏi ngay (6 câu, đều đã có trả lời)

Các câu này làm đổi kết quả đúng, nên cần trả lời sớm.

## A1. Đang bị chặn mà nhập đúng vẫn vào được, có đúng ý không?

**Người trả lời gợi ý:** BA và Dev

Mình đăng nhập sai liên tiếp cho tới khi màn hình báo "Too many failed attempts. Try again in 5 minutes." (lúc 14:23). Khoảng 2 phút sau, tức vẫn trong 5 phút bị chặn, mình nhập đúng mã P100001 và đúng mật khẩu. Hệ thống cho vào Danh sách việc như bình thường.

**Hỏi:** Anh/chị cho mình hỏi: khi đang bị chặn, người nhập đúng thông tin có phải vẫn được vào không?

**Mình đang hiểu:** Mình chưa chắc. Có thể chặn chỉ áp cho các lần nhập sai. Cũng có thể đây là lỗi, vì thường đã chặn thì ai cũng không vào được. Mình chưa kết luận là lỗi.

**Vì sao hỏi:** Nếu BA muốn chặn hẳn, thì kết quả đúng của ca này là "không vào được" và hệ thống đang làm khác.

**Anh/chị chọn:**

- [ ] Đúng ý: nhập đúng thì luôn được vào, kể cả đang bị chặn
- [x] Không đúng: đang bị chặn thì nhập đúng cũng phải bị chặn
- [ ] Khác: ______

**Câu trả lời của BA:** Đang bị chặn thì không được vào. Sau 5 phút mới được vào kể từ lúc bị chặn. (TL-01, 2026-11-18)

**So với hệ thống hiện tại:** khác. Hệ thống đang cho vào khi bị chặn. BA đã trả lời nên đây là nghi lỗi, chưa phải lỗi đã xác nhận trên hệ thống.

*Mã cũ: S02-AC08, R06, Q06.*

---

## A2. Mấy lần đăng nhập sai thì bị chặn, và lần nào được tính?

**Người trả lời gợi ý:** BA và Dev

SRS ghi bị chặn sau "10 lần liên tiếp". Mình đếm lại các lần gửi form từ lần đăng nhập đúng gần nhất tới lúc bị chặn: 1 lần để trống mã nhân viên (báo 401), 8 lần mã sai dạng (báo 401), 1 lần mã 210 ký tự (báo 400). Tổng 10 lần, và lần thứ 11 bị chặn.

Con số 10 chỉ đúng với một cách đếm. Cách đếm khác cho số khác:

| Cách đếm | Số lần sai đã đếm khi bị chặn |
|---|---|
| Tính cả lỗi 400 (ô trống, mã quá dài); đăng nhập đúng thì đếm lại từ 0 | 10 |
| Chỉ tính lỗi 401; đăng nhập đúng thì đếm lại từ 0 | 9 |
| Chỉ tính lỗi 401; đăng nhập đúng không đếm lại từ 0 | 11 |
| Tính cả lỗi 400; đăng nhập đúng không đếm lại từ 0 | 14 |

**Hỏi:** Anh/chị cho mình hỏi: hệ thống chặn sau bao nhiêu lần đăng nhập sai, lỗi để trống ô có tính không, và đăng nhập đúng có đưa số đếm về 0 không?

**Mình đang hiểu:** Mình đoán là 10 lần, có tính lỗi để trống ô, và về 0 khi đăng nhập đúng, vì chỉ cách đếm này ra đúng 10. Đó chỉ là đoán. Mình cũng chưa biết 10 lần này phải nằm trong bao lâu.

**Vì sao hỏi:** SRS đang ghi "10 lần" như đã chắc, nhưng đã có tới bốn con số có thể đúng. Muốn test ca "bị chặn" thì phải biết đúng lần thứ mấy.

**Anh/chị chọn:**

- Số lần sai thì bị chặn: 10
- Lỗi để trống ô hoặc mã quá dài: [x] có tính  [ ] không tính (trả lời: không phân biệt lỗi gì)
- Đăng nhập đúng: [x] đếm lại từ 0  [ ] không đếm lại (trả lời ở A6, TL-06)
- Các lần sai phải nằm trong khoảng: không tính thời gian, chỉ tính số lần (trả lời ở A6, TL-06)

**Câu trả lời của BA:** 10 lần liên tiếp là chặn, không phân biệt lỗi gì hết. Được tính từ lần nhập sai đầu tiên. (TL-02, 2026-11-18)

**So với hệ thống hiện tại:** khớp ở số lần và loại lỗi, nhưng hệ thống chặn ở lần thứ 11, lệch một lần (xem A6, TL-11). Hai chỗ còn lại đã được trả lời ở A6.

*Mã cũ: S02-AC07, R06, Q06.*

---

## A3. Để trống một ô, hoặc nhập mã quá dài, màn hình phải báo câu gì?

**Người trả lời gợi ý:** BA

Mình thử ba ca:

- Để trống Mật khẩu (mã nhập gì cũng vậy, kể cả `abc123`): khung đỏ có hai dòng, "Một số giá trị không hợp lệ." và `validation.too_small (password)`.
- Để trống Mã nhân viên, có nhập mật khẩu: không có câu "bắt buộc nhập mã". Màn hình báo "Mã không gian, mã nhân viên hoặc mật khẩu không đúng." Ô này vẫn có dấu `*`.
- Nhập mã nhân viên 210 ký tự: "Một số giá trị không hợp lệ." và `validation.too_big (employeeId)`.

Dòng thứ hai là mã kỹ thuật bằng tiếng Anh. Đổi sang Tiếng Việt thì dòng này vẫn giữ nguyên.

**Hỏi:** Anh/chị cho mình hỏi: khi để trống một ô hoặc nhập quá dài, màn hình phải hiện câu nào?

**Mình đang hiểu:** Mình chưa chắc dòng mã kỹ thuật là chủ ý. Mình đoán đây là câu chưa được dịch, vì màn hình Định giá cũng có kiểu `validation.too_small (marketValue)`. Mình cũng đoán ô Mã nhân viên để trống phải báo "bắt buộc", vì ô có dấu `*`.

**Vì sao hỏi:** Câu báo là kết quả đúng của ít nhất ba ca. Nếu BA có câu riêng cho từng ô thì cả ba ca đều đổi.

**Anh/chị chọn:**

- [ ] Giữ như hiện tại
- [ ] Mỗi ô một câu rõ nghĩa, có dịch. Câu cho Mã nhân viên trống: ______. Câu cho Mật khẩu trống: ______. Câu khi mã quá dài: ______
- [x] Khác: một câu chung cho mọi trường hợp là "mã nhân viên hoặc mật khẩu không đúng". Không báo các câu khác

**Câu trả lời của BA:** Màn hình phải báo "mã nhân viên hoặc mật khẩu không đúng". Không báo những câu kia. (TL-03, 2026-11-18)

**So với hệ thống hiện tại:** khác. Hệ thống đang báo hai dòng kèm mã kỹ thuật khi để trống mật khẩu hoặc nhập mã quá dài, và câu sai thông tin còn cụm "Mã không gian". **Còn lại:** nguyên văn đầy đủ và bản English. Hỏi ở B13.

*Mã cũ: S02-AC03, S02-AC05, S02-AC06, S03-AC02, R04, M03, M04, Q03, Q05.*

---

## A4. Mã nhân viên hợp lệ gồm những gì: chữ thường, khoảng trắng, độ dài?

**Người trả lời gợi ý:** BA và Dev

Dòng gợi ý dưới ô ghi "Chữ P và 6 chữ số, ví dụ P100001." Mình thấy:

- Gõ `p100001` (chữ p thường) vẫn đăng nhập được. Thanh trên hiện `P100001` chữ hoa.
- Các mã P99999, P9999999, X999999, P99999A, P99-999, và mã có khoảng trắng đầu hoặc cuối đều chỉ nhận câu "Mã không gian, mã nhân viên hoặc mật khẩu không đúng." Không có câu nào nói "sai dạng". (Cả tám mã này đều là mã không tồn tại.)
- Mã 210 ký tự bị từ chối. Mình chưa biết mức tối đa là bao nhiêu.
- Mình chưa thử mã thật có khoảng trắng, ví dụ `P100001 `.

**Hỏi:** Anh/chị cho mình hỏi: mã nhân viên hợp lệ phải theo quy tắc nào, và hệ thống có tự chỉnh chữ hoa và khoảng trắng không?

**Mình đang hiểu:** Mình đoán hệ thống cố ý đổi chữ thường thành chữ hoa. Mình chưa chắc về khoảng trắng, và chưa chắc việc không báo riêng lỗi sai dạng có phải chủ ý.

**Vì sao hỏi:** Chữ thường và khoảng trắng quyết định ca nào được vào, ca nào bị từ chối. SRS cũng đang xếp `p999999` vào nhóm "sai dạng" trong khi chữ thường lại được chấp nhận.

**Anh/chị chọn:**

- Chữ thường: [x] chấp nhận (hoa thường đều được; chưa nói có đổi thành chữ hoa không)  [ ] không chấp nhận
- Khoảng trắng đầu/cuối: [x] tự cắt bỏ  [ ] coi là sai (người dùng xác nhận "tự cắt bỏ" ngày 2026-11-18)
- Mã sai dạng (thiếu số, thừa số, có chữ khác): [x] báo chung (cùng câu ở A3)  [ ] báo riêng, câu: ______
- Mã nhân viên dài nhất là: không quy định ở màn hình đăng nhập (giới hạn độ dài thuộc phần đăng ký)

**Câu trả lời của BA:** Khoảng trắng đầu/cuối: tự cắt bỏ. Chữ p thì hoa thường đều được. Độ dài không quy định vì đã chặn là phần đăng ký, nhập đúng là được. (TL-04, 2026-11-18)

**So với hệ thống hiện tại:** khớp ở chữ thường, khác ở độ dài (hệ thống từ chối mã 210 ký tự). Khoảng trắng với mã thật chưa thử (mục C1). **Còn lại:** dòng gợi ý "Chữ P và 6 chữ số" còn giữ không.

*Mã cũ: S01-AC04, S02-AC04, S02-AC06, R01, R02, R03, Q04.*

---

## A5. "Mã không gian" trong câu báo sai thông tin là gì?

**Người trả lời gợi ý:** BA

Khi nhập sai, màn hình báo "Mã không gian, mã nhân viên hoặc mật khẩu không đúng." Nhưng form chỉ có hai ô: Mã nhân viên và Mật khẩu. Không có ô nào là "mã không gian". Sau khi đăng nhập, thanh trên hiện `P100001 · Chuyên viên khách hàng · DEFAULT`. Bản English của câu báo (mình chỉ thấy trong tệp giao diện) ghi "Workspace, employee ID or password is incorrect."

**Hỏi:** Anh/chị cho mình hỏi: "mã không gian" (Workspace) là gì, và người đăng nhập có phải nhập nó không?

**Mình đang hiểu:** Mình đoán "mã không gian" là bản dịch của Workspace, và `DEFAULT` trên thanh trên là giá trị của nó. Mình chưa chắc là người dùng có bao giờ phải nhập, hay câu báo nên bỏ cụm này.

**Vì sao hỏi:** Đây là câu mọi ca đăng nhập sai đều hiện ra, nên mình cần biết nguyên văn đúng. Nếu form phải có thêm ô Workspace thì cả màn hình đổi.

**Anh/chị chọn:**

- [ ] Chỉ là tên bên trong hệ thống. Câu báo nên bỏ cụm "mã không gian"
- [ ] Sau này form sẽ có ô này. Câu báo hiện tại đúng
- [x] Khác: mã không gian (Workspace) đã bị bỏ, không còn được sử dụng

**Câu trả lời của BA:** Mã không gian là bị bỏ, không còn được sử dụng. (TL-05, 2026-11-18)

**So với hệ thống hiện tại:** khác. Câu báo còn cụm "Mã không gian", thanh trên còn `DEFAULT`. **Còn lại:** thanh trên và `/api/me` có bỏ `DEFAULT` không. Hỏi ở B12.

*Mã cũ: S01-AC02, M01, R05, Q01.*

---

## A6. Đăng nhập đúng xen giữa các lần sai thì đếm sao, và lần sai thứ 10 báo gì?

**Người trả lời gợi ý:** BA và Dev

Câu trả lời của A2 là 10 lần sai liên tiếp thì bị chặn, và "được tính từ lần nhập sai đầu tiên". Mình chưa thử các tình huống dưới đây trên hệ thống, vì mỗi lần sai đều tính vào 10 lần. Mình chưa chắc hiểu đúng ba chỗ:

- Mình sai 9 lần, nhập đúng một lần và vào được, rồi đăng xuất và sai thêm 1 lần. Lần sai đó là lần thứ 1 hay lần thứ 10?
- Mình sai 5 lần buổi sáng và 5 lần buổi chiều cùng ngày, giữa hai buổi không có lần đúng. Mình có bị chặn không, hay 10 lần sai phải nằm trong một khoảng thời gian?
- Hệ thống hiện báo sai thông tin bình thường ở 10 lần sai đầu. Tới lần thứ 11 mới báo "Too many failed attempts. Try again in 5 minutes."

**Hỏi:** Anh/chị cho mình hỏi: đăng nhập đúng có đưa số lần sai về 0 không, 10 lần sai có phải nằm trong một khoảng thời gian nào không, và lần sai thứ 10 còn báo sai thông tin hay đã báo bị chặn?

**Mình đang hiểu:** Mình đoán đăng nhập đúng thì đếm lại từ 0 (vì ghi "liên tiếp"), không có khoảng thời gian, và 10 lần sai đầu đều báo sai thông tin, tới lần thứ 11 mới bị chặn, giống hệ thống đang làm. Đó chỉ là đoán.

**Vì sao hỏi:** Ba chỗ này quyết định các ca sát biên: sai 9 lần, sai 10 lần và sai 11 lần. Cần biết đúng lần nào bị chặn.

**Anh/chị chọn:**

- Đăng nhập đúng xen giữa: [x] đếm lại từ 0  [ ] không đếm lại
- 10 lần sai phải nằm trong khoảng: ______ phút  [x] không giới hạn thời gian (chỉ tính số lần, không tính thời gian)
- Lần sai thứ 10 báo: [ ] sai thông tin, từ lần thứ 11 mới chặn  [x] bị chặn ngay ở lần thứ 10

**Câu trả lời của BA:** Đăng nhập đúng xen giữa đưa số lần sai về 0. Chỉ tính số lần, không tính thời gian. (TL-06, 2026-11-18) Lần sai thứ 10 thì báo bị chặn. (TL-11, 2026-11-18)

**So với hệ thống hiện tại:** đếm lại khi đăng nhập đúng khớp SRS. Lần sai thứ 10: khác. Hệ thống báo sai thông tin ở 10 lần đầu, lần thứ 11 mới báo bị chặn (lệch một lần). BA đã trả lời nên đây là nghi lỗi, chưa phải lỗi đã xác nhận.

*Mã cũ: S02-AC07, R06 (nảy ra từ câu trả lời A2).*

---

# Phần B. Hỏi sau, gom một lần (13 câu, B1, B3, B12, B13 đã có trả lời)

Các câu này chủ yếu về hiển thị, câu chữ, hoặc phần mình chưa test được.

## B1. Mã không tồn tại và sai mật khẩu dùng chung một câu, có đúng ý không?

**Người trả lời gợi ý:** BA

Mình thử `P100001` với mật khẩu sai, rồi `P999999` (mã không có thật) với mật khẩu bất kỳ. Cả hai đều hiện đúng một câu: "Mã không gian, mã nhân viên hoặc mật khẩu không đúng."

**Hỏi:** Anh/chị cho mình hỏi: hai trường hợp này có chủ ý dùng chung một câu không?

**Mình đang hiểu:** Mình đoán là chủ ý, nhưng tài liệu không nói gì về việc này.

**Vì sao hỏi:** Nếu mỗi trường hợp phải có câu riêng thì kết quả đúng của hai ca đổi.

**Câu trả lời của BA:** Câu "mã nhân viên hoặc mật khẩu không đúng" nói chung cả mã lẫn mật khẩu, nên hai trường hợp dùng chung một câu. (TL-10, 2026-11-18)

**So với hệ thống hiện tại:** khớp (hệ thống dùng chung một câu cho hai trường hợp).

*Mã cũ: S02-AC01, S02-AC02, Q02.*

---

## B2. Việc chặn tính theo cái gì: mã nhân viên, trình duyệt, hay cả hệ thống?

**Người trả lời gợi ý:** BA và Dev

Mình thử đăng nhập sai bằng các mã không có thật mà vẫn bị chặn. Nên việc chặn không chỉ theo tài khoản có thật. Mình chưa biết hệ thống đếm theo mã nhân viên, theo trình duyệt (hoặc địa chỉ mạng), hay chung cho cả hệ thống.

**Hỏi:** Anh/chị cho mình hỏi: khi bị chặn, ai bị ảnh hưởng?

**Mình đang hiểu:** Mình chưa chắc. Mình chưa thử đổi trình duyệt khi đang bị chặn.

**Vì sao hỏi:** Nếu chặn chung cả hệ thống thì một người nhập sai có thể làm người khác không đăng nhập được. Mình cần biết để dựng ca test đúng.

**Anh/chị chọn:**

- [ ] Theo mã nhân viên
- [ ] Theo trình duyệt / địa chỉ mạng
- [ ] Chung cho cả hệ thống
- [ ] Khác: ______

**Câu trả lời của BA:** ______

*Mã cũ: R06, Q06.*

---

## B3. Hết 5 phút thì hết chặn chưa, và có luôn là 5 phút không?

**Người trả lời gợi ý:** BA và Dev

Màn hình báo "Try again in 5 minutes." Mình chưa chờ hết 5 phút để thử lại, vì thử sai thêm có thể bị chặn tiếp.

**Hỏi:** Anh/chị cho mình hỏi: sau 5 phút người dùng có tự đăng nhập lại được không, và số phút này có đổi không (ví dụ tăng dần khi sai tiếp)?

**Mình đang hiểu:** Mình đoán là tự hết sau 5 phút, và lúc nào cũng là 5 phút. Mình chưa kiểm.

**Vì sao hỏi:** Có hai ca test cần biết: lúc chưa hết hạn chặn và lúc đã hết.

**Câu trả lời của BA:** Hết 5 phút là hết chặn, lúc bị chặn nhập thêm không tính. Sau khi hết 5 phút nhập sai thì mới được tính số lần lại. (TL-09, 2026-11-18)

**So với hệ thống hiện tại:** chưa kiểm. Mình không chờ hết 5 phút để thử, vì thử sai thêm có thể bị chặn tiếp.

*Mã cũ: R06, Q06.*

---

## B4. Câu báo bị chặn bằng Tiếng Việt có đúng như trong tệp giao diện không?

**Người trả lời gợi ý:** BA

Bản English hiện trên màn hình: "Too many failed attempts. Try again in 5 minutes." Bản Tiếng Việt mình chưa thấy hiện lần nào. Trong tệp giao diện có câu "Đăng nhập sai quá nhiều lần. Thử lại sau {minutes} phút."

**Hỏi:** Anh/chị cho mình hỏi: bản Tiếng Việt có đúng là câu này không, và {minutes} có được thay bằng 5 không?

**Mình đang hiểu:** Mình đoán là đúng, {minutes} thành 5.

**Vì sao hỏi:** Mình chưa tự thấy được câu này trên màn hình mà không cố ý làm mình bị chặn.

**Câu trả lời của BA:** ______

*Mã cũ: M05, S02-AC07.*

---

## B5. Đăng nhập xong quay lại đúng link đã mở, áp dụng cho mọi link không?

**Người trả lời gợi ý:** BA

Mình mở link hồ sơ HL-000019 (hồ sơ do chính P100001 tạo) khi chưa đăng nhập. Hệ thống hiện form đăng nhập, giữ nguyên link. Đăng nhập đúng xong thì vào thẳng hồ sơ đó. Mình chưa thử link hồ sơ của người khác hay hồ sơ mà vai trò này không được xem.

**Hỏi:** Anh/chị cho mình hỏi: cách quay lại link này áp dụng cho mọi link không, kể cả hồ sơ người khác tạo hoặc hồ sơ vai trò này không có quyền xem?

**Mình đang hiểu:** Mình đoán mọi link đều quay lại, và quyền xem được kiểm khi hồ sơ mở ra. Mình chưa thử.

**Vì sao hỏi:** Nếu link không có quyền xem phải về Danh sách việc thì kết quả đúng đổi.

**Câu trả lời của BA:** ______

*Mã cũ: S01-AC03, Q07.*

---

## B6. Mở `/login` khi đã đăng nhập, hoặc mở địa chỉ không có thật, hệ thống làm vậy có đúng ý không?

**Người trả lời gợi ý:** BA

Khi đã đăng nhập: mở `/login` thì hiện Danh sách việc nhưng thanh địa chỉ vẫn là `/login`. Mở địa chỉ không có thật, ví dụ `/khong-ton-tai-xyz`, cũng hiện Danh sách việc, giữ nguyên địa chỉ, không có trang "không tìm thấy". Khi chưa đăng nhập: mở địa chỉ không có thật thì hiện form đăng nhập, cũng giữ nguyên địa chỉ.

**Hỏi:** Anh/chị cho mình hỏi: đây có phải cách hệ thống phải làm không, hay cần chuyển sang trang chủ hoặc hiện trang "không tìm thấy"?

**Mình đang hiểu:** Mình chưa chắc. Mình đoán đây là mặc định chưa ai chỉnh, không phải chủ ý.

**Vì sao hỏi:** Nếu cần chuyển hướng hoặc trang "không tìm thấy" thì ba ca đều đổi.

**Câu trả lời của BA:** ______

*Mã cũ: S01-AC07, S01-AC08, S04-AC02, Q08.*

---

## B7. Khi bị đăng xuất ở nơi khác, màn hình có phải báo "Vui lòng đăng nhập." không?

**Người trả lời gợi ý:** BA

Mình mở hai tab cùng một phiên và đăng xuất ở tab 2. Tab 1 vẫn hiện Danh sách việc cho tới khi mình bấm "Tất cả hồ sơ". Lúc đó tab 1 chuyển sang form đăng nhập, không có thông báo nào. Trong tệp giao diện có câu "Vui lòng đăng nhập." nhưng mình chưa thấy nó hiện lần nào.

**Hỏi:** Anh/chị cho mình hỏi: lúc tab 1 bị đưa về form đăng nhập, màn hình có phải hiện câu "Vui lòng đăng nhập." không?

**Mình đang hiểu:** Mình đoán là có, câu này sinh ra cho tình huống này. Mình chưa chắc.

**Vì sao hỏi:** Nếu có thì ca này hiện đang thiếu thông báo.

**Câu trả lời của BA:** ______

*Mã cũ: S04-AC04, M06, Q09.*

---

## B8. Phiên đăng nhập giữ được bao lâu, hết hạn thì màn hình làm gì?

**Người trả lời gợi ý:** Dev

Mình tải lại trang (F5) thì vẫn đang đăng nhập. Mình chưa chờ để xem bao lâu không thao tác thì bị đăng xuất. Mình cũng không đọc được cách hệ thống giữ phiên: không có khóa phiên trong bộ nhớ trình duyệt, và `document.cookie` rỗng.

**Hỏi:** Anh/chị cho mình hỏi: phiên giữ được bao lâu, và khi hết hạn người dùng thấy gì?

**Mình đang hiểu:** Mình đoán là có thời hạn, nhưng chưa biết bao lâu.

**Vì sao hỏi:** Mình không chờ được vài giờ để thử, nên cần con số để biết khi nào kiểm.

**Câu trả lời của BA:** ______

*Mã cũ: S01-AC06, Q10.*

---

## B9. Sau khi báo lỗi, ô Mật khẩu nên giữ chữ đã gõ hay xóa?

**Người trả lời gợi ý:** BA

Mình gõ `P100001` và mật khẩu sai 3 ký tự, bấm Đăng nhập. Khung đỏ hiện. Ô Mã nhân viên giữ chữ đã gõ. Ô Mật khẩu cũng còn nguyên 3 ký tự. SRS chỉ ghi ô Mã nhân viên giữ chữ.

**Hỏi:** Anh/chị cho mình hỏi: sau khi báo lỗi, ô Mật khẩu phải giữ chữ đã gõ hay phải xóa?

**Mình đang hiểu:** Mình thấy hệ thống đang giữ. Mình chưa chắc đó là chủ ý.

**Vì sao hỏi:** Chi tiết này không có trong SRS, nên mình cần BA nói là đúng hay sai.

**Câu trả lời của BA:** ______

*Mã cũ: S02 (luồng chung).*

---

## B10. Các chức năng chưa thấy trên màn hình đăng nhập là chưa làm hay không làm?

**Người trả lời gợi ý:** BA

Màn hình đăng nhập chưa có "quên mật khẩu", "đổi mật khẩu", "đăng ký", "ghi nhớ đăng nhập", và ô chọn Workspace. SRS ghi các chức năng này là "chưa có" nên mình chưa soát chúng.

**Hỏi:** Anh/chị cho mình hỏi: những chức năng này là chưa làm (sẽ có sau) hay không làm?

**Mình đang hiểu:** Mình chưa chắc. Mình tạm xem đây là phần chưa cần test cho tới khi anh/chị trả lời.

**Vì sao hỏi:** Nếu sẽ có thì mình cần biết sớm để không bỏ sót.

**Câu trả lời của BA:** Một phần: ô chọn Workspace đã rõ ở A5 là bỏ. Các chức năng còn lại chưa trả lời. Lưu ý: câu trả lời A4 có nhắc "phần đăng ký", mình chưa biết nó nằm ở đâu.

*Mã cũ: phạm vi trong mục 1 của SRS.*

---

## B11. Mật khẩu hợp lệ dài bao nhiêu ký tự và gồm những gì?

**Người trả lời gợi ý:** BA và Dev

Mật khẩu để trống thì bị báo `validation.too_small (password)`, nên có mức tối thiểu. Mình gõ mật khẩu sai 3 ký tự thì chỉ bị báo "Mã không gian, mã nhân viên hoặc mật khẩu không đúng.", nên mức tối thiểu không quá 3. Mình chưa biết mức tối đa, và chưa thử ký tự đặc biệt hay khoảng trắng. Mỗi lần thử sai đều tính vào giới hạn đăng nhập sai (xem câu A2), nên mình chưa dám thử.

**Hỏi:** Anh/chị cho mình hỏi: mật khẩu ít nhất và nhiều nhất bao nhiêu ký tự, và có cho khoảng trắng hay ký tự đặc biệt không?

**Mình đang hiểu:** Mình đoán mức tối thiểu là 1 ký tự. Mình chưa biết mức tối đa.

**Vì sao hỏi:** Cần biết mức này để dựng các ca sát biên.

**Câu trả lời của BA:** Chưa trả lời. Gợi ý từ A3 và A4: ô mật khẩu trống chỉ báo câu chung, và độ dài mã nhân viên thuộc phần đăng ký. Chưa nói với độ dài mật khẩu.

*Mã cũ: phần "chưa khám phá" trong mục 6.2 của SRS, M03.*

---

## B12. Mã không gian đã bỏ, thanh trên còn hiện `DEFAULT` không?

**Người trả lời gợi ý:** BA và Dev

Sau khi mình đăng nhập P100001, thanh trên hiện `P100001 · Chuyên viên khách hàng · DEFAULT`. Qua công cụ đọc mạng, `/api/me` trả `workspace` là `DEFAULT`. Câu trả lời A5 nói mã không gian đã bị bỏ.

**Hỏi:** Anh/chị cho mình hỏi: chữ `DEFAULT` trên thanh trên, và trường `workspace` trong dữ liệu `/api/me`, có phải bỏ theo không?

**Mình đang hiểu:** Mình đoán `DEFAULT` chính là mã không gian nên cũng phải bỏ khỏi thanh trên. Mình chưa chắc, vì câu trả lời A5 chỉ nói mã không gian bị bỏ, chưa nói thanh trên có đổi.

**Vì sao hỏi:** Thanh trên hiện ở mọi màn hình sau khi đăng nhập. Nếu phải bỏ chữ `DEFAULT` thì kết quả đúng của các ca xem thanh trên đổi.

**Câu trả lời của BA:** Bỏ. (TL-07, 2026-11-18)

**So với hệ thống hiện tại:** khác. Thanh trên còn `DEFAULT` và `/api/me` còn trả `workspace`.

*Mã cũ: S01-AC02, R05, M01 (nảy ra từ câu trả lời A5).*

---

## B13. Câu báo sai thông tin viết nguyên văn thế nào, Tiếng Việt và English?

**Người trả lời gợi ý:** BA

Theo câu trả lời A3 và A5, câu báo là "mã nhân viên hoặc mật khẩu không đúng", không còn cụm "Mã không gian". Hệ thống hiện báo "Mã không gian, mã nhân viên hoặc mật khẩu không đúng." Bản English mình chỉ thấy trong tệp giao diện: "Workspace, employee ID or password is incorrect."

**Hỏi:** Anh/chị cho mình hỏi: câu mới viết nguyên văn thế nào (có viết hoa chữ đầu và dấu chấm cuối không), và bản English là câu gì?

**Mình đang hiểu:** Mình đoán Tiếng Việt là "Mã nhân viên hoặc mật khẩu không đúng." và English là "Employee ID or password is incorrect.", tức là bỏ cụm đầu của câu hiện tại. Đó chỉ là đoán.

**Vì sao hỏi:** Đây là kết quả đúng của mọi ca đăng nhập sai, ô trống và mã quá dài, nên cần chép đúng từng chữ.

**Câu trả lời của BA:** Tiếng Việt: "Mã nhân viên hoặc mật khẩu không đúng." English: "Employee ID or password is incorrect." (TL-08, 2026-11-18)

**So với hệ thống hiện tại:** khác. Hệ thống còn cụm "Mã không gian" (bản English còn "Workspace") và hai chỗ trùng với đoán của mình.

*Mã cũ: S02-AC01, M01 (nảy ra từ câu trả lời A3 và A5).*

---

# Phần C. Mình tự kiểm tra trên hệ thống trước (9 mục, C6 không cần làm nữa)

Câu nào xem hệ thống đang chạy là tìm được câu trả lời thì mình tự làm trước, chỉ hỏi BA khi không tìm ra. Xem hệ thống chỉ cho biết hệ thống **đang làm gì**, không chứng minh là **đúng**. Chỉ dùng dữ liệu của mình, không đổi dữ liệu của người khác.

Hai điều cần nhớ:

- Mình không tự gõ mật khẩu. Mình điền sẵn ô Mã nhân viên, mật khẩu do người giữ tài khoản gõ.
- Mỗi lần nhập sai đều tính vào giới hạn (theo A2: 10 lần sai liên tiếp thì bị chặn 5 phút), và mình không biết số đếm hiện còn bao nhiêu. Mục C1 có thể có lần nhập sai (nếu hệ thống không cắt khoảng trắng). Chỉ làm khi đã báo trước, tối đa 3 lần.

## C1. Mã thật có khoảng trắng đầu hoặc cuối có đăng nhập được không?

- **Cần làm:** gõ `P100001 ` (thừa khoảng trắng cuối), rồi ` P100001` (thừa khoảng trắng đầu), cùng mật khẩu đúng. Xem vào được hay bị từ chối.
- **Mình đang hiểu:** Tám mã mình đã thử đều là mã không có thật, nên chưa biết. Mình đoán hệ thống cắt khoảng trắng, vì chữ thường cũng được chấp nhận.
- **Nếu không tìm ra, hỏi BA:** Hệ thống có phải tự cắt khoảng trắng đầu và cuối của mã nhân viên không?
- **Cập nhật 2026-11-18:** A4 đã trả lời là khoảng trắng đầu/cuối tự cắt bỏ. Mục này chỉ còn là kiểm hệ thống có làm đúng.

*Mã cũ: S02-AC04, Q04.*

## C2. Nhấn Enter ở ô Mật khẩu có gửi form không?

- **Cần làm:** nhập mã và mật khẩu đúng, đặt con trỏ ở ô Mật khẩu, nhấn Enter (không bấm nút).
- **Mình đang hiểu:** Mình mới thử Enter ở ô Mã nhân viên khi mật khẩu trống. Mình đoán Enter ở ô Mật khẩu cũng gửi form và vào được.
- **Nếu không tìm ra, hỏi BA:** Nhấn Enter ở ô nào cũng phải gửi form, đúng không?

*Mã cũ: S01-AC05.*

## C3. Mã chữ thường của P200001 và P300001 có đăng nhập được không?

- **Cần làm:** gõ `p200001` rồi `p300001` (chữ p thường) cùng mật khẩu đúng của từng tài khoản. Xem vào được không, thanh trên hiện chữ gì.
- **Mình đang hiểu:** Mình mới thử chữ thường với P100001. Mình đoán hai tài khoản kia cũng vậy.
- **Nếu không tìm ra, hỏi BA:** Quy tắc chữ thường áp dụng cho mọi tài khoản, đúng không?
- **Cập nhật 2026-11-18:** A4 đã trả lời là chữ p hoa hay thường đều được. Mục này chỉ còn là kiểm hệ thống làm đúng với hai tài khoản kia.

*Mã cũ: S01-AC04, R02.*

## C4. Tên vai trò bằng English của P200001 và P300001 là gì?

- **Cần làm:** đăng nhập từng tài khoản, bấm English, đọc tên vai trò trên thanh trên.
- **Mình đang hiểu:** Mình mới thấy `Chuyên viên khách hàng` đổi thành `Banker`. Hai vai trò kia, Tiếng Việt là `Chuyên viên định giá` và `Chuyên viên thẩm định tín dụng`, mình chưa thấy tên English.
- **Nếu không tìm ra, hỏi BA:** Tên English chính thức của hai vai trò này là gì?

*Mã cũ: S03-AC04.*

## C5. P100002 là tài khoản gì?

- **Cần làm:** đăng nhập P100002 (mật khẩu do người giữ tài khoản gõ). Xem thanh trên và Danh sách việc.
- **Mình đang hiểu:** SRS ghi vai trò của tài khoản này là chưa biết và chưa đăng nhập lần nào. Mình đoán là một Chuyên viên khách hàng thứ hai, nhưng chưa chắc.
- **Nếu không tìm ra, hỏi BA:** Tài khoản P100002 dùng để làm gì, và vai trò gì?

*Mã cũ: tài khoản P100002 trong mục 1 của SRS.*

## C6. Mã quá dài ở bản English báo câu gì?

- **Cần làm:** đổi sang English, gõ mã 210 ký tự, bấm Sign in, đọc khung lỗi. Đây là một lần nhập sai.
- **Mình đang hiểu:** SRS ghi cột English của dòng này là "chưa quan sát" nhưng lại nói dòng mã lỗi giữ nguyên ở cả hai ngôn ngữ. Mình đoán sẽ là `validation.too_big (employeeId)` giống bản Tiếng Việt.
- **Nếu không tìm ra, hỏi BA:** Câu English chính thức cho lỗi mã quá dài là gì? (Hỏi chung với câu A3.)
- **Cập nhật 2026-11-18:** không cần làm nữa. A3 đã trả lời là mã quá dài không còn hiện dòng `too_big`. Bỏ được một lần nhập sai.

*Mã cũ: M04, S03-AC02.*

## C7. Một tài khoản đăng nhập ở hai trình duyệt khác nhau thì sao?

- **Cần làm:** đăng nhập P100001 ở trình duyệt thứ nhất, rồi đăng nhập cùng tài khoản ở trình duyệt thứ hai. Quay lại trình duyệt thứ nhất, bấm một tab cần tải dữ liệu.
- **Mình đang hiểu:** Mình mới thử hai tab cùng một trình duyệt (dùng chung phiên). Mình đoán cả hai trình duyệt cùng vào được, nhưng chưa chắc.
- **Nếu không tìm ra, hỏi BA:** Một tài khoản được đăng nhập cùng lúc ở nhiều nơi không?

*Mã cũ: phần "chưa khám phá" trong mục 6.2 của SRS.*

## C8. Bấm nút Đăng nhập hai lần nhanh thì có gửi hai lần không?

- **Cần làm:** nhập thông tin đúng, bấm nút hai lần thật nhanh. Xem nút có bị khóa lúc đang gửi không, và có vào được bình thường không.
- **Mình đang hiểu:** SRS ghi ca này là chưa khám phá. Mình đoán hệ thống vẫn vào được bình thường.
- **Nếu không tìm ra, hỏi BA:** Nút Đăng nhập có phải bị khóa trong lúc đang gửi không?

*Mã cũ: phần "chưa khám phá" trong mục 6.2 của SRS.*

## C9. Khung lỗi đỏ biến mất vào lúc nào?

- **Cần làm:** làm cùng lúc với C1 nếu C1 bị từ chối (không thêm lần nhập sai). Xem khung lỗi mất khi mình gõ lại, khi bấm gửi lần mới, hay khi vừa đổi ngôn ngữ.
- **Mình đang hiểu:** Lúc khám phá, mình từng bấm đúng lúc khung lỗi biến mất và nút bị lệch chỗ. Mình đoán khung lỗi mất khi bấm gửi lần mới.
- **Nếu không tìm ra, hỏi BA:** Khung lỗi phải biến mất vào lúc nào?

*Mã cũ: S02 (luồng chung), S03-AC01.*

---

## Đối chiếu mã cũ và mã mới
| Mã mới | Mã cũ | Nhóm |
|---|---|---|
| A1 | S02-AC08, R06, Q06 | Hỏi ngay |
| A2 | S02-AC07, R06, Q06 | Hỏi ngay |
| A3 | S02-AC03, S02-AC05, S02-AC06, S03-AC02, R04, M03, M04, Q03, Q05 | Hỏi ngay |
| A4 | S01-AC04, S02-AC04, S02-AC06, R01, R02, R03, Q04 | Hỏi ngay |
| A5 | S01-AC02, M01, R05, Q01 | Hỏi ngay |
| A6 | S02-AC07, R06 (nảy ra từ A2) | Hỏi ngay |
| B1 | S02-AC01, S02-AC02, Q02 | Hỏi sau |
| B2 | R06, Q06 | Hỏi sau |
| B3 | R06, Q06 | Hỏi sau |
| B4 | M05, S02-AC07 | Hỏi sau |
| B5 | S01-AC03, Q07 | Hỏi sau |
| B6 | S01-AC07, S01-AC08, S04-AC02, Q08 | Hỏi sau |
| B7 | S04-AC04, M06, Q09 | Hỏi sau |
| B8 | S01-AC06, Q10 | Hỏi sau |
| B9 | S02 (luồng chung) | Hỏi sau |
| B10 | phạm vi (mục 1) | Hỏi sau |
| B11 | mục 6.2, M03 | Hỏi sau |
| B12 | S01-AC02, R05, M01 (nảy ra từ A5) | Hỏi sau |
| B13 | S02-AC01, M01 (nảy ra từ A3 và A5) | Hỏi sau |
| C1 | S02-AC04, Q04 | Tự kiểm tra |
| C2 | S01-AC05 | Tự kiểm tra |
| C3 | S01-AC04, R02 | Tự kiểm tra |
| C4 | S03-AC04 | Tự kiểm tra |
| C5 | tài khoản P100002 (mục 1) | Tự kiểm tra |
| C6 | M04, S03-AC02 | Tự kiểm tra (không cần làm nữa) |
| C7 | mục 6.2 | Tự kiểm tra |
| C8 | mục 6.2 | Tự kiểm tra |
| C9 | S02 (luồng chung), S03-AC01 | Tự kiểm tra |

## Lịch sử thay đổi
| Ngày | Thay đổi |
|---|---|
| 2026-11-17 | Tạo mới |
| 2026-11-18 | Ghi câu trả lời A1–A5 (TL-01 đến TL-05). Thêm A6, B12, B13. C6 không cần làm nữa. Ghi chú ở B1, B3, B10, B11, C1, C3 |
| 2026-11-18 | Ghi câu trả lời A6 (một phần), B12, B13 (TL-06 đến TL-08) |
| 2026-11-18 | Ghi nguồn: BA trả lời (người dùng chuyển lại) |
| 2026-11-18 | Ghi câu trả lời B1 (TL-10) và B3 (TL-09) |
| 2026-11-18 | Ghi câu trả lời phần cuối của A6 (TL-11): lần sai thứ 10 báo bị chặn |
