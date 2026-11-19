---
name: tao-test-plan
description: Lập kế hoạch kiểm thử (test plan) cho một dự án/đợt test/bản build theo khuôn 12 mục (mục tiêu, phạm vi trong/ngoài, cách kiểm thử, môi trường và dữ liệu, tiêu chí bắt đầu/kết thúc/tạm dừng, phân công và lịch, quản lý bug, sản phẩm bàn giao, rủi ro, truy vết requirement ↔ test case, phê duyệt). Ra `testing/<dự-án>/test-plan.md` và trang HTML không logo, có nút In / Lưu PDF, viết như tài liệu thật gửi sếp/công ty, CHỈ có kế hoạch, không ghi kết quả test. Tự điền từ tài liệu có sẵn của dự án, chỗ chưa biết (con số tiêu chí, tên người, ngày, công cụ) thì hỏi người test rồi mới điền, không tự đặt. Dùng khi người dùng (thường là tester) nói "lập test plan", "làm kế hoạch kiểm thử", "sếp yêu cầu test plan", "viết test plan cho build X", "cập nhật test plan", "điền thông tin vào test plan", "bản gọn test plan". Không dùng để chạy test (chay-test-tu-dong), viết báo cáo kết quả (tao-test-summary-report), chọn smoke (tao-smoke-test) hay regression (de-xuat-regression).
---

# Lập kế hoạch kiểm thử (test plan)

**Test plan là phần CHƯA test.** Nó trả lời: sẽ test cái gì, bằng cách nào, khi nào xong, rủi ro gì, ai làm. Kết quả test nằm ở báo cáo tổng kết (`tao-test-summary-report`), không nằm ở đây. Tiếng Việt với người dùng; chỉ test chức năng, trừ khi sếp yêu cầu khác.

## Bước 0: dự án
Đọc `.du-an-hien-tai` (chưa có thì làm theo `CLAUDE.md` bước 0). Chỉ đọc `memories/modules/<slug>/`, `srs/<slug>/`, `testing/<slug>/`, `evidence/<slug>/` của dự án đó. Skill này không chứa thông tin dự án nào.

## Quy tắc người dùng đã chốt (2026-11-19)
1. **Không ghi kết quả test**: không số case đã chạy/Đạt/Không đạt, không mã bug đã ghi, không "lượt chạy", không cột "Hiện trạng", không "Tình trạng thực hiện". Rủi ro viết dạng "có thể", dựa trên requirement và khám phá. Script kiểm bắt các mẫu này.
2. **Viết như bản thật** gửi được ngay: không khung "bản nháp", không nhãn "Giả định H…", không "soạn bằng Claude". Điều người lập tự quyết (phạm vi, thứ tự) viết thẳng; điều đang coi là đúng gom ở mục 9.2 "Giả định".
3. **Không logo**, không thanh điều hướng nội bộ, không dòng "Trang tự sinh…" (tên file `test-plan*.md` tự dùng kiểu gửi ra ngoài trong `docs_pages.py`, `clean=True`). Có nút In / Lưu PDF.
4. **Không tự đặt con số hay tên người**: ngưỡng tiêu chí kết thúc (số bug còn mở, tỉ lệ Đạt, số tầng regression), tên BA/Dev/người duyệt, ngày bắt đầu và hạn, mã kế hoạch, số bản trình duyệt, công cụ bug. Chưa có thì ghi `……………` rồi hỏi người test (bước 4). Con số nào đã có sẵn ở dự án (trần nhập sai, thời gian chặn, thời hạn phiên) thì lấy từ `memories/modules/<slug>/` và `testing/<slug>/auto-config.json`.
5. Điều người test quyết "tùy người quyết theo nguồn lực/thời gian" thì ghi đúng như vậy kèm nơi ghi lại (báo cáo tổng kết ghi phần đã chạy, chưa chạy, lý do), không ép thành con số.
6. **Mọi tài liệu nhắc tới có link bấm được** (requirement, test case, smoke, regression, truy vết). File kết quả chưa có thì ghi tên trong dấu `…` không link.
7. Văn phong: tiếng Việt thường, câu đủ ý, thuật ngữ IT đúng; không Given/When/Then, không mã nội bộ làm nội dung chính. Mật khẩu không ghi vào tài liệu.

## Quy trình
1. **Xác định đợt test:** hệ thống, bản build, tính năng trong phạm vi, ai yêu cầu. Tra `memories/` và `testing/<slug>/` trước; chỉ hỏi cái thiếu (bước 4). Đợt/bản build mới giữ bản cũ: đặt `test-plan-<build>.md`; lần đầu dùng `test-plan.md`.
2. **Thu thập từ repo** (bảng "Nguồn điền từng mục" ở `references/thong-tin-can-hoi.md`): requirement/SRS, bảng soát, test case, smoke, regression, truy vết, `memories/modules/<slug>/`, `auto-config.json`. **Không đọc file kết quả** (`*-ket-qua.md`, `run-results/`, bug, `test-summary-report.md`) để điền kế hoạch; chỉ liệt kê tên chúng ở mục 8 (sản phẩm bàn giao).
3. **Viết:** sao khuôn `testing/_template-test-plan.md` thành `testing/<slug>/test-plan.md`, bỏ khối chú thích đầu và chữ nghiêng hướng dẫn, điền theo nguồn. Chưa có smoke/regression/test case thì ghi "Chưa có" ở phạm vi và rủi ro, hoặc đề nghị người dùng làm trước bằng skill tương ứng; không bịa.
4. **Hỏi người test các chỗ còn trống.** Chạy `python -X utf8 .claude/skills/tao-test-plan/scripts/kiem-tra-test-plan.py <slug>` (máy không có `python` thì `python3`): mục "CÒN TRỐNG" là danh sách ô chờ điền. Hỏi theo nhóm trong `references/thong-tin-can-hoi.md`: mỗi câu đủ ngữ cảnh (đang ở mục nào, vì sao cần), có lựa chọn khi có cách làm phổ biến, không hỏi lại điều đã có trong chat/memory. **Bẫy đã gặp:** khi cần người dùng gõ số hoặc tên, hỏi bằng tin nhắn thường trong chat; hộp hỏi có nút chọn (`AskUserQuestion`) không chuyển phần chữ gõ ở ô "Other" về cho Claude. Hộp hỏi chỉ dùng cho lựa chọn có sẵn. Dừng chờ trả lời; câu nào chưa trả lời thì để `……………`.
5. **Điền câu trả lời** đúng nguyên văn người dùng (không làm tròn, không thêm). Điều người dùng nêu thêm có tính quy tắc → ghi vào `memories/modules/<slug>/` hoặc skill.
6. **Sinh và kiểm:** `python -X utf8 scripts/build_docs.py --all` (sinh trang HTML), kiểm lại bằng script ở bước 4 (phải 0 LỖI), rồi `python -X utf8 scripts/kiem-tra-bo-nho.py`.
7. **Trả lời người dùng:** link trang HTML, phần nào đã điền từ tài liệu, danh sách ô còn trống (nếu còn), nêu rõ mục 2.2 (ngoài phạm vi) và mục 9 (rủi ro) là chỗ sếp đọc kỹ nhất. Không dán cả bảng vào chat. Commit chỉ khi người dùng nhờ.

## Bản gọn (1–2 trang)
Khi sếp cần xem nhanh: giữ bảng đầu và mục 1, 2, 3, 5, 9, 10; bỏ phần còn lại. Lưu `test-plan-gon.md` (kiểm bằng `--file test-plan-gon.md` sẽ báo thiếu mục: bình thường, chỉ để đối chiếu). **Chưa thử.**

## Cập nhật test plan
Requirement/test case đổi hoặc build mới: sửa tại chỗ, thêm dòng vào mục 12 (ngày, người sửa, nội dung, lý do), cập nhật "Cập nhật lần cuối", chạy lại `scripts/truy-vet.py kiem <slug> <tính-năng>` để làm lại bảng truy vết mục 10, rồi bước 6.

## Tự kiểm trước khi trả lời
- [ ] Script kiểm báo 0 LỖI; trang HTML không logo.
- [ ] Không có kết quả test nào (số case, bug, lượt chạy).
- [ ] Không con số, tên người, ngày nào do Claude tự đặt; chỗ chưa biết còn `……………`.
- [ ] Mục 2.2 (ngoài phạm vi) có lý do và rủi ro; mục 9 có cột "Cách giảm / ai quyết".
- [ ] Mã requirement/test case/tài liệu đều có link, không link gãy.

## Tệp trong skill
- `references/thong-tin-can-hoi.md`: nguồn điền từng mục, danh sách thông tin phải hỏi người test, cách đặt câu hỏi.
- `scripts/kiem-tra-test-plan.py`: kiểm đúng khuôn, không kết quả, không nhãn nháp, link, HTML; in danh sách chỗ còn trống.
- Khuôn: `testing/_template-test-plan.md` (dùng chung mọi dự án, tự sinh HTML).

**Đã thử (2026-11-19):** lập `testing/<dự-án>/test-plan.md` từ khuôn (dự án đầu tiên ghi ở `memories/MEMORY.md`), bỏ kết quả test theo lời người dùng, kiểm bằng script (0 lỗi; thử cố tình thêm 7 lỗi bắt đủ). **Chưa thử:** gọi từ phiên mới hoàn toàn (xem có bị nhầm với `tao-test-summary-report`/`tao-smoke-test` không); dự án thứ hai; bản gọn; in PDF thật.
