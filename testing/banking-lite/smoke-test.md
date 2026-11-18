# Bộ smoke test — Banking Lite (bản 1.3.0)

| | |
|---|---|
| Ngày lập | 2026-11-18 |
| Cập nhật lần cuối | 2026-11-18 20:52:17 (+07:00) (cập nhật: Thêm giao thức chạy smoke (references/chay-smoke.md) và mục Lượt chạy; lệnh ghi-luot) |
| Người lập | Sunny Tran |
| Hệ thống | Banking Lite, https://banking-lite.vercel.app/ |
| Thời gian mục tiêu (tham khảo, không cứng) | **khoảng 15 phút** (người dùng chốt) |
| Nguồn case | Chỉ chọn từ test case đã có: [Đăng nhập](dang-nhap/test-case.md) (43 case) và [Khuyến nghị LTV/DSR](khuyen-nghi-ltv-dsr/test-case.md) (38 case). Hai file đều có mã TC-001, TC-002… nên cột Mã case gốc ghi kèm tên module |
| Case mới đề xuất | Không có (đã có case phù hợp cho mọi dòng) |
| Release note | **Chưa có**, nên chưa có dòng nào thuộc phần Theo build |
| Truy vết | Cột Mã case gốc link tới đúng dòng test case gốc; mục "Truy vết" và "Lịch sử tạo và cập nhật" ở cuối file. Chỉ một file này, mốc nằm trong file |
| Tình trạng | Mọi case gốc đang ở trạng thái "Chưa chạy" (chưa case nào chạy thật trên hệ thống); thời gian là **ước lượng**. 4 trong 7 case thuộc Khuyến nghị LTV/DSR, mà SRS này là bản nháp chưa BA xác nhận: lượt chạy đầu là lượt hiệu chuẩn, case Không đạt thì kiểm lại test case trước khi kết luận trả build |

**Mục đích.** Smoke test trả lời một câu: build này đủ ổn để bắt đầu test sâu chưa? Một case được chọn khi nó hỏng thì việc test khác vô nghĩa hoặc bị chặn, không phải vì nó nhanh hay dễ. Thời gian chỉ là mục tiêu để giữ smoke nông và gọn; nếu một case cần cho mục đích mà làm vượt mục tiêu thì giữ case, chấp nhận vượt và ghi lý do, không bỏ case quan trọng chỉ vì thời gian.

**Cách đọc.** Bảng xếp theo **thứ tự nên chạy**, không phải theo module: làm xong các case Đăng nhập bằng `P100001` thì giữ nguyên phiên đăng nhập đó để chạy luôn các case Khuyến nghị, rồi mới đăng xuất để thử hai vai trò còn lại. Mật khẩu do người kiểm thử tự gõ, không ghi vào tài liệu.

| # | Smoke case | Mã case gốc | Phần | Vì sao chọn | Thời gian ước tính | Nên tự động hoá? |
|---|---|---|---|---|---|---|
| 1 | Hiển thị form đăng nhập đủ ô nhập, nút và phiên bản ở chân trang khi mở hệ thống lúc chưa đăng nhập | [Đăng nhập · TC-005](dang-nhap/test-case.md#tc-005) | Cố định | Là màn hình đầu tiên mọi người gặp; nếu form không hiện hoặc sai thì chưa cần chạy tiếp. Không cần mật khẩu nên nhanh nhất. Dòng phiên bản ở chân trang còn cho biết có đúng bản build cần test không (case gốc ghi `1.3.0`; build mới đổi số phiên bản thì đối chiếu theo số của build đó) | 1 phút | Nên: kiểm giao diện tĩnh, không cần mật khẩu |
| 2 | Vào được Danh sách việc của Chuyên viên khách hàng khi đăng nhập đúng `P100001` | [Đăng nhập · TC-001](dang-nhap/test-case.md#tc-001) | Cố định | Đăng nhập đúng là cửa vào của mọi việc test khác, và `P100001` là tài khoản tạo hồ sơ nên các case Khuyến nghị bên dưới cần nó. ⚠️ Kết quả mong đợi gốc có ý "thanh trên không còn chữ `DEFAULT`" (BA đã chốt ở câu TL-07) nhưng bản 1.3.0 hiện còn chữ này, nên case sẽ Không đạt ở ý đó nếu chưa sửa (xem mục "Cần team chốt") | 1,5 phút | Nên, có điều kiện: script lấy mật khẩu từ biến môi trường, không ghi mật khẩu vào script |
| 3 | Hiển thị khuyến nghị Phê duyệt khi nhập lương 100 triệu và hồ sơ đạt mọi quy tắc | [Khuyến nghị LTV/DSR · TC-002](khuyen-nghi-ltv-dsr/test-case.md#tc-002) | Cố định | Đường chạy bình thường của chức năng Khuyến nghị: nhập lương thì khung `Thẩm định` đổi ngay (không cần bấm `Lưu`), ra nhãn, các chỉ số và lý do. Case gốc không có điểm hệ thống đang làm khác | 1 phút | Nên: chỉ nhập số rồi đọc chữ trên khung |
| 4 | Hiển thị Chuyển cấp trên khi DSR 54,40% (lương 75 triệu) | [Khuyến nghị LTV/DSR · TC-023](khuyen-nghi-ltv-dsr/test-case.md#tc-023) | Cố định | Kết quả thứ hai của Khuyến nghị, kiểm bằng một lần nhập. Chọn số nằm giữa 50% và 70%, không sát ranh giới nên không dính lỗi làm tròn đã biết ở các case sát 50%/70% | 1 phút | Nên: như dòng 3 |
| 5 | Hiển thị Từ chối kèm lý do khi thặng dư hằng tháng thiếu 1 đồng so với mức tối thiểu | [Khuyến nghị LTV/DSR · TC-009](khuyen-nghi-ltv-dsr/test-case.md#tc-009) | Cố định | Kết quả thứ ba của Khuyến nghị: Từ chối và có dòng lý do. Chọn ca thặng dư vì chỉ cần đổi hai ô và không dính lỗi làm tròn DSR/LTV đã biết | 1,5 phút | Nên: như dòng 3 |
| 6 | Cập nhật khuyến nghị ở đầu trang hồ sơ sau vài giây khi nhập lương rồi bấm Lưu | [Khuyến nghị LTV/DSR · TC-022](khuyen-nghi-ltv-dsr/test-case.md#tc-022) | Cố định | Ô Khuyến nghị ở đầu trang là chỗ mọi người nhìn thấy. Một case kiểm cả chuỗi: bấm `Lưu` → hiện `Đã lưu.` → đầu trang đổi sau vài giây → bước `Tài chính` ghi `Đã xong` → tải lại trang vẫn còn số liệu. Hỏng chỗ này thì khung xem trước đúng nhưng hồ sơ vẫn sai | 2 phút (có chờ khoảng 8 giây) | Nên, làm sau cùng: phải chờ cập nhật nên dễ chập chờn nếu chờ cố định, cần chờ theo điều kiện |
| 7 | Vào được đúng Danh sách việc và đúng vai trò khi đăng nhập bằng `P200001` rồi `P300001` | [Đăng nhập · TC-002](dang-nhap/test-case.md#tc-002) | Cố định | Hai vai trò còn lại của hệ thống; nếu một trong hai không đăng nhập được thì không test được việc của vai trò đó. Case gốc không có điểm hệ thống đang làm khác. Xếp cuối vì phải đăng xuất khỏi `P100001` trước | 2,5 phút | Nên, có điều kiện: như dòng 2, đổi tài khoản giữa chừng |

**Theo build:** chưa có dòng nào vì chưa có release note. Khi chưa có release note, gợi ý chỗ đổi bằng `python -X utf8 scripts/truy-vet.py kiem banking-lite <tính-năng>` (tính đến 2026-11-18 chưa có mã requirement nào đổi sau lần chốt gần nhất); là gợi ý suy ra từ requirement, không phải từ build, người dùng đồng ý mới đưa vào bảng.

**Phạm vi chưa phủ:** hành trình then chốt của hệ thống (tạo hồ sơ, định giá, gửi thẩm định, quyết định tín dụng) và trang Tích hợp chưa có test case nào, nên smoke Đạt không bảo đảm các hành trình này; chỉ bảo đảm Đăng nhập, ba vai trò và Khuyến nghị LTV/DSR dùng được.

## Thời gian ước tính (tham khảo)

| Khoản | Phút (ước lượng) |
|---|---|
| 7 smoke case (1 + 1,5 + 1 + 1 + 1,5 + 2 + 2,5) | 10,5 |
| Chuẩn bị chung, không phải case: tạo một hồ sơ nháp bằng `Tạo từ hồ sơ có sẵn` để dùng cho dòng 3–6 (làm một lần; bỏ qua nếu đã có sẵn hồ sơ nháp đúng điều kiện trước của các case gốc) | 2 |
| **Tổng** | **12,5, dưới mục tiêu khoảng 15** |

Ước lượng theo số bước (mỗi bước khoảng 15–20 giây, trang tải 3–5 giây, thêm thời gian tự gõ mật khẩu), chưa đo bằng chạy thật; sau lần chạy đầu nên thay bằng số đo thực. Không dùng con số này để cắt case.

## Tiêu chí trả build

Chạy theo thứ tự bảng. **Case nào Không đạt thì dừng ngay, trả build, không chạy tiếp.** "Đạt" chỉ xét **ý chính** (theo số bước của case gốc); ý phụ chỉ ghi vào Kết quả thực tế, không dừng. *Phần tách ý chính/ý phụ là đề xuất, chờ người dùng duyệt.*

| Case | Đạt khi (ý chính; ý phụ ghi trong ngoặc) | Không đạt thì dừng vì |
|---|---|---|
| 1. Form đăng nhập | Bước 2, 4, 5: có ô `Mã nhân viên`, ô `Mật khẩu`, nút `Đăng nhập` và chân trang đúng số phiên bản của build. (Ý phụ: bước 3 dòng gợi ý định dạng, bước 7 chữ mật khẩu hiện dạng chấm) | Hệ thống không dùng được hoặc sai bản build |
| 2. Đăng nhập `P100001` | Bước 4, 5: vào Danh sách việc của `P100001`, thanh trên hiện `P100001` và vai trò `Chuyên viên khách hàng`. (Ý phụ: không có thông báo "đăng nhập thành công".) **Ngoại lệ đã chốt 2026-11-18:** bản 1.3.0 còn chữ `DEFAULT` trên thanh trên dù BA đã chốt bỏ (TL-07); chỉ sai ở ý này thì ghi "Đạt kèm lỗi đã biết" kèm mã bug ở Kết quả thực tế, không dừng. Bỏ ngoại lệ khi lỗi được sửa | Không vào được Danh sách việc, hoặc thanh trên sai mã hay vai trò: không test được gì tiếp |
| 3. Khuyến nghị Phê duyệt | Bước 5: khung `Thẩm định` đổi ngay khi nhập (không cần `Lưu`); nhãn `Phê duyệt`; DSR `40,80%`; thặng dư `54.700.000 VND`; lý do `Đáp ứng mọi quy tắc tín dụng.` (Ý phụ: dòng nhỏ "Xem trước…", các chỉ số khoản trả mới, thu nhập và chi phí được tính) | Khuyến nghị cho sai nhãn, sai chỉ số hoặc không hiện |
| 4. Khuyến nghị Chuyển cấp trên | Bước 5: DSR `54,40%` và nhãn `Chuyển cấp trên` | Như dòng 3 |
| 5. Khuyến nghị Từ chối | Bước 6: thặng dư `2.999.999 VND`, nhãn `Từ chối`, lý do `Từ chối: Thặng dư hằng tháng 2.999.999 VND thấp hơn 3.000.000 VND.` | Như dòng 3 |
| 6. Cập nhật đầu trang sau khi Lưu | Bước 5 đến 8: hiện `Đã lưu.`; sau vài giây ô Khuyến nghị đầu trang thành `Phê duyệt`; bước `Tài chính` ghi `Đã xong`; tải lại trang ô `Lương hằng tháng` vẫn `100000000` | Khuyến nghị đã lưu không phản ánh lên hồ sơ |
| 7. Đăng nhập `P200001`, `P300001` | Bước 4, 5, 9, 10: mỗi tài khoản vào đúng Danh sách việc và đúng vai trò. (Ý phụ: bước 6 đăng xuất về form `Đăng nhập`) | Một vai trò không vào được, các việc của vai trò đó bị chặn |

Đạt cả 7 thì nhận build để test sâu.

## Lượt chạy

Mỗi lần chạy smoke cho một build ghi một dòng: `python -X utf8 scripts/truy-vet-smoke.py ghi-luot <dự-án> --build "<số bản ở chân trang>" --ket-qua "1=Đạt,2=Không đạt" [--ghi-chu "…"]` (số là cột # của bảng; case không nêu coi là Chưa chạy; script tự tính nhận hay trả build). Cách chạy: skill `tao-smoke-test`, mục "Chạy smoke".

<!-- LUOT-CHAY:BAT-DAU (tự sinh bởi scripts/truy-vet-smoke.py ghi-luot, không sửa tay) -->
<!-- LUOT-CHAY:KET-THUC -->

## Truy vết về test case và requirement

Bảng tự sinh khi chốt (đừng sửa tay). Chỉ mã có điểm nhảy trong tài liệu nguồn mới có link (SRS Đăng nhập chưa có điểm nhảy theo mã).

<!-- TRUY-VET:BAT-DAU (tự sinh bởi scripts/truy-vet-smoke.py, không sửa tay) -->
| # | Test case gốc | Requirement mà test case dựa vào |
|---|---|---|
| 1 | [Đăng nhập · TC-005](dang-nhap/test-case.md#tc-005) | M07 Nhãn, nút, gợi ý, chân trang<br>R01 Mã nhân viên: định dạng<br>R08 Thuộc tính ô nhập<br>S01-AC01 Mở hệ thống khi chưa đăng nhập<br>[TL-04](dang-nhap/bang-soat-requirement.md#tl-04) BA: tự cắt khoảng trắng, p hoa thường đều được |
| 2 | [Đăng nhập · TC-001](dang-nhap/test-case.md#tc-001) | R05 Hiển thị sau đăng nhập<br>S01-AC02 Đăng nhập đúng<br>[TL-05](dang-nhap/bang-soat-requirement.md#tl-05) BA: bỏ mã không gian<br>[TL-07](dang-nhap/bang-soat-requirement.md#tl-07) BA: bỏ DEFAULT trên thanh trên |
| 3 | [Khuyến nghị LTV/DSR · TC-002](khuyen-nghi-ltv-dsr/test-case.md#tc-002) | [M02](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#reco-m02) Không có lý do<br>[M03](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#reco-m03) Dòng xem trước<br>[S01-AC02](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#reco-s01-ac02) Đạt mọi quy tắc<br>[S03-AC01](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#reco-s03-ac01) DSR và thặng dư cơ bản |
| 4 | [Khuyến nghị LTV/DSR · TC-023](khuyen-nghi-ltv-dsr/test-case.md#tc-023) | [R02](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#reco-r02) DSR<br>[S01-AC03](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#reco-s01-ac03) DSR trên 50% |
| 5 | [Khuyến nghị LTV/DSR · TC-009](khuyen-nghi-ltv-dsr/test-case.md#tc-009) | [M07](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#reco-m07) Thặng dư thấp<br>[R03](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#reco-r03) Thặng dư tối thiểu<br>[S01-AC09](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#reco-s01-ac09) Thặng dư thiếu 1 đồng |
| 6 | [Khuyến nghị LTV/DSR · TC-022](khuyen-nghi-ltv-dsr/test-case.md#tc-022) | [M11](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#reco-m11) Đã lưu<br>[S05-AC01](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#reco-s05-ac01) Đầu trang sau khi lưu |
| 7 | [Đăng nhập · TC-002](dang-nhap/test-case.md#tc-002) | S01-AC02 Đăng nhập đúng |
<!-- TRUY-VET:KET-THUC -->

## Khi requirement hoặc test case đổi

Chạy `python -X utf8 scripts/truy-vet-smoke.py kiem banking-lite` (chỉ đọc, in vài dòng). Case báo "Cần xem lại" hoặc "Test case đã sửa": đọc lại test case gốc rồi giữ, đổi hoặc bỏ; sửa trực tiếp bảng 7 cột trong file này. Khớp rồi thì chốt: `python -X utf8 scripts/truy-vet-smoke.py chot banking-lite -m "đã làm gì"` (thêm một dòng lịch sử, không tạo file mới). Case mới chưa có test case gốc thì viết test case gốc trước rồi link.

## Lịch sử tạo và cập nhật

<!-- LICH-SU:BAT-DAU (tự sinh bởi scripts/truy-vet-smoke.py, không sửa tay) -->
| Thời điểm | Việc | Người | Nội dung | Số case · tổng phút (ước lượng) | Commit |
|---|---|---|---|---|---|
| 2026-11-18 20:52:17 (+07:00) | Cập nhật | Sunny Tran | Thêm giao thức chạy smoke (references/chay-smoke.md) và mục Lượt chạy; lệnh ghi-luot | 7 case · 10.5 phút | `b4aa480` + sửa chưa commit |
| 2026-11-18 20:44:03 (+07:00) | Cập nhật | Sunny Tran | Sửa skill theo 9 điểm yếu: tiêu chí trả build tách ý chính/ý phụ, ghi nguồn nháp và hiệu chuẩn, nêu hành trình then chốt chưa phủ, cách gợi ý Theo build khi thiếu release note | 7 case · 10.5 phút | `b4aa480` + sửa chưa commit |
| 2026-11-18 20:01:17 (+07:00) | Cập nhật | Sunny Tran | Gộp mốc vào chính smoke-test.md (bỏ file trạng thái riêng), nêu mục đích smoke, thời gian chỉ là mục tiêu tham khảo, kiem chỉ đọc | 7 case · 10.5 phút | `b4aa480` + sửa chưa commit |
| 2026-11-18 19:54:27 (+07:00) | Tạo | Sunny Tran | Lập bộ smoke 7 case (15 phút) từ test case Đăng nhập và Khuyến nghị LTV/DSR; dòng 2 chấp nhận Đạt kèm lỗi đã biết (chữ DEFAULT) | 7 case · 10.5 phút | `cf37198` + sửa chưa commit |
<!-- LICH-SU:KET-THUC -->
<!-- SMOKE-MOC: {"case":{"dang-nhap/TC-005":{"r":"7b602cd913f0","ma":{"M07":["d7c4552a3a88","da39a3ee5e6b"],"R01":["0b762b63fb39","e92d1ddc9d42"],"R08":["7bba4ba50532","da39a3ee5e6b"],"S01-AC01":["d13831240388","da39a3ee5e6b"],"TL-04":["872b30229470",null]}},"dang-nhap/TC-001":{"r":"874bedfd980f","ma":{"R05":["c6a67abebd4a","54252341552a"],"S01-AC02":["08ac33d9778f","77693246d074"],"TL-05":["42a89a86e071",null],"TL-07":["c738acb48580",null]}},"khuyen-nghi-ltv-dsr/TC-002":{"r":"c6cdf480503e","ma":{"M02":["a0cfc54cf81c","da39a3ee5e6b"],"M03":["03e173a7af08","da39a3ee5e6b"],"S01-AC02":["e3a41c4cc822","da39a3ee5e6b"],"S03-AC01":["dffce2b59092","da39a3ee5e6b"]}},"khuyen-nghi-ltv-dsr/TC-023":{"r":"11b360a076f7","ma":{"R02":["b9978d62c370","da39a3ee5e6b"],"S01-AC03":["cdd38ef22c13","da39a3ee5e6b"]}},"khuyen-nghi-ltv-dsr/TC-009":{"r":"07f587002874","ma":{"M07":["d015cb137888","da39a3ee5e6b"],"R03":["5fcd2e15a9f3","da39a3ee5e6b"],"S01-AC09":["dcdf8c8b87c7","da39a3ee5e6b"]}},"khuyen-nghi-ltv-dsr/TC-022":{"r":"a26e5e9923d6","ma":{"M11":["b28f98ecb030","da39a3ee5e6b"],"S05-AC01":["f36aa740a105","da39a3ee5e6b"]}},"dang-nhap/TC-002":{"r":"e74cb91dcb47","ma":{"S01-AC02":["08ac33d9778f","77693246d074"]}}}} -->
