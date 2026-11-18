# MEMORY.md — Bản đồ bộ nhớ của repo

Đọc ngay sau `CLAUDE.md`. Mỗi dòng: file nào, chứa gì, khi nào đọc. Chỉ hai file đánh dấu **luôn đọc** là đọc ở mọi yêu cầu; còn lại chỉ đọc khi việc liên quan.
Thêm, đổi tên hoặc xóa file bộ nhớ thì sửa bản đồ trong cùng lượt. Mỗi dòng giữ ngắn; chi tiết để trong file. Không ghi nhật ký cập nhật ở đây.

## Người dùng
- [user/working-preferences.md](user/working-preferences.md) — **luôn đọc**. Sở thích cốt lõi: tiếng Việt, từng bước nhỏ, không gõ mật khẩu, tối đa 3 lần, đọc là hiểu.
- [user/document-preferences.md](user/document-preferences.md) — cách viết báo cáo, SRS, bảng soát, checklist mà người dùng muốn. Đọc khi viết tài liệu.
- [user/connectors-and-plugins.md](user/connectors-and-plugins.md) — Notion, Claude Docs đã tắt; hỏi trước khi bật. Đọc khi việc cần connector/plugin.

## Quy ước
- [conventions/memory-writing-rules.md](conventions/memory-writing-rules.md) — đặt tên, độ dài, khuôn file bộ nhớ. Đọc trước khi ghi/sửa bộ nhớ.
- [conventions/ba-question-wording.md](conventions/ba-question-wording.md) — xưng hô, từ đã chốt, khuôn câu hỏi gửi BA. Đọc khi viết câu hỏi cho BA.

## Dự án
- [project/overview.md](project/overview.md) — **luôn đọc**. Dự án là gì, hệ thống đang test (Banking Lite), trạng thái.
- [project/skills.md](project/skills.md) — ba skill của repo, thành phần, đã thử gì. Đọc khi dùng hoặc sửa skill.
- [project/srs-process.md](project/srs-process.md) — quy trình khám phá → SRS, khuôn và quy tắc ID. Đọc khi làm SRS.
- [project/session-speed.md](project/session-speed.md) — vì sao phiên chậm, số đo, hướng đã/chưa làm. Đọc khi người dùng than chậm hoặc khi sửa skill/khuôn.
- [project/git-remote.md](project/git-remote.md) — remote GitHub, `.env` bị loại trừ. Đọc khi commit/push.
- [project/architecture.md](project/architecture.md) — cấu trúc thư mục, quyền cho phép sẵn, cài đặt máy mới. Đọc khi thêm thư mục, đổi quyền, hoặc làm trên máy mới.
- [project/notion-journey-page.md](project/notion-journey-page.md) — trang Notion hành trình (3 database, hướng dẫn v2). Đọc khi người dùng nhắc Notion, hướng dẫn người mới, content.

## Quyết định
- [decisions/decision-log.md](decisions/decision-log.md) — quyết định đã chốt và lý do. Đọc trước khi đề xuất đổi hướng.

## Module: Banking Lite
| File | Nội dung |
|---|---|
| [modules/banking-lite/exploration-findings.md](modules/banking-lite/exploration-findings.md) | Luồng hồ sơ vay, vai trò, tích hợp, bẫy khi thao tác browser |
| [modules/banking-lite/feature-dang-nhap.md](modules/banking-lite/feature-dang-nhap.md) | Đăng nhập (`LOGIN`): thông báo lỗi, link sâu, câu trả lời BA, điều chưa thử |
| [modules/banking-lite/feature-khuyen-nghi-ltv-dsr.md](modules/banking-lite/feature-khuyen-nghi-ltv-dsr.md) | Khuyến nghị LTV/DSR (`RECO`): luật thẩm định, dữ liệu test, bẫy |
| [modules/banking-lite/feature-gui-tham-dinh.md](modules/banking-lite/feature-gui-tham-dinh.md) | Nút Gửi thẩm định: điều kiện bật/tắt, dữ liệu test, việc còn lại |
| [modules/banking-lite/report-v2-html.md](modules/banking-lite/report-v2-html.md) | Báo cáo HTML v2: cấu trúc, khoanh nút, cách xem thử |

Module mới: tạo thư mục con trong `modules/` từ [modules/_template.md](modules/_template.md).

## Bẫy
- [pitfalls/dont-trigger-lockouts.md](pitfalls/dont-trigger-lockouts.md) — từng tự kích hoạt chặn đăng nhập 5 phút. Đọc trước khi lặp thao tác có thể gây khóa.

## Sản phẩm trong `testing/` (không phải bộ nhớ)
- [../testing/chien-luoc-phan-tich-requirement.md](../testing/chien-luoc-phan-tich-requirement.md) — chiến lược Tách–Xoay–Lọc rút từ sách Sunny. Đọc khi phân tích requirement mới hoặc người dùng nhắc “sách”.
- `LOGIN` — [bảng soát](../testing/banking-lite/dang-nhap/bang-soat-requirement.md) (TL-01…11) và [câu hỏi BA](../testing/banking-lite/dang-nhap/cau-hoi-cho-ba.md) (A1–A6, B1, B3, B12, B13 đã trả lời). Đọc trước khi làm checklist/test case `LOGIN`.
- `RECO` — [bảng soát](../testing/banking-lite/khuyen-nghi-ltv-dsr/bang-soat-requirement.md), [câu hỏi BA](../testing/banking-lite/khuyen-nghi-ltv-dsr/cau-hoi-cho-ba.md), [phân tích cũ có 62 test case](../testing/banking-lite/khuyen-nghi-ltv-dsr/phan-tich-requirement.md). Đọc trước khi làm checklist/test case `RECO`.
