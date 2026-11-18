---
name: tao-checklist-test-case
description: Tạo checklist test và test case chi tiết từ requirement/SRS (có mã requirement, có bảng soát và câu trả lời BA thì dùng luôn). Nhờ "tạo checklist" thì chỉ ra checklist (bảng Mã, Tình huống, Ưu tiên, Kỹ thuật, Nguồn) rồi dừng. Nhờ "tạo/viết test case" thì ra cả checklist lẫn test case chi tiết trong một lần (test case luôn thiết kế từ checklist bằng EP, BVA, bảng quyết định, chuyển trạng thái, use case, đoán lỗi). Test case có điều kiện trước, các bước đánh số, dữ liệu giả, kết quả mong đợi ghi theo bước, kèm bốn cột để điền khi chạy (kết quả thực tế, trạng thái, người viết, tự động hóa). Cũng dùng để cập nhật checklist/test case khi requirement đổi (script truy vết báo test case nào cần xem lại). Dùng khi người dùng (thường là tester) nói "tạo checklist", "viết checklist test", "viết test case", "tạo test case", "thiết kế test case", "viết test case từ checklist", "cập nhật test case vì requirement đổi". Không dùng để phân tích requirement/lập câu hỏi cho BA (dùng phan-tich-requirement), khám phá website hay viết SRS (dùng srs-from-website), làm báo cáo HTML (dùng feature-exploration-report), hay báo lỗi.
---

# Tạo checklist và test case

Biến requirement thành **checklist** (danh sách tình huống cần test, kèm kỹ thuật, ưu tiên, nguồn) và **test case chi tiết** (làm theo là chạy được). Luôn đi theo thứ tự: tình huống trước, chi tiết sau. Ngôn ngữ: **tiếng Việt**. Nền: cách làm đã chạy thật trên feature Đăng nhập (mã `LOGIN`, dự án Banking Lite, 41 test case) cộng sách *Nền Tảng Tester Thời AI*. Mẫu thật (chỉ mở khi đang làm Banking Lite): `testing/banking-lite/dang-nhap/checklist.md`, `test-case.md`.

## Ba chế độ, chọn theo lời người dùng

| Người dùng nhờ | Làm | Ra file | Dừng ở đâu |
|---|---|---|---|
| "Tạo checklist" | Chỉ checklist, **chưa viết bước chi tiết** | `checklist.md` | Sau checklist. Đừng viết test case khi chưa được nhờ |
| "Tạo test case" (chưa có checklist) | Lập checklist trước, rồi viết test case từ **chính checklist đó**, một mạch, không dừng chờ duyệt checklist | `checklist.md` + `test-case.md` (lưu **cả hai**, người dùng chốt 2026-11-18) | Sau test case. Nói rõ trong tóm tắt là đã có checklist đi kèm |
| "Viết test case từ checklist" (đã có checklist đã xác nhận) | Giữ **nguyên mã và số lượng** TC của checklist; thấy trùng hoặc thiếu thông tin thì ghi riêng, không tự gộp, xóa, thêm | `test-case.md` | Sau test case |
| "Requirement đổi, cập nhật" | Chạy `scripts/truy-vet.py kiem`, sửa test case ở trạng thái Cần xem lại; mã TC mới lấy số kế tiếp; bỏ test case thì hỏi trước. **Xem ngữ cảnh một vài mã/TC bằng `truy-vet.py tra <dự-án> <tính-năng> --ma S02-AC07,TC-014`** (SRS, theo BA, test case, trạng thái), **không đọc cả** `truy-vet.md`, bảng soát, SRS hay `test-case.md` | sửa file có sẵn | Sau khi chốt mốc truy vết |

## Quy tắc không được phá (và vì sao)

1. **Chỉ dựa vào nguồn người dùng đưa** (requirement, bảng soát, câu trả lời BA). Không dùng kiến thức chung để thêm quy tắc nghiệp vụ, quy định ngành, luật. Chưa có trong nguồn thì chỉ là **câu hỏi**. *AI hay tự điền chỗ bỏ ngỏ và trông rất chuyên nghiệp.*
2. **Ba nhãn nguồn, dòng nào cũng có:** `Có trong tài liệu` (ghi mã requirement hoặc mã câu trả lời), `Suy luận` (ghi **một câu lý do**, điểm xuất phát phải là điều nguồn đã ghi rõ), `Giả định` (nguồn không nói). **Giả định không vào bảng chính**: chuyển thành "Câu hỏi cho BA". Nếu đã có bảng soát: chỉ viết các dòng đã rõ hoặc đã chốt, phần ❓ ghi ở mục "Chưa đưa vào" (người dùng chốt 2026-11-18). Xem `references/quy-tac-checklist.md`.
3. **Chọn kỹ thuật theo dấu hiệu trong requirement**, không theo thói quen: khoảng giá trị/độ dài/ngưỡng → EP và BVA ba giá trị; nhiều điều kiện cùng quyết định một kết quả → bảng quyết định; một thứ đi qua nhiều trạng thái → chuyển trạng thái; hành trình nhiều bước → use case; còn lại hợp lý mới đoán lỗi. Chỉ dùng góc (người dùng mới/đã có dữ liệu, gián đoạn giữa chừng, thao tác lặp lại, phân quyền) khi liên quan requirement. Xem `references/ky-thuat-thiet-ke.md`.
4. **Mỗi dòng checklist một mục tiêu, một giá trị không hợp lệ hoặc một đường không được phép.** Đừng gộp "mã đúng hoặc sai", "ba kiểu sai dạng" vào một dòng: sang bước test case phải chọn một giá trị rồi ghi "riêng" phần còn lại. *Lần `LOGIN` gộp 5 dòng như vậy và phải ghi nhận riêng.*
5. **Test case tự đứng được**: người khác cầm lên là chạy, không mở requirement, không lật sang case khác, không "như TC-xxx", viết đủ từ bước đầu. **Điều kiện trước** ghi rõ trạng thái hệ thống, tài khoản, dữ liệu. **Kết quả mong đợi** chép thẳng câu chữ, con số từ nguồn và ghi **ở bước nào**; mã requirement chỉ ghi ở cột Nguồn.
6. **Nguồn không đủ để viết cụ thể thì ghi `CẦN XÁC NHẬN`, không tự điền**, và đưa vào mục "Câu hỏi cho BA" kèm mã TC. Giá trị do mình chọn để kiểm (ví dụ mốc thời gian "trước 5 phút") thì ghi rõ là giá trị chọn để kiểm.
7. **Sau khi checklist đã xác nhận: giữ nguyên mã và số lượng TC.** Trùng lặp, thiếu thông tin thì ghi vào mục "Ghi nhận riêng", không tự gộp, xóa, thêm.
8. **Chỉ test chức năng.** Không tự đặt ca bảo mật hay hiệu năng; lý do bảo mật của requirement chỉ để suy ra hành vi chức năng. Điều requirement nói thuộc phần khác (ví dụ độ dài mật khẩu thuộc phần đăng ký) thì không test ở đây.
9. **An toàn với hệ thống đang test.** Ca nào cố ý làm sai nhiều lần hoặc có thể kích hoạt khóa/giới hạn: ghi rõ ở điều kiện trước ("cố ý nhập sai N lần, chỉ chạy khi người dùng đồng ý"). Skill này **chỉ viết**, không chạy test, không gõ mật khẩu, không ghi mật khẩu thật vào tài liệu.
10. **Dữ liệu test là dữ liệu giả** (email `@example.com`, chuỗi giả). Tài khoản có thật của hệ thống đang test thì chỉ ghi mã tài khoản, mật khẩu do người dùng cung cấp.
11. **Bảng test case 12 cột cố định, bốn cột cuối để ghi khi chạy** (`Kết quả thực tế`, `Trạng thái`, `Người viết`, `Tự động hóa`). Không bao giờ ghi đè nội dung người dùng đã điền; `sinh-bang.py` tự giữ lại theo mã TC.
12. **Kết quả dài thì lưu file**, chat chỉ tóm tắt và link. Đừng làm quá việc được giao. Làm từng bước nhỏ, hỏi khi chưa rõ (tối đa 3 câu khi không làm tiếp được).

## Đọc gì cho từng việc
Luôn đọc (sau `CLAUDE.md` và `memories/MEMORY.md`): `memories/user/working-preferences.md`, `memories/user/document-preferences.md`, `memories/project/overview.md`, `memories/modules/<slug>/overview.md` của **dự án hiện tại** (slug trong `.du-an-hien-tai`; chưa có thì hỏi người dùng trước, xem `CLAUDE.md` bước 0). Không mở file của dự án khác, kể cả làm mẫu: dùng `assets/` của skill. Thêm theo việc:

| Việc | Đọc | Không cần đọc |
|---|---|---|
| Tạo checklist | Requirement (cả file), bảng soát nếu có (mục câu trả lời và các dòng ✅/❓), `memories/modules/<slug>/feature-<tên>.md`. Skill: `references/ky-thuat-thiet-ke.md`, `quy-tac-checklist.md`, `bai-hoc.md`, `assets/mau-checklist.md`, `assets/mau-du-lieu-checklist.json` | `quy-tac-test-case.md`, `scripts/*.py` (chỉ chạy, không đọc) |
| Tạo test case (có hoặc chưa có checklist) | Như trên cộng `references/quy-tac-test-case.md`, `assets/mau-test-case.md`, `assets/mau-du-lieu-test-case.json`; checklist đã có (cả file) | Bảng soát, câu hỏi của feature khác |
| Cập nhật vì requirement đổi | `truy-vet.md` của feature (mục 1, 5, 6), các dòng test case được báo Cần xem lại, phần requirement đã đổi (chỉ mã được báo). `references/quy-tac-test-case.md` mục "Cập nhật" | Cả requirement, các test case còn đúng |
| Sửa chính skill này | `memories/project/skills.md`, file cần sửa | Sản phẩm trong `testing/` |

File trên ~30 KB mà chỉ cần một phần: Grep rồi đọc đoạn đó (`offset`/`limit`).

## Quy trình

0. **Đọc đúng những file cần cho việc này** (bảng trên).
1. **Chốt đầu vào** (hỏi nếu thiếu): đường dẫn requirement; hệ thống và feature (slug); requirement có mã chưa (chưa có thì gán R1, R2… theo thứ tự, hoặc đề nghị chạy `srs-from-website`); có bảng soát/câu trả lời BA chưa (chưa có mà requirement còn mơ hồ nhiều thì **đề nghị chạy `phan-tich-requirement` trước**, nhưng vẫn làm được phần có căn cứ nếu người dùng muốn); đã có checklist chưa; chế độ nào (bảng trên).
2. **Đọc để hiểu**, liệt kê các đơn vị cần test (mỗi tiêu chí, quy tắc, thông báo). Tính lại số liệu/công thức bằng script nhỏ trong thư mục tạm nếu requirement có con số.
3. **Chọn kỹ thuật** cho từng đơn vị theo `references/ky-thuat-thiet-ke.md`; gán ưu tiên (Cao cho luồng chính, tiền, bảo mật, tài khoản).
4. **Viết dữ liệu checklist** thành JSON trong thư mục tạm (mẫu `assets/mau-du-lieu-checklist.json`), rồi sinh file:
   ```bash
   python -X utf8 .claude/skills/tao-checklist-test-case/scripts/sinh-bang.py checklist \
     --du-lieu <dl-checklist.json> --ra testing/<hệ thống>/<feature>/checklist.md
   ```
   Mã TC-001… tự đánh sau khi xếp Cao, Trung bình, Thấp. **Chế độ "Tạo checklist": kiểm (bước 6) rồi sang bước 8, dừng.**
5. **Viết dữ liệu test case** (mẫu `assets/mau-du-lieu-test-case.json`): mỗi mã TC của checklist một `ca` với điều kiện trước, các bước, dữ liệu, kết quả theo bước. Mục "Câu hỏi cho BA" cho mọi chỗ `CẦN XÁC NHẬN`; mục "Ghi nhận riêng" cho trùng lặp, gộp giá trị.
   ```bash
   python -X utf8 .claude/skills/tao-checklist-test-case/scripts/sinh-bang.py test-case \
     --du-lieu <dl-test-case.json> --checklist testing/<hệ thống>/<feature>/checklist.md \
     --ra testing/<hệ thống>/<feature>/test-case.md
   ```
   Tình huống, Ưu tiên, Nguồn lấy nguyên văn từ checklist; bốn cột ghi khi chạy mặc định trống / `Chưa chạy` / `Sunny Tran` / `Chưa có`.
6. **Kiểm bằng script**, sửa hết lỗi rồi mới trả lời:
   ```bash
   python -X utf8 .claude/skills/tao-checklist-test-case/scripts/kiem-tra-tc.py \
     --checklist testing/<hệ thống>/<feature>/checklist.md --test-case testing/<hệ thống>/<feature>/test-case.md \
     --nguon <file requirement> --ma "<biểu thức chính quy của mã, ví dụ LOGIN-(?:S\d\d-AC\d\d|R\d\d|M\d\d)>" --tien-to LOGIN
   ```
   Rồi soát tay: đọc vài test case như người chưa biết gì về feature, xem có chạy được không.
7. **Truy vết** (người dùng chốt 2026-11-18: tự làm khi requirement có mã): theo `memories/project/truy-vet-requirement.md` — tạo `truy-vet-cau-hinh.json` (đường dẫn, tiền tố, tên ngắn từng mã), đổi cột Nguồn thành `mã (tên ngắn)`, chạy `python -X utf8 scripts/truy-vet.py kiem <dự-án> <feature>` rồi `chot -m "…"`. Requirement chưa có mã thì bỏ qua và nói rõ.
8. **Cập nhật bộ nhớ**: `memories/modules/<slug>/feature-<tên>.md` (điều học được, bẫy, trạng thái), một dòng trong `MEMORY.md`.
9. **Trả lời** bằng tóm tắt ngắn và link file (không dán bảng): số dòng/số case, chỗ `CẦN XÁC NHẬN`, câu hỏi cho BA, giá trị do mình chọn, việc ghi nhận riêng; nói rõ **chưa chạy test** và chế độ vừa làm. Commit chỉ khi người dùng nhờ.

## Tệp trong skill
- `references/ky-thuat-thiet-ke.md` — dấu hiệu chọn kỹ thuật, cách làm từng kỹ thuật, bốn góc gợi ý, cách xếp ưu tiên.
- `references/quy-tac-checklist.md` — khuôn bảng 5 cột, nhãn nguồn, cột Nguồn kèm tên ngắn, câu hỏi cho BA, "Chưa đưa vào", tự kiểm.
- `references/quy-tac-test-case.md` — khuôn bảng 12 cột, cách viết điều kiện/bước/dữ liệu/kết quả, `CẦN XÁC NHẬN`, trạng thái, cập nhật khi requirement đổi, tự kiểm.
- `references/bai-hoc.md` — bẫy đã gặp khi làm `LOGIN`.
- `assets/mau-checklist.md`, `assets/mau-test-case.md` — hình dạng file đầu ra (ví dụ trung lập).
- `assets/mau-du-lieu-checklist.json`, `assets/mau-du-lieu-test-case.json` — dữ liệu đầu vào cho `sinh-bang.py`.
- `scripts/sinh-bang.py` — sinh `checklist.md`, `test-case.md` từ JSON, giữ bốn cột ghi khi chạy.
- `scripts/kiem-tra-tc.py` — kiểm đầu ra.
- Ngoài skill: `scripts/truy-vet.py` (truy vết, dùng chung cho mọi feature), `memories/project/truy-vet-requirement.md`.
