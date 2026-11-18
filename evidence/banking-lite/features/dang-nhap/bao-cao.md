# Đăng nhập — nhật ký khám phá bổ sung (phần không cần mật khẩu)

Ngày: 2026-11-17 · Hệ thống: https://banking-lite.vercel.app/ · Phiên bản ghi ở chân trang: **1.3.0**
Khung nhìn 606×845. Ảnh: `screenshots/NN-…jpg`. Ảnh nền cũ của màn hình đăng nhập: `../../screenshots/01-login-page-vi.jpg` (Tiếng Việt, chưa có lỗi) và `../../screenshots/33-…` (English, sau khi đăng nhập).
Quy tắc: Claude **không tự gõ mật khẩu**. Các ca cần mật khẩu ở mục "Cần người dùng làm" bên dưới, chưa có kết quả.

## 0. Bảng phủ (dựng 2026-11-18 từ các hàng sẵn có, không khám phá lại)
| Nhóm ca | Trạng thái | Hàng nhật ký / lý do |
|---|---|---|
| Luồng chính thành công (đăng nhập đúng) | Đã làm | #12, #22, #26 |
| Từng nhánh lỗi (để trống, sai định dạng, sai mật khẩu, mã không tồn tại, mã rất dài, bị chặn 429) | Đã làm | #5, #6, #10, #11, #18, #19, #20, #21 |
| Từng vai trò | Chưa có trong nhật ký | Chỉ đăng nhập đúng bằng P100001; P100002 chưa thử (mục 3); P200001, P300001 chưa đăng nhập trong nhật ký này |
| Đổi ngôn ngữ | Đã làm | #2, #3, #7; thông báo chặn 429 bản tiếng Việt chưa thấy (#21), chỉ đọc từ tệp giao diện (#23) |
| Tải lại trang, nút Back, hai tab | Đã làm | #3, #25, #17 |
| Link sâu khi chưa đăng nhập; địa chỉ không tồn tại | Đã làm | #1, #8, #9, #12, #16 |
| Phản hồi mạng (mã trạng thái, `GET /api`) | Đã làm | #14, #15 |
| Tệp giao diện (chuỗi thông báo) | Đã làm | #23, #24 |
| Form: để trống, sai định dạng, khoảng trắng, hoa/thường, rất dài, Enter, thuộc tính HTML | Đã làm | #5, #6, #13, #19, #20, #26, #27 |
| Form: độ dài/ký tự cho phép của mật khẩu; bấm hai lần liên tiếp | Chưa làm | Mục 3 (mật khẩu do người dùng gõ; thao tác lặp có thể kích hoạt chặn, xem ghi chú an toàn) |
| Phiên: hết hạn phiên | Chưa làm | Mục 3 (cần chờ thời gian dài) |
| Phiên: hai trình duyệt/máy khác nhau cùng tài khoản | Chưa làm | Mục 3 (cần trình duyệt/máy thứ hai) |
| Danh sách/bảng; luồng nhiều bước | Không áp dụng | Đăng nhập không có danh sách hay bước riêng (Danh sách việc là màn sau đăng nhập, thuộc feature khác) |

## 1. Đã thấy (có thao tác thật)

| # | Thao tác | Kết quả quan sát (nguyên văn khi có) | Ảnh |
|---|---|---|---|
| 1 | Trình duyệt đang đăng nhập sẵn P100001. Mở `/login` | URL giữ `/login` nhưng hiện **Danh sách việc** (không chuyển sang trang khác, không hiện form đăng nhập) | 01 |
| 2 | Bấm **English** khi đã đăng nhập | Toàn bộ nhãn đổi ngay; thanh trên đổi từ `P100001 · Chuyên viên khách hàng · DEFAULT` sang `P100001 · Banker · DEFAULT`; số hiện `2,000,000,000`; cột ngày bị cắt ở khung hẹp (thấy `17/11/20…` rồi `12:40`) | 02 |
| 3 | Tải lại trang `/` | Vẫn đăng nhập, vẫn English. `localStorage` có đúng một khóa `bl.locale` = `en`; `<html lang="en">`. Không thấy khóa phiên trong `localStorage`/`sessionStorage`; `document.cookie` rỗng (cách giữ phiên ❓ chưa biết) | — |
| 4 | Bấm **Sign out** (Đăng xuất) | Về trang đăng nhập, URL `/`; ngôn ngữ English giữ nguyên; `bl.locale` còn | 03 |
| 5 | Bấm **Sign in** khi **để trống cả hai ô** | Khung đỏ: `Some values are not valid.` + một dòng `validation.too_small (password)`. Chỉ nhắc ô password, **không nhắc Employee ID**. Không có kiểm tra nhập liệu của trình duyệt (thẻ form có `novalidate`; hai ô có thuộc tính `required`) | 04 |
| 6 | Gõ Employee ID `abc123`, để trống mật khẩu, bấm **Sign in** | Lỗi y hệt mục 5 (chỉ `validation.too_small (password)`), **không có lỗi về định dạng mã nhân viên**; ô ID giữ `abc123` | 05 |
| 7 | Bấm **Tiếng Việt** trên trang đăng nhập đang có lỗi | Nhãn đổi ngay; chữ đã gõ giữ nguyên; dòng đầu dịch thành `Một số giá trị không hợp lệ.` nhưng dòng mã `validation.too_small (password)` **vẫn nguyên mã** (không dịch). `bl.locale` = `vi` | 06 |
| 8 | Chưa đăng nhập, mở thẳng `/applications/db5f18e6-…` (HL-000019) | Hiện **form đăng nhập**, URL giữ nguyên link hồ sơ, không có thông báo "cần đăng nhập", không chuyển hướng | 07 |
| 9 | Chưa đăng nhập, mở `/integrations` và `/khong-ton-tai-xyz` | Cả hai đều hiện form đăng nhập, URL giữ nguyên (không có trang "không tìm thấy" nào) | — |
| 10 | **Ca A** (người dùng gõ): mở link hồ sơ HL-000019 khi chưa đăng nhập, Mã nhân viên `P100001` + mật khẩu sai, bấm Đăng nhập | Khung đỏ (`role=alert`): **`Mã không gian, mã nhân viên hoặc mật khẩu không đúng.`** Ô mã nhân viên giữ `P100001`; ô mật khẩu vẫn còn chữ đã gõ (3 ký tự); URL vẫn là link hồ sơ; không ghi nhận khóa hay chậm trễ ở lần thử đầu. Thông báo nhắc "mã không gian" nhưng form **không có ô nào tên như vậy** (❓ nghĩa là gì) | 08 |
| 11 | **Ca B** (người dùng gõ/bấm): Mã nhân viên `P999999` (mình điền sẵn) + mật khẩu sai, bấm Đăng nhập | Khung đỏ **giống hệt ca A**: `Mã không gian, mã nhân viên hoặc mật khẩu không đúng.` → không phân biệt "mã không tồn tại" với "sai mật khẩu". Lưu ý: vì thông báo giống lần trước nên mình không tự chứng kiến lúc bấm; ô ID đã là `P999999` và khung lỗi đang hiện | 09 |
| 12 | **Ca C** (người dùng gõ): đang ở link hồ sơ HL-000019, đăng nhập **đúng** bằng P100001 | **Vào thẳng đúng hồ sơ HL-000019** (URL giữ nguyên, hiện bước "Người vay", trạng thái Đã phê duyệt), không về Danh sách việc. Thanh trên: `P100001 · Chuyên viên khách hàng · DEFAULT`; ngôn ngữ Tiếng Việt (đang đặt ở Tiếng Việt từ trước); không có thông báo "đăng nhập thành công" | 10 |
| 13 | Thuộc tính ô nhập | Employee ID: `name=employeeId`, `autocomplete=username`, không có `maxlength`/`pattern`. Password: `type=password`, `autocomplete=current-password` | — |
| 14 | Xem các lệnh gọi mạng (công cụ đọc mạng của trình duyệt, **không đọc nội dung gửi đi**) quanh các ca ở hàng 5–12 | Đăng nhập gọi `POST /api/auth/sign-in`. Theo thứ tự các lần bấm: **400** (hai lần: để trống; `abc123`), **401** (hai lần: ca A, ca B), **200** (ca C đúng). Đăng xuất: `POST /api/auth/sign-out` → **204**. Khi chưa đăng nhập, `GET /api/me` → **401**; đã đăng nhập → **200**. `GET /api/health` → 200 `{"status":"ok","version":"1.3.0"}`. `GET /api/settings` → `{"release":"1.3.0","settings":{}}`. (Khớp thứ tự lần bấm là suy ra từ thứ tự yêu cầu, không có dấu thời gian.) Không đọc được nội dung phản hồi lỗi | — (không có ảnh; cách kiểm lại: mở công cụ nhà phát triển → tab Network) |
| 15 | Đã đăng nhập P100001, đọc `GET /api/me` | Trả `{"employeeId":"P100001","role":"BANKER","workspace":"DEFAULT","permissions":["application.view","application.create","application.capture","valuation.request","valuation.cancel","pricing.set","application.submit","events.view","registry.search"]}`. → chữ `DEFAULT` trên thanh trên là **workspace** của tài khoản; "mã không gian" trong thông báo lỗi **có thể** là "workspace" (suy luận, ❓ chờ team xác nhận) | — (cách kiểm lại: Network → `/api/me`) |
| 16 | **Đã đăng nhập**, mở địa chỉ không tồn tại `/khong-ton-tai-xyz` | Hiện **Danh sách việc**, URL giữ nguyên; không có trang "không tìm thấy" | 11 |
| 17 | Mở **hai tab** cùng phiên; bấm Đăng xuất ở tab 2; ở tab 1 (cũ) bấm tab "Tất cả hồ sơ" | Tab 2 dùng chung phiên (đã đăng nhập sẵn). Sau khi tab 2 đăng xuất, tab 1 **vẫn hiện Danh sách việc** (không tự cập nhật). Khi tab 1 gọi API (`/api/applications?scope=all` → **401**) thì tab 1 chuyển sang **form đăng nhập**, không có thông báo nào | 12 |
| 18 | (Người dùng bấm) **ô Mã nhân viên trống** + mật khẩu có giá trị, bấm Đăng nhập | Lệnh gọi sign-in trả **401**; cùng thông báo `Mã không gian, mã nhân viên hoặc mật khẩu không đúng.` (không có lỗi "bắt buộc" cho ô mã). Mình thấy kết quả sau khi người dùng báo xong, xác nhận bằng lệnh gọi mạng | 13 |
| 19 | Mật khẩu giữ nguyên (do người dùng gõ). Điền lần lượt mã **không tồn tại** rồi bấm Đăng nhập: `p999999` · ` P999999` (khoảng trắng đầu) · `P999999 ` (khoảng trắng cuối) · `P99999` (5 số) · `P9999999` (7 số) · `X999999` · `P99999A` · `P99-999` | **Cả 8 đều 401** và cùng thông báo như hàng 10: không có thông báo riêng về định dạng/chữ thường/khoảng trắng. (Một lần bấm trong chuỗi này không gửi đi do mình bấm đúng lúc khung lỗi biến mất làm nút lệch chỗ; đã làm lại. Không có ảnh từng biến thể, chỉ có số liệu lệnh gọi mạng) | — |
| 20 | Điền mã rất dài (210 ký tự, `P` + toàn số 9) rồi bấm Đăng nhập | Lệnh gọi trả **400**; khung lỗi: `Một số giá trị không hợp lệ.` + `validation.too_big (employeeId)` → **Mã nhân viên có độ dài tối đa** (giá trị tối đa chưa biết); mã lỗi thô, không dịch (giống hàng 5). Không có ảnh (khung lỗi chỉ đọc bằng văn bản) | — |
| 21 | Bấm Đăng nhập tiếp (giao diện English, mã `P999999`, mật khẩu sai) sau chuỗi trên | Lệnh gọi trả **429**; khung lỗi: **`Too many failed attempts. Try again in 5 minutes.`** Xảy ra lúc **14:23 17/11/2026 (giờ máy)**, sau **9 lần 401 và 1 lần 400 liên tiếp** kể từ lần đăng nhập đúng gần nhất (tính cả 2 lần 401 trước đó ở ca A, B thì là 11 lần 401); lần thứ 11 bị chặn. Chưa biết lần đăng nhập đúng có đặt lại bộ đếm không. Bị chặn cả với **mã không tồn tại** → giới hạn không chỉ theo một tài khoản thật; chặn theo cái gì (địa chỉ IP, trình duyệt, toàn hệ thống) ❓ chưa biết. Ngưỡng chính xác ❓ (bị chặn sau 10–11 lần thất bại, tùy cách đếm). Thông báo tiếng Việt chưa quan sát. **Mình đã vô tình kích hoạt việc chặn này (xem ghi chú dưới)** | 14 |
| 22 | (Người dùng gõ) Lúc **14:25**, khoảng 2 phút sau lần bị 429, đăng nhập **đúng** `P100001` ở giao diện English | **Đăng nhập thành công** (sign-in trả **200**), vào Worklist; không bị chặn. → việc chặn 429 **không ngăn đăng nhập đúng** trong thời gian bị chặn (lý do ❓: chỉ chặn lần sai? đặt lại bộ đếm khi đúng? theo mã nhân viên?). Sau đó mình chưa thử lại lần sai nào để xem còn bị chặn không | 15 |
| 23 | Đọc **tệp giao diện công khai** `/assets/main.99595f2e.js` (không phải hành vi thấy trên màn hình): tìm bảng thông báo | Có các cặp thông báo: `auth.invalidCredentials` = `Mã không gian, mã nhân viên hoặc mật khẩu không đúng.` / EN **`Workspace, employee ID or password is incorrect.`**; `auth.locked` = `Đăng nhập sai quá nhiều lần. Thử lại sau {minutes} phút.` / EN `Too many failed attempts. Try again in {minutes} minutes.`; `auth.required` = `Vui lòng đăng nhập.` / `Please sign in.` (thông báo này **chưa từng thấy hiện** trên màn hình). → "Mã không gian" = bản dịch của "Workspace". Mã trả về của máy chủ dùng khóa `auth.invalidCredentials`, `auth.locked`, `auth.required` | — (cách kiểm lại: mở tệp trong tab Network/Sources, tìm `auth.locked`) |
| 24 | Cùng tệp, đoạn xử lý lỗi gọi API | Khi API trả **401** với mã `auth.required` thì giao diện phát sự kiện `bl:signed-out` → đưa về form đăng nhập. Khớp hành vi hai tab ở hàng 17 | — |
| 25 | Đang đăng nhập, mở link hồ sơ HL-000019, bấm **Sign out**; sau đó bấm nút **Back** của trình duyệt | Sau Sign out URL chuyển thành `/` và hiện form đăng nhập. Bấm Back → URL quay về link hồ sơ nhưng chỉ hiện **form đăng nhập**, không hiện dữ liệu hồ sơ (không thấy bản lưu tạm của trang đã đăng nhập) | 16 |
| 26 | (Người dùng gõ) Mã **chữ thường `p100001`** (mình điền sẵn, đã kiểm trước khi bấm) + mật khẩu đúng, đang ở link hồ sơ HL-000019 | **Đăng nhập thành công** (sign-in **200**), vào đúng hồ sơ HL-000019; thanh trên hiện `P100001` (chữ hoa). → mã nhân viên **không phân biệt hoa/thường** khi đăng nhập (mới thử với tài khoản P100001) | 17 |
| 27 | Sau Đăng xuất, điền `P100001`, **mật khẩu trống**, đặt con trỏ ở ô Mã nhân viên và nhấn **Enter** (không bấm nút) | Form **được gửi** (Enter gửi form); sign-in trả **400**; khung lỗi `Một số giá trị không hợp lệ.` + `validation.too_small (password)`. → mã đúng định dạng + mật khẩu trống cùng kết quả như hàng 5/6. Ô mã giữ `P100001` | 18 |

> **Ghi chú an toàn:** lượt thử hàng 19–21 gửi liên tiếp 10 lần đăng nhập sai/không hợp lệ nhằm kiểm tra định dạng mã nhân viên; mình không biết trước hệ thống có giới hạn số lần thử. Hệ quả: đăng nhập từ trình duyệt này bị chặn khoảng 5 phút kể từ 14:23 (có thể ảnh hưởng cả tài khoản thật cùng nguồn kết nối). Không đổi dữ liệu nào.

Văn bản trên màn hình đăng nhập (Tiếng Việt): `Đăng nhập` · `Mã nhân viên *` · gợi ý `Chữ P và 6 chữ số, ví dụ P100001.` · `Mật khẩu *` · nút `Đăng nhập` · chân trang `Banking Lite · Phiên bản 1.3.0`. English: `Sign in` · `Employee ID *` · `P followed by 6 digits, e.g. P100001.` · `Password *` · `Sign in` · `Banking Lite · Version 1.3.0`.

## 2. Cần người dùng làm (vì phải gõ mật khẩu) — chưa có kết quả
- A. ✅ Đã làm (mục 1, hàng 10, ảnh 08).
- B. ✅ Đã làm (hàng 11, ảnh 09): thông báo giống ca A.
- C. ✅ Đã làm (hàng 12, ảnh 10): vào thẳng hồ sơ.
- D. ✅ Đã gặp (ngoài ý muốn, hàng 21): chặn 5 phút sau nhiều lần thất bại. Còn cần: hết 5 phút thử lại; đăng nhập **đúng** trong lúc bị chặn có được không (người dùng gõ).

## 3. Chưa thử / không kiểm tra được
- Độ dài/ký tự cho phép của mật khẩu; chữ P thường (`p100001`) có được không; khoảng trắng thừa.
- Hết hạn phiên (bao lâu không thao tác thì bị đăng xuất).
- Đăng nhập hai **trình duyệt/máy khác nhau** cùng tài khoản (hai tab cùng trình duyệt đã thử, hàng 17).
- Cách giữ phiên (cookie/token) — không đọc được từ trang.
- Tài khoản P100002 (vai trò ❓).

## 4. Điểm chưa rõ (ứng viên cho SRS mục "chưa rõ")
1. Mã nhân viên sai định dạng (`abc123`) không bị báo lỗi định dạng khi mật khẩu trống. Chưa biết định dạng được kiểm khi nào (sau khi có mật khẩu? ở phía máy chủ?).
2. Lỗi hiển thị mã thô `validation.too_small (password)` thay vì câu dịch được (cùng kiểu với `validation.too_small (marketValue)` đã thấy ở Định giá).
3. Để trống cả hai ô chỉ báo password; không báo Employee ID dù ô đánh dấu `*` bắt buộc.
4. URL `/login` khi đã đăng nhập hiện Danh sách việc nhưng không đổi URL.
5. Chưa đăng nhập mà mở địa chỉ không tồn tại → vẫn hiện form đăng nhập (không phân biệt "chưa đăng nhập" và "không có trang").
6. Thông báo sai đăng nhập là `Mã không gian, mã nhân viên hoặc mật khẩu không đúng.` — nhắc "mã không gian" nhưng form không có ô đó (chưa rõ nghĩa; có thể là câu dịch chưa chuẩn). Cùng một câu cho cả "mã không tồn tại" và "sai mật khẩu" (che thông tin nào đúng/sai).
7. Sau khi đăng nhập đúng từ link hồ sơ, hệ thống quay lại đúng link đó (không về trang chủ). Chưa biết có áp dụng cho mọi link, và có chặn link của hồ sơ người khác theo vai trò không.
