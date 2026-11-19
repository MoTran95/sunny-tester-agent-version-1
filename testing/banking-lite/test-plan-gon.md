# Kế hoạch kiểm thử (Test plan) — Banking Lite, bản build 1.3.0

| | |
|---|---|
| Hệ thống | Banking Lite — Vay mua nhà, https://staging-banking-lite.vercel.app/ |
| Bản build | 1.3.0 (số hiển thị ở chân trang và ở `/api/health`) |
| Mã kế hoạch | …………… |
| Ngày lập | 2026-11-19 |
| Cập nhật lần cuối | 2026-11-19 |
| Người lập | Sunny Tran |
| Người yêu cầu | …………… |
| Người duyệt kế hoạch | …………… |

*Bản gọn của kế hoạch đầy đủ ([bản đầy đủ](test-plan.md)); các mục giữ số của bản đầy đủ để dễ đối chiếu.*

## 1. Mục tiêu và bối cảnh
- **Mục tiêu:** đánh giá bản 1.3.0 trên môi trường staging có đủ điều kiện để nhận hay không, và ghi lại các rủi ro còn lại.
- **Câu hỏi cần trả lời:** Đăng nhập và Khuyến nghị LTV/DSR có hoạt động đúng theo requirement không, có lỗi nào chặn việc nhận bản này không.
- **Kết quả bàn giao:** báo cáo tổng kết kiểm thử (`testing/banking-lite/test-summary-report.md`) kèm quyết định nhận / không nhận / nhận có điều kiện của người duyệt build.
- **Hệ thống làm gì:** xử lý hồ sơ vay mua nhà (mã `HL-xxxxxx`) qua 8 bước: Người vay → Khoản vay & tài sản → Tài chính → Định giá → Lãi suất → Kiểm tra & gửi → Quyết định tín dụng → Lịch sử. Ba vai trò sử dụng: Chuyên viên khách hàng, Chuyên viên định giá, Chuyên viên thẩm định tín dụng.
- **Tài liệu đầu vào:**

| Tài liệu | Tình trạng |
|---|---|
| [Requirement Đăng nhập](../../srs/banking-lite/dang-nhap.md), [bảng soát](dang-nhap/bang-soat-requirement.md), [câu hỏi cho BA](dang-nhap/cau-hoi-cho-ba.md) | Đã có; BA đã trả lời 14 câu |
| [Requirement Khuyến nghị LTV/DSR](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md) | Đã có, là bản nháp, BA chưa xác nhận; mới có 2 câu trả lời |
| Release note của build 1.3.0 | Chưa có |
| Requirement cho Tạo hồ sơ, Định giá, Gửi thẩm định, Quyết định tín dụng, Tích hợp | Chưa có; chỉ có [ghi chép khám phá](../../evidence/banking-lite/bao-cao-kham-pha.md) |

## 2. Phạm vi

**2.1. Trong phạm vi**

| Tính năng | Vai trò (tài khoản) liên quan | Căn cứ | Test case |
|---|---|---|---|
| Đăng nhập | Cả ba vai trò: P100001, P200001, P300001 | [Requirement Đăng nhập](../../srs/banking-lite/dang-nhap.md) | 43 case: [test-case.md](dang-nhap/test-case.md) |
| Khuyến nghị LTV/DSR: hệ thống xem trước kết quả thẩm định (Phê duyệt / Chuyển cấp trên / Từ chối) khi nhập thu nhập và chi phí | Chuyên viên khách hàng (P100001) | [Requirement Khuyến nghị](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md) (bản nháp) | 38 case: [test-case.md](khuyen-nghi-ltv-dsr/test-case.md) |

**2.2. Ngoài phạm vi**

| Nội dung | Lý do không test | Rủi ro nếu bỏ qua |
|---|---|---|
| Tạo hồ sơ, Định giá, Lãi suất, Gửi thẩm định, Quyết định tín dụng, Lịch sử hồ sơ | Chưa có requirement và test case; mới khám phá | Hành trình then chốt của hệ thống không được kiểm; smoke Đạt không bảo đảm các bước này |
| Trang Tích hợp (VNeID, CIC, SMS, nhật ký gọi hệ thống ngoài) và tải báo cáo CSV | Chưa có test case; môi trường tích hợp chưa thiết lập | Lỗi gọi hệ thống ngoài hoặc tải báo cáo không bị phát hiện |
| Thẩm định chính thức lúc Gửi thẩm định | Chưa có test case; chỉ kiểm bước xem trước ở bước Tài chính | Kết quả xem trước và kết quả chính thức có thể lệch nhau mà không ai thấy |
| Bảo mật, hiệu năng, tải | Đợt này chỉ test chức năng | Không đánh giá được |
| Trình duyệt khác Chrome, thiết bị di động | Chỉ dùng Chrome | Lỗi riêng từng trình duyệt hoặc thiết bị không được phát hiện |
| Các mã requirement chưa có test case (7 mã, danh sách ở mục 10) | Chưa viết case (xem [truy vết](khuyen-nghi-ltv-dsr/truy-vet.md)) | Phần định giá, CIC và vài quy tắc của Khuyến nghị không được kiểm |

## 3. Cách kiểm thử

| Lớp test | Để làm gì | Chạy khi nào | Cách làm | Bộ case |
|---|---|---|---|---|
| Smoke | Build có đủ ổn để test sâu không | Ngay khi nhận build | Tự động (Playwright), có thể làm tay | [smoke-test.md](smoke-test.md): 7 case, khoảng 12,5 phút |
| Test từng tính năng | Từng tính năng đúng theo requirement | Sau khi smoke Đạt | Tự động phần lớn; ca có thể làm khóa tài khoản do người kiểm thử làm tay | 43 case: [test-case.md](dang-nhap/test-case.md) (Đăng nhập); 38 case: [test-case.md](khuyen-nghi-ltv-dsr/test-case.md) (Khuyến nghị) |
| Regression | Chỗ đã đúng còn đúng sau khi build đổi | Khi build có thay đổi | Tự động; vùng chặn đăng nhập làm tay | [regression-test.md](regression-test.md): Tầng 1 (13 case lõi), Tầng 2 (13 vùng, 68 case), Tầng 3 (toàn bộ 81 case). Người kiểm thử duyệt việc chọn tầng trước khi chạy |
| Re-test | Bug đã sửa có hết thật không | Khi Dev báo đã sửa | Làm theo kế hoạch re-test của từng bug | Kế hoạch lập khi có bug cần re-test |

**Thứ tự thực hiện:** smoke → test từng tính năng → regression → re-test. Smoke Không đạt thì dừng, trả build.

**Kỹ thuật thiết kế test case:** phân vùng tương đương, giá trị biên, bảng quyết định, chuyển trạng thái, use case, đoán lỗi (ghi ở cột Kỹ thuật của file test case).

## 5. Tiêu chí bắt đầu, kết thúc, tạm dừng

**5.1. Điều kiện để bắt đầu test**

| Điều kiện | Cách kiểm |
|---|---|
| Build 1.3.0 đã lên môi trường test | Số phiên bản ở chân trang và `/api/health` |
| Có release note của build | Xin từ Dev (hiện chưa có) |
| Tài khoản test đăng nhập được | Đăng nhập thử bằng cả ba tài khoản |
| Hồ sơ nháp cho các ca Khuyến nghị sẵn sàng | Tạo bằng script, khi người kiểm thử đồng ý |
| Phần thời hạn phiên 10 phút (TC-042, TC-043) | Hỏi Dev đã làm chưa trước khi chạy |

**5.2. Điều kiện để kết thúc test (đủ thì gửi báo cáo tổng kết)**

| Tiêu chí | Ngưỡng | Nguồn |
|---|---|---|
| Smoke | Đạt theo tiêu chí trả build trong [smoke-test.md](smoke-test.md) | Smoke test |
| Test case bắt buộc đã chạy | Do người kiểm thử quyết định theo nguồn lực và thời gian của đợt test; báo cáo tổng kết ghi rõ phần đã chạy, phần chưa chạy và lý do | Người kiểm thử |
| Tỉ lệ Đạt tối thiểu | …………… | …………… |
| Bug mức Nghiêm trọng còn mở | …………… | …………… |
| Bug mức Lớn còn mở | …………… | …………… |
| Regression | Số tầng chạy do người kiểm thử quyết định theo nguồn lực và thời gian; báo cáo tổng kết ghi rõ tầng đã chạy | Người kiểm thử |
| Re-test | Mọi bug đã sửa đều được re-test | Quy ước của dự án |
| Ca do người kiểm thử làm tay (TC-015…020, 022, 037 và TC-042, TC-043) | Chưa làm xong thì ghi vào phần rủi ro của báo cáo tổng kết | Mục 9 |

**5.3. Khi nào tạm dừng và khi nào chạy tiếp**

| Dừng khi | Chạy tiếp khi |
|---|---|
| Một case smoke Không đạt | Dev giao build mới và smoke Đạt |
| Tài khoản test bị chặn đăng nhập | Hết 5 phút hoặc đã xả bộ đếm |
| Staging không truy cập được hoặc báo lỗi hệ thống | Staging hoạt động lại, `/api/health` đúng số bản |
| Số phiên bản ở chân trang khác 1.3.0 | Xác nhận với Dev đây có phải build cần test |

## 9. Rủi ro, giả định, phụ thuộc

**9.1. Rủi ro và phụ thuộc**

| Loại | Nội dung | Ảnh hưởng | Cách giảm / ai quyết |
|---|---|---|---|
| Rủi ro | Requirement Khuyến nghị là bản nháp, BA chưa xác nhận | 38 case Khuyến nghị có thể phải sửa; case Không đạt cần kiểm lại case trước khi kết luận | Gửi BA xác nhận trước khi chạy |
| Rủi ro | Các ca nhập sai nhiều lần có thể kích hoạt chặn đăng nhập 5 phút | Tài khoản test bị chặn, các ca sau không chạy được | Xả bộ đếm bằng đăng nhập đúng xen kẽ; làm tay ca chặn đăng nhập |
| Rủi ro | Thời hạn phiên 10 phút (TC-042, TC-043): mỗi ca phải chờ khoảng 11 phút và chưa xác nhận với Dev phần này đã triển khai | Mất thời gian chờ mà ca có thể không chạy được nếu phần này chưa có | Hỏi Dev trước khi chạy |
| Rủi ro | Staging dùng chung dữ liệu; hồ sơ nháp có thể bị dùng hết hoặc bị người khác đổi | Ca Khuyến nghị cho kết quả sai do điều kiện trước | Tạo hồ sơ nháp mới trước mỗi lượt, khi người kiểm thử đồng ý |
| Rủi ro | Mỗi ca chỉ chạy 1–2 lần, chỉ trên Chrome | Không loại được lỗi chập chờn hoặc lỗi riêng từng trình duyệt | Chạy lặp ca nghi ngờ; thêm trình duyệt khi cần |
| Rủi ro | Chưa có release note | Regression chọn theo vùng chức năng, không theo thay đổi thật của build | Xin release note từ Dev |
| Phụ thuộc | Chờ Dev trả lời câu hỏi và sửa lỗi | Re-test và regression không chạy được khi chưa có bản sửa | Gửi câu hỏi cho Dev sớm |

**9.2. Giả định**
- Chỉ test chức năng.
- Staging phản ánh đúng build 1.3.0.
- Tích hợp VNeID, CIC, SMS chưa thiết lập nên không nằm trong đợt test này.
- Smoke dùng quy tắc "Đạt kèm lỗi đã biết" và tiêu chí trả build đã chốt trong [smoke-test.md](smoke-test.md).

## 10. Truy vết requirement ↔ test case

| Tính năng | Requirement | Test case | Chưa có test case | Smoke | Regression Tầng 1 | Truy vết |
|---|---|---|---|---|---|---|
| Đăng nhập | 40 mã, 14 câu trả lời của BA | 43 | Không có | 3 ca (TC-001, 002, 005) | 7 ca (TC-001…005, 023, 026) | [mở](dang-nhap/truy-vet.md) |
| Khuyến nghị LTV/DSR | 61 mã, 2 câu trả lời của BA | 38 | [M09](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L154), [M10](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L155), [R12](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L141), [S03-AC11](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L93), [S04-AC01](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L102), [S04-AC04](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L105), [S05-AC02](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L115) | 4 ca (TC-002, 009, 022, 023) | 6 ca (TC-001, 002, 009, 014, 022, 023) | [mở](khuyen-nghi-ltv-dsr/truy-vet.md) |

**Độ phủ theo kế hoạch:** Đăng nhập 40/40; Khuyến nghị LTV/DSR 54/61 mã requirement có test case.
