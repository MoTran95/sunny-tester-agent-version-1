# Banking Lite — tổng quan
Đọc khi: đầu tiên khi làm Banking Lite (`.du-an-hien-tai` = banking-lite).

- https://staging-banking-lite.vercel.app/ ("Banking Lite — Vay mua nhà", bản 1.3.0, giao diện Tiếng Việt/English), xử lý hồ sơ vay mua nhà `HL-xxxxxx`.
- Tài khoản test P100001, P200001, P300001; mật khẩu trong `.env`, khóa `BANKING_LITE_*`. Đăng nhập: "Mã nhân viên" (P + 6 số) + "Mật khẩu"; mình điền ô mã, người dùng gõ mật khẩu.
- Người dùng là tester, chưa biết hệ thống; khám phá theo tài khoản, luồng end-to-end, ảnh bằng chứng, không bịa.

| Loại | Đường dẫn |
|---|---|
| Memory | `memories/modules/banking-lite/` |
| SRS | `srs/banking-lite/` (`dang-nhap.md` = `LOGIN`, `khuyen-nghi-ltv-dsr.md` = `RECO`) |
| Phân tích/checklist/test case | `testing/banking-lite/` |
| Bằng chứng, báo cáo HTML | `evidence/banking-lite/` |
| Ngữ cảnh riêng của skill báo cáo | `.claude/skills/feature-exploration-report/references/banking-lite-context.md` |
