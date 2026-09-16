# Dàn ý Bài 02: Mô hình tính toán Map-Reduce

## 1. Giới thiệu bài học

- Slide 1: tiêu đề bài, tên môn học và học kỳ theo yêu cầu người dùng.

- Slide 2: Nội dung; bổ sung mục thứ ba “Các ví dụ Map-Reduce” sau “Giới thiệu” và “Mô hình tính toán Map-Reduce”. Khi thêm section mới, bổ sung mục tương ứng vào slide này.

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
- Sau section ví dụ, section chính dự kiến: **Hệ thống Map-Reduce**. Dự kiến mạch: chia đầu vào và giao tác vụ → hàm phân phối khóa → chuyển và nhóm dữ liệu → theo dõi tác vụ → phát hiện lỗi và phục hồi Map/Reduce → phân biệt chạy lại và thực thi dự phòng. Làm rõ dữ liệu nào được lưu bền vững, dữ liệu trung gian nào cần tạo lại; nguồn MMDS 2.2.2, 2.2.5 và Dean–Ghemawat 3.1–3.6.
- Section chính riêng: **Chi phí và lợi ích của song song hóa**. Dự kiến mạch: quy ước mô hình chi phí → tổng công việc và thời gian hoàn thành → ví dụ tính tuần tự/song song với giả thiết rõ → chi phí truyền dữ liệu và Combine → giới hạn do lệch tải, tác vụ chậm và chi phí điều phối. Đối chiếu MMDS 2.5–2.6 trước khi soạn chi tiết.
- Hai section mới hiện ở mức kế hoạch; chưa dựng slide tiêu đề rỗng hoặc đưa vào mục lục. Cập nhật mục lục khi triển khai từng section như quy trình người dùng đang chỉ đạo. Thứ tự dự kiến Hệ thống trước Chi phí để mô hình chi phí dựa trên cơ chế đã học.

## 3. Các ví dụ Map-Reduce

Theo yêu cầu mới, triển khai section ví dụ trước hai section Hệ thống và Chi phí đã dự kiến. Section có một slide mở, mỗi bài năm slide cốt lõi và một slide ứng dụng, cùng một slide Câu hỏi kiểm tra cuối: tổng 20 slide sau khi thêm một slide ứng dụng cho mỗi bài.

| Cụm | Slide | Đặc tả và nguồn | Vai trò |
|---|---|---|---|
| Mở phần | lec02-s03-01 | Chọn khóa và giá trị từ mô hình ở section 2 | Cầu nối |
| Nhân ma trận–véc tơ | lec02-s03-02 đến 06 | MMDS 2.3.1 tr.31–32; 2.2.4 tr.27–28 | Cốt lõi |
| Số từ phân biệt | lec02-s03-07 đến 11 | MMDS bài 2.3.1(d), tr.40, đổi số nguyên thành từ theo yêu cầu; cơ chế nhóm và loại trùng | Cốt lõi |
| Trung bình cộng | lec02-s03-12 đến 16 | MMDS bài 2.3.1(b), tr.40; mở miền số nguyên sang số thực với giả thiết số học chính xác | Cốt lõi |
| Câu hỏi kiểm tra | lec02-s03-17 | Dùng lại ba ví dụ và các giả thiết đã xây | Kiểm tra |

Mỗi cụm: bài toán hình thức → ứng dụng → đặc điểm/ý tưởng → đặc tả Map, Reduce, Combine → ví dụ → chứng minh. Thứ tự này là chỉ dẫn cụ thể của người dùng, ưu tiên hơn chu trình mặc định ưu tiên ví dụ trước hình thức. Chi phí chi tiết sẽ ở section riêng.

Quyết định nguồn: dùng sách MMDS cho thuật toán ma trận và đề bài trung bình/đếm phân biệt; slide MMDS và Stanford xác nhận cơ chế Combine nhưng không cung cấp đủ cả ba cụm theo khuôn yêu cầu. Các lời giải và ví dụ chạy tay được diễn giải từ nguồn và tự kiểm, không gán số liệu minh họa cho sách. Không đưa đại số quan hệ/CSDL vào bài.

Ký hiệu: $p$ là số hàng, $q$ là số cột của ma trận, $A=(a_{ij})$, $v$ đầu vào, $y=Av$ đầu ra; $n$ là số văn bản hoặc số phần tử theo từng bài; $W_i$ tập từ văn bản $d_i$; $D$ số từ phân biệt; $g$ khóa chung cố định; $(s,c)$ là tổng và số lượng; $L$ danh sách giá trị cùng khóa; $\mu$ là trung bình.

Giả thiết: ma trận có đủ bản ghi tọa độ kể cả 0, mỗi tọa độ một lần; $v$ vừa RAM mỗi tác vụ Map. Trung bình có $n\geq1$, số học chính xác trong chứng minh. Đếm phân biệt dùng hai công việc, chương trình điều phối trả 0 khi không có từ. Combine đếm phân biệt ở công việc 1 giữ sự hiện diện, không cộng tần suất; công việc 2 cộng các số 1. Đây là một thiết kế, không khẳng định hai công việc là cận dưới.

Hình: sơ đồ chọn khóa, hai công việc loại trùng–đếm, trạng thái tổng–số lượng; slide đặc điểm có icon SVG kèm nhãn. Bảng chạy tay và công thức dựng bằng HTML/KaTeX. Chứng minh ưu tiên các bước suy luận, không ép thêm hình.

Lưu trữ ma trận: các bản ghi tọa độ được chia thành khối và nhân bản trên nhiều máy; phân biệt dữ liệu logic với bản sao vật lý. Hình dùng ba khối, hai bản sao mỗi khối chỉ để minh họa. Nguồn MMDS 2.1.2 và 2.3.1.

Trong ví dụ ma trận, Map nhận một khối B và duyệt các bản ghi (i,j,a_ij), yield(i,a_ij*v[j]); Combine và Reduce cũng dùng yield. Đây là điều chỉnh giao diện theo người dùng so với Map nhận một phần tử trong MMDS; tập cặp trung gian không đổi.

## Ứng dụng của ba ví dụ

Theo yêu cầu, đặt một slide ứng dụng ngay sau phát biểu bài toán của từng bài:
- lec02-s03-06a: chấm điểm tương đồng các trang web với một truy vấn. A có p hàng trang web và q cột từ; v là véc tơ truy vấn cùng trục. Chuẩn hóa mỗi hàng A và v về độ dài Euclid1 để y=Av cho điểm cosine; bước chọn trang điểm cao tách khỏi phép nhân.
- lec02-s03-11a: số từ phân biệt cho kích thước từ vựng, bằng số cột khi dùng nguyên bộ từ.
- lec02-s03-16a: dùng số lần xuất hiện từ của từng trang làm dãy đầu vào để tính số từ trung bình mỗi trang; trang rỗng vẫn góp vào số trang.

Nguồn bổ sung theo yêu cầu ứng dụng: Manning, Raghavan, Schütze, Introduction to Information Retrieval, 6.3.1–6.3.2, [tích vô hướng](https://nlp.stanford.edu/IR-book/html/htmledition/dot-products-1.html) và [truy vấn như véc tơ](https://nlp.stanford.edu/IR-book/html/htmledition/queries-as-vectors-1.html). Điều phối đã đọc và duyệt trước khi soạn; không thêm học phần TF-IDF hoặc chỉ mục tìm kiếm vào phạm vi.

Ví dụ nhân ma trận đổi thành A4×4 chia bốn khối2×2 B11/B12/B21/B22, v=[1,2,3,4], y=[9,8,9,11]. Mỗi hàng trải trên hai khối; Combine tạo tổng bộ phận và Reduce cộng hai tổng. Đặc tả tổng quát vẫn p×q.
