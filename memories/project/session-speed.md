# Tốc độ phiên: số đo và cách giữ nhanh
Đọc khi: người dùng than chậm/tốn token, hoặc sửa skill/khuôn/bộ nhớ.

## Số đo (nhật ký `~/.claude/projects/D--AI-build-sunny-agent-version-1/*.jsonl`)
- Ngữ cảnh ở lượt trả lời đầu: **~73–76 nghìn token** (đo 2026-11-18 bằng `scripts/do-toc-do-phien.py`). Phân tích phiên đo: ~55 nghìn là phần đệm cố định (prompt hệ thống + schema công cụ của Claude Code); skill listing 30 nghìn ký tự (~7,5 nghìn token: repo+built-in 10,9K, `anthropic-skills` 10K, plugin tài khoản 9,1K ký tự); danh sách công cụ hoãn ~9K ký tự; `CLAUDE.md` ~4 KB. **Plugin/skill tài khoản chỉ ~2–5 nghìn token (3–6%)**, không phải "gần hết" như từng ghi. Repo chỉ góp `CLAUDE.md` + 4 skill (~1,5 nghìn token).
- Công cụ chỉ ~0,3–6 phút/phiên; phần lớn thời gian là mô hình **sinh chữ** (phiên ghi TL-01…05: 11,6 phút, một bước 52 nghìn token).
- Phiên kéo tới 300–700 nghìn token ngữ cảnh → mỗi bước sau chậm hơn.
- Nguyên nhân từng có: bảng soát 84 KB chép lặp câu hỏi; lớp "luôn đọc" dày; phiên dài nhiều việc; máy mới thiếu allowlist/Python/`.env`.

## Đã làm (2026-11-18)
| Việc | Kết quả |
|---|---|
| Bảng soát không chép lại câu hỏi | `LOGIN` 84→63 KB, `RECO` 67→48 KB |
| Gọn phần luôn đọc | 17,4→8,9 KB, sau đó thu gọn bộ nhớ AI (xem dưới) |
| Bảng "Đọc gì cho từng việc" trong mỗi `SKILL.md` | |
| Máy mới | `.claude/settings.json` (13 quyền), `.env.example`, `kiem-tra-may-moi.py`, `docs/cai-dat-may-moi.md` (chưa thử máy mới thật) |
| Kịch bản kiểm thử `docs/kiem-thu-cac-thay-doi.md` T1–T7 | T4, T5, T6 đạt (T6: phiên bản sao tự commit → thêm quy tắc commit); chưa có T2, T3, T7 |
| Bộ nhớ chỉ cho AI đọc, viết ngắn, bản đồ dạng bảng | xem `memory-writing-rules.md` |
| Script tắt plugin qua `.claude/settings.local.json` (`syncClaudeAiPlugins=false`, `disableClaudeAiConnectors=true`) | **Đã đo, vô tác dụng → đã xóa script**: phiên mới vẫn 74,4 nghìn token, đủ 57 skill. Thử thêm 23 deny `Skill(...)`: vẫn 74,5 nghìn. Chi tiết `user/connectors-and-plugins.md` |

## Rủi ro khi sửa
- Bảng soát: đừng thay câu hỏi bằng mã trần (người dùng chê mã nội bộ); `kiem-tra.py` phải theo.
- Gọn bộ nhớ: chuyển chỗ, không xóa quy tắc; sau sửa kiểm từng quy tắc còn đúng một nơi (`scripts/kiem-tra-bo-nho.py`).
- Hạ effort chỉ cho việc đơn giản (push git, ghi TL, sửa chữ); phân tích requirement/khám phá giữ mức cao.
- Thói quen người dùng: mỗi việc một phiên mới; nói rõ việc + feature ngay câu đầu.
