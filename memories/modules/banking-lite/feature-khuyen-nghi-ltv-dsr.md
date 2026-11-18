# Banking Lite — Khuyến nghị thẩm định xem trước (`RECO`)
Đọc khi: làm SRS/bảng soát/checklist/test case `RECO`. SRS `srs/banking-lite/khuyen-nghi-ltv-dsr.md` (6 story, 37 AC, 12 R, 12 M, 7 Q, 22 E; `check-srs.py` 0 lỗi). Nhật ký + 10 ảnh: `evidence/banking-lite/features/khuyen-nghi-ltv-dsr/`. Lần đầu chạy trọn skill `srs-from-website`. **SRS chưa được người dùng review, chưa sửa theo TL-02.**

## Luật (đọc từ thông báo lý do + API)
- Khung "Thẩm định" ở bước Tài chính tính **ngay khi nhập**; ô **Khuyến nghị đầu trang chỉ đổi sau `Lưu`**, chậm vài giây (đợi ≥8 giây).
- LTV tối đa **80% (Mua nhà) / 70% (Xây/sửa nhà)** → Từ chối. DSR ≤50% ổn; **>50–70% Chuyển cấp trên; >70% Từ chối**. Thặng dư ≥ **3.000.000** (so đúng từng đồng). Tuổi cao nhất lúc đáo hạn ≤ **70**. Còn 2 luật chỉ thấy trong tệp giao diện: `valuationShortfall`, `cicDebtGroup` (cần định giá/CIC). Bảng ghi nhớ cũ "LTV>80, DSR>50" **thiếu** ba luật sau và luật 70%.
- Chi phí tính = max(nhập, 4.500.000 + 2.000.000 × người phụ thuộc); DSR = (khoản trả mới + nợ hiện có)/thu nhập; khoản trả mới đổi theo thời hạn, Niên kim/Gốc đều, ân hạn. Lãi suất thẩm định đổi theo LTV và sản phẩm (36 tháng thấp hơn 0,5 điểm ở LTV 64%).
- **Bất thường (Q02):** tuổi >70 → API `DECLINE` + `ageAtMaturity` nhưng màn hình **không hiện nhãn/lý do**, lại hiện "Nhập đủ thông tin…". Tệp giao diện còn câu bước quyết định "Không thể phê duyệt hồ sơ được khuyến nghị từ chối." (Q07, cần P300001).

## TL-02 làm tròn (người dùng chốt 2026-11-17, **chưa có BA xác nhận**)
- So ngưỡng LTV/DSR dùng số làm tròn 2 chữ số. Hệ thống làm tròn **gần nhất** (80,0025% và 50,0006% vẫn đạt). Người dùng chọn phương án C: làm tròn **LÊN** 2 chữ số rồi so ngưỡng, **áp dụng cả khi hiển thị** ("về phía bất lợi cho người vay"). Mình đã nói đây chỉ là gợi ý chung, không có nguồn về "ngân hàng thường làm", khuyên giữ A (khớp hệ thống); người dùng vẫn chọn C.
- Hệ quả: 3 ca khác kết quả hệ thống → nghi lỗi nếu BA xác nhận: lương 58.285.714 (đúng ra Từ chối, hệ thống Chuyển cấp trên); lương 81.599.000 (đúng ra Chuyển cấp trên, hệ thống Phê duyệt); vay 3.200.100.000 (đúng ra Từ chối, hệ thống Phê duyệt). 8 số % trong SRS khác số đúng: 50,37→50,38; 70,34→70,35; 77,18→77,19; 53,33→53,34; 76,19→76,20; 34,13→34,14; 31,50→31,51; 53,51→53,52. Tổng 11 AC khác hệ thống. Số đã đúng: 54,40; 40,80; 48,00; 45,80; 64,00; 80,00; 81,00; 106,67; 30,99; 30,47.
- **Số trong SRS = số hệ thống đang hiển thị, KHÔNG phải kết quả mong đợi theo TL-02.** Lãi suất thẩm định tại LTV 53,34% chưa biết còn 9,90% không.

## Chỗ SRS tự lệch (chưa sửa)
- `S01-AC06` gọi "DSR đúng 70,00%" nhưng 40.800.000 ÷ 58.285.714 ≈ 70,0000003% mà vẫn Chuyển cấp trên → bằng chứng cho Q01 (so số làm tròn). Chỉ `S01-AC05` (lương 81.600.000) đúng 50,0000%.
- `S03-AC11`: thặng dư 99.999.915.366.666 lệch 39.333.333 so công thức hồ sơ nền (đúng …954.699.999); hiệu 84.633.333 = chi phí 44,5 triệu (20 người phụ thuộc) + khoản trả mới 40.133.333 (LTV 64%) → có thể trạng thái dư từ lượt thử trước; cần chạy lại.
- `S03-AC08/09/10` không ghi lương/chi phí/nợ (DSR 30,99% suy ra lương 100 triệu); `S03-AC09` ghi `31,5%` khác định dạng 2 chữ số.
- Tuổi 56/70/71 (S04) đúng theo ngày quan sát; quy tắc tính tuổi chưa ghi nên đổi ngày có thể đổi.

## Bảng soát / câu hỏi (`testing/banking-lite/khuyen-nghi-ltv-dsr/`)
- Bảng soát 37 AC; câu hỏi BA: A hỏi ngay 5, B hỏi sau 12, C tự kiểm tra 14. Phân tích cũ 62 TC (Cao 22, TB 34, Thấp 6), 18 CH, 16 KN; 10 mã chỉ nằm ở câu hỏi (M09, M10, R12, S01-AC06/07, S02-AC02, S03-AC11, S04-AC01/04, S05-AC02). Có thể thêm 3 TC biên làm tròn (chưa thêm vì luật giữ số lượng).
- Số liệu ví dụ trong câu hỏi đã tính lại bằng script (sai lệch <1 đồng).

## Dữ liệu test mình tạo
- HL-000024 (`172396e6-7d1e-4579-9666-c9e057eb8a62`): nháp rỗng, bỏ.
- HL-000025 (`38d4fdef-efd5-4f59-8c7e-6f29084975b0`): Nháp; vay 3,2 tỷ; Xây/sửa nhà · Niên kim · ân hạn 12 tháng · khai báo 4,2 tỷ; lương 100 triệu; chưa định giá/gửi; giao diện đã về Tiếng Việt.

## Bẫy
- Công cụ tự chặn `Yêu cầu định giá` bấm bằng JS ("Destructive or Unwanted Actions"): dừng, không đi đường vòng; cần người dùng cho phép rõ.
- `read_page`/`find` chập chờn khi "Đang tải…": chờ 6–7 giây hoặc đọc `document.querySelector('main').innerText` bằng `javascript_tool`.
- Đọc **thân GET `/api/applications/<id>`** bằng `fetch` trong `javascript_tool` → `assessment` (metrics, reasons, mã lý do): nhanh hơn, lộ cả lỗi hiển thị. Bấm `Lưu` bằng JS (button có chữ `Lưu`) ổn định hơn `find`. Mỗi lần lưu ~8 giây; ~20 lần không thấy giới hạn tốc độ.
- Bước Tài chính chỉ mở sau bước Người vay → dùng `Tạo từ hồ sơ có sẵn`.

## Chưa làm
Định giá/CIC (M09, M10), P200001/P300001 xem khung, nhiều người vay, sản phẩm 24 tháng; Q01–Q07 cần team.
