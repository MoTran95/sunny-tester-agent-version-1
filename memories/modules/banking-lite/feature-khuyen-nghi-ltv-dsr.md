# Feature “Khuyến nghị thẩm định xem trước (LTV/DSR)” — kết quả khám phá + SRS
Cập nhật: 2026-11-17 · Liên quan: [exploration-findings.md](exploration-findings.md), [../../project/srs-process.md](../../project/srs-process.md), [../../project/skills.md](../../project/skills.md)

SRS: `srs/banking-lite/khuyen-nghi-ltv-dsr.md` (mã `RECO`, 6 story, 37 AC, 12 R, 12 M, 7 Q, 22 E; `check-srs.py` 0 lỗi 0 cảnh báo). Nhật ký + 10 ảnh: `evidence/banking-lite/features/khuyen-nghi-ltv-dsr/`. Đây là **lần đầu chạy trọn skill `srs-from-website` trên feature mới**; người dùng chọn feature này trong 3 ứng viên.

## Điều học được (đã thấy; mọi ngưỡng đọc từ thông báo lý do + API)
- Khung “Thẩm định” ở bước Tài chính tính **ngay khi nhập** (không cần lưu); ô **Khuyến nghị đầu trang chỉ đổi sau `Lưu`** (và chậm vài giây — đợi ≥8 giây trước khi đọc).
- Luật hiện có: LTV tối đa **80% (Mua nhà) / 70% (Xây/sửa nhà)** → Từ chối; DSR ≤50% ổn, **>50–70% Chuyển cấp trên, >70% Từ chối**; thặng dư ≥ **3.000.000** (tính tuyệt đối); tuổi cao nhất lúc đáo hạn ≤ **70**. Bảng ghi nhớ cũ “LTV>80 → Từ chối; DSR>50 → Chuyển cấp trên” **thiếu** ba luật sau (DSR>70, thặng dư, tuổi) và luật 70% của Xây/sửa nhà. Còn 2 luật chỉ thấy trong tệp giao diện: `valuationShortfall`, `cicDebtGroup` (cần định giá/CIC).
- So ngưỡng LTV/DSR dùng **số làm tròn 2 chữ số** (80,0025% và 50,0006% vẫn đạt); thặng dư thì so đúng từng đồng. **Quyết định của người dùng 2026-11-17 (TL-02, thay TL-01 “làm tròn gần nhất”): làm tròn LÊN 2 chữ số thập phân** (phương án C, “về phía bất lợi cho người vay”) rồi so ngưỡng; người dùng tự chốt, **chưa có BA xác nhận**. Mình đã nói rõ đây chỉ là gợi ý chung, không có nguồn trích dẫn được về “ngân hàng thường làm”, và khuyên giữ phương án A vì khớp hệ thống — người dùng vẫn chọn C. **Hệ quả:** hệ thống hiện tại làm tròn gần nhất khi so ngưỡng ⇒ khác kết quả mong đợi ở 3 ca (lương 58.285.714: đúng ra Từ chối, hệ thống cho Chuyển cấp trên; lương 81.599.000: đúng ra Chuyển cấp trên, hệ thống Phê duyệt; vay 3.200.100.000: đúng ra Từ chối, hệ thống Phê duyệt) → nghi lỗi nếu BA xác nhận. **Phạm vi (người dùng chốt 2026-11-17): áp dụng CẢ khi hiển thị** ⇒ 8 số % trong SRS khác số đúng (50,37→50,38; 70,34→70,35; 77,18→77,19; 53,33→53,34; 76,19→76,20; 34,13→34,14; 31,50→31,51; 53,51→53,52), tổng 11 AC khác hệ thống hiện tại (nghi một nguyên nhân chung: hệ thống làm tròn gần nhất ở mọi chỗ). Các số đã chính xác không đổi (54,40; 40,80; 48,00; 45,80; 64,00; 80,00; 81,00; 106,67; 30,99; 30,47). Điểm cần nhớ: số trong SRS = số hệ thống đang hiển thị, KHÔNG phải kết quả mong đợi theo TL-02; lãi suất thẩm định tại LTV 53,34% chưa biết còn 9,90% không. SRS `RECO` chưa sửa (chờ BA/PO xác nhận).
- Chi phí được tính = max(nhập, 4.500.000 + 2.000.000 × người phụ thuộc) (3 điểm: 2, 5, 20); cho thuê tính 70%; DSR = (khoản trả mới + nợ hiện có)/thu nhập. Khoản trả mới đổi theo thời hạn, Niên kim/Gốc đều, ân hạn. Lãi suất thẩm định đổi theo LTV và sản phẩm (36 tháng thấp hơn 0,5 điểm % ở LTV 64%).
- **Điểm bất thường cần hỏi team:** thời hạn vay quá dài (tuổi >70) → API trả `DECLINE` + lý do `ageAtMaturity` nhưng màn hình **không hiện nhãn/lý do**, lại hiện “Nhập đủ thông tin…” (Q02). Tệp giao diện còn câu bước quyết định: “Không thể phê duyệt hồ sơ được khuyến nghị từ chối.” (Q07, cần P300001).

## Chỗ SRS này tự lệch (phát hiện khi phân tích requirement, 2026-11-17 — chưa sửa SRS)
- `S01-AC06` gọi là “DSR đúng 70,00%” nhưng 40.800.000 ÷ 58.285.714 ≈ 70,0000003% (>70) mà vẫn `Chuyển cấp trên` → thêm một bằng chứng cho Q01 (so số làm tròn), không phải ca biên 70% đúng. Chỉ `S01-AC05` (lương 81.600.000) là đúng 50,0000%.
- `S03-AC11`: thặng dư ghi 99.999.915.366.666 lệch 39.333.333 so với công thức hồ sơ nền (đúng ra …954.699.999); hiệu số 84.633.333 = chi phí 44,5 triệu (20 người phụ thuộc) + khoản trả mới 40.133.333 (LTV 64%) → có thể là trạng thái dư từ lượt thử trước. Cần chạy lại để sửa số.
- `S03-AC08/09/10` không ghi lương/chi phí/nợ trong bối cảnh (DSR 30,99% suy ra lương 100 triệu); `S03-AC09` ghi DSR `31,5%` (một số lẻ) khác định dạng 2 chữ số chỗ khác.
- Tuổi 56/70/71 (S04) đúng theo ngày quan sát; quy tắc tính tuổi (mốc ngày, tròn năm) chưa ghi nên chạy ngày khác có thể đổi.

## Dữ liệu test mình tạo
- HL-000024 (id `172396e6-7d1e-4579-9666-c9e057eb8a62`): nháp rỗng, bỏ không dùng.
- HL-000025 (id `38d4fdef-efd5-4f59-8c7e-6f29084975b0`): Nháp; vay 3,2 tỷ; Xây/sửa nhà · Niên kim · ân hạn 12 tháng · khai báo 4,2 tỷ; lương 100 triệu; chưa định giá, chưa gửi. Giao diện đã đưa về Tiếng Việt.

## Bẫy và bài học khi làm feature này
- **Công cụ tự động chặn** thao tác `Yêu cầu định giá` bấm bằng JS (“Destructive or Unwanted Actions”): mình dừng, không đi đường vòng. Muốn làm cần người dùng cho phép rõ.
- `read_page`/`find` chập chờn khi trang còn “Đang tải…”: chờ 6–7 giây, hoặc đọc `document.querySelector('main').innerText` bằng `javascript_tool`.
- Đọc **thân phản hồi GET `/api/applications/<id>`** bằng `fetch` trong `javascript_tool` cho ra `assessment` (metrics, reasons, mã lý do) — nhanh hơn đọc màn hình và lộ cả lỗi hiển thị. Bấm `Lưu` bằng JS (`button` có chữ `Lưu`) ổn định hơn `find`.
- Bước Tài chính chỉ mở sau bước Người vay; cách nhanh: `Tạo từ hồ sơ có sẵn` (Tester Mot + CT 100019).
- Mỗi lần lưu mất ~8 giây; đã lưu khoảng 20 lần trên hồ sơ nháp của mình, không thấy giới hạn tốc độ.

## Việc còn lại
Chờ người dùng review SRS; chưa làm: định giá/CIC (thông báo M09, M10), P200001/P300001 xem khung, nhiều người vay, sản phẩm 24 tháng. Trả lời Q01–Q07 cần team.
