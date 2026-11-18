---
name: feature-exploration-report
description: Khám phá một feature/hệ thống bằng thao tác thật rồi lập báo cáo HTML dễ đọc cho người mới — vai trò tài khoản, ảnh khoanh nút đánh số, sơ đồ luồng có số bước, luồng end-to-end, điểm mơ hồ kèm bằng chứng. Dùng khi người dùng (thường là tester) nói "khám phá feature", "báo cáo khám phá", "làm báo cáo cho feature X", "tạo/cập nhật báo cáo HTML", hoặc muốn mô tả vai trò/luồng của một hệ thống chưa có tài liệu. Không dùng cho báo cáo lỗi (bug report) hay test case.
---

# Báo cáo khám phá feature (HTML)

Biến một lượt khám phá thật trên hệ thống thành **một file HTML tự chứa**, mở được ngay trong khung xem trước của app. Mẫu tham chiếu đã chạy thật (dự án Banking Lite, chỉ mở khi đang làm dự án đó): `evidence/banking-lite/bao-cao-kham-pha-v2.html` (nguồn: `evidence/banking-lite/_src/`).

Ngôn ngữ: **tiếng Việt**, dùng đúng thuật ngữ IT, dễ hiểu (xem `references/report-structure.md` mục "Thuật ngữ").

## Quy tắc không được phá

1. **Chỉ ghi điều đã nhìn thấy trên màn hình.** Điều chưa kiểm chứng ghi `❓ chưa xác nhận`. Không suy đoán công thức, quyền, ý nghĩa thiết kế. Không kết luận “lỗi” hay “đúng thiết kế” khi chưa có tài liệu — viết “đã thấy / vì sao chưa rõ / cần làm rõ”.
2. **Trung thực về bằng chứng.** Chỗ nào không có ảnh thì nói “không có ảnh, chỉ ghi nhận trong báo cáo”. Không dựng lại ảnh, không gán ảnh cho khoảnh khắc khác.
3. **Mật khẩu:** không tự gõ mật khẩu; người dùng tự đăng nhập từng tài khoản trong cửa sổ trình duyệt. Không ghi mật khẩu vào báo cáo, bộ nhớ hay chat.
4. **Hỏi trước khi tạo/sửa dữ liệu thật, tải file, gửi thứ có thể ra ngoài** (SMS, email…). Dữ liệu test do mình tạo thì ghi rõ mã để người dùng nhận ra.
5. **Hỏi người dùng khi chưa rõ**, đừng tự quyết (xem mục 7 của báo cáo).

## Đọc gì cho từng việc
Luôn đọc: `memories/user/working-preferences.md`, `memories/project/overview.md`, và `memories/modules/<slug>/overview.md` của **dự án hiện tại** (slug trong `.du-an-hien-tai`; chưa có thì hỏi người dùng trước, xem `CLAUDE.md` bước 0). `<hệ thống>` trong các đường dẫn dưới đây chính là slug đó. **Không mở file của dự án khác, kể cả để làm mẫu**: dùng khuôn trong `assets/` (và `srs/_template.md`). Thêm theo việc:

| Việc | Đọc | Không cần đọc |
|---|---|---|
| Khám phá + làm báo cáo mới | `references/report-structure.md`, `references/evidence-and-build.md`, `assets/report-template.src.html`, `memories/user/document-preferences.md`, `memories/pitfalls/dont-trigger-lockouts.md`. Nếu là Banking Lite: thêm `references/banking-lite-context.md`, `memories/modules/banking-lite/exploration-findings.md` và bộ nhớ của feature nếu có | File HTML đã build (~500 KB, đọc vô ích); ảnh cũ trong `evidence/` trừ khi dùng lại; `scripts/build-embed.py` (chỉ chạy) |
| Sửa báo cáo có sẵn | Phần cần sửa trong file `*.src.html` (tìm bằng Grep), `references/evidence-and-build.md` (mục build, soát), `memories/modules/banking-lite/report-v2-html.md` | File HTML đã build; cả file nguồn nếu chỉ sửa một mục |
| Sửa chính skill này | `memories/project/skills.md`, file cần sửa | Báo cáo và ảnh |

Ảnh: chỉ mở những ảnh cần khoanh nút hoặc cần kiểm, không mở hàng loạt (một phiên trước mở 41 ảnh trước khi viết dòng đầu tiên).

## Quy trình

0. **Đọc đúng những file cần cho việc này** (bảng "Đọc gì cho từng việc" ngay dưới), sau `CLAUDE.md` và `memories/MEMORY.md`. Không đọc thêm cho chắc.
1. **Chốt phạm vi** (hỏi nếu thiếu): tên feature, URL hệ thống/phiên bản, danh sách tài khoản + vai trò đã biết, được phép tạo dữ liệu test không, tích hợp bên ngoài (SMS/email/…) là thật hay mô phỏng. **Nếu là feature của Banking Lite** (https://banking-lite.vercel.app/): đọc `references/banking-lite-context.md` — có sẵn tài khoản, bản đồ feature, điều đã/chưa khám phá; chỉ khám phá thêm phần còn thiếu, phần đã có thì tham chiếu báo cáo v2. **Dự án khác: không đọc file đó**, mọi thông tin về hệ thống phải lấy từ khám phá thật của dự án này.
2. **Khám phá thật** bằng trình duyệt (xem `references/evidence-and-build.md` mục "Chụp ảnh"). Với mỗi vai trò: màn hình đầu, từng nút, trường nhập, thông báo (chép **nguyên văn**), trạng thái chuyển. Chạy hết luồng chính rồi các nhánh (thành công, từ chối, trả lại/hoàn tác, nhập sai).
3. **Ghi nhật ký gốc bằng Markdown** (`evidence/<hệ thống>/features/<feature>/bao-cao.md`) ngay trong lúc khám phá: bảng thao tác → kết quả → số ảnh. Đây là nguồn sự thật để dựng HTML. Giữ mục “Chưa thử” và “Câu hỏi cho team”.
4. **Dựng nguồn HTML** từ `assets/report-template.src.html` → `evidence/<hệ thống>/features/<feature>/_src/<ten>.src.html`. Cấu trúc 7 mục và cách viết từng mục: `references/report-structure.md`.
5. **Khoanh nút trên ảnh**: đo toạ độ thật từ ảnh gốc (mở ảnh, đọc vị trí), điền `<i class="mk" ...>`; vị trí số do script tự chọn. Chi tiết: `references/evidence-and-build.md`.
6. **Build**: `python -X utf8 scripts/build-embed.py --src <src.html> --out <report.html> --shots <thư_mục_ảnh>`. Phải ≤ 512 KiB.
7. **Soát**: chạy thêm `--review <thư_mục>` và xem từng tranh ghép (khung có đúng ô? số có đè chữ/đè nhau?); mở file thật trong khung xem trước kiểm tra ảnh hiện, thanh tab cuộn đúng. Xong mới giao.
8. **Cập nhật bộ nhớ** (`memories/modules/<hệ thống>/feature-<tên>.md` + `MEMORY.md`): kết quả khám phá, bẫy mới, khoảng trống bằng chứng.
9. **Trả lời người dùng**: nêu file, điều đã kiểm tra, điều **chưa** kiểm tra, và các câu cần họ trả lời.

## Khi người dùng nhờ sửa báo cáo đã có

Sửa **file nguồn `*.src.html`**, chạy lại build — không sửa file đã build. Lỗi hay gặp: khung vẽ sai ô (không phải chỉ chồng số) → soát bằng `--review`. Đổi từ ngữ → áp cho toàn bộ báo cáo, rồi grep lại các từ cũ.

## Tệp trong skill

- `references/report-structure.md` — 7 mục báo cáo, văn phong, bảng thuật ngữ IT, quy tắc sơ đồ.
- `references/banking-lite-context.md` — ngữ cảnh hệ thống Banking Lite: tài khoản, bản đồ feature + độ phủ khám phá, cách làm báo cáo cho từng feature.
- `references/evidence-and-build.md` — chụp ảnh, đặt tên, khoanh nút, build, soát, các bẫy đã gặp.
- `assets/report-template.src.html` — khung HTML nguồn (đã có CSS, thanh tab, mẫu step/flow/điểm mơ hồ).
- `scripts/build-embed.py` — nhúng ảnh thu nhỏ, tự đặt số thứ tự, JS thanh tab, kiểm tra giới hạn 512 KiB.
