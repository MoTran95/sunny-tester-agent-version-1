# Git & remote của repo
Cập nhật: 2026-11-18

- Thư mục này **trước 2026-11-18 chưa phải git repo**. Ngày 2026-11-18 đã `git init -b main`, commit đầu tiên (143 file) và push lên `git@github.com:MoTran95/sunny-tester-agent-version-1.git` (nhánh `main`, remote `origin`, đã set upstream).
- `.gitignore` chỉ có `.env` → mật khẩu tài khoản test **không** lên GitHub. Đã kiểm: giá trị mật khẩu trong `.env` không xuất hiện ở file nào khác. Mã nhân viên test (P100001…) thì có trong tài liệu và đã lên repo (không phải bí mật).
- Git đã có sẵn `user.name`/`user.email` (MoTran95). Cảnh báo LF→CRLF khi commit là bình thường trên Windows.

**Why:** lần sau người dùng nhờ push/commit thì khỏi dò lại.
**How to apply:** trước khi commit file mới, đảm bảo không chép mật khẩu từ `.env` vào tài liệu; commit/push chỉ khi người dùng yêu cầu.
