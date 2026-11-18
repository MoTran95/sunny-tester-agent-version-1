# Người dùng muốn tài liệu được viết thế nào (chi tiết)
Cập nhật: 2026-11-18 · Liên quan: [working-preferences.md](working-preferences.md), [../conventions/ba-question-wording.md](../conventions/ba-question-wording.md), [../project/srs-process.md](../project/srs-process.md), [../modules/banking-lite/report-v2-html.md](../modules/banking-lite/report-v2-html.md)

Chuyển từ `working-preferences.md` sang đây ngày 2026-11-18 để phần luôn đọc được gọn. Đọc khi viết báo cáo, SRS, bảng soát, checklist hay câu hỏi BA.

## Báo cáo khám phá
- Báo cáo MD có sơ đồ Mermaid, ảnh bằng chứng, luồng end-to-end như người dùng thật; không bịa, chỗ chưa rõ thì hỏi.
- Báo cáo HTML (2026-11-17): giải thích vai trò cho người mới chưa biết lĩnh vực; ảnh có khoanh nút đánh số; sơ đồ luồng đánh số bước 1, 2, 3…; đường end-to-end; điểm mơ hồ phải có lý do + bằng chứng; vẫn không thêm giả định, thiếu thì hỏi.
- **Giao diện báo cáo HTML giữ nguyên như đã chốt ở mọi máy, mọi dự án** (font, màu, cách trình bày; sơ đồ cùng kiểu cho trường hợp tương tự). Người dùng báo 2026-11-18 khi báo cáo tạo trên Mac bị đổi font/màu/sơ đồ; chọn nhúng font Open Sans. Cách làm: [../decisions/decision-log.md](../decisions/decision-log.md), skill `feature-exploration-report` `references/so-do.md`.
- File báo cáo phải mở được ngay trong khung xem trước của app (xem [report-v2-html](../modules/banking-lite/report-v2-html.md)).
- Thuật ngữ IT đúng ngữ cảnh; từ đã bị chê: “giải phẫu”, “dây chuyền”, “tick” (script của skill đã chặn).

## SRS
- Muốn SRS **truy nguồn được** (ID thống nhất, bằng chứng có liên kết) và viết kiểu **story + AC**, không tách nhiều bảng khó đọc (2026-11-17).
- Muốn khám phá **đầy đủ**, chỉ tránh đổi dữ liệu người khác/khóa hệ thống — đừng tự chừa rủi ro nhỏ rồi “bỏ ngõ”. Chi tiết: [../project/srs-process.md](../project/srs-process.md).

## Bảng gửi người dùng/BA (bài học bảng soát `RECO`, 2026-11-17)
Bản đầu viết quá cô đọng (nội dung kiểu “thiếu (Dữ liệu)”, “KN-02”, “M01”, “DSR” không giải thích, không nói người dùng làm gì) → người dùng không hiểu dòng `RECO-S01-AC01`. Quy tắc cho mọi bảng:
- Mỗi dòng có **cột Tình huống** (người dùng làm gì, dữ liệu cụ thể); nội dung bằng **câu đủ ý**.
- **Chép nội dung thông báo thay vì mã** (M01…); giải thích LTV/DSR/thặng dư/“hồ sơ nền” ở bảng thuật ngữ đầu file.
- Không để mã nội bộ (KN-02, CH-03) làm nội dung chính, chỉ để tra chéo; nhãn bằng chữ thường (“Hỏi BA ngay”, “Tự kiểm tra trên hệ thống trước”) thay tên riêng của sách.
- Gộp cột phụ cho bảng gọn (6 cột).
- Cột "Câu hỏi gửi BA" ghi luôn câu BA đã trả lời (người dùng yêu cầu 2026-11-18).

## Checklist / test case
- Câu hỏi BA dựa vào kinh nghiệm (không có dấu vết trong nguồn) phải **tách riêng, hỏi sau khi cần**.
- **Requirement ghi rõ thì suy luận tiếp theo logic, ghi chưa rõ thì hỏi** (người dùng chốt 2026-11-18, sau khi chê A7, A8, B14 của `LOGIN` là "vô tri"). Ghi "suy ra từ <mã/TL>" kèm lý do. Lý do bảo mật được dùng để suy ra hành vi chức năng (ví dụ lỗi đăng nhập báo chung một câu), không tự đặt ca test bảo mật. A4 phần độ dài mã cũng **không cần hỏi**: đăng nhập vì bảo mật chỉ báo đúng hoặc sai, nên không test độ dài ở màn hình đăng nhập (người dùng chỉ ra 2026-11-18). A6 (lần sai thứ 10 hay 11 bị chặn, đăng nhập đúng có đếm lại) **không cần hỏi**: suy ra từ chữ "10 lần liên tiếp"; đi theo câu chữ, hệ thống làm khác thì là nghi lỗi (người dùng chỉ ra 2026-11-18). Chi tiết: skill `phan-tich-requirement`, quy tắc 1b.
- Thêm cột ưu tiên và lý do vì sao cần nhiều test case/câu hỏi.

- **Bảng test case có chỗ ghi khi chạy** (người dùng yêu cầu 2026-11-18): thêm cột Ưu tiên, Kết quả thực tế, Trạng thái, Người viết, rồi Tự động hóa (để lưu script chạy lại, đỡ token). Skill `tao-checklist-test-case` giữ khuôn 12 cột này. Tên người viết mặc định: Sunny Tran.

## Câu hỏi gửi BA
Bài học “câu chữ máy móc, như dịch từ tiếng Anh” (2026-11-17), từ đã chốt, xưng hô và khuôn câu hỏi: [../conventions/ba-question-wording.md](../conventions/ba-question-wording.md).
