# Sở thích làm việc của người dùng
Cập nhật: 2026-11-17

- Giao tiếp bằng **tiếng Việt**.
- Muốn bộ nhớ lưu **ngay trong repo** (`memories/`), không để ở nơi khác.
- Muốn bộ nhớ chia nhỏ theo module/phần, đặt tên rõ ràng, không để một file phình to.
- Mỗi khi giao việc làm chức năng: phải đọc `CLAUDE.md` → `memories/MEMORY.md` → các file bộ nhớ liên quan, rồi mới làm, để không thiếu thông tin.

- Người dùng là tester; muốn báo cáo MD có sơ đồ Mermaid, ảnh bằng chứng, luồng end-to-end như người dùng thật; không bịa, chỗ chưa rõ thì hỏi.
- Báo cáo bản HTML (2026-11-17): giải thích vai trò cho người mới chưa biết lĩnh vực; ảnh có khoanh nút đánh số; sơ đồ luồng đánh số bước 1,2,3…; đường end-to-end; điểm mơ hồ phải có lý do + bằng chứng; vẫn không thêm giả định, thiếu thì hỏi.
- Dùng đúng thuật ngữ chuyên ngành IT, tránh từ khó hiểu hoặc sai ngữ cảnh (ví dụ không dùng “giải phẫu”, “dây chuyền”, “tick”); file báo cáo phải mở được ngay trong khung xem trước của app (xem [report-v2-html](../modules/banking-lite/report-v2-html.md)).
- Muốn lưu tài khoản test vào file `.env` ở gốc repo (đã làm 2026-11-17, có `.gitignore`).

- Làm **từng bước nhỏ rồi ghép lại** để thử nghiệm, không dựng cả quy trình một lúc; chỗ nào chưa rõ phải **hỏi lại, không tự suy diễn** (2026-11-17). Người dùng nói theo giọng nói nên có từ nghe lệch (“thiết khai”, “sự khoai mạnh”) — hỏi lại nghĩa.
- Người dùng từng hỏi mình tự đăng nhập/nhập mật khẩu sai qua Playwright hay trực tiếp: mình **không gõ mật khẩu** (kể cả sai), người dùng tự gõ; mình điền sẵn ô Mã nhân viên rồi đọc kết quả.

- Muốn SRS **truy nguồn được** (ID thống nhất, bằng chứng có liên kết) và viết kiểu **story + AC**, không tách nhiều bảng khó đọc (2026-11-17). Muốn khám phá **đầy đủ**, chỉ tránh đổi dữ liệu người khác/khóa hệ thống — đừng tự chừa rủi ro nhỏ rồi “bỏ ngõ”.

- **Quy tắc an toàn khi thao tác trên hệ thống đang test (mọi feature):** không làm việc có thể **khóa hệ thống/tài khoản, đổi dữ liệu của người khác** hoặc kích hoạt giới hạn (đăng nhập sai lặp lại, gửi hàng loạt yêu cầu…). Nếu một ca test có thể lặp lại thao tác như vậy → tối đa **3 lần**, kiểm tra phản hồi sau từng lần (không chạy lô), rồi **dừng và hỏi người dùng** trước khi tiếp tục; không tự nâng ngưỡng; không giả định “dùng dữ liệu giả thì an toàn”. Lỡ kích hoạt thì báo thẳng ngay, nói rõ ảnh hưởng. Chi tiết sự cố: [pitfalls/dont-trigger-lockouts.md](../pitfalls/dont-trigger-lockouts.md) (2026-11-17, người dùng đã nhắc và phải nhắc lại).
- Tài liệu phải **đọc là hiểu**: không dùng thuật ngữ kiểm thử/viết tắt khó hiểu (Given/When/Then, FR/BR, NK#, DN-…) làm tên cột hay nhãn; giải thích hoặc dùng tiếng Việt thường, câu đầy đủ (2026-11-17).

- Kết quả phân tích/checklist **dài thì lưu thành file trong repo, không dán cả bảng vào khung chat** (khó đọc) — chat chỉ tóm tắt + link (2026-11-17). Chỉ test **functional**, không tự suy diễn bảo mật/hiệu năng. Câu hỏi BA dựa vào kinh nghiệm (không có dấu vết trong nguồn) phải **tách riêng, hỏi sau khi cần**; thêm cột ưu tiên và lý do vì sao cần nhiều TC/câu hỏi.

- **Bài học 2026-11-17 (bảng soát RECO):** bản đầu viết quá cô đọng (nội dung kiểu “thiếu (Dữ liệu)”, “KN-02”, “M01”, “DSR” không giải thích, không nói người dùng làm gì) → người dùng không hiểu dòng `RECO-S01-AC01`. Quy tắc cho mọi bảng gửi người dùng/BA: mỗi dòng có **cột Tình huống** (người dùng làm gì, dữ liệu cụ thể), nội dung bằng **câu đủ ý**, **chép nội dung thông báo thay vì mã** (M01…), giải thích LTV/DSR/thặng dư/“hồ sơ nền” ở bảng thuật ngữ đầu file, không để mã nội bộ (KN-02, CH-03) làm nội dung chính (chỉ để tra chéo), dùng nhãn bằng chữ thường (“Hỏi BA ngay”, “Tự kiểm tra trên hệ thống trước”) thay tên riêng của sách. Gộp cột phụ cho bảng gọn (6 cột).

- **Câu chữ nghe “máy móc, như dịch từ tiếng Anh” (2026-11-17):** người dùng chê câu hỏi BA dù đã đủ ý. Nguyên nhân mình xác định: (1) trộn nhãn gốc của hệ thống (“đáo hạn”, “thặng dư hằng tháng”, “khoản trả mới theo lãi suất thẩm định”) với từ mình tự đặt (“hết hạn vay”, “hạn mức”, “ngưỡng”, “kết quả mong đợi”) nên thuật ngữ không nhất quán; (2) câu dài, nhiều danh từ hóa, bố cục kiểu tiếng Anh (“Vấn đề cần BA trả lời”, “Ví dụ cụ thể”); (3) xưng hô lẫn (“người test”, “mình”, “anh/chị”). Hướng sửa đang đề xuất: chốt 1 từ cho mỗi khái niệm (hỏi người dùng team/BA hay dùng từ nào, hoặc xin 2–3 tin nhắn thật của BA làm mẫu giọng), câu ngắn nói như chat với đồng nghiệp (số liệu trước, câu hỏi sau, xưng “mình”, gọi BA “anh/chị” vì chưa biết giới), không để mình tự đoán giọng. **Người dùng đã duyệt giọng mẫu A1, A2 (2026-11-17, “Ổn, viết hết”) → đã viết lại cả 31 câu**, tạm chốt từ: “mức tối đa”, “hết hạn vay” (giữ “đáo hạn” khi trích chữ trên màn hình); người dùng chưa trả lời câu hỏi về từ team dùng nên đây là mặc định của mình, sửa khi họ báo. Khuôn mới: tiêu đề là câu hỏi nói thường → kể tình huống thật có số (“Mình thử…”) → **Hỏi:** “Anh/chị cho mình hỏi: …” → **Mình đang hiểu:** (nói “mình đoán/chưa chắc” khi suy đoán) → **Vì sao hỏi:** → ô chọn/trả lời. Giữ nguyên nhãn gốc của hệ thống (Phê duyệt, Chuyển cấp trên, Từ chối, Khung Thẩm định).

- **Tài liệu hành trình + content (2026-11-17):** người dùng muốn lưu quá trình làm việc dạng **database có ngày giờ trên Notion** (nhật ký, feedback trước/sau, lỗi + cách giải quyết) và hướng dẫn để dạy người mới dựng lại skill; coi lỗi/feedback là chất liệu content quảng bá sản phẩm. Chi tiết: [../project/notion-journey-page.md](../project/notion-journey-page.md). Khi có feedback/lỗi lớn mới, nên bổ sung vào các database đó nếu người dùng nhờ.

**Why:** người dùng muốn ngữ cảnh được giữ bền vững qua các phiên và không bị sót.
**How to apply:** luôn theo quy trình trong `CLAUDE.md`; ghi thêm sở thích mới vào file này.
