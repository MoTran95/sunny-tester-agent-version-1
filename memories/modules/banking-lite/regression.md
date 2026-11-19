# Banking Lite — bộ regression (`testing/banking-lite/regression-test.md`)
Đọc khi: chọn/chạy/cập nhật regression Banking Lite.

- **Quyết định 2026-11-19 (người dùng):** làm cho `LOGIN` + `RECO` đang có; requirement đổi → test case cập nhật → regression cập nhật theo (script `truy-vet-regression.py`). Chưa có release note nên phân tích ảnh hưởng theo **vùng chức năng**; có release note thì thêm mục "Theo đợt phát hành".
- Hiện: 81 case = Tầng 1 13 case (LOGIN TC-001..005, 023, 026; RECO TC-001, 002, 009, 014, 022, 023) + Tầng 2 13 vùng 68 case. **Bản đề xuất, chờ người dùng duyệt** việc chọn Tầng 1 và chia vùng. Đã chốt mốc 2026-11-19.
- Bẫy riêng: ca `SAI-1` ở LOGIN (TC-006…013, 030, 035, 036, 040) cộng dồn vào bộ đếm 10 lần chặn (TL-02, TL-06 nhập đúng thì về 0, TL-12 đếm theo tài khoản — suy ra): **xả bằng đăng nhập đúng xen kẽ**. Vùng "chặn sau nhiều lần sai" (TC-014…022, 037) do người dùng tự chạy tay. TC-042/043 chờ ~9/10,5 phút. Tầng 1 chỉ TC-001 có ⚠️ (chữ DEFAULT, "Đạt kèm lỗi đã biết" như smoke).
- Chưa có bug lọt production nào được đưa vào bộ (chưa ai dán bug); khi có thì làm theo rule trong skill `de-xuat-regression`.
- Chưa có case: định giá/CIC (`RECO-M09/M10`), Gửi thẩm định, `RECO-S04-AC01/04`, `S05-AC02`, `S03-AC11`, `R12`; đã ghi mục "Case đề xuất viết thêm", chưa viết (phải hỏi người dùng trước).
- Nhãn "Suy luận" trong bảng ảnh hưởng (Khuyến nghị dùng chung phiên/ngôn ngữ/lưu với chỗ khác; Gửi thẩm định dùng lại ngưỡng) cần Dev xác nhận: đã ghi thành 5 câu hỏi Dev trong file.

## Lượt chạy Tầng 1 đầu tiên (2026-11-19, staging, bản 1.3.0, tự động)
- 13 case: 8 Đạt, 1 Đạt kèm ý phụ sai (LOGIN TC-001: `DEFAULT`, BUG-001), 2 Không đạt, 1 Không kết luận (xem dưới), cộng LOGIN TC-004 Không đạt (BUG-002, lỗi đã biết; câu báo lỗi còn `Mã không gian`).
- **RECO TC-001 Không đạt (phát hiện mới, chưa tạo bug, chờ người dùng):** hồ sơ nháp vay 3,2 tỷ chưa nhập thu nhập: khung Thẩm định và đầu trang Khuyến nghị hiện `Từ chối` (SRS S01-AC01 mong đợi không nhãn + thông báo `Nhập đủ thông tin…`). Cùng nguyên nhân: hồ sơ nháp mới đầu trang đã `Từ chối`, không phải `—` nên **RECO TC-022 Không kết luận** (điều kiện trước sai); hồ sơ `draft_application_for_tc_022` còn nguyên chưa dùng. Chưa biết là lỗi hay khác biệt giữa staging và bản cũ (lúc quan sát SRS).
- Script mới: `khuyen-nghi-ltv-dsr/auto/tc-001.py`, `tc-014.py` (TC-014 bấm Lưu hai lần nên dùng hết `draft_application_for_tc_014`; `create_draft_application.py --keys ... --overwrite` tạo hồ sơ mới). Hàm mới trong `reco_common.py`: `header_recommendation`, `save_and_wait`.
- Ghi lượt: `truy-vet-regression.py ghi-luot` (mục "Lượt chạy" của regression-test.md). Thứ tự chạy đã dùng: LOGIN 005, 001, 002, 003, 004, 026 → RECO → LOGIN 023 (đăng xuất làm mất phiên P100001 nên xếp cuối).
- Trang kết quả Tầng 1: `testing/banking-lite/regression-tang-1-ket-qua.html` (RG-01…RG-13: 1 L005, 2 L001, 3 L002, 4 L004, 5 L003, 6 L023, 7 L026, 8 R001, 9 R002, 10 R023, 11 R009, 12 R014, 13 R022); lượt 1 ghi 2026-11-19 với kết luận và rủi ro.
