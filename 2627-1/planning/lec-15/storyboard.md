# Storyboard Bài 15

## Hành trình khái niệm

Hai bảng lớn hơn bộ nhớ (`P00–P02`) → phép nối và mô hình I/O (`M00–M03`) → tái sử dụng phía trong theo tuple, nhóm khối hoặc chỉ mục (`N00–N11`) → tái sử dụng thứ tự bằng Sort-Merge (`S00–S09`) → tái sử dụng phân hoạch bằng Hash Join và Grace Hash Join (`H00–H15`) → chọn thuật toán theo điều kiện và trạng thái dữ liệu (`C00–C04`) → ba bài trực tiếp từ giáo trình (`X00–X09`).

## Chu trình trọng tâm

### Nested, Block Nested và Indexed Nested

- Tình huống/vấn đề: `N00`, dùng lại `student/takes` từ `P01`.
- Trực giác: `N01`, `N05`, `N09`.
- Ví dụ chạy tay: `N02`, `N06`, `N09`.
- Hình thức hóa: `N03`, `N07`, `N10–N11`.
- Thuật toán/tính đúng: `N03–N04`, `N07`, `N10–N11`.
- Ứng dụng/chi phí: `N04`, `N08`, `N11`.
- Kiểm tra: `N04`, `N08`, `N11`.
- Dữ liệu truyền: 5.000/10.000 tuple và 100/400 khối đi từ `P01` sang mọi công thức; ví dụ nhỏ khóa 1,2,4 đi từ `N02` sang bất biến `N03`.

### Sort-Merge Join

- Tình huống/vấn đề: `S00`.
- Trực giác: `S01`.
- Ví dụ chạy tay: `S02–S04`, gồm hai nhóm khóa 2 có kích thước 2 và 3.
- Hình thức hóa: `S05`.
- Thuật toán/tính đúng: `S05–S07`.
- Ứng dụng/chi phí: `S08`.
- Kiểm tra: `S09`.
- Dữ liệu truyền: các nhóm $G_r(2)$ và $G_s(2)$ tạo sáu cặp ở `S03–S07`.

### Hash Join trong bộ nhớ

- Tình huống/vấn đề: `H00`.
- Trực giác: `H01`.
- Ví dụ chạy tay: `H02`.
- Hình thức hóa: `H03`.
- Thuật toán/tính đúng: `H03–H04`.
- Ứng dụng/chi phí: `H05`.
- Kiểm tra: `H05`.
- Dữ liệu truyền: ngăn có hai tuple cùng khóa ở `H02` buộc bảng băm giữ bản sao và `H03` kiểm khóa thật.

### Grace Hash Join

- Tình huống/vấn đề: `H06`.
- Trực giác: `H07`.
- Ví dụ chạy tay: `H07`, `H10`, dùng khóa nhỏ để theo $h_1$, $h_2$, va chạm và cặp kết quả; `H08` dùng 100/400 khối cho điều kiện bộ nhớ.
- Hình thức hóa: `H09`.
- Thuật toán/tính đúng: `H11–H12`.
- Ứng dụng/chi phí: `H13–H14`, sau thuật toán và chứng minh.
- Kiểm tra: `H15`.
- Dữ liệu truyền: $p_h=6$ và $M-2=18$ đi từ `H08` sang chi phí 1.500/1.524 và seek 336 ở `H14`; điều kiện thật là $\max_i b_{s_i}\le M-2$.

## Bản đồ trang và thời lượng

| Trang | Phút | Bước tiến và sản phẩm | Nguồn |
|---|---:|---|---|
| P00 | 1 | Tên bài và nối từ Bài 12–13 | source.md B15 |
| P01 | 2 | Use case `student/takes`, 100/400 khối | slide 24 |
| P02 | 2 | Mục tiêu quan sát được và tuyến lựa chọn | slide 24–41 |
| M00 | 2 | Đặc tả equi-join, bản sao và miền không `NULL` | slide 24–25 |
| M01 | 2 | Ký hiệu $n,b,M,M-2,b_b$ | slide 7–9, 24, 28 |
| M02 | 3 | Tách truyền khối và seek | slide 7–9 |
| M03 | 2 | Chốt giả thiết chi phí và đầu ra không ghi đĩa | slide 7–9 |
| N00 | 2 | Theta join tổng quát và đường cơ sở | slide 25 |
| N01 | 2 | Trực giác vòng lặp theo tuple | slide 25 |
| N02 | 2 | Vết chạy tay trên ba tuple ngoài | slide 25; dữ liệu minh họa cấu trúc nguồn |
| N03 | 2 | Giả mã, bất biến, dừng | slide 25 |
| N04 | 3 | Công thức và ví dụ 2.000.100/1.000.400 | slide 26 |
| N05 | 2 | Chuyển đơn vị tái sử dụng sang khối | slide 27–28 |
| N06 | 2 | Vết chạy nhóm hai khối ngoài với hai khối trong | slide 27–28 |
| N07 | 2 | Giả mã và tính đúng Block Nested | slide 27–28 |
| N08 | 2 | Chi phí, chọn phía ngoài và kiểm tra | slide 28 ẩn |
| N09 | 2 | Vết khóa vắng và hai bản sao qua chỉ mục | slide 29–30 |
| N10 | 2 | Giả mã tự chứa, dừng và duyệt hết RID | slide 29–30 |
| N11 | 2 | Tính đúng và chi phí thời gian $b_r(t_T+t_S)+n_rc$ | slide 29–30; Bài 15.4 |
| S00 | 2 | Equi-join cho phép dùng thứ tự | slide 31 |
| S01 | 2 | Hai con trỏ trên hai dãy đã sắp | slide 31 |
| S02 | 3 | Vết tiến qua khóa 1 và dừng ở khóa 2 | slide 31 |
| S03 | 2 | Hai nhóm khóa 2 tạo sáu cặp | slide 31 |
| S04 | 3 | Hình tích hai nhóm | slide 31 |
| S05 | 3 | Giả mã theo nhóm | slide 31 |
| S06 | 2 | Bất biến và kết luận đúng | slide 31 |
| S07 | 3 | Nhóm trùng không vừa bộ nhớ | slide 31–32 |
| S08 | 2 | Quét $b_r+b_s$ và cộng chi phí sắp | slide 32; slide 17–23 |
| S09 | 2 | Kiểm tra điều kiện một lượt quét | slide 32 |
| H00 | 2 | Build input vừa bộ nhớ | slide 36, 39 |
| H01 | 2 | Xây nhỏ, dò lớn | slide 36 |
| H02 | 3 | Vết ngăn có bản sao và va chạm | slide 36 |
| H03 | 3 | Giả mã build–probe, kiểm khóa | slide 36 |
| H04 | 2 | Bất biến và tính đúng | slide 35–36 |
| H05 | 2 | Chi phí $b_r+b_s$ và kiểm tra | slide 39 |
| H06 | 3 | Build input không vừa bộ nhớ | slide 33–37 |
| H07 | 3 | Vết $h_1$ trên hai quan hệ nhỏ | slide 33–35; dữ liệu minh họa cơ chế |
| H08 | 3 | Sáu phân hoạch gần cân bằng và điều kiện cực đại | slide 37, 40; sửa lỗi nguồn |
| H09 | 3 | Điều kiện $s_i\le M-2$ và phía dò không cần vừa | slide 36–37; sửa slide 37 |
| H10 | 3 | Vết $h_2(k)=\lfloor k/2\rfloor\bmod2\ne h_1$, va chạm và kiểm khóa | slide 35–36; dữ liệu tiếp H07 |
| H11 | 3 | Hàng đợi với ba nhánh loại trừ và fallback khi không tiến triển | slide 36–38 |
| H12 | 3 | Chứng minh phân hoạch rời và xử lý đúng một lần | slide 35–38 |
| H13 | 2 | Skew, băm lại và fallback | slide 38 |
| H14 | 2 | Chi phí 1.500/1.524 transfer và 336 seek khi không đệ quy | slide 39–40 |
| H15 | 3 | Kiểm tra bộ nhớ, bản sao và skew | slide 37–41 |
| C00 | 3 | Bản đồ điều kiện nối → họ thuật toán | slide 24–41 |
| C01 | 3 | Bảng so sánh truyền khối, seek và điều kiện | slide 26, 28–32, 39 |
| C02 | 3 | Áp dụng cho `student/takes` theo ba trạng thái | slide 24–41 |
| C03 | 3 | Quy trình chọn thuật toán | tổng hợp nguồn |
| C04 | 3 | Kiểm tra cuối và chuyển recitation | Bài 15.3–15.5 |
| X00 | 0 | Giao ba bài; tổng 60 phút | Practice Exercises 15.3–15.5 |
| X01 | 10 | 15.3: đổi tuple sang khối, chốt $M$ | đề PDF 2; lời giải 112–113 |
| X02 | 10 | 15.3a–b: Nested và Block Nested | lời giải 113 |
| X03 | 8 | 15.3c: Merge Join; seek theo $P(b)$, $M,b_b$ | lời giải 113; slide 23 |
| X04 | 7 | 15.3d: Grace Hash; tách bộ đệm phân hoạch và vùng xây | lời giải 113; slide 37, 39 |
| X05 | 5 | 15.4: chỉ mục thứ cấp và bản sao | đề PDF 2 |
| X06 | 5 | 15.4: nối với lá rồi sắp địa chỉ | lời giải 113 |
| X07 | 5 | 15.4: điều kiện so với hybrid merge | lời giải 113 |
| X08 | 5 | 15.5: tối thiểu I/O với bộ nhớ vô hạn | đề PDF 2 |
| X09 | 5 | 15.5: $b_r+b_s$, $\min(b_r,b_s)+2$ khối | lời giải 114 |

## Câu nối và quyết định biên tập

- `M03→N00`: chốt mô hình chi phí trước khi so thuật toán.
- `N04→N05`: vòng lặp theo tuple đọc lại phía trong quá nhiều; giữ một nhóm khối ngoài để tái sử dụng.
- `N08→N09`: nếu phía trong có chỉ mục phù hợp, thay lượt quét bằng phép tra.
- `N11→S00`: nếu không có chỉ mục nhưng có thể sắp theo khóa, hai con trỏ thay nhiều phép tra ngẫu nhiên.
- `S09→H00`: equi-join còn cho phép gom khóa bằng băm thay vì thứ tự.
- `H05→H06`: khi phía xây không vừa RAM, ghi các phân hoạch ra đĩa rồi xử lý từng cặp.
- `H15→C00`: mọi lựa chọn quay lại điều kiện nối, bộ nhớ, trạng thái sắp/chỉ mục và skew.

Slide nguồn 28, 30, 35 và 40 bị ẩn nhưng chứa công thức hoặc ví dụ cần thiết nên vẫn được kiểm chứng và dùng có ghi nguồn. Các lỗi ở slide 33, 37, 39, 40 và 41 được sửa như `outline.md` mô tả.

Lời giải 15.3 dùng $q=M-1$ cho Block Nested-Loop Join; deck dùng $q=M-2$ khi đếm cả khối đầu ra. `X02` yêu cầu công bố quy ước rồi tính, không trộn hai giá trị. `X03–X04` chỉ giao sản phẩm trên mặt trang; đáp án nằm trong notes. Lời giải chính thức không cho một giá trị $M$, nên kết quả Merge/Hash giữ dạng biểu thức.
