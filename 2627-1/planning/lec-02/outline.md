# Dàn ý Bài 02: Mô hình tính toán Map-Reduce

## 1. Giới thiệu bài học

- Slide 1: tiêu đề bài, tên môn học và học kỳ theo yêu cầu người dùng.

- Slide 2: Nội dung; hiện có hai mục “Giới thiệu” và “Mô hình tính toán Map-Reduce”. Khi thêm section mới, bổ sung mục tương ứng vào slide này.

- Slide 3: Bối cảnh Google, các máy phổ thông và ba bài toán có quy mô lịch sử: chỉ mục hơn 8 tỷ trang (2004), mẫu nhật ký truy vấn nén 450 GB (2005), kho 24 triệu trang với hơn 259 triệu liên kết (1998).
- Slide 4: Dữ liệu phân tán, song song hóa, tính toán gần dữ liệu, điều phối/chống lỗi/phục hồi trong suốt.

- Slide 5: Cộng n số tại các máy rồi gộp; khái quát bằng toán tử giao hoán và kết hợp.

- Slide 6: Mạng các rack và HDFS; tính toán gần khối dữ liệu, nhân bản qua rack để chịu lỗi.

## 2. Mô hình tính toán Map-Reduce

- Khả năng của mô hình: xử lý dữ liệu phân tán, song song hóa, tính toán gần dữ liệu, điều phối và phục hồi tự động. Chưa mô tả cách làm theo yêu cầu người dùng.
- Ví dụ xuyên suốt: đếm tần suất xuất hiện từ trong n văn bản. Bước đầu đặc tả đầu vào, đầu ra, số đếm và khó khăn khi dữ liệu lớn.
- Hai hàm cho ví dụ đếm từ: Map phát (từ,1), hệ thống nhóm, Reduce cộng số đếm.
- Hệ thống phân chia/giao tác vụ và chuyển dữ liệu theo từ; phân biệt tác vụ với máy.
- Chạy tay hai văn bản “mèo chó mèo” và “chó chim” qua Map, nhóm, Reduce.
- Hình thức hóa chữ ký Map và Reduce, đối chiếu ví dụ đếm từ.
- Quy tắc nhóm/phân phối khóa; các pha logic của một công việc.
- Giả mã mô hình tổng quát, giữ phần tử lặp, phân biệt tác vụ logic và lượt thực thi.


## Động lực và yêu cầu mô hình

Duyệt một slide động lực trong section Giới thiệu, sau Nội dung. Giữ ba bài toán của Google từ bài báo2004, hình máy phổ thông và phần dữ liệu. Theo câu hỏi tiếp theo của người dùng, câu chốt phải làm rõ tính chất chung: xử lý tương tự trên từng phần/bản ghi, rồi gộp kết quả cục bộ. Không đưa chữ ký Map/Reduce, khóa hoặc cơ chế chuyển dữ liệu lên mặt slide này. Notes giải thích ba ví dụ và nhu cầu phối hợp máy; đây là động lực mô hình lập trình, không tuyên bố mọi bài toán dữ liệu lớn đều phù hợp. Hình ba máy minh họa, không số đo Google. Không thêm section mới, mục lục vẫn chỉ Giới thiệu. Không phục hồi deck/ghi chú đã xóa; không commit/push.

Theo các chỉ dẫn tiếp theo của người dùng, tách phần dẫn dắt thành slide 3 về Google và slide 4 về bốn yêu cầu: dữ liệu trên nhiều máy; tính toán song song; tính toán gần dữ liệu; phân chia, lập lịch, chống lỗi và phục hồi trong suốt đối với lập trình viên. Người dùng chỉ đạo từng slide nên chưa lập lại cả bài hoặc tài liệu tự học.

## Bổ sung Combine theo yêu cầu

Thêm sau đặc tả mô hình cơ bản: gộp cục bộ bằng Combine, dùng lại ví dụ đếm từ, giảm 5 xuống 4 cặp truyền. Nguồn MMDS 2.2.4, trang 27–28. Giữ khóa và kiểu trung gian; phép gộp kết hợp, giao hoán và tương thích với Reduce. Đây là điều kiện đủ cho cách gộp trình bày, không phải đặc tính bắt buộc của mọi Reduce. Một slide cùng section 2; không thêm mục lục.

## Chốt cấu trúc tiếp theo theo yêu cầu giảng viên

- Kết section 2 “Mô hình tính toán Map-Reduce” bằng slide “Câu hỏi kiểm tra” (`lec02-s02-12`); chỉ kiểm tra kiến thức vừa học.
- Section chính tiếp theo: **Hệ thống Map-Reduce**. Dự kiến mạch: chia đầu vào và giao tác vụ → hàm phân phối khóa → chuyển và nhóm dữ liệu → theo dõi tác vụ → phát hiện lỗi và phục hồi Map/Reduce → phân biệt chạy lại và thực thi dự phòng. Làm rõ dữ liệu nào được lưu bền vững, dữ liệu trung gian nào cần tạo lại; nguồn MMDS 2.2.2, 2.2.5 và Dean–Ghemawat 3.1–3.6.
- Section chính riêng: **Chi phí và lợi ích của song song hóa**. Dự kiến mạch: quy ước mô hình chi phí → tổng công việc và thời gian hoàn thành → ví dụ tính tuần tự/song song với giả thiết rõ → chi phí truyền dữ liệu và Combine → giới hạn do lệch tải, tác vụ chậm và chi phí điều phối. Đối chiếu MMDS 2.5–2.6 trước khi soạn chi tiết.
- Hai section mới hiện ở mức kế hoạch; chưa dựng slide tiêu đề rỗng hoặc đưa vào mục lục. Cập nhật mục lục khi triển khai từng section như quy trình người dùng đang chỉ đạo. Thứ tự dự kiến Hệ thống trước Chi phí để mô hình chi phí dựa trên cơ chế đã học.
