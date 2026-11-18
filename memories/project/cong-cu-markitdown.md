# Công cụ MarkItDown (đọc docx/pdf/xlsx/pptx thành Markdown)
Cập nhật: 2026-11-18

- **Là gì:** gói `markitdown` của Microsoft (PyPI, MIT, repo `microsoft/markitdown`), đổi file Office/PDF sang Markdown để đọc ít token hơn.
- **Đã cài:** bản 0.1.9, trong venv **ngoài repo** `C:\Users\Admin\.venvs\markitdown` (máy này). Lệnh: `C:\Users\Admin\.venvs\markitdown\Scripts\markitdown.exe <file> -o <ra.md>`.
- **Phần mở rộng đã cài:** `pdf, docx, pptx, xlsx, xls`. **Cố ý bỏ** Azure, âm thanh, YouTube (cần khóa/mạng ngoài).
- **Đã soát an toàn (2026-11-18):** tác giả Microsoft, mã băm sdist/wheel khớp PyPI, không có `eval/exec`/mã hóa đáng ngờ. `subprocess` chỉ gọi `exiftool` (tùy chọn); `requests` chỉ chạy khi đưa URL. Cảnh báo chính thức: công cụ đọc file/URL bằng quyền của tiến trình, nên **chỉ đưa file/URL đã biết**, không dùng `convert_uri` với đầu vào lạ.
- **Bẫy:** trên Windows, in ra console làm tiếng Việt thành `?`. Luôn ghi ra file bằng `-o` kèm `PYTHONUTF8=1` rồi đọc file.
- **Chưa thử:** file `.docx`/`.pdf` thật, ước lượng mức tiết kiệm token. Chưa có cấu hình quyền cho phép sẵn lệnh này.

## Quy tắc giảm token (người dùng chốt 2026-11-18)
- **Dùng** khi đọc Word, PowerPoint, HTML, PDF chữ, hoặc nhiều file cùng lúc: đổi sang Markdown trước rồi mới đọc.
  Lệnh: `C:\Users\Admin\.venvs\markitdown\Scripts\python.exe -m markitdown <file> -o <thư-mục-tạm>\<tên>.md` (`python` thường **không** có markitdown).
- **Ghi `.md` ra thư mục tạm** (scratchpad), không để cạnh file gốc trong repo, tránh commit nhầm hoặc đọc nhầm bản cũ.
- **Chỉ dùng với file/URL đã biết nguồn** (Microsoft cảnh báo công cụ đọc bằng quyền của tiến trình).
- **Không dùng** cho: `.txt`/`.md`; Excel lớn (dùng pandas); PDF scan hoặc nhiều hình/biểu đồ (đọc trực tiếp trang ảnh); việc cần sửa file mà giữ định dạng (sửa file gốc).

**Why:** người dùng muốn đọc tài liệu Office/PDF của dự án tốn ít token.
**How to apply:** gặp file docx/pdf/xlsx/pptx cần đọc thì đổi sang `.md` bằng lệnh trên rồi đọc bản `.md`; không cài lại, chỉ kiểm tra venv còn không (máy mới phải cài lại, xem `docs/cai-dat-may-moi.md`).
