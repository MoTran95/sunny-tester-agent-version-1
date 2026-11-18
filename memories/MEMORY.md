# MEMORY — bản đồ cho AI (không phải tài liệu cho người)
Chỉ 2 file **LUÔN ĐỌC** (★). Còn lại mở khi việc khớp cột "Khi". Chỉ mở mục của dự án hiện tại (`.du-an-hien-tai`). Thêm/đổi tên/xóa file → sửa bảng này cùng lượt, rồi `python -X utf8 scripts/kiem-tra-bo-nho.py`.

## Chung
| File (trong `memories/`) | Khi | Chứa |
|---|---|---|
| ★ `user/working-preferences.md` | mọi việc | quy tắc cốt lõi: tiếng Việt, hỏi không đoán, mật khẩu, tối đa 3 lần, commit khi nhờ |
| ★ `project/overview.md` | mọi việc | repo là gì, danh sách dự án |
| `user/document-preferences.md` | viết báo cáo/SRS/bảng soát/checklist | cách người dùng muốn tài liệu |
| `user/connectors-and-plugins.md` | cần connector/plugin; chậm | Notion/Docs tắt; tắt plugin từ repo không được (đã đo) |
| `conventions/nhieu-du-an.md` | máy mới, đổi/tạo dự án | chọn dự án, không lẫn kiến thức |
| `conventions/memory-writing-rules.md` | trước khi ghi/sửa memory | khuôn viết cho AI, độ dài |
| `conventions/ba-question-wording.md` | viết câu hỏi BA | xưng hô, từ chung, khuôn |
| `project/skills.md` | dùng/sửa skill | 5 skill, script, trạng thái đã thử |
| `project/srs-process.md` | làm SRS; hỏi vì sao khuôn thế | quyết định khuôn/ID, bẫy |
| `project/truy-vet-requirement.md` | requirement đổi; sửa checklist/TC; sửa smoke | `truy-vet.py`, `truy-vet-smoke.py`, neo TC, lịch sử, bẫy |
| `project/session-speed.md` | than chậm/tốn token; sửa skill/khuôn | số đo, đã làm, rủi ro |
| `project/git-remote.md` | commit/push | remote, `.env` loại trừ |
| `project/architecture.md` | thêm thư mục, đổi quyền, máy mới | cấu trúc, script |
| `project/cong-cu-markitdown.md` | đọc docx/pdf/xlsx/pptx; cài máy | cách dùng, bẫy |
| `project/notion-journey-page.md` | nhắc Notion/hướng dẫn/content | trang Notion, bẫy |
| `decisions/decision-log.md` | trước khi đề xuất đổi hướng | quyết định + lý do + phương án loại |
| `pitfalls/dont-trigger-lockouts.md` | trước thao tác có thể gây khóa | bài học khóa đăng nhập |
| `modules/_template.md` | tạo file module | khuôn |

## Dự án `banking-lite` (chỉ khi `.du-an-hien-tai` = banking-lite)
| File | Khi | Chứa |
|---|---|---|
| `modules/banking-lite/overview.md` | đầu tiên | hệ thống, tài khoản, thư mục |
| `modules/banking-lite/tu-ngu-cau-hoi-ba.md` | viết câu hỏi BA | từ đã chốt với BA |
| `modules/banking-lite/exploration-findings.md` | cần luồng hồ sơ/vai trò/dữ liệu test | vòng đời, vai trò, bẫy trình duyệt |
| `modules/banking-lite/feature-dang-nhap.md` | `LOGIN` | hành vi, TL-01…13, trạng thái |
| `modules/banking-lite/feature-khuyen-nghi-ltv-dsr.md` | `RECO` | luật, TL-02, chỗ SRS lệch |
| `modules/banking-lite/feature-gui-tham-dinh.md` | nút Gửi thẩm định | điều kiện bật/tắt |
| `modules/banking-lite/report-v2-html.md` | sửa báo cáo v2 | build, khoanh nút, bẫy |

Sản phẩm cho người đọc (không phải memory): `testing/chien-luoc-phan-tich-requirement.md` (sách Sunny; đọc khi nhắc "sách"); `testing/banking-lite/<feature>/` gồm `bang-soat-requirement.md`, `cau-hoi-cho-ba.md`, `checklist.md`, `test-case.md`, `truy-vet.md` (`dang-nhap` = LOGIN, `khuyen-nghi-ltv-dsr` = RECO: có `test-case.md` gộp 38 TC, không có `checklist.md`, thêm `phan-tich-requirement.md` cũ). `testing/banking-lite/smoke-test.md` = bộ smoke 7 case chọn từ LOGIN+RECO (15 phút, người dùng chốt 2026-11-18; chưa release note nên chưa có phần "Theo build"; case LOGIN-TC-001 còn `DEFAULT`: đã chốt ghi "Đạt kèm lỗi đã biết", không dừng build). Đọc trước khi làm checklist/test case feature đó.
