# Storyboard Bài 8

## Hành trình khái niệm

- **Lấy mẫu theo khóa:** tình huống P01 → vấn đề K00–K01 → trực giác và ví dụ K02 → đặc tả K03 → thuật toán K04 → lập luận đúng K05 → ứng dụng K06, chi phí K07 → kiểm tra K08.
- **Lấy mẫu hồ chứa:** tình huống P01, R00 → phân biệt mục tiêu R01 → ví dụ chạy tay R03 → đặc tả R02 → thuật toán R04 → bất biến và chứng minh R05–R07 → chi phí, giả thiết ngẫu nhiên và kiểm tra R08.
- **Bloom filter:** tình huống B00 → vị trí trong hệ thống B02 → trực giác và ví dụ B05 → đặc tả B01 → thuật toán B03–B04 → bảo đảm B06 → hình thức hóa và xác suất B07–B11 → chi phí, giới hạn và kiểm tra B12.

Tình huống xuyên suốt là dòng truy vấn `(người dùng, truy vấn, thời gian)` không biết trước độ dài và không thể giữ toàn bộ lịch sử. Đầu ra cần có là mẫu phục vụ thống kê truy vấn lặp hoặc quyết định loại sớm khóa không thuộc tập. Tình huống trở lại ở K00–K08 để bảo toàn nhóm theo người dùng, R00–R08 để giữ đúng số vị trí và C01 để chọn cấu trúc. Bloom dùng thêm tình huống một tỷ địa chỉ cho phép và một gigabyte từ MMDS trang 139.

## Bản đồ chu trình theo cụm

| Cụm | Bước và mã trang | Đầu vào → sản phẩm | Dữ kiện truyền | Gộp hoặc không áp dụng | Câu nối | Phút |
|---|---|---|---|---|---|---:|
| Mô hình dòng | tình huống P01; vấn đề–hình thức A00–A02; ứng dụng–kiểm tra A03–A04 | dòng bộ chưa biết độ dài, bộ nhớ hữu hạn → hợp đồng và bốn trục chi phí | bộ `(người dùng, truy vấn, thời gian)`, đầu ra mẫu/lọc | trực giác và hình thức hóa gộp ở A00–A01 vì đây là mô hình, không phải thuật toán | Từ giới hạn chung, chọn trạng thái theo truy vấn. | 19 |
| Mẫu theo khóa | tình huống–vấn đề K00–K01; trực giác–ví dụ K02; hình thức K03; thuật toán K04; đúng K05; ứng dụng–chi phí K06–K07; kiểm tra K08 | bộ $t$, khóa $K(t)$, $a,b,h$ → mẫu nhất quán theo khóa | $x,d$ ở K01 tạo nhu cầu; cùng `An`, $a=3,b=10$ ở K02 truyền sang quy tắc $h(K)<a$ | ví dụ và trực giác gộp K02; ứng dụng tách K06–K07 để không lộ bài tập | Một quyết định cố định cho khóa thay lấy độc lập từng bộ. | 26 |
| Hồ chứa | tình huống R00; vấn đề R01; ví dụ R03; hình thức R02; thuật toán R04; đúng R05–R07; ứng dụng–chi phí–kiểm tra R08 | dòng vị trí, $s$, số ngẫu nhiên đều → đúng $s$ vị trí với xác suất biên $s/n$ | vết $s=2$, các giá trị $j$ và trạng thái $S$ ở R03 truyền sang đặc tả, giả mã và quy nạp | ứng dụng, chi phí và kiểm tra gộp R08 vì cùng kiểm tra giả thiết mô hình RAM/ngẫu nhiên | Vết chạy cho thấy trạng thái; đặc tả sau đó nêu bảo đảm cần chứng minh. | 26 |
| Bloom filter | tình huống B00; vấn đề B02; trực giác–ví dụ B05; hình thức B01; thuật toán B03–B04; đúng B06; xác suất–chi phí B07–B11; kiểm tra B12 | $S,m,n,k,h_i$ → “chắc chắn không” hoặc “có thể thuộc” | ví dụ 11 bit truyền chỉ số, va chạm và hai câu trả lời sang đặc tả/giả mã; $q$ ở B07 truyền sang FPR B08 và tối ưu B10 | trực giác và ví dụ gộp B05; ứng dụng và kiểm tra gộp B12 | Ví dụ cụ thể được khái quát thành hợp đồng, rồi phân tích tỷ lệ dương giả. | 44 |
| Tổng hợp | ứng dụng C00–C01; nguồn C02 | ba loại truy vấn → chọn đúng cấu trúc và nêu giới hạn | tình huống P01 cùng các bảo đảm K05, R05–R07, B06 | không áp dụng bước thuật toán mới vì chỉ đối chiếu sản phẩm | Chuyển từ lựa chọn cấu trúc sang bài tập đúng nguồn. | 5 |

Tổng phần giảng theo các cụm: **120 phút**.

## Trang phần giảng

| ID | Phút | Bước tiến và sản phẩm | Nguồn |
|---|---:|---|---|
| P00 | 0 | Nhận diện bài và giới hạn phạm vi. | `sources/source.md`; MMDS Ch.4 |
| P01 | 4 | Mở bằng dòng truy vấn; nêu dữ liệu, giới hạn bộ nhớ, đầu ra và câu kiểm tra. | MMDS tr.136–138; Streams 1 tr.13–16 |
| P02 | 2 | Nêu ba sản phẩm quan sát được. | `sources/source.md` |
| A00 | 3 | Vẽ mô hình dòng, bộ nhớ hữu hạn và truy vấn. | MMDS tr.133–135; Streams 1 tr.6 |
| A01 | 3 | Đặc tả đầu vào, trạng thái, đầu ra và một lượt. | MMDS tr.133–135 |
| A02 | 3 | Đặt bốn trục chi phí. | MMDS tr.135 |
| A03 | 2 | Tách ba sản phẩm và trạng thái. | MMDS 4.2–4.3; Streams 1 tr.12 |
| A04 | 2 | Kiểm tra chọn cấu trúc theo truy vấn. | tổng hợp nguồn |
| K00 | 3 | Nêu nhu cầu giữ quan hệ theo khóa. | MMDS 4.2.1 |
| K01 | 4 | Định nghĩa $x,d$ theo giá trị truy vấn phân biệt; phân biệt tỷ lệ đích với tỷ số từ số đếm kỳ vọng. | MMDS tr.136–137; `stanford-cs246/16-streams.pdf`, CS246 26/02/2026, tr.13–14 |
| K02 | 3 | Ví dụ 30%: cùng khóa nhận cùng quyết định. | Streams 1 tr.15–16; ví dụ dựng từ cơ chế nguồn |
| K03 | 3 | Hình thức hóa $h(K)<a$, miền băm và điều kiện sau; $h$ phải phân bố đều trên toàn miền để tỷ lệ $a/b$ được bảo đảm. | MMDS 4.2.2–4.2.3 |
| K04 | 3 | Giả mã và điều kiện dừng. | MMDS 4.2.2–4.2.3 |
| K05 | 3 | Chứng minh nhất quán và xác suất $a/b$. | MMDS 4.2.2–4.2.3 |
| K06 | 3 | Nêu quy trình xác định khóa từ đơn vị thống kê qua tình huống truy vấn theo người dùng, không lộ đáp án Ex.4.2.1. | MMDS 4.2.1–4.2.3 |
| K07 | 2 | Phân tích chi phí và giới hạn kích thước. | MMDS 4.2.4 |
| K08 | 2 | Kiểm tra biên ngưỡng và khóa nặng. | MMDS 4.2.3 |
| R00 | 3 | Đặt tình huống bộ nhớ chỉ đủ $s$ vị trí. | Streams 1 tr.18 |
| R01 | 2 | Phân biệt khóa với vị trí. | Streams 1 tr.12,18 |
| R03 | 3 | Chạy tay $s=2$ với trạng thái trung gian. | Streams 1 tr.18–19; dãy j minh họa cơ chế nguồn |
| R02 | 3 | Từ vết chạy, đặc tả $s\ge1$, $n<s$, $n\ge s$ và xác suất biên. | Streams 1 tr.18–19 |
| R04 | 4 | Giả mã $j$ đều trong $1,\ldots,n$. | Streams 1 tr.19 |
| R05 | 3 | Phát biểu bất biến và cơ sở quy nạp. | Streams 1 tr.19–20 |
| R06 | 2 | Chứng minh xác suất của phần tử mới. | Streams 1 tr.20–21 |
| R07 | 3 | Chứng minh xác suất của phần tử cũ. | Streams 1 tr.21 |
| R08 | 3 | Nêu $\Theta(s)$ và $\Theta(1)$ trong mô hình RAM, giả thiết bộ sinh số ngẫu nhiên và kiểm tra. | Streams 1 tr.18–21 |
| B00 | 3 | Mở bằng một tỷ địa chỉ và một gigabyte. | MMDS tr.139–140; Streams 2 tr.4–8 |
| B02 | 3 | Đặt Bloom trước phép tra chính xác. | Streams 2 tr.6–7 |
| B05 | 4 | Định nghĩa $h_1,h_2$ (bit lẻ/chẵn vị trí 1-based từ phải) và chạy ví dụ 11 bit (mảng hiển thị chỉ số 0–10 từ trái); chỉ bit 7 va chạm, bit 3 bằng 0 loại 118. | `stanford-cs246-2017/streams-2.pdf`, Ullman 01/03/2017, tr.5–8 |
| B01 | 3 | Khái quát ví dụ thành đặc tả $n,m,k$ và hai loại câu trả lời. | MMDS 4.3.2 |
| B03 | 4 | Giả mã xây dựng và chi phí. | MMDS 4.3.2 |
| B04 | 4 | Giả mã truy vấn và dừng sớm. | MMDS 4.3.2 |
| B06 | 4 | Chứng minh không âm giả với điều kiện trạng thái. | MMDS 4.3.2 |
| B07 | 4 | Dẫn xác suất một bit 0/1 hữu hạn. | MMDS 4.3.3 |
| B08 | 4 | Tách mật độ bit chính xác $q$ khỏi FPR xấp xỉ: $q^k$ là xấp xỉ chuẩn, dạng mũ là xấp xỉ khi $n$ lớn. | MMDS 4.3.3 |
| B09 | 3 | Giải thích đánh đổi khi tăng $k$; thiết lập Ex.4.3.2 mà chưa giải. | MMDS Ex.4.3.2; Streams 2 tr.12–14 |
| B10 | 3 | Dẫn xuất $k^*$, chứng minh cực tiểu và nêu quy tắc số nguyên $k\ge1$. | MMDS Ex.4.3.3; Streams 2 tr.14 |
| B11 | 2 | Vẽ đủ $k=1,\ldots,10$, đánh dấu 5/6; sửa phép tính $k=6$ thành 0,02158. | MMDS công thức; `stanford-cs246/16-streams.pdf`, CS246 26/02/2026, tr.31–32 |
| B12 | 3 | Tổng hợp chi phí, giới hạn và kiểm tra dương giả; câu hỏi dùng một khóa ngoài $S$ khác với 118 để không mâu thuẫn ví dụ B05. | MMDS 4.3.2–4.3.3 |
| C00 | 2 | So sánh ba cấu trúc theo đơn vị và bảo đảm. | tổng hợp nguồn |
| C01 | 2 | Áp dụng lại vào dòng truy vấn P01. | tổng hợp nguồn |
| C02 | 1 | Ghi nguồn, quyết định MMDS/Stanford và phạm vi loại. | các nguồn đã dùng |

Tổng phần giảng: **120 phút**.

## Trang bài tập

| Cụm bài tập | Bước và mã trang | Đầu vào → sản phẩm | Dữ kiện truyền từ phần giảng | Gộp hoặc không áp dụng | Câu nối | Phút |
|---|---|---|---|---|---|---:|
| Chọn khóa | X01 | phân tích ba câu hỏi trên `Grades` → ba khóa và ba giải thích | quy trình xác định đơn vị thống kê K06; quy tắc nhất quán K03–K05 | không chạy lại ví dụ để tránh lộ đáp án | Dùng đơn vị thống kê để tự xác định khóa. | 15 |
| Tính FPR | X02 | $n/m=8$, $k=3,4$ → hai phép tính | công thức B08 | không yêu cầu so sánh vì giáo trình chỉ hỏi hai giá trị | Thay tham số vào mô hình xấp xỉ đã thiết lập. | 10 |
| Chia mảng | X03 | $k\mid n$, băm đều/độc lập → công thức theo $n$ hữu hạn, xấp xỉ và so sánh | câu thiết lập B09; xác suất bit B07–B08 | dẫn xuất và so sánh cùng trang vì là một bài | Thay đổi cách tổ chức bit nhưng giữ tổng ngân sách. | 15 |
| Tối ưu $k$ | X04 | $n,m$ → bản tái dựng độc lập của $k^*$ và quy tắc số nguyên | mô hình mẫu B10; khi làm bài, sinh viên không xem lại lời giải B10; B11 chỉ là ví dụ phần giảng | không dùng lại dữ kiện $n/m=8$ trong yêu cầu bài tập; chủ đích luyện tái dựng chứng minh từ công thức gốc | Tái dựng lập luận để kiểm tra khả năng dùng mô hình, không chép kết quả. | 20 |

Tổng phần bài tập: **60 phút**. Các bước trên chỉ chia nhỏ cách trình bày; dữ kiện và yêu cầu toán học giữ nguyên giáo trình.

| ID | Phút | Dữ kiện, yêu cầu và sản phẩm | Đáp án trong ghi chú | Nguồn trực tiếp |
|---|---:|---|---|---|
| X00 | 0 | Mở phần, nêu bốn bài và phiếu nộp. | Nêu không có bài hồ chứa trực tiếp trong sách. | MMDS 4.2–4.3 |
| X01 | 15 | Lược đồ Grades với định danh university duy nhất toàn cục; chọn ba khóa và giải thích. Không thêm điều kiện ngưỡng băm. | `(university,courseID)`, `(university,studentID)`, `(university,courseID)`; rubric 10 điểm trong ghi chú. Đáp án/rubric là lời giải giảng viên suy ra từ đề. | Ex.4.2.1, tr.138 |
| X02 | 10 | $n/m=8$; tính $p_3,p_4$, không thêm yêu cầu so sánh. | 0,030579 và 0,023969; rubric 10 điểm trong ghi chú. | Ex.4.3.1, tr.141 |
| X03 | 15 | Với $k\mid n$ và băm đều, độc lập, dẫn FPR mảng chia và so với mảng chung. | Hai biểu thức theo $n$ hữu hạn khác nhau; biểu thức mảng chung $q^k$ là xấp xỉ chuẩn của FPR vì trạng thái bit phụ thuộc và vị trí truy vấn có thể trùng; cả hai dẫn tới $(1-e^{-km/n})^k$ trong xấp xỉ mũ; rubric 10 điểm. | Ex.4.3.2, tr.141 |
| X04 | 20 | Tối thiểu hóa FPR theo $n,m$; chứng minh cực tiểu và nêu quy tắc số nguyên, không thêm $n/m=8$. | $k^*=(n/m)\ln2$ và so hai số nguyên lân cận không nhỏ hơn 1; rubric 10 điểm. Đáp án/rubric là lời giải giảng viên suy ra từ đề. | Ex.4.3.3, tr.142 |
| X05 | 0 | Đối chiếu đủ bốn sản phẩm, không thêm yêu cầu toán học. | Nhắc đối chiếu phiếu với rubric trong ghi chú. | tổng hợp bốn bài |

Tổng recitation: **60 phút**. Chỉ dịch, chia bước và thêm mẫu sản phẩm; không đổi dữ kiện hoặc yêu cầu toán học.
