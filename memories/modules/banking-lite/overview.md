# Dự án Banking Lite — tổng quan
Cập nhật: 2026-11-18 · Liên quan: [exploration-findings.md](exploration-findings.md), [tu-ngu-cau-hoi-ba.md](tu-ngu-cau-hoi-ba.md)

Slug dự án: `banking-lite`. Chỉ đọc file này khi dự án hiện tại là Banking Lite (xem `memories/conventions/nhieu-du-an.md`).

## Hệ thống
- https://banking-lite.vercel.app/ ("Banking Lite — Vay mua nhà", bản 1.3.0, giao diện Tiếng Việt/English). Xử lý hồ sơ vay mua nhà `HL-xxxxxx`.
- Tài khoản test: P100001, P200001, P300001 (mật khẩu trong `.env`, khóa bắt đầu bằng `BANKING_LITE_`).
- Đăng nhập: "Mã nhân viên" (chữ P + 6 số) và "Mật khẩu". Claude điền sẵn ô Mã nhân viên, người dùng tự gõ mật khẩu.

## Bối cảnh (2026-11-17)
- Người dùng là tester, chưa biết gì về hệ thống. Yêu cầu: khám phá chức năng theo từng tài khoản, ghi luồng end-to-end, sơ đồ Mermaid, ảnh bằng chứng. Không bịa; chỗ chưa rõ thì hỏi.

## Thư mục của dự án
| Loại | Đường dẫn |
|---|---|
| Bộ nhớ | `memories/modules/banking-lite/` |
| SRS | `srs/banking-lite/` (`dang-nhap.md` = `LOGIN`, `khuyen-nghi-ltv-dsr.md` = `RECO`) |
| Phân tích requirement | `testing/banking-lite/` |
| Bằng chứng, báo cáo HTML | `evidence/banking-lite/` |
| Ngữ cảnh riêng trong skill báo cáo HTML | `.claude/skills/feature-exploration-report/references/banking-lite-context.md` |

## Việc cần làm tiếp
_Điền khi có._
