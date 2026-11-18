# Truy vết requirement ↔ checklist/test case (`scripts/truy-vet.py`)
Đọc khi: requirement đổi, sửa checklist/test case, làm truy vết cho tính năng mới.

## Cách hoạt động
- Mỗi `testing/<dự-án>/<tính-năng>/` có: `truy-vet-cau-hinh.json` (đường dẫn SRS/bảng soát/checklist/test case, tiền tố mã, tên ngắn từng mã; thiếu tên ngắn thì lấy 40 ký tự đầu), `truy-vet-trang-thai.json` (mốc đã chốt, **script tự tạo, không sửa tay**), `truy-vet.md` (tự sinh: tra mã, requirement→TC, TC→requirement, lịch sử).
- `kiem`: so requirement hiện tại với mốc; mã đổi → TC dùng mã đó thành **Cần xem lại**; thoát mã 1 nếu có việc. `chot -m "..."`: ghi lịch sử + chốt mốc mới (người dùng quyết định khi chốt, sau khi sửa TC).
- Mã "đổi" = băm dòng của mã trong SRS (bỏ cột bằng chứng/nhãn) **hoặc** dòng TL/Suy ra trong bảng soát (băm riêng `ba_hash`). Đổi link/ngày không tính. Đã thử: đổi TL-11 → S02-AC07 thì TC-014, 015, 037 bị bắt.
- Khối "Lịch sử thay đổi" cuối checklist/test case nằm giữa `<!-- LICH-SU:… -->`, script tự ghi đè, đừng sửa tay.
- Script cũng báo: checklist và test case lệch mã TC/mã nguồn; mã dùng ở TC mà không có trong SRS/bảng soát; mã SRS chưa có TC.
- Đọc bảng checklist/test case **theo tên cột** (bảng đầu có tiêu đề bắt đầu `| Mã |`), `Nguồn` bất kỳ vị trí. Dấu vết `row` bỏ 4 cột `Kết quả thực tế`, `Trạng thái`, `Người viết`, `Tự động hóa`. Mục 6 `truy-vet.md` có cột Tự động hóa, báo "script cần xem lại" khi TC Cần xem lại mà đã có script. Test case có `Ưu tiên` khác checklist → báo vấn đề. Đổi cấu trúc bảng làm `row_hash` đổi cả 41 TC → `chot` mô tả "đổi cấu trúc bảng, nội dung không đổi" (đã làm 2026-11-18 16:09).
- Mục 4 `truy-vet.md` gom từ bảng soát cho từng mã SRS: "Theo BA (hoặc suy ra)", "Hệ thống 1.3.0 hiện tại", "Còn mở". Parser đọc theo chuỗi trạng thái ("theo TL", "Suy ra", "hành vi hiện tại", ❓): đổi cách viết trạng thái thì sửa `parse_ba` trong script.

## Lệnh `tra` (chỉ đọc, 2026-11-18)
- `truy-vet.py tra <dự-án> <tính-năng> --ma S02-AC07,R06,TL-11,TC-014 [--day-du]`: in gọn SRS (theo tên cột), theo BA/hiện tại/còn mở, TL liên quan, TC + trạng thái. Thay cho đọc cả SRS + bảng soát + `test-case.md` (~190 KB LOGIN) bằng 1–7 KB. Không ghi file (khác `kiem`/`chot`). Nhận mã có tiền tố và `TC-14`. Đối chiếu 52 mã LOGIN: danh sách TC khớp đúng mục 5 của `truy-vet.md`.
- Bẫy: chạy `kiem` để thử cũng **ghi lại** `truy-vet.md`, checklist, test case (giờ chạy) → `git checkout` các file đó nếu chỉ thử.

## Lịch sử có giờ
- `chot` ghi `thoi_diem` (giờ máy + múi giờ), `commit_goc` (HEAD lúc chốt), `chua_commit`, `--ngay-ba` (nếu biết). Mốc cũ chỉ có ngày → "không rõ giờ", **không bịa giờ**. Giờ chốt ≠ giờ BA trả lời ≠ giờ requirement đổi. Muốn truy từng chữ thì dùng git; sau `chot` nên commit (chỉ khi người dùng nhờ). Quy ước: `srs/id-and-source-rules.md` 2c.

## SRS theo BA (hướng C đã làm 2026-11-18)
- Sau khi BA xác nhận TL-01…13: giữ ID; cột phản hồi → "Yêu cầu"; thêm cột "Hệ thống 1.3.0 hiện tại" (chữ quan sát cũ, `Khớp yêu cầu`/`⚠️ Khác yêu cầu`); nhãn `đã xác nhận (BA, ngày, TL-xx)`; mục BA bỏ giữ dòng `đã bỏ`. Quy tắc 2b trong `srs/id-and-source-rules.md`. Trích nguyên văn bảng soát vẫn khớp SRS mới (83/83). Khi có ticket thì thêm link vào cột Nguồn của TL.

## Link từ SRS tới câu trả lời và câu hỏi BA
- Mọi `TL-xx`, `B4`, `B8` trong SRS là link tới điểm nhảy `<a id="tl-11">` (ô cuối dòng TL trong bảng soát) và `<a id="b4">` (trước tiêu đề câu hỏi trong `cau-hoi-cho-ba.md`, 24 câu). Điểm nhảy ở ô không bị băm nên không làm TC bị đánh dấu; **không** đặt trong ô mã/nội dung của dòng TL (script đọc `^| TL-xx |`, băm hai ô đầu). Thêm TL/câu hỏi mới → thêm điểm nhảy + link; kiểm bằng script so link với điểm nhảy (62 link, 0 hỏng).

## Smoke test truy vết (`scripts/truy-vet-smoke.py`, 2026-11-18)
- Quy trình chọn case smoke nằm ở skill `tao-smoke-test`; phần này chỉ ghi cơ chế truy vết. **Chỉ MỘT file smoke** (`testing/<dự-án>/smoke-test.md`, người dùng chốt: "chỉ 1 file, cập nhật, không tạo nhiều file"). Mốc nằm trong file (một dòng chú thích `<!-- SMOKE-MOC: {json} -->`), lịch sử là bảng trong file, không có file trạng thái. Cột "Mã case gốc" là link markdown tới `<thư-mục>/test-case.md#tc-005` (script đọc link để biết tính năng + TC).
- **Mục đích smoke trước thời gian** (người dùng chốt): thời gian chỉ là mục tiêu tham khảo, script chỉ "lưu ý" khi vượt, không lỗi, không chặn `chot`; không cắt case cần cho mục đích vì thời gian.
- **Tiết kiệm token:** kiểm smoke bằng `kiem` (CHỈ ĐỌC, in ~5 dòng), **không đọc cả smoke-test.md** (~15 KB). Chỉ `chot` mới ghi file (mục Truy vết, dòng lịch sử, mốc, "Cập nhật lần cuối"). `kiem` báo: Còn đúng / Cần xem lại (mã requirement của TC gốc đổi so với mốc) / Test case đã sửa / Test case không còn; cũng báo TC trùng, link hỏng, cột Phần sai. Dùng hàm băm của `truy-vet.py`. Đã thử giả lập đổi mốc → bắt đúng. Chốt smoke **sau** khi chốt truy vết tính năng.
- **Neo dòng test case**: ô Mã của `test-case.md` là `<a id="tc-005"></a>TC-005` (id không tiền tố vì link kèm đường dẫn file). `truy-vet.py`, `kiem-tra-tc.py`, `sinh-bang.py` chấp nhận neo; `sinh-bang.py` tự ghi khi sinh bảng `gop`/`test-case` (lệnh `checklist` chưa ghi, chưa chạy thử sinh lại trên bảng thật). Đã thêm neo cho 43 TC LOGIN + 38 TC RECO; hash không đổi.
- `truy-vet.py kiem/chot` in thêm một dòng nhắc chạy `truy-vet-smoke.py kiem` khi smoke có link tới tính năng đó (chỉ khi `chot`, có mã đổi hoặc TC không "Còn đúng"). `kiem` của smoke chỉ lưu ý (không lỗi) với: ⚠️, nhập sai N lần, tác dụng phụ, nguồn nháp, case chưa chạy thật, dòng `Case mới`/`Ngoài repo: …` (không truy vết được).
- `truy-vet-smoke.py ghi-luot` chỉ ghi khối `LUOT-CHAY` (không đụng mốc/lịch sử); đã thử 13 tình huống (Nhận/Trả/Chưa kết luận, đầu vào sai, ghi chú có `|`), file thật khôi phục nguyên. Muốn xem lượt gần nhất thì `kiem`, không đọc cả file.
- Case mới (chưa có TC gốc) chưa truy vết được bằng script: viết TC gốc trước rồi link. SRS LOGIN chưa có neo theo mã nên bảng truy vết chỉ link mã RECO và TL của LOGIN.
- Bài học: lệnh Bash gộp có `git checkout --` trên file tracked bị trình phân loại chặn cả lệnh; thử thay đổi giả lập bằng cách sửa mốc của chính mình (sao lưu trước). Heredoc Python dài dễ lỗi cú pháp bash: viết script vào file (Write) rồi chạy.

## Bẫy
- TC thêm sau khi requirement đổi lấy số kế tiếp nên xếp cuối bảng, trái luật "Cao trước": khai báo dòng `| Dòng thêm sau khi requirement đổi | TC-042, TC-043 (…) |` ở bảng đầu checklist để `kiem-tra-tc.py` bỏ qua khi kiểm thứ tự (làm 2026-11-18). Phải hỏi người dùng trước khi thêm TC mới.
- Sửa script qua heredoc Bash/Python: `\n` thành xuống dòng thật làm vỡ chuỗi. Dùng Edit hoặc `chr(92)+"n"`; sau sửa chạy `ast.parse`.
- Cột Nguồn của TC phải ghi đúng mã (`S02-AC07`, `R06`, `M05`, `TL-11`); mã trong giải thích ngoặc cũng bị tính là nguồn.
- Script chỉ ghi mã nào đổi, không ghi nội dung cũ.
- Tính năng mới: copy `truy-vet-cau-hinh.json`, đổi đường dẫn/tiền tố/tên ngắn; SRS phải theo khuôn mã `` `PREFIX-S01-AC01` ``. Chạy `kiem` rồi `chot` lần đầu.
