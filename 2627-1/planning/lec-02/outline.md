# Bài 2: MapReduce và ngăn xếp xử lý dữ liệu lớn

## Mục tiêu và phạm vi

Sau phần giảng, sinh viên có thể:

1. Mô tả đúng ba giai đoạn map, nhóm theo khóa và reduce, đồng thời phân biệt phần do người dùng viết với phần hệ thống thực hiện.
2. Đặc tả và chứng minh tính đúng của chương trình MapReduce đếm từ.
3. Quyết định khi nào dùng bộ kết hợp, phân tích lệch tải và giải thích khôi phục tác vụ.
4. Phân biệt quy ước đầu vào tác vụ $I+M$ trong giáo trình MMDS với quy ước vào/ra $I+2M+O$ trong bộ trang chiếu chính thức MMDS.
5. Chọn MapReduce cho tác vụ phân tích theo lô phù hợp và định vị nó trong ngăn xếp xử lý dữ liệu lớn.

Phần giảng dài 120 phút. Phần bài tập trong cùng HTML dài 60 phút, dùng trực tiếp toàn bộ MMDS Bài 2.2.1(a–c), trang in 30, PDF trang 11 và Bài 2.3.1(a–d), trang in 40, PDF trang 21. Không dạy PageRank, phép nối hoặc nhân ma trận–vector.

## Kiến thức tiên quyết

- Bài 1: giới hạn bộ nhớ, lượt quét và chi phí di chuyển dữ liệu.
- Ánh xạ khóa–giá trị, bảng băm và phép nhóm.
- Bất biến vòng lặp và phép toán kết hợp, giao hoán.

## Dàn ý phần giảng

| Phần | Mã trang | Nội dung | Thời lượng |
|---|---|---|---:|
| Mở đầu | P00–P01 | Vị trí bài và sản phẩm học tập | 5 phút |
| Đưa tính toán đến dữ liệu | A00–A03 | Kho tài liệu lớn, hệ tệp phân tán, chia trách nhiệm, đặc tả đầu ra | 15 phút |
| Luồng khóa–giá trị | B00, B01, B05, B02, B03, B04, B06, B07 | Ví dụ Word Count, đặc tả, map, nhóm khóa, reduce, tính đúng, kiểm tra | 31 phút |
| Giảm dữ liệu trung gian | C00–C06 | Bộ kết hợp, điều kiện đại số, phân vùng, lệch tải, số tác vụ | 27 phút |
| Thực thi khi máy hỏng | D00–D05 | Điều phối, khôi phục, hai quy ước chi phí, tác động của bộ kết hợp | 23 phút |
| Ngăn xếp dữ liệu | E00–E04 | Các tầng phần mềm, phạm vi phù hợp, khuôn đặc tả, kiểm tra lựa chọn | 19 phút |
| **Tổng** |  |  | **120 phút** |

## Dàn ý phần bài tập

| Hoạt động | Mã trang | Nguồn | Thời lượng | Sản phẩm |
|---|---|---|---:|---|
| Giao việc Bài 2.2.1 | R01 | MMDS Bài 2.2.1, trang in 30, PDF trang 11 | 4 phút | Phân công ba ý (a–c) |
| Lệch reducer khi không có bộ kết hợp | R02 | MMDS Bài 2.2.1(a), trang in 30, PDF trang 11 | 8 phút | Lời giải ý (a) |
| So sánh 10 và 10.000 Reduce task | R03 | MMDS Bài 2.2.1(b), trang in 30, PDF trang 11 | 11 phút | Lời giải ý (b) |
| Lệch tải với 100 bộ kết hợp | R04 | MMDS Bài 2.2.1(c), trang in 30, PDF trang 11 | 9 phút | Lời giải ý (c) |
| Thiết kế cực đại | lec02-r06a | MMDS Bài 2.3.1(a), trang in 40, PDF trang 21 | 6 phút | Lời giải ý (a) |
| Thiết kế trung bình | lec02-r06b | MMDS Bài 2.3.1(b), trang in 40, PDF trang 21 | 8 phút | Lời giải ý (b) |
| Loại bản sao | R07 | MMDS Bài 2.3.1(c), trang in 40, PDF trang 21 | 6 phút | Lời giải ý (c) |
| Đếm số giá trị phân biệt | R08 | MMDS Bài 2.3.1(d), trang in 40, PDF trang 21 | 8 phút | Hai lượt MapReduce |
| **Tổng** |  |  | **60 phút** |  |

R00 và R05 là trang chuyển phần hoặc nêu nguyên văn phạm vi bài, không tính thời lượng. R01 dành 4 phút giao việc. Mặt trang R01–R08 chỉ giữ nội dung bài MMDS đã dịch; hướng dẫn tổ chức và chấm nằm trong ghi chú diễn giả. R06 được tách thành hai trang dọc lec02-r06a (6 phút) và lec02-r06b (8 phút); tổng phần bài tập vẫn 60 phút.

## Ánh xạ nguồn

MMDS 3e Chương 2 và bộ trang chiếu chính thức MMDS Chương 2 là nguồn chính cho luồng cốt lõi, ví dụ, thuật toán và bài tập. Stanford CS246 trang chiếu 50–60 và 66 được chọn cho DAG, Spark và giới hạn của xử lý theo lô vì trực quan và hiện thời hơn slide MMDS v2.1. Bộ trang chiếu MMDS được dùng theo giấy phép ghi ở trang 1; ghi công tại http://www.mmds.org. Không sao chép bố cục, CSS hoặc tài sản của nguồn; nội dung được Việt hóa và hình kỹ thuật được vẽ lại thành SVG.

| Nguồn | Phạm vi dùng | Mã trang |
|---|---|---|
| `sources/source.md` | Tên bài, mục tiêu, tiên quyết, việc tách MapReduce khỏi PageRank | P00–P01, E02–E04 |
| Bộ trang chiếu chính thức MMDS, Chương 2, trang chiếu 2–11 | Động cơ, cụm máy, hệ tệp phân tán, đưa tính toán đến dữ liệu | A00–A02 |
| Bộ trang chiếu chính thức MMDS, trang chiếu 12–20 | Kho Web, Word Count, luồng, giả mã và trách nhiệm môi trường | A03, B00–B07 |
| Bộ trang chiếu chính thức MMDS, trang chiếu 21–26 | Thực thi phân tán, bộ điều phối và khôi phục lỗi | D00–D02 |
| Bộ trang chiếu chính thức MMDS, trang chiếu 27–32 | Độ hạt tác vụ, bộ kết hợp và hàm phân vùng | C00–C06, D01 |
| Bộ trang chiếu chính thức MMDS, trang chiếu 34–35 | Tổng byte theo máy chủ và chuỗi năm từ | E04 |
| Bộ trang chiếu chính thức MMDS, trang chiếu 38–40 | Chi phí I/O $I+2M+O$ | D03–D04 |
| MMDS 3e, mục 2.1, trang in 21–24 | Hệ tệp phân tán, khối, bản sao, vị trí dữ liệu | A00–A02 |
| MMDS 3e, mục 2.2.1–2.2.3, trang in 25–27 | Mô hình ba bước, Word Count, map, nhóm khóa, reduce | A03, B00–B07 |
| MMDS 3e, mục 2.2.4–2.2.5, trang in 27–29 | Bộ kết hợp, reducer, Reduce task, lệch tải, thực thi | C00–C06, D01 |
| MMDS 3e, mục 2.2.6, trang in 30 | Khôi phục sau lỗi máy | D00–D02 |
| MMDS 3e, mục 2.4, trang in 41–50 | Hệ luồng công việc và Spark | E00–E01 |
| Stanford CS246, trang chiếu 50–60 và 66 | DAG, Spark và giới hạn của MapReduce theo lô | E00–E02 |
| MMDS 3e, mục 2.5.1, trang in 53–55 | Chi phí truyền thông là tổng kích thước đầu vào tác vụ | D03–D04 |
| MMDS 3e, Bài 2.2.1, trang in 30, PDF trang 11 | Toàn bộ bài tập lệch tải | R01–R04 |
| MMDS 3e, Bài 2.3.1, trang in 40, PDF trang 21 | Toàn bộ bài tập thiết kế | R05–R08, lec02-r06a, lec02-r06b |

Không dùng bộ trang chiếu chính thức MMDS trang chiếu 36–37 vì chứa phép nối, hoặc 43–48 vì mô tả phần mềm Hadoop cũ và tài liệu lịch sử ngoài mục tiêu. Không dùng các mục MMDS 2.3.1–2.3.10 về nhân ma trận và đại số quan hệ. Bài tập 2.3.1 chỉ được dùng trong phần recitation theo chỉ định.

## Thuật toán trọng tâm

### Đặc tả Word Count

- Đầu vào: tập tài liệu $D$ đã có quy tắc tách từ xác định; mỗi tài liệu là một phần tử không bị chia qua hai khối.
- Đầu ra: với mỗi từ $w$ đã xuất hiện, đúng một cặp $(w,c(w))$.
- Điều kiện trước: phép tách từ xác định và bộ đếm không tràn.
- Điều kiện sau: $c(w)=\sum_{d\in D}\operatorname{số\_lần}(w,d)$.
- Map: mỗi lần gặp $w$ phát $(w,1)$.
- Nhóm theo khóa: hệ thống tạo $(w,[1,\ldots,1])$ chứa mọi đóng góp của $w$.
- Reduce: cộng danh sách giá trị và phát $(w,c(w))$.
- Dừng: map dừng sau số từ hữu hạn của tài liệu; reduce dừng sau độ dài danh sách hữu hạn.
- Biên: đầu vào rỗng cho đầu ra rỗng; tài liệu rỗng không phát cặp.

### Lập luận tính đúng

Mỗi lần xuất hiện của $w$ tạo đúng một giá trị 1. Bảo đảm nhóm theo khóa đặt toàn bộ và chỉ các giá trị có khóa $w$ vào một reducer. Sau $j$ bước, biến tổng của reducer bằng tổng $j$ giá trị đầu. Khi dừng, tổng bằng số lần $w$ xuất hiện trong toàn bộ đầu vào.

### Bộ kết hợp và chi phí

- Với Word Count, phép cộng kết hợp và giao hoán nên mỗi Map task có thể thay nhiều cặp $(w,1)$ bằng $(w,m)$.
- Bộ kết hợp không loại bỏ bước nhóm và reduce toàn cục.
- Trạng thái phải đóng dưới phép gộp và giữ cùng ngữ nghĩa qua mọi thứ tự, mọi cây gộp.
- Ký hiệu: $I$ là tổng đầu vào map, $M$ là tổng dữ liệu trung gian, $O$ là tổng đầu ra reduce.
- MMDS đếm tổng đầu vào của tác vụ: $I+M$ cho một công việc, thường bỏ đầu ra cuối nhỏ.
- Bộ trang chiếu chính thức MMDS, trang chiếu 38–40, đếm toàn bộ I/O: $I+2M+O$ vì dữ liệu trung gian được ghi rồi đọc. Hai công thức là mô hình I/O của tác vụ, không chỉ đếm byte qua mạng.

## Thuật ngữ và ký hiệu

| Thuật ngữ hoặc ký hiệu | Nghĩa dùng trong bài |
|---|---|
| map, reduce, MapReduce | Tên thao tác và mô hình thuật toán đã ổn định; giữ nguyên tiếng Anh |
| Map task, Reduce task | Đơn vị lập lịch; phân biệt với một lần gọi mapper hoặc reducer. Bài dùng nhất quán "Reduce task", không dùng "tác vụ reduce" |
| bộ kết hợp | Combiner; phép tổng hợp cục bộ trước khi chuyển dữ liệu |
| nhóm theo khóa | Group by key; gồm phân vùng, trộn và sắp theo mô hình nguồn |
| lệch tải | Skew; chênh lệch khối lượng xử lý giữa reducer hoặc tác vụ |
| $I,M,O$ | Tổng kích thước đầu vào, dữ liệu trung gian và đầu ra |
| Hadoop, HDFS, Spark | Tên riêng phần mềm; không dịch |

## Hình được vẽ lại

| Tệp | Mã trang | Căn cứ |
|---|---|---|
| `he-tep-phan-tan.svg` | A01 | Trang chiếu MMDS 9–11; MMDS mục 2.1 và 2.2.5 |
| `luong-mapreduce.svg` | B01 | Trang chiếu MMDS 18–19; MMDS Hình 2.2 và Ví dụ 2.1–2.2 |
| `phan-vung-va-bo-ket-hop.svg` | C01 | Trang chiếu MMDS 30–32; MMDS mục 2.2.2 và 2.2.4 |
| `khoi-phuc-tac-vu.svg` | D02 | Trang chiếu MMDS 23–26; MMDS mục 2.2.6 |
| `ngan-xep-du-lieu.svg` | E01 | MMDS mục 2.4; Stanford CS246 trang chiếu 51–59 |

Mọi hình là SVG cục bộ có `role="img"`, `title`, `desc` và mô tả thay thế trong HTML. Không dùng ảnh raster.
