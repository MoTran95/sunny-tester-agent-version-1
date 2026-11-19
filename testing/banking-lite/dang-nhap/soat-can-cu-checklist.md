# Soát căn cứ checklist Đăng nhập (Banking Lite)

| | |
|---|---|
| Ngày soát | 2026-11-19 |
| Cái được soát | Checklist Đăng nhập (nay là phần checklist trong [test-case.md](test-case.md), gộp 2026-11-19): 43 dòng, TC-001 đến TC-043 (test case chi tiết bám theo các dòng này, chưa soát riêng) |
| Requirement dùng để so | [SRS Đăng nhập](../../../srs/banking-lite/dang-nhap.md) (cột "Yêu cầu") và [bảng soát](bang-soat-requirement.md) mục 3, câu trả lời của BA TL-01 đến TL-14 |
| Quy tắc riêng dự án | Không có thêm quy tắc ngoài requirement. Ba con số 10 lần sai, chặn 5 phút, phiên 10 phút đều lấy từ câu trả lời của BA (TL-02, TL-11, TL-01, TL-09, TL-14) |
| Không soát | Cột "Ưu tiên" và "Kỹ thuật" của checklist: requirement không nói gì về hai cột này, đó là nhận định của người test |

**Cách đọc cờ.** ĐÚNG NGUỒN: có trong requirement, kèm trích dẫn. CẦN XÁC NHẬN: suy luận hợp lý nhưng requirement không nói thẳng. TỰ THÊM: không có trong requirement, giống quy tắc phổ biến bên ngoài. MƠ HỒ: dùng từ chung chung, không biết nhìn vào đâu để chấm.

**Một lưu ý chung về nguồn.** Mọi câu TL đều là "BA trả lời, người dùng chuyển lại trong chat", chưa có ticket hay link. Với dòng ĐÚNG NGUỒN mà nguồn chỉ là SRS ghi lại điều đã quan sát trên hệ thống (BA chưa nói riêng), cột Lý do ghi rõ "SRS quan sát".

| Mã | Nội dung | Cờ | Lý do | Đề xuất sửa |
|---|---|---|---|---|
| TC-001 | Đăng nhập đúng P100001: vào Danh sách việc, không có thông báo "thành công", thanh trên không còn `DEFAULT` | ĐÚNG NGUỒN | S01-AC02: "Thanh trên cùng hiện mã và vai trò … không có chữ DEFAULT". TL-07: "B12: bỏ (chữ DEFAULT trên thanh trên …)" | Giữ. Lưu ý TL-07 có chữ "mình hiểu" của người ghi, nên nếu BA nói lại khác thì sửa |
| TC-002 | Đăng nhập đúng P200001, P300001: vào đúng Danh sách việc và đúng vai trò | CẦN XÁC NHẬN | Bảng tài khoản ở mục 1 SRS chỉ là điều đã thấy ở lượt khám phá đầu ("Chỉ đăng nhập thành công"). S01-AC02 chỉ có ví dụ P100001. Không có chỗ nào nói Danh sách việc của từng vai trò gồm gì | Sửa kết quả mong đợi thành "vào được, thanh trên hiện đúng mã và vai trò ghi ở bảng SRS". Phần "đúng Danh sách việc của vai trò" chuyển thành câu hỏi (hoặc để cho feature khác) |
| TC-003 | Chưa đăng nhập mở link hồ sơ: hiện form, giữ địa chỉ; đăng nhập đúng thì mở thẳng hồ sơ | CẦN XÁC NHẬN | Phần form giữ địa chỉ có trong S04-AC02: "Hiện form đăng nhập, thanh địa chỉ giữ nguyên". Phần "mở thẳng hồ sơ": S01-AC03 ghi nhãn "suy ra: áp dụng cho mọi link … BA chưa nêu riêng", Q07 chưa hỏi, và mới thử một link | Giữ ca với link HL-000019 đã thử; bỏ ý "áp dụng cho mọi link" hoặc hỏi BA câu Q07 |
| TC-004 | Sai một lần rồi sửa đúng: vào được Danh sách việc | ĐÚNG NGUỒN | S01-AC02: nhập đúng thì "Vào trang Danh sách việc". TL-06: "Đăng nhập đúng xen giữa đưa số lần sai về 0." | Cột Nguồn đang ghi "luồng S01", nên đổi sang S01-AC02 và TL-06 |
| TC-005 | Form đăng nhập có ô mã kèm gợi ý, ô mật khẩu chấm, nút, chân trang | ĐÚNG NGUỒN | S01-AC01: "ô Mã nhân viên * (gợi ý … Chữ P và 6 chữ số, ví dụ P100001.), ô Mật khẩu * (chữ gõ hiện dạng chấm), nút Đăng nhập, và chân trang ghi Banking Lite · Phiên bản 1.3.0". SRS quan sát | Giữ |
| TC-006 | P100001 sai mật khẩu: khung lỗi "Mã nhân viên hoặc mật khẩu không đúng." | ĐÚNG NGUỒN | TL-08: "Tiếng Việt: "Mã nhân viên hoặc mật khẩu không đúng."" | Giữ |
| TC-007 | Mã không tồn tại P999999: cùng một câu như sai mật khẩu | ĐÚNG NGUỒN | TL-10: "hai trường hợp dùng chung một câu." | Giữ |
| TC-008 | Trống ô mã, có mật khẩu: câu chung | ĐÚNG NGUỒN | S02-AC03: "Cùng khung lỗi LOGIN-M01 như AC01. Không có câu "bắt buộc nhập mã"" | Giữ |
| TC-009 | Trống ô mật khẩu: câu chung, không còn `Một số giá trị không hợp lệ.` và `validation.too_small (password)` | ĐÚNG NGUỒN | S02-AC05: "không hiện câu `Một số giá trị không hợp lệ.` và không hiện dòng `validation.too_small (password)`" | Giữ |
| TC-010 | Trống cả hai ô: câu chung | ĐÚNG NGUỒN | R04: "Để trống ô nào (một hoặc cả hai) cũng chỉ báo câu chung". S02-AC05 cũng ghi "ô mã: trống" | Cột Nguồn đang ghi "Suy luận" mà thật ra requirement nói thẳng: đổi sang R04 và S02-AC05 |
| TC-011 | Sau khi báo lỗi, ô Mật khẩu phải trống; ô mã giữ chữ | TỰ THÊM | Không câu nào của BA nói ô Mật khẩu phải bị xóa. TL-03 không nhắc bảo mật. Lý do "bảo mật" là suy luận của người test, SRS ghi "suy ra … BA chưa nêu riêng" và "người dùng xác nhận" (người dùng không phải BA). Giống quy tắc phổ biến bên ngoài. Dòng này còn đang tính là Không đạt, tức nghi lỗi, trên căn cứ không có | Tách đôi. Giữ "ô mã giữ chữ đã gõ" (SRS luồng chung S02, có quan sát). Bỏ phần "mật khẩu phải trống" khỏi kết quả mong đợi, đổi thành câu hỏi BA; trong lúc chờ không tính là lỗi |
| TC-012 | Mật khẩu đổi một chữ hoa thành thường: không đăng nhập, câu chung | ĐÚNG NGUỒN | TL-13: "phân biệt chữ hoa, chữ thường … sai hoa thường là sai mật khẩu" | Giữ. Bỏ R08 khỏi cột Nguồn vì không liên quan. Cẩn thận: TL-13 vừa ghi "không gửi BA hỏi riêng" vừa ghi "BA đã xác nhận", chưa có ticket |
| TC-013 | Mật khẩu thừa khoảng trắng cuối: không đăng nhập, câu chung | ĐÚNG NGUỒN | TL-13: "gõ thừa khoảng trắng hoặc sai hoa thường là sai mật khẩu" | Giữ (cùng lưu ý nguồn như TC-012) |
| TC-014 | Sai 9 lần cùng một tài khoản: lần 9 vẫn báo câu chung, chưa bị chặn | ĐÚNG NGUỒN | TL-11: "Lần sai thứ 10 thì báo bị chặn." Bối cảnh S02-AC07: "9 lần liên tiếp" | Giữ |
| TC-015 | Lần sai thứ 10: bị chặn, bản Việt "Đăng nhập sai quá nhiều lần. Thử lại sau 5 phút." | ĐÚNG NGUỒN | TL-11 như trên. S02-AC07: "Tiếng Việt: Đăng nhập sai quá nhiều lần. Thử lại sau 5 phút." Nguồn của câu chữ là SRS quan sát (M05 ghi "chỉ thấy trong tệp giao diện", chưa thấy trên màn hình), BA chưa nói câu này | Giữ, nhưng trong test case ghi rõ câu tiếng Việt chưa từng thấy trên màn hình |
| TC-016 | Đang bị chặn, sai thêm lần 11: vẫn bị chặn, không tính thêm, không kéo dài thời gian chặn | CẦN XÁC NHẬN | "Không tính thêm": TL-09 "lúc bị chặn nhập thêm không tính". "Không kéo dài thời gian chặn": chỉ suy ra từ TL-01 "tính từ lúc bị chặn", BA không nói thẳng. Màn hình khi nhập lúc đang bị chặn còn mở (B4) | Giữ "không tính thêm". Phần "không kéo dài" ghi rõ là suy luận hoặc thêm vào câu hỏi B4 |
| TC-017 | Đang bị chặn, nhập đúng: không vào được | ĐÚNG NGUỒN | TL-01: "Đang bị chặn thì không được vào, kể cả nhập đúng." | Giữ |
| TC-018 | Ngay trước mốc 5 phút, nhập đúng: vẫn không vào | ĐÚNG NGUỒN | TL-01: "Sau 5 phút mới được vào, tính từ lúc bị chặn." | Giữ. "Ngay trước" chưa là giá trị đo được: trong test case ghi một thời điểm cụ thể (ví dụ cách mốc 30 giây như TC-043) |
| TC-019 | Ngay sau mốc 5 phút, nhập đúng: vào được | ĐÚNG NGUỒN | TL-01 như trên; TL-09: "Hết 5 phút là hết chặn" | Giữ, cùng lưu ý "ngay sau" như TC-018. Đúng giây thứ 5 phút đã đúng khi không đưa vào (BA nói cả "sau" lẫn "hết") |
| TC-020 | Hết 5 phút, nhập sai: câu chung, đếm lại từ đầu | ĐÚNG NGUỒN | TL-09: "Sau khi hết 5 phút nhập sai thì mới được tính số lần lại." R06: "nhập sai sau đó thì đếm lại từ đầu" | Giữ |
| TC-021 | Sai 9 lần, đúng một lần, sai tiếp: không bị chặn | ĐÚNG NGUỒN | TL-06: "Đăng nhập đúng xen giữa đưa số lần sai về 0. Chỉ tính số lần, không tính thời gian." | Giữ |
| TC-022 | P100001 sai 9 lần, P200001 sai 1 lần: P200001 chưa bị chặn; P100001 sai thêm thì bị chặn | CẦN XÁC NHẬN | TL-12: "chặn đúng tài khoản đã nhập sai, không chặn tài khoản khác" nói về phạm vi chặn. Còn việc lần sai của P200001 xen giữa có làm đứt chuỗi "liên tiếp" của P100001 không thì BA chưa trả lời. TL-12 cũng ghi "Chưa nói: mã không có thật thì đếm thế nào" | Chờ câu 2 trong test-case.md (đã soạn sẵn cho BA). Có thể tách: giữ nửa đầu (P200001 chưa bị chặn), nửa sau (P100001 bị chặn) chờ BA |
| TC-023 | Đăng xuất: về form, địa chỉ `/`, giữ ngôn ngữ | ĐÚNG NGUỒN | S04-AC01: "Về form đăng nhập, thanh địa chỉ là `/`; ngôn ngữ giữ nguyên". SRS quan sát | Giữ |
| TC-024 | Đăng xuất ở trang hồ sơ rồi Back: chỉ hiện form | ĐÚNG NGUỒN | S04-AC03: "chỉ hiện form đăng nhập; dữ liệu hồ sơ không hiện ra". SRS quan sát | Giữ |
| TC-025 | Hai tab: đăng xuất tab 2, thao tác ở tab 1: về form đăng nhập | CẦN XÁC NHẬN | S04-AC04 có ghi tab 1 chuyển sang form, nhưng đó là quan sát. Q09 ghi rõ "suy ra: về form đăng nhập để đăng nhập lại là đủ", BA chưa nêu | Giữ, ghi nhãn "suy luận từ Q09" ở kết quả mong đợi, hoặc hỏi BA |
| TC-026 | Chưa đăng nhập mở `/integrations` hoặc địa chỉ không có thật: hiện form, giữ địa chỉ | ĐÚNG NGUỒN | S04-AC02: "Hiện form đăng nhập, thanh địa chỉ giữ nguyên. Không có thông báo "cần đăng nhập" và không có trang "không tìm thấy"". SRS quan sát (Q08: BA không nêu khác) | Giữ |
| TC-027 | Gõ `p100001` + mật khẩu đúng: đăng nhập được | ĐÚNG NGUỒN | TL-04: "Chữ p thì hoa thường đều được." | Giữ |
| TC-028 | Mã thừa khoảng trắng đầu: đăng nhập được | ĐÚNG NGUỒN | TL-04: "Khoảng trắng đầu/cuối: tự cắt bỏ" | Giữ |
| TC-029 | Mã thừa khoảng trắng cuối: đăng nhập được | ĐÚNG NGUỒN | TL-04: "Khoảng trắng đầu/cuối: tự cắt bỏ" | Giữ |
| TC-030 | Mã sai dạng (`X999999`, `P99999A`, `P99-999`): câu chung | ĐÚNG NGUỒN | S02-AC04: "Mỗi kiểu đều nhận cùng khung lỗi LOGIN-M01; không có thông báo riêng nói "mã sai định dạng"" | Giữ |
| TC-031 | Enter ở ô mã và ở ô mật khẩu: form gửi như bấm nút | CẦN XÁC NHẬN | S01-AC05 chỉ nói được phần ô Mã nhân viên ("Form được gửi đi giống như bấm nút"). Phần ô Mật khẩu là "Suy ra" và SRS ghi "ô Mật khẩu chưa thử" | Tách hai bước: ô mã giữ; ô mật khẩu ghi là suy luận |
| TC-032 | Tải lại trang: vẫn đăng nhập | ĐÚNG NGUỒN | S01-AC06: "Vẫn đang đăng nhập, không phải nhập lại". SRS quan sát | Giữ |
| TC-033 | Đã đăng nhập mở `/login`: hiện Danh sách việc, địa chỉ vẫn `/login` | ĐÚNG NGUỒN | S01-AC07: "Hiện Danh sách việc (không hiện form đăng nhập); thanh địa chỉ vẫn là `/login`". SRS quan sát (Q08: BA không nêu khác) | Giữ |
| TC-034 | Đã đăng nhập mở địa chỉ không có thật: hiện Danh sách việc | ĐÚNG NGUỒN | S01-AC08: "Hiện Danh sách việc; thanh địa chỉ giữ nguyên; không có trang "không tìm thấy"". SRS quan sát | Giữ |
| TC-035 | Đổi ngôn ngữ khi đang có lỗi: nhãn đổi ngay, chữ ở ô mã còn, câu lỗi đổi, không còn dòng mã kỹ thuật | ĐÚNG NGUỒN | S03-AC01: "chữ đã gõ ở ô mã vẫn còn; khung lỗi vẫn hiện, câu lỗi được dịch qua lại". S03-AC02: "Đã bỏ: không còn dòng mã lỗi kỹ thuật" (TL-03) | Giữ |
| TC-036 | Bản English sai mật khẩu: "Employee ID or password is incorrect." | ĐÚNG NGUỒN | TL-08: "English: "Employee ID or password is incorrect."" | Giữ |
| TC-037 | Bản English bị chặn: "Too many failed attempts. Try again in 5 minutes." | ĐÚNG NGUỒN | M05 (cột English): "Too many failed attempts. Try again in 5 minutes." SRS quan sát, BA chưa nói câu chữ | Giữ |
| TC-038 | Chọn ngôn ngữ, tải lại, Đăng xuất: giữ ngôn ngữ | ĐÚNG NGUỒN | S03-AC03: "Vẫn đúng ngôn ngữ đã chọn". SRS quan sát | Giữ |
| TC-039 | Bấm English: vai trò thành "Banker", số tiền hiện kiểu English (ví dụ `2,000,000,000`) | MƠ HỒ | Phần vai trò đúng nguồn (S03-AC04: "Chuyên viên khách hàng" thành "Banker"). Phần "số tiền hiện kiểu English" không nói số tiền ở màn hình nào, của hồ sơ nào, nên không biết nhìn vào đâu để chấm. Câu hỏi 3 trong test-case.md đã nêu đúng điểm này | Giữ ý vai trò. Phần số tiền bỏ ra khỏi kết quả mong đợi cho tới khi BA trả lời |
| TC-040 | Mã 210 ký tự: câu chung, không còn `validation.too_big (employeeId)` | ĐÚNG NGUỒN | S02-AC06: "chỉ ghi `Mã nhân viên hoặc mật khẩu không đúng.`; không hiện … dòng `validation.too_big (employeeId)`". TL-04: "Độ dài không quy định" | Giữ |
| TC-041 | Form không có ô Workspace, không có quên mật khẩu, đăng ký, "ghi nhớ đăng nhập" | CẦN XÁC NHẬN | Chỉ Workspace có BA nói (TL-05: "Mã không gian là bị bỏ, không còn được sử dụng"). Ba chức năng kia SRS chỉ ghi "Không thấy trên màn hình … (ngoài phạm vi vì chưa có)", đó là quan sát chứ không phải yêu cầu phải vắng mặt. Cột Nguồn dẫn TL-04 là sai chỗ (TL-04 nói về khoảng trắng, hoa thường, độ dài) | Giữ ý Workspace (dẫn TL-05). Bỏ ba chức năng kia hoặc đổi thành câu hỏi. Bỏ TL-04 khỏi cột Nguồn |
| TC-042 | Chờ 9 phút không thao tác rồi F5: vẫn đăng nhập | ĐÚNG NGUỒN | TL-14: "Thời hạn phiên đăng nhập là 10 phút." S01-AC09: "Phiên đăng nhập hết hạn sau 10 phút". Chưa đủ 10 phút là phần còn lại của câu đó. Kết quả không phụ thuộc câu B15 vì ca không thao tác | Giữ |
| TC-043 | Chờ 10 phút 30 giây không thao tác rồi F5: không còn đăng nhập; màn hình hiện gì: CẦN XÁC NHẬN | ĐÚNG NGUỒN | TL-14 và S01-AC09 như trên: "người dùng không còn được coi là đã đăng nhập". Dòng đã tự để phần màn hình là CẦN XÁC NHẬN, đúng với B15 | Giữ. Trong test case, để phần màn hình là "chưa chấm" cho đến khi BA trả lời B15 |

## Tổng kết

| Cờ | Số dòng | Dòng |
|---|---|---|
| ĐÚNG NGUỒN | 34 | trong đó 10 dòng chỉ có SRS quan sát làm căn cứ, BA chưa nói riêng: TC-005, 015, 023, 024, 026, 032, 033, 034, 037, 038 |
| CẦN XÁC NHẬN | 7 | TC-002, 003, 016, 022, 025, 031, 041 |
| TỰ THÊM | 1 | TC-011 |
| MƠ HỒ | 1 | TC-039 |

- **Số dòng TỰ THÊM: 1** (TC-011). Phải xóa phần "mật khẩu phải trống" hoặc chuyển thành câu hỏi BA. Đây cũng là một trong các dòng đang ghi Không đạt dựa trên căn cứ không có.
- **Số dòng CẦN XÁC NHẬN: 7.** Trong đó chỉ TC-022 đã có câu hỏi soạn sẵn trong test-case.md (câu 2); TC-039 (nhóm MƠ HỒ) cũng có sẵn (câu 3). Sáu dòng CẦN XÁC NHẬN còn lại chưa có câu hỏi.
- **Cột Nguồn dẫn sai hoặc chưa đúng nhãn:** TC-004 (dẫn "luồng S01" thay vì S01-AC02), TC-010 (ghi "Suy luận" nhưng R04 nói thẳng), TC-012 (R08 không liên quan), TC-041 (TL-04 không liên quan).

### Requirement chưa có dòng nào phủ tới
1. **TL-02 và R06, "mọi loại lỗi đều tính":** không dòng nào trộn các loại lỗi (sai mật khẩu, mã không tồn tại, ô trống, mã quá dài) trong cùng chuỗi 10 lần. S02-AC06 còn ghi "Lần nhập này vẫn tính vào số lần sai".
2. **S02-AC08 và TL-12, "tài khoản khác vẫn đăng nhập bình thường":** TC-022 chỉ kiểm tài khoản kia sai một lần, chưa có ca nhập đúng ở tài khoản khác lúc P100001 đang bị chặn.
3. **S02 luồng chung:** "vẫn ở màn hình đăng nhập, địa chỉ không đổi" khi báo lỗi chưa có dòng kiểm.
4. **S04-AC04:** phần "Tab 1 không tự thay đổi cho đến khi bạn thao tác" TC-025 không kiểm.
5. **R08 (thuộc tính ô nhập) và M07 (nhãn bản English):** phủ yếu, chỉ có gián tiếp (TC-005 cho chữ chấm, TC-035 cho "mọi nhãn đổi"). Có thể là cố ý nếu coi là kiểm ở mức mã nguồn.
6. Ngoài ra, B4 (câu báo lúc đang bị chặn) và B15 (mốc tính 10 phút) chưa có dòng là đúng, vì BA chưa trả lời.

### Đánh giá chung: **CẦN SỬA**
Phần lõi bám sát câu trả lời của BA (34/43 dòng có trích dẫn). Chưa thể gửi vì còn 1 dòng TỰ THÊM đang bị tính là lỗi, 1 dòng MƠ HỒ, 7 dòng cần ghi nhãn xác nhận hoặc tách phần chưa có căn cứ, và hai chỗ hở về độ phủ (loại lỗi trộn, tài khoản khác lúc bị chặn). Không cần làm lại.
