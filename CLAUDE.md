# CLAUDE.md — build-sunny-agent-version-1

File này được đọc ĐẦU TIÊN trong mọi phiên làm việc. Ngôn ngữ trao đổi với người dùng: **tiếng Việt**.

## Quy trình bắt buộc khi nhận BẤT KỲ yêu cầu nào

0. **Xác định dự án đang làm** (repo chứa nhiều dự án, mỗi dự án là một hệ thống đang test): đọc file `.du-an-hien-tai` ở gốc repo (một dòng slug, không commit, mỗi máy một file).
   - **Chưa có file (máy mới):** hỏi người dùng đang làm dự án nào **trước khi làm bất cứ việc gì khác**, đưa danh sách dự án trong `memories/project/overview.md` và lựa chọn "dự án mới". Hỏi **riêng câu này**: chưa gộp câu hỏi khác, chưa đưa tài liệu hay feature của dự án nào làm lựa chọn khi người dùng chưa chọn dự án. Ghi slug vào `.du-an-hien-tai`. Dự án mới: làm theo `memories/conventions/nhieu-du-an.md` (có `scripts/tao-du-an.py`).
   - **Có file:** dùng luôn. Người dùng nhắc dự án khác → hỏi xác nhận đổi rồi ghi lại.
   - **Không dùng kiến thức của dự án khác** (quy tắc nghiệp vụ, tài khoản, dữ liệu test, từ ngữ, thông báo): chỉ đọc `memories/modules/<slug>/`, `srs/<slug>/`, `testing/<slug>/`, `evidence/<slug>/` của dự án hiện tại.
1. Đọc `CLAUDE.md` (file này).
2. Đọc `memories/MEMORY.md` — đây là **bản đồ**, chỉ cho biết file bộ nhớ nào chứa thông tin gì.
3. Dựa vào bản đồ, đọc **các file bộ nhớ liên quan** đến yêu cầu (phần chung + phần của dự án hiện tại, quyết định liên quan, sở thích của người dùng). Không đọc tràn lan, nhưng không được bỏ sót file mà bản đồ chỉ ra là liên quan. Việc dùng skill: đọc theo bảng "Đọc gì cho từng việc" trong `SKILL.md` của skill đó.
4. Thực hiện công việc.
5. Cập nhật bộ nhớ (xem mục dưới) trước khi kết thúc lượt làm việc.

Nếu bản đồ và thực tế code mâu thuẫn, tin code, rồi sửa lại bộ nhớ cho đúng.

Máy mới hoặc người dùng nhờ "kiểm tra máy mới": xem `docs/cai-dat-may-moi.md`, chạy `python -X utf8 scripts/kiem-tra-may-moi.py`.

## Quy tắc giảm token khi đọc file (MarkItDown)

- Word, PowerPoint, HTML, PDF chữ, hoặc nhiều file cần đọc cùng lúc: đổi sang Markdown trước rồi mới đọc, bằng `C:\Users\Admin\.venvs\markitdown\Scripts\python.exe -m markitdown <file> -o <thư-mục-tạm>\<tên>.md` (`python` thường không có markitdown; máy khác xem `memories/project/cong-cu-markitdown.md`).
- Ghi `.md` ra thư mục tạm, không để cạnh file gốc trong repo. Chỉ dùng với file/URL đã biết nguồn.
- Không dùng cho: `.txt`/`.md`; Excel lớn (dùng pandas); PDF scan hoặc nhiều hình/biểu đồ (đọc trực tiếp trang ảnh); việc cần sửa file mà giữ định dạng (sửa file gốc).

## Quy tắc bộ nhớ trong repo (`memories/`)

- Bộ nhớ lưu **trong chính repo này**, thư mục `memories/`, không lưu ở nơi khác.
- `memories/MEMORY.md` là file bản đồ bắt buộc phải có. Mỗi file bộ nhớ phải có đúng một dòng trong bản đồ.
- Chia nhỏ theo phần/module chức năng: **mỗi file một chủ đề**, mục tiêu dưới ~150 dòng. Vượt thì tách file hoặc tách thư mục con.
- Đặt tên thư mục/file rõ nghĩa, kebab-case, phản ánh đúng nội dung (ví dụ `modules/auth/session-handling.md`).
- Khi trao đổi hoặc khám phá hệ thống mà học được điều mới (kiến trúc, quyết định, quy ước, bẫy đã gặp, sở thích người dùng), ghi vào đúng file; chưa có thì tạo file mới và thêm vào `MEMORY.md`.
- Chỉ ghi điều **không thể suy ra nhanh từ code**: lý do thiết kế, ràng buộc, quyết định, điểm dễ sai. Không chép lại code.
- Chi tiết cách viết: `memories/conventions/memory-writing-rules.md`.
