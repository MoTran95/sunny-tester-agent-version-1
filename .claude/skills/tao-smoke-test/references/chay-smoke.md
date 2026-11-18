# Chạy smoke trên hệ thống (giao thức)

Đọc khi người dùng nhờ chạy smoke. Quy trình chọn case nằm ở `SKILL.md`.

Chỉ chạy khi người dùng nhờ ("chạy smoke", "chạy thử smoke trên build này"); không tự chạy.

**Trước khi chạy (hỏi một lần cho cả lượt):**
- Môi trường và địa chỉ hệ thống nào; người dùng đồng ý chạy trên hệ thống thật.
- Dữ liệu sẽ bị đổi (vd tạo hồ sơ nháp của chính họ): đồng ý tạo, và dọn lại sau lượt nếu case gốc yêu cầu.
- **Mật khẩu: AI không gõ.** Người dùng đăng nhập, hoặc tự chạy script lưu phiên của dự án nếu có (Banking Lite: `scripts/dang-nhap-tu-dong.py <mã>`; phiên hết hạn sau 10 phút nên smoke dài phải đăng nhập lại, mỗi tài khoản một phiên). AI chỉ điền ô mã nhân viên.
- Không nhập sai thông tin đăng nhập, không làm gì có thể khóa tài khoản (`memories/pitfalls/dont-trigger-lockouts.md`).

**Chạy từng case, theo thứ tự bảng:**
1. Đọc case gốc một lần: `python -X utf8 scripts/truy-vet.py tra <dự-án> <tính-năng> --ma TC-005 --day-du` (không mở cả file). Làm đúng điều kiện, bước, dữ liệu của case gốc; chỉ cần đạt các bước nêu ở cột "Đạt khi" của bảng tiêu chí.
2. Đọc kết quả bằng văn bản trang (`get_page_text`/`read_page`) trước; chụp ảnh chỉ khi Không đạt hoặc cần bằng chứng (đỡ token).
3. Chấm theo **ý chính**: `Đạt`; `Đạt kèm lỗi đã biết` (chỉ khi bảng tiêu chí ghi ngoại lệ cho đúng case đó và chỉ ý được miễn sai); `Không đạt`; `Bị chặn` (không chạy được vì lý do ngoài case: hết phiên, mất mạng…). Ý phụ lệch thì chỉ ghi nhận.
4. **Không đạt thì dừng ngay**, các case sau để `Chưa chạy`. Nếu nghi do thao tác của mình (nhất là lượt hiệu chuẩn) thì làm lại **một** lần cẩn thận; vẫn lệch thì kiểm lại test case gốc với requirement trước khi kết luận build sai. Không thử lại nhiều lần.
5. Ghi quan sát cụ thể (chữ, số thấy trên màn hình) cho case Không đạt và ngoại lệ; không bịa kết quả chưa thấy.

**Sau lượt chạy:** `python -X utf8 scripts/truy-vet-smoke.py ghi-luot <dự-án> --build "<số bản đọc ở chân trang>" --ket-qua "1=Đạt,2=Đạt kèm lỗi đã biết,3=Không đạt" --ghi-chu "…"` (số là cột # của bảng; case không nêu = Chưa chạy; script tự tính Nhận/Trả build và ghi một dòng vào mục "Lượt chạy"). Rồi báo người dùng: nhận hay trả build, case lỗi và quan sát, ngoại lệ đã dùng, phạm vi chưa phủ. Muốn tạo bug thì hỏi người dùng rồi dùng `tao-bug-report`; không tự tạo.

**Lượt hiệu chuẩn** (lần đầu, hoặc test case chưa chạy thật): chạy cùng người dùng và ghi thêm kết quả vào cột `Kết quả thực tế` + `Trạng thái` của test case gốc (không làm test case bị coi là đã sửa); case sai vì test case sai thì sửa test case theo `tao-checklist-test-case`. Rồi lưu script tự động cho case "Nên" vào cột `Tự động hóa` của test case gốc (`Có: <đường dẫn>`, chỉ ghi khi script đã chạy được, không chứa mật khẩu). **Lượt build thường không ghi đè** các cột của test case (giữ kết quả chạy sâu), chỉ ghi vào mục "Lượt chạy".

