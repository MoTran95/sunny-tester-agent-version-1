# Connector/plugin: mặc định tắt, hỏi trước khi bật
Đọc khi: việc cần connector/plugin; người dùng than chậm/tốn token.

- Yêu cầu của người dùng (2026-11-18): tắt thứ không dùng cho kiểm thử; **chỉ bật khi người dùng yêu cầu hoặc thật cần, và hỏi trước**.
- Notion, Claude Docs đã tắt; bật bằng `set_session_connector_enabled` sau khi người dùng đồng ý (có tác dụng từ lượt sau). Cần Notion: cập nhật trang hành trình/feedback; cần Docs: tạo doc chia sẻ. Kiểm thử bằng skill repo + trình duyệt có sẵn + script Python không cần cái nào.
- Plugin `data` (Amplitude, BigQuery, Hex…), skill `assp-*`, `kundalini-yoga-translator`, `flipbook-builder` gắn với tài khoản claude.ai; app gắn theo cách riêng. **Không tắt được từ repo** (đã đo 2026-11-18, mỗi lần mở phiên mới đo ctx đầu bằng `do-toc-do-phien.py`):
  - `syncClaudeAiPlugins=false` + `disableClaudeAiConnectors=true` trong `.claude/settings.local.json` → phiên mới vẫn 74,4 nghìn token, đủ 57 skill + 118 công cụ.
  - Thêm 23 `permissions.deny` `Skill(assp-…:assp-…)`, `Skill(data:…)`, kundalini, flipbook → vẫn 74,5 nghìn, danh sách skill không đổi.
  - Tài liệu Claude Code: `skillOverrides` không áp dụng cho skill của plugin; `enabledPlugins` cần tên marketplace (không xác định được). Không sửa dữ liệu app `%LOCALAPPDATA%\Claude-Data` (app cấm).
  - Script `gon-phien.py` (tat/bat các khóa trên) chạy đúng chức năng nhưng vô tác dụng với app desktop → đã xóa 2026-11-18. Đừng viết lại; chỉ thử lại nếu app/CLI đổi, bằng cách đo ctx đầu phiên mới.
- Tắt tay trong app chỉ đáng khoảng **2–5 nghìn token** (~3–6%): skill plugin tài khoản (assp 11 + data 10 + kundalini + flipbook) ≈ 9,1 nghìn ký tự ≈ 2,3 nghìn token; `anthropic-skills:*` ≈ 10 nghìn ký tự ≈ 2,5 nghìn. Phần lớn 74 nghìn là prompt hệ thống + schema công cụ của Claude Code (cache), không tắt được.
