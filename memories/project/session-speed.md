# Tốc độ phiên làm việc: số đo và nguyên nhân chậm
Cập nhật: 2026-11-18 · Liên quan: [skills.md](skills.md), [../user/working-preferences.md](../user/working-preferences.md)

## Số đo (từ nhật ký 13 phiên trong `~/.claude/projects/D--AI-build-sunny-agent-version-1/*.jsonl`, đo 2026-11-18)
- Ngữ cảnh lúc bắt đầu, **trước khi đọc file nào của repo**: ~76–100 nghìn token. Gần hết đến từ app/plugin/MCP cài ở cấp người dùng (Notion, Claude Docs, plugin data, assp-*, kundalini, flipbook…), không phải từ repo (`CLAUDE.md` chỉ 2 KB).
- Thời gian chạy công cụ (Read, Bash, Edit) chỉ ~0,3–6 phút mỗi phiên. **Phần lớn thời gian là mô hình tự suy nghĩ và viết ra**: phiên ghi TL-01…05 của `LOGIN` mất 11,6 phút sinh chữ, riêng một bước sinh 52 nghìn token (~6 phút) ngay sau khi đọc xong ~12 file; phiên phân tích `LOGIN` 35 nghìn token một bước; phiên `RECO` 59 nghìn.
- Bảng soát rất nặng: `testing/banking-lite/dang-nhap/bang-soat-requirement.md` 84 KB, có ô dài ~2000 ký tự → phải đọc 2 lần (vượt giới hạn một lần đọc), rồi mô hình viết script Python 34 KB để sửa bảng.
- Phiên kéo dài tới 300–700 nghìn token ngữ cảnh → mỗi bước sau chậm và tốn hơn.

## Nguyên nhân chính (xếp theo mức ảnh hưởng)
1. File sản phẩm quá lớn và bảng soát **chép lại nguyên văn câu hỏi** từ file câu hỏi (quy tắc 9 của `phan-tich-requirement`) → nội dung bị nhân đôi, sửa một câu trả lời phải đọc/viết lại cả hai file.
2. Lớp "luôn đọc" dày và lặp ý: `MEMORY.md` 8 KB (mô tả dài, dòng nhật ký cập nhật), `user/working-preferences.md` 7,4 KB; cùng một quy tắc (mật khẩu, 3 lần, đọc là hiểu, không dán bảng) nằm ở 3–4 nơi.
3. Phiên dài, làm nhiều việc nối nhau trong cùng một phiên.
4. Máy mới (chưa đo, chỉ là giả thuyết): chưa có allowlist quyền trong `.claude/settings.json` nên mỗi lệnh đều hỏi; có thể thiếu Python/Pillow; `.env` không theo git nên thiếu tài khoản test.

## Rủi ro khi sửa (đã nói với người dùng 2026-11-18)
- Làm gọn bảng soát: đừng thay câu hỏi bằng mã trần (người dùng từng chê mã nội bộ) → giữ một câu tóm tắt đọc được + liên kết; phải sửa `kiem-tra.py` theo, kẻo mất bước kiểm bảng soát khớp file câu hỏi; hai bảng cũ (`RECO`, `LOGIN`) cần chuyển hoặc script phải đọc được cả hai dạng.
- Làm gọn bộ nhớ: chuyển chỗ, không xóa; sau khi sửa grep lại từng quy tắc còn đúng một nơi.
- Hạ effort chỉ cho việc đơn giản; phân tích requirement giữ mức cao.
- Cách kiểm: chạy lại skill trên `LOGIN`, so số ✅/❓, số câu hỏi, script 0 lỗi với bản cũ.

## Trạng thái
- Hướng 1 "làm gọn bảng soát": **đã làm 2026-11-18** (xem decision-log). Chưa đo lại thời gian trên một lần ghi câu trả lời thật.
- Hướng 2 "làm gọn bộ nhớ luôn đọc": **đã làm 2026-11-18**. `MEMORY.md` 8,7→4,8 KB, `working-preferences.md` 7,4→2,6 KB (tổng phần luôn đọc kể cả `overview.md`: 17,4→8,9 KB). Chi tiết tài liệu chuyển sang `user/document-preferences.md`, bài học giọng văn sang `conventions/ba-question-wording.md`; đã kiểm bằng script: không mất cụm quy tắc nào, không liên kết gãy, mọi file có trong bản đồ.
- Hướng 3–5 (skill chỉ rõ file cần đọc, phiên ngắn/effort, chuẩn bị máy mới): chưa làm.
