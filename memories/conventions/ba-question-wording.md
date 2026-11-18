# Từ ngữ và giọng văn của câu hỏi gửi BA (chung cho mọi dự án)
Cập nhật: 2026-11-18 · Liên quan: [nhieu-du-an.md](nhieu-du-an.md), [../project/skills.md](../project/skills.md), skill `phan-tich-requirement`

Skill `phan-tich-requirement` đọc file này trước khi viết câu hỏi. **Từ riêng của từng dự án** (thuật ngữ nghiệp vụ, nhãn màn hình) nằm ở `memories/modules/<slug>/tu-ngu-cau-hoi-ba.md` của dự án hiện tại; dự án mới chưa có file đó thì hỏi người dùng team/BA dùng từ nào, rồi tạo file. Không lấy từ của dự án khác.

## Xưng hô
- Tự xưng **"mình"**. Gọi BA là **"anh/chị"** (chưa biết giới tính của BA, không đoán).
- Không dùng "người test", "tester" trong câu hỏi gửi BA.

## Quy tắc từ ngữ chung
| Khái niệm | Dùng | Tránh |
|---|---|---|
| Chữ trên màn hình, tên khung, tên ô, nhãn kết quả | giữ nguyên trong dấu ngoặc kép | dịch, viết lại bằng từ khác |
| Phần thập phân của số | "số sau dấu phẩy" | "chữ số thập phân" |
| Điều mình suy đoán | "mình đang hiểu", "mình đoán", "mình chưa chắc" | "giả định", "kết quả mong đợi" |
| Một khái niệm | **một từ** trong cả file | trộn nhãn hệ thống với từ mình tự đặt |

## Khuôn một câu hỏi
Tiêu đề là câu hỏi nói thường. Rồi: kể tình huống thật có số ("Mình thử …") → **Hỏi:** "Anh/chị cho mình hỏi: …" → **Mình đang hiểu:** … → **Vì sao hỏi:** … → ô chọn hoặc ô trả lời. Chi tiết và ví dụ trước/sau: `.claude/skills/phan-tich-requirement/references/viet-cau-hoi-de-doc.md`.

## Vì sao
Người dùng chê bản đầu "tối nghĩa, máy móc như dịch từ tiếng Anh" (2026-11-17), dù câu hỏi đã đủ ý. Nguyên nhân mình đã xác định:
1. Trộn nhãn gốc của hệ thống với từ mình tự đặt nên thuật ngữ không nhất quán (ví dụ cụ thể ở Banking Lite: `memories/modules/banking-lite/tu-ngu-cau-hoi-ba.md`).
2. Câu dài, nhiều danh từ hóa, bố cục kiểu tiếng Anh (“Vấn đề cần BA trả lời”, “Ví dụ cụ thể”).
3. Xưng hô lẫn (“người test”, “mình”, “anh/chị”).

Hướng sửa: chốt một từ cho mỗi khái niệm (hỏi người dùng team/BA hay dùng từ nào, hoặc xin 2–3 tin nhắn thật của BA làm mẫu giọng); câu ngắn nói như chat với đồng nghiệp, số liệu trước, câu hỏi sau; không tự đoán giọng.
