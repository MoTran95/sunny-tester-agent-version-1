---
name: phan-tich-requirement
description: Đọc soát một requirement (file SRS/tài liệu yêu cầu/ticket) để tìm chỗ thiếu, mơ hồ, mâu thuẫn, số liệu sai, chỗ chưa đủ để biết kết quả đúng; lập bảng soát (đã rõ / cần hỏi) kèm trích nguyên văn, rồi soạn file câu hỏi cho BA viết đọc là hiểu (kể tình huống thật, nêu cách mình đang hiểu, xếp nhóm hỏi ngay / hỏi sau / tự kiểm tra). Dừng chờ BA trả lời, không viết checklist hay test case. Dùng khi người dùng (thường là tester) nói "phân tích requirement", "soát requirement", "tìm chỗ mơ hồ/thiếu/mâu thuẫn", "lập bảng soát", "đặt câu hỏi cho BA", "viết câu hỏi gửi BA", "đọc requirement trước khi viết test", hoặc khi có câu trả lời của BA cần cập nhật vào bảng soát. Không dùng để khám phá website (dùng srs-from-website), làm báo cáo HTML (dùng feature-exploration-report), tạo checklist/test case, hay báo lỗi.
---

# Phân tích requirement: bảng soát và câu hỏi cho BA

Làm **một việc**: đọc requirement trước khi viết test, tìm mọi chỗ chưa đủ căn cứ để biết kết quả đúng, rồi biến thành (1) **bảng soát** để tester tự kiểm tra và (2) **file câu hỏi** để mang đi hỏi BA. Xong thì **dừng**, chờ BA trả lời. Checklist và test case là việc của skill khác, sau khi BA trả lời.

Ngôn ngữ: **tiếng Việt**. Nền: cách làm "Tách, Xoay, Lọc" trong sách *Nền Tảng Tester Thời AI* (Phần 1) cộng các bài học từ lần làm thật trên feature Khuyến nghị LTV/DSR (mã `RECO`). Mẫu đã chạy thật: `testing/banking-lite/khuyen-nghi-ltv-dsr/`.

## Quy tắc không được phá (và vì sao)

1. **Chưa có trong requirement thì chưa phải sự thật.** Điều rút từ kinh nghiệm hay kiến thức chung (nghiệp vụ, ngành, luật) chỉ là **câu hỏi**, không phải quy tắc. *Vì AI hay tự điền chỗ bỏ ngỏ và trông rất chuyên nghiệp.*
2. **Giữ mã requirement sẵn có** (`RECO-S01-AC01`…). Chỉ gán R1, R2… theo thứ tự xuất hiện khi tài liệu chưa có mã. *Để truy vết về sau.*
3. **Trích nguyên văn thì chép đúng từng ký tự, rồi để script kiểm.** Không viết lại câu trong dấu trích.
4. **Tính lại mọi con số và công thức** trong requirement bằng một script nhỏ. *Lần `RECO` bắt được 2 chỗ tài liệu tự lệch (ca "đúng 70,00%" thật ra hơn 70%; một kết quả sai 39.333.333) mà đọc bằng mắt không thấy.*
5. **Chỉ xét chức năng (functional).** Không tự suy diễn bảo mật, hiệu năng, trừ khi requirement nói tới.
6. **Câu hỏi phải đọc là hiểu**: kể tình huống thật có số, rồi hỏi, rồi nói mình đang hiểu thế nào. Một từ cho một khái niệm. Không để mã nội bộ (CH-02, M01) làm nội dung chính. Xem `references/viet-cau-hoi-de-doc.md`. *Bản đầu bị chê "không hiểu đang nói gì", rồi "máy móc như dịch từ tiếng Anh".*
7. **Không tự trả lời thay BA.** "Mình đang hiểu" luôn nói rõ khi đó là đoán. Quyết định của người dùng (ví dụ chọn cách làm tròn) ghi là **câu trả lời có nguồn "người dùng chốt, chưa có BA xác nhận"**, không nâng thành sự thật.
8. **Ghi hết vào bảng, nhưng hỏi có chọn lọc**: ba nhóm hỏi ngay / hỏi sau / tự kiểm tra trước. *Gửi BA mười mấy câu cùng lúc thì câu quan trọng bị chìm.*
9. **Một nguồn câu chữ**: câu hỏi viết **một lần** ở file câu hỏi; bảng soát chỉ ghi số câu, tiêu đề và nhóm (cộng câu BA đã trả lời, nếu có), **không chép lại** phần Hỏi/Mình đang hiểu. Script kiểm tiêu đề khớp. *Chép lại làm bảng phình gấp rưỡi và mỗi lần sửa phải đọc lại cả bảng.*
10. **Đừng làm quá việc được giao.** Chưa được yêu cầu thì không dựng checklist, test case, ưu tiên. *Lần `RECO` mình dựng 62 test case khi người dùng chỉ cần phân tích và hỏi BA.*
11. **Làm từng bước nhỏ, hỏi khi chưa rõ** (tối đa 3 câu khi không làm tiếp được). Từ nghe lệch thì hỏi lại nghĩa.

## Đọc gì cho từng việc
Luôn đọc: `memories/user/working-preferences.md`, `memories/project/overview.md`. Thêm theo việc:

| Việc | Đọc | Không cần đọc |
|---|---|---|
| Phân tích requirement mới | File requirement (cả file). Bộ nhớ: `memories/conventions/ba-question-wording.md`, `memories/modules/<hệ thống>/feature-<tên>.md` nếu có. Skill: `references/quy-trinh-tach-xoay-loc.md`, `quy-tac-nguon-va-tra-loi.md`, `viet-cau-hoi-de-doc.md`, `bai-hoc.md`, hai file trong `assets/` | Bảng soát, câu hỏi của feature khác; `scripts/kiem-tra.py` (chỉ chạy, không đọc) |
| Ghi câu trả lời BA (`TL-xx`) | Bộ nhớ của feature. `references/quy-tac-nguon-va-tra-loi.md` mục 4. Trong bảng soát: chỉ mục 3 và các dòng `--tim` chỉ ra. Trong file câu hỏi: chỉ khối của câu được trả lời (tìm `## A4.`). Requirement: chỉ đoạn của mã liên quan | Cả bảng soát, cả file câu hỏi, cả requirement; các file references khác. Đọc thêm `viet-cau-hoi-de-doc.md` **chỉ khi** phải viết câu hỏi mới |
| Sửa câu chữ một câu hỏi | Khối câu đó trong file câu hỏi, `memories/conventions/ba-question-wording.md`, `references/viet-cau-hoi-de-doc.md` | Bảng soát (chỉ sửa tiêu đề nếu tiêu đề đổi, dùng `--tim`) |
| Sửa chính skill này | `memories/project/skills.md`, file cần sửa | Sản phẩm trong `testing/` |

File trên ~30 KB mà chỉ cần một phần: tìm bằng Grep rồi đọc đoạn đó (`offset`/`limit`), đừng đọc cả file.

## Quy trình

0. **Đọc đúng những file cần cho việc này** (bảng "Đọc gì cho từng việc" ngay dưới), sau `CLAUDE.md` và `memories/MEMORY.md`. Không đọc thêm cho chắc.
1. **Chốt đầu vào** (hỏi nếu thiếu): đường dẫn requirement; hệ thống và feature; requirement đã có mã chưa; đã có bản phân tích trước chưa (có thì sang "Khi có câu trả lời"). Nếu `ba-question-wording.md` thiếu hoặc người dùng muốn đổi từ ngữ thì hỏi: xưng hô, từ team dùng cho các khái niệm chính, rồi cập nhật file đó.
2. **Đọc để hiểu**, rồi liệt kê mọi đơn vị cần soát (mỗi AC, quy tắc, thông báo là một đơn vị). Dùng năm câu tự hỏi và sáu dấu hiệu lấn cấn trong `references/quy-trinh-tach-xoay-loc.md`.
3. **Tính lại số liệu** bằng script nhỏ (để trong thư mục tạm, không lưu vào repo). Ghi các chỗ lệch.
4. **Soát từng đơn vị**: Tách (một ý một mã) → Xoay (qua sáu nút, chỉ nút liên quan) → Lọc. Quyết ✅ đã rõ hay ❓ cần hỏi theo `references/quy-trinh-tach-xoay-loc.md`. Chỗ rõ một nửa thì tách hai dòng.
5. **Soạn file câu hỏi** `testing/<hệ thống>/<feature>/cau-hoi-cho-ba.md` theo `assets/mau-cau-hoi-cho-ba.md` và `references/viet-cau-hoi-de-doc.md`. Chia Phần A (hỏi ngay), B (hỏi sau), C (tự kiểm tra trước).
6. **Lập bảng soát** `testing/<hệ thống>/<feature>/bang-soat-requirement.md` theo `assets/mau-bang-soat.md`. Cột câu hỏi chỉ ghi `**A1. <tiêu đề>** (<nhóm>)`, tiêu đề đúng chữ như ở file câu hỏi.
7. **Kiểm bằng script**, sửa hết lỗi:
   ```bash
   python -X utf8 .claude/skills/phan-tich-requirement/scripts/kiem-tra.py \
     --nguon <file requirement> \
     --bang-soat testing/<hệ thống>/<feature>/bang-soat-requirement.md \
     --cau-hoi testing/<hệ thống>/<feature>/cau-hoi-cho-ba.md \
     --ma "<biểu thức chính quy của mã, ví dụ RECO-S\d\d-AC\d\d>"
   ```
   Script báo: bảng lệch số cột, trích dẫn không khớp nguyên văn, mã requirement chưa có mặt, câu hỏi thiếu trường, bảng soát lệch với file câu hỏi, từ dịch máy và mã nội bộ lọt vào câu hỏi. Rồi soát tay: đọc to vài câu hỏi xem có nghe lạ không; mở thử file trong khung xem trước.
8. **Cập nhật bộ nhớ**: `memories/modules/<hệ thống>/feature-<tên>.md` (điều học được, bẫy, trạng thái), một dòng trong `MEMORY.md`.
9. **Trả lời người dùng** bằng tóm tắt ngắn và link file (không dán cả bảng vào chat): số dòng ✅ và ❓, các câu nhóm hỏi ngay, chỗ cần họ quyết, việc họ làm tiếp. Nói rõ **chưa gửi BA** và chưa viết checklist hay test case. Rồi dừng.

## Khi có câu trả lời (từ BA hoặc người dùng)

**Không đọc lại cả bảng soát.** Chạy `kiem-tra.py … --tim A4,<mã requirement liên quan>` để lấy số dòng cần sửa, chỉ đọc các dòng đó (`Read` với `offset`/`limit`) và sửa bằng `Edit`. Ghi mỗi câu trả lời thành `TL-xx` trong mục "Câu trả lời đã nhận" của bảng soát: nội dung, **nguồn** (ai nói, ngày, ở đâu), áp dụng cho mã nào, còn lại gì. Đổi các dòng ❓ liên quan thành ✅ "theo TL-xx". Nếu hệ thống hiện tại cho kết quả khác câu trả lời, ghi "khác hệ thống hiện tại" và **không tự kết luận lỗi** (chỉ là nghi lỗi nếu BA xác nhận). Nếu câu trả lời làm đổi số hiển thị, liệt kê số nào đổi. Ở cột "Câu hỏi gửi BA" của các dòng liên quan, thêm dòng `**BA trả lời:** <nguyên văn> (TL-xx)` ngay sau tiêu đề câu hỏi (người dùng yêu cầu 2026-11-18). Hỏi **ai là người chốt**; quyết định của tester chưa có BA xác nhận thì nói rõ như vậy và đưa vào Phần A để BA xác nhận. Không sửa SRS tại chỗ khi chưa có BA hoặc team xác nhận. Chi tiết: `references/quy-tac-nguon-va-tra-loi.md`.

## Tệp trong skill
- `references/quy-trinh-tach-xoay-loc.md` — năm câu tự hỏi, sáu dấu hiệu, sáu nút (chỉ chức năng), cách quyết ✅/❓, ba nhóm câu hỏi, cách tính lại số liệu.
- `references/quy-tac-nguon-va-tra-loi.md` — nhãn nguồn, cách trích nguyên văn, mã requirement, ghi câu trả lời `TL-xx`, quyết định của người dùng.
- `references/viet-cau-hoi-de-doc.md` — khuôn câu hỏi, giọng văn, từ ngữ, ví dụ trước và sau, danh sách tự kiểm.
- `references/bai-hoc.md` — các bẫy đã gặp (bảng hỏng, làm quá, câu chữ máy móc…).
- `assets/mau-bang-soat.md`, `assets/mau-cau-hoi-cho-ba.md` — khuôn hai file đầu ra (nhãn trường là cố định để script đọc).
- `scripts/kiem-tra.py` — soát đầu ra.
- Bộ nhớ ngoài skill: `memories/conventions/ba-question-wording.md` (xưng hô, từ đã chốt).
