# Trang Notion “Hành trình xây skill AI” (tổng hợp ngày 17/11/2026)
Cập nhật: 2026-11-17 · Liên quan: [skills.md](skills.md), [srs-process.md](srs-process.md), [../user/working-preferences.md](../user/working-preferences.md)

## Là gì
Người dùng nhờ (19:30 ngày 2026-11-17) hệ thống lại toàn bộ quá trình làm việc với AI: bản trước/sau feedback, tạo tài liệu dạng database có ngày, hướng dẫn dạy người mới dựng lại skill, và các lỗi + cách giải quyết làm chất liệu content quảng bá. Đã tạo trên Notion, **bản nháp riêng tư** (chưa chuyển vào chỗ nào; người dùng tự chuyển).

- Trang gốc: https://app.notion.com/p/41bfcb30974e81fbb1fdf9cf6121d358
- 3 database con: 📅 Nhật ký tiến trình (23 mốc), 🔁 Feedback trước → sau (24 dòng), 🐞 Lỗi và cách giải quyết (23 dòng; có cột “Ý tưởng content”).
- Trang con v1 “Hướng dẫn dạy người mới dựng lại 3 skill (từ số 0)”: **đã xóa (vào thùng rác Notion, khôi phục được) ngày 2026-11-17** theo yêu cầu người dùng, sau khi chép 4 gợi ý chỉnh skill `srs-from-website` sang v2 (mục 10). Không tạo lại; mọi nội dung nằm ở v2.
- Trang con v2 (2026-11-17, người dùng nhờ “rút quy tắc, viết prompt chi tiết để người học sau không gặp lỗi giống mình”): https://app.notion.com/p/41bfcb30974e81b0a8ffd21fd20ff7ab — “Hướng dẫn thực hành v2: dựng 3 skill đúng ngay lần đầu”. Gồm: 30 quy tắc vàng (A phạm vi, B an toàn, C bằng chứng, D cách viết, E kiểm, F bộ nhớ; mỗi quy tắc kèm lỗi thật + câu chặn trong prompt), Prompt nền (18 dòng, dán vào CLAUDE.md), lộ trình 6 chặng (0 bộ nhớ, 1 khám phá, 2 báo cáo HTML + skill 1, 3 SRS + skill 2, 4 phân tích requirement chia 4A–4E + skill 3, 5 ghi TL-xx), mỗi chặng có prompt dán được + cổng nghiệm thu + lỗi đã chặn; thêm mục 3 phép thử skill, công thức feedback 4 phần, bảng triệu chứng → câu dán, bài tập có tiêu chí. **Chưa có người học nào chạy thử** (đã ghi thẳng trên trang). Đây là trang hướng dẫn duy nhất.

## Quyết định người dùng chọn
- Phạm vi chỉ **repo này (ngày 17/11)**, không gồm các phiên cũ ở `D:\Sunny-Agent-Learning`, `D:\Sunny-AI-Testing` (từ 29/10) — nếu sau này muốn thêm thì làm riêng.
- Cấu trúc: 1 trang gốc + 3 database + 1 trang hướng dẫn.

## Điều không suy ra nhanh từ code
- **Ngày giờ lấy từ log phiên**, không phải từ bộ nhớ (bộ nhớ chỉ ghi ngày). Log ở `C:\Users\Admin\.claude\projects\D--AI-build-sunny-agent-version-1\*.jsonl` (giờ UTC, cộng 7 ra giờ Việt Nam). Cách lấy lời nhắn gốc của người dùng: script Python đọc từng dòng JSON, lấy `type == "user"`, bỏ tool_result/system-reminder (script tạm ở scratchpad, không lưu repo).
- Lời nhắn gốc của người dùng có chứa **mật khẩu tài khoản test** (tin nhắn 10:32) — khi tổng hợp phải bỏ, không đưa lên Notion.
- Prompt “Bước 0 dựng bộ nhớ” trong trang hướng dẫn là **mình viết lại**, không phải nguyên văn (log của phiên tạo repo trống) — đã ghi chú trên trang.
- Bẫy khi gõ tiếng Việt vào tham số công cụ: từng gõ nhầm “hiết hạn vay” (đúng: “hết hạn vay”) và “Cap nhật”, “column”, “dây chuyền” (từ người dùng cấm). Sau khi tạo trang phải soát lại chính tả và các từ bị cấm.
- Trang dài (>30k ký tự): tạo trang với phần đầu rồi `insert_content` từng phần (≈10–12k ký tự mỗi lần). Viết tiếng Việt **trực tiếp**, không dùng chuỗi mã `\uXXXX` (lần dùng mã đã dễ gõ nhầm dấu). `notion-fetch` trang dài bị lưu ra tệp: dùng script Python tách `text` rồi quét từ cấm/lỗi chính tả (từ “thiết” khớp nhầm “hiết”, đó là dương tính giả).
- Gọi `notion-create-pages` với JSON quá lớn có thể bị lỗi parse; chia lô ≤ ~8 dòng.

## Khi cần cập nhật
Thêm dòng mới vào đúng database (cột “Thời điểm” dạng ngày giờ có múi giờ +07:00; cột STT để xếp). Nếu feedback mới đổi quy tắc skill, ghi cả “Bản trước” và “Bản sau”.
