# Dàn ý Bài 02: Mô hình tính toán Map-Reduce

## 1. Giới thiệu bài học

- Slide 1: tiêu đề bài, tên môn học và học kỳ theo yêu cầu người dùng.

- Slide 2: Nội dung; hiện có một mục “Giới thiệu”. Khi thêm section mới, bổ sung mục tương ứng vào slide này.

- Slide 3: Bối cảnh Google, các máy phổ thông và ba bài toán có quy mô lịch sử: chỉ mục hơn 8 tỷ trang (2004), mẫu nhật ký truy vấn nén 450 GB (2005), kho 24 triệu trang với hơn 259 triệu liên kết (1998).
- Slide 4: Dữ liệu phân tán, song song hóa, tính toán gần dữ liệu, điều phối/chống lỗi/phục hồi trong suốt.

- Slide 5: Cộng n số tại các máy rồi gộp; khái quát bằng toán tử giao hoán và kết hợp.

- Slide 6: Mạng các rack và HDFS; tính toán gần khối dữ liệu, nhân bản qua rack để chịu lỗi.

Các section nội dung tiếp theo chưa được soạn.


## Động lực và yêu cầu mô hình

Duyệt một slide động lực trong section Giới thiệu, sau Nội dung. Giữ ba bài toán của Google từ bài báo2004, hình máy phổ thông và phần dữ liệu. Theo câu hỏi tiếp theo của người dùng, câu chốt phải làm rõ tính chất chung: xử lý tương tự trên từng phần/bản ghi, rồi gộp kết quả cục bộ. Không đưa chữ ký Map/Reduce, khóa hoặc cơ chế chuyển dữ liệu lên mặt slide này. Notes giải thích ba ví dụ và nhu cầu phối hợp máy; đây là động lực mô hình lập trình, không tuyên bố mọi bài toán dữ liệu lớn đều phù hợp. Hình ba máy minh họa, không số đo Google. Không thêm section mới, mục lục vẫn chỉ Giới thiệu. Không phục hồi deck/ghi chú đã xóa; không commit/push.

Theo các chỉ dẫn tiếp theo của người dùng, tách phần dẫn dắt thành slide 3 về Google và slide 4 về bốn yêu cầu: dữ liệu trên nhiều máy; tính toán song song; tính toán gần dữ liệu; phân chia, lập lịch, chống lỗi và phục hồi trong suốt đối với lập trình viên. Người dùng chỉ đạo từng slide nên chưa lập lại cả bài hoặc tài liệu tự học.
