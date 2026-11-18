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
- Hướng **C** (sửa SRS cho khớp BA) **đã làm 2026-11-18** sau khi người dùng báo BA xác nhận đúng TL-01…TL-13 (chưa có ticket/link). Mốc trước khi sửa: commit `46feb45`. Cách làm: giữ ID; cột phản hồi → "Yêu cầu"; thêm cột "Hệ thống 1.3.0 hiện tại" (giữ nguyên chữ quan sát cũ, `Khớp yêu cầu`/`⚠️ Khác yêu cầu`); nhãn `đã xác nhận (BA, ngày, TL-xx)`; mục BA bỏ giữ dòng nhãn `đã bỏ` (S03-AC02, M02, M03, M04). Ghi thành quy tắc 2b trong `srs/id-and-source-rules.md`. Trích nguyên văn của bảng soát vẫn khớp SRS mới (83/83) nhờ giữ chữ cũ ở cột hiện tại; kiểm bằng script so chuỗi. TL-12, TL-13 chuyển từ "suy ra" sang BA xác nhận ở bảng soát và 3 TC (012, 013, 022). Vẫn mở: B4 (câu báo khi nhập lúc đang bị chặn), B8 (thời hạn phiên). Khi có ticket thì thêm link vào cột Nguồn của các TL.
- Parser đọc bảng soát theo chuỗi trạng thái ("theo TL", "Suy ra", "hành vi hiện tại", ❓); đổi cách viết trạng thái thì phải sửa `parse_ba` trong script.

## Thời điểm trong lịch sử (2026-11-18)
Người dùng muốn lịch sử ghi tới giờ phút giây. `chot` ghi `thoi_diem` (giờ máy + múi giờ), `commit_goc` (HEAD lúc chốt), `chua_commit` (còn sửa chưa commit), `--ngay-ba` (ngày BA trả lời, nếu biết). Mốc cũ chỉ có ngày thì hiện "không rõ giờ", **không bịa giờ**. Giờ chốt ≠ giờ BA trả lời ≠ giờ requirement đổi; muốn trace từng chữ thì dùng commit (git giữ giờ thật). Sau `chot` nên commit ngay để commit gốc có nghĩa. Quy ước ghi ở `srs/id-and-source-rules.md` 2c.

## Link từ SRS tới câu trả lời và câu hỏi BA (2026-11-18)
Trong SRS mọi `TL-xx`, `B4`, `B8` là link bấm được tới điểm nhảy `<a id="tl-11">` (ô cuối dòng TL trong bảng soát) và `<a id="b4">` (trước mỗi tiêu đề câu hỏi trong `cau-hoi-cho-ba.md`, 24 câu A/B/C). Điểm nhảy đặt ở ô không bị băm nên không làm test case bị đánh dấu. Thêm TL mới hoặc câu hỏi mới thì thêm điểm nhảy tương ứng và link ở SRS; kiểm bằng script so link với điểm nhảy (62 link, 0 hỏng lúc làm). Không đặt điểm nhảy trong ô mã hoặc ô nội dung của dòng TL (script đọc `^| TL-xx |` và băm hai ô đầu).

## Bảng test case nhiều cột, đọc theo tên (11 cột 2026-11-18, nay 12 cột)
`truy-vet.py` đọc bảng checklist/test case **theo tên cột** (bảng đầu có tiêu đề bắt đầu `| Mã |`), cột `Nguồn` bất kỳ vị trí. Dấu vết `row` bỏ bốn cột `Kết quả thực tế`, `Trạng thái`, `Người viết`, `Tự động hóa`; mục 6 của `truy-vet.md` có cột Tự động hóa và báo "script cần xem lại" khi TC Cần xem lại mà đã có script (đã thử). Nếu test case có cột `Ưu tiên` mà khác checklist thì báo vấn đề. Đổi cấu trúc bảng làm `row_hash` đổi cho cả 41 TC → `chot` với mô tả "đổi cấu trúc bảng, nội dung không đổi" (đã làm 2026-11-18 16:09).

## Bẫy
- **Sửa script qua heredoc Bash/Python:** `\n` trong mã bị biến thành xuống dòng thật làm vỡ chuỗi (đã gặp 2026-11-18). Dùng công cụ Edit, hoặc viết `chr(92)+"n"`; sau khi sửa luôn chạy `ast.parse` kiểm cú pháp.
- Tên ngắn nằm trong `truy-vet-cau-hinh.json`; thêm mã mới vào SRS thì thêm tên ngắn (không có thì script lấy 40 ký tự đầu).
- Cột Nguồn của TC phải ghi đúng mã (`S02-AC07`, `R06`, `M05`, `TL-11`); script dò mã bằng regex trong cột đó. Mã nằm trong phần giải thích trong ngoặc cũng bị tính là nguồn.
- Muốn thấy từng chữ đã đổi thì cần **commit** sau mỗi lần chốt (git giữ lịch sử); script chỉ ghi mã nào đổi, không ghi nội dung cũ. Commit chỉ khi người dùng nhờ.
- Tính năng mới: copy `truy-vet-cau-hinh.json`, đổi đường dẫn/tiền tố/tên ngắn; SRS phải theo khuôn có mã dạng `` `PREFIX-S01-AC01` ``. Chạy `kiem` rồi `chot` lần đầu.
