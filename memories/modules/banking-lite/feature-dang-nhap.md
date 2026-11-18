# Banking Lite — Đăng nhập (`LOGIN`)
Đọc khi: làm SRS/bảng soát/checklist/test case/truy vết `LOGIN`. Chi tiết: `evidence/banking-lite/features/dang-nhap/` (nhật ký, ảnh), `srs/banking-lite/dang-nhap.md`, `testing/banking-lite/dang-nhap/`.

## Trạng thái (2026-11-18)
- BA xác nhận đúng TL-01…13 (chưa có ticket). **SRS `LOGIN` nay là yêu cầu theo BA**: cột "Yêu cầu: hệ thống phản hồi" + cột "Hệ thống 1.3.0 hiện tại" (`Khớp` / `⚠️ Khác` = nghi lỗi). Bỏ: S03-AC02, M02, M03, M04. Mốc trước khi sửa: commit `46feb45`. (Trước 2026-11-17 SRS chỉ là bản quan sát.)
- **TL-14 (2026-11-18, BA qua người dùng): B8 thời hạn phiên = 10 phút.** SRS thêm `S01-AC09` (chưa kiểm hệ thống, cần chờ 10 phút), Q10 trả lời một phần. **TC-042 (chờ 9 phút, còn đăng nhập) và TC-043 (chờ 10 phút 30 giây, hết hạn; màn hình hiện gì = CẦN XÁC NHẬN, câu 4 → B15)** đã thêm 2026-11-18, người dùng chọn 2 ca; `chot` rồi (43 TC còn đúng). Ca vừa thao tác vừa chờ quá 10 phút chưa viết (chưa rõ cách tính, B15).
- Câu hỏi BA còn mở: **B4** (câu báo + số phút khi nhập lúc đang bị chặn), **B15** (10 phút tính từ lúc đăng nhập hay từ lần thao tác cuối; màn hình khi hết hạn; nảy ra từ B8) + 8 mục tự kiểm tra (C1–C3 chỉ còn kiểm hệ thống). Bỏ: B5–B7, B9–B11, B14, C6. A7, A8 không gửi BA (người dùng chốt TL-12, TL-13).
- Checklist 43 dòng (TC-001…043; TC-042/043 thêm sau, xếp cuối bảng, khai báo ở bảng đầu checklist, chỉ phần đã chốt, mã nguồn bỏ tiền tố `LOGIN-`); test case 12 cột, 43 TC, **chưa chạy ca nào**, chưa ca có script `auto/`. Ca khóa tài khoản (TC-014, 015, 021, 022, 037) ghi Không tự động được. Ca chạm ngưỡng 10 lần (TC-014…022) chỉ chạy khi người dùng đồng ý (tối đa 3 lần sai).
- 3 câu BA mới từ test case: (1) câu báo/số phút khi nhập lúc bị chặn (= B4, TC-016…018); (2) lần sai của tài khoản khác xen giữa có làm đứt chuỗi "liên tiếp" không (TC-022); (3) `2,000,000,000` hiện ở đâu (TC-039). Mật khẩu đúng không ghi trong tài liệu.
- Truy vết: `truy-vet.md` (tự sinh) + `truy-vet-cau-hinh.json` (tên ngắn 52 mã) + `truy-vet-trang-thai.json`. Xem `project/truy-vet-requirement.md`.

## Hành vi đã thấy ở hệ thống 1.3.0
- Sai mật khẩu và mã không tồn tại: cùng câu `Mã không gian, mã nhân viên hoặc mật khẩu không đúng.` (EN `Workspace, employee ID or password is incorrect.`).
- Trống ô → `Some values are not valid.` + `validation.too_small (password)` (chưa dịch). Mã 210 ký tự → 400 `validation.too_big (employeeId)`. Mã không bị kiểm định dạng phía máy chủ (`p999999`, khoảng trắng, `X999999`… đều 401). Chữ thường `p100001` đăng nhập được. Mật khẩu 3 ký tự sai chỉ 401.
- Chưa đăng nhập mở link bất kỳ → form đăng nhập giữ URL; đăng nhập đúng quay lại link đó. Đã đăng nhập mở `/login` → Danh sách việc, URL vẫn `/login`. Địa chỉ không tồn tại khi đã đăng nhập → Danh sách việc (không có 404). Back sau đăng xuất chỉ hiện form.
- Ô Mật khẩu **giữ chữ** sau khi báo lỗi (nghi lỗi theo bảo mật, bảng soát).
- Ngôn ngữ ở `localStorage` `bl.locale` (`vi`/`en`), giữ qua đăng xuất. English: vai trò `Banker` (VI `Chuyên viên khách hàng`). Phiên đăng nhập không đọc được từ trang (không có storage, `document.cookie` rỗng). Hai tab chung phiên; tab kia chỉ về form khi gọi API 401, không báo.
- API: `POST /api/auth/sign-in` 400/401/200; `sign-out` 204; `GET /api/me` 401 / 200; `GET /api/health` → `{"status":"ok","version":"1.3.0"}`. `/api/me` P100001: `role: BANKER`, `workspace: DEFAULT`, 9 quyền. Không đọc được thân phản hồi lỗi sign-in; **không đọc thân yêu cầu sign-in** (chứa mật khẩu).
- Tệp giao diện `/assets/main.<băm>.js` (băm đổi theo bản) chứa bảng thông báo: `auth.invalidCredentials`, `auth.locked` VI "Đăng nhập sai quá nhiều lần. Thử lại sau {minutes} phút.", `auth.required` "Vui lòng đăng nhập." 401 + `auth.required` → phát `bl:signed-out`.
- **Chặn tạm:** sau chuỗi thất bại liên tiếp (lần kích hoạt 2026-11-17 14:23: 9×401 + 1×400, lần 11 → 429 "Too many failed attempts. Try again in 5 minutes."). Xảy ra với mã không tồn tại (không chỉ tài khoản thật). Đăng nhập đúng lúc đang bị chặn **vẫn thành công** (hệ thống; BA nói phải bị chặn → khác). Nhật ký hàng 19: gõ mã khác nhau vẫn bị chặn → hệ thống không đếm riêng từng mã (đừng đoán "đếm theo mã"). Ngưỡng lệch tùy cách đếm: 9 / 10 / 11 / 14.

## Yêu cầu theo BA (TL) — tóm tắt
| TL | Nội dung | Với hệ thống |
|---|---|---|
| 01 | Đang bị chặn thì không vào được kể cả nhập đúng; hết chặn sau 5 phút kể từ lúc bị chặn | Khác (đang cho vào) |
| 02 | 10 lần sai liên tiếp là chặn, mọi loại lỗi đều tính | Khớp; lệch 1 lần (TL-11) |
| 03 | Mọi ca sai/trống/quá dài chỉ báo "Mã nhân viên hoặc mật khẩu không đúng"; không còn `Some values are not valid` / `validation…`. Lý do: **bảo mật** | Khác |
| 04 | Chữ p hoa/thường đều được; khoảng trắng đầu/cuối tự cắt; không quy định độ dài mã ở màn đăng nhập | Khác với mã 210 ký tự |
| 05 | Bỏ "mã không gian"/Workspace khỏi câu báo | Khác |
| 06 | Đăng nhập đúng xen giữa đưa số lần sai về 0; chỉ tính số lần, không tính thời gian | |
| 07 | Bỏ `DEFAULT` trên thanh trên và `workspace` trong `/api/me` | Khác |
| 08 | VI "Mã nhân viên hoặc mật khẩu không đúng." / EN "Employee ID or password is incorrect." | |
| 09 | Hết 5 phút là hết chặn; nhập thêm lúc bị chặn không tính; sau đó nhập sai mới đếm lại | chưa kiểm |
| 10 | Mã không tồn tại và sai mật khẩu dùng chung một câu | Khớp |
| 11 | Lần sai thứ 10 đã báo bị chặn | Khác 1 lần |
| 12 | Chặn đúng tài khoản nhập sai (người dùng chốt) | |
| 13 | Mật khẩu không có khoảng trắng, phân biệt hoa thường (người dùng chốt) | |
| 14 | Thời hạn phiên 10 phút (chưa rõ tính từ đâu → B15) | chưa kiểm |
- 13 đơn vị "khác" ≠ 13 lỗi (có thể chung nguyên nhân; chỉ là nghi lỗi tới khi BA xác nhận). Bảng soát có hai kiểu dòng cho cùng mã: dòng ✅ cũ "hành vi hiện tại, khác TL-xx" và dòng "theo TL-xx" là đúng. Nhãn "✅ Suy ra từ <mã>" (7 đơn vị). "Tự cắt bỏ" khoảng trắng: người dùng xác nhận 2026-11-18.

## Quy tắc người dùng đưa ra khi làm LOGIN
- **Requirement ghi rõ thì suy luận tiếp, ghi chưa rõ thì hỏi.** Người dùng chê A7, A8, B14 "vô tri". Không hỏi: độ dài mã (đăng nhập chỉ báo đúng/sai), A6 (suy từ chữ "10 lần liên tiếp"), B5, B6, B7, B9, B10, B11.
- Mỗi đợt TL xong **soát lại** chứ không chỉ đổi ❓→✅ (lần này sinh A7, A8, B14, viết lại B4).
- Checklist chỉ viết từ dòng đã chốt, không lập "Câu hỏi cho BA" mới. Test case: mỗi case một giá trị không hợp lệ (checklist gộp nhiều giá trị thì dùng giá trị đầu và ghi nhận riêng), không có mã R/TL trong cột Kết quả.
- Tổng kết bảng soát tính bằng script đếm cột Trạng thái (từng đếm sai 8 vs 9).
- Mục C có lần nhập sai (C1 khoảng trắng với mã thật…) → có thể tính vào bộ đếm; chưa biết bộ đếm còn bao nhiêu → chỉ làm khi báo người dùng, tối đa 3 lần cộng cả hai (`pitfalls/dont-trigger-lockouts.md`). Chờ hết 5 phút để kiểm chặn tự hết cũng cần lần sai → hỏi BA thay vì tự thử.

## Chưa thử trên hệ thống
Sai mật khẩu nhiều lần, hết hạn phiên (chờ 10 phút, không cần nhập sai), hai tab đầy đủ, đăng nhập P100002.

## Bẫy khi test
- Không tự gõ mật khẩu **kể cả sai**. Cách tốt: mình điền Mã nhân viên bằng `form_input`, người dùng gõ mật khẩu + bấm, báo "xong", mình đọc kết quả + chụp ảnh.
- Pane trình duyệt ẩn thì người dùng không thấy gì: `mcp__ccd_view__show_pane` (pane `preview`).
- Bấm Đăng xuất làm mất phiên P100001; người dùng phải đăng nhập lại. Cuối khám phá trình duyệt đang đăng xuất, giao diện Tiếng Việt.
