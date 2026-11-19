---
name: tao-bug-report
description: Viết bug report đầy đủ từ ghi chú lỗi thô của người dùng, hoặc từ một test case bị Không đạt khi người dùng nhờ "tạo bug". Ra một file bug (md) kèm trang HTML dễ xem có nút sao chép từng mục, tiêu đề dạng [Module] mô tả lỗi (chỉ nói cái gì sai, không kèm lý do hay ngữ cảnh), test case liên quan, môi trường (trình duyệt chỉ ghi tên + số bản), điều kiện trước, các bước tái hiện đánh số, kết quả mong đợi (lấy từ requirement/test case, không có thì ghi câu hỏi cho BA), kết quả thực tế cụ thể, phạm vi ảnh hưởng, ảnh hưởng nghiệp vụ, mức độ nghiêm trọng (tiếng Việt) kèm lý do, mức độ ưu tiên đề xuất, tần suất, đính kèm cần có (ảnh lỗi tô đỏ chỗ lỗi, ghi lỗi ở bước nào), câu hỏi cho Dev viết đủ ngữ nghĩa, và danh sách thông tin gắn nhãn Giả định để người dùng kiểm lại; bug sinh từ lượt chạy smoke thì điền mã bug và ảnh tô đỏ vào bảng kết quả smoke. Không thêm thông tin ngoài ghi chú, không tự gộp nhiều lỗi, thiếu bước tái hiện/môi trường thì hỏi trước (tối đa 3 câu). Dùng khi người dùng (thường là tester) nói "tạo bug", "viết bug", "viết bug report", "ghi bug", "báo lỗi", "test case X fail, tạo bug", "viết lại ghi chú này thành bug", hoặc sau khi nhờ bạn chạy test thật mà test case Không đạt và họ bảo tạo bug. Không dùng để viết test case (dùng tao-checklist-test-case), phân tích requirement/hỏi BA (dùng phan-tich-requirement), hay khám phá website (dùng srs-from-website).
---

# Tạo bug report

Biến ghi chú lỗi thô (hoặc một test case Không đạt) thành bug report mà Dev đọc xong **tái hiện được ngay, không phải hỏi lại**. Ngôn ngữ: **tiếng Việt**. Sản phẩm: file `BUG-nnn.md` + trang `BUG-nnn.html` (dễ xem, có nút Sao chép) + ảnh bằng chứng đã tô đỏ chỗ lỗi; bug đến từ lượt smoke thì còn điền vào bảng kết quả smoke. Skill này chỉ **viết**: không tự chạy lại test, không khám phá thêm để "tìm thêm chi tiết" (người dùng không đủ lượt chạy lại, xem `memories/user/working-preferences.md`).

Chỉ tạo bug **khi người dùng nhờ**. Đang chạy test hộ người dùng mà test case Không đạt: báo kết quả Không đạt, **hỏi có tạo bug không**, không tự viết.

## Ba nguồn đầu vào

| Người dùng đưa | Lấy gì ở đâu |
|---|---|
| **Ghi chú lỗi thô** (kèm môi trường, có thể kèm mã test case, đoạn requirement) | Mọi dữ kiện từ ghi chú; kết quả mong đợi từ requirement/test case đi kèm |
| **Mã test case Không đạt** ("TC-014 fail, tạo bug") | Điều kiện trước, các bước, kết quả mong đợi **lấy từ dòng test case đó** (tìm bằng `Grep` mã trong `testing/<slug>/<feature>/test-case.md`, đọc đúng dòng; nguồn có câu trả lời BA thì theo câu trả lời). Kết quả thực tế lấy từ người dùng, hoặc cột `Kết quả thực tế` nếu họ đã điền. Người dùng nói bước làm khác test case thì **theo lời họ** |
| **Chính mình vừa chạy trong phiên này** (người dùng nhờ chạy rồi tạo bug) | Kết quả thực tế = điều **thật sự quan sát được** (nguyên văn thông báo, giá trị hiện ra); đường dẫn ảnh/log vừa lưu làm đính kèm (chạy bằng `scripts/run_tests.py` thì ảnh tô đỏ và câu chú thích lỗi đã có sẵn trong file kết quả `result-*.json`: trường `anh_loi`, `anh_loi_chu_thich`); môi trường chỉ ghi cái đã thấy (ví dụ số bản hiện trên giao diện). Không viết điều không thấy |

## Quy tắc không được phá (và vì sao)

1. **Không thêm thông tin không có trong ghi chú.** Chỗ bắt buộc phải tự thêm (điền cho đủ mục, suy ra từ ngữ cảnh) thì gắn nhãn **`[Giả định: …]`** ngay tại chỗ đó. *AI hay điền cho trọn bộ rồi Dev đi tìm một điều kiện chưa từng có.* Điều lấy từ test case hoặc requirement không phải giả định, nhưng ghi nguồn (`theo TC-014, bước 3`).
2. **Kết quả mong đợi chỉ lấy từ requirement hoặc test case** (chép câu chữ; nguồn ghi ở mục Test case liên quan, **không chèn** câu kiểu "theo TC-014, bước 4; theo BA…" vào trong mục Kết quả mong đợi). Nguồn không nói điều đáng ra phải xảy ra thì **không tự đặt**: ghi `Chưa xác định` và đưa **một câu hỏi cho BA** vào mục "Câu hỏi còn mở" (xưng hô, khuôn câu: `memories/conventions/ba-question-wording.md`). Khi đó đây là **nghi lỗi, chờ BA chốt**; nói rõ ở đầu file.
3. **Chỉ gộp nhiều chỗ vào một bug khi ghi chú nói rõ chúng chung một nguyên nhân hoặc Dev đã xác nhận.** Chưa chắc thì **tách thành bug riêng** (một file mỗi bug), mỗi bug ghi chú "có thể chung nguyên nhân với BUG-0xx, cần hỏi Dev" và đưa câu hỏi cho Dev vào "Câu hỏi còn mở". Một ghi chú có nhiều lỗi khác nhau → nhiều bug.
4. **Thiếu các bước tái hiện hoặc môi trường thì hỏi người dùng trước, tối đa 3 câu, rồi dừng chờ.** Môi trường đủ = nơi chạy + trình duyệt hoặc thiết bị + số build/phiên bản (**Trình duyệt chỉ ghi tên + số bản + hệ điều hành**, ví dụ `Chrome 157 trên Windows 11`; không ghi công cụ hay chế độ chạy test như Playwright, ẩn cửa sổ, và không gắn Giả định ở dòng này); chỉ lấy cái người dùng đã nói trong lượt này hoặc cái mình vừa quan sát; **không lấy từ memory đoán thay** (địa chỉ hệ thống trong memory chỉ giúp hiểu, số build thì phải do người dùng hoặc giao diện cho biết). Câu hỏi nêu rõ thiếu gì và cho ví dụ cách trả lời. Chưa đủ hai thứ này thì không viết bản "tạm".
5. **Kết quả thực tế phải cụ thể**: màn hình nào, thao tác nào, thấy chính xác gì (nguyên văn thông báo, mã lỗi, giá trị/số liệu sai và giá trị đúng, nút bị mờ hay không phản hồi, trang trắng…). **Cấm** các câu chung chung: "không hoạt động", "bị lỗi", "sai", "không đúng", "lỗi hệ thống", "không như mong đợi". Ghi chú chỉ nói chung chung mà thiếu chi tiết thì hỏi (tính vào 3 câu của quy tắc 4); hết lượt hỏi thì ghi `CẦN BỔ SUNG: <thiếu gì>` và đưa vào danh sách cuối, không viết cho đẹp.
6. **Không đoán nguyên nhân gốc, không đề xuất cách sửa.** Đó là việc của Dev; ghi chú nêu nguyên nhân thì chép lại kèm "theo ghi chú của người dùng".
7. **Mức độ nghiêm trọng dựa trên ảnh hưởng, không dựa cảm giác**: nêu ai bị ảnh hưởng, việc gì không làm được hoặc ra kết quả sai, có cách đi vòng không (thang ở dưới). **Mức độ ưu tiên chỉ là đề xuất**, ghi "team hoặc PO sẽ chốt". Thiếu dữ kiện để chấm (ví dụ không biết có cách đi vòng không) thì dữ kiện đó là Giả định, ghi nhãn.
8. **Tần suất chỉ ghi điều đã thử**: `Luôn xảy ra` (nói rõ lần nào cũng bị: N/N lần), `Thỉnh thoảng (x/y lần thử)`, hoặc `Một lần` (xảy ra một lần, chưa tái hiện được). Mới thử một lần và bị: ghi `1/1 lần thử, chưa thử lại`, không viết "luôn xảy ra". Ghi chú không nêu số lần: ghi `Chưa rõ`, đưa vào danh sách cuối.
9. **Chỉ lỗi chức năng.** Không tự thêm nhận xét bảo mật, hiệu năng, giao diện thẩm mỹ khi ghi chú không nói tới.
10. **Không ghi mật khẩu, mã thông báo, dữ liệu cá nhân thật** vào bug. Tài khoản test chỉ ghi mã tài khoản (ví dụ `P100001`). Ảnh/log đính kèm có dữ liệu nhạy cảm thì nhắc người dùng che trước khi gửi.
11. **Đính kèm: chỉ liệt kê cái có thật hoặc cái cần có.** Có đường dẫn người dùng đưa thì ghi đường dẫn; chưa có thì ghi `Cần bổ sung`. Không viết "xem ảnh đính kèm" khi chưa có ảnh. **Ảnh thể hiện lỗi phải kèm bản tô đỏ chỗ lỗi** (giữ ảnh gốc, thêm ảnh `-loi`), và mỗi dòng ảnh ghi **lỗi ở bước nào** của các bước tái hiện (xem mục "Ảnh bằng chứng tô đỏ").
12. **Kết quả dài thì lưu file**, chat chỉ tóm tắt và link; riêng danh sách Giả định và câu hỏi còn mở thì in trong chat (ngắn, người dùng cần duyệt ngay).
13. **Văn phong theo người dùng đã chỉnh (2026-11-18, bug đầu tiên)**: tiêu đề chỉ mô tả lỗi, không lý do/ngữ cảnh/hậu quả (không "dù BA đã chốt…"); gọi thành phần giao diện đúng tên người dùng dùng ("thanh điều hướng", không "thanh điều hướng"); dòng Trình duyệt chỉ ghi tên + số bản (+ hệ điều hành); mục Kết quả mong đợi không chèn ngoặc nguồn; mức độ nghiêm trọng/ưu tiên ghi tiếng Việt; câu hỏi cho Dev viết đủ ngữ nghĩa. Đọc `memories/user/document-preferences.md` mục Bug report khi cần nhắc lại.
14. **Bug đến từ lượt chạy smoke thì nối vào bảng kết quả** (không để bảng ghi "chưa tạo bug"): điền mã bug, ảnh tô đỏ và câu chú thích lỗi (mục "Nối vào bảng kết quả smoke"). Việc này ghi vào file dữ liệu của bảng, không phải việc sửa test case; còn điền `Trạng thái` của test case thì vẫn phải hỏi người dùng trước.

## Thang mức độ nghiêm trọng và mức độ ưu tiên (mặc định, team đổi được; ghi bằng tiếng Việt, không ghi Severity/Priority/Critical/Major…)

| Mức độ nghiêm trọng | Khi nào |
|---|---|
| Nghiêm trọng (Critical) | Luồng chính không thực hiện được hoặc làm sai/mất dữ liệu, số tiền; không có cách đi vòng |
| Lớn (Major) | Chức năng quan trọng sai kết quả nghiệp vụ, hoặc không dùng được nhưng còn cách đi vòng |
| Nhỏ (Minor) | Chức năng phụ hoặc tình huống hiếm sai; có cách đi vòng; kết quả nghiệp vụ chính vẫn đúng |
| Rất nhỏ (Trivial) | Chữ, chính tả, căn lề, thông báo thiếu rõ nhưng không ảnh hưởng thao tác |

Lý do viết 1–2 câu nối với **ảnh hưởng cụ thể của bug này** (không chép định nghĩa). Mức độ ưu tiên: `Cao` (chặn việc test/vận hành tiếp theo hoặc cần sửa ngay), `Trung bình`, `Thấp`, kèm một câu lý do. Hai mức khác nhau: một bug Nhỏ vẫn có thể ưu tiên Cao nếu chặn luồng test khác. Trong file bug ghi chỉ tên tiếng Việt (ví dụ `**Rất nhỏ.**`), không kèm chữ tiếng Anh.

## Ảnh bằng chứng tô đỏ chỗ lỗi

Người đọc phải nhìn ảnh là thấy ngay lỗi ở đâu. Hai cách:
- **Script test tự làm** (nên dùng khi có script `auto/`): trong `check_main`/`check_minor` khai `mark_text="chữ lỗi"` và `error_note="Lỗi ở bước 5 (…): <thấy gì>, đáng ra <đúng là gì>."`. Khi ý đó sai, runner tự chụp thêm ảnh có khung đỏ + nhãn "LỖI" đúng chỗ chữ sai (trường `anh_loi`, câu chú thích ở `anh_loi_chu_thich`).
- **Ảnh đã chụp sẵn**: `python -X utf8 scripts/mark_error.py <ảnh.png> --box x1,y1,x2,y2` (góc trên-trái và dưới-phải của chữ lỗi, đơn vị điểm ảnh; khung tự nới vài điểm; ảnh gốc giữ nguyên, ra file `…-loi.png`). Xem ảnh kết quả bằng `Read` để chắc khung đúng chỗ rồi mới đính kèm.

Trong mục "Đính kèm cần có" mỗi ảnh lỗi ghi một dòng gồm cả hai đường dẫn, ví dụ: ảnh gốc `evidence/<dự-án>/…/x.png`; ảnh đã tô đỏ chỗ `DEFAULT` (lỗi ở bước 5 của các bước tái hiện): `evidence/<dự-án>/…/x-loi.png`. Chú thích lỗi theo khuôn: **"Lỗi ở bước N (việc đang làm): thấy <gì>, đáng ra <đúng là gì>."**

## Trang HTML của bug

Sau khi lưu file md: `python -X utf8 scripts/build_report.py bug-pages` (cũng chạy khi `… build`) dựng `BUG-nnn.html` cạnh file md. Trang này **tự sinh, không sửa tay**; sửa file md rồi chạy lại. Có: huy hiệu mức độ nghiêm trọng/ưu tiên/tần suất ở đầu; mỗi mục một thẻ có nút **Sao chép** (chép chữ thường để dán Jira, chat); "Sao chép tiêu đề" và "Sao chép cả bug (md)"; ảnh bằng chứng hiện thành ảnh nhỏ, ảnh tô đỏ có viền đỏ; `[Giả định: …]` tô vàng; chế độ sáng/tối. Mở bằng Chrome/Edge và báo link trang HTML cho người dùng (không chỉ link file md).

## Nối vào bảng kết quả smoke (khi bug đến từ lượt smoke)

Bảng ở `testing/<dự-án>/smoke-ket-qua.md/.html` sinh từ `testing/<dự-án>/run-results/smoke.json`. Lượt đã ghi mà chưa có bug thì dựng lại bằng lệnh ghi lượt kèm `--bug "N=BUG-nnn"` (cột Bug link thẳng tới trang HTML của bug), `--error-images "N=<ảnh -loi>"` và `--error-captions "N=Lỗi ở bước …"` (N là số ở cột # của `smoke-test.md`); chi tiết và ví dụ lệnh: `docs/chay-test-tu-dong.md` mục "Bảng kết quả smoke và trang web". Lượt mới sau này chạy `run_tests.py --smoke --record-run --build X` rồi ghi bug theo cùng cách. Hỏi người dùng trước khi dựng lại lượt đã ghi.

## Đọc gì cho từng việc
Sau `CLAUDE.md` và `memories/MEMORY.md` (bước 0 của quy trình chung: đọc `.du-an-hien-tai`): luôn đọc `memories/user/working-preferences.md`, `memories/project/overview.md`, `memories/modules/<slug>/overview.md` của **dự án hiện tại**. Không mở file dự án khác. Thêm:

| Việc | Đọc |
|---|---|
| Có mã test case | Dòng test case đó (`Grep` mã rồi `Read` đúng dòng, hoặc `python -X utf8 scripts/truy-vet.py tra <dự-án> <tính-năng> --ma TC-014`); **không đọc cả** `test-case.md` |
| Có mã requirement hoặc câu trả lời BA | Đúng dòng đó trong SRS/bảng soát (`Grep` kèm `| cut -c1-300`) |
| Cần viết câu hỏi cho BA | `memories/conventions/ba-question-wording.md`, `memories/modules/<slug>/tu-ngu-cau-hoi-ba.md` |
| Cần hiểu nghiệp vụ để chấm ảnh hưởng | `memories/modules/<slug>/feature-<tên>.md` của feature liên quan |

## Quy trình

0. **Đọc đúng những file cần cho việc này** (bảng trên).
1. **Chốt đầu vào**: ghi chú lỗi; môi trường; mã test case (hoặc "không có"); requirement (hoặc "không có"); hệ thống và feature (slug). Người dùng chỉ đưa ghi chú trần thì vẫn làm, phần nào thiếu thì xử lý ở bước 2.
2. **Kiểm cái chặn việc viết**: thiếu bước tái hiện, thiếu môi trường, hoặc kết quả thực tế quá chung chung → **hỏi tối đa 3 câu rồi dừng** (quy tắc 4, 5). Có mã test case thì bước và điều kiện trước lấy từ test case, không phải hỏi lại.
3. **Tách hay gộp**: đọc ghi chú tìm các lỗi riêng (quy tắc 3). Nhiều chỗ khác nhau mà ghi chú nói chung nguyên nhân/Dev đã xác nhận → một bug, có mục "Phạm vi ảnh hưởng" liệt kê **từng chỗ** (màn hình, dữ liệu, kết quả sai của từng chỗ). Còn lại tách riêng. Một bug thì bỏ trống mục Phạm vi ảnh hưởng ("Không có: chỉ một chỗ").
4. **Viết** theo `assets/mau-bug-report.md` (đúng thứ tự và tên mục). Tiêu đề `[Module] Mô tả lỗi`: module là tên màn hình/chức năng người dùng thấy, mô tả **chỉ nói cái gì đang sai**, ngắn gọn (ví dụ `[Hồ sơ vay] Nút Gửi thẩm định vẫn bật khi thiếu tài sản`), không "lỗi ở màn hình X", **không thêm lý do hay ngữ cảnh** như "dù BA đã chốt bỏ" hoặc hậu quả (hậu quả để ở mục Ảnh hưởng nghiệp vụ). Gọi các thành phần giao diện bằng tên người dùng quen (ví dụ "thanh điều hướng", không "thanh điều hướng"). **Câu hỏi cho Dev** viết đủ nghĩa để đọc một mình cũng hiểu: nêu điều đã thấy, điều chưa biết, vì sao hỏi và mình sẽ làm gì tùy câu trả lời; không viết cụt kiểu "A có chung nguyên nhân với B không?". Gắn `[Giả định: …]` ở chỗ tự thêm.
5. **Lưu file**: `testing/<slug>/<feature>/bug/BUG-<nnn>.md` (feature chưa rõ: `testing/<slug>/bug/`). `nnn` là số kế tiếp trong thư mục (001, 002…); tạo thư mục nếu chưa có. Mã `BUG-nnn` chỉ là mã nội bộ của repo; công cụ quản lý bug của team cấp mã riêng thì người dùng ghi thêm. Một bug một file. **Trước khi lưu**, có ảnh lỗi thì tô đỏ chỗ lỗi và soạn câu chú thích "Lỗi ở bước N" (mục "Ảnh bằng chứng tô đỏ chỗ lỗi"). **Sau khi lưu**, chạy `python -X utf8 scripts/build_report.py bug-pages` dựng trang `BUG-<nnn>.html` cạnh file md (mục "Trang HTML của bug") và báo link trang HTML cho người dùng.
6. **Tự kiểm** (dưới), sửa hết rồi mới trả lời.
7. **Cập nhật bộ nhớ** nếu có điều mới đáng ghi (bẫy, quy ước người dùng vừa chốt): `memories/modules/<slug>/feature-<tên>.md` hoặc `memories/project/skills.md`.
8. **Trả lời** ngắn: link trang HTML và file md của bug; tiêu đề; mức độ nghiêm trọng + mức độ ưu tiên đề xuất; **danh sách Giả định** (in nguyên trong chat); **câu hỏi còn mở** cho BA/Dev; đính kèm còn thiếu. Nói rõ **chưa tái hiện lại** (chỉ viết theo ghi chú). Test case Không đạt: **hỏi có muốn điền `Kết quả thực tế` và `Trạng thái` = Không đạt vào dòng test case không**, không tự sửa. Bug từ lượt smoke: hỏi có dựng lại lượt để điền mã bug và ảnh tô đỏ vào bảng smoke không. Commit chỉ khi người dùng nhờ.

## Tự kiểm trước khi trả lời
- [ ] Mục **Kết quả thực tế** không có câu chung chung nào ở quy tắc 5: đọc lại từng câu, hỏi "Dev đọc câu này có thấy được màn hình lúc đó không?".
- [ ] Mọi thông tin tự thêm đều có nhãn `[Giả định: …]` và nhãn đó xuất hiện đủ trong danh sách Giả định cuối file (đếm hai bên bằng nhau).
- [ ] Kết quả mong đợi có nguồn (requirement hoặc test case); không có thì là `Chưa xác định` + câu hỏi BA.
- [ ] Mọi bước tái hiện bắt nguồn từ ghi chú hoặc test case; bước đầu có môi trường/tài khoản đủ để làm theo.
- [ ] Không có mật khẩu, không có nguyên nhân gốc tự đoán, không có cách sửa.
- [ ] Gộp nhiều chỗ chỉ khi ghi chú nói chung nguyên nhân/Dev xác nhận; tách riêng thì có câu hỏi cho Dev.
- [ ] Đủ các mục theo mẫu; tần suất đúng một trong ba dạng (hoặc `Chưa rõ` kèm danh sách cuối).
- [ ] **Tiêu đề** chỉ nói cái gì sai: không có "dù…", "vì…", "theo BA…", không có hậu quả; dùng đúng tên thành phần người dùng gọi.
- [ ] **Môi trường**: dòng Trình duyệt chỉ có tên + số bản (+ hệ điều hành), không công cụ chạy, không nhãn Giả định.
- [ ] **Kết quả mong đợi** không có ngoặc "(theo TC…, theo BA…)"; nguồn nằm ở mục Test case liên quan.
- [ ] **Mức độ nghiêm trọng/ưu tiên** viết tiếng Việt (Nghiêm trọng/Lớn/Nhỏ/Rất nhỏ; Cao/Trung bình/Thấp), không có chữ Severity/Priority/Trivial…
- [ ] **Câu hỏi cho Dev** đọc một mình cũng hiểu: có điều đã thấy, điều chưa biết, vì sao hỏi, sẽ làm gì tùy câu trả lời.
- [ ] **Ảnh lỗi** có bản tô đỏ (đã `Read` kiểm khung đúng chỗ) và mỗi dòng ghi lỗi ở bước nào.
- [ ] **Trang HTML** đã dựng lại sau lần sửa md cuối; bug từ smoke đã được hỏi để nối vào bảng kết quả.

## Tệp trong skill
- `assets/mau-bug-report.md` — hình dạng file bug (ví dụ trung lập, đủ nhãn Giả định, câu hỏi BA, câu hỏi Dev, phạm vi ảnh hưởng, ảnh lỗi tô đỏ kèm lỗi ở bước nào).
- Công cụ dùng chung của repo (không nằm trong skill): `scripts/build_report.py` (`bug-pages`, ghi lượt smoke), `scripts/mark_error.py` (tô đỏ ảnh), `scripts/test_automation/bug_html.py` (dựng trang bug), `docs/chay-test-tu-dong.md` (hướng dẫn cho người dùng).
- Bug mẫu đã làm xong để tham khảo cách viết đúng ý người dùng: `testing/banking-lite/dang-nhap/bug/BUG-001.md`.
