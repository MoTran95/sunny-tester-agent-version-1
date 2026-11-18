# Nhiều dự án: chọn dự án, tạo dự án mới, không lẫn kiến thức
Cập nhật: 2026-11-18 · Liên quan: [../project/overview.md](../project/overview.md), [../decisions/decision-log.md](../decisions/decision-log.md)

Người dùng yêu cầu (2026-11-18): sang máy mới thì hỏi đang làm dự án nào; dự án khác thì tạo thư mục riêng; **không dùng kiến thức của Banking Lite cho dự án khác** để khỏi lẫn lộn. Người dùng chọn: hỏi **một lần mỗi máy**, thư mục **theo cấu trúc hiện có**.

## Dự án hiện tại trên máy này
- Ghi ở file `.du-an-hien-tai` ở gốc repo: một dòng là slug (ví dụ `banking-lite`). File này **không commit** (`.gitignore`), mỗi máy một file.
- Chưa có file (máy mới) → **hỏi người dùng trước khi làm gì khác**: liệt kê các dự án trong bảng ở [../project/overview.md](../project/overview.md) và lựa chọn "dự án mới". Trả lời xong thì ghi slug vào file.
- Có file → dùng luôn, không hỏi lại. Người dùng nhắc tên dự án khác → hỏi xác nhận đổi, rồi ghi lại file.

## Dự án mới
1. Hỏi: tên dự án, URL hệ thống (nếu có), slug ngắn (kebab-case, tiếng Anh không dấu, ví dụ `shop-online`). Không tự đặt khi người dùng chưa đồng ý.
2. Chạy: `python -X utf8 scripts/tao-du-an.py <slug> "<Tên dự án>" [<URL>]`. Script tạo `memories/modules/<slug>/overview.md`, các thư mục `srs/<slug>/`, `testing/<slug>/`, `evidence/<slug>/` (có `.gitkeep`), thêm dòng vào bảng dự án, ghi `.du-an-hien-tai`.
3. Thêm dòng cho dự án vào `memories/MEMORY.md` (mục "Dự án").
4. Tài khoản test: người dùng tự thêm vào `.env` với tiền tố `<SLUG_HOA>_` (ví dụ `SHOP_ONLINE_URL`), theo mẫu `.env.example`.

## Không lẫn kiến thức giữa các dự án
- Chỉ đọc bộ nhớ, SRS, bảng soát, bằng chứng của **dự án hiện tại**. Thư mục của dự án khác: không mở, kể cả "để xem mẫu".
- Làm theo khuôn chung: `srs/_template.md`, `srs/id-and-source-rules.md`, `assets/` của skill. Ví dụ trong khuôn và trong bài học của skill (có nhắc `LOGIN`, `RECO`, LTV…) chỉ minh họa **cách làm**, không phải quy tắc nghiệp vụ của dự án mới.
- Không mang sang dự án khác: quy tắc nghiệp vụ, tài khoản, dữ liệu test, tên màn hình, thông báo, từ ngữ đã chốt với BA (nằm trong `memories/modules/<slug>/tu-ngu-cau-hoi-ba.md`), giới hạn khóa/chặn đã đo.
- Được mang theo: sở thích của người dùng (`memories/user/`), quy ước chung (`memories/conventions/`), quy trình và bài học về cách làm trong skill.
- Dự án mới chưa có điều gì đã biết thì ghi là chưa biết và hỏi, không suy từ dự án cũ.
