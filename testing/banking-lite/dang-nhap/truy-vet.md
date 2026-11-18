# Truy vết — Đăng nhập (Banking Lite)

*File này do `scripts/truy-vet.py` tự sinh, đừng sửa tay. Muốn đổi thì sửa nguồn rồi chạy lại script.*

| | |
|---|---|
| Lần chạy gần nhất | 2026-11-18 (chỉ kiểm, chưa đổi mốc) |
| Requirement | srs/banking-lite/dang-nhap.md (cập nhật 2026-11-17); bảng soát (cập nhật 2026-11-18), câu trả lời đến TL-13 |
| Checklist, test case | [checklist.md](checklist.md), [test-case.md](test-case.md) |
| Mốc đã chốt | 2026-11-18 (khi đó: SRS 2026-11-17, bảng soát 2026-11-18, TL đến TL-13) |

## 1. Tóm tắt
- Mã requirement: 39 trong SRS, 13 câu trả lời (TL). Test case: 41.
- Trạng thái test case: Còn đúng 41
- Mã requirement đã đổi so với mốc đã chốt: không có; mã mới: không có.
- Mã SRS chưa có test case nào: không có.
- Test case đã bỏ khỏi file: không có.
- Vấn đề khác: không có

## 2. Khi requirement đổi, làm gì
1. Sửa SRS hoặc ghi câu trả lời mới của BA vào bảng soát (như mọi lần).
2. Chạy `python -X utf8 scripts/truy-vet.py kiem banking-lite dang-nhap`. Script liệt kê mã đã đổi và các test case chuyển sang **Cần xem lại**.
3. Mở từng test case đó (bảng 6 dưới đây), sửa checklist và test case cho khớp.
4. Chạy `python -X utf8 scripts/truy-vet.py chot banking-lite dang-nhap -m "đã làm gì, vì sao"`. Script ghi một dòng lịch sử và chốt mốc mới.
5. Muốn xem từng chữ đã đổi, dùng lịch sử git (commit sau mỗi lần chốt).

## 3. Bảng tra mã
Mã trong cột Nguồn của checklist và test case bỏ tiền tố `LOGIN-`. `S01-AC02` là story 1, tình huống 2; `R` là quy tắc; `M` là thông báo; `TL` là câu trả lời của BA (TL-12, TL-13 là điều suy ra, người dùng xác nhận).

| Mã | Tên ngắn | Nguyên văn (rút gọn) | Mở ở đâu |
|---|---|---|---|
| M01 | Câu báo sai thông tin đăng nhập | `Mã không gian, mã nhân viên hoặc mật khẩu không đúng.` (thấy trên màn hình) | [dang-nhap.md dòng 103](../../../srs/banking-lite/dang-nhap.md#L103) |
| M02 | Câu chung dữ liệu không hợp lệ | `Một số giá trị không hợp lệ.` | [dang-nhap.md dòng 104](../../../srs/banking-lite/dang-nhap.md#L104) |
| M03 | Dòng mã lỗi khi mật khẩu trống | `validation.too_small (password)` | [dang-nhap.md dòng 105](../../../srs/banking-lite/dang-nhap.md#L105) |
| M04 | Dòng mã lỗi khi mã quá dài | `validation.too_big (employeeId)` | [dang-nhap.md dòng 106](../../../srs/banking-lite/dang-nhap.md#L106) |
| M05 | Câu báo bị chặn | `Đăng nhập sai quá nhiều lần. Thử lại sau {minutes} phút.` (**chỉ** thấy trong tệp giao diện) | [dang-nhap.md dòng 107](../../../srs/banking-lite/dang-nhap.md#L107) |
| M06 | Câu Vui lòng đăng nhập | `Vui lòng đăng nhập.` (có trong tệp giao diện, **chưa từng thấy hiện**) | [dang-nhap.md dòng 108](../../../srs/banking-lite/dang-nhap.md#L108) |
| M07 | Nhãn, nút, gợi ý, chân trang | `Đăng nhập` · `Mã nhân viên *` · `Mật khẩu *` · `Chữ P và 6 chữ số, ví dụ P100001.` · `Banking Lite · Phiên bản 1.3.0` · `Đăng xuất` | [dang-nhap.md dòng 109](../../../srs/banking-lite/dang-nhap.md#L109) |
| R01 | Mã nhân viên: định dạng | Dòng gợi ý: `Chữ P và 6 chữ số, ví dụ P100001.` Máy chủ **không** báo lỗi định dạng riêng (mọi mã sai định dạng chỉ nhận `LOGIN-M01`). | [dang-nhap.md dòng 91](../../../srs/banking-lite/dang-nhap.md#L91) |
| R02 | Mã nhân viên: hoa/thường | `p100001` đăng nhập được như `P100001` (mới thử với một tài khoản). | [dang-nhap.md dòng 92](../../../srs/banking-lite/dang-nhap.md#L92) |
| R03 | Mã nhân viên: độ dài tối đa | Có độ dài tối đa (mã 210 ký tự bị từ chối `too_big`); giá trị tối đa **chưa biết**. | [dang-nhap.md dòng 93](../../../srs/banking-lite/dang-nhap.md#L93) |
| R04 | Hai ô bắt buộc | Cả hai ô đánh dấu `*`, thẻ form có `novalidate` (trình duyệt không chặn). Mật khẩu trống → 400 `too_small (password)`. Mã trống + mật khẩu có giá trị… | [dang-nhap.md dòng 94](../../../srs/banking-lite/dang-nhap.md#L94) |
| R05 | Hiển thị sau đăng nhập | `/api/me` trả `employeeId`, `role` (ví dụ `BANKER`), `workspace` (`DEFAULT`), danh sách quyền; thanh trên hiện `<mã> · <vai trò> · DEFAULT` (`DEFAULT… | [dang-nhap.md dòng 95](../../../srs/banking-lite/dang-nhap.md#L95) |
| R06 | Giới hạn đăng nhập sai | Sau 10 lần thất bại liên tiếp (kể từ lần đăng nhập đúng gần nhất) → 429, `thử lại sau 5 phút` (`{minutes}` = 5). Áp dụng cả với mã không tồn tại. Đăn… | [dang-nhap.md dòng 96](../../../srs/banking-lite/dang-nhap.md#L96) |
| R07 | Ngôn ngữ | Lưu ở trình duyệt, khóa `bl.locale` ∈ {`vi`, `en`}; `<html lang>` đổi theo. | [dang-nhap.md dòng 97](../../../srs/banking-lite/dang-nhap.md#L97) |
| R08 | Thuộc tính ô nhập | Mã nhân viên: `name=employeeId`, `autocomplete=username`. Mật khẩu: `type=password`, `autocomplete=current-password`. Không có `maxlength`/`pattern`… | [dang-nhap.md dòng 98](../../../srs/banking-lite/dang-nhap.md#L98) |
| S01-AC01 | Mở hệ thống khi chưa đăng nhập | Hiện form **Đăng nhập** gồm: ô `Mã nhân viên *` (gợi ý bên dưới: `Chữ P và 6 chữ số, ví dụ P100001.`), ô `Mật khẩu *` (chữ gõ hiện dạng chấm), nút `Đ… | [dang-nhap.md dòng 42](../../../srs/banking-lite/dang-nhap.md#L42) |
| S01-AC02 | Đăng nhập đúng | Vào trang **Danh sách việc** của tài khoản đó. Thanh trên cùng hiện mã, vai trò và `DEFAULT`, ví dụ `P100001 · Chuyên viên khách hàng · DEFAULT`. **K… | [dang-nhap.md dòng 43](../../../srs/banking-lite/dang-nhap.md#L43) |
| S01-AC03 | Đăng nhập khi đã mở link hồ sơ | Mở **thẳng hồ sơ đó**, không về Danh sách việc | [dang-nhap.md dòng 44](../../../srs/banking-lite/dang-nhap.md#L44) |
| S01-AC04 | Gõ mã nhân viên bằng chữ thường | Đăng nhập thành công; thanh trên hiện `P100001` (chữ P hoa). Vậy mã nhân viên **không phân biệt hoa/thường** (mới thử với một tài khoản) | [dang-nhap.md dòng 45](../../../srs/banking-lite/dang-nhap.md#L45) |
| S01-AC05 | Nhấn Enter thay vì bấm nút | Form được gửi đi giống như bấm nút `Đăng nhập` | [dang-nhap.md dòng 46](../../../srs/banking-lite/dang-nhap.md#L46) |
| S01-AC06 | Tải lại trang khi đã đăng nhập | Vẫn đang đăng nhập, không phải nhập lại | [dang-nhap.md dòng 47](../../../srs/banking-lite/dang-nhap.md#L47) |
| S01-AC07 | Mở /login khi đã đăng nhập | Hiện **Danh sách việc** (không hiện form đăng nhập); thanh địa chỉ vẫn là `/login` | [dang-nhap.md dòng 48](../../../srs/banking-lite/dang-nhap.md#L48) |
| S01-AC08 | Mở địa chỉ không có thật khi đã đăng nhập | Hiện **Danh sách việc**; thanh địa chỉ giữ nguyên; **không** có trang "không tìm thấy" | [dang-nhap.md dòng 49](../../../srs/banking-lite/dang-nhap.md#L49) |
| S02-AC01 | Sai mật khẩu | Không đăng nhập. Khung lỗi đỏ: `Mã không gian, mã nhân viên hoặc mật khẩu không đúng.` (thông báo `LOGIN-M01`) | [dang-nhap.md dòng 58](../../../srs/banking-lite/dang-nhap.md#L58) |
| S02-AC02 | Mã nhân viên không tồn tại | **Cùng khung lỗi y hệt AC01**: hệ thống không cho biết là mã sai hay mật khẩu sai | [dang-nhap.md dòng 59](../../../srs/banking-lite/dang-nhap.md#L59) |
| S02-AC03 | Bỏ trống Mã nhân viên | Cùng khung lỗi `LOGIN-M01` như AC01. **Không** có câu "bắt buộc nhập mã" dù ô có dấu `*` | [dang-nhap.md dòng 60](../../../srs/banking-lite/dang-nhap.md#L60) |
| S02-AC04 | Mã nhân viên sai dạng | **Mỗi kiểu đều nhận cùng khung lỗi `LOGIN-M01`**; không có thông báo riêng nói "mã sai định dạng" | [dang-nhap.md dòng 61](../../../srs/banking-lite/dang-nhap.md#L61) |
| S02-AC05 | Bỏ trống Mật khẩu | Không đăng nhập. Khung lỗi đỏ có **2 dòng**: `Một số giá trị không hợp lệ.` (`LOGIN-M02`) và `validation.too_small (password)` (`LOGIN-M03` — mã kỹ t… | [dang-nhap.md dòng 62](../../../srs/banking-lite/dang-nhap.md#L62) |
| S02-AC06 | Mã nhân viên quá dài | Không đăng nhập. Khung lỗi đỏ 2 dòng: `Một số giá trị không hợp lệ.` (`LOGIN-M02`) và `validation.too_big (employeeId)` (`LOGIN-M04`). Giới hạn tối đ… | [dang-nhap.md dòng 63](../../../srs/banking-lite/dang-nhap.md#L63) |
| S02-AC07 | Sai liên tiếp thì bị chặn tạm | Bị chặn. Bản English hiện `Too many failed attempts. Try again in 5 minutes.` (`LOGIN-M05`). Bản tiếng Việt chưa thấy hiện trên màn hình. Ngưỡng chín… | [dang-nhap.md dòng 64](../../../srs/banking-lite/dang-nhap.md#L64) |
| S02-AC08 | Đang bị chặn mà nhập đúng | **Vẫn đăng nhập thành công** (việc chặn không ngăn đăng nhập đúng) | [dang-nhap.md dòng 65](../../../srs/banking-lite/dang-nhap.md#L65) |
| S03-AC01 | Đổi ngôn ngữ ở màn hình đăng nhập | Mọi nhãn đổi **ngay** sang ngôn ngữ đã chọn; chữ đã gõ ở ô mã vẫn còn; khung lỗi vẫn hiện, câu chung được dịch (`Some values are not valid.` ⇄ `Một s… | [dang-nhap.md dòng 72](../../../srs/banking-lite/dang-nhap.md#L72) |
| S03-AC02 | Mã lỗi kỹ thuật không được dịch | Dòng mã lỗi đó **giữ nguyên chữ tiếng Anh** ở cả hai ngôn ngữ | [dang-nhap.md dòng 73](../../../srs/banking-lite/dang-nhap.md#L73) |
| S03-AC03 | Nhớ ngôn ngữ đã chọn | Vẫn đúng ngôn ngữ đã chọn (trình duyệt lưu lại, khóa `bl.locale`, giá trị `vi` hoặc `en`) | [dang-nhap.md dòng 74](../../../srs/banking-lite/dang-nhap.md#L74) |
| S03-AC04 | Tên vai trò và số đổi theo ngôn ngữ | Vai trò đổi từ `Chuyên viên khách hàng` thành `Banker`; số tiền hiện kiểu English (ví dụ `2,000,000,000`) | [dang-nhap.md dòng 75](../../../srs/banking-lite/dang-nhap.md#L75) |
| S04-AC01 | Đăng xuất | Về form đăng nhập, thanh địa chỉ là `/`; ngôn ngữ giữ nguyên | [dang-nhap.md dòng 82](../../../srs/banking-lite/dang-nhap.md#L82) |
| S04-AC02 | Mở trang khi chưa đăng nhập | Hiện **form đăng nhập**, thanh địa chỉ giữ nguyên. **Không** có thông báo "cần đăng nhập" và **không** có trang "không tìm thấy" | [dang-nhap.md dòng 83](../../../srs/banking-lite/dang-nhap.md#L83) |
| S04-AC03 | Back sau khi đăng xuất | Địa chỉ quay về link hồ sơ nhưng chỉ hiện **form đăng nhập**; dữ liệu hồ sơ **không** hiện ra | [dang-nhap.md dòng 84](../../../srs/banking-lite/dang-nhap.md#L84) |
| S04-AC04 | Đăng xuất ở tab này, tab kia còn mở | Tab 1 **không tự thay đổi** cho đến khi bạn thao tác; khi thao tác, tab 1 chuyển sang **form đăng nhập** (không có thông báo nào) | [dang-nhap.md dòng 85](../../../srs/banking-lite/dang-nhap.md#L85) |
| TL-01 | BA: đang bị chặn thì không vào được, 5 phút | Đang bị chặn thì không được vào, kể cả nhập đúng. Sau 5 phút mới được vào, tính từ lúc bị chặn. | [bang-soat-requirement.md dòng 50](bang-soat-requirement.md#L50) |
| TL-02 | BA: 10 lần sai liên tiếp là chặn, mọi loại lỗi | 10 lần liên tiếp là chặn, không phân biệt lỗi gì hết. Được tính từ lần nhập sai đầu tiên. | [bang-soat-requirement.md dòng 51](bang-soat-requirement.md#L51) |
| TL-03 | BA: mọi ca sai, trống, quá dài báo một câu chung | Màn hình phải báo "mã nhân viên hoặc mật khẩu không đúng". Không báo những câu kia (người dùng nói về ô trống và mã quá dài; mình hiểu "những câu kia… | [bang-soat-requirement.md dòng 52](bang-soat-requirement.md#L52) |
| TL-04 | BA: tự cắt khoảng trắng, p hoa thường đều được | Khoảng trắng đầu/cuối: tự cắt bỏ (người dùng xác nhận lại ngày 2026-11-18). Chữ p thì hoa thường đều được. Độ dài không quy định vì đã chặn là phần đ… | [bang-soat-requirement.md dòng 53](bang-soat-requirement.md#L53) |
| TL-05 | BA: bỏ mã không gian | Mã không gian là bị bỏ, không còn được sử dụng. | [bang-soat-requirement.md dòng 54](bang-soat-requirement.md#L54) |
| TL-06 | BA: đăng nhập đúng đưa số lần sai về 0 | Đăng nhập đúng xen giữa đưa số lần sai về 0. Chỉ tính số lần, không tính thời gian. | [bang-soat-requirement.md dòng 55](bang-soat-requirement.md#L55) |
| TL-07 | BA: bỏ DEFAULT trên thanh trên | B12: bỏ (chữ `DEFAULT` trên thanh trên và trường `workspace` trong `/api/me` bỏ theo mã không gian; mình hiểu "bỏ" áp dụng cho cả hai chỗ mà câu hỏi… | [bang-soat-requirement.md dòng 56](bang-soat-requirement.md#L56) |
| TL-08 | BA: nguyên văn câu báo tiếng Việt và English | Tiếng Việt: "Mã nhân viên hoặc mật khẩu không đúng." English: "Employee ID or password is incorrect." | [bang-soat-requirement.md dòng 57](bang-soat-requirement.md#L57) |
| TL-09 | BA: hết 5 phút hết chặn, nhập thêm lúc bị chặn không tính | B3: Hết 5 phút là hết chặn, lúc bị chặn nhập thêm không tính. Sau khi hết 5 phút nhập sai thì mới được tính số lần lại. | [bang-soat-requirement.md dòng 58](bang-soat-requirement.md#L58) |
| TL-10 | BA: mã không tồn tại dùng chung một câu | B1: Câu "mã nhân viên hoặc mật khẩu không đúng" nói chung cả mã lẫn mật khẩu, nên hai trường hợp dùng chung một câu. | [bang-soat-requirement.md dòng 59](bang-soat-requirement.md#L59) |
| TL-11 | BA: lần sai thứ 10 báo bị chặn | A6 (phần cuối): Lần sai thứ 10 thì báo bị chặn. | [bang-soat-requirement.md dòng 60](bang-soat-requirement.md#L60) |
| TL-12 | Suy ra: chặn theo từng tài khoản | A7 (gộp B2): Bị chặn thì chặn đúng tài khoản đã nhập sai, không chặn tài khoản khác. | [bang-soat-requirement.md dòng 61](bang-soat-requirement.md#L61) |
| TL-13 | Suy ra: mật khẩu không cắt khoảng trắng, phân biệt hoa thường | A8: Mật khẩu không có khoảng trắng và phân biệt chữ hoa, chữ thường. Mình hiểu: không cắt khoảng trắng như ô mã; gõ thừa khoảng trắng hoặc sai hoa th… | [bang-soat-requirement.md dòng 62](bang-soat-requirement.md#L62) |

## 4. Yêu cầu theo BA của từng mã SRS
Gom từ bảng soát (mục 5, 6) để mỗi mã SRS có chỗ ghi điều BA trả lời, kể cả khi SRS (bản quan sát hệ thống 1.3.0) ghi khác. Test case viết theo cột "Theo BA"; chỗ có ⚠️ là nghi lỗi của hệ thống, chưa phải lỗi đã xác nhận. SRS không bị sửa.

| Mã | Tên ngắn | Theo BA (hoặc suy ra) | Hệ thống 1.3.0 hiện tại | Còn mở |
|---|---|---|---|---|
| M01 | Câu báo sai thông tin đăng nhập | Câu báo sai thông tin là "Mã nhân viên hoặc mật khẩu không đúng." (Tiếng Việt) và "Employee ID or password is incorrect." (English) (TL-08). Hệ thống hiện còn cụm "Mã không gian" ("Workspace" ở bản English). (TL-03, TL-05, TL-08) | ⚠️ Khác. Tiếng Việt thấy trên màn hình: "Mã không gian, mã nhân viên hoặc mật khẩu không đúng.". | — |
| M02 | Câu chung dữ liệu không hợp lệ | Câu "Một số giá trị không hợp lệ." / "Some values are not valid." không còn hiện ở màn hình đăng nhập (TL-03); thay bằng "Mã nhân viên hoặc mật khẩu không đúng." / "Employee ID or password is incorrect." (TL-08). (TL-03, TL-08) | ⚠️ Khác. Câu chung: "Một số giá trị không hợp lệ." / "Some values are not valid.". | — |
| M03 | Dòng mã lỗi khi mật khẩu trống | Dòng `validation.too_small (password)` không còn hiện (TL-03); thay bằng câu chung "mã nhân viên hoặc mật khẩu không đúng". (TL-03) | ⚠️ Khác. Xem dòng theo BA ở cột bên cạnh | — |
| M04 | Dòng mã lỗi khi mã quá dài | Dòng `validation.too_big (employeeId)` không còn hiện (TL-03); thay bằng câu chung "mã nhân viên hoặc mật khẩu không đúng". (TL-03)<br>Không còn dòng `too_big` nên không cần câu English của nó, và mục C6 không cần làm nữa. (TL-03) | ⚠️ Khác. Xem dòng theo BA ở cột bên cạnh | — |
| M05 | Câu báo bị chặn | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | B4 |
| M06 | Câu Vui lòng đăng nhập | Suy ra: Câu "Vui lòng đăng nhập." có trong tệp giao diện nhưng chưa từng hiện. Hành vi trên màn hình đã rõ (về form đăng nhập để đăng nhập lại, S04-AC04, S04-AC02), nên câu chỉ có trong tệp giao diện không làm hành vi thành chưa rõ. (suy ra từ SRS) | Không có điểm khác đã biết | — |
| M07 | Nhãn, nút, gợi ý, chân trang | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| R01 | Mã nhân viên: định dạng | Máy chủ không báo lỗi định dạng riêng: mã sai dạng chỉ nhận câu chung (TL-03, TL-04). Khớp hệ thống hiện tại. Dòng gợi ý vẫn đúng là định dạng chuẩn nên giữ nguyên (suy ra, không cần hỏi: gõ chữ p thường được chấp nhận không làm gợi ý sai). (TL-04) | Không có điểm khác đã biết | — |
| R02 | Mã nhân viên: hoa/thường | Chữ thường hay hoa đều được; khoảng trắng đầu và cuối tự cắt bỏ (TL-04). Thanh trên hiện chữ hoa: suy ra từ dòng gợi ý (định dạng chuẩn là chữ P hoa) và S01-AC04. (TL-04) | Không có điểm khác đã biết | — |
| R03 | Mã nhân viên: độ dài tối đa | Độ dài mã nhân viên không quy định ở màn hình đăng nhập (TL-04: giới hạn thuộc phần đăng ký). Hệ thống hiện có mức tối đa (mã 210 ký tự bị từ chối bằng `too_big`). (TL-04) | ⚠️ Khác. Xem dòng theo BA ở cột bên cạnh | — |
| R04 | Hai ô bắt buộc | Để trống ô nào cũng chỉ báo câu chung "mã nhân viên hoặc mật khẩu không đúng", không có câu "bắt buộc" riêng cho ô nào (TL-03). Hệ thống hiện xử lý hai ô khác nhau: mật khẩu trống báo lỗi 400 kèm dòng mã, mã trống kèm mật khẩu báo 401. (TL-03) | ⚠️ Khác. Xem dòng theo BA ở cột bên cạnh | — |
| R05 | Hiển thị sau đăng nhập | Workspace (mã không gian) bị bỏ (TL-05): thanh trên không còn `DEFAULT` và `/api/me` không còn trả `workspace` (TL-07). Hệ thống hiện vẫn hiện và vẫn trả. (TL-05, TL-07) | ⚠️ Khác. Thanh trên hiện mã, vai trò và `DEFAULT`. `/api/me` trả mã, vai trò, workspace, danh sách quyền. | — |
| R06 | Giới hạn đăng nhập sai | 10 lần đăng nhập sai liên tiếp thì bị chặn; mọi loại lỗi đều tính, kể cả ô trống và mã quá dài (TL-02). Khớp số lần và loại lỗi hệ thống đang đếm (10 lần, có tính lỗi 400), nhưng hệ thống chặn ở lần thứ 11, lệch một lần (TL-11). (TL-02)<br>Đăng nhập đúng xen giữa thì đưa số lần sai về 0. Chỉ tính số lần, không tính thời gian (TL-06). Khớp câu "kể từ lần đăng nhập đúng gần nhất" trong SRS. (TL-06)<br>Lần sai thứ 10 thì báo bị chặn (TL-11): từ lần sai thứ 10 đã hiện câu bị chặn. Hệ thống hiện báo sai thông tin ở 10 lần đầu, lần thứ 11 mới báo bị chặn, lệch một lần. BA đã trả lời nên đây là nghi lỗi. (TL-11)<br>Đang bị chặn, nhập đúng mã và mật khẩu: vẫn không vào được. Chỉ vào được sau 5 phút kể từ lúc bị chặn (TL-01). Hệ thống hiện cho vào. BA đã trả lời nên đây là nghi lỗi, chưa phải lỗi đã xác nhận trên hệ thống. (TL-01)<br>Suy ra: Chặn theo từng tài khoản: chỉ tài khoản đã nhập sai bị chặn (TL-12, người dùng chốt). Hệ thống hiện có thể khác (nhiều mã khác nhau cộng lại vẫn bị chặn), cần kiểm. Chưa nói mã không có thật thì đếm thế nào. (TL-12)<br>Hết chặn sau 5 phút kể từ lúc bị chặn (TL-01, TL-09). (TL-01, TL-09)<br>Lúc đang bị chặn, nhập thêm không tính và không kéo dài thời gian chặn. Hết 5 phút thì hết chặn; sau đó nhập sai mới được tính số lần lại từ đầu (TL-09). Hệ thống: chưa kiểm, vì mỗi lần sai đều tính vào 10 lần. (TL-09) | ⚠️ Khác. Xem dòng theo BA ở cột bên cạnh | — |
| R07 | Ngôn ngữ | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| R08 | Thuộc tính ô nhập | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S01-AC01 | Mở hệ thống khi chưa đăng nhập | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S01-AC02 | Đăng nhập đúng | Thanh trên không còn chữ `DEFAULT` sau mã và vai trò (TL-05: mã không gian bị bỏ; TL-07: bỏ cả `DEFAULT`). Hệ thống hiện vẫn hiện `DEFAULT`. (TL-05, TL-07) | ⚠️ Khác. Xem dòng theo BA ở cột bên cạnh | — |
| S01-AC03 | Đăng nhập khi đã mở link hồ sơ | Suy ra: Áp dụng cho mọi link: chưa đăng nhập thì mọi địa chỉ đều hiện form và giữ nguyên địa chỉ (S04-AC02), đăng nhập đúng thì mở đúng địa chỉ đó. Hồ sơ mà vai trò không được xem thì hiện gì là việc của phần quyền xem hồ sơ, không thuộc Đăng nhập. (suy ra từ SRS) | Không có điểm khác đã biết | — |
| S01-AC04 | Gõ mã nhân viên bằng chữ thường | Chữ p thường hay hoa đều đăng nhập được (TL-04), áp dụng cho mọi tài khoản. Hệ thống: đã thấy với P100001, chưa thử với P200001 và P300001. Mục C3 chỉ còn là kiểm hệ thống có làm đúng. (TL-04) | Không có điểm khác đã biết | — |
| S01-AC05 | Nhấn Enter thay vì bấm nút | Suy ra: Enter ở ô Mật khẩu, hay khi thông tin đúng, cũng gửi form như bấm nút: Enter ở ô nhập là cách gửi form, không phụ thuộc ô nào. Hệ thống: chưa thử, mục C2 chỉ còn là kiểm hệ thống. (suy ra từ SRS) | Không có điểm khác đã biết | — |
| S01-AC06 | Tải lại trang khi đã đăng nhập | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | B8 |
| S01-AC07 | Mở /login khi đã đăng nhập | Suy ra: SRS ghi rõ hành vi này, không có chỗ nào nói khác: đã đăng nhập thì mọi địa chỉ đều về Danh sách việc, kể cả `/login`. Không hỏi. (suy ra từ SRS) | Không có điểm khác đã biết | — |
| S01-AC08 | Mở địa chỉ không có thật khi đã đăng nhập | Suy ra: SRS ghi rõ: địa chỉ không có thật cũng hiện Danh sách việc, không có trang "không tìm thấy". Không có chỗ nào nói khác. Không hỏi. (suy ra từ SRS) | Không có điểm khác đã biết | — |
| S02-AC01 | Sai mật khẩu | Kết quả đúng: không đăng nhập; khung lỗi ghi "Mã nhân viên hoặc mật khẩu không đúng." (English: "Employee ID or password is incorrect."), không có cụm "Mã không gian" (TL-03, TL-05, TL-08). Hệ thống hiện vẫn có cụm "Mã không gian". (TL-03, TL-05, TL-08) | ⚠️ Khác. Không đăng nhập. Khung lỗi đỏ ghi câu "Mã không gian, mã nhân viên hoặc mật khẩu không đúng." (chữ "mã không gian": xem dòng LOGIN-M01). | — |
| S02-AC02 | Mã nhân viên không tồn tại | Mã không có thật và sai mật khẩu dùng chung một câu "mã nhân viên hoặc mật khẩu không đúng", vì câu này nói chung cả mã lẫn mật khẩu (TL-10). Khớp hệ thống hiện tại về việc dùng chung một câu. (TL-10) | Không có điểm khác đã biết | — |
| S02-AC03 | Bỏ trống Mã nhân viên | Ô Mã nhân viên trống, có mật khẩu: báo "mã nhân viên hoặc mật khẩu không đúng", không có câu "bắt buộc nhập mã" riêng (TL-03). Hệ thống hiện báo câu còn cụm "Mã không gian" (xem dòng AC01). (TL-03) | ⚠️ Khác. Xem dòng theo BA ở cột bên cạnh | — |
| S02-AC04 | Mã nhân viên sai dạng | Mã sai dạng (thiếu hoặc thừa số, chữ khác, ký tự lạ) không được kiểm riêng, chỉ báo câu chung (TL-03, TL-04). Chữ p thường vẫn hợp lệ (hoa thường đều được), nên `p999999` chỉ là mã không có thật, không phải "sai dạng". Hệ thống hiện khớp. (TL-04)<br>Mã thật có khoảng trắng đầu hoặc cuối: tự cắt bỏ, đăng nhập được (TL-04). Hệ thống: chưa thử với mã thật. Mục C1 chỉ còn là kiểm hệ thống có làm đúng. (TL-04) | Không có điểm khác đã biết | — |
| S02-AC05 | Bỏ trống Mật khẩu | Mật khẩu trống (kể cả khi ô mã trống, hoặc `abc123`, hoặc `P100001`): báo "mã nhân viên hoặc mật khẩu không đúng". Không hiện "Một số giá trị không hợp lệ." và không hiện dòng `validation.too_small (password)` (TL-03). Hệ thống hiện vẫn hiện hai dòng này. (TL-03) | ⚠️ Khác. Khung lỗi đỏ có hai dòng: "Một số giá trị không hợp lệ." và `validation.too_small (password)`. Đúng theo hành vi đã quan sát. | — |
| S02-AC06 | Mã nhân viên quá dài | Mã nhân viên rất dài: không có mức tối đa ở màn hình đăng nhập (TL-04: độ dài thuộc phần đăng ký), nên chỉ báo "mã nhân viên hoặc mật khẩu không đúng" như mọi lần nhập sai (TL-03), và vẫn tính vào 10 lần sai (TL-02). Hệ thống hiện từ chối mã 210 ký tự bằng `validation.too_big (employeeId)`. (TL-03, TL-04) | ⚠️ Khác. Khung lỗi đỏ hai dòng: "Một số giá trị không hợp lệ." và `validation.too_big (employeeId)`. Đúng theo hành vi đã quan sát. | — |
| S02-AC07 | Sai liên tiếp thì bị chặn tạm | 10 lần đăng nhập sai liên tiếp thì bị chặn; mọi loại lỗi đều tính, kể cả ô trống và mã quá dài (TL-02). Khớp số lần và loại lỗi hệ thống đang đếm (10 lần, có tính lỗi 400), nhưng hệ thống chặn ở lần thứ 11, lệch một lần (TL-11). (TL-02)<br>Đăng nhập đúng xen giữa thì đưa số lần sai về 0. Chỉ tính số lần, không tính thời gian (TL-06). Khớp câu "kể từ lần đăng nhập đúng gần nhất" trong SRS. (TL-06)<br>Lần sai thứ 10 thì báo bị chặn (TL-11): từ lần sai thứ 10 đã hiện câu bị chặn. Hệ thống hiện báo sai thông tin ở 10 lần đầu, lần thứ 11 mới báo bị chặn, lệch một lần. BA đã trả lời nên đây là nghi lỗi. (TL-11) | ⚠️ Khác. Xem dòng theo BA ở cột bên cạnh | — |
| S02-AC08 | Đang bị chặn mà nhập đúng | Đang bị chặn, nhập đúng mã và mật khẩu: vẫn không vào được. Chỉ vào được sau 5 phút kể từ lúc bị chặn (TL-01). Hệ thống hiện cho vào (đã thấy khi đang bị chặn khoảng 2 phút). BA đã trả lời nên đây là nghi lỗi, chưa phải lỗi đã xác nhận trên hệ thống. (TL-01)<br>Suy ra: Chỉ tài khoản đã nhập sai bị chặn; tài khoản khác vẫn đăng nhập được bình thường (TL-12, người dùng chốt). Hệ thống hiện có thể khác: lúc khám phá, nhiều mã khác nhau cộng lại vẫn bị chặn. Cần kiểm. (TL-12) | ⚠️ Khác. Vẫn đăng nhập thành công. Đúng theo hành vi đã quan sát. | B4 |
| S03-AC01 | Đổi ngôn ngữ ở màn hình đăng nhập | Khung lỗi không còn câu "Một số giá trị không hợp lệ." (TL-03). Câu được dịch qua lại là "Mã nhân viên hoặc mật khẩu không đúng." ⇄ "Employee ID or password is incorrect." (TL-08). Hệ thống hiện dịch qua lại "Một số giá trị không hợp lệ." ⇄ "Some values are not valid." khi để trống mật khẩu. (TL-03, TL-08) | ⚠️ Khác. Xem dòng theo BA ở cột bên cạnh | — |
| S03-AC02 | Mã lỗi kỹ thuật không được dịch | Không còn dòng mã kỹ thuật, nên không còn chuyện dịch hay không dịch dòng này. Chỉ còn câu chung "mã nhân viên hoặc mật khẩu không đúng" (TL-03). Bản English của câu này: "Employee ID or password is incorrect." (TL-08). (TL-03)<br>Không còn dòng `validation.too_big (employeeId)` nên không cần biết bản English của nó, và mục C6 không cần làm nữa. (TL-03) | ⚠️ Khác. Dòng mã lỗi giữ nguyên chữ tiếng Anh ở cả hai ngôn ngữ. Đã thấy với `too_small` (Ảnh 06). | — |
| S03-AC03 | Nhớ ngôn ngữ đã chọn | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S03-AC04 | Tên vai trò và số đổi theo ngôn ngữ | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | C4 |
| S04-AC01 | Đăng xuất | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S04-AC02 | Mở trang khi chưa đăng nhập | Suy ra: SRS ghi rõ: chưa đăng nhập thì mọi địa chỉ đều hiện form đăng nhập; đăng nhập xong mở đúng địa chỉ đó (S01-AC03), nên không cần báo "cần đăng nhập". Không hỏi. (suy ra từ SRS) | Không có điểm khác đã biết | — |
| S04-AC03 | Back sau khi đăng xuất | Chưa có câu trả lời riêng của BA; theo SRS | Không có điểm khác đã biết | — |
| S04-AC04 | Đăng xuất ở tab này, tab kia còn mở | Suy ra: Đã bị đăng xuất thì phải đăng nhập lại: tab 1 về form đăng nhập là đúng, SRS ghi rõ. Không cần hỏi có báo thêm câu nào không. (suy ra từ SRS) | Không có điểm khác đã biết | — |

## 5. Từ requirement tới test case
| Mã | Tên ngắn | Trạng thái requirement | Test case |
|---|---|---|---|
| M01 | Câu báo sai thông tin đăng nhập | Không đổi | 2: TC-006, TC-036 |
| M02 | Câu chung dữ liệu không hợp lệ | Không đổi | 2: TC-009, TC-035 |
| M03 | Dòng mã lỗi khi mật khẩu trống | Không đổi | 1: TC-009 |
| M04 | Dòng mã lỗi khi mã quá dài | Không đổi | 1: TC-040 |
| M05 | Câu báo bị chặn | Không đổi | 2: TC-015, TC-037 |
| M06 | Câu Vui lòng đăng nhập | Không đổi | 2: TC-025, TC-026 |
| M07 | Nhãn, nút, gợi ý, chân trang | Không đổi | 1: TC-005 |
| R01 | Mã nhân viên: định dạng | Không đổi | 2: TC-005, TC-030 |
| R02 | Mã nhân viên: hoa/thường | Không đổi | 1: TC-027 |
| R03 | Mã nhân viên: độ dài tối đa | Không đổi | 1: TC-040 |
| R04 | Hai ô bắt buộc | Không đổi | 2: TC-008, TC-009 |
| R05 | Hiển thị sau đăng nhập | Không đổi | 1: TC-001 |
| R06 | Giới hạn đăng nhập sai | Không đổi | 4: TC-014, TC-018, TC-021, TC-022 |
| R07 | Ngôn ngữ | Không đổi | 1: TC-038 |
| R08 | Thuộc tính ô nhập | Không đổi | 2: TC-005, TC-012 |
| S01-AC01 | Mở hệ thống khi chưa đăng nhập | Không đổi | 1: TC-005 |
| S01-AC02 | Đăng nhập đúng | Không đổi | 2: TC-001, TC-002 |
| S01-AC03 | Đăng nhập khi đã mở link hồ sơ | Không đổi | 1: TC-003 |
| S01-AC04 | Gõ mã nhân viên bằng chữ thường | Không đổi | 1: TC-027 |
| S01-AC05 | Nhấn Enter thay vì bấm nút | Không đổi | 1: TC-031 |
| S01-AC06 | Tải lại trang khi đã đăng nhập | Không đổi | 1: TC-032 |
| S01-AC07 | Mở /login khi đã đăng nhập | Không đổi | 1: TC-033 |
| S01-AC08 | Mở địa chỉ không có thật khi đã đăng nhập | Không đổi | 1: TC-034 |
| S02-AC01 | Sai mật khẩu | Không đổi | 1: TC-006 |
| S02-AC02 | Mã nhân viên không tồn tại | Không đổi | 1: TC-007 |
| S02-AC03 | Bỏ trống Mã nhân viên | Không đổi | 1: TC-008 |
| S02-AC04 | Mã nhân viên sai dạng | Không đổi | 3: TC-028, TC-029, TC-030 |
| S02-AC05 | Bỏ trống Mật khẩu | Không đổi | 1: TC-009 |
| S02-AC06 | Mã nhân viên quá dài | Không đổi | 1: TC-040 |
| S02-AC07 | Sai liên tiếp thì bị chặn tạm | Không đổi | 3: TC-014, TC-015, TC-037 |
| S02-AC08 | Đang bị chặn mà nhập đúng | Không đổi | 1: TC-017 |
| S03-AC01 | Đổi ngôn ngữ ở màn hình đăng nhập | Không đổi | 1: TC-035 |
| S03-AC02 | Mã lỗi kỹ thuật không được dịch | Không đổi | 1: TC-035 |
| S03-AC03 | Nhớ ngôn ngữ đã chọn | Không đổi | 1: TC-038 |
| S03-AC04 | Tên vai trò và số đổi theo ngôn ngữ | Không đổi | 1: TC-039 |
| S04-AC01 | Đăng xuất | Không đổi | 1: TC-023 |
| S04-AC02 | Mở trang khi chưa đăng nhập | Không đổi | 2: TC-003, TC-026 |
| S04-AC03 | Back sau khi đăng xuất | Không đổi | 1: TC-024 |
| S04-AC04 | Đăng xuất ở tab này, tab kia còn mở | Không đổi | 1: TC-025 |
| TL-01 | BA: đang bị chặn thì không vào được, 5 phút | Không đổi | 4: TC-016, TC-017, TC-018, TC-019 |
| TL-02 | BA: 10 lần sai liên tiếp là chặn, mọi loại lỗi | Không đổi | 2: TC-014, TC-015 |
| TL-03 | BA: mọi ca sai, trống, quá dài báo một câu chung | Không đổi | 7: TC-006, TC-008, TC-009, TC-010, TC-011, TC-035, TC-040 |
| TL-04 | BA: tự cắt khoảng trắng, p hoa thường đều được | Không đổi | 7: TC-005, TC-027, TC-028, TC-029, TC-030, TC-040, TC-041 |
| TL-05 | BA: bỏ mã không gian | Không đổi | 2: TC-001, TC-041 |
| TL-06 | BA: đăng nhập đúng đưa số lần sai về 0 | Không đổi | 2: TC-004, TC-021 |
| TL-07 | BA: bỏ DEFAULT trên thanh trên | Không đổi | 1: TC-001 |
| TL-08 | BA: nguyên văn câu báo tiếng Việt và English | Không đổi | 5: TC-006, TC-007, TC-008, TC-035, TC-036 |
| TL-09 | BA: hết 5 phút hết chặn, nhập thêm lúc bị chặn không tính | Không đổi | 4: TC-016, TC-018, TC-019, TC-020 |
| TL-10 | BA: mã không tồn tại dùng chung một câu | Không đổi | 1: TC-007 |
| TL-11 | BA: lần sai thứ 10 báo bị chặn | Không đổi | 2: TC-014, TC-015 |
| TL-12 | Suy ra: chặn theo từng tài khoản | Không đổi | 1: TC-022 |
| TL-13 | Suy ra: mật khẩu không cắt khoảng trắng, phân biệt hoa thường | Không đổi | 2: TC-012, TC-013 |

## 6. Từ test case tới requirement
| Mã | Tình huống | Ưu tiên | Mã requirement dùng | Trạng thái | Tạo | Sửa lần cuối |
|---|---|---|---|---|---|---|
| TC-001 | Đăng nhập đúng `P100001` + mật khẩu đúng: vào Danh sách việc của tài khoản đó, không có t… | Cao | R05 (Hiển thị sau đăng nhập), S01-AC02 (Đăng nhập đúng), TL-05 (BA: bỏ mã không gian), TL-07 (BA: bỏ DEFAULT trên thanh trên) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-002 | Đăng nhập đúng bằng tài khoản vai trò khác (`P200001` Chuyên viên định giá, `P300001` Chu… | Cao | S01-AC02 (Đăng nhập đúng) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-003 | Chưa đăng nhập mà mở link một hồ sơ (ví dụ HL-000019 của chính người đó): hiện form đăng… | Cao | S01-AC03 (Đăng nhập khi đã mở link hồ sơ), S04-AC02 (Mở trang khi chưa đăng nhập) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-004 | Nhập sai một lần (thấy khung lỗi), rồi sửa lại cho đúng và đăng nhập: vào được Danh sách… | Cao | TL-06 (BA: đăng nhập đúng đưa số lần sai về 0) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-005 | Mở hệ thống khi chưa đăng nhập: form có ô Mã nhân viên (kèm gợi ý "Chữ P và 6 chữ số, ví… | Cao | M07 (Nhãn, nút, gợi ý, chân trang), R01 (Mã nhân viên: định dạng), R08 (Thuộc tính ô nhập), S01-AC01 (Mở hệ thống khi chưa đăng nhập), TL-04 (BA: tự cắt khoảng trắng, p hoa thường đều được) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-006 | Mã nhân viên có thật (`P100001`) + **sai mật khẩu**: không đăng nhập; khung lỗi đỏ ghi đú… | Cao | M01 (Câu báo sai thông tin đăng nhập), S02-AC01 (Sai mật khẩu), TL-03 (BA: mọi ca sai, trống, quá dài báo một câu chung), TL-08 (BA: nguyên văn câu báo tiếng Việt và English) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-007 | Mã nhân viên không tồn tại (`P999999`) + mật khẩu bất kỳ: ra **cùng một câu** như sai mật… | Cao | S02-AC02 (Mã nhân viên không tồn tại), TL-08 (BA: nguyên văn câu báo tiếng Việt và English), TL-10 (BA: mã không tồn tại dùng chung một câu) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-008 | Để trống ô Mã nhân viên, nhập một mật khẩu: ra câu chung "Mã nhân viên hoặc mật khẩu khôn… | Cao | R04 (Hai ô bắt buộc), S02-AC03 (Bỏ trống Mã nhân viên), TL-03 (BA: mọi ca sai, trống, quá dài báo một câu chung), TL-08 (BA: nguyên văn câu báo tiếng Việt và English) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-009 | Để trống ô Mật khẩu (mã nhân viên đúng hoặc sai): ra câu chung; **không** còn câu "Một số… | Cao | M02 (Câu chung dữ liệu không hợp lệ), M03 (Dòng mã lỗi khi mật khẩu trống), R04 (Hai ô bắt buộc), S02-AC05 (Bỏ trống Mật khẩu), TL-03 (BA: mọi ca sai, trống, quá dài báo một câu chung) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-010 | Để trống cả hai ô rồi bấm Đăng nhập: ra câu chung | Cao | TL-03 (BA: mọi ca sai, trống, quá dài báo một câu chung) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-011 | Nhập sai rồi nhìn lại form sau khi báo lỗi: ô Mật khẩu phải trống (mật khẩu đã gõ không đ… | Cao | TL-03 (BA: mọi ca sai, trống, quá dài báo một câu chung) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-012 | Mật khẩu đúng nhưng đổi một chữ hoa thành chữ thường: không đăng nhập, báo câu chung (mật… | Cao | R08 (Thuộc tính ô nhập), TL-13 (Suy ra: mật khẩu không cắt khoảng trắng, phân biệt hoa thường) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-013 | Mật khẩu đúng nhưng thừa khoảng trắng ở cuối: không đăng nhập, báo câu chung (khác ô mã,… | Cao | TL-13 (Suy ra: mật khẩu không cắt khoảng trắng, phân biệt hoa thường) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-014 | Sai liên tiếp **9 lần** (cùng một tài khoản): lần thứ 9 vẫn báo câu chung "không đúng", c… | Cao | R06 (Giới hạn đăng nhập sai), S02-AC07 (Sai liên tiếp thì bị chặn tạm), TL-02 (BA: 10 lần sai liên tiếp là chặn, mọi loại lỗi), TL-11 (BA: lần sai thứ 10 báo bị chặn) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-015 | Lần sai thứ **10**: báo bị chặn tạm, bản Tiếng Việt ghi "Đăng nhập sai quá nhiều lần. Thử… | Cao | M05 (Câu báo bị chặn), S02-AC07 (Sai liên tiếp thì bị chặn tạm), TL-02 (BA: 10 lần sai liên tiếp là chặn, mọi loại lỗi), TL-11 (BA: lần sai thứ 10 báo bị chặn) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-016 | Đang bị chặn, nhập sai thêm lần thứ **11**: vẫn bị chặn, không tính thêm lần, thời gian c… | Cao | TL-01 (BA: đang bị chặn thì không vào được, 5 phút), TL-09 (BA: hết 5 phút hết chặn, nhập thêm lúc bị chặn không tính) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-017 | Đang bị chặn (chưa đủ 5 phút), nhập **đúng** mã và mật khẩu: không vào được | Cao | S02-AC08 (Đang bị chặn mà nhập đúng), TL-01 (BA: đang bị chặn thì không vào được, 5 phút) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-018 | Ngay **trước** mốc 5 phút kể từ lúc bị chặn, nhập đúng: vẫn không vào được | Cao | R06 (Giới hạn đăng nhập sai), TL-01 (BA: đang bị chặn thì không vào được, 5 phút), TL-09 (BA: hết 5 phút hết chặn, nhập thêm lúc bị chặn không tính) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-019 | Ngay **sau** mốc 5 phút kể từ lúc bị chặn, nhập đúng: vào được Danh sách việc | Cao | TL-01 (BA: đang bị chặn thì không vào được, 5 phút), TL-09 (BA: hết 5 phút hết chặn, nhập thêm lúc bị chặn không tính) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-020 | Hết 5 phút, nhập **sai**: báo câu chung (không phải câu bị chặn) và số lần sai đếm lại từ… | Cao | TL-09 (BA: hết 5 phút hết chặn, nhập thêm lúc bị chặn không tính) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-021 | Sai 9 lần, đăng nhập đúng một lần, rồi sai tiếp: không bị chặn (số lần sai về 0 sau lần đ… | Cao | R06 (Giới hạn đăng nhập sai), TL-06 (BA: đăng nhập đúng đưa số lần sai về 0) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-022 | Sai 9 lần với `P100001`, rồi sai một lần với `P200001`: `P200001` chưa bị chặn; `P100001`… | Cao | R06 (Giới hạn đăng nhập sai), TL-12 (Suy ra: chặn theo từng tài khoản) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-023 | Đăng xuất khi đang đăng nhập: về form đăng nhập, địa chỉ là `/`, ngôn ngữ đã chọn giữ ngu… | Cao | S04-AC01 (Đăng xuất) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-024 | Đăng xuất khi đang ở trang một hồ sơ, rồi bấm Back của trình duyệt: chỉ hiện form đăng nh… | Cao | S04-AC03 (Back sau khi đăng xuất) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-025 | Hai tab cùng trình duyệt: đăng xuất ở tab 2, ở tab 1 thao tác cần tải dữ liệu (ví dụ bấm… | Cao | M06 (Câu Vui lòng đăng nhập), S04-AC04 (Đăng xuất ở tab này, tab kia còn mở) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-026 | Chưa đăng nhập, mở `/integrations` hoặc một địa chỉ không có thật: hiện form đăng nhập, đ… | Cao | M06 (Câu Vui lòng đăng nhập), S04-AC02 (Mở trang khi chưa đăng nhập) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-027 | Gõ mã bằng chữ thường `p100001` + mật khẩu đúng: đăng nhập được; thanh trên hiện `P100001` | Trung bình | R02 (Mã nhân viên: hoa/thường), S01-AC04 (Gõ mã nhân viên bằng chữ thường), TL-04 (BA: tự cắt khoảng trắng, p hoa thường đều được) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-028 | Mã có thật, thừa khoảng trắng ở **đầu** + mật khẩu đúng: đăng nhập được (tự cắt bỏ khoảng… | Trung bình | S02-AC04 (Mã nhân viên sai dạng), TL-04 (BA: tự cắt khoảng trắng, p hoa thường đều được) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-029 | Mã có thật, thừa khoảng trắng ở **cuối** + mật khẩu đúng: đăng nhập được (tự cắt bỏ khoản… | Trung bình | S02-AC04 (Mã nhân viên sai dạng), TL-04 (BA: tự cắt khoảng trắng, p hoa thường đều được) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-030 | Mã sai dạng, mỗi lần một kiểu (`X999999`, `P99999A`, `P99-999`): đều ra câu chung, không… | Trung bình | R01 (Mã nhân viên: định dạng), S02-AC04 (Mã nhân viên sai dạng), TL-04 (BA: tự cắt khoảng trắng, p hoa thường đều được) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-031 | Nhấn Enter thay vì bấm nút, khi đang ở ô Mã nhân viên và khi đang ở ô Mật khẩu: form được… | Trung bình | S01-AC05 (Nhấn Enter thay vì bấm nút) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-032 | Đã đăng nhập, tải lại trang (F5): vẫn đăng nhập, không phải nhập lại | Trung bình | S01-AC06 (Tải lại trang khi đã đăng nhập) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-033 | Đã đăng nhập, mở `/login`: hiện Danh sách việc (không hiện form), thanh địa chỉ vẫn là `/… | Trung bình | S01-AC07 (Mở /login khi đã đăng nhập) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-034 | Đã đăng nhập, mở địa chỉ không có thật (`/khong-ton-tai-xyz`): hiện Danh sách việc, không… | Trung bình | S01-AC08 (Mở địa chỉ không có thật khi đã đăng nhập) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-035 | Đang hiện khung lỗi và đã gõ mã, bấm đổi ngôn ngữ giữa chừng: nhãn đổi ngay, chữ ở ô mã c… | Trung bình | M02 (Câu chung dữ liệu không hợp lệ), S03-AC01 (Đổi ngôn ngữ ở màn hình đăng nhập), S03-AC02 (Mã lỗi kỹ thuật không được dịch), TL-03 (BA: mọi ca sai, trống, quá dài báo một câu chung), TL-08 (BA: nguyên văn câu báo tiếng Việt và English) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-036 | Bản English, sai mật khẩu: khung lỗi ghi "Employee ID or password is incorrect." | Trung bình | M01 (Câu báo sai thông tin đăng nhập), TL-08 (BA: nguyên văn câu báo tiếng Việt và English) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-037 | Bản English, bị chặn vì sai quá nhiều lần: ghi "Too many failed attempts. Try again in 5… | Trung bình | M05 (Câu báo bị chặn), S02-AC07 (Sai liên tiếp thì bị chặn tạm) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-038 | Chọn một ngôn ngữ rồi tải lại trang, và rồi bấm Đăng xuất: vẫn đúng ngôn ngữ đã chọn | Trung bình | R07 (Ngôn ngữ), S03-AC03 (Nhớ ngôn ngữ đã chọn) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-039 | Đã đăng nhập `P100001`, bấm English: vai trò đổi từ "Chuyên viên khách hàng" thành "Banke… | Trung bình | S03-AC04 (Tên vai trò và số đổi theo ngôn ngữ) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-040 | Nhập mã nhân viên rất dài (ví dụ 210 ký tự) + mật khẩu bất kỳ: ra câu chung, không còn dò… | Thấp | M04 (Dòng mã lỗi khi mã quá dài), R03 (Mã nhân viên: độ dài tối đa), S02-AC06 (Mã nhân viên quá dài), TL-03 (BA: mọi ca sai, trống, quá dài báo một câu chung), TL-04 (BA: tự cắt khoảng trắng, p hoa thường đều được) | Còn đúng | 2026-11-18 | 2026-11-18 |
| TC-041 | Nhìn form đăng nhập: không có ô chọn Workspace, không có quên mật khẩu, đăng ký, "ghi nhớ… | Thấp | TL-04 (BA: tự cắt khoảng trắng, p hoa thường đều được), TL-05 (BA: bỏ mã không gian) | Còn đúng | 2026-11-18 | 2026-11-18 |

## 7. Lịch sử thay đổi
Ghi mỗi lần chạy `chot`. Cột "Dựa trên" là phiên bản requirement lúc chốt.

| Ngày | Đối tượng | Nội dung | Dựa trên | Mã requirement đổi | Test case mới / sửa / bỏ |
|---|---|---|---|---|---|
| 2026-11-18 | checklist, test-case | Tạo lần đầu: checklist 41 dòng và test case chi tiết 41 case (TC-001 đến TC-041), dựa trên phần requirement đã chốt. Thêm tên ngắn vào cột Nguồn, bảng tra mã, ma trận truy vết hai chiều. | SRS 2026-11-17; bảng soát 2026-11-18; TL đến TL-13 | M01 (mới), M02 (mới), M03 (mới), M04 (mới), M05 (mới), M06 (mới), M07 (mới), R01 (mới), R02 (mới), R03 (mới), R04 (mới), R05 (mới), R06 (mới), R07 (mới), R08 (mới), S01-AC01 (mới), S01-AC02 (mới), S01-AC03 (mới), S01-AC04 (mới), S01-AC05 (mới), S01-AC06 (mới), S01-AC07 (mới), S01-AC08 (mới), S02-AC01 (mới), S02-AC02 (mới), S02-AC03 (mới), S02-AC04 (mới), S02-AC05 (mới), S02-AC06 (mới), S02-AC07 (mới), S02-AC08 (mới), S03-AC01 (mới), S03-AC02 (mới), S03-AC03 (mới), S03-AC04 (mới), S04-AC01 (mới), S04-AC02 (mới), S04-AC03 (mới), S04-AC04 (mới), TL-01 (mới), TL-02 (mới), TL-03 (mới), TL-04 (mới), TL-05 (mới), TL-06 (mới), TL-07 (mới), TL-08 (mới), TL-09 (mới), TL-10 (mới), TL-11 (mới), TL-12 (mới), TL-13 (mới) | mới 41; sửa 0; bỏ 0 |
| 2026-11-18 | checklist, test-case | Thêm phần Yêu cầu theo BA của từng mã SRS (mục 4 trong truy-vet.md), gom từ bảng soát; phần này được tính vào việc phát hiện thay đổi. Không sửa SRS. | SRS 2026-11-17; bảng soát 2026-11-18; TL đến TL-13 | — | mới 0; sửa 0; bỏ 0 |
