# Kết quả chạy regression tầng 1 — banking-lite

> File tự sinh từ `testing/banking-lite/run-results/regression-tang-1.json` bằng `scripts/build_report.py` — đừng sửa tay, chạy lại là ghi đè. Bản dễ xem: `regression-tang-1-ket-qua.html`.

| | |
|---|---|
| Build | **1.3.0** |
| Lượt | 1 / 1 (lượt mới nhất) |
| Thời điểm | 2026-11-19 15:36:51 |
| Người chạy | Sunny Tran |
| Cách chạy | Tự động (Playwright) |
| Kết luận | **Có case không đạt** |
| Ghi chú | Chạy tự động bằng Playwright trên môi trường thử staging (https://staging-banking-lite.vercel.app/), bản 1.3.0, ngày 2026-11-19, theo bảng Tầng 1 của regression-test.md. 12 trong 13 case có kết luận; case RG-13 không kết luận vì điều kiện trước không đúng. Case RG-08 chạy hai lần (cùng kết quả), RG-12 chạy lại một lần sau khi sửa điều kiện trước của script. |

## Kết luận và rủi ro

Chưa nên coi Tầng 1 đạt: 10 trên 13 case đạt (có 1 case đạt kèm lỗi đã biết), 2 case không đạt và 1 case chưa kết luận được; một trong hai case không đạt là phát hiện mới của Khuyến nghị.

Số liệu lượt này: 12 trên 13 case đã có kết quả (92%): 9 Đạt, 1 Đạt kèm ý phụ sai, 2 Không đạt, 1 Không kết luận.

**Đã kiểm và đạt**

- Đăng nhập: mở hệ thống thấy form đủ ô nhập, nút và chân trang bản 1.3.0 (RG-01).
- Đăng nhập: P100001 vào đúng Danh sách việc; chỉ sai ý phụ là còn chữ DEFAULT trên thanh điều hướng, lỗi đã biết BUG-001 (RG-02).
- Đăng nhập: P200001 và P300001 vào đúng Danh sách việc và đúng vai trò (RG-03).
- Đăng nhập: mở link hồ sơ khi chưa đăng nhập, đăng nhập xong vào đúng hồ sơ (RG-05).
- Đăng nhập: đăng xuất về form đăng nhập, giữ nguyên ngôn ngữ đã chọn (RG-06).
- Đăng nhập: chưa đăng nhập thì mọi địa chỉ khác đều ra form đăng nhập (RG-07).
- Khuyến nghị: Phê duyệt, Chuyển cấp trên, Từ chối vì thặng dư thiếu 1 đồng, và Từ chối kèm lý do khi LTV 81% đều ra đúng nhãn, chỉ số và lý do (RG-09 đến RG-12).

**Chưa có kết quả và vì sao**

| Case | Trạng thái | Lý do |
|---|---|---|
| RG-13 | Không kết luận | Điều kiện trước không đúng: hồ sơ nháp mới tạo đã có Khuyến nghị đầu trang là Từ chối, trong khi test case yêu cầu dấu —; chưa kiểm được việc đầu trang đổi sau khi bấm Lưu theo đúng trạng thái đầu. |

**Rủi ro để người kiểm thử đánh giá**

- **Hồ sơ chưa nhập thu nhập đã bị hiện nhãn Từ chối.** Ở Khuyến nghị TC-001 (RG-08) hồ sơ vay 3,2 tỷ chưa nhập thu nhập mà khung Thẩm định và đầu trang hồ sơ hiện Từ chối, thay vì không có nhãn và báo cần nhập đủ thông tin. Chuyên viên có thể thấy hồ sơ bị từ chối khi mới tạo xong. Đã quan sát trên staging bản 1.3.0, chưa biết đây là lỗi hay khác biệt so với lúc khảo sát; chưa tạo bug.
- **Câu báo sai mật khẩu vẫn còn cụm Mã không gian.** Ở Đăng nhập TC-004 (RG-04) câu báo lỗi sau khi nhập sai một lần vẫn còn cụm Mã không gian dù BA đã chốt bỏ; người dùng sẽ thấy một khái niệm không còn trong hệ thống. Lỗi đã biết, ghi ở BUG-002.

**Đề xuất (người kiểm thử hoặc PO quyết định)**

Đề xuất: hỏi Dev hồ sơ chưa nhập thu nhập có chủ ý hiện Từ chối hay không, rồi tạo bug hoặc cập nhật requirement; sau đó chạy lại RG-13 với hồ sơ có đúng trạng thái đầu. Quyết định nhận hay trả build là của người kiểm thử hoặc PO.

## Kết quả lượt mới nhất

| ID | Regression case | Các bước | Kết quả mong đợi | Status | Evidence | Bug | Số lần chạy |
|---|---|---|---|---|---|---|---|
| RG-01 | [Đăng nhập · TC-005] Mở hệ thống khi chưa đăng nhập: form có ô Mã nhân viên (kèm gợi ý "Chữ P và 6 chữ số, ví dụ P100001."), ô Mật khẩu (chữ gõ hiện dạng chấm), nút Đăng nhập, chân trang phiên bản (Đăng nhập: vào hệ thống) | 1. Mở https://staging-banking-lite.vercel.app/.<br>2. Nhìn tên hai ô nhập.<br>3. Nhìn dòng chữ gợi ý bên dưới ô Mã nhân viên.<br>4. Nhìn nút bên dưới hai ô.<br>5. Nhìn chân trang.<br>6. Bấm vào ô Mật khẩu *, gõ abc123 (chưa bấm nút).<br>7. Nhìn chữ vừa gõ trong ô Mật khẩu. | Bước 2: có ô Mã nhân viên * và ô Mật khẩu *.<br>Bước 3: dòng gợi ý Chữ P và 6 chữ số, ví dụ P100001.<br>Bước 4: nút Đăng nhập.<br>Bước 5: chân trang ghi Banking Lite · Phiên bản 1.3.0.<br>Bước 7: chữ gõ trong ô Mật khẩu hiện dạng chấm, không hiện chữ rõ. | Đạt | [dang-nhap-tc-005-form-dang-nhap-20261119-153412.png](../../evidence/banking-lite/chay-test/dang-nhap-tc-005-form-dang-nhap-20261119-153412.png) | — | 1 |
| RG-02 | [Đăng nhập · TC-001] Đăng nhập đúng `P100001` + mật khẩu đúng: vào Danh sách việc của tài khoản đó, không có thông báo "đăng nhập thành công"; thanh trên hiện mã và vai trò, không còn chữ `DEFAULT` (Đăng nhập: vào hệ thống) | 1. Mở https://staging-banking-lite.vercel.app/.<br>2. Ở ô Mã nhân viên * nhập P100001.<br>3. Ở ô Mật khẩu * nhập mật khẩu đúng của P100001.<br>4. Bấm nút Đăng nhập.<br>5. Nhìn trang hiện ra và thanh trên cùng. | Bước 4: vào trang Danh sách việc của P100001; không hiện thông báo "đăng nhập thành công".<br>Bước 5: thanh trên cùng hiện P100001 và vai trò Chuyên viên khách hàng; không có chữ DEFAULT. | Đạt kèm ý phụ sai | [dang-nhap-tc-001-danh-sach-viec-20261119-153417.png](../../evidence/banking-lite/chay-test/dang-nhap-tc-001-danh-sach-viec-20261119-153417.png)<br>🔴 [dang-nhap-tc-001-loi-20261119-153417.png](../../evidence/banking-lite/chay-test/dang-nhap-tc-001-loi-20261119-153417.png) (tô đỏ chỗ lỗi): Lỗi ở bước 5 (nhìn thanh điều hướng sau khi đăng nhập): thanh điều hướng hiện chữ DEFAULT sau mã và vai trò, đáng ra không có chữ này.<br>🎬 [dang-nhap-tc-001-p100001-20261119-153417.webm](../../evidence/banking-lite/chay-test/video/dang-nhap-tc-001-p100001-20261119-153417.webm) (video quay lại ca) | [BUG-001](dang-nhap/bug/BUG-001.md) | 1 |
| RG-03 | [Đăng nhập · TC-002] Đăng nhập đúng bằng tài khoản vai trò khác (`P200001` Chuyên viên định giá, `P300001` Chuyên viên thẩm định tín dụng): vào đúng Danh sách việc và đúng vai trò của từng người (Đăng nhập: vào hệ thống) | 1. Mở https://staging-banking-lite.vercel.app/.<br>2. Ở ô Mã nhân viên * nhập P200001.<br>3. Ở ô Mật khẩu * nhập mật khẩu đúng của P200001.<br>4. Bấm nút Đăng nhập.<br>5. Nhìn trang hiện ra và thanh trên cùng.<br>6. Bấm Đăng xuất.<br>7. Ở ô Mã nhân viên * nhập P300001.<br>8. Ở ô Mật khẩu * nhập mật khẩu đúng của P300001.<br>9. Bấm nút Đăng nhập.<br>10. Nhìn trang hiện ra và thanh trên cùng. | Bước 4: vào Danh sách việc của P200001.<br>Bước 5: thanh trên cùng hiện P200001 và vai trò Chuyên viên định giá.<br>Bước 6: về form Đăng nhập.<br>Bước 9: vào Danh sách việc của P300001.<br>Bước 10: thanh trên cùng hiện P300001 và vai trò Chuyên viên thẩm định tín dụng. | Đạt | [dang-nhap-tc-002-p200001-danh-sach-viec-20261119-153420.png](../../evidence/banking-lite/chay-test/dang-nhap-tc-002-p200001-danh-sach-viec-20261119-153420.png)<br>[dang-nhap-tc-002-p300001-danh-sach-viec-20261119-153425.png](../../evidence/banking-lite/chay-test/dang-nhap-tc-002-p300001-danh-sach-viec-20261119-153425.png) | — | 1 |
| RG-04 | [Đăng nhập · TC-004] Nhập sai một lần (thấy khung lỗi), rồi sửa lại cho đúng và đăng nhập: vào được Danh sách việc (Đăng nhập: vào hệ thống) | 1. Mở https://staging-banking-lite.vercel.app/.<br>2. Ở ô Mã nhân viên * nhập P100001.<br>3. Ở ô Mật khẩu * nhập mật khẩu sai Sai@Matkhau1.<br>4. Bấm nút Đăng nhập.<br>5. Nhìn khung lỗi.<br>6. Chọn hết ô Mật khẩu (Ctrl+A), nhập mật khẩu đúng của P100001.<br>7. Kiểm ô Mã nhân viên còn P100001 (nếu trống thì nhập lại P100001).<br>8. Bấm nút Đăng nhập.<br>9. Nhìn trang hiện ra. | Bước 4: không đăng nhập; khung lỗi đỏ ghi "Mã nhân viên hoặc mật khẩu không đúng."<br>Bước 8: vào trang Danh sách việc của P100001. | Không đạt | [dang-nhap-tc-004-sau-nhap-sai-20261119-153437.png](../../evidence/banking-lite/chay-test/dang-nhap-tc-004-sau-nhap-sai-20261119-153437.png)<br>[dang-nhap-tc-004-sau-dang-nhap-20261119-153441.png](../../evidence/banking-lite/chay-test/dang-nhap-tc-004-sau-dang-nhap-20261119-153441.png)<br>[dang-nhap-tc-004-kiem-20261119-153441.png](../../evidence/banking-lite/chay-test/dang-nhap-tc-004-kiem-20261119-153441.png)<br>🎬 [dang-nhap-tc-004-20261119-153441.webm](../../evidence/banking-lite/chay-test/video/dang-nhap-tc-004-20261119-153441.webm) (video quay lại ca) | [BUG-002](dang-nhap/bug/BUG-002.md) | 1 |
| RG-05 | [Đăng nhập · TC-003] Chưa đăng nhập mà mở link một hồ sơ (ví dụ HL-000019 của chính người đó): hiện form đăng nhập, địa chỉ giữ nguyên; đăng nhập đúng thì mở thẳng hồ sơ đó, không về Danh sách việc (Đăng nhập: về đúng hồ sơ) | 1. Mở link hồ sơ https://staging-banking-lite.vercel.app/applications/db5f18e6-7a49-4d61-b307-0a485c8ab20d.<br>2. Nhìn trang và thanh địa chỉ.<br>3. Ở ô Mã nhân viên * nhập P100001.<br>4. Ở ô Mật khẩu * nhập mật khẩu đúng của P100001.<br>5. Bấm nút Đăng nhập.<br>6. Nhìn trang hiện ra. | Bước 2: hiện form Đăng nhập; thanh địa chỉ vẫn là link hồ sơ vừa mở.<br>Bước 6: mở thẳng hồ sơ HL-000019, không phải trang Danh sách việc. | Đạt | [dang-nhap-tc-003-link-ho-so-chua-dang-nhap-20261119-153427.png](../../evidence/banking-lite/chay-test/dang-nhap-tc-003-link-ho-so-chua-dang-nhap-20261119-153427.png)<br>[dang-nhap-tc-003-sau-dang-nhap-20261119-153430.png](../../evidence/banking-lite/chay-test/dang-nhap-tc-003-sau-dang-nhap-20261119-153430.png)<br>[dang-nhap-tc-003-kiem-20261119-153430.png](../../evidence/banking-lite/chay-test/dang-nhap-tc-003-kiem-20261119-153430.png) | — | 1 |
| RG-06 | [Đăng nhập · TC-023] Đăng xuất khi đang đăng nhập: về form đăng nhập, địa chỉ là `/`, ngôn ngữ đã chọn giữ nguyên (Đăng nhập: ra khỏi hệ thống) | 1. Bấm English.<br>2. Bấm Sign out.<br>3. Nhìn trang hiện ra và thanh địa chỉ. | Bước 2: về form đăng nhập.<br>Bước 3: form hiện bằng English (nhãn Employee ID *, Password *, nút Sign in); thanh địa chỉ là / (địa chỉ gốc); ngôn ngữ vẫn là English. | Đạt | [dang-nhap-tc-023-sau-dang-xuat-20261119-153534.png](../../evidence/banking-lite/chay-test/dang-nhap-tc-023-sau-dang-xuat-20261119-153534.png) | — | 1 |
| RG-07 | [Đăng nhập · TC-026] Chưa đăng nhập, mở `/integrations` hoặc một địa chỉ không có thật: hiện form đăng nhập, địa chỉ giữ nguyên, không có thông báo "cần đăng nhập", không có trang "không tìm thấy" (Đăng nhập: ra khỏi hệ thống) | 1. Mở https://staging-banking-lite.vercel.app/integrations.<br>2. Nhìn trang và thanh địa chỉ. | Bước 2: hiện form Đăng nhập; thanh địa chỉ giữ nguyên /integrations; không có thông báo "cần đăng nhập"; không có trang "không tìm thấy". | Đạt | [dang-nhap-tc-026-integrations-20261119-153442.png](../../evidence/banking-lite/chay-test/dang-nhap-tc-026-integrations-20261119-153442.png) | — | 1 |
| RG-08 | [Khuyến nghị LTV/DSR · TC-001] Không hiển thị khuyến nghị mà báo cần nhập đủ thông tin khi chưa nhập thu nhập (Khuyến nghị: kết quả chính) | 1. Mở https://staging-banking-lite.vercel.app/ và đăng nhập P100001.<br>2. Mở hồ sơ nháp ở điều kiện trước.<br>3. Mở bước Tài chính, không nhập gì.<br>4. Nhìn khung Thẩm định: nhãn khuyến nghị, mục Lý do, thông báo và các chỉ số. | Bước 4: khung Thẩm định không có nhãn khuyến nghị và không có mục Lý do.<br>Bước 4: có thông báo xanh Nhập đủ thông tin người vay, khoản vay, tài sản và thu nhập để xem khuyến nghị.<br>Bước 4: các chỉ số vẫn hiện: LTV 80,00% (LTV tối đa 80,00%); khoản trả mới 40.800.000 VND; thu nhập được tính 0 VND; chi phí được tính 4.500.000 VND; DSR —; thặng dư -45.300.000 VND. | Không đạt | [khuyen-nghi-ltv-dsr-tc-001-khung-tham-dinh-20261119-153603.png](../../evidence/banking-lite/chay-test/khuyen-nghi-ltv-dsr-tc-001-khung-tham-dinh-20261119-153603.png) | — | 1 |
| RG-09 | [Khuyến nghị LTV/DSR · TC-002] Hiển thị khuyến nghị Phê duyệt khi nhập lương 100 triệu và đạt mọi quy tắc (Khuyến nghị: kết quả chính) | 1. Mở https://staging-banking-lite.vercel.app/ và đăng nhập P100001.<br>2. Mở hồ sơ nháp ở điều kiện trước.<br>3. Mở bước Tài chính.<br>4. Ở ô Lương hằng tháng nhập 100000000, không bấm Lưu.<br>5. Nhìn khung Thẩm định. | Bước 5: khung Thẩm định đổi ngay khi nhập, không cần bấm Lưu.<br>Bước 5: nhãn Phê duyệt; dòng nhỏ Xem trước: thẩm định chính thức chạy khi gửi, có dữ liệu CIC.<br>Bước 5: khoản trả mới 40.800.000 VND; thu nhập được tính 100.000.000 VND; chi phí được tính 4.500.000 VND; DSR 40,80%; thặng dư 54.700.000 VND.<br>Bước 5: mục Lý do ghi Đáp ứng mọi quy tắc tín dụng. | Đạt | [khuyen-nghi-ltv-dsr-tc-002-khung-tham-dinh-20261119-153511.png](../../evidence/banking-lite/chay-test/khuyen-nghi-ltv-dsr-tc-002-khung-tham-dinh-20261119-153511.png) | — | 1 |
| RG-10 | [Khuyến nghị LTV/DSR · TC-023] Hiển thị Chuyển cấp trên khi DSR 54,40% (nằm giữa 50% và 70%) (Khuyến nghị: kết quả chính) | 1. Mở https://staging-banking-lite.vercel.app/ và đăng nhập P100001.<br>2. Mở hồ sơ nháp ở điều kiện trước.<br>3. Mở bước Tài chính.<br>4. Ở ô Lương hằng tháng nhập 75000000, không bấm Lưu.<br>5. Nhìn khung Thẩm định: nhãn, DSR, thặng dư và mục Lý do. | Bước 5: DSR 54,40%.<br>Bước 5: nhãn Chuyển cấp trên. | Đạt | [khuyen-nghi-ltv-dsr-tc-023-khung-tham-dinh-20261119-153522.png](../../evidence/banking-lite/chay-test/khuyen-nghi-ltv-dsr-tc-023-khung-tham-dinh-20261119-153522.png) | — | 1 |
| RG-11 | [Khuyến nghị LTV/DSR · TC-009] Hiển thị Từ chối kèm lý do khi thặng dư thiếu 1 đồng so với mức tối thiểu (2.999.999) (Khuyến nghị: kết quả chính) | 1. Mở https://staging-banking-lite.vercel.app/ và đăng nhập P100001.<br>2. Mở hồ sơ nháp ở điều kiện trước.<br>3. Mở bước Tài chính.<br>4. Ở ô Lương hằng tháng nhập 100000000.<br>5. Ở ô Chi phí sinh hoạt hằng tháng nhập 56200001.<br>6. Nhìn khung Thẩm định. | Bước 6: thặng dư 2.999.999 VND.<br>Bước 6: nhãn Từ chối; lý do Từ chối: Thặng dư hằng tháng 2.999.999 VND thấp hơn 3.000.000 VND. | Đạt | [khuyen-nghi-ltv-dsr-tc-009-khung-tham-dinh-20261119-153517.png](../../evidence/banking-lite/chay-test/khuyen-nghi-ltv-dsr-tc-009-khung-tham-dinh-20261119-153517.png) | — | 1 |
| RG-12 | [Khuyến nghị LTV/DSR · TC-014] Hiển thị Từ chối kèm lý do LTV vượt mức khi LTV là 81% (Khuyến nghị: kết quả chính) | 1. Mở https://staging-banking-lite.vercel.app/ và đăng nhập P100001.<br>2. Mở hồ sơ nháp ở điều kiện trước.<br>3. Mở bước Tài chính.<br>4. Ở bước Tài chính, ô Lương hằng tháng nhập 100000000.<br>5. Bấm Lưu, chờ khoảng 8 giây cho tới khi đầu trang cập nhật.<br>6. Mở bước Khoản vay và tài sản, đổi số tiền vay thành 3240000000, bấm Lưu, chờ khoảng 8 giây cho tới khi đầu trang cập nhật.<br>7. Mở bước Tài chính.<br>8. Nhìn khung Thẩm định và đầu trang hồ sơ (LTV, Khuyến nghị). | Bước 8: đầu trang LTV 81,00%; Khuyến nghị Từ chối.<br>Bước 8: khung Thẩm định ghi 81,00% (LTV tối đa 80,00%); lý do Từ chối: LTV 81% vượt mức tối đa 80%. | Đạt | [khuyen-nghi-ltv-dsr-tc-014-sau-khi-luu-20261119-153650.png](../../evidence/banking-lite/chay-test/khuyen-nghi-ltv-dsr-tc-014-sau-khi-luu-20261119-153650.png)<br>[khuyen-nghi-ltv-dsr-tc-014-kiem-20261119-153650.png](../../evidence/banking-lite/chay-test/khuyen-nghi-ltv-dsr-tc-014-kiem-20261119-153650.png) | — | 1 |
| RG-13 | [Khuyến nghị LTV/DSR · TC-022] Cập nhật khuyến nghị ở đầu trang hồ sơ sau vài giây khi nhập lương rồi bấm Lưu (Khuyến nghị: đầu trang hồ sơ) | 1. Mở https://staging-banking-lite.vercel.app/ và đăng nhập P100001.<br>2. Mở hồ sơ nháp ở điều kiện trước.<br>3. Mở bước Tài chính.<br>4. Nhập Lương hằng tháng 100000000, Khoản trả nợ hiện có hằng tháng 5000000, Số người phụ thuộc 5.<br>5. Bấm Lưu.<br>6. Nhìn đầu trang hồ sơ ngay sau khi lưu, rồi chờ khoảng 8 giây và nhìn lại ô Khuyến nghị.<br>7. Nhìn trạng thái của bước Tài chính.<br>8. Tải lại trang, mở lại bước Tài chính và nhìn ô Lương hằng tháng. | Bước 5: hiện thông báo Đã lưu.<br>Bước 6: phản hồi chậm vài giây (lần quan sát: 4 giây sau khi lưu vẫn —); sau đó ô Khuyến nghị đầu trang thành Phê duyệt.<br>Bước 7: bước Tài chính ghi Đã xong.<br>Bước 8: ô Lương hằng tháng giữ giá trị 100000000. | Không kết luận | — | — | 0 |

## Lịch sử các lượt

| Lượt | Build | Thời điểm | Người chạy | Kết quả | Kết luận |
|---|---|---|---|---|---|
| 1 | 1.3.0 | 2026-11-19 15:36:51 | Sunny Tran | 9 Đạt, 1 Đạt kèm ý phụ sai, 2 Không đạt, 1 Không kết luận | Có case không đạt |

## Từng case qua các lượt (tối đa 8 lượt gần nhất)

| ID | Lượt 1 (1.3.0) |
|---|---|
| RG-01 | Đạt |
| RG-02 | Đạt kèm ý phụ sai |
| RG-03 | Đạt |
| RG-04 | Không đạt |
| RG-05 | Đạt |
| RG-06 | Đạt |
| RG-07 | Đạt |
| RG-08 | Không đạt |
| RG-09 | Đạt |
| RG-10 | Đạt |
| RG-11 | Đạt |
| RG-12 | Đạt |
| RG-13 | Không kết luận |

Các bước và Kết quả mong đợi lấy từ test case gốc. Bị chặn: chưa test được vì bug khác (xem cột Bug). Số lần chạy: số lượt có kết luận Đạt, Đạt kèm lỗi đã biết, Đạt kèm ý phụ sai hoặc Không đạt; lượt Không kết luận và Chưa chạy không tính.
