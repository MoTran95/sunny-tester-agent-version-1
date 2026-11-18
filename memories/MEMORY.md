# MEMORY.md — Bản đồ bộ nhớ của repo

Đọc ngay sau `CLAUDE.md`. Mỗi dòng: file nào, chứa gì, khi nào đọc. Chỉ hai file đánh dấu **luôn đọc** là đọc ở mọi yêu cầu; còn lại chỉ đọc khi việc liên quan.
Repo có nhiều dự án: đọc phần **Chung** khi cần, và **chỉ** mục của dự án hiện tại (`.du-an-hien-tai`). Không mở mục của dự án khác.
Thêm, đổi tên hoặc xóa file bộ nhớ thì sửa bản đồ trong cùng lượt. Mỗi dòng giữ ngắn; chi tiết để trong file. Không ghi nhật ký cập nhật ở đây.

# Chung (mọi dự án)

## Người dùng
- [user/working-preferences.md](user/working-preferences.md) — **luôn đọc**. Sở thích cốt lõi: tiếng Việt, từng bước nhỏ, không gõ mật khẩu, tối đa 3 lần, đọc là hiểu, không lẫn dự án.
- [user/document-preferences.md](user/document-preferences.md) — cách viết báo cáo, SRS, bảng soát, checklist mà người dùng muốn. Đọc khi viết tài liệu.
- [user/connectors-and-plugins.md](user/connectors-and-plugins.md) — Notion, Claude Docs đã tắt; hỏi trước khi bật. Đọc khi việc cần connector/plugin.

## Quy ước
- [conventions/nhieu-du-an.md](conventions/nhieu-du-an.md) — chọn dự án, tạo dự án mới, không lẫn kiến thức giữa dự án. Đọc khi máy mới, đổi dự án hoặc tạo dự án.
- [conventions/memory-writing-rules.md](conventions/memory-writing-rules.md) — đặt tên, độ dài, khuôn file bộ nhớ. Đọc trước khi ghi/sửa bộ nhớ.
- [conventions/ba-question-wording.md](conventions/ba-question-wording.md) — xưng hô, quy tắc từ ngữ chung, khuôn câu hỏi gửi BA. Đọc khi viết câu hỏi cho BA.

## Repo
- [project/overview.md](project/overview.md) — **luôn đọc**. Repo là gì, danh sách dự án, thư mục theo dự án.
- [project/skills.md](project/skills.md) — ba skill của repo, thành phần, đã thử gì. Đọc khi dùng hoặc sửa skill.
- [project/srs-process.md](project/srs-process.md) — quy trình khám phá → SRS, khuôn và quy tắc ID. Đọc khi làm SRS.
- [project/session-speed.md](project/session-speed.md) — vì sao phiên chậm, số đo, hướng đã/chưa làm. Đọc khi người dùng than chậm hoặc khi sửa skill/khuôn.
- [project/git-remote.md](project/git-remote.md) — remote GitHub, `.env` bị loại trừ. Đọc khi commit/push.
- [project/architecture.md](project/architecture.md) — cấu trúc thư mục, quyền cho phép sẵn, cài đặt máy mới. Đọc khi thêm thư mục, đổi quyền, hoặc làm trên máy mới.
- [project/notion-journey-page.md](project/notion-journey-page.md) — trang Notion hành trình (3 database, hướng dẫn v2). Đọc khi người dùng nhắc Notion, hướng dẫn người mới, content.

## Quyết định và bẫy
- [decisions/decision-log.md](decisions/decision-log.md) — quyết định đã chốt và lý do. Đọc trước khi đề xuất đổi hướng.
- [pitfalls/dont-trigger-lockouts.md](pitfalls/dont-trigger-lockouts.md) — từng tự kích hoạt chặn đăng nhập khi test. Đọc trước khi lặp thao tác có thể gây khóa.

Dự án mới: `scripts/tao-du-an.py` tạo `modules/<slug>/overview.md`; thêm mục cho dự án ở dưới. Khuôn file module: [modules/_template.md](modules/_template.md).

# Dự án: Banking Lite (`banking-lite`)
Chỉ đọc khi `.du-an-hien-tai` là `banking-lite`.

| File | Nội dung |
|---|---|
| [modules/banking-lite/overview.md](modules/banking-lite/overview.md) | Hệ thống, tài khoản, bối cảnh, thư mục của dự án. Đọc đầu tiên khi làm Banking Lite |
| [modules/banking-lite/tu-ngu-cau-hoi-ba.md](modules/banking-lite/tu-ngu-cau-hoi-ba.md) | Từ đã chốt với BA (mức tối đa, hết hạn vay, bị chặn…) |
| [modules/banking-lite/exploration-findings.md](modules/banking-lite/exploration-findings.md) | Luồng hồ sơ vay, vai trò, tích hợp, bẫy khi thao tác browser |
| [modules/banking-lite/feature-dang-nhap.md](modules/banking-lite/feature-dang-nhap.md) | Đăng nhập (`LOGIN`): thông báo lỗi, link sâu, câu trả lời BA, điều chưa thử |
| [modules/banking-lite/feature-khuyen-nghi-ltv-dsr.md](modules/banking-lite/feature-khuyen-nghi-ltv-dsr.md) | Khuyến nghị LTV/DSR (`RECO`): luật thẩm định, dữ liệu test, bẫy |
| [modules/banking-lite/feature-gui-tham-dinh.md](modules/banking-lite/feature-gui-tham-dinh.md) | Nút Gửi thẩm định: điều kiện bật/tắt, dữ liệu test, việc còn lại |
| [modules/banking-lite/report-v2-html.md](modules/banking-lite/report-v2-html.md) | Báo cáo HTML v2: cấu trúc, khoanh nút, cách xem thử |

Sản phẩm trong `testing/` (không phải bộ nhớ):
- [../testing/chien-luoc-phan-tich-requirement.md](../testing/chien-luoc-phan-tich-requirement.md) — chiến lược Tách–Xoay–Lọc rút từ sách Sunny, đối chiếu với `RECO`. Đọc khi người dùng nhắc “sách” (với dự án khác: chỉ dùng phần cách làm, bỏ phần đối chiếu `RECO`).
- `LOGIN` — [bảng soát](../testing/banking-lite/dang-nhap/bang-soat-requirement.md) (TL-01…11) và [câu hỏi BA](../testing/banking-lite/dang-nhap/cau-hoi-cho-ba.md) (A1–A6, B1, B3, B12, B13 đã trả lời; A7, A8 suy ra TL-12, TL-13; B5–B7, B9–B11, B14 bỏ; còn hỏi B4, B8). Đọc trước khi làm checklist/test case `LOGIN`.
- `RECO` — [bảng soát](../testing/banking-lite/khuyen-nghi-ltv-dsr/bang-soat-requirement.md), [câu hỏi BA](../testing/banking-lite/khuyen-nghi-ltv-dsr/cau-hoi-cho-ba.md), [phân tích cũ có 62 test case](../testing/banking-lite/khuyen-nghi-ltv-dsr/phan-tich-requirement.md). Đọc trước khi làm checklist/test case `RECO`.
