# Feature “Đăng nhập” — kết quả khám phá
Cập nhật: 2026-11-17 · Liên quan: [exploration-findings.md](exploration-findings.md), [../../project/srs-process.md](../../project/srs-process.md)

Nhật ký đầy đủ + 10 ảnh: `evidence/banking-lite/features/dang-nhap/` (`bao-cao.md`, `screenshots/`). File này chỉ giữ điều cần nhớ. Đây là feature thử nghiệm đầu tiên cho bước “khám phá → SRS”.

## Điều học được (đã thấy)
- Sai mật khẩu **và** mã nhân viên không tồn tại cho **cùng một** thông báo: `Mã không gian, mã nhân viên hoặc mật khẩu không đúng.` Câu nhắc “mã không gian” dù form không có ô đó (❓ nghĩa gì).
- Để trống ô → `Some values are not valid.` + mã thô `validation.too_small (password)` (chỉ nhắc password, kể cả khi ID là `abc123` sai định dạng). Phần mã không được dịch sang tiếng Việt.
- Chưa đăng nhập mà mở link bất kỳ (hồ sơ, `/integrations`, địa chỉ không tồn tại) → hiện form đăng nhập, **giữ nguyên URL**. Đăng nhập đúng → quay lại đúng link hồ sơ đã mở.
- Đã đăng nhập mà mở `/login` → hiện Danh sách việc, URL vẫn `/login`.
- Ngôn ngữ lưu ở `localStorage` khóa `bl.locale` (`vi`/`en`), giữ qua tải lại và qua đăng xuất. Cách giữ phiên đăng nhập không đọc được từ trang (không có khóa trong storage; `document.cookie` rỗng).
- English: vai trò hiện `Banker` (Tiếng Việt: `Chuyên viên khách hàng`).

## Quan sát qua công cụ đọc mạng (không có ảnh; mở lại bằng Network của trình duyệt)
- `POST /api/auth/sign-in`: 400 (để trống / `abc123`), 401 (sai mật khẩu hoặc mã không tồn tại), 200 (đúng). `POST /api/auth/sign-out` 204. `GET /api/me`: 401 khi chưa đăng nhập, 200 khi đã đăng nhập. `GET /api/health` → `{"status":"ok","version":"1.3.0"}`.
- `/api/me` của P100001: `role: BANKER`, `workspace: DEFAULT`, 9 quyền (`application.view/create/capture/submit…`, `valuation.request/cancel`, `pricing.set`, `events.view`, `registry.search`). → `DEFAULT` trên thanh trên = workspace; “mã không gian” trong lỗi **có thể** là workspace (suy luận, chờ team).
- Công cụ không đọc được thân phản hồi lỗi của sign-in; **không đọc thân yêu cầu sign-in** (chứa mật khẩu).
- Hai tab cùng trình duyệt dùng chung phiên; đăng xuất ở tab này, tab kia chỉ bị đưa về form đăng nhập khi gọi API (401), không có thông báo. Đã đăng nhập + địa chỉ không tồn tại → vẫn Danh sách việc (không có trang 404).

## Giới hạn đăng nhập sai và kiểm tra ID (2026-11-17, vô tình kích hoạt)
- Mã nhân viên **không** bị kiểm định dạng ở phía máy chủ: `p999999`, khoảng trắng đầu/cuối, thiếu/thừa số, `X999999`, `P99999A`, `P99-999`, để trống ID (khi có mật khẩu) đều chỉ 401 + câu `Mã không gian, mã nhân viên hoặc mật khẩu không đúng.`. Chỉ mã rất dài (210 ký tự) bị 400 `validation.too_big (employeeId)` → có độ dài tối đa (chưa biết bao nhiêu).
- **Chặn tạm: sau 10 lần thất bại liên tiếp kể từ lần đăng nhập đúng (9×401 + 1×400; 11×401 nếu tính cả hai lần trước đó) → lần thứ 11 trả 429 “Too many failed attempts. Try again in 5 minutes.”** (14:23 17/11/2026). Xảy ra với mã không tồn tại → không chỉ theo tài khoản thật; chặn theo IP/trình duyệt/toàn hệ thống chưa biết.
- **Bài học:** mình đã vô tình kích hoạt chặn này khi thử các kiểu mã nhân viên. Quy tắc chung (tối đa 3 lần, rồi hỏi người dùng) nằm ở [../../user/working-preferences.md](../../user/working-preferences.md); chi tiết ở [../../pitfalls/dont-trigger-lockouts.md](../../pitfalls/dont-trigger-lockouts.md).

## Điều thêm về cuối phiên (2026-11-17)
- Đăng nhập đúng lúc đang bị chặn 429 vẫn thành công. Mã chữ thường `p100001` đăng nhập được (không phân biệt hoa/thường). Enter trong ô mã gửi form. Back sau đăng xuất chỉ hiện form, không lộ hồ sơ.
- Tệp giao diện `/assets/main.99595f2e.js` (tên băm đổi theo bản) chứa bảng thông báo VI/EN: `auth.invalidCredentials` EN = “Workspace, employee ID or password is incorrect.” (→ “mã không gian” = Workspace); `auth.locked` VI = “Đăng nhập sai quá nhiều lần. Thử lại sau {minutes} phút.”; `auth.required` = “Vui lòng đăng nhập.” (chưa thấy hiện). 401 + `auth.required` → giao diện phát `bl:signed-out`.
- SRS đã viết xong tại `srs/banking-lite/dang-nhap.md`; kết thúc phiên trình duyệt đang **đăng xuất**, giao diện Tiếng Việt.

## Phân tích requirement (2026-11-17, skill `phan-tich-requirement`)
Sản phẩm ở `testing/banking-lite/dang-nhap/`: `bang-soat-requirement.md` (39 đơn vị có mã + 6 mục không mã; 10 chỉ ✅, 25 cả hai, 4 chỉ ❓) và `cau-hoi-cho-ba.md` (A 5 / B 11 / C 9). **Chưa gửi BA; A1–A5 đã có TL-01…05 (xem mục dưới), thêm A6/B12/B13 (A 6 / B 13 / C 9, C6 bỏ).** Điều không suy ra nhanh được từ code/SRS:
- SRS `LOGIN` là bản nháp tả lại hệ thống, **không phải yêu cầu của BA** → “✅ đã rõ” chỉ nghĩa “hệ thống đang làm vậy”. Đã nói rõ ở đầu hai file; cần xin tài liệu chính thức.
- **Ngưỡng chặn “10 lần” lệch tùy cách đếm** (tính lại từ nhật ký hàng 14, 18–21): 9 (chỉ 401, đếm lại khi đúng), 10 (tính cả 400, đếm lại), 11 (chỉ 401, không đếm lại), 14 (tính cả 400, không đếm lại). SRS ghi “10” như đã chắc và R06 tự mâu thuẫn (“kể từ lần đăng nhập đúng gần nhất” vs “có đặt lại không: chưa rõ”). → câu A2.
- Mật khẩu 3 ký tự sai chỉ bị 401 (không `too_small`) → mức tối thiểu ≤ 3. Ô Mật khẩu **giữ chữ** sau khi báo lỗi (nhật ký hàng 10) nhưng SRS không ghi → B9.
- SRS tự lệch nhỏ: S02-AC04 xếp `p999999` vào “sai dạng” trong khi chữ thường được chấp nhận; S03-AC02 nói cả `too_small`/`too_big` giữ tiếng Anh nhưng M04 cột English “chưa quan sát”.
- Phần C có 2 mục (C1 khoảng trắng với mã thật, C6 mã 210 ký tự bản English) **có lần nhập sai → có thể tính vào giới hạn chặn**; chưa biết bộ đếm hiện còn bao nhiêu. Chỉ làm khi báo người dùng trước, tối đa 3 lần cộng cả hai ([../../pitfalls/dont-trigger-lockouts.md](../../pitfalls/dont-trigger-lockouts.md)). Chờ hết 5 phút để kiểm chặn tự hết (B3) cũng cần lần sai → để hỏi BA thay vì tự thử.

## Câu trả lời A1–A5 đã nhận (2026-11-18, TL-01…TL-05 trong bảng soát)
Người dùng xác nhận **BA trả lời** (chuyển lại trong chat, chưa có link ticket/kênh chung) → các dòng khác hệ thống là **nghi lỗi**, chưa phải lỗi đã xác nhận. Chưa sửa SRS (chỉ sửa khi BA/team xác nhận). Nội dung:
- Đang bị chặn thì **không** vào được kể cả nhập đúng; hết chặn sau 5 phút tính từ lúc bị chặn → **khác hệ thống** (đang cho vào).
- 10 lần sai liên tiếp là chặn, mọi loại lỗi đều tính → khớp hệ thống. Lệch một lần: BA nói lần sai thứ 10 đã báo bị chặn (TL-11), hệ thống báo sai thông tin ở 10 lần đầu, lần thứ 11 mới chặn. Đăng nhập đúng đưa số lần về 0, chỉ tính số lần không tính thời gian (TL-06).
- Mọi ca sai/trống/quá dài chỉ báo “mã nhân viên hoặc mật khẩu không đúng”; không còn “Một số giá trị không hợp lệ.” và dòng `validation…` → **khác hệ thống**. Nguyên văn + English chưa có (→ B13).
- Chữ p hoa/thường đều được; khoảng trắng đầu/cuối “tự cắt bỏ” (ô chọn gửi lại **chưa đánh dấu rõ**, mình hiểu là tự cắt bỏ); độ dài mã không quy định ở màn đăng nhập → hệ thống từ chối mã 210 ký tự là **khác**.
- “Mã không gian”/Workspace bị bỏ → câu báo và thanh trên (`DEFAULT`, `/api/me`) còn → **khác**; chưa nói thanh trên có bỏ theo (→ B12).
- Hệ quả cho việc test: **C6 bỏ** (không còn `too_big` → bớt một lần nhập sai); C1, C3 chỉ còn là kiểm hệ thống có làm đúng. Bộ đếm hiện còn bao nhiêu vẫn không biết nên quy tắc tối đa 3 lần nhập sai vẫn giữ.
- **Đợt 2 (cùng ngày):** TL-06 (A6): đăng nhập đúng xen giữa đưa số lần sai về 0, chỉ tính số lần, không tính thời gian; lần sai thứ 10 báo bị chặn (TL-11, phần cuối A6, **khác** hệ thống một lần). TL-07 (B12): bỏ `DEFAULT` trên thanh trên và `workspace` trong `/api/me` (hệ thống còn → khác). TL-08 (B13): câu báo VI “Mã nhân viên hoặc mật khẩu không đúng.”, EN “Employee ID or password is incorrect.”. TL-09 (B3): hết 5 phút là hết chặn, nhập thêm lúc bị chặn không tính, sau đó nhập sai mới đếm lại số lần (chưa kiểm hệ thống). TL-10 (B1): mã không tồn tại và sai mật khẩu dùng chung một câu (khớp). Còn mở: B2, B4–B11 và 8 mục tự kiểm tra; Người trả lời đã xác nhận là BA. “Tự cắt bỏ” khoảng trắng đã được người dùng xác nhận (2026-11-18).
- Bảng soát có hai kiểu dòng cho cùng một mã: dòng ✅ cũ ghi “hành vi hiện tại, khác TL-xx” và dòng “theo TL-xx” là kết quả đúng. Đừng đếm 13 đơn vị “khác” thành 13 lỗi (có thể chung nguyên nhân, và chỉ là nghi lỗi nếu BA xác nhận).

## Chưa thử
Sai mật khẩu nhiều lần (nguy cơ khóa tài khoản test — hỏi người dùng trước), chữ P thường, khoảng trắng, hết hạn phiên, hai tab, đăng nhập P100002.

## Bẫy khi test feature này
- Không tự gõ mật khẩu **kể cả mật khẩu sai** (người dùng đã thử thuyết phục, vẫn giữ quy tắc). Cách làm đã chạy tốt: mình điền sẵn **Mã nhân viên** bằng `form_input`, người dùng gõ mật khẩu và bấm, báo “xong”, mình đọc kết quả và chụp ảnh.
- Cửa sổ trình duyệt bị ẩn thì người dùng không thấy gì: dùng `mcp__ccd_view__show_pane` (pane `preview`) để bật lại.
- Bấm Đăng xuất làm mất phiên P100001 sẵn có; người dùng phải đăng nhập lại.
