# Banking Lite — báo cáo khám phá v2 HTML
Đọc khi: sửa/build báo cáo v2.

- File `evidence/banking-lite/bao-cao-kham-pha-v2.html` là **file build, không sửa tay**. Nguồn: `evidence/banking-lite/_src/bao-cao-kham-pha-v2.src.html` (không còn CSS: `<style id="giao-dien-chuan">` rỗng, build chèn CSS + font chuẩn của skill) + sơ đồ `_src/so-do/{tong-quan,tuan-tu,trang-thai}.json` (sửa sơ đồ = sửa JSON). Build: `python -X utf8 _src/build-embed.py`. Nội dung bám bản MD, không thêm giả định. Bản nguồn trước khi chuyển nằm trong git (commit `a1b7f15`).
- Khung xem trước của app hiện file như ảnh tĩnh (`data:`): ảnh đường dẫn tương đối **không tải được**; **từ chối file >512 KiB** (500 KB mở được, 540 KB không). Xử lý: mỗi ảnh nhúng 1 lần WebP thu nhỏ (360px) trong class `.fNN`; JS thay bằng ảnh gốc nếu `screenshots/` nằm cạnh. Build in % so giới hạn; hiện 98,3% (q37, có font ~40 KB) → thêm ảnh/chữ thì giảm `--thumb-w` hoặc chia báo cáo.
- Thanh tab điều hướng: `#anchor` thuần không chạy trong khung `data:` → JS bắt click → `window.scrollTo` (trừ chiều cao thanh sticky), tô tab đang xem; 8 tab đã kiểm.
- Khoanh nút: `<i class="mk" data-n="1" style="--x:..;--y:..;--w:..;--h:..">`, `--W/--H` = kích thước ảnh gốc trên `<figure>`; tọa độ = pixel ảnh gốc (đa số 606×845; ảnh 07/08/10: 411×675; 25/32: 485×676; 01: 800×600). Bấm ảnh để phóng to. `build-embed.py` tự chọn vị trí badge (đo điểm tối, phạt đè khung/số khác, tự giảm độ nới khi hai khung chạm). `--review <thư_mục>` xuất tranh ghép để soát bằng mắt. Lỗi hay gặp: **tọa độ sai ô** (LTV ở (210,216,75,40), Khuyến nghị ở (33,262,115,40) trong ảnh 36/40/41). Khung dùng `outline` để không đè chữ.
- Cấu trúc: Cách đọc → 1 Hệ thống là gì → 2 Bản đồ kết nối (SVG, số 1–11) → 3 Ba vai trò (từng bước kèm ảnh khoanh nút) → 4 End-to-end (tuần tự 15 bước, trạng thái, 4 đường A–D) → 5 Điểm mơ hồ M-01…M-13 → 6 Chưa thử C-1…C-6 → 7 Việc cần người dùng trả lời.
- Thuật ngữ người dùng yêu cầu: luồng (flow), quy trình (workflow), nút bị vô hiệu hóa (disabled), hồ sơ bị khóa, banner, trường nhập, đánh dấu (checkbox), mô phỏng (mock). Tiêu đề mục "Phân tích hồ sơ". Từ bị chê: giải phẫu, dây chuyền, tick (script chặn).
- Xem thử: phải mở qua `http://` (`python -m http.server` trong `evidence/banking-lite`), vì pane Browser hiện file cục bộ như ảnh tĩnh. Pane ẩn thì chụp màn hình timeout — thử lại.

## Khoảng trống bằng chứng (đừng bịa bù)
- Không có ảnh nút "Gửi thẩm định" (chỉ ảnh kết quả 24/41); cần P100001 đăng nhập lại.
- Không có ảnh "Khuyến nghị cũ sau khi sửa, trước khi gửi lại" (M-04).
- "Nút Gửi không khóa khi LTV 85%" và HL-000003 "Đã hủy" chỉ là ghi chép, không ảnh. Ảnh 36, 32 chỉ chụp đầu trang.
