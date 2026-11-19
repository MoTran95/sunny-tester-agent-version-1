# Kế hoạch re-test BUG-001: thanh điều hướng vẫn hiện chữ `DEFAULT`

Bug: [BUG-001](../bug/BUG-001.md) · Mức độ nghiêm trọng: Rất nhỏ · Ưu tiên đề xuất: Thấp.
Build có bản sửa: [chưa có số build] (chờ bản mới; bản lúc tạo bug và lượt re-test 2026-11-19 đều là 1.3.0).
Môi trường: https://staging-banking-lite.vercel.app/ (địa chỉ cũ `banking-lite.vercel.app` đã gỡ).
Chạy bằng script: `python -X utf8 scripts/run_tests.py --case-id dang-nhap/retest-bug-001 --bug-build 1.3.0` (đăng nhập trước bằng `scripts/auto_login.py P100001 P200001 P300001 --headless`).

| Mã bug | Bước tái hiện cần làm lại | Biến thể nên thử | Bằng chứng cần lưu | Đạt thì / Không đạt thì |
|---|---|---|---|---|
| **BUG-001** | Làm đúng bước 1–5 của [TC-001](../test-case.md#tc-001), lần lượt đủ 3 tài khoản trong Phạm vi ảnh hưởng, mỗi tài khoản một lượt đăng nhập riêng:<br>**(a)** `P100001`: nhìn thanh điều hướng, phải là `P100001 · Chuyên viên khách hàng`, không có `DEFAULT`.<br>**(b)** `P200001`: phải là `P200001 · Chuyên viên định giá`, không có `DEFAULT`.<br>**(c)** `P300001`: phải là `P300001 · Chuyên viên thẩm định tín dụng`, không có `DEFAULT`, và vẫn còn menu `Tích hợp`.<br>Mỗi lượt: mở trang chưa đăng nhập, nhập mã và mật khẩu đúng (người test hoặc script đọc `.env`), bấm `Đăng nhập`, chờ `Danh sách việc` tải xong rồi mới nhìn. | 1. Mở `/api/me` sau đăng nhập `P100001`: trường `workspace` (giá trị `DEFAULT`) phải biến mất. Yêu cầu TL-07 đòi bỏ cả hai chỗ nhưng bug chưa kiểm chỗ này, nên không tính vào điều kiện đóng; lệch thì ghi riêng.<br>2. Bấm `English` rồi nhìn lại thanh điều hướng: vai trò là `Banker`, không có `DEFAULT`; bấm lại `Tiếng Việt` cũng vậy.<br>3. Tải lại trang (F5) khi đang đăng nhập: thanh điều hướng vẫn không có `DEFAULT`. (Phần "mở một màn hình khác" chưa có đường dẫn đã biết: làm tay.) | Ảnh toàn thanh điều hướng của từng tài khoản (3 ảnh) kèm chữ đọc được nguyên văn; số build đọc ở chân trang và ở `/api/health`; địa chỉ đã test; biến thể 1: kết quả `/api/me` có hay không có `workspace`; biến thể 2, 3: một ảnh mỗi biến thể; kết quả chạy `result-*.json`; video nếu không đạt. | **Đạt** khi cả 3 tài khoản (`P100001`, `P200001`, `P300001`) không còn `DEFAULT` và phần còn lại của TC-001 vẫn đúng (vào `Danh sách việc`, mã và vai trò đúng, không có thông báo "đăng nhập thành công"): chuyển **Đóng**. Biến thể sai thì ghi bug mới, không giữ bug này mở.<br>**Không đạt** khi còn `DEFAULT` ở một tài khoản bất kỳ, hoặc mã và vai trò sai: **Mở lại** kèm số build, tài khoản còn lỗi và ảnh tô đỏ. Còn một chỗ chưa đạt thì chưa đóng. |

## Gợi ý vùng cần regression sau khi re-test xong
- **Đăng nhập cơ bản:** smoke số 2 (TC-001) và RG-02 trong Tầng 1; hai ca đang ghi "Đạt kèm lỗi đã biết", đổi sang Đạt khi bug đóng.
- **Câu báo lỗi đăng nhập:** BUG-002 cùng nhóm bỏ `workspace` (TL-05, TL-07); kiểm câu báo sai mật khẩu không bị hỏng.
- **Vai trò và menu theo tài khoản:** TC-002 (ba vai trò, `P300001` có thêm menu `Tích hợp`).
- **Chuyển ngôn ngữ:** vai trò hiển thị đúng ở Tiếng Việt và English.
- **Các màn hình dùng thông tin người đăng nhập:** TC-003, TC-004.
