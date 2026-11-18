# Checklist test — Đặt số lượng sản phẩm vào giỏ (ví dụ mẫu)

| | |
|---|---|
| Ngày lập | YYYY-MM-DD (mẫu) |
| Hệ thống | Web bán hàng (ví dụ trung lập, không phải requirement thật). Phạm vi: ô Số lượng và nút Thêm vào giỏ |
| Nguồn | Requirement mẫu: R1 số lượng mỗi lần thêm từ 1 đến 10; R2 dưới 1 báo "Số lượng tối thiểu là 1."; R3 trên 10 báo "Số lượng tối đa là 10."; R4 để trống báo "Vui lòng nhập số lượng." |
| Chỉ làm | Checklist. Chưa viết bước chi tiết |

**Cách đọc cột Nguồn.** `Có trong tài liệu`: ghi mã requirement (kèm tên ngắn trong ngoặc). `Suy luận`: ghi một câu lý do, điểm xuất phát là điều nguồn đã ghi rõ. Không có dòng `Giả định` trong bảng; phần nguồn không nói chuyển thành câu hỏi bên dưới.

<!-- BANG-TC:BAT-DAU (bảng test case; tiêu đề cột là cố định để script đọc) -->
| Mã | Tình huống | Ưu tiên | Kỹ thuật | Nguồn |
|---|---|---|---|---|
| TC-001 | Nhập số lượng hợp lệ `5` rồi bấm Thêm vào giỏ: giỏ hiện 5 sản phẩm | Cao | EP | Có trong tài liệu: R1 (Số lượng từ 1 đến 10) |
| TC-002 | Nhập số lượng ở biên dưới `1`: thêm được, giỏ hiện 1 sản phẩm | Cao | BVA | Có trong tài liệu: R1 (Số lượng từ 1 đến 10) |
| TC-003 | Nhập số lượng ngay dưới biên `0`: không thêm, báo "Số lượng tối thiểu là 1." | Cao | BVA | Có trong tài liệu: R1 (Số lượng từ 1 đến 10), R2 (Báo khi dưới 1) |
| TC-004 | Nhập số lượng ở biên trên `10`: thêm được, giỏ hiện 10 sản phẩm | Cao | BVA | Có trong tài liệu: R1 (Số lượng từ 1 đến 10) |
| TC-005 | Nhập số lượng ngay trên biên `11`: không thêm, báo "Số lượng tối đa là 10." | Cao | BVA | Có trong tài liệu: R1 (Số lượng từ 1 đến 10), R3 (Báo khi trên 10) |
| TC-006 | Để trống ô Số lượng rồi bấm Thêm vào giỏ: báo "Vui lòng nhập số lượng." | Trung bình | EP | Có trong tài liệu: R4 (Báo khi để trống) |
| TC-007 | Giỏ đã có 5 sản phẩm, thêm lần hai `3` sản phẩm: giỏ hiện 8 sản phẩm | Trung bình | Use case | Suy luận: R1 (Số lượng từ 1 đến 10), vì R1 áp dụng cho mỗi lần thêm nên lần hai `3` cũng là một lần thêm hợp lệ |
<!-- BANG-TC:KET-THUC -->

## Câu hỏi cho BA
1. Giỏ đã có 8 sản phẩm, thêm lần hai 3 sản phẩm thì tổng 11: có bị chặn không, hay chỉ kiểm mỗi lần thêm? Mình đang hiểu là chỉ kiểm mỗi lần thêm (R1). Liên quan: R1.

## Chưa đưa vào
- Số lượng có phần thập phân (`2.5`) hoặc chữ: requirement không nói, chưa đưa vào (xem câu hỏi cho BA).

## Tự kiểm
- 7 dòng: Cao 5, Trung bình 2, Thấp 0. Chạy `kiem-tra-tc.py` để kiểm đầy đủ.
