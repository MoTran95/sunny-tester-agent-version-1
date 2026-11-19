---
name: tao-checklist-test-case
description: Tạo checklist test và test case chi tiết từ requirement/SRS (có mã requirement, có bảng soát và câu trả lời BA thì dùng luôn). Feature mới: nhờ "tạo checklist" hay "tạo/viết test case" đều đi cùng một đường: chọn tình huống (EP, BVA, bảng quyết định, chuyển trạng thái, use case, đoán lỗi), in danh sách tình huống ngắn trong chat cho người dùng duyệt, rồi viết chi tiết và ra MỘT file `test-case.md` gộp (có cả phần checklist lẫn phần chi tiết, không có `checklist.md` riêng). Test case có điều kiện trước, các bước đánh số, dữ liệu giả, kết quả mong đợi ghi theo bước, kèm bốn cột để điền khi chạy (kết quả thực tế, trạng thái, người viết, tự động hóa). Cũng dùng để cập nhật checklist/test case khi requirement đổi (script truy vết báo test case nào cần xem lại). Dùng khi người dùng (thường là tester) nói "tạo checklist", "viết checklist test", "viết test case", "tạo test case", "thiết kế test case", "viết test case từ checklist", "cập nhật test case vì requirement đổi". Không dùng để phân tích requirement/lập câu hỏi cho BA (dùng phan-tich-requirement), khám phá website hay viết SRS (dùng srs-from-website), làm báo cáo HTML (dùng feature-exploration-report), hay báo lỗi.
---

# Tạo checklist và test case

Biến requirement thành **checklist** (danh sách tình huống cần test, kèm kỹ thuật, ưu tiên, nguồn) và **test case chi tiết** (làm theo là chạy được). Luôn đi theo thứ tự: tình huống trước (**người dùng duyệt trong chat**), chi tiết sau, nhưng **từ 2026-11-18 ghi vào một bảng gộp** (người dùng chốt: đỡ lòng vòng, về lâu dài chỉ bảo trì một file): mỗi dòng có cả phần checklist (Tình huống, Ưu tiên, Kỹ thuật, Nguồn) và phần chi tiết (Điều kiện trước, Các bước, Dữ liệu test, Kết quả mong đợi), kèm 4 cột ghi khi chạy. **Không còn file `checklist.md` riêng** với feature mới; feature đã có hai file (Đăng nhập `LOGIN`) giữ cách cũ. Ngôn ngữ: **tiếng Việt**. Nền: cách làm đã chạy thật trên những feature đã làm với người dùng cộng sách *Nền Tảng Tester Thời AI*. Khuôn: `assets/`.

## Ba chế độ, chọn theo lời người dùng

| Người dùng nhờ | Làm | Ra file | Dừng ở đâu |
|---|---|---|---|
| "Tạo checklist", "tạo test case", "viết test case" (feature mới, chưa có file) | Chọn tình huống + kỹ thuật + ưu tiên → **dừng, in danh sách trong chat cho người dùng duyệt** (bước 4 quy trình) → viết điều kiện, bước, dữ liệu, kết quả cho đúng các dòng đã duyệt, trong cùng một dòng của bảng | **một file** `test-case.md` (bảng gộp 13 cột; không tạo `checklist.md`) | Dừng **một lần** chờ duyệt danh sách tình huống; sau đó đến file gộp. Nói rõ trong tóm tắt là đã có cả phần checklist và phần chi tiết |
| Feature **đã có hai file** `checklist.md` + `test-case.md` (hiện chỉ `LOGIN`) nhờ thêm/sửa | Giữ cách cũ: sửa cả hai file, mã TC mới lấy số kế tiếp ở cả hai. Không tự chuyển sang file gộp (hỏi người dùng nếu muốn chuyển) | hai file như cũ | Sau test case |
| "Viết test case từ checklist" (có sẵn `checklist.md` đã xác nhận, cách cũ) | Giữ **nguyên mã và số lượng** TC của checklist; thấy trùng hoặc thiếu thông tin thì ghi riêng, không tự gộp, xóa, thêm | `test-case.md` | Sau test case |
| "Requirement đổi, cập nhật" | Chạy `scripts/truy-vet.py kiem`, sửa test case ở trạng thái Cần xem lại; mã TC mới lấy số kế tiếp; bỏ test case thì hỏi trước. **Xem ngữ cảnh một vài mã/TC bằng `truy-vet.py tra <dự-án> <tính-năng> --ma S02-AC07,TC-014`** (SRS, theo BA, test case, trạng thái), **không đọc cả** `truy-vet.md`, bảng soát, SRS hay `test-case.md` | sửa file có sẵn (file gộp: sửa ngay trong `test-case.md`, dòng TC mới xếp cuối bảng và khai báo `Dòng thêm sau khi requirement đổi`) | Sau khi chốt mốc truy vết |

## Quy tắc không được phá (và vì sao)

1. **Chỉ dựa vào nguồn người dùng đưa** (requirement, bảng soát, câu trả lời BA). Không dùng kiến thức chung để thêm quy tắc nghiệp vụ, quy định ngành, luật. Chưa có trong nguồn thì chỉ là **câu hỏi**. *AI hay tự điền chỗ bỏ ngỏ và trông rất chuyên nghiệp.*
2. **Ba nhãn nguồn, dòng nào cũng có:** `Có trong tài liệu` (ghi mã requirement hoặc mã câu trả lời), `Suy luận` (ghi **một câu lý do**, điểm xuất phát phải là điều nguồn đã ghi rõ), `Giả định` (nguồn không nói). **Giả định không vào bảng chính**: chuyển thành "Câu hỏi cho BA". Nếu đã có bảng soát: chỉ viết các dòng đã rõ hoặc đã chốt, phần ❓ ghi ở mục "Chưa đưa vào" (người dùng chốt 2026-11-18). Xem `references/quy-tac-checklist.md`.
3. **Chọn kỹ thuật theo dấu hiệu trong requirement**, không theo thói quen: khoảng giá trị/độ dài/ngưỡng → EP và BVA ba giá trị; nhiều điều kiện cùng quyết định một kết quả → bảng quyết định; một thứ đi qua nhiều trạng thái → chuyển trạng thái; hành trình nhiều bước → use case; còn lại hợp lý mới đoán lỗi. Chỉ dùng góc (người dùng mới/đã có dữ liệu, gián đoạn giữa chừng, thao tác lặp lại, phân quyền) khi liên quan requirement. Xem `references/ky-thuat-thiet-ke.md`.
4. **Mỗi dòng checklist một mục tiêu, một giá trị không hợp lệ hoặc một đường không được phép.** Đừng gộp "mã đúng hoặc sai", "ba kiểu sai dạng" vào một dòng: sang bước test case phải chọn một giá trị rồi ghi "riêng" phần còn lại. *Lần `LOGIN` gộp 5 dòng như vậy và phải ghi nhận riêng.*
5. **Test case tự đứng được**: người khác cầm lên là chạy, không mở requirement, không lật sang case khác, không "như TC-xxx", viết đủ từ bước đầu (bước 1 là mở địa chỉ và đăng nhập tài khoản; không ghi mật khẩu, không cần nhắc "tự nhập mật khẩu"). **Điều kiện trước chỉ ghi dữ kiện quan trọng để vào kiểm tra ca này** (người dùng chốt 2026-11-18, sau ba vòng sửa): gạch đầu dòng `- …`, mỗi ý một dòng ngắn, thường 2–4 gạch: cách có hồ sơ/dữ liệu, trạng thái liên quan tới kết quả của ca (số tiền, thời hạn, đang ở bước nào…; **kể cả dữ kiện ẩn làm kết quả đổi**, ví dụ khách hàng nào vì tuổi tính từ ngày sinh, hàng đã hay chưa có giá), trạng thái đặc biệt nếu có. **Không** ghi điều đã nằm ở bước 1 ("đã đăng nhập", "mở được trang") và **không** định nghĩa dữ liệu dùng chung một lần ở đầu file rồi trỏ về. Trạng thái phải đạt được bằng cách làm. **Kết quả mong đợi** chép thẳng câu chữ, con số từ nguồn và ghi **ở bước nào**; mã requirement chỉ ghi ở cột Nguồn.
6. **Nguồn không đủ để viết cụ thể thì ghi `CẦN XÁC NHẬN`, không tự điền**, và đưa vào mục "Câu hỏi cho BA" kèm mã TC. Giá trị do mình chọn để kiểm (ví dụ mốc thời gian "trước 5 phút") thì ghi rõ là giá trị chọn để kiểm.
7. **Sau khi danh sách tình huống đã được duyệt (trong chat, hoặc `checklist.md` cách cũ): giữ nguyên số lượng và nội dung tình huống đã duyệt.** Trùng lặp, thiếu thông tin thì ghi vào mục "Ghi nhận riêng", không tự gộp, xóa, thêm. Người dùng sửa danh sách thì chỉnh theo lời họ rồi mới viết chi tiết.
8. **Chỉ test chức năng.** Không tự đặt ca bảo mật hay hiệu năng; lý do bảo mật của requirement chỉ để suy ra hành vi chức năng. Điều requirement nói thuộc phần khác (ví dụ độ dài mật khẩu thuộc phần đăng ký) thì không test ở đây.
9. **An toàn với hệ thống đang test.** Ca nào cố ý làm sai nhiều lần hoặc có thể kích hoạt khóa/giới hạn: ghi rõ ở điều kiện trước ("cố ý nhập sai N lần, chỉ chạy khi người dùng đồng ý"). Skill này **chỉ viết**, không chạy test, không gõ mật khẩu, không ghi mật khẩu thật vào tài liệu.
10. **Dữ liệu test là dữ liệu giả** (email `@example.com`, chuỗi giả). Tài khoản có thật của hệ thống đang test thì chỉ ghi mã tài khoản, mật khẩu do người dùng cung cấp.
11. **Bảng gộp 13 cột cố định (`Mã, Tình huống, Ưu tiên, Kỹ thuật, Điều kiện trước, Các bước, Dữ liệu test, Kết quả mong đợi, Nguồn` + bốn cột ghi khi chạy; cách cũ hai file thì test case 12 cột, không có `Kỹ thuật`), bốn cột cuối để ghi khi chạy** (`Kết quả thực tế`, `Trạng thái`, `Người viết`, `Tự động hóa`). Không bao giờ ghi đè nội dung người dùng đã điền; `sinh-bang.py` tự giữ lại theo mã TC.
12. **Kết quả dài thì lưu file**, chat chỉ tóm tắt và link. Đừng làm quá việc được giao. Làm từng bước nhỏ, hỏi khi chưa rõ (tối đa 3 câu khi không làm tiếp được).
13. **Cột `Tình huống` là tên test case, viết thành câu đầy đủ rõ nghĩa** (người dùng chốt 2026-11-18, sau khi chê câu dài lộn xộn và cả bản rút gọn `điều kiện: kết quả`): dạng `<Hệ thống làm gì/hiển thị gì> khi <người dùng làm gì/điều kiện>`. Ví dụ: `Đăng nhập thành công khi nhập đúng tên và mật khẩu`; `Hiển thị Từ chối kèm lý do khi thặng dư thiếu 1 đồng so với mức tối thiểu (2.999.999)`. Con số chi tiết để cột Dữ liệu test (trong tên chỉ giữ số làm nên ca, đặt trong ngoặc); không dùng mã nội bộ; một tên một mục tiêu. Quy tắc 5 và 13 áp dụng cho file gộp (feature mới); `LOGIN` giữ cách viết cũ cho tới khi chuyển.

## Đọc gì cho từng việc
Luôn đọc (sau `CLAUDE.md` và `memories/MEMORY.md`): `memories/user/working-preferences.md`, `memories/user/document-preferences.md`, `memories/project/overview.md`, `memories/modules/<slug>/overview.md` của **dự án hiện tại** (slug trong `.du-an-hien-tai`; chưa có thì hỏi người dùng trước, xem `CLAUDE.md` bước 0). Không mở file của dự án khác, kể cả làm mẫu: dùng `assets/` của skill. Thêm theo việc:

| Việc | Đọc | Không cần đọc |
|---|---|---|
| Tạo checklist / test case (một file gộp) | Requirement (cả file), bảng soát nếu có (mục câu trả lời và các dòng ✅/❓), `memories/modules/<slug>/feature-<tên>.md`. Skill: `references/ky-thuat-thiet-ke.md`, `quy-tac-checklist.md` (cho các cột Tình huống, Ưu tiên, Kỹ thuật, Nguồn), `quy-tac-test-case.md` (cho các cột chi tiết), `bai-hoc.md`, `assets/mau-du-lieu-gop.json` (dữ liệu đầu vào), `assets/mau-test-case.md` (hình dạng chi tiết) | `scripts/*.py` (chỉ chạy), `mau-du-lieu-checklist.json`, `mau-du-lieu-test-case.json` (cách cũ hai file) |
| Cập nhật vì requirement đổi | `truy-vet.md` của feature (mục 1, 5, 6), các dòng test case được báo Cần xem lại, phần requirement đã đổi (chỉ mã được báo). `references/quy-tac-test-case.md` mục "Cập nhật" | Cả requirement, các test case còn đúng |
| Sửa chính skill này | `memories/project/skills.md`, file cần sửa | Sản phẩm trong `testing/` |

File trên ~30 KB mà chỉ cần một phần: Grep rồi đọc đoạn đó (`offset`/`limit`).

## Quy trình

0. **Đọc đúng những file cần cho việc này** (bảng trên).
1. **Chốt đầu vào** (hỏi nếu thiếu): đường dẫn requirement; hệ thống và feature (slug); requirement có mã chưa (chưa có thì gán R1, R2… theo thứ tự, hoặc đề nghị chạy `srs-from-website`); có bảng soát/câu trả lời BA chưa (chưa có mà requirement còn mơ hồ nhiều thì **đề nghị chạy `phan-tich-requirement` trước**, nhưng vẫn làm được phần có căn cứ nếu người dùng muốn); đã có checklist chưa; chế độ nào (bảng trên).
2. **Đọc để hiểu**, liệt kê các đơn vị cần test (mỗi tiêu chí, quy tắc, thông báo). Tính lại số liệu/công thức bằng script nhỏ trong thư mục tạm nếu requirement có con số.
3. **Chọn kỹ thuật** cho từng đơn vị theo `references/ky-thuat-thiet-ke.md`; gán ưu tiên (Cao cho luồng chính, tiền, bảo mật, tài khoản).
4. **Duyệt tình huống trong chat (feature mới, một lần).** Lưu danh sách vào JSON ở thư mục tạm (chat không lưu bền; bước 5 dùng lại chính file này), rồi in trong chat, **mỗi dòng ngắn**: số thứ tự · tên test case (câu đầy đủ theo quy tắc 13) · ưu tiên · kỹ thuật · mã requirement nguồn. Gom theo requirement. Không dán điều kiện/bước/kết quả (quy tắc 12). Feature trên ~40 dòng: duyệt từng nhóm requirement, nhóm nào duyệt xong mới viết chi tiết nhóm đó. In kèm: số dòng, mã requirement chưa có dòng nào (nếu có), phần ❓ "Chưa đưa vào". Rồi **dừng chờ người dùng** gật hoặc sửa; sửa thì chỉnh thẳng JSON. Người dùng đã nói "không cần duyệt" hoặc "viết luôn" thì bỏ qua bước này.
5. **Viết dữ liệu gộp** thành JSON trong thư mục tạm (mẫu `assets/mau-du-lieu-gop.json`; thêm phần chi tiết vào file danh sách đã duyệt): mỗi `ca` có `tinh_huong` (tên test case, quy tắc 13), `uu_tien`, `ky_thuat`, `nguon` (phần checklist) và `dieu_kien` (mỗi phần tử một gạch đã có `- ` ở đầu, quy tắc 5), `buoc`, `du_lieu`, `ket_qua` (phần chi tiết). Mục "Câu hỏi cho BA" cho mọi chỗ `CẦN XÁC NHẬN`; "Chưa đưa vào" cho phần ❓; "Ghi nhận riêng" cho trùng lặp, gộp giá trị. Rồi sinh file:
   ```bash
   python -X utf8 .claude/skills/tao-checklist-test-case/scripts/sinh-bang.py gop \
     --du-lieu <dl-gop.json> --ra testing/<hệ thống>/<feature>/test-case.md
   ```
   Mã TC-001… tự đánh sau khi xếp Cao, Trung bình, Thấp. Bốn cột ghi khi chạy mặc định trống / `Chưa chạy` / `Sunny Tran` / `Chưa có`; chạy lại lệnh thì giữ lại theo mã.
6. (Cách cũ hai file, chỉ khi feature đã có `checklist.md`: `sinh-bang.py checklist` rồi `sinh-bang.py test-case --checklist …`; xem docstring của script.)
7. **Kiểm bằng script**, sửa hết lỗi rồi mới trả lời:
   ```bash
   python -X utf8 .claude/skills/tao-checklist-test-case/scripts/kiem-tra-tc.py \
     --test-case testing/<hệ thống>/<feature>/test-case.md \
     --nguon <file requirement> --ma "<biểu thức chính quy của mã, ví dụ LOGIN-(?:S\d\d-AC\d\d|R\d\d|M\d\d)>" --tien-to LOGIN
   ```
   Rồi soát tay: đọc vài test case như người chưa biết gì về feature, xem có chạy được không.
8. **Truy vết** (người dùng chốt 2026-11-18: tự làm khi requirement có mã): theo `memories/project/truy-vet-requirement.md` — tạo `truy-vet-cau-hinh.json` (đường dẫn, tiền tố, tên ngắn từng mã; **file gộp thì bỏ khóa `checklist`**, script tự hiểu), cột Nguồn viết theo `references/quy-tac-checklist.md` (câu thường + link tới dòng SRS, cần thẻ neo trong SRS), chạy `python -X utf8 scripts/truy-vet.py kiem <dự-án> <feature>` rồi `chot -m "…"`. Requirement chưa có mã thì bỏ qua và nói rõ.
9. **Cập nhật bộ nhớ**: `memories/modules/<slug>/feature-<tên>.md` (điều học được, bẫy, trạng thái), một dòng trong `MEMORY.md`.
10. **Trả lời** bằng tóm tắt ngắn và link file (không dán bảng): số dòng/số case, chỗ `CẦN XÁC NHẬN`, câu hỏi cho BA, giá trị do mình chọn, việc ghi nhận riêng; nói rõ **chưa chạy test** và chế độ vừa làm. Commit chỉ khi người dùng nhờ.

## Giữ ngữ cảnh gọn khi soát
Mỗi lượt gọi mô hình đọc lại toàn bộ ngữ cảnh, nên một lần `cat` dài bị trả tiền lại ở mọi lượt sau (nhật ký: các phiên nặng có 190–240 KB kết quả lệnh, phần lớn là `cat` bộ nhớ và `grep` dòng bảng soát dài 700 ký tự).
- Script soát của skill chỉ in vài trăm byte kết luận. **Đạt (0 lỗi) thì không đọc lại file vừa sinh** để "soát cho chắc"; chỉ đọc đúng dòng script báo (`Read` với `offset`/`limit`).
- Không `cat` file bằng Bash. Dùng `Read` đoạn cần, hoặc `Grep` kèm `| cut -c1-200`. Cần xem vài mã (SRS, bảng soát, test case): `python -X utf8 scripts/truy-vet.py tra <dự-án> <tính-năng> --ma ...`.
- Lệnh có thể in nhiều: thêm `| head -40`.
- Soát tay chỉ phần script không kiểm được (câu chữ đọc có hiểu không, ý nghĩa): lấy mẫu vài dòng, không đọc cả file.

## Tệp trong skill
- `references/ky-thuat-thiet-ke.md` — dấu hiệu chọn kỹ thuật, cách làm từng kỹ thuật, bốn góc gợi ý, cách xếp ưu tiên.
- `references/quy-tac-checklist.md` — khuôn bảng 5 cột, nhãn nguồn, cột Nguồn (câu thường, link tới SRS; feature cũ: mã kèm tên ngắn), câu hỏi cho BA, "Chưa đưa vào", tự kiểm.
- `references/quy-tac-test-case.md` — khuôn bảng 12 cột, cách viết điều kiện/bước/dữ liệu/kết quả, `CẦN XÁC NHẬN`, trạng thái, cập nhật khi requirement đổi, tự kiểm.
- `references/bai-hoc.md` — bẫy đã gặp khi làm `LOGIN`.
- `assets/mau-checklist.md`, `assets/mau-test-case.md` — hình dạng file đầu ra (ví dụ trung lập).
- `assets/mau-du-lieu-gop.json` — dữ liệu đầu vào cho `sinh-bang.py gop` (một file, mặc định).
- `assets/mau-du-lieu-checklist.json`, `assets/mau-du-lieu-test-case.json` — dữ liệu đầu vào cách cũ (hai file).
- `scripts/sinh-bang.py` — lệnh `gop` (mặc định) sinh `test-case.md` gộp từ JSON; `checklist` + `test-case` là cách cũ. Giữ bốn cột ghi khi chạy.
- `scripts/kiem-tra-tc.py` — kiểm đầu ra (chỉ `--test-case` = file gộp; có `--checklist` = cách cũ).
- Ngoài skill: `scripts/truy-vet.py` (truy vết, dùng chung cho mọi feature), `scripts/truy-vet-smoke.py` (smoke test), `memories/project/truy-vet-requirement.md`.
- Ô Mã của test case có thẻ neo `<a id="tc-005"></a>TC-005` để smoke và tài liệu khác link tới đúng dòng; `sinh-bang.py` tự ghi (không bỏ khi sửa tay). Sửa test case xong có smoke dùng nó thì chạy `truy-vet-smoke.py kiem <dự-án>`.
