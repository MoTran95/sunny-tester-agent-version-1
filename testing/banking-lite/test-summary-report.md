# Báo cáo tổng kết kiểm thử

> File tự sinh bằng `scripts/build_docs.py` từ các lượt chạy, bug và truy vết; đừng sửa tay. Quyết định của người test và người duyệt nằm ở `testing/banking-lite/duyet-build.json` (điền trên trang HTML rồi tải file về). Bản dễ xem và có nút in PDF: `test-summary-report.html`.

## 1. Thông tin chung

| Mục | Nội dung |
|---|---|
| Dự án | banking-lite |
| Build | 1.3.0 |
| Môi trường | https://staging-banking-lite.vercel.app |
| Thời gian test | 2026-11-18 21:23:25 đến 2026-11-19 15:36:51 |
| Người viết báo cáo | Sunny Tran |
| Người test | Sunny Tran: Tự động (Playwright) (Smoke test (lượt 2); Regression Tầng 1 (lượt 1); Test case Đăng nhập (lượt 1)) |
| Phạm vi | Smoke, regression và test case theo từng tính năng: Đăng nhập, Khuyến nghị LTV/DSR |

## 2. Kết luận

**Tình trạng theo số liệu.** Tổng 81 test case của 2 tính năng: 37 đã có kết luận (46%), trong đó 22 Đạt, 1 Đạt kèm lỗi, 14 Không đạt; 2 bị chặn hoặc chưa kết luận được, 10 bỏ qua, 32 chưa chạy. 6 bug được ghi nhận trong các lượt của build này (tổng 7 bug đã ghi).

- Smoke test: Chưa đủ căn cứ nhận hay trả bản 1.3.0 theo bộ smoke ở lượt 2: 5 trên 7 case Đạt, 1 case Đạt kèm lỗi đã biết ([BUG-001](dang-nhap/bug/BUG-001.md)) và 1 case chưa kết luận được vì hồ sơ nháp dành riêng cho ca đó đã dùng hết.
- Regression Tầng 1: Chưa nên coi Tầng 1 đạt: 10 trên 13 case đạt (có 1 case đạt kèm lỗi đã biết), 2 case không đạt và 1 case chưa kết luận được; một trong hai case không đạt là phát hiện mới của Khuyến nghị.
- Test case Đăng nhập: Chưa thể kết luận đạt cho tính năng Đăng nhập ở bản 1.3.0. Các luồng chính (đăng nhập đúng, đăng xuất, mở link, tải lại trang, đổi ngôn ngữ) chạy đúng và không có lỗi nào làm người dùng không đăng nhập được. Nhưng còn 7 bug đang mở (5 bug mức Rất nhỏ, 1 bug mức Nhỏ, 1 bug mức Nặng) và 12 trong 43 case chưa có kết quả, trong đó có phần cách hệ thống chặn đăng nhập sau nhiều lần sai.

**Đề xuất của người test** (nhận build / không nhận / nhận có điều kiện):

| Mục | Nội dung |
|---|---|
| Đề xuất | (chưa điền) |
| Lý do | (chưa điền) |
| Ngày | (chưa điền) |

## 3. Kết quả theo tính năng

Mỗi test case lấy kết quả mới nhất trong các lượt của build này (smoke, regression, test case tính năng). Tỉ lệ đạt tính trên số đã có kết luận.

| Tính năng | Tổng | Đạt | Đạt kèm lỗi | Không đạt | Bị chặn / Không kết luận | Bỏ qua | Chưa chạy | Đã chạy | Tỉ lệ đạt |
|---|---|---|---|---|---|---|---|---|---|
| Đăng nhập | 43 | 17 | 1 | 13 | 2 | 10 | 0 | 72% | 58% |
| Khuyến nghị LTV/DSR | 38 | 5 | 0 | 1 | 0 | 0 | 32 | 16% | 83% |

## 4. Kết quả theo bộ test

| Bộ test | Lượt | Thời điểm | Kết quả | Kết luận | Trang kết quả |
|---|---|---|---|---|---|
| Smoke test | 2 | 2026-11-19 11:34:35 | 5 Đạt, 1 Đạt kèm lỗi đã biết, 1 Không kết luận | Chưa đủ kết luận | [mở](smoke-ket-qua.html) |
| Regression Tầng 1 | 1 | 2026-11-19 15:36:51 | 9 Đạt, 1 Đạt kèm ý phụ sai, 2 Không đạt, 1 Không kết luận | Có case không đạt | [mở](regression-tang-1-ket-qua.html) |
| Test case Đăng nhập | 1 | 2026-11-19 11:00:31 | 14 Không đạt, 17 Đạt, 2 Bị chặn, 10 Bỏ qua | Có case không đạt | [mở](dang-nhap/ket-qua-test-case.html) |

## 5. Bug

| Bug | Tiêu đề | Mức độ nghiêm trọng | Case thấy lỗi ở build này |
|---|---|---|---|
| [BUG-001](dang-nhap/bug/BUG-001.md) | [Đăng nhập] Thanh điều hướng vẫn hiện chữ DEFAULT sau mã và vai trò | Rất nhỏ | [SM-02](dang-nhap/test-case.md#tc-001) (Smoke test); [RG-02](dang-nhap/test-case.md#tc-001) (Regression Tầng 1); [TC-001](dang-nhap/test-case.md#tc-001) (Test case Đăng nhập) |
| [BUG-002](dang-nhap/bug/BUG-002.md) | [Đăng nhập] Câu báo sai mã nhân viên hoặc mật khẩu còn cụm Mã không gian (bản English còn chữ Workspace) | Rất nhỏ | [RG-04](dang-nhap/test-case.md#tc-004) (Regression Tầng 1); [TC-004](dang-nhap/test-case.md#tc-004) (Test case Đăng nhập); [TC-006](dang-nhap/test-case.md#tc-006) (Test case Đăng nhập); [TC-007](dang-nhap/test-case.md#tc-007) (Test case Đăng nhập); [TC-008](dang-nhap/test-case.md#tc-008) (Test case Đăng nhập); [TC-011](dang-nhap/test-case.md#tc-011) (Test case Đăng nhập); [TC-012](dang-nhap/test-case.md#tc-012) (Test case Đăng nhập); [TC-013](dang-nhap/test-case.md#tc-013) (Test case Đăng nhập); [TC-030](dang-nhap/test-case.md#tc-030) (Test case Đăng nhập); [TC-035](dang-nhap/test-case.md#tc-035) (Test case Đăng nhập); [TC-036](dang-nhap/test-case.md#tc-036) (Test case Đăng nhập) |
| [BUG-004](dang-nhap/bug/BUG-004.md) | [Đăng nhập] Để trống ô Mật khẩu hiện Một số giá trị không hợp lệ. và dòng mã kỹ thuật validation.too_small (password) | Rất nhỏ | [TC-009](dang-nhap/test-case.md#tc-009) (Test case Đăng nhập) |
| [BUG-005](dang-nhap/bug/BUG-005.md) | [Đăng nhập] Để trống cả hai ô hiện Một số giá trị không hợp lệ. và dòng mã kỹ thuật validation.too_small (password) | Rất nhỏ | [TC-010](dang-nhap/test-case.md#tc-010) (Test case Đăng nhập) |
| [BUG-006](dang-nhap/bug/BUG-006.md) | [Đăng nhập] Nhập mã nhân viên 210 ký tự hiện Một số giá trị không hợp lệ. và dòng mã kỹ thuật validation.too_big (employeeId) | Rất nhỏ | [TC-040](dang-nhap/test-case.md#tc-040) (Test case Đăng nhập) |
| [BUG-007](dang-nhap/bug/BUG-007.md) | [Đăng nhập] Ô Mật khẩu vẫn giữ nguyên chữ đã gõ sau khi báo sai | Nhỏ | [TC-011](dang-nhap/test-case.md#tc-011) (Test case Đăng nhập) |
| [BUG-008](dang-nhap/bug/BUG-008.md) | [Đăng nhập] Tài khoản bị chặn sau 5 lần sai kể từ lần đăng nhập đúng gần nhất, đăng nhập đúng không đưa số lần sai về 0 | Nặng | — |

File bug chưa có trường trạng thái (mở hoặc đã đóng); đóng bug theo kế hoạch re-test do người dùng chốt.

## 6. Độ phủ requirement

| Tính năng | Mã requirement | Mã chưa có test case | Trạng thái test case | Truy vết |
|---|---|---|---|---|
| Đăng nhập | 40 trong SRS, 14 câu trả lời (TL). Test case: 43 | không có | Còn đúng 43 | [mở](dang-nhap/truy-vet.html) |
| Khuyến nghị LTV/DSR | 61 trong SRS, 2 câu trả lời (TL). Test case: 38 | [M09](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L154), [M10](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L155), [R12](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L141), [S03-AC11](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L93), [S04-AC01](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L102), [S04-AC04](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L105), [S05-AC02](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L115) | Còn đúng 38 | [mở](khuyen-nghi-ltv-dsr/truy-vet.html) |

## 7. Rủi ro còn lại

**Chưa có kết quả và vì sao**

| Bộ test | Case | Trạng thái | Lý do |
|---|---|---|---|
| Smoke test | [SM-06](khuyen-nghi-ltv-dsr/test-case.md#tc-022) | Không kết luận | Điều kiện trước chưa đúng: ca cần hồ sơ nháp chưa nhập thu nhập (khung Thẩm định còn thông báo Nhập đủ thông tin…) nhưng hồ sơ nháp dành riêng cho ca này đã dùng hết ở lần chạy trước. Cần tạo hồ sơ nháp mới trên staging (tạo dữ liệu thật nên cần người dùng đồng ý) rồi chạy lại. |
| Regression Tầng 1 | [RG-13](khuyen-nghi-ltv-dsr/test-case.md#tc-022) | Không kết luận | Điều kiện trước không đúng: hồ sơ nháp mới tạo đã có Khuyến nghị đầu trang là Từ chối, trong khi test case yêu cầu dấu —; chưa kiểm được việc đầu trang đổi sau khi bấm Lưu theo đúng trạng thái đầu. |
| Test case Đăng nhập | [TC-014](dang-nhap/test-case.md#tc-014), [TC-021](dang-nhap/test-case.md#tc-021) | Bị chặn | Cần bộ đếm số lần sai của hệ thống đếm đúng như BA quy định. Lần chạy [TC-014](dang-nhap/test-case.md#tc-014) cho thấy tài khoản P100001 bị chặn sau 5 lần sai kể từ lần đăng nhập đúng gần nhất ([BUG-008](dang-nhap/bug/BUG-008.md)). Chạy tiếp lúc này có thể chặn tài khoản thêm 5 phút mỗi lần và kết quả không đáng tin. |
| Test case Đăng nhập | [TC-015](dang-nhap/test-case.md#tc-015), [TC-016](dang-nhap/test-case.md#tc-016), [TC-017](dang-nhap/test-case.md#tc-017), [TC-018](dang-nhap/test-case.md#tc-018), [TC-019](dang-nhap/test-case.md#tc-019), [TC-020](dang-nhap/test-case.md#tc-020), [TC-022](dang-nhap/test-case.md#tc-022), [TC-037](dang-nhap/test-case.md#tc-037) | Bỏ qua | Chính các bước của những ca này làm hệ thống chặn đăng nhập (lần sai thứ 10, nhập khi đang bị chặn, chờ hết chặn, bản English bị chặn, chặn theo từng tài khoản). Không chạy tự động để tránh chặn tài khoản test; người kiểm thử tự làm bằng tay khi cần. |
| Test case Đăng nhập | [TC-042](dang-nhap/test-case.md#tc-042), [TC-043](dang-nhap/test-case.md#tc-043) | Bỏ qua | Code chưa làm phần thời hạn phiên 10 phút (người dùng xác nhận ngày 2026-11-19), nên chưa kiểm được ý phiên hết hạn sau 10 phút. Đã chạy thử bằng script: sau 543 giây tải lại trang vẫn đăng nhập ([TC-042](dang-nhap/test-case.md#tc-042)); sau khoảng 633 giây vẫn đăng nhập ([TC-043](dang-nhap/test-case.md#tc-043)), nhưng các lần chạy thử này chạy song song cùng tài khoản nên chưa tính là kết luận. Chạy lại khi code làm xong phần này (mỗi ca khoảng 11 phút). |

- **Cập nhật khuyến nghị ở đầu trang sau khi lưu chưa được kiểm ở lượt này** (Smoke test). [SM-06](khuyen-nghi-ltv-dsr/test-case.md#tc-022) chưa có kết quả nên chưa biết ô Khuyến nghị đầu trang hồ sơ có đổi sang Phê duyệt sau vài giây khi nhập lương 100 triệu rồi bấm Lưu ở bản 1.3.0. Lượt 1 cùng bản 1.3.0 ca này Đạt, nhưng lượt 2 chưa xác nhận lại.
- **Chữ DEFAULT còn trên thanh điều hướng ([BUG-001](dang-nhap/bug/BUG-001.md))** (Smoke test). Cả ba tài khoản test (P100001, P200001, P300001) vẫn thấy mã và vai trò kèm chữ DEFAULT mà BA đã chốt bỏ; bug mức Rất nhỏ, không chặn thao tác nào và bộ smoke đã chốt cho nhận build ở trường hợp này.
- **Hồ sơ chưa nhập thu nhập đã bị hiện nhãn Từ chối** (Regression Tầng 1). Ở Khuyến nghị [TC-001](khuyen-nghi-ltv-dsr/test-case.md#tc-001) ([RG-08](khuyen-nghi-ltv-dsr/test-case.md#tc-001)) hồ sơ vay 3,2 tỷ chưa nhập thu nhập mà khung Thẩm định và đầu trang hồ sơ hiện Từ chối, thay vì không có nhãn và báo cần nhập đủ thông tin. Chuyên viên có thể thấy hồ sơ bị từ chối khi mới tạo xong. Đã quan sát trên staging bản 1.3.0, chưa biết đây là lỗi hay khác biệt so với lúc khảo sát; chưa tạo bug.
- **Câu báo sai mật khẩu vẫn còn cụm Mã không gian** (Regression Tầng 1). Ở Đăng nhập [TC-004](dang-nhap/test-case.md#tc-004) ([RG-04](dang-nhap/test-case.md#tc-004)) câu báo lỗi sau khi nhập sai một lần vẫn còn cụm Mã không gian dù BA đã chốt bỏ; người dùng sẽ thấy một khái niệm không còn trong hệ thống. Lỗi đã biết, ghi ở [BUG-002](dang-nhap/bug/BUG-002.md).
- **Người dùng thật có thể bị chặn đăng nhập sớm hơn quy định** (Test case Đăng nhập). BA quy định chỉ chặn sau 10 lần sai liên tiếp và đăng nhập đúng đưa số lần sai về 0. Thực tế P100001 bị chặn 5 phút khi mới sai 5 lần kể từ lần đăng nhập đúng gần nhất. Nếu người dùng thật đăng nhập sai rải rác trong ngày thì có thể bị chặn nhầm. Chưa biết hệ thống đếm theo tài khoản, theo máy hay toàn hệ thống ([BUG-008](dang-nhap/bug/BUG-008.md), đã có câu hỏi cho Dev).
- **Cơ chế chặn đăng nhập chưa được kiểm trọn vẹn** (Test case Đăng nhập). 10 ca về chặn đăng nhập chưa có kết quả. Chưa biết lần sai thứ 10 có bị chặn đúng lúc không, khi đang bị chặn mà nhập đúng thì có bị từ chối như BA yêu cầu không (ngày 2026-11-17 từng thấy hệ thống vẫn cho vào), và hết 5 phút có tự mở lại không.
- **Thời hạn phiên 10 phút chưa được làm trong code** (Test case Đăng nhập). Người dùng đăng nhập rồi để yên hơn 10 phút thì phiên vẫn còn, chưa tự hết hạn như BA quy định. Hiện chưa kiểm được thêm vì code chưa làm phần này; khi làm xong cần kiểm cả hai phía: phiên không hết sớm hơn 10 phút (tránh mất dữ liệu đang nhập) và hết đúng sau 10 phút.
- **Mật khẩu vẫn còn trong ô sau khi báo sai** (Test case Đăng nhập). Sau mỗi lần nhập sai, ô Mật khẩu vẫn giữ nguyên các chấm ([BUG-007](dang-nhap/bug/BUG-007.md)). Nếu nhiều người dùng chung một máy thì người sau thấy ô còn chữ của người trước. Chưa kiểm xem chữ này có đọc ra được không.
- **Độ tin cậy của kết quả** (Test case Đăng nhập). Mỗi ca chỉ chạy tự động một đến hai lần, trên trình duyệt Chrome, ở môi trường thử staging. Chưa chạy lặp để loại trừ lỗi chập chờn, chưa thử trình duyệt hoặc thiết bị khác. Sau khi Dev sửa bug, cần chạy lại các ca liên quan.

## 8. Đề xuất bước tiếp theo

- Smoke test: Tạo hồ sơ nháp mới trên staging (tạo dữ liệu thật nên cần người dùng đồng ý) rồi chạy lại [SM-06](khuyen-nghi-ltv-dsr/test-case.md#tc-022); nếu đạt thì bộ smoke đủ 7 case Đạt hoặc Đạt kèm lỗi đã biết. Nhận hay trả bản là quyết định của người kiểm thử hoặc PO.
- Regression Tầng 1: Đề xuất: hỏi Dev hồ sơ chưa nhập thu nhập có chủ ý hiện Từ chối hay không, rồi tạo bug hoặc cập nhật requirement; sau đó chạy lại [RG-13](khuyen-nghi-ltv-dsr/test-case.md#tc-022) với hồ sơ có đúng trạng thái đầu. Quyết định nhận hay trả build là của người kiểm thử hoặc PO.
- Test case Đăng nhập: Thứ tự nên làm: (1) Dev trả lời 4 câu về cách đếm lần sai ở [BUG-008](dang-nhap/bug/BUG-008.md) và sửa; (2) đặt lại bộ đếm rồi chạy [TC-014](dang-nhap/test-case.md#tc-014) và [TC-021](dang-nhap/test-case.md#tc-021); (3) người kiểm thử tự làm 8 ca bị bỏ qua; (4) khi code làm xong thời hạn phiên và BA trả lời câu B15, chạy lại [TC-042](dang-nhap/test-case.md#tc-042), [TC-043](dang-nhap/test-case.md#tc-043) (script đã có); (5) chạy lại cả bộ sau khi Dev sửa 7 bug. Về nhận hay trả bản 1.3.0 cho tính năng này: đây là quyết định của người kiểm thử và PO; căn cứ chính là không có lỗi nào chặn việc đăng nhập bình thường, nhưng có 1 bug mức Nặng và 12 case chưa có kết quả.

## 9. Duyệt build

Người duyệt điền trên trang HTML (mục 9), tải file `duyet-build.json`, đặt vào `testing/banking-lite/` rồi chạy lại `python -X utf8 scripts/build_docs.py`.

| Mục | Nội dung |
|---|---|
| Người duyệt | (chưa điền) |
| Chức danh | (chưa điền) |
| Quyết định | (chưa điền) |
| Điều kiện kèm theo | (chưa điền) |
| Ghi chú | (chưa điền) |
| Ngày duyệt | (chưa điền) |

## Phụ lục: trang kết quả từng lượt

- [Smoke test](smoke-ket-qua.html)
- [Regression Tầng 1](regression-tang-1-ket-qua.html)
- [Test case Đăng nhập](dang-nhap/ket-qua-test-case.html)
