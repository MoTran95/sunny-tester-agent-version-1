# Truy vết requirement ↔ checklist/test case
Cập nhật: 2026-11-18 · Liên quan: [architecture.md](architecture.md), [../modules/banking-lite/feature-dang-nhap.md](../modules/banking-lite/feature-dang-nhap.md)

Người dùng hỏi (2026-11-18): khi requirement đổi thì làm sao biết sửa đúng test case nào, có lưu lịch sử tạo/cập nhật không. Lời giải: `scripts/truy-vet.py`.

## Cách hoạt động
- Thư mục `testing/<dự-án>/<tính-năng>/` có `truy-vet-cau-hinh.json` (đường dẫn SRS, bảng soát, checklist, test case, tiền tố mã, tên ngắn từng mã), `truy-vet-trang-thai.json` (mốc đã chốt, **script tự tạo, không sửa tay**), `truy-vet.md` (tự sinh: bảng tra mã, requirement→TC, TC→requirement, lịch sử).
- `kiem`: so requirement hiện tại với mốc; mã nào đổi thì TC dùng mã đó thành **Cần xem lại**; thoát mã 1 nếu có việc. `chot -m "..."`: ghi lịch sử, chốt mốc mới (người dùng quyết định khi nào chốt, sau khi sửa TC).
- Mã "đổi" = băm dòng của mã trong SRS (bỏ cột bằng chứng/nhãn) hoặc dòng TL trong bảng soát (mã + nội dung trả lời). Đổi link/ngày không bị tính.
- Khối "Lịch sử thay đổi" ở cuối checklist và test case nằm giữa hai dấu `<!-- LICH-SU:… -->`, script tự ghi đè; đừng sửa tay trong khối đó.
- Script kiểm cả: checklist và test case lệch mã TC hoặc mã nguồn; mã dùng ở TC mà không có trong SRS/bảng soát; mã SRS chưa có TC.

## Yêu cầu theo BA gắn với mã SRS (làm 2026-11-18, hướng "B")
- Người dùng hỏi nên để mã TL thế nào; chọn **B**: không sửa SRS, `truy-vet.md` mục 4 gom từ bảng soát (mục 5, 6) cho từng mã SRS: "Theo BA (hoặc suy ra)", "Hệ thống 1.3.0 hiện tại", "Còn mở". Test case viết theo cột Theo BA.
- Phần theo BA tính vào phát hiện thay đổi (băm riêng `ba_hash`): sửa dòng "theo TL"/"Suy ra" của một mã trong bảng soát thì TC dùng mã đó thành Cần xem lại. Đã thử: đổi TL-11 → S02-AC07 và TC-014, 015, 037 bị bắt.
- Hướng **C** (sửa SRS cho khớp BA) **hoãn tới khi có ticket/BA xác nhận bằng văn bản**. Rủi ro đã nêu với người dùng: mất hồ sơ quan sát, TL-12/13 chỉ là suy ra, trích dẫn trong bảng soát không còn khớp SRS, mã bị bỏ (M03, M04, S03-AC02) phải giữ mã và đánh dấu "Đã bỏ theo BA", script báo nhiễu. Cần commit trước khi làm C.
- Parser đọc bảng soát theo chuỗi trạng thái ("theo TL", "Suy ra", "hành vi hiện tại", ❓); đổi cách viết trạng thái thì phải sửa `parse_ba` trong script.

## Bẫy
- Tên ngắn nằm trong `truy-vet-cau-hinh.json`; thêm mã mới vào SRS thì thêm tên ngắn (không có thì script lấy 40 ký tự đầu).
- Cột Nguồn của TC phải ghi đúng mã (`S02-AC07`, `R06`, `M05`, `TL-11`); script dò mã bằng regex trong cột đó. Mã nằm trong phần giải thích trong ngoặc cũng bị tính là nguồn.
- Muốn thấy từng chữ đã đổi thì cần **commit** sau mỗi lần chốt (git giữ lịch sử); script chỉ ghi mã nào đổi, không ghi nội dung cũ. Commit chỉ khi người dùng nhờ.
- Tính năng mới: copy `truy-vet-cau-hinh.json`, đổi đường dẫn/tiền tố/tên ngắn; SRS phải theo khuôn có mã dạng `` `PREFIX-S01-AC01` ``. Chạy `kiem` rồi `chot` lần đầu.
