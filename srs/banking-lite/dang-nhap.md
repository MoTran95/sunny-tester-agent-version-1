# SRS — Đăng nhập (Banking Lite)

| | |
|---|---|
| Mã feature | `LOGIN` (quy tắc ID: [id-and-source-rules.md](../id-and-source-rules.md)) |
| Phiên bản hệ thống đã quan sát | 1.3.0 (https://banking-lite.vercel.app/) |
| Cập nhật lần cuối | 2026-11-17 |
| Tình trạng | **nháp** — chỉ ghi hành vi quan sát được, chưa xác nhận với team |
| Nhật ký khám phá gốc | [bao-cao.md](../../evidence/banking-lite/features/dang-nhap/bao-cao.md) (27 hàng, theo thứ tự thời gian) |

## 1. Mục đích, phạm vi, vai trò
- **Mục đích:** cổng vào hệ thống. Người dùng nhập **Mã nhân viên** và **Mật khẩu** để vào **Danh sách việc**; chưa đăng nhập thì mọi địa chỉ đều hiện màn hình này. Gồm cả đăng xuất, đổi ngôn ngữ ở màn hình đăng nhập và giới hạn đăng nhập sai.
- **Không thấy trên màn hình đăng nhập (ngoài phạm vi vì chưa có):** quên/đổi mật khẩu, đăng ký, "ghi nhớ đăng nhập", ô chọn workspace ([E01](#e01), [E02](#e02)).

| Tài khoản | Vai trò hiển thị (VI / EN) | Đã thử với feature này |
|---|---|---|
| P100001 | Chuyên viên khách hàng / `Banker` | Hầu hết các ca |
| P200001 | Chuyên viên định giá | Chỉ đăng nhập thành công (lượt khám phá đầu) — [E20](#e20) |
| P300001 | Chuyên viên thẩm định tín dụng | Chỉ đăng nhập thành công (lượt khám phá đầu) — [E20](#e20) |
| P100002 | ❓ chưa biết | Chưa đăng nhập |

## 2. Điều kiện tiên quyết
- Có Mã nhân viên + Mật khẩu của một tài khoản (do người dùng cung cấp; mật khẩu **không** ghi trong tài liệu).
- Mở hệ thống bằng trình duyệt tại https://banking-lite.vercel.app/.

## 3. User story và tiêu chí chấp nhận

**Cách đọc các bảng dưới đây.** Mỗi dòng là **một tình huống có thể đem đi test**, đọc từ trái sang phải như một câu chuyện:
1. **Bối cảnh** — hệ thống/người dùng đang ở tình trạng nào *trước khi* làm (ví dụ: "chưa đăng nhập").
2. **Người dùng làm** — thao tác cụ thể: nhập gì, bấm gì, mở gì.
3. **Hệ thống phản hồi** — điều đã **nhìn thấy** sau thao tác đó. Chữ trong dấu `…` là câu nguyên văn trên màn hình.

Cột cuối ghi nhãn (`đã thấy` = mình đã tự nhìn thấy; `chưa rõ` = còn thiếu/không chắc), bằng chứng (bấm số `E..` để xem ảnh/cách kiểm lại ở mục 6.1) và quy tắc/thông báo liên quan (tra ở mục 4). *(Trong tài liệu kiểm thử, ba cột đầu thường được gọi là Given – When – Then; mỗi dòng gọi là một "tiêu chí chấp nhận", viết tắt AC.)*

### `LOGIN-S01` — Đăng nhập để vào việc của mình
**Là** nhân viên ngân hàng có tài khoản, **tôi muốn** đăng nhập bằng Mã nhân viên và Mật khẩu **để** vào Danh sách việc (hoặc đúng trang tôi đang mở).

**Luồng:** mở hệ thống → thấy form → nhập mã + mật khẩu → bấm "Đăng nhập" (hoặc Enter) → vào Danh sách việc / đúng trang đã mở. Nếu nhập sai hoặc thiếu → xem `LOGIN-S02`.

| ID | Tình huống | Bối cảnh | Người dùng làm | Hệ thống phản hồi | Nhãn · Bằng chứng |
|---|---|---|---|---|---|
| `LOGIN-S01-AC01` | Mở hệ thống khi chưa đăng nhập | Chưa đăng nhập | Mở địa chỉ gốc `https://banking-lite.vercel.app/` | Hiện form **Đăng nhập** gồm: ô `Mã nhân viên *` (gợi ý bên dưới: `Chữ P và 6 chữ số, ví dụ P100001.`), ô `Mật khẩu *` (chữ gõ hiện dạng chấm), nút `Đăng nhập`, và chân trang ghi `Banking Lite · Phiên bản 1.3.0` | đã thấy · [E01](#e01) [E02](#e02) [E07](#e07) · Liên quan: `LOGIN-R01`, `LOGIN-R08`, `LOGIN-M07` |
| `LOGIN-S01-AC02` | Đăng nhập đúng | Đang ở form đăng nhập; có tài khoản hợp lệ | Nhập đúng Mã nhân viên và Mật khẩu, bấm `Đăng nhập` | Vào trang **Danh sách việc** của tài khoản đó. Thanh trên cùng hiện mã, vai trò và `DEFAULT`, ví dụ `P100001 · Chuyên viên khách hàng · DEFAULT`. **Không** có thông báo "đăng nhập thành công" | đã thấy · [E11](#e11) [E20](#e20) [E22](#e22) · Liên quan: `LOGIN-R05` |
| `LOGIN-S01-AC03` | Đăng nhập khi đã mở sẵn link hồ sơ | Chưa đăng nhập, nhưng đã mở link của một hồ sơ (đã thử: HL-000019 của chính người tạo) | Đăng nhập đúng | Mở **thẳng hồ sơ đó**, không về Danh sách việc | đã thấy (mới thử 1 link) · [E11](#e11) |
| `LOGIN-S01-AC04` | Gõ mã nhân viên bằng chữ thường | Đang ở form đăng nhập | Gõ `p100001` (chữ p thường) và mật khẩu đúng | Đăng nhập thành công; thanh trên hiện `P100001` (chữ P hoa). Vậy mã nhân viên **không phân biệt hoa/thường** (mới thử với một tài khoản) | đã thấy · [E12](#e12) · Liên quan: `LOGIN-R02` |
| `LOGIN-S01-AC05` | Nhấn phím Enter thay vì bấm nút | Đang ở form đăng nhập | Đặt con trỏ ở ô Mã nhân viên, nhấn **Enter** (đã thử khi mật khẩu trống) | Form được gửi đi giống như bấm nút `Đăng nhập` | đã thấy · [E10](#e10) |
| `LOGIN-S01-AC06` | Tải lại trang | Đã đăng nhập | Tải lại trang (F5) | Vẫn đang đăng nhập, không phải nhập lại | đã thấy · [E25](#e25) |
| `LOGIN-S01-AC07` | Mở `/login` khi đã đăng nhập | Đã đăng nhập | Mở `https://banking-lite.vercel.app/login` | Hiện **Danh sách việc** (không hiện form đăng nhập); thanh địa chỉ vẫn là `/login` | đã thấy · [E13](#e13) |
| `LOGIN-S01-AC08` | Mở địa chỉ không tồn tại khi đã đăng nhập | Đã đăng nhập | Mở địa chỉ không có thật, ví dụ `/khong-ton-tai-xyz` | Hiện **Danh sách việc**; thanh địa chỉ giữ nguyên; **không** có trang "không tìm thấy" | đã thấy · [E15](#e15) |

### `LOGIN-S02` — Được báo khi nhập sai, thiếu hoặc bị chặn
**Là** người dùng nhập chưa đúng, **tôi muốn** hệ thống từ chối và cho biết ở mức cần thiết **để** sửa lại hoặc chờ thử lại.

**Luồng chung:** nhập sai/thiếu → bấm "Đăng nhập" → hiện **khung lỗi màu đỏ** ở đầu form; vẫn ở màn hình đăng nhập, địa chỉ không đổi, ô Mã nhân viên giữ chữ đã gõ.

| ID | Tình huống | Bối cảnh | Người dùng làm | Hệ thống phản hồi | Nhãn · Bằng chứng |
|---|---|---|---|---|---|
| `LOGIN-S02-AC01` | Sai mật khẩu | Form đăng nhập; mã nhân viên **có thật** (ví dụ `P100001`) | Nhập **sai mật khẩu**, bấm `Đăng nhập` | Không đăng nhập. Khung lỗi đỏ: `Mã không gian, mã nhân viên hoặc mật khẩu không đúng.` (thông báo `LOGIN-M01`) | đã thấy · [E07](#e07) [E21](#e21) · Liên quan: `LOGIN-M01` |
| `LOGIN-S02-AC02` | Mã nhân viên không tồn tại | Form đăng nhập | Nhập mã không có thật (`P999999`) + mật khẩu bất kỳ | **Cùng khung lỗi y hệt AC01**: hệ thống không cho biết là mã sai hay mật khẩu sai | đã thấy · [E08](#e08) · Liên quan: `LOGIN-M01` |
| `LOGIN-S02-AC03` | Bỏ trống Mã nhân viên | Form đăng nhập | Để trống ô Mã nhân viên, nhập một mật khẩu, bấm `Đăng nhập` | Cùng khung lỗi `LOGIN-M01` như AC01. **Không** có câu "bắt buộc nhập mã" dù ô có dấu `*` | đã thấy · [E09](#e09) · Liên quan: `LOGIN-M01`, `LOGIN-R04` |
| `LOGIN-S02-AC04` | Mã nhân viên sai dạng | Form đăng nhập; mật khẩu đã gõ | Nhập mã sai dạng, mỗi lần một kiểu: `p999999`, thừa khoảng trắng đầu hoặc cuối, 5 hoặc 7 chữ số, `X999999`, `P99999A`, `P99-999` | **Mỗi kiểu đều nhận cùng khung lỗi `LOGIN-M01`**; không có thông báo riêng nói "mã sai định dạng" | đã thấy · [E23](#e23) · Liên quan: `LOGIN-M01`, `LOGIN-R01` |
| `LOGIN-S02-AC05` | Bỏ trống Mật khẩu | Form đăng nhập | Để trống ô Mật khẩu (ô mã: trống, hoặc `abc123`, hoặc `P100001`), bấm `Đăng nhập` hoặc nhấn Enter | Không đăng nhập. Khung lỗi đỏ có **2 dòng**: `Một số giá trị không hợp lệ.` (`LOGIN-M02`) và `validation.too_small (password)` (`LOGIN-M03` — mã kỹ thuật, chưa dịch ra câu dễ hiểu) | đã thấy · [E03](#e03) [E04](#e04) [E10](#e10) · Liên quan: `LOGIN-M02`, `LOGIN-M03`, `LOGIN-R04` |
| `LOGIN-S02-AC06` | Mã nhân viên quá dài | Form đăng nhập | Nhập mã rất dài (thử 210 ký tự) + mật khẩu bất kỳ | Không đăng nhập. Khung lỗi đỏ 2 dòng: `Một số giá trị không hợp lệ.` (`LOGIN-M02`) và `validation.too_big (employeeId)` (`LOGIN-M04`). Giới hạn tối đa là bao nhiêu ký tự: **chưa biết** | đã thấy · [E24](#e24) · Liên quan: `LOGIN-M02`, `LOGIN-M04`, `LOGIN-R03` |
| `LOGIN-S02-AC07` | Sai liên tiếp nhiều lần → bị chặn tạm | Đã đăng nhập không thành công **10 lần liên tiếp** kể từ lần đăng nhập đúng gần nhất | Gửi thêm một lần thông tin sai nữa | Bị chặn. Bản English hiện `Too many failed attempts. Try again in 5 minutes.` (`LOGIN-M05`). Bản tiếng Việt chưa thấy hiện trên màn hình. Ngưỡng chính xác là bao nhiêu lần: **chưa rõ** | đã thấy (1 lần; ngưỡng chưa rõ) · [E17](#e17) [E26](#e26) · Liên quan: `LOGIN-M05`, `LOGIN-R06` |
| `LOGIN-S02-AC08` | Đang bị chặn nhưng nhập đúng | Đang trong thời gian bị chặn của AC07 (đã thử khoảng 2 phút sau) | Nhập đúng mã và mật khẩu | **Vẫn đăng nhập thành công** (việc chặn không ngăn đăng nhập đúng) | đã thấy (1 lần) · [E18](#e18) · Liên quan: `LOGIN-R06` |

### `LOGIN-S03` — Dùng giao diện bằng Tiếng Việt hoặc English
**Là** người dùng, **tôi muốn** đổi ngôn ngữ ngay ở màn hình đăng nhập **để** đọc hiểu thông báo.

| ID | Tình huống | Bối cảnh | Người dùng làm | Hệ thống phản hồi | Nhãn · Bằng chứng |
|---|---|---|---|---|---|
| `LOGIN-S03-AC01` | Đổi ngôn ngữ ở màn hình đăng nhập | Đang ở màn hình đăng nhập (có thể đang hiện khung lỗi và đã gõ mã) | Bấm `Tiếng Việt` hoặc `English` | Mọi nhãn đổi **ngay** sang ngôn ngữ đã chọn; chữ đã gõ ở ô mã vẫn còn; khung lỗi vẫn hiện, câu chung được dịch (`Some values are not valid.` ⇄ `Một số giá trị không hợp lệ.`) | đã thấy · [E05](#e05) [E02](#e02) · Liên quan: `LOGIN-M02` |
| `LOGIN-S03-AC02` | Mã lỗi kỹ thuật không được dịch | Khung lỗi đang hiện dòng `validation.too_small (password)` hoặc `validation.too_big (employeeId)` | Đổi ngôn ngữ | Dòng mã lỗi đó **giữ nguyên chữ tiếng Anh** ở cả hai ngôn ngữ | đã thấy · [E05](#e05) · Liên quan: `LOGIN-M03`, `LOGIN-M04` |
| `LOGIN-S03-AC03` | Hệ thống nhớ ngôn ngữ đã chọn | Đã chọn một ngôn ngữ | Tải lại trang, hoặc bấm Đăng xuất | Vẫn đúng ngôn ngữ đã chọn (trình duyệt lưu lại, khóa `bl.locale`, giá trị `vi` hoặc `en`) | đã thấy · [E25](#e25) [E02](#e02) · Liên quan: `LOGIN-R07` |
| `LOGIN-S03-AC04` | Tên vai trò và định dạng số đổi theo ngôn ngữ | Đã đăng nhập `P100001` | Bấm `English` | Vai trò đổi từ `Chuyên viên khách hàng` thành `Banker`; số tiền hiện kiểu English (ví dụ `2,000,000,000`) | đã thấy · [E14](#e14) |

### `LOGIN-S04` — Đăng xuất và truy cập khi không có phiên đăng nhập
**Là** người dùng, **tôi muốn** đăng xuất và không ai xem được dữ liệu khi chưa đăng nhập **để** giữ an toàn tài khoản.

| ID | Tình huống | Bối cảnh | Người dùng làm | Hệ thống phản hồi | Nhãn · Bằng chứng |
|---|---|---|---|---|---|
| `LOGIN-S04-AC01` | Đăng xuất | Đã đăng nhập | Bấm `Đăng xuất` | Về form đăng nhập, thanh địa chỉ là `/`; ngôn ngữ giữ nguyên | đã thấy · [E02](#e02) [E21](#e21) |
| `LOGIN-S04-AC02` | Mở trang khi chưa đăng nhập | Chưa đăng nhập | Mở link một hồ sơ, hoặc `/integrations`, hoặc một địa chỉ không có thật | Hiện **form đăng nhập**, thanh địa chỉ giữ nguyên. **Không** có thông báo "cần đăng nhập" và **không** có trang "không tìm thấy" | đã thấy · [E06](#e06) [E27](#e27) · Liên quan: `LOGIN-M06` |
| `LOGIN-S04-AC03` | Nhấn Back sau khi đăng xuất | Vừa đăng xuất khi đang ở trang một hồ sơ | Bấm nút **Back** của trình duyệt | Địa chỉ quay về link hồ sơ nhưng chỉ hiện **form đăng nhập**; dữ liệu hồ sơ **không** hiện ra | đã thấy · [E19](#e19) |
| `LOGIN-S04-AC04` | Đăng xuất ở tab này, tab kia còn mở | Hai tab cùng trình duyệt, cùng phiên; đã đăng xuất ở tab 2; tab 1 vẫn đang hiện Danh sách việc | Ở tab 1 làm thao tác cần tải dữ liệu (ví dụ bấm tab `Tất cả hồ sơ`) | Tab 1 **không tự thay đổi** cho đến khi bạn thao tác; khi thao tác, tab 1 chuyển sang **form đăng nhập** (không có thông báo nào) | đã thấy · [E16](#e16) [E26](#e26) · Liên quan: `LOGIN-M06` |

## 4. Bảng tra cứu
### 4.1 Quy tắc dữ liệu
| ID | Trường / chủ đề | Quy tắc quan sát được | Nhãn | Bằng chứng |
|---|---|---|---|---|
| `LOGIN-R01` | Mã nhân viên — định dạng | Dòng gợi ý: `Chữ P và 6 chữ số, ví dụ P100001.` Máy chủ **không** báo lỗi định dạng riêng (mọi mã sai định dạng chỉ nhận `LOGIN-M01`). | đã thấy (gợi ý); chưa rõ (có kiểm tra không) | [E01](#e01), [E23](#e23) |
| `LOGIN-R02` | Mã nhân viên — hoa/thường | `p100001` đăng nhập được như `P100001` (mới thử với một tài khoản). | đã thấy | [E12](#e12) |
| `LOGIN-R03` | Mã nhân viên — độ dài tối đa | Có độ dài tối đa (mã 210 ký tự bị từ chối `too_big`); giá trị tối đa **chưa biết**. | chưa rõ | [E24](#e24) |
| `LOGIN-R04` | Hai ô bắt buộc | Cả hai ô đánh dấu `*`, thẻ form có `novalidate` (trình duyệt không chặn). Mật khẩu trống → 400 `too_small (password)`. Mã trống + mật khẩu có giá trị → 401 (không báo bắt buộc). | đã thấy; chưa rõ (vì sao khác nhau) | [E03](#e03), [E09](#e09), [E10](#e10), [E25](#e25) |
| `LOGIN-R05` | Hiển thị sau đăng nhập | `/api/me` trả `employeeId`, `role` (ví dụ `BANKER`), `workspace` (`DEFAULT`), danh sách quyền; thanh trên hiện `<mã> · <vai trò> · DEFAULT` (`DEFAULT` = workspace). | đã thấy | [E22](#e22) |
| `LOGIN-R06` | Giới hạn đăng nhập sai | Sau 10 lần thất bại liên tiếp (kể từ lần đăng nhập đúng gần nhất) → 429, `thử lại sau 5 phút` (`{minutes}` = 5). Áp dụng cả với mã không tồn tại. Đăng nhập đúng vẫn qua lúc bị chặn. Ngưỡng chính xác, phạm vi chặn (IP/trình duyệt/mã/toàn hệ thống), có đặt lại sau lần đúng không: **chưa rõ**. | đã thấy; chưa rõ (tham số) | [E17](#e17), [E18](#e18), [E26](#e26) |
| `LOGIN-R07` | Ngôn ngữ | Lưu ở trình duyệt, khóa `bl.locale` ∈ {`vi`, `en`}; `<html lang>` đổi theo. | đã thấy | [E25](#e25) |
| `LOGIN-R08` | Thuộc tính ô nhập | Mã nhân viên: `name=employeeId`, `autocomplete=username`. Mật khẩu: `type=password`, `autocomplete=current-password`. Không có `maxlength`/`pattern` ở HTML. | đã thấy | [E25](#e25) |

### 4.2 Thông báo hệ thống (nguyên văn)
| ID | Khi nào | Tiếng Việt | English | Bằng chứng |
|---|---|---|---|---|
| `LOGIN-M01` | Sai thông tin đăng nhập (401) | `Mã không gian, mã nhân viên hoặc mật khẩu không đúng.` (thấy trên màn hình) | `Workspace, employee ID or password is incorrect.` (**chỉ** thấy trong tệp giao diện, chưa thấy trên màn hình) | [E07](#e07), [E26](#e26) |
| `LOGIN-M02` | Dữ liệu nhập không hợp lệ (400), câu chung | `Một số giá trị không hợp lệ.` | `Some values are not valid.` | [E03](#e03), [E05](#e05) |
| `LOGIN-M03` | Mật khẩu trống, dòng mã lỗi | `validation.too_small (password)` | `validation.too_small (password)` | [E03](#e03), [E10](#e10) |
| `LOGIN-M04` | Mã nhân viên quá dài, dòng mã lỗi | `validation.too_big (employeeId)` | chưa quan sát | [E24](#e24) |
| `LOGIN-M05` | Bị chặn vì sai quá nhiều lần (429) | `Đăng nhập sai quá nhiều lần. Thử lại sau {minutes} phút.` (**chỉ** thấy trong tệp giao diện) | `Too many failed attempts. Try again in 5 minutes.` (thấy trên màn hình) | [E17](#e17), [E26](#e26) |
| `LOGIN-M06` | Chưa có phiên (`auth.required`) | `Vui lòng đăng nhập.` (có trong tệp giao diện, **chưa từng thấy hiện**) | `Please sign in.` (cùng ghi chú) | [E26](#e26) |
| `LOGIN-M07` | Nhãn, nút, gợi ý, chân trang | `Đăng nhập` · `Mã nhân viên *` · `Mật khẩu *` · `Chữ P và 6 chữ số, ví dụ P100001.` · `Banking Lite · Phiên bản 1.3.0` · `Đăng xuất` | `Sign in` · `Employee ID *` · `Password *` · `P followed by 6 digits, e.g. P100001.` · `Banking Lite · Version 1.3.0` · `Sign out` | [E01](#e01), [E02](#e02) |

## 5. Điểm chưa rõ và câu hỏi cho team
| ID | Đã thấy | Vì sao chưa rõ | Câu hỏi | Liên quan | Trạng thái |
|---|---|---|---|---|---|
| `LOGIN-Q01` | Thông báo lỗi nhắc "mã không gian" (EN: *Workspace*); `/api/me` có `workspace: DEFAULT`; form không có ô workspace | Chưa biết workspace là gì và có đổi được không | Workspace là gì? Vì sao form không cho nhập? Có tài khoản ở workspace khác không? | M01, R05, S01-AC02 | mở (có manh mối) |
| `LOGIN-Q02` | Mọi lỗi thông tin đều ra cùng một câu | Không rõ có chủ ý che thông tin hay không | Cùng thông báo cho "mã không tồn tại" và "sai mật khẩu" có phải chủ ý? | S02-AC01..AC03 | mở |
| `LOGIN-Q03` | Dòng `validation.too_small/too_big (…)` hiện nguyên mã, không dịch | Cùng kiểu với `validation.too_small (marketValue)` ở Định giá | Thông báo lỗi nhập liệu có cần câu dễ hiểu và có dịch không? | M03, M04, S03-AC02 | mở |
| `LOGIN-Q04` | Mã sai định dạng không bị báo riêng; không phân biệt hoa/thường; mã 210 ký tự bị từ chối | Không rõ quy tắc chính thức | Định dạng chính thức của Mã nhân viên? Có chuẩn hóa chữ hoa/khoảng trắng không? Độ dài tối đa? | R01, R02, R03 | mở |
| `LOGIN-Q05` | Mật khẩu trống báo lỗi; mã trống + mật khẩu có giá trị không báo "bắt buộc" | Không rõ vì sao hai ô xử lý khác nhau dù cùng dấu `*` | Ô Mã nhân viên bắt buộc theo cách nào? | R04, S02-AC03 | mở |
| `LOGIN-Q06` | Chặn 429 sau 10 lần thất bại, 5 phút, cả với mã không tồn tại; đăng nhập đúng vẫn qua | Không rõ ngưỡng, phạm vi chặn, có đặt lại sau lần đúng, có mở khóa thủ công | Chính sách chặn là gì (ngưỡng, thời gian, theo IP/mã/toàn hệ thống)? Vì sao đăng nhập đúng vẫn qua? | R06, S02-AC07, AC08 | mở |
| `LOGIN-Q07` | Quay lại đúng link sau khi đăng nhập | Chỉ thử một link của chính người tạo | Áp dụng cho mọi link không? Link hồ sơ của người khác / vai trò không đủ quyền thì sao? | S01-AC03 | mở |
| `LOGIN-Q08` | `/login` khi đã đăng nhập và địa chỉ không tồn tại đều hiện Danh sách việc, URL giữ nguyên | Không rõ có chủ ý | Có cần chuyển hướng, có trang "không tìm thấy" không? | S01-AC07, AC08, S04-AC02 | mở |
| `LOGIN-Q09` | Thông báo `Vui lòng đăng nhập.` có trong hệ thống nhưng chưa từng hiện; tab bị đăng xuất chỉ về form | Không rõ khi nào hiện | Khi phiên hết/bị đăng xuất ở nơi khác, người dùng có được thông báo không? | M06, S04-AC04 | mở |
| `LOGIN-Q10` | Không đọc được cách giữ phiên (không có khóa phiên trong `localStorage`/`sessionStorage`; `document.cookie` rỗng) | Không biết thời hạn phiên | Phiên giữ bằng gì, hết hạn sau bao lâu? | S01-AC06 | mở |

## 6. Bằng chứng và chưa khám phá
Cách gọi tên: **Ảnh NN** = ảnh trong thư mục `evidence/banking-lite/features/dang-nhap/screenshots/` (đánh số NN). **Ảnh cũ NN** = ảnh trong `evidence/banking-lite/screenshots/` (lượt khám phá đầu). **Nhật ký, hàng N** = hàng N trong bảng ở mục 1 của [bao-cao.md](../../evidence/banking-lite/features/dang-nhap/bao-cao.md) (ghi thao tác theo thứ tự thời gian). Mọi ngày đều **2026-11-17**, phiên bản hệ thống **1.3.0**.

### 6.1 Bằng chứng
Loại: **ảnh** · **quan sát** (công cụ nhà phát triển/Network/giá trị lưu trình duyệt — **không có ảnh**) · **tệp giao diện** (đọc mã công khai của trang, không phải hành vi trên màn hình) · **báo cáo cũ**.

| ID | Loại · tài khoản | Thao tác đã làm | Tệp | Cách kiểm lại |
|---|---|---|---|---|
| <a id="e01"></a>`LOGIN-E01` | ảnh · chưa đăng nhập | Mở màn hình đăng nhập (Tiếng Việt) | [Ảnh cũ 01](../../evidence/banking-lite/screenshots/01-login-page-vi.jpg) | Đăng xuất, mở `/`, chọn Tiếng Việt |
| <a id="e02"></a>`LOGIN-E02` | ảnh · P100001 → chưa đăng nhập | Đăng xuất khi đang English | [Ảnh 03](../../evidence/banking-lite/features/dang-nhap/screenshots/03-chua-dang-nhap-sau-Sign-out-trang-Sign-in-English.jpg) | Chọn English, bấm Sign out |
| <a id="e03"></a>`LOGIN-E03` | ảnh · chưa đăng nhập | Để trống hai ô, bấm Sign in | [Ảnh 04](../../evidence/banking-lite/features/dang-nhap/screenshots/04-chua-dang-nhap-de-trong-hai-o-loi-validation-too_small-password.jpg) | Mở `/`, bấm nút khi để trống |
| <a id="e04"></a>`LOGIN-E04` | ảnh · chưa đăng nhập | Mã `abc123`, mật khẩu trống | [Ảnh 05](../../evidence/banking-lite/features/dang-nhap/screenshots/05-chua-dang-nhap-ma-abc123-mat-khau-trong-van-chi-bao-password.jpg) | Gõ `abc123` ở ô mã, để trống mật khẩu, bấm nút |
| <a id="e05"></a>`LOGIN-E05` | ảnh · chưa đăng nhập | Đang hiện lỗi, bấm Tiếng Việt | [Ảnh 06](../../evidence/banking-lite/features/dang-nhap/screenshots/06-chua-dang-nhap-doi-Tieng-Viet-giu-chu-da-go-ma-loi-khong-dich.jpg) | Tái hiện E04 rồi đổi ngôn ngữ |
| <a id="e06"></a>`LOGIN-E06` | ảnh · chưa đăng nhập | Mở link hồ sơ HL-000019 khi chưa đăng nhập | [Ảnh 07](../../evidence/banking-lite/features/dang-nhap/screenshots/07-chua-dang-nhap-mo-link-ho-so-hien-form-dang-nhap-giu-nguyen-URL.jpg) | Đăng xuất, dán `/applications/db5f18e6-7a49-4d61-b307-0a485c8ab20d` |
| <a id="e07"></a>`LOGIN-E07` | ảnh · chưa đăng nhập | `P100001` + mật khẩu sai | [Ảnh 08](../../evidence/banking-lite/features/dang-nhap/screenshots/08-chua-dang-nhap-P100001-sai-mat-khau-bao-ma-khong-gian-ma-nhan-vien-hoac-mat-khau-khong-dung.jpg) | Nhập mã đúng + một mật khẩu sai |
| <a id="e08"></a>`LOGIN-E08` | ảnh · chưa đăng nhập | `P999999` + mật khẩu sai | [Ảnh 09](../../evidence/banking-lite/features/dang-nhap/screenshots/09-chua-dang-nhap-P999999-khong-ton-tai-van-bao-cung-thong-bao-nhu-sai-mat-khau.jpg) | Nhập mã `P999999` + mật khẩu bất kỳ |
| <a id="e09"></a>`LOGIN-E09` | ảnh · chưa đăng nhập | Ô mã trống + mật khẩu có giá trị | [Ảnh 13](../../evidence/banking-lite/features/dang-nhap/screenshots/13-chua-dang-nhap-de-trong-ma-nhan-vien-co-mat-khau-van-bao-thong-tin-khong-dung-401.jpg) | Chỉ gõ mật khẩu, bấm nút |
| <a id="e10"></a>`LOGIN-E10` | ảnh · chưa đăng nhập | `P100001`, mật khẩu trống, nhấn Enter | [Ảnh 18](../../evidence/banking-lite/features/dang-nhap/screenshots/18-chua-dang-nhap-P100001-mat-khau-trong-nhan-Enter-400-validation-too_small-password.jpg) | Gõ mã, nhấn Enter ở ô mã |
| <a id="e11"></a>`LOGIN-E11` | ảnh · P100001 | Đăng nhập đúng khi đang ở link hồ sơ | [Ảnh 10](../../evidence/banking-lite/features/dang-nhap/screenshots/10-P100001-dang-nhap-dung-tu-link-ho-so-vao-thang-HL-000019.jpg) | Mở link hồ sơ khi chưa đăng nhập, đăng nhập đúng |
| <a id="e12"></a>`LOGIN-E12` | ảnh · P100001 | Đăng nhập bằng `p100001` chữ thường | [Ảnh 17](../../evidence/banking-lite/features/dang-nhap/screenshots/17-P100001-dang-nhap-bang-ma-chu-thuong-p100001-thanh-cong-thanh-tren-hien-P100001.jpg) | Gõ `p100001` + mật khẩu đúng |
| <a id="e13"></a>`LOGIN-E13` | ảnh · P100001 | Đã đăng nhập, mở `/login` | [Ảnh 01](../../evidence/banking-lite/features/dang-nhap/screenshots/01-P100001-mo-url-login-khi-da-dang-nhap-van-hien-danh-sach-viec.jpg) | Đăng nhập rồi mở `https://banking-lite.vercel.app/login` |
| <a id="e14"></a>`LOGIN-E14` | ảnh · P100001 | Đổi sang English khi đã đăng nhập | [Ảnh 02](../../evidence/banking-lite/features/dang-nhap/screenshots/02-P100001-doi-sang-English-nhan-vai-tro-Banker.jpg) | Bấm English ở thanh trên |
| <a id="e15"></a>`LOGIN-E15` | ảnh · P100001 | Đã đăng nhập, mở `/khong-ton-tai-xyz` | [Ảnh 11](../../evidence/banking-lite/features/dang-nhap/screenshots/11-P100001-da-dang-nhap-mo-dia-chi-khong-ton-tai-van-hien-danh-sach-viec.jpg) | Mở địa chỉ đó khi đã đăng nhập |
| <a id="e16"></a>`LOGIN-E16` | ảnh · P100001 | Hai tab: đăng xuất ở tab 2, thao tác ở tab 1 | [Ảnh 12](../../evidence/banking-lite/features/dang-nhap/screenshots/12-P100001-hai-tab-dang-xuat-o-tab-kia-tab-cu-bam-Tat-ca-ho-so-ve-form-dang-nhap.jpg) | Mở 2 tab, đăng xuất ở tab 2, bấm "Tất cả hồ sơ" ở tab 1 |
| <a id="e17"></a>`LOGIN-E17` | ảnh · chưa đăng nhập | Sau 10 lần thất bại liên tiếp, thử tiếp (English) | [Ảnh 14](../../evidence/banking-lite/features/dang-nhap/screenshots/14-chua-dang-nhap-English-Too-many-failed-attempts-429-thu-lai-sau-5-phut.jpg) | **Cẩn thận:** gây chặn 5 phút; xem nhật ký, hàng 21 |
| <a id="e18"></a>`LOGIN-E18` | ảnh · P100001 | Đăng nhập đúng khi đang bị chặn | [Ảnh 15](../../evidence/banking-lite/features/dang-nhap/screenshots/15-P100001-dang-nhap-dung-luc-dang-bi-chan-429-van-vao-duoc-English.jpg) | Ngay sau E17, đăng nhập đúng |
| <a id="e19"></a>`LOGIN-E19` | ảnh · P100001 | Đăng xuất từ trang hồ sơ rồi bấm Back | [Ảnh 16](../../evidence/banking-lite/features/dang-nhap/screenshots/16-chua-dang-nhap-nhan-Back-sau-dang-xuat-hien-form-khong-lo-ho-so.jpg) | Mở hồ sơ, Đăng xuất, bấm Back |
| <a id="e20"></a>`LOGIN-E20` | báo cáo cũ · P100001/P200001/P300001 | Danh sách việc sau đăng nhập | [Ảnh cũ 02](../../evidence/banking-lite/screenshots/02-P100001-danh-sach-viec-ho-so-cua-toi.jpg), [Ảnh cũ 19](../../evidence/banking-lite/screenshots/19-P200001-danh-sach-viec-cho-dinh-gia.jpg), [Ảnh cũ 27](../../evidence/banking-lite/screenshots/27-P300001-danh-sach-viec-cho-quyet-dinh.jpg) | Đăng nhập từng tài khoản |
| <a id="e21"></a>`LOGIN-E21` | quan sát · nhiều | Mã trả về của API đăng nhập/đăng xuất | [Nhật ký, hàng 14](../../evidence/banking-lite/features/dang-nhap/bao-cao.md) | F12 → Network, lọc `/api/auth`: `sign-in` 400/401/200, `sign-out` 204, `/api/me` 401/200 |
| <a id="e22"></a>`LOGIN-E22` | quan sát · P100001 | Đọc `GET /api/me` | [Nhật ký, hàng 15](../../evidence/banking-lite/features/dang-nhap/bao-cao.md) | Đã đăng nhập, F12 → Network → `/api/me` → Response |
| <a id="e23"></a>`LOGIN-E23` | quan sát · chưa đăng nhập | 8 biến thể mã không tồn tại → đều 401 | [Nhật ký, hàng 19](../../evidence/banking-lite/features/dang-nhap/bao-cao.md) | Giữ mật khẩu, thử lần lượt từng mã; xem Network (không có ảnh). **Cẩn thận giới hạn đăng nhập (R06)** |
| <a id="e24"></a>`LOGIN-E24` | quan sát · chưa đăng nhập | Mã 210 ký tự → 400 `too_big` | [Nhật ký, hàng 20](../../evidence/banking-lite/features/dang-nhap/bao-cao.md) | Gõ mã rất dài + mật khẩu bất kỳ (không có ảnh) |
| <a id="e25"></a>`LOGIN-E25` | quan sát · nhiều | `localStorage` (`bl.locale`), tải lại giữ phiên, thuộc tính ô nhập | [Nhật ký, hàng 3 và 13](../../evidence/banking-lite/features/dang-nhap/bao-cao.md) | F12 → Application → Local Storage; Elements → thẻ `<input>`/`<form>` |
| <a id="e26"></a>`LOGIN-E26` | tệp giao diện | Bảng thông báo VI/EN và xử lý `auth.required` trong `/assets/main.99595f2e.js` | [Nhật ký, hàng 23 và 24](../../evidence/banking-lite/features/dang-nhap/bao-cao.md) | F12 → Sources/Network mở tệp, tìm `auth.locked`, `auth.invalidCredentials`, `auth.required` (tên tệp có thể đổi theo bản phát hành) |
| <a id="e27"></a>`LOGIN-E27` | quan sát · chưa đăng nhập | Mở `/integrations` và địa chỉ không tồn tại | [Nhật ký, hàng 9](../../evidence/banking-lite/features/dang-nhap/bao-cao.md) | Đăng xuất, mở hai địa chỉ đó (không có ảnh riêng) |

### 6.2 Chưa khám phá
- Hết hạn phiên theo thời gian (chưa chờ); đăng nhập hai **trình duyệt/máy** khác nhau.
- Chặn đăng nhập: có hết sau 5 phút không (chưa chờ kiểm), thông báo tiếng Việt trên màn hình, chặn theo IP/mã/toàn hệ thống.
- Mật khẩu rất dài, ký tự đặc biệt, khoảng trắng.
- Ca sai mật khẩu của P200001, P300001, P100002 (mỗi lần sai tính vào giới hạn đăng nhập); đăng nhập P100002.
- Bấm Đăng nhập hai lần nhanh; giao diện điện thoại; điều hướng bằng bàn phím/trợ năng.

## 7. Lịch sử thay đổi
| Ngày | Phiên bản hệ thống | Thay đổi | Lý do |
|---|---|---|---|
| 2026-11-17 | 1.3.0 | Tạo SRS lần đầu theo khuôn FR/BR (14 FR, 5 BR) | Pilot "khám phá → SRS" |
| 2026-11-17 | 1.3.0 | **Viết lại theo khuôn v2** (4 story, 24 AC, 8 quy tắc, 7 thông báo, 10 câu hỏi, 27 bằng chứng có liên kết); thêm kết quả khám phá mới: Network, tệp giao diện, hai tab, Back, chặn 429, mã chữ thường/dài/Enter | Người dùng cần truy nguồn, ID thống nhất, kiểu story + AC |
