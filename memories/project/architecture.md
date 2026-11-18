# Kiến trúc tổng thể
Cập nhật: 2026-11-18 · Liên quan: [overview.md](overview.md), [skills.md](skills.md)

Repo không có ứng dụng; là bộ tài liệu kiểm thử + skill + bộ nhớ cho Claude. Công cụ duy nhất phải cài: Git, Python 3 (+ Pillow cho build báo cáo HTML).

## Thư mục
| Thư mục | Vai trò |
|---|---|
| `.claude/skills/` | 3 skill của dự án, mỗi skill có `SKILL.md`, `references/`, `assets/`, `scripts/` |
| `.claude/settings.json` | Quyền cho phép sẵn (sửa file trong các thư mục dự án, chạy script soát, git đọc). Commit/push/xóa vẫn hỏi |
| `memories/` | Bộ nhớ dự án, bản đồ ở `MEMORY.md` |
| `srs/` | Khuôn, quy tắc ID và SRS theo feature |
| `testing/` | Sản phẩm phân tích requirement (bảng soát, câu hỏi BA) |
| `evidence/` | Nhật ký khám phá, ảnh, báo cáo HTML |
| `docs/cai-dat-may-moi.md` | Hướng dẫn cài đặt máy mới |
| `scripts/kiem-tra-may-moi.py` | Kiểm máy mới (Python, Pillow, Git, `.env`, skill, quyền, chạy thử script soát) |
| `.env` / `.env.example` | Tài khoản test (không commit) / mẫu khóa để chép |

## Bẫy trên Windows
- Chạy Python luôn kèm `-X utf8` (tiếng Việt trong đầu ra).
- Heredoc qua Git Bash có thể làm méo `\\` trong regex: viết script ra tệp rồi chạy.
