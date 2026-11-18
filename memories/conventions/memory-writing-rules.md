# Quy tắc viết bộ nhớ

## Cấu trúc thư mục
```
memories/
  MEMORY.md              bản đồ (bắt buộc, luôn cập nhật)
  conventions/           quy ước về chính hệ thống bộ nhớ
  user/                  sở thích, cách làm việc của người dùng
  project/               tổng quan, kiến trúc
  decisions/             nhật ký quyết định
  modules/<ten-module>/  bộ nhớ riêng cho từng module chức năng
  pitfalls/              bẫy, lỗi đã gặp (tạo khi cần)
```

## Đặt tên
- kebab-case, tiếng Anh không dấu, tên nói lên nội dung: `session-handling.md`, không dùng `notes.md`, `misc.md`.
- Một thư mục con cho mỗi module; trong đó chia file theo khía cạnh (ví dụ `overview.md`, `data-flow.md`, `known-issues.md`).
- Nội dung viết bằng tiếng Việt.

## Độ dài & tách file
- Một file = một chủ đề. Mục tiêu dưới ~150 dòng.
- Quá dài hoặc có hai chủ đề trở lên → tách file, cập nhật `MEMORY.md`.
- Không nhân bản thông tin: một sự thật nằm ở một nơi, nơi khác chỉ link.

## Ghi gì / không ghi gì
- Ghi: lý do thiết kế, ràng buộc, quyết định, quy ước, bẫy đã gặp, ngữ cảnh người dùng.
- Không ghi: nội dung code (đọc code là được), lịch sử commit, thông tin tạm thời của một phiên.

## Khuôn mẫu đầu file
Mỗi file bộ nhớ mở đầu bằng:
```
# <Tiêu đề>
Cập nhật: YYYY-MM-DD · Liên quan: <file/module khác nếu có>
```
Dùng ngày tuyệt đối, không dùng "hôm qua", "tuần trước".

## Bảo trì
- Thông tin sai/lỗi thời: sửa hoặc xóa ngay, đừng để lại.
- Cuối mỗi lượt có học được điều mới: ghi vào đúng file, rồi kiểm tra `MEMORY.md` đã khớp chưa.
