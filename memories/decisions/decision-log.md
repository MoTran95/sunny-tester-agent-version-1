# Nhật ký quyết định
Cập nhật: 2026-11-17

Mỗi quyết định một mục, mới nhất ở trên. Khi file quá dài, tách theo năm/chủ đề.

## 2026-11-17 — SRS dùng Story + AC, ID thống nhất, truy nguồn có liên kết
- **Quyết định:** thân SRS = story + luồng + AC (cột Tình huống / Bối cảnh / Người dùng làm / Hệ thống phản hồi — bỏ tên cột Cho trước/Khi/Thì vì người dùng không hiểu); quy tắc dữ liệu và thông báo chỉ là bảng tra cứu phụ; ID `<FEATURE>-S01-AC01` / `-R` / `-M` / `-Q` / `-E`, mã feature tiếng Anh ngắn; bằng chứng có bảng riêng với liên kết tệp + cách kiểm lại. Chi tiết: `srs/id-and-source-rules.md`. Khám phá phải đầy đủ, chỉ tránh đổi dữ liệu người khác/khóa hệ thống.
- **Lý do:** người dùng không truy được nguồn dạng `NK#n/DN-NN/BC-NN`; cần ID để sau này gắn test case; bảng FR/BR/thông báo tách rời khó đọc; việc chừa trống do ngại rủi ro làm SRS thiếu.
- **Phương án đã loại:** khuôn v1 (FR/BR/bảng thông báo tách riêng, nguồn viết tắt); gộp hết thông báo vào từng AC (chép lặp).

## 2026-11-17 — Làm từng bước nhỏ: khám phá → SRS (Markdown), thử trên Đăng nhập
- **Quyết định:** chỉ làm bước “khám phá → SRS”; SRS sửa tại chỗ (có Lịch sử thay đổi), khám phá/ảnh tạo mới theo ngày; SRS ghi hành vi quan sát được với nhãn đã thấy/chưa rõ; lưu Markdown trong repo; bug nháp MD trước, Jira sau; pilot = Đăng nhập. Chi tiết: [../project/srs-process.md](../project/srs-process.md).
- **Lý do:** người dùng thấy chuỗi 11 giai đoạn “chưa đúng lắm”, làm hết một lúc thì sai phải sửa nhiều; muốn ghép dần để thử nghiệm.
- **Phương án đã loại:** kế hoạch 11 giai đoạn + cây thư mục `qa/…` + nhiều skill `sot-*` (bỏ, có thể xét lại từng phần sau); SRS mới mỗi lần cập nhật (nhiều bản song song, test case mất chỗ bám).

## 2026-11-17 — Bộ nhớ lưu trong repo tại `memories/`
- **Quyết định:** dùng `memories/` trong repo, `MEMORY.md` là bản đồ, chia nhỏ theo module, `CLAUDE.md` bắt buộc đọc bộ nhớ trước khi làm.
- **Lý do:** người dùng muốn ngữ cảnh bền vững, không bị sót, không phình to.

<!-- Mẫu:
## YYYY-MM-DD — Tiêu đề
- **Quyết định:** ...
- **Lý do:** ...
- **Phương án đã loại:** ...
-->
