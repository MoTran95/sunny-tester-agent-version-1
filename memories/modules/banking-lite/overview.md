# Banking Lite — tổng quan
Đọc khi: đầu tiên khi làm Banking Lite (`.du-an-hien-tai` = banking-lite).

- https://staging-banking-lite.vercel.app/ ("Banking Lite — Vay mua nhà", bản 1.3.0, giao diện Tiếng Việt/English), xử lý hồ sơ vay mua nhà `HL-xxxxxx`.
- Tài khoản test P100001, P200001, P300001; mật khẩu trong `.env`, khóa `BANKING_LITE_*`. Đăng nhập: "Mã nhân viên" (P + 6 số) + "Mật khẩu"; mình điền ô mã, người dùng gõ mật khẩu.
- Người dùng là tester, chưa biết hệ thống; khám phá theo tài khoản, luồng end-to-end, ảnh bằng chứng, không bịa.

| Loại | Đường dẫn |
|---|---|
| Memory | `memories/modules/banking-lite/` |
| SRS | `srs/banking-lite/` (`dang-nhap.md` = `LOGIN`, `khuyen-nghi-ltv-dsr.md` = `RECO`; mã `SUBMIT` giữ cho Gửi thẩm định, chưa có SRS) |
| Phân tích/checklist/test case | `testing/banking-lite/` |
| Bằng chứng, báo cáo HTML | `evidence/banking-lite/` |
| Ngữ cảnh khi làm báo cáo khám phá | `memories/modules/banking-lite/bao-cao-kham-pha-ngu-canh.md` |
- Bug: đang dùng thang mức độ mặc định của skill `tao-bug-report` (BUG-001…008); team có thang riêng thì khai file `thang-muc-do-bug.json` trong thư mục testing của dự án (2026-11-19).

## Sản phẩm cho người đọc (dời từ MEMORY.md 2026-11-19)
`testing/banking-lite/<feature>/` gồm `bang-soat-requirement.md`, `cau-hoi-cho-ba.md`, `test-case.md` (gộp cả checklist, từ 2026-11-19 cả `dang-nhap`), `truy-vet.md` (`dang-nhap` = LOGIN, `khuyen-nghi-ltv-dsr` = RECO: có `test-case.md` gộp 38 TC, không có `checklist.md`, thêm `phan-tich-requirement.md` cũ). `testing/banking-lite/regression-test.md` = bộ regression ba tầng (một file, truy vết bằng `truy-vet-regression.py`). `testing/banking-lite/smoke-test.md` = bộ smoke 7 case chọn từ LOGIN+RECO, **một file duy nhất** (mục tiêu ~15 phút, không cứng; chưa release note nên chưa có phần "Theo build"; case LOGIN-TC-001 còn `DEFAULT`: đã chốt ghi "Đạt kèm lỗi đã biết", không dừng build). Đọc trước khi làm checklist/test case feature đó. Banking Lite: `testing/banking-lite/test-plan.md` là file **sinh ra** từ `test-plan-nguon.txt` + `test-plan-thong-tin.json` (đừng sửa tay; chạy `.claude/skills/tao-test-plan/scripts/sinh-test-plan.py sinh banking-lite`); viết như bản thật gửi sếp, **không ghi kết quả test nào** (test plan là phần chưa test, dặn 2026-11-19); số ngưỡng tiêu chí, tên người, ngày, số bản Chrome, mã kế hoạch, công cụ bug còn `……………` chờ người dùng điền (không tự đặt). **Test plan không có logo** (dặn 2026-11-19; `docs_pages.py` `clean=True` cho file tên `test-plan*`/`_template-test-plan*`: không logo, không thanh điều hướng, không dòng "trang tự sinh", có nút In / Lưu PDF).
