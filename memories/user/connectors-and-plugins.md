# Connector và plugin: mặc định tắt, hỏi trước khi bật
Cập nhật: 2026-11-18 · Liên quan: [../project/session-speed.md](../project/session-speed.md), [../project/notion-journey-page.md](../project/notion-journey-page.md)

- Người dùng yêu cầu (2026-11-18): tắt các connector/plugin không dùng cho việc kiểm thử, **chỉ bật khi người dùng yêu cầu hoặc khi thật sự cần, và phải hỏi người dùng trước khi bật**.
- Đã tắt (2026-11-18, mặc định cho phiên mới): connector **Notion**, **Claude Docs**. Bật lại bằng công cụ `set_session_connector_enabled` sau khi người dùng đồng ý; có tác dụng từ lượt sau.
- Mình không tự tắt được: plugin `data` (Amplitude, BigQuery, Hex, Snowflake…) và các skill cấp tài khoản (`assp-*`, `kundalini-yoga-translator`, `flipbook-builder`) vì chúng gắn với tài khoản claude.ai → người dùng tự tắt trong phần quản lý plugin/skill của app.
- Khi nào cần hỏi bật: Notion — cập nhật trang hành trình/database feedback; Claude Docs — người dùng muốn tạo doc chia sẻ. Kiểm thử (skill trong repo, trình duyệt có sẵn, script Python) không cần cái nào.

**Why:** giảm phần nạp sẵn ~77 nghìn token mỗi phiên, bớt nhiễu khi chọn skill.
**How to apply:** việc nào cần connector/plugin đang tắt → dừng, hỏi người dùng, chỉ bật khi được đồng ý.
