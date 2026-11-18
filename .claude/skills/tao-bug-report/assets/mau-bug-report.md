# [Đặt lịch hẹn] Nút Xác nhận vẫn bật khi chưa chọn giờ, cho tạo lịch hẹn không có giờ

> Ví dụ trung lập để minh họa hình dạng. Dữ liệu và hệ thống trong ví dụ là bịa, không dùng làm nội dung thật. Kết quả mong đợi bên dưới có nguồn, nên đây là lỗi đã rõ; nếu không có nguồn thì đổi thành `Chưa xác định` + câu hỏi cho BA và ghi ngay dưới tiêu đề "Nghi lỗi, chờ BA chốt".

## Test case liên quan
TC-014 (Nút Xác nhận bị tắt khi chưa chọn giờ hẹn). Không có test case: ghi "Không có".

## Môi trường
- Hệ thống: bản thử nghiệm đặt lịch hẹn, địa chỉ `https://example.test/` (người dùng cung cấp)
- Trình duyệt: Chrome 126 trên Windows 11
- Số build: 2.4.1
- Tài khoản: `USER-TEST-01`

## Điều kiện trước
- Tài khoản `USER-TEST-01` đã có sẵn một dịch vụ cần đặt lịch (theo TC-014)
- Chưa có lịch hẹn nào trong ngày được chọn

## Các bước tái hiện
1. Đăng nhập bằng tài khoản `USER-TEST-01`.
2. Vào màn hình "Đặt lịch hẹn", chọn dịch vụ "Khám tổng quát".
3. Chọn ngày hẹn 20/12/2026, **không chọn giờ** (ô "Giờ hẹn" vẫn hiện "Chọn giờ").
4. Quan sát nút "Xác nhận" và bấm vào nút đó.

## Kết quả mong đợi
Nút "Xác nhận" bị tắt (mờ, không bấm được) cho đến khi chọn giờ hẹn (theo TC-014, bước 4; theo requirement: "Nút Xác nhận chỉ được bật khi đã chọn đủ ngày và giờ").

## Kết quả thực tế
Ở bước 4, nút "Xác nhận" sáng bình thường và bấm được. Sau khi bấm, hệ thống hiện thông báo "Đặt lịch thành công" và trong danh sách lịch hẹn có thêm một dòng ngày 20/12/2026 với cột "Giờ" để trống. [Giả định: dòng mới nằm ở trạng thái "Chờ xác nhận" như các lịch hẹn khác, vì ghi chú không nói trạng thái]

## Phạm vi ảnh hưởng
Không có: chỉ một chỗ.

(Khi cùng một lỗi gốc xuất hiện ở nhiều chỗ **và ghi chú nói rõ chung nguyên nhân hoặc Dev đã xác nhận**, liệt kê từng chỗ, ví dụ:
- Màn hình "Đặt lịch hẹn": nút Xác nhận bật khi chưa chọn giờ.
- Màn hình "Đổi lịch hẹn": nút Lưu bật khi xóa giờ đã chọn.)

## Ảnh hưởng nghiệp vụ
Người dùng tạo được lịch hẹn không có giờ, nên nhân viên không biết khung giờ phục vụ. [Giả định: lịch không có giờ không thể được xếp nhân viên, vì ghi chú không nêu cách hệ thống xử lý lịch này]

## Severity
**Major.** Chức năng chính (đặt lịch) cho phép lưu dữ liệu không đầy đủ, người dùng thấy "Đặt lịch thành công" nhưng lịch không dùng được. Còn cách đi vòng: người dùng sửa lại lịch rồi chọn giờ [Giả định: có chức năng sửa lịch hẹn đã tạo].

## Priority đề xuất
**Cao** — lịch không có giờ dễ lọt vào dữ liệu thật. (Đề xuất; team hoặc PO sẽ chốt.)

## Tần suất
Luôn xảy ra (3/3 lần thử).

## Đính kèm cần có
- [ ] Ảnh chụp màn hình bước 3: ô "Giờ hẹn" chưa chọn, nút "Xác nhận" sáng — `Cần bổ sung`
- [ ] Ảnh chụp thông báo "Đặt lịch thành công" và dòng lịch hẹn không có giờ — `evidence/<dự-án>/bug/BUG-001-thanh-cong.png`
- [ ] Bản ghi dữ liệu: dòng lịch hẹn vừa tạo (mã lịch hẹn, cột giờ trống) — `Cần bổ sung`
- [ ] Log / phản hồi mạng của lần bấm Xác nhận — `Cần bổ sung`
- [ ] Video thao tác 4 bước — không bắt buộc

## Câu hỏi còn mở
**Cho BA** (khi kết quả mong đợi không có trong nguồn; ví dụ này đã có nguồn nên bỏ trống):
- (Không có)

**Cho Dev**:
- Lỗi nút Xác nhận ở "Đặt lịch hẹn" có chung nguyên nhân với nút Lưu ở "Đổi lịch hẹn" (BUG-002) không? Hai bug đang để riêng cho tới khi có câu trả lời.

## Thông tin đã gắn nhãn Giả định (cần kiểm lại)
1. Dòng lịch hẹn mới nằm ở trạng thái "Chờ xác nhận" (mục Kết quả thực tế).
2. Lịch không có giờ không thể được xếp nhân viên (mục Ảnh hưởng nghiệp vụ).
3. Có chức năng sửa lịch hẹn đã tạo (mục Severity).
