# Nhật ký quyết định
Cập nhật: 2026-11-18

Mỗi quyết định một mục, mới nhất ở trên. Khi file quá dài, tách theo năm/chủ đề.

## 2026-11-18 — Repo nhiều dự án, mỗi máy chọn một dự án
- **Quyết định:** máy mới (chưa có `.du-an-hien-tai`) thì hỏi đang làm dự án nào trước mọi việc, ghi slug vào `.du-an-hien-tai` (không commit). Dự án mới tạo thư mục theo cấu trúc hiện có (`scripts/tao-du-an.py`). Kiến thức riêng của Banking Lite tách khỏi phần chung: tổng quan sang `memories/modules/banking-lite/overview.md`, từ ngữ với BA sang `memories/modules/banking-lite/tu-ngu-cau-hoi-ba.md`; skill không mở file của dự án khác kể cả làm mẫu. Chi tiết: [../conventions/nhieu-du-an.md](../conventions/nhieu-du-an.md).
- **Lý do:** người dùng yêu cầu, để không lẫn kiến thức Banking Lite sang dự án khác.
- **Phương án đã loại (người dùng chọn):** hỏi ở mọi phiên mới (phải trả lời nhiều lần); gom mỗi dự án vào `du-an/<tên>/` (phải dời toàn bộ Banking Lite).

## 2026-11-18 — Skill ghi rõ file cần đọc; quyền cho phép sẵn cho máy mới
- **Quyết định:** mỗi `SKILL.md` có bảng "Đọc gì cho từng việc" thay cho bước "đọc bộ nhớ liên quan" chung chung. `.claude/settings.json` (commit theo repo) cho phép sẵn: `Edit` trong `memories/`, `srs/`, `testing/`, `evidence/`, `docs/`, `.claude/skills/`, `CLAUDE.md`; chạy script trong `.claude/skills/` và `scripts/kiem-tra-may-moi.py`; `git status/diff/log/show`.
- **Lý do:** người dùng nhờ (2026-11-18) để phiên đầu trên máy mới không mất ~30 phút.
- **Phương án đã loại:** cho phép sẵn `git commit`/`git push`/xóa file (người dùng muốn commit/push chỉ khi được nhờ); cho phép sửa `.claude/settings.json` (tự nới quyền).

## 2026-11-18 — Bộ nhớ luôn đọc chỉ giữ phần cốt lõi
- **Quyết định:** chỉ `user/working-preferences.md` và `project/overview.md` là luôn đọc. `working-preferences.md` giữ quy tắc cốt lõi mỗi ý một dòng; chi tiết về cách viết tài liệu sang `user/document-preferences.md`. `MEMORY.md` mỗi dòng một câu ngắn, không ghi nhật ký cập nhật, sản phẩm trong `testing/` gom một mục.
- **Lý do:** người dùng duyệt "Làm gọn bộ nhớ" sau khi đo thấy phần luôn đọc dày và lặp ý ([../project/session-speed.md](../project/session-speed.md)).
- **Phương án đã loại:** xóa bớt bài học (có thể mất điều người dùng đã dặn) — chỉ chuyển chỗ.

## 2026-11-18 — Bảng soát không chép lại nội dung câu hỏi
- **Quyết định:** cột "Câu hỏi gửi BA" chỉ ghi `**A1. <tiêu đề>** (<nhóm>)`, cộng `**BA trả lời:** <nguyên văn> (TL-xx)` khi đã có trả lời (người dùng yêu cầu ghi câu BA trả lời vào cột này, 2026-11-18). Bỏ phần chép Hỏi/Mình đang hiểu/Cần xem. Đã chuyển cả hai bảng `LOGIN` (84→63 KB) và `RECO` (67→48 KB), không đổi trạng thái dòng nào. `kiem-tra.py` kiểm tiêu đề + nhóm khớp, báo lỗi nếu chép lại, có `--tim` để tìm dòng cần sửa.
- **Lý do:** người dùng duyệt "Làm gọn bảng soát" sau khi đo thấy phiên chậm vì bảng quá lớn ([../project/session-speed.md](../project/session-speed.md)).
- **Phương án đã loại:** chỉ để mã câu hỏi trần (người dùng từng chê mã nội bộ); bỏ luôn câu BA trả lời khỏi cột (trái yêu cầu của người dùng); thêm thẻ neo `<a id>` vào file câu hỏi (file gửi BA, không chắc khung xem trước hiểu).

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
