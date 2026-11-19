# Cài đặt repo trên máy mới

Mục tiêu: lần đầu mở repo trên máy khác, Claude bắt tay làm việc ngay, không mất thời gian dò lỗi cài đặt hay chờ bạn bấm cho phép từng lệnh. Làm một lần, khoảng 10–15 phút.

## 1. Cài phần mềm (một lần cho mỗi máy)
| Cần | Để làm gì | Cách cài |
|---|---|---|
| Git | Lấy repo, commit, push | git-scm.com → Git for Windows |
| Python 3.10 trở lên | Chạy các script soát của skill | python.org (tick "Add python.exe to PATH") hoặc Microsoft Store |
| Pillow | Script build báo cáo HTML cần | lệnh bên dưới |
| App Claude (desktop) | Làm việc với Claude | claude.ai/download |

```powershell
python -m pip install pillow
```

Nếu gõ `python` mà Windows mở Microsoft Store thay vì chạy: Python chưa được cài, hoặc đang bị "App execution aliases" chặn. Cài Python rồi mở lại cửa sổ PowerShell.

## 2. Lấy repo
```powershell
git clone git@github.com:MoTran95/sunny-tester-agent-version-1.git D:\AI\build-sunny-agent-version-1
```

## 3. Chọn dự án và tạo file tài khoản test `.env`
Repo chứa nhiều dự án (mỗi dự án là một hệ thống đang test, hiện có `banking-lite`). Mở phiên Claude đầu tiên trên máy mới, **Claude sẽ hỏi bạn đang làm dự án nào** rồi ghi vào file `.du-an-hien-tai` (chỉ nằm trên máy này, không commit). Các phiên sau không hỏi lại; muốn đổi thì nói tên dự án khác.
- Dự án đã có: chọn trong danh sách.
- Dự án mới: Claude hỏi tên, URL, tên thư mục ngắn rồi tạo thư mục riêng (`scripts/tao-du-an.py`). Claude **không dùng kiến thức của Banking Lite** cho dự án mới.

`.env` không đi theo git (để không lộ mật khẩu). Chép file mẫu rồi **tự điền mật khẩu** của dự án đang làm bằng Notepad. Đừng gửi mật khẩu qua chat. Dự án mới: thêm nhóm khóa riêng theo hướng dẫn ở đầu `.env.example`.

```powershell
Copy-Item D:\AI\build-sunny-agent-version-1\.env.example D:\AI\build-sunny-agent-version-1\.env
```

## 4. Việc phải tự làm trong app Claude
1. Mở thư mục repo trong tab Code. Khi app hỏi có tin cậy thư mục không, chọn tin cậy: app mới đọc `.claude/settings.json`, nơi đã cho phép sẵn các lệnh an toàn (sửa file trong `memories/`, `srs/`, `testing/`, `evidence/`, `docs/`, skill; chạy script soát; `git status/diff/log/show`). `git commit`, `git push`, xóa file vẫn hỏi bạn trước.
2. (Tùy chọn, ít tác dụng) Tắt tay trong phần quản lý plugin/skill của app những thứ không dùng cho kiểm thử: plugin `data`, skill `assp-*`, `kundalini-yoga-translator`, `flipbook-builder`; Notion và Claude Docs chỉ bật khi cần. Đã đo 2026-11-18: nạp sẵn ~74 nghìn token, phần của plugin/skill tài khoản chỉ ~2–5 nghìn, và **script/cấu hình trong repo không tắt được** chúng (`memories/user/connectors-and-plugins.md`).
3. Lần đầu Claude mở trang Banking Lite trong trình duyệt của app: bấm cho phép trang, rồi tự đăng nhập (Claude không gõ mật khẩu).

## 5. Kiểm tra máy đã sẵn sàng
```powershell
python -X utf8 scripts/kiem-tra-may-moi.py
```
Chạy trong thư mục repo. Script kiểm Python, Pillow, Git, `.env` (không in mật khẩu), skill, quyền trong `.claude/settings.json`, và chạy thử hai script soát. "0 mục THIẾU" là xong. Hoặc nhờ Claude: "chạy kiểm tra máy mới".

## 6. Thói quen để phiên nào cũng nhanh
- **Mỗi việc một phiên mới.** Phiên dài làm mỗi bước sau chậm hơn.
- **Nói rõ việc và feature ngay câu đầu** (ví dụ "ghi câu trả lời BA cho LOGIN: A7 …"). Skill đã ghi sẵn cần đọc file nào cho từng việc, không cần bảo Claude "đọc hết bộ nhớ".
- **Việc đơn giản** (push git, ghi câu trả lời BA, sửa chữ) thì hạ mức suy nghĩ (effort) trong app; phân tích requirement, khám phá thì để mức cao.

## Điều không đi theo repo (bình thường)
- Lịch sử chat và bộ nhớ tự động của Claude nằm ở `C:\Users\<tên>\.claude\` của từng máy. Bộ nhớ quan trọng của dự án đã nằm trong `memories/` nên máy mới vẫn đủ ngữ cảnh.
- Đăng nhập trình duyệt, cho phép trang web, bật/tắt plugin: làm lại trên từng máy (mục 4).

## Hook git để trang HTML luôn khớp file md
Chạy một lần trong mỗi bản clone: `git config core.hooksPath .githooks`. Từ đó mỗi lần commit, hook tự chạy `python -X utf8 scripts/build_docs.py --all --stage` để sinh lại mọi trang HTML (tài liệu, kết quả chạy, bug, trang tổng) và đưa vào commit. `python -X utf8 scripts/kiem-tra-may-moi.py` kiểm hook đã bật chưa. Giao diện và font: `docs/thuong-hieu/README.md`.
