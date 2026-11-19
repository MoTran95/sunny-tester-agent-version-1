# Kết quả chạy smoke test — banking-lite

> File tự sinh từ `testing/banking-lite/run-results/smoke.json` bằng `scripts/build_report.py` — đừng sửa tay, chạy lại là ghi đè. Bản dễ xem: `smoke-ket-qua.html`.

| | |
|---|---|
| Build | **1.3.0** |
| Lượt | 2 / 2 (lượt mới nhất) |
| Thời điểm | 2026-11-19 11:34:35 |
| Người chạy | Sunny Tran |
| Cách chạy | Tự động (Playwright) |
| Kết luận | **Chưa đủ kết luận** |
| Ghi chú | Chạy tự động bằng Playwright trên môi trường thử staging (https://staging-banking-lite.vercel.app/), bản 1.3.0, ngày 2026-11-19. Ca số 2 (TC-001) còn chữ DEFAULT trên thanh điều hướng: lỗi đã biết ở BUG-001, bộ smoke cho phép nhận build. Ca số 6 (TC-022 của tính năng Khuyến nghị LTV/DSR) không kết luận được vì hồ sơ nháp của riêng ca này đã dùng hết; cần tạo hồ sơ nháp mới trên staging (tạo dữ liệu thật nên cần bạn đồng ý) rồi chạy lại. |

## Kết quả lượt mới nhất

| ID | Smoke case | Các bước | Kết quả mong đợi | Status | Evidence | Bug | Số lần chạy |
|---|---|---|---|---|---|---|---|
| SM-01 | Hiển thị form đăng nhập đủ ô nhập, nút và phiên bản ở chân trang khi mở hệ thống lúc chưa đăng nhập (Đăng nhập · TC-005) | 1. Mở https://staging-banking-lite.vercel.app/.<br>2. Nhìn tên hai ô nhập.<br>3. Nhìn dòng chữ gợi ý bên dưới ô Mã nhân viên.<br>4. Nhìn nút bên dưới hai ô.<br>5. Nhìn chân trang.<br>6. Bấm vào ô Mật khẩu *, gõ abc123 (chưa bấm nút).<br>7. Nhìn chữ vừa gõ trong ô Mật khẩu. | Bước 2: có ô Mã nhân viên * và ô Mật khẩu *.<br>Bước 3: dòng gợi ý Chữ P và 6 chữ số, ví dụ P100001.<br>Bước 4: nút Đăng nhập.<br>Bước 5: chân trang ghi Banking Lite · Phiên bản 1.3.0.<br>Bước 7: chữ gõ trong ô Mật khẩu hiện dạng chấm, không hiện chữ rõ. | Đạt | [dang-nhap-tc-005-form-dang-nhap-20261119-113358.png](../../evidence/banking-lite/chay-test/dang-nhap-tc-005-form-dang-nhap-20261119-113358.png) | — | 2 |
| SM-02 | Vào được Danh sách việc của Chuyên viên khách hàng khi đăng nhập đúng `P100001` (Đăng nhập · TC-001) | 1. Mở https://staging-banking-lite.vercel.app/.<br>2. Ở ô Mã nhân viên * nhập P100001.<br>3. Ở ô Mật khẩu * nhập mật khẩu đúng của P100001.<br>4. Bấm nút Đăng nhập.<br>5. Nhìn trang hiện ra và thanh trên cùng. | Bước 4: vào trang Danh sách việc của P100001; không hiện thông báo "đăng nhập thành công".<br>Bước 5: thanh trên cùng hiện P100001 và vai trò Chuyên viên khách hàng; không có chữ DEFAULT. | Đạt kèm lỗi đã biết | [dang-nhap-tc-001-danh-sach-viec-20261119-113402.png](../../evidence/banking-lite/chay-test/dang-nhap-tc-001-danh-sach-viec-20261119-113402.png)<br>🔴 [dang-nhap-tc-001-loi-20261119-113402.png](../../evidence/banking-lite/chay-test/dang-nhap-tc-001-loi-20261119-113402.png) (tô đỏ chỗ lỗi): Lỗi ở bước 5 (nhìn thanh điều hướng sau khi đăng nhập): thanh điều hướng hiện chữ DEFAULT sau mã và vai trò, đáng ra không có chữ này.<br>🎬 [dang-nhap-tc-001-p100001-20261119-113402.webm](../../evidence/banking-lite/chay-test/video/dang-nhap-tc-001-p100001-20261119-113402.webm) (video quay lại ca) | [BUG-001](dang-nhap/bug/BUG-001.md) | 2 |
| SM-03 | Hiển thị khuyến nghị Phê duyệt khi nhập lương 100 triệu và hồ sơ đạt mọi quy tắc (Khuyến nghị LTV/DSR · TC-002) | 1. Mở https://staging-banking-lite.vercel.app/ và đăng nhập P100001.<br>2. Mở hồ sơ nháp ở điều kiện trước.<br>3. Mở bước Tài chính.<br>4. Ở ô Lương hằng tháng nhập 100000000, không bấm Lưu.<br>5. Nhìn khung Thẩm định. | Bước 5: khung Thẩm định đổi ngay khi nhập, không cần bấm Lưu.<br>Bước 5: nhãn Phê duyệt; dòng nhỏ Xem trước: thẩm định chính thức chạy khi gửi, có dữ liệu CIC.<br>Bước 5: khoản trả mới 40.800.000 VND; thu nhập được tính 100.000.000 VND; chi phí được tính 4.500.000 VND; DSR 40,80%; thặng dư 54.700.000 VND.<br>Bước 5: mục Lý do ghi Đáp ứng mọi quy tắc tín dụng. | Đạt | [khuyen-nghi-ltv-dsr-tc-002-khung-tham-dinh-20261119-113408.png](../../evidence/banking-lite/chay-test/khuyen-nghi-ltv-dsr-tc-002-khung-tham-dinh-20261119-113408.png) | — | 2 |
| SM-04 | Hiển thị Chuyển cấp trên khi DSR 54,40% (lương 75 triệu) (Khuyến nghị LTV/DSR · TC-023) | 1. Mở https://staging-banking-lite.vercel.app/ và đăng nhập P100001.<br>2. Mở hồ sơ nháp ở điều kiện trước.<br>3. Mở bước Tài chính.<br>4. Ở ô Lương hằng tháng nhập 75000000, không bấm Lưu.<br>5. Nhìn khung Thẩm định: nhãn, DSR, thặng dư và mục Lý do. | Bước 5: DSR 54,40%.<br>Bước 5: nhãn Chuyển cấp trên. | Đạt | [khuyen-nghi-ltv-dsr-tc-023-khung-tham-dinh-20261119-113413.png](../../evidence/banking-lite/chay-test/khuyen-nghi-ltv-dsr-tc-023-khung-tham-dinh-20261119-113413.png) | — | 2 |
| SM-05 | Hiển thị Từ chối kèm lý do khi thặng dư hằng tháng thiếu 1 đồng so với mức tối thiểu (Khuyến nghị LTV/DSR · TC-009) | 1. Mở https://staging-banking-lite.vercel.app/ và đăng nhập P100001.<br>2. Mở hồ sơ nháp ở điều kiện trước.<br>3. Mở bước Tài chính.<br>4. Ở ô Lương hằng tháng nhập 100000000.<br>5. Ở ô Chi phí sinh hoạt hằng tháng nhập 56200001.<br>6. Nhìn khung Thẩm định. | Bước 6: thặng dư 2.999.999 VND.<br>Bước 6: nhãn Từ chối; lý do Từ chối: Thặng dư hằng tháng 2.999.999 VND thấp hơn 3.000.000 VND. | Đạt | [khuyen-nghi-ltv-dsr-tc-009-khung-tham-dinh-20261119-113419.png](../../evidence/banking-lite/chay-test/khuyen-nghi-ltv-dsr-tc-009-khung-tham-dinh-20261119-113419.png) | — | 2 |
| SM-06 | Cập nhật khuyến nghị ở đầu trang hồ sơ sau vài giây khi nhập lương rồi bấm Lưu (Khuyến nghị LTV/DSR · TC-022) | 1. Mở https://staging-banking-lite.vercel.app/ và đăng nhập P100001.<br>2. Mở hồ sơ nháp ở điều kiện trước.<br>3. Mở bước Tài chính.<br>4. Nhập Lương hằng tháng 100000000, Khoản trả nợ hiện có hằng tháng 5000000, Số người phụ thuộc 5.<br>5. Bấm Lưu.<br>6. Nhìn đầu trang hồ sơ ngay sau khi lưu, rồi chờ khoảng 8 giây và nhìn lại ô Khuyến nghị.<br>7. Nhìn trạng thái của bước Tài chính.<br>8. Tải lại trang, mở lại bước Tài chính và nhìn ô Lương hằng tháng. | Bước 5: hiện thông báo Đã lưu.<br>Bước 6: phản hồi chậm vài giây (lần quan sát: 4 giây sau khi lưu vẫn —); sau đó ô Khuyến nghị đầu trang thành Phê duyệt.<br>Bước 7: bước Tài chính ghi Đã xong.<br>Bước 8: ô Lương hằng tháng giữ giá trị 100000000. | Không kết luận | — | — | 1 |
| SM-07 | Vào được đúng Danh sách việc và đúng vai trò khi đăng nhập bằng `P200001` rồi `P300001` (Đăng nhập · TC-002) | 1. Mở https://staging-banking-lite.vercel.app/.<br>2. Ở ô Mã nhân viên * nhập P200001.<br>3. Ở ô Mật khẩu * nhập mật khẩu đúng của P200001.<br>4. Bấm nút Đăng nhập.<br>5. Nhìn trang hiện ra và thanh trên cùng.<br>6. Bấm Đăng xuất.<br>7. Ở ô Mã nhân viên * nhập P300001.<br>8. Ở ô Mật khẩu * nhập mật khẩu đúng của P300001.<br>9. Bấm nút Đăng nhập.<br>10. Nhìn trang hiện ra và thanh trên cùng. | Bước 4: vào Danh sách việc của P200001.<br>Bước 5: thanh trên cùng hiện P200001 và vai trò Chuyên viên định giá.<br>Bước 6: về form Đăng nhập.<br>Bước 9: vào Danh sách việc của P300001.<br>Bước 10: thanh trên cùng hiện P300001 và vai trò Chuyên viên thẩm định tín dụng. | Đạt | [dang-nhap-tc-002-p200001-danh-sach-viec-20261119-113429.png](../../evidence/banking-lite/chay-test/dang-nhap-tc-002-p200001-danh-sach-viec-20261119-113429.png)<br>[dang-nhap-tc-002-p300001-danh-sach-viec-20261119-113434.png](../../evidence/banking-lite/chay-test/dang-nhap-tc-002-p300001-danh-sach-viec-20261119-113434.png) | — | 2 |

## Lịch sử các lượt

| Lượt | Build | Thời điểm | Người chạy | Kết quả | Kết luận |
|---|---|---|---|---|---|
| 2 | 1.3.0 | 2026-11-19 11:34:35 | Sunny Tran | 5 Đạt, 1 Đạt kèm lỗi đã biết, 1 Không kết luận | Chưa đủ kết luận |
| 1 | 1.3.0 | 2026-11-18 21:23:25 | Sunny Tran | 6 Đạt, 1 Đạt kèm lỗi đã biết | Nhận build |

## Từng case qua các lượt (tối đa 8 lượt gần nhất)

| ID | Lượt 1 (1.3.0) | Lượt 2 (1.3.0) |
|---|---|---|
| SM-01 | Đạt | Đạt |
| SM-02 | Đạt kèm lỗi đã biết | Đạt kèm lỗi đã biết |
| SM-03 | Đạt | Đạt |
| SM-04 | Đạt | Đạt |
| SM-05 | Đạt | Đạt |
| SM-06 | Đạt | Không kết luận |
| SM-07 | Đạt | Đạt |

Các bước và Kết quả mong đợi lấy từ test case gốc. Bị chặn: chưa test được vì bug khác (xem cột Bug). Số lần chạy: số lượt có kết luận Đạt, Đạt kèm lỗi đã biết, Đạt kèm ý phụ sai hoặc Không đạt; lượt Không kết luận và Chưa chạy không tính.
