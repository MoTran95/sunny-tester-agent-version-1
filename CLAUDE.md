# CLAUDE.md — build-sunny-agent-version-1

File này được đọc ĐẦU TIÊN trong mọi phiên làm việc. Ngôn ngữ trao đổi với người dùng: **tiếng Việt**.

## Quy trình bắt buộc khi nhận BẤT KỲ yêu cầu nào

1. Đọc `CLAUDE.md` (file này).
2. Đọc `memories/MEMORY.md` — đây là **bản đồ**, chỉ cho biết file bộ nhớ nào chứa thông tin gì.
3. Dựa vào bản đồ, đọc **các file bộ nhớ liên quan** đến yêu cầu (module sẽ đụng tới, quyết định liên quan, sở thích của người dùng). Không đọc tràn lan, nhưng không được bỏ sót file mà bản đồ chỉ ra là liên quan.
4. Thực hiện công việc.
5. Cập nhật bộ nhớ (xem mục dưới) trước khi kết thúc lượt làm việc.

Nếu bản đồ và thực tế code mâu thuẫn, tin code, rồi sửa lại bộ nhớ cho đúng.

## Quy tắc bộ nhớ trong repo (`memories/`)

- Bộ nhớ lưu **trong chính repo này**, thư mục `memories/`, không lưu ở nơi khác.
- `memories/MEMORY.md` là file bản đồ bắt buộc phải có. Mỗi file bộ nhớ phải có đúng một dòng trong bản đồ.
- Chia nhỏ theo phần/module chức năng: **mỗi file một chủ đề**, mục tiêu dưới ~150 dòng. Vượt thì tách file hoặc tách thư mục con.
- Đặt tên thư mục/file rõ nghĩa, kebab-case, phản ánh đúng nội dung (ví dụ `modules/auth/session-handling.md`).
- Khi trao đổi hoặc khám phá hệ thống mà học được điều mới (kiến trúc, quyết định, quy ước, bẫy đã gặp, sở thích người dùng), ghi vào đúng file; chưa có thì tạo file mới và thêm vào `MEMORY.md`.
- Chỉ ghi điều **không thể suy ra nhanh từ code**: lý do thiết kế, ràng buộc, quyết định, điểm dễ sai. Không chép lại code.
- Chi tiết cách viết: `memories/conventions/memory-writing-rules.md`.
