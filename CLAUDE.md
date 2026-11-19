# CLAUDE.md — build-sunny-agent-version-1

Đọc ĐẦU TIÊN mọi phiên. Trao đổi với người dùng bằng **tiếng Việt**.

## Quy trình bắt buộc với MỌI yêu cầu

0. **Dự án đang làm** (repo nhiều dự án, mỗi dự án là một hệ thống đang test): đọc `.du-an-hien-tai` ở gốc repo (một dòng slug, không commit, mỗi máy một file).
   - **Chưa có file (máy mới):** hỏi dự án nào **trước mọi việc khác**, **riêng câu này** (không gộp câu khác, không đưa tài liệu/feature của dự án nào làm lựa chọn khi chưa chọn dự án); liệt kê dự án trong `memories/project/overview.md` + "dự án mới". Ghi slug vào file. Dự án mới: `memories/conventions/nhieu-du-an.md` (`scripts/tao-du-an.py`).
   - **Có file:** dùng luôn; người dùng nhắc dự án khác → hỏi xác nhận đổi rồi ghi lại.
   - **Không dùng kiến thức dự án khác** (nghiệp vụ, tài khoản, dữ liệu test, từ ngữ, thông báo): chỉ đọc `memories/modules/<slug>/`, `srs/<slug>/`, `testing/<slug>/`, `evidence/<slug>/` của dự án hiện tại.
1. Đọc `CLAUDE.md` (file này).
2. Đọc `memories/MEMORY.md` — **bảng** `File | Khi | Chứa` cho AI. Chỉ 2 file ★ luôn đọc (`user/working-preferences.md`, `project/overview.md`).
3. Mở **chỉ các file có cột "Khi" khớp việc** (phần chung + dự án hiện tại); không bỏ sót file bản đồ chỉ là liên quan, không đọc tràn lan. Dùng skill: đọc theo bảng "Đọc gì cho từng việc" trong `SKILL.md`.
4. Làm việc. 5. Cập nhật memory trước khi kết thúc lượt, rồi `python -X utf8 scripts/kiem-tra-bo-nho.py`. Nếu lượt này sửa file md của `srs/`, `testing/` hoặc `evidence/`: chạy thêm `python -X utf8 scripts/build_docs.py` để sinh lại trang HTML và trang tổng (`--check` chỉ báo trang cũ).

Bản đồ mâu thuẫn code → tin code, sửa memory. Máy mới / "kiểm tra máy mới": `docs/cai-dat-may-moi.md`, `python -X utf8 scripts/kiem-tra-may-moi.py`. Phiên than nặng: nạp sẵn ~74 nghìn token, phần plugin tài khoản chỉ ~3–6%, không tắt được từ repo (`memories/project/session-speed.md`, `memories/user/connectors-and-plugins.md`).

## Giảm token khi đọc file (MarkItDown)
Word, PowerPoint, HTML, PDF chữ hoặc nhiều file → đổi sang Markdown trước: `C:\Users\Admin\.venvs\markitdown\Scripts\python.exe -m markitdown <file> -o <thư-mục-tạm>\<tên>.md` (ra thư mục tạm, chỉ file/URL đã biết nguồn). Không dùng cho `.txt`/`.md`, Excel lớn (pandas), PDF scan/nhiều hình, việc sửa file giữ định dạng. Máy khác: `memories/project/cong-cu-markitdown.md`.

## Memory (`memories/`) chỉ cho AI đọc
- Viết **ngắn, bảng/gạch đầu dòng**; một file một chủ đề; chỉ điều **không suy ra nhanh từ code/SRS** (lý do, ràng buộc, quyết định, bẫy, sở thích người dùng). Không chép lại code hay nội dung đã có ở `srs/`, `testing/`, `evidence/`.
- Tài liệu cho **người đọc** (`srs/`, `testing/`, `evidence/`, `docs/`, báo cáo HTML) vẫn viết đầy đủ, đọc là hiểu.
- Thêm/đổi tên/xóa file memory → sửa bảng trong `MEMORY.md` cùng lượt. Chi tiết: `memories/conventions/memory-writing-rules.md`.
