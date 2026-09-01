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
- Ví dụ chạy tay: `H07`, `H10`, dùng khóa nhỏ để theo $h_1$, $h_2$, va chạm và cặp kết quả; `H08` dùng 100/400 khối cho pha phân hoạch.
- Hình thức hóa: `H08–H09`, tách bộ đệm phân hoạch khỏi pha xây–dò.
- Thuật toán/tính đúng: `H13`, `H11–H12`.
- Ứng dụng/chi phí: `H14`, sau đường lui và chứng minh.
- Kiểm tra: `H15`.
- Dữ liệu truyền: $M=20$, $b_b=2$, $p_h=7$, $\alpha=1{,}2$ và các kích thước $15;15;14;14;14;14;14$ đi từ `H08–H09` sang chi phí 1.500/1.528 và 500 seek tổng ở `H14`; $b_b$ là hệ số đọc/ghi liên tiếp, độc lập với $b_{in}=b_{out}=1$ của pha xây–dò.

## Bản đồ trang và thời lượng

| Trang | Phút | Bước tiến và sản phẩm | Nguồn |
|---|---:|---|---|
| P00 | 1 | Tên bài và nối từ Bài 12–13 | source.md B15 |
| P01 | 2 | Use case `student/takes`, 100/400 khối | slide 24 |
| P02 | 2 | Mục tiêu quan sát được và tuyến lựa chọn | slide 24–41 |
| M00 | 2 | Đặc tả equi-join, bản sao và miền không `NULL` | slide 24–25 |
| M01 | 2 | Ký hiệu $n,b,M,q,b_b,p_h,\alpha$; không có vùng $M-2$ toàn cục | slide 7–9, 24, 28, 37–40 |
| M02 | 3 | Tách truyền khối và seek | slide 7–9 |
| M03 | 2 | Chốt giả thiết chi phí và đầu ra không ghi đĩa | slide 7–9 |
| N00 | 2 | Theta join tổng quát và đường cơ sở | slide 25 |
| N01 | 2 | Trực giác vòng lặp theo tuple | slide 25 |
| N02 | 2 | Vết chạy tay trên ba tuple ngoài | slide 25; dữ liệu minh họa cấu trúc nguồn |
| N03 | 2 | Giả mã, bất biến, dừng | slide 25 |
| N04 | 3 | Công thức và ví dụ 2.000.100/1.000.400 | slide 26 |
| N05 | 2 | Chuyển đơn vị tái sử dụng sang khối; phân biệt $q=M-2$ và $q=M-1$ | slide 27–28; lời giải 15.3 |
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
| S08 | 2 | Vật chất hóa hai dãy đã sắp rồi quét $b_r+b_s$ | slide 32; slide 17–23; lời giải 15.3 |
| S09 | 2 | Kiểm tra điều kiện một lượt quét | slide 32 |
| H00 | 2 | Build input vừa bộ nhớ | slide 36, 39 |
| H01 | 2 | Xây nhỏ, dò lớn | slide 36 |
| H02 | 3 | Vết ngăn có bản sao và va chạm | slide 36 |
| H03 | 3 | Giả mã build–probe, kiểm khóa | slide 36 |
| H04 | 2 | Bất biến và tính đúng | slide 35–36 |
| H05 | 2 | Chi phí $b_r+b_s$ và kiểm tra | slide 39 |
| H06 | 3 | Build input không vừa bộ nhớ | slide 33–37 |
| H07 | 3 | Vết $h_1$ trên hai quan hệ nhỏ | slide 33–35; dữ liệu minh họa cơ chế |
| H10 | 3 | Vết $h_2(k)=\lfloor k/2\rfloor\bmod2\ne h_1$, va chạm và kiểm khóa | slide 35–36; dữ liệu tiếp H07 |
| H08 | 3 | Pha phân hoạch: $100\to15;15;14;14;14;14;14$ và $(p_h+1)b_b=16\le20$ | slide 37, 40; sửa lỗi nguồn |
| H09 | 3 | Pha xây–dò tái dùng bộ nhớ: $\alpha\max_i b_{s_i}+b_{in}+b_{out}\le M$ | slide 36–37; bổ sung phụ trội |
| H13 | 2 | Skew, băm lại và fallback | slide 38 |
| H11 | 3 | Hàng đợi với ba nhánh loại trừ và fallback khi không tiến triển | slide 36–38 |
| H12 | 3 | Chứng minh phân hoạch rời và xử lý đúng một lần | slide 35–38 |
| H14 | 2 | Chi phí 1.500/1.528 transfer và 500 seek khi không đệ quy | slide 39–40 |
| H15 | 3 | Kiểm tra bộ nhớ, bản sao và skew | slide 37–41 |
| C00 | 3 | Bản đồ điều kiện nối → họ thuật toán | slide 24–41 |
| C01 | 3 | Bảng so sánh truyền khối, seek và điều kiện | slide 26, 28–32, 39 |
| C02 | 3 | Áp dụng cho `student/takes` theo ba trạng thái | slide 24–41 |
| C03 | 3 | Quy trình chọn thuật toán | tổng hợp nguồn |
| C04 | 3 | Kiểm tra cuối và chuyển recitation | Bài 15.3–15.5 |
| X00 | 0 | Giao ba bài; tổng 60 phút | Practice Exercises 15.3–15.5 |
| X01 | 10 | 15.3: đổi tuple sang khối, chốt $M$ | đề PDF 2; lời giải 112–113 |
| X02 | 10 | 15.3a–b: Nested và Block Nested | lời giải 113 |
| X03 | 8 | 15.3c: Merge Join vật chất hóa; transfer và seek theo $P(b),M,b_b$ | lời giải 113; slide 23 |
| X04 | 7 | 15.3d: Grace Hash; tách bộ đệm phân hoạch và điều kiện bảng băm có $\alpha$ | lời giải 113; slide 37, 39 |
| X05 | 5 | 15.4: chỉ mục thứ cấp và bản sao | đề PDF 2 |
| X06 | 5 | 15.4: nối với lá rồi sắp địa chỉ | lời giải 113 |
| X07 | 5 | 15.4: so tổng I/O với Hybrid Merge, không suy chỉ từ kích thước | lời giải 113; hiệu chỉnh điều kiện |
| X08 | 5 | 15.5: tối thiểu I/O với bộ nhớ vô hạn | đề PDF 2 |
| X09 | 5 | 15.5: $b_r+b_s$, $\min(b_r,b_s)+2$ khối | lời giải 114 |

## Câu nối và quyết định biên tập

- `M03→N00`: chốt mô hình chi phí trước khi so thuật toán.
- `N04→N05`: vòng lặp theo tuple đọc lại phía trong quá nhiều; giữ một nhóm khối ngoài để tái sử dụng.
- `N08→N09`: nếu phía trong có chỉ mục phù hợp, thay lượt quét bằng phép tra.
- `N11→S00`: nếu không có chỉ mục nhưng có thể sắp theo khóa, hai con trỏ thay nhiều phép tra ngẫu nhiên.
- `S09→H00`: equi-join còn cho phép gom khóa bằng băm thay vì thứ tự.
- `H05→H06`: khi điều kiện vùng xây không giữ, ghi các phân hoạch ra đĩa rồi xử lý từng cặp.
- `H07→H10→H08`: vết khóa nhỏ xác nhận tính đúng trước khi chuyển sang bố trí pha phân hoạch ở quy mô nguồn.
- `H09→H13→H11`: khi pha xây–dò không vừa, nhận diện skew rồi chọn một trong ba nhánh hữu hạn.
- `H15→C00`: mọi lựa chọn quay lại điều kiện nối, bộ nhớ, trạng thái sắp/chỉ mục và skew.

Slide nguồn 28, 30, 35 và 40 bị ẩn nhưng chứa công thức hoặc ví dụ cần thiết nên vẫn được kiểm chứng và dùng có ghi nguồn. Các lỗi ở slide 33, 37, 39, 40 và 41 được sửa như `outline.md` mô tả.

Lời giải 15.3 dùng $q=M-1$ cho Block Nested-Loop Join khi không giữ riêng đầu ra; bố trí vật chất hóa của slide 28 cho $q=M-2$. `X02` yêu cầu công bố quy ước rồi tính. `X03` chốt sắp xếp vật chất hóa để bám lời giải chính thức; `X04` tách bộ đệm phân hoạch khỏi dung lượng bảng băm. Lời giải không cho một giá trị $M$, nên kết quả Merge/Hash của bài tập giữ dạng biểu thức.

## Hành trình của ghi chú tự học

| `note-topic-id` | Kết nối vào → đầu ra | Kiến thức đầu vào | Thành phần trình bày |
|---|---|---|---|
| `L15-N01` | Bài 12–13 → mô hình chung cho mọi phép nối | khối, bộ đệm, quan hệ | vai trò, đặc tả, ví dụ `student/takes`, mô hình chi phí, kiểm tra |
| `L15-N02` | đường cơ sở → tái sử dụng theo khối | vòng lặp lồng | vết tuple, giả mã, bất biến, dừng, chi phí |
| `L15-N03` | quét lại theo tuple → nhóm $q$ khối | `L15-N02`, bố trí bộ đệm | hai bố trí, vết khối, tính đúng, chi phí |
| `L15-N04` | quét phía trong → tra chỉ mục | B+-Tree Bài 13 | vết bản sao/khóa không khớp, giả mã, chi phí thời gian |
| `L15-N05` | tra ngẫu nhiên → thứ tự khóa | External Merge Sort Bài 12 | vết đầy đủ, nhóm trùng, giả mã, bất biến, chi phí vật chất hóa |
| `L15-N06` | thứ tự → gom ngăn trong RAM | băm Bài 13 | điều kiện bộ nhớ, va chạm, bản sao, build–probe, chứng minh |
| `L15-N07` | phía xây tràn → phân hoạch hai đầu vào | `L15-N06` | vết $h_1/h_2$, hai bố trí bộ đệm, điều kiện cực đại |
| `L15-N08` | phân hoạch lệch → đường lui hữu hạn | `L15-N07` | hàng đợi ba nhánh, ví dụ tiến triển, chứng minh, cận I/O |
| `L15-N09` | sáu thuật toán → quyết định có điều kiện | `L15-N02`–`N08` | bảng và bản đồ lựa chọn, kiểm tra đơn vị |
| `L15-N10` | quy tắc lựa chọn → Bài 15.3–15.4 | toàn bộ mô hình chi phí | dữ kiện nguồn, phép tính, gợi ý và lời giải |
| `L15-N11` | trường hợp đủ RAM → cận dưới đọc | `L15-N06`, cận I/O | thuật toán hai bước, chứng minh cận, bài kiểm tra |

Ghi chú dùng lại dữ kiện `student/takes` từ mở bài đến Nested, Grace và bảng chọn. Vết Sort-Merge truyền cùng hai dãy qua so khóa, tích nhóm và điều kiện dừng; vết Grace truyền cùng tuple qua phân hoạch, bảng băm, va chạm và phép so khóa thật. Các mục ghi chú không mang mã trang hay thời lượng vì đây là sản phẩm tự học.
