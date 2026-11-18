---
name: srs-from-website
description: Khám phá một website/web app bằng thao tác thật rồi viết tài liệu SRS bằng Markdown cho từng feature, kiểu User story + tiêu chí chấp nhận (AC), mỗi yêu cầu có ID cố định và bằng chứng truy được (ảnh, Network, tệp giao diện, nhật ký). Dùng bất cứ khi nào người dùng (thường là tester) nói "tạo SRS từ website", "viết SRS/requirement cho feature X", "khám phá rồi làm tài liệu yêu cầu", "chuyển khám phá thành SRS", "cập nhật SRS vì feature đổi", "soát SRS", kể cả khi họ không nói chữ SRS mà muốn có tài liệu mô tả hành vi hệ thống để sau này viết test case. Không dùng cho báo cáo khám phá dạng HTML (dùng feature-exploration-report), báo cáo lỗi, hay viết test case.
---

# SRS từ website (Markdown, Story + AC)

Biến một lượt khám phá **thật** trên website thành một file SRS **truy được nguồn**: người mới đọc là hiểu, và sau này test case gắn thẳng vào từng ID. SRS ở đây ghi **hành vi quan sát được**, chưa phải yêu cầu nghiệp vụ chính thức.

Ngôn ngữ: **tiếng Việt**, câu đầy đủ, dễ hiểu. Mẫu đã chạy thật (dự án Banking Lite, chỉ mở khi đang làm dự án đó): `srs/banking-lite/dang-nhap.md` (nhật ký + ảnh ở `evidence/banking-lite/features/dang-nhap/`).

## Quy tắc không được phá (và vì sao)

1. **Chỉ ghi điều đã nhìn thấy.** Chưa chắc → nhãn `chưa rõ` + câu hỏi cho team. Không kết luận "lỗi" hay "đúng thiết kế" khi chưa có tài liệu nghiệp vụ. *Vì SRS làm nền cho test; một điều bịa sẽ thành test sai.*
2. **Mật khẩu do người dùng gõ — kể cả mật khẩu sai.** Mình điền sẵn ô mã, người dùng gõ mật khẩu và báo "xong", mình đọc kết quả. Cách làm chi tiết: `references/safety-and-collaboration.md`.
3. **Không làm khóa hệ thống hay đổi dữ liệu của người khác.** Thao tác lặp có thể kích hoạt giới hạn → **tối đa 3 lần, kiểm tra từng lần, rồi dừng và hỏi.** *Từng làm 10 lần đăng nhập sai bằng mã "giả" và bị chặn 5 phút; "dữ liệu giả thì an toàn" là giả định sai.*
4. **Hỏi trước** khi tạo/sửa dữ liệu thật, tải file, gây SMS/email, hoặc bấm Đăng xuất làm mất phiên của người dùng.
5. **Mỗi yêu cầu có bằng chứng truy được**, ghi đúng loại (ảnh / quan sát bằng công cụ / tệp giao diện). Không có ảnh thì nói "không có ảnh" và chỉ cách kiểm lại. *Người dùng từng không truy được các mã nguồn viết tắt.*
6. **Đọc là hiểu**: tiếng Việt thường, không dùng thuật ngữ kiểm thử/viết tắt khó (Given/When/Then, FR/BR, `NK#`…) làm tên cột hay nhãn.
7. **Khám phá đầy đủ.** Mục "Chưa khám phá" chỉ chứa ca có **lý do thật** (cần người dùng gõ mật khẩu, chờ thời gian, thiếu tài khoản, có thể gây khóa, **bị công cụ chặn**). "Ngại rủi ro nhỏ / hơi lâu / giá trị thấp" không phải lý do. Thao tác bị công cụ chặn → **không đi đường vòng**, ghi vào "Chưa khám phá" kèm lý do (`references/safety-and-collaboration.md` mục 6).
8. **Làm từng bước nhỏ, hỏi khi chưa rõ.** Từ nghe lệch (người dùng nói bằng giọng nói) → hỏi lại nghĩa, không đoán.
9. **Đã khám phá rồi thì KHÔNG khám phá lại.** Chỉ mở trình duyệt khám phá lại khi **người dùng nói rõ** "khám phá lại" hoặc "feature đã đổi" (và đổi phần nào). Tự thấy "nên kiểm lại cho chắc" không phải lý do. *Người dùng hết token để chạy lại; khám phá là bước tốn nhất (100–400 lượt gọi, hàng chục ảnh).* Cách kiểm xem đã khám phá chưa: bước 2.

## Đọc gì cho từng việc
Luôn đọc: `memories/user/working-preferences.md`, `memories/project/overview.md`, và `memories/modules/<slug>/overview.md` của **dự án hiện tại** (slug trong `.du-an-hien-tai`; chưa có thì hỏi người dùng trước, xem `CLAUDE.md` bước 0). `<hệ thống>` trong các đường dẫn dưới đây chính là slug đó. **Không mở file của dự án khác, kể cả để làm mẫu**: dùng khuôn trong `assets/` (và `srs/_template.md`). Thêm theo việc:

| Việc | Đọc | Không cần đọc |
|---|---|---|
| Khám phá + viết SRS cho feature mới | Bộ nhớ: `memories/modules/<hệ thống>/exploration-findings.md`, `feature-<tên>.md` nếu có, `memories/pitfalls/dont-trigger-lockouts.md`. Khi khám phá: `references/exploration-checklist.md`, `references/safety-and-collaboration.md`, `assets/exploration-log-template.md`. Khi viết: `srs/_template.md`, `srs/id-and-source-rules.md`, `references/srs-writing-guide.md` | SRS và nhật ký của feature khác (chỉ mở một đoạn nếu cần xem mẫu); `scripts/check-srs.py` (chỉ chạy) |
| Cập nhật SRS vì feature đổi | SRS hiện có, nhật ký gốc của feature, bộ nhớ của feature, `references/srs-writing-guide.md` mục 6, `references/safety-and-collaboration.md` | `srs/_template.md` (SRS đã theo khuôn), feature khác |
| Soát một SRS có sẵn | Chạy `scripts/check-srs.py`; đọc SRS ở các dòng script báo. Sửa thì đọc thêm `references/srs-writing-guide.md` | Nhật ký và ảnh, trừ khi phải kiểm lại một nguyên văn |
| Sửa chính skill này | `memories/project/skills.md`, `memories/project/srs-process.md`, file cần sửa | SRS và bằng chứng |

File trên ~30 KB mà chỉ cần một phần: tìm bằng Grep rồi đọc đoạn đó (`offset`/`limit`), đừng đọc cả file.

## Quy trình

0. **Đọc đúng những file cần cho việc này** (bảng "Đọc gì cho từng việc" ngay dưới), sau `CLAUDE.md` và `memories/MEMORY.md`. Không đọc thêm cho chắc.
1. **Chốt phạm vi** (hỏi nếu thiếu): feature; URL + phiên bản; tài khoản và vai trò đã biết; được phép tạo dữ liệu test không; tích hợp bên ngoài thật hay mô phỏng; **mã feature** (2–8 chữ HOA tiếng Anh, ví dụ `LOGIN`); đã có SRS cho feature này chưa → nếu có, xem "Cập nhật SRS".
2. **Cổng khám phá — làm trước khi mở trình duyệt.** Tìm bằng Glob/Grep nhật ký đã có: `evidence/<hệ thống>/features/<feature>/bao-cao.md` và `evidence/<hệ thống>/bao-cao-kham-pha.md` (báo cáo tổng, dò theo tên feature).
   - **Đã có và đủ:** chạy `python -X utf8 .claude/skills/srs-from-website/scripts/kiem-tra-bang-phu.py <bao-cao.md>` (in vài dòng). "Đủ" = **mục 0 "Bảng phủ"** của nhật ký không có ô trống, mọi dòng là Đã làm / Không áp dụng / Chưa làm kèm lý do thật. Báo **ĐỦ** → dùng nhật ký + ảnh sẵn có làm nguồn, **không mở trình duyệt**, viết thẳng SRS (bước 4); ca "Chưa làm" đã có lý do thật thì đưa vào "Chưa khám phá" của SRS. Báo **KHÔNG CÓ** (nhật ký cũ chưa có bảng) → dựng bảng từ các hàng sẵn có, không mở trình duyệt. Báo **CÒN THIẾU** (dòng "Chưa có trong nhật ký", ô trống) → ghi `chưa rõ` kèm lý do, rồi **hỏi người dùng** có muốn khám phá thêm phần đó không; không tự khám phá.
   - **Người dùng nói feature đã đổi / yêu cầu khám phá lại:** chỉ khám phá **phần đổi** (hỏi nếu chưa rõ phần nào), lưu vào nhật ký/ảnh mới, không ghi đè bộ cũ.
   - **Chưa có gì (feature mới):** khám phá theo `references/exploration-checklist.md` — luồng chính, mọi nhánh lỗi, từng vai trò, biên, ngôn ngữ, phiên, Network, tệp giao diện. Ca cần mật khẩu → phối hợp theo `references/safety-and-collaboration.md`.
3. **Ghi nhật ký gốc ngay trong lúc làm**: `evidence/<hệ thống>/features/<feature>/bao-cao.md` theo `assets/exploration-log-template.md`, **điền mục 0 "Bảng phủ" khi xong** (cổng ở bước 2 đọc bảng này); copy ảnh sang `screenshots/` và đặt tên `NN-<tài-khoản>-<mô-tả>.jpg`. Nhật ký là nguồn sự thật; SRS dẫn tới nó.
4. **Viết SRS** `srs/<hệ thống>/<feature>.md`: đọc `srs/_template.md` + `srs/id-and-source-rules.md` (nguồn chuẩn), rồi `references/srs-writing-guide.md`. Thứ tự gợi ý: bảng bằng chứng → story + AC → quy tắc dữ liệu/thông báo → câu hỏi cho team → chưa khám phá → lịch sử thay đổi.
5. **Soát**:
   ```bash
   python -X utf8 .claude/skills/srs-from-website/scripts/check-srs.py srs/<hệ thống>/<feature>.md
   ```
   Script báo ID trùng/gãy, AC thiếu bằng chứng hoặc nhãn, liên kết tệp gãy, từ bị cấm, và in số liệu. Script hiểu dải ID `MÃ-R01–R04` nhưng không kiểm ID rút gọn thiếu mã (`R01`) — xem `references/srs-writing-guide.md` mục 2. Sửa hết lỗi, rồi soát tay: nguyên văn thông báo khớp nhật ký; số liệu ở "Lịch sử thay đổi" khớp file; mở thử vài liên kết ảnh.
6. **Cập nhật bộ nhớ** (`memories/modules/<hệ thống>/feature-<ten>.md` + dòng trong `MEMORY.md`): điều học được, bẫy mới, trạng thái SRS.
7. **Trả lời người dùng**: file đã tạo (link), điều đã/chưa kiểm tra và lý do, các câu cần họ trả lời, việc họ cần làm tiếp. Nếu lỡ kích hoạt khóa/giới hạn → nói thẳng ở đầu.

## Cập nhật SRS khi feature đổi
Chỉ khi người dùng nói feature đã đổi. Sửa **tại chỗ**, giữ ID, thêm dòng ở "Lịch sử thay đổi"; khám phá lại **chỉ phần đổi** vào **bộ ảnh/nhật ký mới** (không ghi đè). Đổi ý nghĩa → ID mới, mục cũ `đã bỏ`. Chi tiết: `references/srs-writing-guide.md` mục 6.

## Giữ ngữ cảnh gọn khi soát
Mỗi lượt gọi mô hình đọc lại toàn bộ ngữ cảnh, nên một lần `cat` dài bị trả tiền lại ở mọi lượt sau (nhật ký: các phiên nặng có 190–240 KB kết quả lệnh, phần lớn là `cat` bộ nhớ và `grep` dòng bảng soát dài 700 ký tự).
- Script soát của skill chỉ in vài trăm byte kết luận. **Đạt (0 lỗi) thì không đọc lại file vừa sinh** để "soát cho chắc"; chỉ đọc đúng dòng script báo (`Read` với `offset`/`limit`).
- Không `cat` file bằng Bash. Dùng `Read` đoạn cần, hoặc `Grep` kèm `| cut -c1-200`. Cần xem vài mã (SRS, bảng soát, test case): `python -X utf8 scripts/truy-vet.py tra <dự-án> <tính-năng> --ma ...`.
- Lệnh có thể in nhiều: thêm `| head -40`.
- Soát tay chỉ phần script không kiểm được (câu chữ đọc có hiểu không, ý nghĩa): lấy mẫu vài dòng, không đọc cả file.

## Tệp trong skill
- `references/exploration-checklist.md` — ba loại bằng chứng, kỹ thuật dùng được (Network, tệp giao diện, DOM), ca cần phủ, khi nào được ghi "chưa khám phá".
- `references/safety-and-collaboration.md` — mật khẩu, giới hạn 3 lần, hỏi trước, trung thực khi báo cáo.
- `references/srs-writing-guide.md` — cách viết AC, văn phong, bằng chứng, cập nhật, số liệu khớp.
- `assets/exploration-log-template.md` — khuôn nhật ký khám phá.
- `scripts/check-srs.py` — soát SRS.
- Nguồn chuẩn nằm ngoài skill: `srs/_template.md`, `srs/id-and-source-rules.md` (nếu thiếu, hỏi người dùng, đừng tự dựng).
