# Bộ smoke test — Banking Lite (bản 1.3.0)

| | |
|---|---|
| Ngày lập | 2026-11-18 |
| Cập nhật lần cuối | 2026-11-18 19:54:27 (+07:00) (tạo: Lập bộ smoke 7 case (15 phút) từ test case Đăng nhập và Khuyến nghị LTV/DSR; dòng 2 chấp nhận Đạt kèm lỗi đã biết (chữ DEFAULT)) |
| Người lập | Sunny Tran |
| Hệ thống | Banking Lite, https://banking-lite.vercel.app/ |
| Thời gian tối đa cho một lượt smoke | **15 phút** (người dùng chốt) |
| Nguồn case | Chỉ chọn từ test case đã có: [Đăng nhập](dang-nhap/test-case.md) (43 case) và [Khuyến nghị LTV/DSR](khuyen-nghi-ltv-dsr/test-case.md) (38 case). Hai file đều có mã TC-001, TC-002… nên cột Mã case gốc ghi kèm tên module |
| Case mới đề xuất | Không có (đã có case phù hợp cho mọi dòng) |
| Release note | **Chưa có**, nên chưa có dòng nào thuộc phần Theo build |
| Truy vết | Từng smoke case link tới đúng dòng test case gốc (cột Mã case gốc) và về requirement; xem mục "Truy vết" và "Lịch sử tạo và cập nhật" ở cuối file. Mốc lưu ở `smoke-trang-thai.json` |
| Tình trạng | Mọi case gốc đang ở trạng thái "Chưa chạy"; thời gian bên dưới là **ước lượng**, chưa đo bằng cách chạy thật |

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

**Theo build:** chưa có dòng nào vì chưa có release note. Khi có release note, mình chọn thêm case từ hai module trên theo chỗ vừa đổi (hoặc đề xuất case mới nếu chỗ đổi chưa có case nào).

## Tổng thời gian ước tính

| Khoản | Phút (ước lượng) |
|---|---|
| 7 smoke case (1 + 1,5 + 1 + 1 + 1,5 + 2 + 2,5) | 10,5 |
| Chuẩn bị chung, không phải case: tạo một hồ sơ nháp bằng `Tạo từ hồ sơ có sẵn` để dùng cho dòng 3–6 (làm một lần; bỏ qua nếu đã có sẵn hồ sơ nháp đúng điều kiện trước của các case gốc) | 2 |
| **Tổng** | **12,5 trên mức tối đa 15, còn dư khoảng 2,5 phút** |

Cách ước lượng: mỗi bước thao tác khoảng 15–20 giây, trang tải khoảng 3–5 giây, thêm thời gian người kiểm thử tự gõ mật khẩu. Đây là ước lượng theo số bước, chưa đo bằng chạy thật; sau lần chạy đầu nên thay bằng số đo thực.

## Tiêu chí trả build

Chạy theo thứ tự bảng. **Case nào Không đạt thì dừng ngay, trả build, không chạy tiếp**:

| Case không đạt | Vì sao dừng |
|---|---|
| 1. Form đăng nhập | Hệ thống không dùng được hoặc sai bản build |
| 2. Đăng nhập `P100001` | Không vào được Danh sách việc, hoặc thanh trên không hiện đúng mã và vai trò: không test được gì tiếp. Riêng ý chữ `DEFAULT` đã chốt: chỉ sai ở ý này thì ghi "Đạt kèm lỗi đã biết", không dừng (xem mục "Đã chốt") |
| 3, 4, 5. Phê duyệt / Chuyển cấp trên / Từ chối | Chức năng Khuyến nghị cho sai nhãn, sai chỉ số hoặc không hiện |
| 6. Cập nhật đầu trang sau khi Lưu | Khuyến nghị đã lưu không phản ánh lên hồ sơ |
| 7. Đăng nhập `P200001`, `P300001` | Một vai trò không vào được, các việc của vai trò đó bị chặn |

Đạt cả 7 thì nhận build để test sâu.

## Đã chốt

- **Dòng 2 và chữ `DEFAULT`** (người dùng chốt 2026-11-18). Bản 1.3.0 còn chữ `DEFAULT` trên thanh trên trong khi BA đã chốt bỏ (TL-07). Cách xử lý: khi chỉ sai ở ý chữ `DEFAULT` mà vẫn vào được Danh sách việc và thanh trên hiện đúng `P100001` cùng vai trò `Chuyên viên khách hàng`, ghi Trạng thái "Đạt kèm lỗi đã biết" ở dòng 2 và chạy tiếp. Ghi mã bug vào cột Kết quả thực tế. Bỏ cách xử lý này khi lỗi được sửa. Chưa kiểm tra bug này đã được tạo chưa.

## Còn cần

- **Release note** của build: có thì gửi để bổ sung phần Theo build.

## Không đưa vào smoke (và lý do)

- **Các case khóa tài khoản** (Đăng nhập TC-014 đến TC-022: sai 9–11 lần, chờ 5 phút): có thể khóa tài khoản và mỗi case mất vài phút, không hợp với smoke.
- **Sai mật khẩu một lần** (Đăng nhập TC-006): thuộc luồng lỗi, không phải luồng cơ bản, và phải được người dùng đồng ý trước khi nhập sai; nên để ở test sâu.
- **Các case Khuyến nghị sát ranh giới 50%, 70%, 80%** (như TC-004, TC-005, TC-006, TC-010, TC-012): bản 1.3.0 đang làm tròn khác kết quả mong đợi, đưa vào smoke sẽ chặn build vì một lỗi chưa BA xác nhận.
- **Chức năng chưa có test case** (tạo hồ sơ, định giá, gửi thẩm định, quyết định tín dụng, tích hợp): không đưa vào vì chưa có case và không tự thêm chức năng. Hành trình thật của hệ thống đi qua các chức năng này nên bộ smoke hiện mới phủ phần Đăng nhập và Khuyến nghị; muốn phủ rộng hơn thì cần viết test case cho chúng trước.

## Truy vết về test case và requirement

Mỗi smoke case chỉ là một con trỏ tới test case gốc, nên khi requirement đổi và test case gốc được sửa theo thì smoke phải được xem lại. Bảng dưới do script tự sinh (đừng sửa tay): cột Test case gốc bấm vào là tới đúng dòng; cột Requirement liệt kê các mã mà test case gốc dựa vào; cột Truy vết cho biết case còn đúng hay cần xem lại. Chỉ những mã có điểm nhảy trong tài liệu nguồn mới có link (SRS Khuyến nghị LTV/DSR có đủ; SRS Đăng nhập chưa có điểm nhảy theo mã).

<!-- TRUY-VET:BAT-DAU (tự sinh bởi scripts/truy-vet-smoke.py, không sửa tay) -->
Lần kiểm gần nhất: 2026-11-18 19:54:55 (+07:00) (chỉ kiểm, chưa đổi mốc). Mốc đã chốt: 2026-11-18 19:54:27 (+07:00). Kết quả: Còn đúng 7.

| # | Smoke case | Test case gốc | Requirement mà test case dựa vào | Truy vết |
|---|---|---|---|---|
| 1 | Hiển thị form đăng nhập đủ ô nhập, nút và phiên bản ở chân trang khi mở hệ thống lúc chưa… | [Đăng nhập · TC-005](dang-nhap/test-case.md#tc-005) | M07 Nhãn, nút, gợi ý, chân trang<br>R01 Mã nhân viên: định dạng<br>R08 Thuộc tính ô nhập<br>S01-AC01 Mở hệ thống khi chưa đăng nhập<br>[TL-04](dang-nhap/bang-soat-requirement.md#tl-04) BA: tự cắt khoảng trắng, p hoa thường đều được | Còn đúng |
| 2 | Vào được Danh sách việc của Chuyên viên khách hàng khi đăng nhập đúng `P100001` | [Đăng nhập · TC-001](dang-nhap/test-case.md#tc-001) | R05 Hiển thị sau đăng nhập<br>S01-AC02 Đăng nhập đúng<br>[TL-05](dang-nhap/bang-soat-requirement.md#tl-05) BA: bỏ mã không gian<br>[TL-07](dang-nhap/bang-soat-requirement.md#tl-07) BA: bỏ DEFAULT trên thanh trên | Còn đúng |
| 3 | Hiển thị khuyến nghị Phê duyệt khi nhập lương 100 triệu và hồ sơ đạt mọi quy tắc | [Khuyến nghị LTV/DSR · TC-002](khuyen-nghi-ltv-dsr/test-case.md#tc-002) | [M02](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#reco-m02) Không có lý do<br>[M03](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#reco-m03) Dòng xem trước<br>[S01-AC02](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#reco-s01-ac02) Đạt mọi quy tắc<br>[S03-AC01](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#reco-s03-ac01) DSR và thặng dư cơ bản | Còn đúng |
| 4 | Hiển thị Chuyển cấp trên khi DSR 54,40% (lương 75 triệu) | [Khuyến nghị LTV/DSR · TC-023](khuyen-nghi-ltv-dsr/test-case.md#tc-023) | [R02](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#reco-r02) DSR<br>[S01-AC03](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#reco-s01-ac03) DSR trên 50% | Còn đúng |
| 5 | Hiển thị Từ chối kèm lý do khi thặng dư hằng tháng thiếu 1 đồng so với mức tối thiểu | [Khuyến nghị LTV/DSR · TC-009](khuyen-nghi-ltv-dsr/test-case.md#tc-009) | [M07](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#reco-m07) Thặng dư thấp<br>[R03](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#reco-r03) Thặng dư tối thiểu<br>[S01-AC09](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#reco-s01-ac09) Thặng dư thiếu 1 đồng | Còn đúng |
| 6 | Cập nhật khuyến nghị ở đầu trang hồ sơ sau vài giây khi nhập lương rồi bấm Lưu | [Khuyến nghị LTV/DSR · TC-022](khuyen-nghi-ltv-dsr/test-case.md#tc-022) | [M11](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#reco-m11) Đã lưu<br>[S05-AC01](../../srs/banking-lite/khuyen-nghi-ltv-dsr.md#reco-s05-ac01) Đầu trang sau khi lưu | Còn đúng |
| 7 | Vào được đúng Danh sách việc và đúng vai trò khi đăng nhập bằng `P200001` rồi `P300001` | [Đăng nhập · TC-002](dang-nhap/test-case.md#tc-002) | S01-AC02 Đăng nhập đúng | Còn đúng |
<!-- TRUY-VET:KET-THUC -->

## Khi requirement hoặc test case đổi thì làm gì

1. Làm như thường lệ cho tính năng đó: sửa test case, chạy `python -X utf8 scripts/truy-vet.py kiem banking-lite <tính-năng>` rồi `chot`.
2. Chạy kiểm smoke:

```powershell
python -X utf8 scripts/truy-vet-smoke.py kiem banking-lite
```

3. Case nào báo **Cần xem lại** (requirement mà test case gốc dựa vào đã đổi) hoặc **Test case đã sửa**: đọc lại test case gốc, quyết định giữ, đổi sang case khác hoặc bỏ; nếu thêm, đổi, bỏ case thì sửa bảng 7 cột, kiểm lại tổng thời gian không vượt mức tối đa, và kiểm lại tiêu chí trả build.
4. Khi bộ smoke đã khớp, chốt mốc kèm một câu nói đã làm gì:

```powershell
python -X utf8 scripts/truy-vet-smoke.py chot banking-lite -m "đã làm gì"
```

Script cũng báo khi: tổng thời gian các case vượt mức tối đa, một test case xuất hiện hai lần, link trỏ tới dòng không còn, hoặc cột Phần ghi khác "Cố định"/"Theo build". Case mới (chưa có test case gốc) chưa truy vết được bằng script; khi thêm, nhớ viết test case gốc trước rồi link.

## Lịch sử tạo và cập nhật

<!-- LICH-SU:BAT-DAU (tự sinh bởi scripts/truy-vet-smoke.py, không sửa tay) -->
| Thời điểm | Việc | Người | Nội dung | Số case · tổng phút (ước lượng) | Commit |
|---|---|---|---|---|---|
| 2026-11-18 19:54:27 (+07:00) | Tạo | Sunny Tran | Lập bộ smoke 7 case (15 phút) từ test case Đăng nhập và Khuyến nghị LTV/DSR; dòng 2 chấp nhận Đạt kèm lỗi đã biết (chữ DEFAULT) | 7 case · 10.5 phút | `cf37198` + sửa chưa commit |
<!-- LICH-SU:KET-THUC -->
