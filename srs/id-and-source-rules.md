# Quy tắc đặt ID và ghi nguồn cho SRS
Cập nhật: 2026-11-17 · Trạng thái: **bản nháp đã thống nhất hướng với người dùng** (Story + AC, mã feature tiếng Anh ngắn) · Khuôn: [_template.md](_template.md)

Mục tiêu: mọi yêu cầu **tra cứu được**, **truy được về bằng chứng**, và sau này test case **gắn thẳng vào ID** mà không phải đoán.

## 1. Cấu trúc ID
Dạng chung: `<FEATURE>-<LOẠI><số>`; riêng tiêu chí chấp nhận nằm dưới story: `<FEATURE>-S<nn>-AC<nn>`.

| Loại | ID mẫu | Là gì |
|---|---|---|
| Feature | `LOGIN` | 2–8 chữ HOA tiếng Anh, không dấu, mỗi feature một mã (xem bảng mã ở mục 5) |
| Story | `LOGIN-S01` | Một mục đích của người dùng ("Là …, tôi muốn … để …") kèm luồng |
| **Tiêu chí chấp nhận (AC)** | `LOGIN-S01-AC01` | **Đơn vị yêu cầu nhỏ nhất kiểm chứng được.** Test case gắn vào AC |
| Quy tắc dữ liệu | `LOGIN-R01` | Quy tắc cho một trường/dữ liệu (độ dài, định dạng, bắt buộc…) |
| Thông báo | `LOGIN-M01` | Một thông báo hệ thống, chép nguyên văn cả hai ngôn ngữ |
| Câu hỏi | `LOGIN-Q01` | Điểm chưa rõ cần team trả lời |
| Bằng chứng | `LOGIN-E01` | Một ảnh / một lần quan sát, có tệp và cách kiểm lại |

## 2. Quy tắc bất biến
1. ID **không bao giờ đổi số, không dùng lại**, không đánh số lại khi xóa/chèn. Mục mới lấy số tiếp theo.
2. Một AC = **một** điều kiểm chứng được. Có chữ "và" nối hai hành vi khác nhau → tách thành hai AC.
3. Bỏ một mục: giữ dòng, đổi nhãn `đã bỏ`, ghi "thay bằng `<ID>`" nếu có. Đổi **ý nghĩa** (không chỉ câu chữ) → tạo ID mới, mục cũ `đã bỏ`. Chỉ sửa câu chữ/ví dụ → giữ ID, ghi dòng ở "Lịch sử thay đổi".
4. Số hai chữ số (`01`…`99`); quá 99 thì dùng ba chữ số cho các mục mới, giữ nguyên mục cũ.
5. Nhãn của story/AC/quy tắc: `đã thấy` (có bằng chứng) · `chưa rõ` (thấy một phần hoặc mâu thuẫn, có Q) · `đã bỏ`. Sau này team xác nhận → thêm nhãn `đã xác nhận` (ghi ngày + người).
6. Không ghi AC nào không có bằng chứng. Điều chưa thử → mục "Chưa khám phá", không phải AC.

### 2b. Khi BA xác nhận yêu cầu thay cho bản quan sát (thêm 2026-11-18, `LOGIN`)
SRS ghi hành vi quan sát có thể được thay bằng yêu cầu BA đã xác nhận. Cách làm: **giữ ID** (tình huống vẫn là tình huống đó, chỉ kết quả mong đợi đổi), cột phản hồi đổi thành **"Yêu cầu"**, thêm cột **"Hệ thống <phiên bản> hiện tại"** giữ nguyên chữ quan sát cũ (ghi `Khớp yêu cầu` hoặc `⚠️ Khác yêu cầu`); nhãn `đã xác nhận` kèm ngày, người, mã câu trả lời. Mục BA bỏ: giữ dòng, nhãn `đã bỏ`, ghi "thay bằng `<ID>`". Chỗ khác yêu cầu là nghi lỗi cho tới khi dev xác nhận. Lý do giữ ID dù ý nghĩa kết quả đổi: test case và truy vết gắn vào ID, đổi ID sẽ làm đứt (xem mục 4); script `scripts/truy-vet.py` báo test case cần xem lại khi nội dung mã đổi.

### 2c. Ghi thời điểm trong lịch sử thay đổi (thêm 2026-11-18)
Dòng lịch sử mới ghi `YYYY-MM-DD HH:MM:SS (+07:00)` theo đồng hồ máy lúc ghi, kèm mã commit gốc nếu có. Dòng cũ chỉ có ngày thì ghi "không rõ giờ", không bịa giờ. Giờ ghi khác giờ BA trả lời; ngày BA trả lời ghi riêng khi biết. Lịch sử truy vết của test case do `scripts/truy-vet.py chot` tự ghi giờ, commit gốc và cờ "sửa chưa commit".

### 2d. Tham chiếu câu trả lời và câu hỏi của BA (thêm 2026-11-18)
Mã câu trả lời (`TL-xx`) và câu hỏi (`B4`…) viết trong SRS phải là link bấm được tới điểm nhảy `<a id="tl-xx">` / `<a id="b4">` đặt ở file bảng soát và file câu hỏi BA. Thêm mã mới thì thêm điểm nhảy trước khi dùng.

## 3. Ghi nguồn (truy vết và kiểm chứng)
- Mỗi AC/quy tắc/thông báo có cột **Bằng chứng** chứa ID `…-Exx`.
- Mỗi bằng chứng nằm trong bảng **Bằng chứng** của SRS với đủ các cột: ID · Loại · Ngày/phiên bản/tài khoản · Thao tác đã làm · **Tệp (liên kết bấm được)** · **Cách kiểm lại**.
- Loại bằng chứng: `ảnh` (có tệp ảnh) · `quan sát công cụ nhà phát triển` (Network, giá trị lưu trong trình duyệt…; **không có ảnh**, ghi rõ cách mở lại) · `báo cáo cũ` (lượt khám phá trước; ghi tệp nguồn).
- "Cách kiểm lại" viết sao cho người khác làm theo là thấy lại đúng kết quả (URL, tài khoản, dữ liệu nhập, nơi nhìn).
- Nhật ký khám phá gốc (`evidence/<hệ thống>/features/<feature>/bao-cao.md`) là nơi ghi thao tác theo thứ tự thời gian; SRS chỉ dẫn tới nó, không chép lại.
- Ảnh/nhật ký là **ảnh chụp tại một thời điểm** — khám phá lại thì lưu bộ mới, không ghi đè; bằng chứng mới nhận ID `E` mới.

## 4. Nối với bước sau (dự kiến, chưa làm)
- Test case sẽ có trường "Covers: `LOGIN-S01-AC01, LOGIN-R02`". Một AC có thể có nhiều test case; một test case có thể phủ nhiều AC.
- AC đổi hoặc `đã bỏ` → các test case trỏ tới nó bị đánh dấu cần xem lại. Đây là lý do SRS **sửa tại chỗ**, giữ ID.

## 5. Bảng mã feature (thêm dòng khi có feature mới, không đổi mã đã dùng)
| Mã | Feature | SRS |
|---|---|---|
| `LOGIN` | Đăng nhập, đăng xuất, ngôn ngữ ở màn hình đăng nhập | `srs/banking-lite/dang-nhap.md` |
| `SUBMIT` | Gửi thẩm định (dự kiến, chưa có SRS) | — |
| `RECO` | Khuyến nghị thẩm định xem trước (LTV, DSR, thặng dư, tuổi đáo hạn) ở bước Tài chính | `srs/banking-lite/khuyen-nghi-ltv-dsr.md` |
