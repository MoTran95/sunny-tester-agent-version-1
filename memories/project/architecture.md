# Cấu trúc repo
Đọc khi: thêm thư mục, đổi quyền, làm máy mới. Repo không có ứng dụng: bộ tài liệu kiểm thử + skill + memory. Cần cài: Git, Python 3 (+ Pillow cho build báo cáo HTML).

| Đường dẫn | Vai trò |
|---|---|
| `.claude/skills/` | 4 skill (`SKILL.md`, `references/`, `assets/`, `scripts/`) |
| `.claude/settings.json` | Quyền cho phép sẵn (Edit trong thư mục dự án, chạy script soát, git đọc). Commit/push/xóa vẫn hỏi |
| `memories/` | Bộ nhớ cho AI, bản đồ `MEMORY.md` |
| `srs/` `testing/` `evidence/` | SRS; bảng soát/câu hỏi/checklist/test case/truy vết; khám phá + ảnh + báo cáo HTML (mỗi dự án có thư mục con `<slug>`) |
| `docs/cai-dat-may-moi.md`, `docs/kiem-thu-cac-thay-doi.md` | Cài máy mới; kịch bản kiểm thử T1–T7 |
| `scripts/kiem-tra-may-moi.py` | Kiểm máy mới (Python, Pillow, Git, dự án, `.env`, skill, quyền, chạy thử script soát) |
| `scripts/do-toc-do-phien.py` | Đo phiên gần nhất từ nhật ký: ngữ cảnh đầu, file đọc, phút tới lúc làm, mở dự án khác |
| `scripts/kiem-tra-bo-nho.py` | Kiểm memory: mọi file có trong bản đồ, link không gãy, in cỡ |
| `scripts/tao-du-an.py` | Tạo thư mục dự án mới |
| `scripts/truy-vet.py` | Truy vết requirement ↔ TC (`kiem`/`chot`); cần `testing/<dự-án>/<tính-năng>/truy-vet-cau-hinh.json` |
| `.du-an-hien-tai`, `.env` / `.env.example` | Dự án đang làm; tài khoản test (không commit) / mẫu khóa |

Bẫy Windows: chạy Python kèm `-X utf8`; heredoc Git Bash làm méo `\\` trong regex → viết script ra file rồi chạy.
