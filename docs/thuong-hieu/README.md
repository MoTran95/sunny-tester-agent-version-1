# Giao diện thương hiệu của mọi trang HTML

Mọi trang HTML do script sinh ra (bảng kết quả chạy, trang bug, trang tài liệu SRS/test case/bảng soát…, trang tổng) dùng **một** bộ giao diện duy nhất: `scripts/test_automation/theme.py`. Máy khác hay dự án khác chỉ cần clone repo là ra trang giống hệt; không có cấu hình riêng theo máy.

## Màu (lấy mẫu từ ảnh thương hiệu, hạ độ sáng cho đỡ chói)

| Vai trò | Sáng | Tối |
|---|---|---|
| Nền trang | `#E8DFD0` | `#251F1A` |
| Thẻ, bảng | `#F2EDE5` | `#2E2721` |
| Chữ chính | `#3A2E26` | `#F1E6D4` |
| Nhấn đỏ san hô (link, nút chính, lỗi) | `#C24E3A` | `#EE8F7C` |
| Vàng hổ phách (cảnh báo, ô được chọn) | `#D9902A` | `#E8A53C` |
| Xanh lá (đạt) | `#2E7D32` | `#86D08F` |
| Khung đỏ chỗ lỗi trên ảnh | `#E5252A` | |
| Khung xanh chỗ đạt trên ảnh | `#1B8F3A` | |

Chế độ sáng/tối theo hệ điều hành, có nút đổi tay (nhớ trong trình duyệt). Giá trị thật nằm ở đầu `CSS_BASE` trong `theme.py`.

## Font

- Tiêu đề: **Fraunces** (có chân, đậm). Chữ thường: **Hanken Grotesk**. Cả hai dùng giấy phép SIL OFL (dùng tự do, được đưa vào repo).
- Font nằm sẵn trong repo ở `docs/thuong-hieu/fonts/` (10 file `.woff2` bản biến thiên, đủ tiếng Việt, khoảng 380 KB, kèm `fonts.json`), nên trang giống hệt trên mọi máy kể cả khi không có mạng. `theme.py` tự dùng chúng.
- Tải lại hoặc cập nhật: `python -X utf8 scripts/tai-font.py` (tải từ Google Fonts), rồi `python -X utf8 scripts/build_docs.py --all`. Chưa có `fonts.json` thì trang tạm lấy font từ Google Fonts (cần mạng).

## Logo

Đặt ảnh logo nền trong suốt tại `docs/thuong-hieu/logo-sunny-nhan-ra-nen-trong.png` (tạo từ logo gốc `logo-sunny-nhan-ra.png` bằng `python scripts/process_logo.py`). Có file thì logo được nhúng thẳng vào mọi trang; chưa có thì bỏ qua.

## Đổi giao diện

Sửa `theme.py` (hoặc `_CSS_DOC` trong `docs_pages.py` cho riêng trang tài liệu) rồi chạy `python -X utf8 scripts/build_docs.py --all`. Mọi trang được sinh lại cùng lúc nên không bao giờ lệch nhau.
