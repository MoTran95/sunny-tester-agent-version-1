# MEMORY.md — Bản đồ bộ nhớ của repo

Đọc file này ngay sau `CLAUDE.md`. Mỗi dòng dưới đây trỏ tới một file bộ nhớ và nói file đó chứa gì / khi nào cần đọc.
Khi thêm, đổi tên hoặc xóa file bộ nhớ, **phải cập nhật bản đồ này trong cùng lượt**.

Cập nhật lần cuối: 2026-11-18 (ghi câu trả lời A1–A5 của `LOGIN` thành TL-01…05; trước đó 2026-11-17: sửa skill srs-from-website theo 4 gợi ý đã duyệt; trước đó: thêm trang Notion tổng hợp hành trình; trước đó: bảng soát + câu hỏi BA cho feature Đăng nhập `LOGIN`; Khuyến nghị LTV/DSR, SRS RECO tự lệch, prompt phân tích v2, khuôn bảng v3 TC/CH, luật viết test case)

## Quy ước & cách dùng bộ nhớ
- [conventions/memory-writing-rules.md](conventions/memory-writing-rules.md) — cách đặt tên, độ dài, khuôn mẫu, khi nào tách file. Đọc trước khi ghi/sửa bộ nhớ.

- [conventions/ba-question-wording.md](conventions/ba-question-wording.md) — xưng hô và từ đã chốt cho câu hỏi gửi BA (“mình/anh-chị”, “mức tối đa”, “hết hạn vay”), khuôn câu hỏi. Skill `phan-tich-requirement` đọc file này. Đọc khi viết câu hỏi cho BA.

## Người dùng
- [user/working-preferences.md](user/working-preferences.md) — ngôn ngữ, cách người dùng muốn làm việc. Đọc ở mọi yêu cầu.

## Tổng quan dự án
- [project/overview.md](project/overview.md) — dự án là gì, mục tiêu, trạng thái hiện tại, bối cảnh khám phá banking-lite (tester). Đọc ở mọi yêu cầu.
- [project/architecture.md](project/architecture.md) — kiến trúc tổng thể, cấu trúc thư mục, công nghệ. Đọc khi thêm/sửa chức năng.

- [project/skills.md](project/skills.md) — ba skill: `feature-exploration-report` (báo cáo khám phá HTML), `srs-from-website` (khám phá → SRS Markdown Story + AC, có script soát) và `phan-tich-requirement` (bảng soát + câu hỏi BA, có script kiểm). Nằm ở đâu, gồm gì. Đọc khi người dùng nhờ làm/sửa báo cáo khám phá, viết/cập nhật/soát SRS, phân tích requirement, hoặc đụng tới skill.

- [project/notion-journey-page.md](project/notion-journey-page.md) — trang Notion tổng hợp hành trình 17/11 (3 database: nhật ký, feedback trước→sau, lỗi + cách giải quyết; trang hướng dẫn thực hành v2 có 30 quy tắc vàng và prompt chi tiết theo 6 chặng; bản v1 đã xóa), link, nguồn ngày giờ, bẫy khi tạo. Đọc khi người dùng nhắc Notion, tracking, hướng dẫn người mới, content quảng bá.
- [project/srs-process.md](project/srs-process.md) — quy trình “khám phá → SRS” đang thử (khuôn v2 Story+AC `srs/_template.md`, quy tắc ID/nguồn `srs/id-and-source-rules.md`, sửa tại chỗ vs tạo mới, phạm vi khám phá, trạng thái). Đọc khi người dùng nhắc SRS/requirement/Sunny Ocean Testing.

- [../testing/banking-lite/khuyen-nghi-ltv-dsr/phan-tich-requirement.md](../testing/banking-lite/khuyen-nghi-ltv-dsr/phan-tich-requirement.md) — (không phải bộ nhớ, là sản phẩm) file phân tích requirement `RECO`: checklist 62 TC có ưu tiên + lý do, 18 câu hỏi CH, 16 câu hỏi KN (kinh nghiệm), dữ liệu nền, luật viết test case. Đọc khi người dùng nhờ viết test case chi tiết cho `RECO`. Thư mục `testing/` mới, mỗi feature một thư mục con.

- [../testing/banking-lite/khuyen-nghi-ltv-dsr/bang-soat-requirement.md](../testing/banking-lite/khuyen-nghi-ltv-dsr/bang-soat-requirement.md) — (sản phẩm) bảng soát 37 AC của `RECO` theo sách: ✅/❓, 3 nhóm câu hỏi (6 Hỏi ngay / 13 Gom hỏi sau / 15 Tự tìm trước), bản nháp câu gửi BA. Bước kế tiếp sau phân tích; đọc trước khi làm checklist/test case `RECO`.
- [../testing/banking-lite/khuyen-nghi-ltv-dsr/cau-hoi-cho-ba.md](../testing/banking-lite/khuyen-nghi-ltv-dsr/cau-hoi-cho-ba.md) — (sản phẩm) bản câu hỏi gửi BA của `RECO` viết cho dễ đọc: Phần A 5 câu hỏi ngay (làm tròn TL-02, quá tuổi, tổ hợp nhãn, cách tính tuổi, tài liệu chính thức), Phần B 12 câu hỏi sau, Phần C 14 mục tự kiểm tra; mỗi câu có vấn đề, ví dụ, cách đang hiểu, lý do, ô trả lời. Dùng khi người dùng muốn hỏi BA.
- [../testing/banking-lite/dang-nhap/bang-soat-requirement.md](../testing/banking-lite/dang-nhap/bang-soat-requirement.md) — (sản phẩm) bảng soát feature `LOGIN` (Đăng nhập): 39 đơn vị có mã + 6 mục không mã, 82 trích dẫn đã kiểm bằng script. Đã có TL-01…TL-10 (2026-11-18), 15 đơn vị khác hệ thống hiện tại. Đọc trước khi làm checklist/test case `LOGIN`.
- [../testing/banking-lite/dang-nhap/cau-hoi-cho-ba.md](../testing/banking-lite/dang-nhap/cau-hoi-cho-ba.md) — (sản phẩm) câu hỏi BA của `LOGIN`: A 6 (đều đã trả lời), B 13 (B1, B3, B12, B13 đã trả lời), tất cả trả lời ngày 2026-11-18 (TL-01…11), C 9 tự kiểm tra (C6 bỏ; chỉ C1 còn có thể nhập sai). BA đã trả lời A1–A6, B1, B3, B12, B13; các câu còn lại chưa hỏi.
- [../testing/chien-luoc-phan-tich-requirement.md](../testing/chien-luoc-phan-tich-requirement.md) — (sản phẩm, không phải bộ nhớ) chiến lược phân tích requirement rút từ sách Sunny: Tách–Xoay–Lọc, 3 nhóm câu hỏi, đối chiếu với `RECO`, chỗ cần người dùng quyết. Đọc khi người dùng nhờ phân tích requirement mới hoặc nhắc “sách”.

## Quyết định
- [decisions/decision-log.md](decisions/decision-log.md) — các quyết định thiết kế đã chốt và lý do. Đọc trước khi đề xuất đổi hướng.

## Module chức năng
Mỗi module một thư mục con trong `modules/`, bắt đầu từ khuôn mẫu [modules/_template.md](modules/_template.md).

| Module | File | Nội dung |
|---|---|---|
| banking-lite (hệ thống đang test) | [modules/banking-lite/exploration-findings.md](modules/banking-lite/exploration-findings.md) | Kết quả khám phá: luồng hồ sơ vay, vai trò, tích hợp, bẫy khi thao tác browser |
| banking-lite — feature “Gửi thẩm định” | [modules/banking-lite/feature-gui-tham-dinh.md](modules/banking-lite/feature-gui-tham-dinh.md) | Điều đã thấy về nút Gửi thẩm định (điều kiện bật/tắt, 12 mục, sau khi gửi), dữ liệu test HL-000022/23, việc còn lại |
| banking-lite — báo cáo HTML v2 | [modules/banking-lite/report-v2-html.md](modules/banking-lite/report-v2-html.md) | Cấu trúc file `bao-cao-kham-pha-v2.html`, cách khoanh nút trên ảnh, cách xem thử, khoảng trống bằng chứng |
| banking-lite — feature “Đăng nhập” | [modules/banking-lite/feature-dang-nhap.md](modules/banking-lite/feature-dang-nhap.md) | Thông báo lỗi đăng nhập, hành vi link sâu, ngôn ngữ, điều chưa thử, cách phối hợp khi cần gõ mật khẩu |

| banking-lite — feature “Khuyến nghị LTV/DSR” | [modules/banking-lite/feature-khuyen-nghi-ltv-dsr.md](modules/banking-lite/feature-khuyen-nghi-ltv-dsr.md) | Luật thẩm định xem trước (LTV 80/70, DSR 50/70, thặng dư 3 triệu, tuổi 70), điểm bất thường tuổi đáo hạn, dữ liệu test HL-000025, bẫy thao tác; SRS `RECO` |

## Bẫy & bài học
- [pitfalls/dont-trigger-lockouts.md](pitfalls/dont-trigger-lockouts.md) — sự cố tự kích hoạt chặn đăng nhập 5 phút khi test; vì sao sai và cách làm đúng. Đọc trước khi lặp bất kỳ thao tác nào có thể gây khóa/giới hạn.
