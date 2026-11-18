# Quy tắc viết test case chi tiết

## Khuôn bảng (12 cột, tiêu đề cố định để script đọc)
`| Mã | Tình huống | Ưu tiên | Điều kiện trước | Các bước | Dữ liệu test | Kết quả mong đợi | Nguồn | Kết quả thực tế | Trạng thái | Người viết | Tự động hóa |`

- **Mã, Tình huống, Ưu tiên, Nguồn:** lấy **nguyên văn** từ checklist (script tự điền). Mỗi mã TC của checklist = một test case riêng.
- **Điều kiện trước:** trạng thái hệ thống, tài khoản, dữ liệu cần có; trạng thái giao diện (ngôn ngữ, đã/chưa đăng nhập). Trạng thái phải **đạt được bằng cách làm** (nếu cần "đang bị chặn" thì ghi cách tạo trạng thái đó), để case chạy riêng được.
- **Các bước:** mỗi bước **một thao tác**, đánh số 1, 2, 3 từ bước đầu tiên (mở đúng địa chỉ). Không "như TC-xxx", không bỏ bước đầu. Lặp lại thao tác thì viết rõ từng lần ("Lần sai thứ 3: …").
- **Dữ liệu test:** giá trị cụ thể từng lần nhập. Dữ liệu giả (email `@example.com`, chuỗi giả như `Sai@Matkhau1`). Tài khoản có thật của hệ thống đang test chỉ ghi mã; mật khẩu thật **không** ghi vào tài liệu ("do người dùng cung cấp, người kiểm thử tự nhập").
- **Kết quả mong đợi:** viết thẳng câu chữ, con số, trạng thái cần thấy, **mở đầu bằng "Bước N:"** cho bước có kết quả. Mọi câu chữ và con số lấy từ nguồn (copy đúng dấu câu, dấu tiếng Việt). **Mã requirement/câu trả lời không viết trong cột này.**
- **Nguồn:** như checklist.
- **Kết quả thực tế, Trạng thái, Người viết, Tự động hóa:** để người chạy test điền. Mặc định: ` ` (trống), `Chưa chạy`, `Sunny Tran` (người dùng chốt 2026-11-18; `sinh-bang.py --nguoi-viet` đổi được cho người khác). **Trạng thái chọn một:** `Chưa chạy`, `Đạt`, `Không đạt`, `Bị chặn`, `Bỏ qua`. Kết quả thực tế ghi điều thấy ở bước nào, số liệu, ảnh chụp nếu có; thấy khác kết quả mong đợi mà kết quả mong đợi theo BA thì ghi "nghi lỗi", chưa phải lỗi đã xác nhận.

## Cột Tự động hóa (người dùng yêu cầu 2026-11-18)
Sau khi chạy test case mà thấy **ca nào lưu được script chạy lại không cần AI** (đỡ token) thì ghi vào cột này; mặc định `Chưa có`. Chỉ ba dạng:
- `Chưa có`
- `Có: <đường dẫn từ gốc repo>` — ví dụ `Có: testing/<hệ thống>/<feature>/auto/TC-006.py`. Quy ước thư mục `auto/` cạnh `test-case.md`, tên file theo mã TC. Chỉ ghi `Có:` khi script **đã chạy được**.
- `Không tự động được: <lý do>` — ví dụ cần người gõ mật khẩu, hoặc ca cố ý làm sai nhiều lần dễ khóa tài khoản.
Quy tắc khi viết script: (1) **không chứa mật khẩu thật**, đọc từ `.env` của dự án (khóa có tiền tố theo dự án) và chỉ khi người dùng đã đồng ý cho script nhập mật khẩu; (2) ca có thể khóa tài khoản/đổi dữ liệu người khác: script phải dừng hỏi xác nhận, không tự lặp; (3) đầu script ghi mã TC, ngày viết, bản hệ thống và `nguồn: test-case.md`; (4) ca chỉ cần nhìn một màn hình thì không đáng làm script. Khi test case chuyển sang **Cần xem lại** mà đã có script, `truy-vet.md` báo "script cần xem lại": sửa script cùng lúc với test case. Điền cột này **không** làm test case bị tính là đã sửa. Công cụ chạy (Playwright hay gọi API bằng Python) chưa chọn; hỏi người dùng khi bắt đầu viết script đầu tiên.

## Mỗi case một mục tiêu
- Một case chỉ thử **một giá trị không hợp lệ** hoặc **một đường không được phép**. Checklist gộp nhiều giá trị: chọn giá trị đầu, các giá trị còn lại ghi vào "Ghi nhận riêng" (không tự thêm TC). Giá trị **hợp lệ** nhiều lần thì được giữ trong một case (ví dụ đăng nhập lần lượt hai tài khoản đúng).
- Mỗi case độc lập: đủ điều kiện trước, bước, dữ liệu, kết quả; không tham chiếu case khác.

## Chỗ nguồn không đủ
Ghi `CẦN XÁC NHẬN` đúng chỗ thiếu trong kết quả mong đợi (kèm "xem Câu hỏi cho BA, câu N"), **không tự điền**. Cuối file có `## Câu hỏi cho BA`: mỗi câu gồm tình huống có số liệu, cách mình đang hiểu, và mã TC/mã requirement liên quan. Không có câu hỏi thì ghi "Không có.". Script kiểm: mọi TC có `CẦN XÁC NHẬN` phải có trong mục này.

## Giá trị do người viết chọn
Con số không có trong nguồn nhưng cần để kiểm (mốc "ngay trước 5 phút" → "4 phút 50 giây") thì ghi rõ trong Dữ liệu test là "giá trị chọn để kiểm; nguồn chỉ nêu mốc 5 phút", và nhắc ở "Ghi nhận riêng".

## Ca có thể gây khóa hoặc đổi dữ liệu người khác
Ghi ở điều kiện trước: "Ca này cố ý nhập sai N lần: chỉ chạy khi người dùng đã đồng ý." Skill chỉ viết, không chạy.

## Cập nhật khi requirement đổi
1. Chạy `python -X utf8 scripts/truy-vet.py kiem <dự-án> <feature>`: liệt kê mã đã đổi và test case chuyển sang **Cần xem lại**.
2. Chỉ đọc requirement phần mã đã đổi và các test case được báo. Sửa test case; mã TC giữ nguyên.
3. Requirement thêm tình huống mới → TC mới lấy **số kế tiếp** trong checklist (hỏi người dùng trước khi thêm); bỏ tình huống → hỏi trước, **không xóa dòng**: ghi "Đã bỏ theo requirement mới" ở Kết quả thực tế và Trạng thái `Bỏ qua`.
4. `sinh-bang.py test-case` chạy lại sẽ **giữ** Kết quả thực tế, Trạng thái, Người viết theo mã; nhưng đã có file thì thường chỉ cần sửa dòng bằng Edit.
5. Chạy `kiem-tra-tc.py`, rồi `truy-vet.py chot -m "<đã làm gì, vì sao>"`. Điền kết quả khi chạy test **không** làm test case bị tính là đã sửa (script bỏ qua bốn cột đó).

## Tự kiểm trước khi trả lời (script làm phần cơ học)
- Số lượng và mã khớp 100% với checklist, mỗi mã một lần.
- Không "như TC-xxx", không nhắc mã TC khác. Case nào cũng có điều kiện trước.
- Không có mã requirement trong Kết quả mong đợi; "Bước N" nằm trong số bước.
- Mỗi `CẦN XÁC NHẬN` có trong "Câu hỏi cho BA". Dữ liệu giả. Không có mật khẩu thật.
