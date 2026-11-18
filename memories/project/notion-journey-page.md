# Trang Notion "Hành trình xây skill AI" (tạo 2026-11-17)
Đọc khi: người dùng nhắc Notion, hướng dẫn người mới, content, hoặc cần bổ sung feedback/lỗi lên Notion (Notion đang tắt, hỏi trước khi bật: `user/connectors-and-plugins.md`).

## Là gì
- Người dùng nhờ hệ thống lại quá trình làm việc với AI: trước/sau feedback, database có ngày, hướng dẫn dạy người mới, lỗi + cách giải quyết làm content. **Bản nháp riêng tư**, người dùng tự chuyển chỗ.
- Trang gốc: https://app.notion.com/p/41bfcb30974e81fbb1fdf9cf6121d358 — 3 database: 📅 Nhật ký tiến trình (23 mốc), 🔁 Feedback trước → sau (24 dòng), 🐞 Lỗi và cách giải quyết (23 dòng, có cột "Ý tưởng content").
- Trang hướng dẫn **duy nhất**: v2 "Hướng dẫn thực hành v2: dựng 3 skill đúng ngay lần đầu" https://app.notion.com/p/41bfcb30974e81b0a8ffd21fd20ff7ab (30 quy tắc vàng A–F, Prompt nền 18 dòng, lộ trình 6 chặng 0–5, phép thử skill, công thức feedback, bảng triệu chứng → câu dán, bài tập). **Chưa có người học chạy thử.** v1 đã xóa (thùng rác Notion) 2026-11-17, không tạo lại.
- Phạm vi chỉ repo này (ngày 17/11), không gồm `D:\Sunny-Agent-Learning`, `D:\Sunny-AI-Testing` (từ 29/10); thêm thì làm riêng. Cấu trúc: 1 trang gốc + 3 database + 1 trang hướng dẫn.

## Bẫy
- Ngày giờ lấy từ log phiên `C:\Users\Admin\.claude\projects\D--AI-build-sunny-agent-version-1\*.jsonl` (UTC, +7 = giờ VN), không từ bộ nhớ. Lấy lời nhắn gốc: script Python đọc từng dòng, `type == "user"`, bỏ tool_result/system-reminder (script tạm, không lưu).
- Lời nhắn gốc có **mật khẩu tài khoản test** (tin 10:32) → bỏ khi tổng hợp, không đưa lên Notion.
- Prompt "Bước 0 dựng bộ nhớ" trong hướng dẫn là mình viết lại, không nguyên văn (log phiên tạo repo trống); đã ghi chú trên trang.
- Gõ tiếng Việt vào tham số công cụ từng sai ("hiết hạn vay", "Cap nhật", "column", "dây chuyền" là từ cấm) → tạo trang xong phải soát chính tả + từ cấm ("thiết" khớp nhầm "hiết" là dương tính giả). Viết tiếng Việt **trực tiếp**, không `\uXXXX`.
- Trang >30k ký tự: tạo phần đầu rồi `insert_content` từng ~10–12k ký tự. `notion-fetch` trang dài bị lưu ra file → script tách `text`. `notion-create-pages` JSON quá lớn lỗi parse → chia lô ≤ ~8 dòng.

## Cập nhật
Thêm dòng vào đúng database (cột "Thời điểm" ngày giờ +07:00; STT để xếp). Feedback đổi quy tắc skill thì ghi cả "Bản trước" và "Bản sau".
