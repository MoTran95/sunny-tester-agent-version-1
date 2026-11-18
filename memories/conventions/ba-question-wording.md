# Từ ngữ và giọng văn của câu hỏi gửi BA
Cập nhật: 2026-11-17 · Liên quan: [../project/srs-process.md](../project/srs-process.md), [../project/skills.md](../project/skills.md), skill `phan-tich-requirement`

**Tình trạng:** giá trị tạm chốt cùng người dùng ở phiên làm feature `RECO`. Người dùng đã duyệt giọng mẫu nhưng **chưa nói team thật dùng từ nào**, nên đây là mặc định của mình; sửa ngay khi họ báo. Skill `phan-tich-requirement` đọc file này trước khi viết câu hỏi; nếu thiếu hoặc người dùng muốn đổi thì hỏi lại rồi cập nhật tại đây.

## Xưng hô
- Tự xưng **"mình"**. Gọi BA là **"anh/chị"** (chưa biết giới tính của BA, không đoán).
- Không dùng "người test", "tester" trong câu hỏi gửi BA.

## Từ đã chốt (mỗi khái niệm một từ)
| Khái niệm | Dùng | Tránh |
|---|---|---|
| Giới hạn tối đa của một chỉ số | "mức tối đa", "mức tối thiểu" | "ngưỡng", "hạn mức" (trộn lẫn) |
| Lúc kết thúc khoản vay | "hết hạn vay" | "đáo hạn" trong lời mình viết. Khi **trích chữ đang hiện trên màn hình** (ví dụ "Tuổi cao nhất khi đáo hạn") thì giữ nguyên trong dấu ngoặc kép |
| Nhãn kết quả của hệ thống | giữ nguyên: Phê duyệt, Chuyển cấp trên, Từ chối | dịch hoặc đổi tên |
| Chữ trên màn hình, tên khung, tên ô | giữ nguyên trong dấu ngoặc kép | viết lại bằng từ khác |
| Phần thập phân của số | "số sau dấu phẩy" | "chữ số thập phân" |
| Hệ thống từ chối tạm sau nhiều lần đăng nhập sai (feature `LOGIN`) | "bị chặn" (khớp chữ trên màn hình "Too many failed attempts") | "bị khóa" (dễ hiểu thành khóa tài khoản). Dùng 2026-11-17, cũng là mặc định của mình |
| Điều mình suy đoán | "mình đang hiểu", "mình đoán", "mình chưa chắc" | "giả định", "kết quả mong đợi" |

Thêm dòng mới vào bảng khi người dùng chọn từ cho một khái niệm mới.

## Khuôn một câu hỏi
Tiêu đề là câu hỏi nói thường. Rồi: kể tình huống thật có số ("Mình thử …") → **Hỏi:** "Anh/chị cho mình hỏi: …" → **Mình đang hiểu:** … → **Vì sao hỏi:** … → ô chọn hoặc ô trả lời. Chi tiết và ví dụ trước/sau: `.claude/skills/phan-tich-requirement/references/viet-cau-hoi-de-doc.md`.

## Vì sao
Người dùng chê bản đầu "tối nghĩa, máy móc như dịch từ tiếng Anh" (2026-11-17), dù câu hỏi đã đủ ý. Nguyên nhân mình đã xác định:
1. Trộn nhãn gốc của hệ thống (“đáo hạn”, “thặng dư hằng tháng”, “khoản trả mới theo lãi suất thẩm định”) với từ mình tự đặt (“hết hạn vay”, “hạn mức”, “ngưỡng”, “kết quả mong đợi”) nên thuật ngữ không nhất quán.
2. Câu dài, nhiều danh từ hóa, bố cục kiểu tiếng Anh (“Vấn đề cần BA trả lời”, “Ví dụ cụ thể”).
3. Xưng hô lẫn (“người test”, “mình”, “anh/chị”).

Hướng sửa: chốt một từ cho mỗi khái niệm (hỏi người dùng team/BA hay dùng từ nào, hoặc xin 2–3 tin nhắn thật của BA làm mẫu giọng); câu ngắn nói như chat với đồng nghiệp, số liệu trước, câu hỏi sau; không tự đoán giọng. Người dùng đã duyệt giọng mẫu A1, A2 (“Ổn, viết hết”) → đã viết lại cả 31 câu của `RECO`.
