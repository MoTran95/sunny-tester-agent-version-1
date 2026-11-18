# Tổng quan repo
Cập nhật: 2026-11-18

- Repo `build-sunny-agent-version-1` (`D:\AI\build-sunny-agent-version-1`, Windows 11), đã push lên GitHub ([git-remote.md](git-remote.md)).
- Là chỗ làm việc của **tester** cho **nhiều dự án** (mỗi dự án là một hệ thống đang test). Phần dùng chung: 3 skill trong `.claude/skills/` ([skills.md](skills.md)), khuôn trong `srs/_template.md`, `srs/id-and-source-rules.md`, bộ nhớ chung trong `memories/` (trừ `memories/modules/`).
- Mỗi dự án có thư mục riêng trong `memories/modules/<slug>/`, `srs/<slug>/`, `testing/<slug>/`, `evidence/<slug>/`. **Không dùng kiến thức của dự án này cho dự án khác.** Quy tắc chọn dự án và tạo dự án mới: [../conventions/nhieu-du-an.md](../conventions/nhieu-du-an.md).

## Các dự án
| Slug | Tên | Tổng quan |
|---|---|---|
| `banking-lite` | Banking Lite — Vay mua nhà | [../modules/banking-lite/overview.md](../modules/banking-lite/overview.md) |

Thêm dòng khi tạo dự án mới (script `scripts/tao-du-an.py` tự thêm).
