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
| 7 mã requirement Khuyến nghị chưa có test case: M09, M10, R12, S03-AC11, S04-AC01, S04-AC04, S05-AC02 | Chưa viết case (xem [truy vết](khuyen-nghi-ltv-dsr/truy-vet.md)) | Phần định giá, CIC và vài quy tắc của Khuyến nghị không được kiểm |

## 3. Cách kiểm thử

| Lớp test | Để làm gì | Chạy khi nào | Cách làm | Bộ case |
|---|---|---|---|---|
| Smoke | Build có đủ ổn để test sâu không | Ngay khi nhận build | Tự động (Playwright), có thể làm tay | [smoke-test.md](smoke-test.md): 7 case, khoảng 12,5 phút |
| Test từng tính năng | Từng tính năng đúng theo requirement | Sau khi smoke Đạt | Tự động phần lớn; ca có thể làm khóa tài khoản do người kiểm thử làm tay | Đăng nhập 43 case, Khuyến nghị 38 case |
| Regression | Chỗ đã đúng còn đúng sau khi build đổi | Khi build có thay đổi | Tự động; vùng chặn đăng nhập làm tay | [regression-test.md](regression-test.md): Tầng 1 (13 case lõi), Tầng 2 (13 vùng, 68 case), Tầng 3 (toàn bộ 81 case). Người kiểm thử duyệt việc chọn tầng trước khi chạy |
| Re-test | Bug đã sửa có hết thật không | Khi Dev báo đã sửa | Làm theo kế hoạch re-test của từng bug | Kế hoạch lập khi có bug cần re-test |

**Thứ tự thực hiện:** smoke → test từng tính năng → regression → re-test. Smoke Không đạt thì dừng, trả build.

**Kỹ thuật thiết kế test case:** phân vùng tương đương, giá trị biên, bảng quyết định, chuyển trạng thái, use case, đoán lỗi (ghi ở cột Kỹ thuật của file test case).

## 4. Môi trường và dữ liệu test
- **Môi trường:** https://staging-banking-lite.vercel.app/ (có nhãn staging). Địa chỉ cũ `banking-lite.vercel.app` đã gỡ. Staging dùng chung dữ liệu: hồ sơ nháp của người khác có thể đang tồn tại.
- **Trình duyệt:** Chrome, chạy qua Playwright. Số bản Chrome: ……………
- **Ngôn ngữ giao diện:** Tiếng Việt và English.
- **Tài khoản test:**

| Tài khoản | Vai trò | Dùng cho |
|---|---|---|
| P100001 | Chuyên viên khách hàng | Đăng nhập; tạo hồ sơ nháp và mọi ca Khuyến nghị |
| P200001 | Chuyên viên định giá | Ca Đăng nhập theo vai trò |
| P300001 | Chuyên viên thẩm định tín dụng | Ca Đăng nhập theo vai trò |

  Mật khẩu lưu riêng trong kho tài khoản test của dự án, không ghi vào tài liệu.
- **Dữ liệu cần chuẩn bị:** mỗi ca Khuyến nghị cần một hồ sơ nháp đúng điều kiện trước. Hồ sơ nháp tạo bằng script `testing/banking-lite/auto/create_draft_application.py`. Ca có bấm `Lưu` (ví dụ TC-014, TC-022) làm hồ sơ không còn ở trạng thái đầu, nên mỗi ca cần một hồ sơ nháp riêng và phải tạo lại trước mỗi lượt chạy. Tạo hồ sơ là tạo dữ liệu thật trên staging, chỉ làm khi người kiểm thử đồng ý.
- **Chỗ dễ khóa hệ thống:** theo requirement, tài khoản bị chặn 5 phút khi nhập sai nhiều lần. Trần nhập sai cho script là 9 lần cộng dồn. Để tránh chặn nhầm, các ca nhập sai xả bộ đếm bằng một lần đăng nhập đúng xen kẽ. Tám ca mà chính bước làm sẽ chặn hệ thống (TC-015…020, 022, 037) do người kiểm thử tự làm tay.

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

## 6. Phân công và lịch

| Việc | Người làm | Bắt đầu | Hạn | Thời gian chạy | Ghi chú |
|---|---|---|---|---|---|
| Soát requirement, hỏi BA | Sunny Tran | …… | …… | — | Khuyến nghị cần BA xác nhận requirement nháp |
| Viết, cập nhật test case | Sunny Tran | …… | …… | — | 7 mã requirement Khuyến nghị chưa có case |
| Chạy smoke | Sunny Tran | …… | …… | Khoảng 12,5 phút | Gồm 2 phút chuẩn bị hồ sơ nháp |
| Chạy test từng tính năng | Sunny Tran | …… | …… | TC-042, TC-043 mỗi ca khoảng 11 phút | 8 ca làm tay |
| Chạy regression | Sunny Tran | …… | …… | — | Theo tầng đã duyệt |
| Re-test bug đã sửa | Sunny Tran | …… | …… | — | Khi Dev giao bản sửa |
| Lập báo cáo tổng kết, gửi duyệt build | Sunny Tran | …… | …… | — | Báo cáo tự sinh; người duyệt điền form quyết định |

**Người liên hệ:** BA: …………… · Dev: …………… · Người duyệt build: ……………

## 7. Quản lý bug
- **Cách ghi:** mỗi lỗi một bug report, đủ bước tái hiện, kết quả thực tế và mong đợi, môi trường, ảnh hoặc video, link tới test case Không đạt.
- **Thang đo:** mức nghiêm trọng gồm Nghiêm trọng / Lớn (còn gọi Nặng) / Nhỏ / Rất nhỏ; mức ưu tiên gồm Cao / Trung bình / Thấp.
- **Vòng đời bug:** Mới → Dev đã sửa → Đã re-test → Đóng hoặc Mở lại. Trạng thái chính thức nằm ở công cụ quản lý bug của team: ……………
- **Bug lọt production:** nếu chưa có test case chặn đúng bug đó thì viết case mới và đưa vào bộ regression.

## 8. Sản phẩm bàn giao

| Sản phẩm | Khi nào có | Vị trí |
|---|---|---|
| Bảng soát requirement, câu hỏi cho BA | Trước khi viết test case | [Bảng soát Đăng nhập](dang-nhap/bang-soat-requirement.md), [Câu hỏi BA](dang-nhap/cau-hoi-cho-ba.md) |
| Test case từng tính năng | Trước khi chạy | [Đăng nhập](dang-nhap/test-case.md), [Khuyến nghị](khuyen-nghi-ltv-dsr/test-case.md) |
| Bộ smoke và kết quả chạy | Khi nhận build | [smoke-test.md](smoke-test.md); kết quả `smoke-ket-qua.md` |
| Bộ regression và kết quả chạy | Khi build có thay đổi | [regression-test.md](regression-test.md); kết quả `regression-tang-1-ket-qua.md` |
| Bug report | Trong lúc test | Thư mục `bug` của từng tính năng |
| Kết quả test case từng tính năng | Sau khi chạy | `ket-qua-test-case.md` của từng tính năng |
| Báo cáo tổng kết kiểm thử (có form duyệt build, in PDF) | Cuối đợt | `test-summary-report.md` |

## 9. Rủi ro, giả định, phụ thuộc

**9.1. Rủi ro và phụ thuộc**

| Loại | Nội dung | Ảnh hưởng | Cách giảm / ai quyết |
|---|---|---|---|
| Rủi ro | Requirement Khuyến nghị là bản nháp, BA chưa xác nhận | 38 case Khuyến nghị có thể phải sửa; case Không đạt cần kiểm lại case trước khi kết luận | Gửi BA xác nhận trước khi chạy |
| Rủi ro | Chưa biết hệ thống đếm lần nhập sai đúng như BA quy định chưa (đếm theo tài khoản, đăng nhập đúng đưa về 0) | Chạy ca nhập sai có thể chặn tài khoản test 5 phút | Xả bộ đếm xen kẽ; làm tay ca chặn đăng nhập |
| Rủi ro | Phần thời hạn phiên 10 phút (TC-042, TC-043) có thể chưa được code làm | Hai ca này chưa kiểm được | Hỏi Dev trước khi chạy |
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
| Khuyến nghị LTV/DSR | 61 mã, 2 câu trả lời | 38 | 7 mã: [M09](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L154), [M10](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L155), [R12](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L141), [S03-AC11](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L93), [S04-AC01](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L102), [S04-AC04](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L105), [S05-AC02](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#L115) | 4 ca (TC-002, 009, 022, 023) | 6 ca (TC-001, 002, 009, 014, 022, 023) | [mở](khuyen-nghi-ltv-dsr/truy-vet.md) |

**Độ phủ theo kế hoạch:** Đăng nhập 40/40 mã requirement có test case; Khuyến nghị 54/61.

## 11. Phê duyệt kế hoạch

| Vai trò | Họ tên | Quyết định (Duyệt / Cần sửa) | Ngày | Ý kiến |
|---|---|---|---|---|
| Người lập | Sunny Tran | | | |
| Người duyệt kế hoạch | | | | |

## 12. Lịch sử cập nhật

| Ngày | Người sửa | Nội dung sửa | Lý do |
|---|---|---|---|
| 2026-11-19 | Sunny Tran | Tạo bản đầu | Lập kế hoạch kiểm thử cho bản 1.3.0 |
