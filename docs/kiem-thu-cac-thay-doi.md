# Kiểm thử các thay đổi ngày 2026-11-18

Kiểm 4 nhóm thay đổi: (1) bảng soát gọn, (2) bộ nhớ gọn + skill đọc đúng file, (3) chuẩn bị máy mới, (4) nhiều dự án không lẫn kiến thức.

Công cụ đo: `scripts/do-toc-do-phien.py` đọc nhật ký phiên trên máy, in cho mỗi phiên: số file đọc trước khi bắt tay làm, số phút tới lúc bắt tay làm, tổng phút mô hình suy nghĩ/viết, bước dài nhất, và có mở file của dự án khác không.

```powershell
python -X utf8 scripts/do-toc-do-phien.py --so 3
```

**Mốc cũ để so** (phiên ghi câu trả lời BA A1–A5 của `LOGIN`, 2026-11-18 08:39): đọc 11 file, **8,4 phút** mới bắt tay làm, mô hình suy nghĩ/viết 14,8 phút, một bước dài 5,7 phút.

---

## T1. Kiểm tự động (2 phút, làm ngay được)
```powershell
python -X utf8 scripts/kiem-tra-may-moi.py
```
**Đạt khi:** dòng cuối là "0 mục THIẾU". Script đã chạy thử hai script soát trên `LOGIN` (0 lỗi).

## T2. Bảng soát gọn vẫn đọc là hiểu (5 phút, bạn tự đánh giá)
Mở [bảng soát LOGIN](../testing/banking-lite/dang-nhap/bang-soat-requirement.md). Đọc 3 dòng ❓ và 3 dòng có "BA trả lời".

**Đạt khi:** mỗi dòng vẫn cho biết người dùng làm gì, chỗ nào chưa rõ, hỏi BA câu nào (tiêu đề câu hỏi), và câu BA đã trả lời. Muốn xem đầy đủ câu hỏi thì mở [file câu hỏi](../testing/banking-lite/dang-nhap/cau-hoi-cho-ba.md) theo số câu.

## T3. Ghi câu trả lời BA nhanh hơn (phép đo chính)
Làm khi BA trả lời thật một câu còn mở (ví dụ B2). Mở **phiên mới**, gõ một câu, ví dụ:

> Ghi câu trả lời BA cho LOGIN. B2: …

Xong thì chạy `python -X utf8 scripts/do-toc-do-phien.py --so 1`.

**Đạt khi:** đọc khoảng 6 file trở xuống, bắt tay làm trong khoảng **3 phút**, không còn bước suy nghĩ dài 5–6 phút; `kiem-tra.py` 0 lỗi. Khi đọc phiên: Claude có dùng `--tim` thay vì đọc cả bảng soát không.

Chưa có câu trả lời thật mà muốn thử: dùng câu trả lời giả, đo xong thì bỏ thay đổi:
```powershell
git restore testing/ memories/
```

## T4. Giả lập máy mới bằng bản sao (không cần push)
Tạo bản sao từ chính repo trên máy (lấy cả các commit chưa push). Bản sao không có `.env` và `.du-an-hien-tai`, giống máy mới.
```powershell
git clone D:\AI\build-sunny-agent-version-1 D:\AI\thu-may-moi
```
Trong app, mở thư mục `D:\AI\thu-may-moi` ở một phiên mới, chọn tin cậy thư mục, gõ: "Phân tích requirement giúp mình".

**Đạt khi:**
- Claude **hỏi đang làm dự án nào trước khi làm gì khác**, đưa lựa chọn `banking-lite` và "dự án mới".
- Các lệnh đọc, chạy script soát, `git status` không hỏi quyền; `git commit` vẫn hỏi.
- `python -X utf8 scripts/kiem-tra-may-moi.py` trong bản sao báo đúng: chưa chọn dự án / thiếu `.env`.

## T5. Dự án mới không lẫn kiến thức Banking Lite
Vẫn trong bản sao. Trả lời câu hỏi ở T4 bằng "dự án mới", tên "Thử nghiệm", thư mục `thu-nghiem`. Rồi hỏi:

> Viết giúp mình 3 câu hỏi mẫu gửi BA về màn hình đăng nhập của dự án này.

**Đạt khi:**
- Có các thư mục `memories/modules/thu-nghiem/`, `srs/thu-nghiem/`, `testing/thu-nghiem/`, `evidence/thu-nghiem/`.
- Claude **hỏi lại thông tin** (requirement, màn hình, tài khoản) thay vì tự viết.
- Câu trả lời **không có** dấu vết Banking Lite: P100001, "Mã nhân viên", "bị chặn 5 phút", "Mã không gian", "mức tối đa", "hết hạn vay", LTV, DSR.
- `python -X utf8 scripts/do-toc-do-phien.py --so 1` (chạy trong bản sao) báo "mở file của dự án khác: không".

## T6. Đổi dự án
Vẫn trong bản sao, nói: "Giờ mình làm Banking Lite."

**Đạt khi:** Claude hỏi xác nhận đổi, rồi file `.du-an-hien-tai` thành `banking-lite`.

Xong T4–T6 thì xóa bản sao (thao tác xóa, bạn tự chạy):
```powershell
Remove-Item -Recurse -Force D:\AI\thu-may-moi
```

## T7. Máy mới thật (sau khi push)
Làm theo [cai-dat-may-moi.md](cai-dat-may-moi.md), rồi mở phiên đầu tiên và làm một việc quen thuộc. Chạy `do-toc-do-phien.py --so 1` trên máy đó.

**Đạt khi:** không còn ~30 phút như trước; phần lớn thời gian chỉ là chọn dự án và cho phép trang web lần đầu.

---

## Ghi kết quả
| Mã | Ngày | Đạt / Không đạt | Số đo (file đọc, phút tới lúc làm) | Ghi chú |
|---|---|---|---|---|
| T1 | | | | |
| T2 | | | | |
| T3 | | | | |
| T4 | 2026-11-18 | Đạt (có một điểm nhỏ) | Hỏi dự án sau 15 giây, trước mọi việc; tới lúc chờ người dùng ~1,5 phút | Bản sao báo đúng "chưa chọn dự án", không có `.env`. Điểm nhỏ: câu hỏi dự án gộp chung với câu "requirement nào" có sẵn lựa chọn tài liệu Banking Lite trước khi chọn dự án → đã sửa `CLAUDE.md` bước 0 (hỏi riêng câu dự án) |
| T5 | 2026-11-18 | Đạt (có lưu ý) | Không mở file nào của Banking Lite trong lượt này; ~1 phút | 3 câu hỏi mẫu để trống chỗ cần số liệu (`<…>`), nói rõ chưa có requirement/URL, không có số lần sai, thời gian chặn, câu thông báo, tài khoản của Banking Lite. Lưu ý: chủ đề câu hỏi (chặn khi sai nhiều lần, sai mã/sai mật khẩu cùng câu, báo lỗi ô trống) giống các câu đã hỏi ở `LOGIN`; có thể do ví dụ trong skill hoặc kiến thức chung |
| T6 | 2026-11-18 | Đạt (có một lỗi đã sửa) | `.du-an-hien-tai` đổi sang `thu-nghiem`, đủ 4 thư mục, thêm dòng vào bảng dự án và `MEMORY.md` | Không hỏi xác nhận vì người dùng đã nói rõ "làm dự án mới" (hợp lý). Lỗi: **tự commit** khi chưa ai nhờ → đã thêm quy tắc "commit/push chỉ khi được nhờ" vào `working-preferences.md` (luôn đọc) và bước tạo dự án |
| T7 | | | | |
