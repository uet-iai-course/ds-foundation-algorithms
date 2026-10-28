# Storyboard Bài 8

Mục hiện hành: **Lượt duyệt từng mạch (2026-10-28)** ở cuối tệp. Các mục trước giữ làm lịch sử; khi mâu thuẫn, mục hiện hành được áp dụng.

## Hành trình khái niệm

- **Lấy mẫu theo khóa:** tình huống P01 → vấn đề K00–K01 → trực giác và ví dụ K02 → đặc tả K03 → thuật toán K04 → lập luận đúng K05 → ứng dụng K06, chi phí K07 → kiểm tra K08.
- **Lấy mẫu hồ chứa:** tình huống P01, R00 → phân biệt mục tiêu R01 → ví dụ chạy tay R03 → đặc tả R02 → thuật toán R04 → bất biến và chứng minh R05–R07 → chi phí, giả thiết ngẫu nhiên và kiểm tra R08.
- **Bloom filter:** tình huống B00 → vị trí trong hệ thống B02 → trực giác và ví dụ B05 → đặc tả B01 → thuật toán B03–B04 → bảo đảm B06 → hình thức hóa và xác suất B07–B11 → chi phí, giới hạn và kiểm tra B12.

Tình huống xuyên suốt là dòng truy vấn `(người dùng, truy vấn, thời gian)` không biết trước độ dài và không thể giữ toàn bộ lịch sử. Đầu ra cần có là mẫu phục vụ thống kê truy vấn lặp hoặc quyết định loại sớm khóa không thuộc tập. Tình huống trở lại ở K00–K08 để bảo toàn nhóm theo người dùng, R00–R08 để giữ đúng số vị trí và C01 để chọn cấu trúc. Bloom dùng thêm tình huống một tỷ địa chỉ cho phép và một gigabyte từ MMDS trang 139.

## Bổ sung trang tiêu đề mạch 2026-10-14

Căn cứ: `AGENTS.md` mục "Trang tiêu đề mạch"; yêu cầu người dùng 2026-10-14. Mỗi section ngoài trừ mạch mở đầu mở bằng một trang `class="strand-title"`, `id="mach-N"`. Mã theo quy ước của bài: mã `<tiền tố>00` đã thuộc trang nội dung đầu mạch, nên trang tiêu đề mạch dùng `<tiền tố>T`. Trang tiêu đề mạch nằm ngoài chu trình khái niệm; thời lượng 0,5 phút mỗi trang lấy từ trang đầu mạch (cột "Trang đầu mạch"), tổng thời lượng bài không đổi. Deck 48 → 55 trang.

Bản đồ mạch (tên trùng từng chữ với trang Nội dung): 1. Mở đầu (mở bằng trang bìa P00); 2. Mô hình tính toán trên dòng (`AT`); 3. Lấy mẫu theo khóa (`KT`); 4. Lấy mẫu hồ chứa (`RT`); 5. Lọc thành viên bằng Bloom filter (`BT`); 6. Tổng kết và chuyển tiếp (`CT`); 7. Bài tập vận dụng (`XT`).

| Mã trang | Tiêu đề (tên mạch) | Mục đích | Vị trí | Kiến thức đầu vào | Đầu ra | Ghi chú | Phút | Quyết định |
|---|---|---|---|---|---|---|---:|---|
| P03 | Nội dung | Liệt kê đánh số mọi mạch, tên trùng trang tiêu đề mạch; notes một câu mỗi mạch | mạch mở đầu, sau P00 | Tên bài | Thứ tự và quan hệ các mạch | trang `agenda-slide` | 0,5 (từ trang bìa) | thêm |
| AT | Mô hình tính toán trên dòng | Dòng dẫn nêu nhu cầu của mạch; notes nối kết quả kế thừa, nhiệm vụ, kết quả giao | điểm vào mạch 2, `id="mach-2"`, trước A00 | Dòng truy vấn không có điểm kết thúc (P01) | Hợp đồng thuật toán dòng, ba sản phẩm | ngoài chu trình khái niệm; tên khác tiêu đề A00 | 0,5 (từ A00) | thêm |
| KT | Lấy mẫu theo khóa | Dòng dẫn nêu nhu cầu của mạch; notes nối kết quả kế thừa, nhiệm vụ, kết quả giao | điểm vào mạch 3, `id="mach-3"`, trước K00 | Hợp đồng một lượt, trạng thái hữu hạn | Mẫu tỷ lệ theo khóa, tính nhất quán | ngoài chu trình khái niệm; tên khác tiêu đề K00 | 0,5 (từ K00) | thêm |
| RT | Lấy mẫu hồ chứa | Dòng dẫn nêu nhu cầu của mạch; notes nối kết quả kế thừa, nhiệm vụ, kết quả giao | điểm vào mạch 4, `id="mach-4"`, trước R00 | Mẫu theo khóa không cố định kích thước | Hồ chứa và bất biến $s/r$ | ngoài chu trình khái niệm; tên khác tiêu đề R00 | 0,5 (từ R00) | thêm |
| BT | Lọc thành viên bằng Bloom filter | Dòng dẫn nêu nhu cầu của mạch; notes nối kết quả kế thừa, nhiệm vụ, kết quả giao | điểm vào mạch 5, `id="mach-5"`, trước B00 | Câu hỏi thành viên với bộ nhớ cố định | Bloom filter, dương giả, số hàm băm tối ưu | ngoài chu trình khái niệm; tên khác tiêu đề B00 | 0,5 (từ B00) | thêm |
| CT | Tổng kết và chuyển tiếp | Dòng dẫn nêu nhu cầu của mạch; notes nối kết quả kế thừa, nhiệm vụ, kết quả giao | điểm vào mạch 6, `id="mach-6"`, trước C00 | Ba cấu trúc đã chứng minh | Bảng đối chiếu và áp lại vào dòng truy vấn | ngoài chu trình khái niệm; tên khác tiêu đề C00 | 0,5 (từ C00) | thêm |
| XT | Bài tập vận dụng | Dòng dẫn nêu nhu cầu của mạch; notes nối kết quả kế thừa, nhiệm vụ, kết quả giao | điểm vào mạch 7, `id="mach-7"`, trước X00 | Tính nhất quán, công thức dương giả | Bốn bài MMDS 4.2.1, 4.3.1–4.3.3 | ngoài chu trình khái niệm; tên khác tiêu đề X00 | 0,5 (từ X01; X00 không có phút riêng nên X01 giảm 0,5 phút) | thêm |

Trang Nội dung: bài chưa có trang này; thêm `P03` (`class="agenda-slide"`, `<h2>Nội dung</h2>`, `ol` 1–7) ngay sau trang bìa P00, tên trùng từng chữ với tên mạch; mạch 1 đặt tên "Mở đầu". Mặt trang khoảng 33 âm tiết; notes một câu cho mỗi mạch, nêu quan hệ suy luận. Mã `P03` theo dãy mã P của mạch mở đầu. Quyết định: thêm (0,5 phút lấy từ trang bìa).

Mạch 6 đặt tên "Tổng kết và chuyển tiếp" theo `AGENTS.md`, vì phần C gồm bảng đối chiếu, áp lại vào dòng truy vấn và nguồn, chưa có câu hỏi tự kiểm tra.

## Bản đồ chu trình theo cụm

| Cụm | Bước và mã trang | Đầu vào → sản phẩm | Dữ kiện truyền | Gộp hoặc không áp dụng | Câu nối | Phút |
|---|---|---|---|---|---|---:|
| Mô hình dòng | tình huống P01; vấn đề–hình thức A00–A02; ứng dụng–kiểm tra A03–A04 | dòng bộ chưa biết độ dài, bộ nhớ hữu hạn → hợp đồng và bốn trục chi phí | bộ `(người dùng, truy vấn, thời gian)`, đầu ra mẫu/lọc | trực giác và hình thức hóa gộp ở A00–A01 vì đây là mô hình, không phải thuật toán | Từ giới hạn chung, chọn trạng thái theo truy vấn. | 19 |
| Mẫu theo khóa | tình huống–vấn đề K00–K01; trực giác–ví dụ K02; hình thức K03; thuật toán K04; đúng K05; ứng dụng–chi phí K06–K07; kiểm tra K08 | bộ $t$, khóa $K(t)$, $a,b,h$ → mẫu nhất quán theo khóa | $x,d$ ở K01 tạo nhu cầu; cùng `An`, $a=3,b=10$ ở K02 truyền sang quy tắc $h(K)<a$ | ví dụ và trực giác gộp K02; ứng dụng tách K06–K07 để không lộ bài tập | Một quyết định cố định cho khóa thay lấy độc lập từng bộ. | 26 |
| Hồ chứa | tình huống R00; vấn đề R01; ví dụ R03; hình thức R02; thuật toán R04; đúng R05–R07; ứng dụng–chi phí–kiểm tra R08 | dòng vị trí, $s$, số ngẫu nhiên đều → đúng $s$ vị trí với xác suất biên $s/r$ | vết $s=2$, các giá trị $j$ và trạng thái $S$ ở R03 truyền sang đặc tả, giả mã và quy nạp | ứng dụng, chi phí và kiểm tra gộp R08 vì cùng kiểm tra giả thiết mô hình RAM/ngẫu nhiên | Vết chạy cho thấy trạng thái; đặc tả sau đó nêu bảo đảm cần chứng minh. | 26 |
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
| R02 | 3 | Từ vết chạy, đặc tả $s\ge1$, $r<s$, $r\ge s$ và xác suất biên. | Streams 1 tr.18–19 |
| R04 | 4 | Giả mã $j$ đều trong $1,\ldots,r$. | Streams 1 tr.19 |
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

## Storyboard ghi chú tự học

Cập nhật 2026-10-28. Ghi chú được viết lại thành chương giáo trình theo `AGENTS.md` §"Tiêu chuẩn giáo trình cho ghi chú bài giảng", lần lượt theo mạch của deck. Mã chủ đề cũ `L08-N01`…`L08-N11` được thay bằng `lec-08-topic-01`…`lec-08-topic-17` (ánh xạ cũ → mới ở `outline.md`, mục "Bản đồ chủ đề cho ghi chú tự học"). Trong thời gian chuyển tiếp, các mục cũ chưa viết lại vẫn nằm sau phần đầu chương và chưa mang `note-topic-id`.

**Ánh xạ mạch deck → phần ghi chú → chủ đề.**

| Mạch deck | `data-slide-id` | Phần ghi chú | `note-topic-id` | Trạng thái |
|---|---|---|---|---|
| 1. Mở đầu | P00, P04, P02, P03, P01 | Giới thiệu chương, Mục tiêu học tập, Kiến thức tiên quyết, Bảng ký hiệu, Bản đồ chủ đề | `lec-08-topic-01` (Kiến thức tiên quyết); các phần còn lại không mang mã | đã viết 2026-10-28 |
| 2. Mô hình tính toán trên dòng | AT, A05, A00, A02, A06 | Mục 1.1–1.6 | `lec-08-topic-02` | đã viết 2026-10-28, sửa sau rà lại mạch 2 |
| 3. Lấy mẫu theo khóa | KT, K01, K09, K01B, K02, K04, K05, K06, K07, K08 | Mục 2.1–2.5 | `lec-08-topic-03`…`06` | đã viết 2026-10-28 |
| 4. Lấy mẫu hồ chứa | RT, R00, R01, R03, R04, R05, R06, R07, R08, R09 | Mục 3.1–3.5 | `lec-08-topic-07`, `08` | đã viết 2026-10-28 |
| 5. Lọc thành viên bằng Bloom filter | BT, B00–B12 | Mục 4.1–4.6 | `lec-08-topic-09`…`12` | chờ viết |
| 6. Tổng kết và chuyển tiếp | CT, C00–C02 | Mục 5, Tình huống, Tóm tắt | `lec-08-topic-13`…`15` | chờ viết |
| 7. Bài tập vận dụng | XT, X00–X05 | Bài tập củng cố; Tham khảo | `lec-08-topic-16`, `17` | chờ viết |

**Phần đầu chương (mạch 1).**

| Phần ghi chú | `note-topic-id` | Trang deck tương ứng | Vai trò | Vào | Ra | Sản phẩm học tập |
|---|---|---|---|---|---|---|
| Giới thiệu chương và liên kết deck | — | P00, P01 | Nêu bài toán dòng (vài trăm triệu truy vấn/ngày, MMDS tr.133), ba loại câu hỏi (ngân sách $1/10$ tr.136; $10^9$ địa chỉ, 1 GB tr.139) | Hai bài toán của ghi chú Bài 01 | Ba cấu trúc cần xây | Nêu được ba câu hỏi và cấu trúc tương ứng |
| Mục tiêu học tập | — | P02 | Ba mục tiêu khớp P02, mỗi mục tách thành việc quan sát được kèm mục ghi chú | Giới thiệu | Đích cho bài tập củng cố (một bài mỗi mục tiêu) | — |
| Kiến thức tiên quyết | `lec-08-topic-01` | P04 (dòng "Nhắc lại:") | Phát biểu lại kết quả dùng lại, có nguồn: ghi chú Bài 01 (mục dòng dữ liệu; mục mô hình ngẫu nhiên), ghi chú Bài 05 (Mục 7, 9, 10, 11), Định lý 06.7, Mệnh đề 06.5, Tình huống 06.2 (Jensen), MMDS §1.3.5, §4.3.3 tr.140 | Học phần Xác suất thống kê, Giải tích; Bài 01, 02, 05, 06 | Công cụ cho Mục 2 (băm tất định, tuyến tính kỳ vọng), Mục 3 (quy tắc nhân, quy nạp), Mục 4 (độc lập, $e^{-1}$, Jensen, Bernoulli, cực trị, hàm lõm) | Dùng đúng công cụ ở từng chứng minh |
| Bảng ký hiệu | — | P04 (dòng "Ký hiệu:") | 21 dòng theo quyết định ký hiệu 2026-10-28 ($t$ là phần tử của dòng truy vấn, $t=x_i$, như P04 mới); quy ước số; bốn chỗ khác MMDS ($s\to u$; $B,t\to b,\tau$; $x,y$ phi tiêu $\to n,km$; slide hồ chứa $S,n\to W,r$) gộp một câu; số liệu sách và số liệu do học phần dựng | P04 | Mọi mục sau | Tra lại ký hiệu |
| Bản đồ chủ đề | — | P03 | 17 chủ đề, bốn nhóm, quan hệ tiên quyết viết theo số mục, phạm vi Bài 09 | — | Thứ tự viết các mục | — |

Số âm tiết phần đầu chương (token cách trắng, từ dòng 1 tới trước Mục 1): 3 110 ở bản đầu, 2 890 sau lượt sửa theo hai báo cáo rà lại mạch 1. Mục tiêu điều phối ≤ 2 800 chưa đạt; phần còn lại là bảng ký hiệu 21 dòng, chín nhóm tiên quyết mà Mục 2–4 cần và bản đồ 17 chủ đề (phần đầu chương của ghi chú Bài 06 là 2 466 âm tiết). Tổng chương vẫn trong khung 12 000–32 000 của `AGENTS.md`; mục tiêu riêng của Bài 08 là 15 000–20 000 theo phân bổ của báo cáo rà ghi chú.

Chu trình rút gọn (thông tin soạn thảo, chuyển khỏi ghi chú ngày 2026-10-28): `lec-08-topic-05` (Mục 2.3, chọn khóa) là quy trình, không có định lý hay chi phí riêng; `lec-08-topic-06` (Mục 2.4, ngưỡng băm) chỉ thêm một mệnh đề bất biến, không có phân tích xác suất mới; `lec-08-topic-13` (Mục 5) tổng hợp ba nhánh, không đưa khái niệm mới.

Điều kiện công bố (điều phối viên, 2026-10-28): số mục dẫn chiếu trong Mục tiêu học tập và Bản đồ chủ đề theo cấu trúc mới (Mục 1–5, 2.1–2.4, 3.1–3.5, 4.1–4.6) chưa khớp thân bài cũ; phải kiểm lại toàn bộ sau khi mạch 2–7 được viết lại.

**Mục 1 (mạch 2), `lec-08-topic-02`.** Thứ tự ghi chú: nhu cầu có số → ví dụ dẫn nhập → định nghĩa → hình (trực quan) → ví dụ giải → thuật toán mẫu → chi phí ba truy vấn → nhầm lẫn → "Trong thực hành" → bài tập phương sai → đoạn kết mục (nhu cầu thống kê theo người dùng khi chỉ lưu $1/10$ dòng → Mục 2).

| Phần ghi chú | Khối, số hiệu | Trang deck | Dữ kiện, ký hiệu | Sản phẩm học tập |
|---|---|---|---|---|
| Mở mục | — | AT (ghi chú) | Cảm biến độ cao mặt biển: $10^6\cdot10\cdot4\cdot86\,400\approx3{,}46\cdot10^{12}$ byte/ngày (MMDS §4.1.2 tr.133); cặp (tổng, số lượng) của Bài 02 | Nhu cầu chọn trạng thái trước khi dòng đến |
| 1.1 Trạng thái theo truy vấn | Ví dụ 08.1; Định nghĩa 08.1; câu hai nghĩa của "truy vấn" | A05, A00 | Dòng $1,5,2,7,4,0,3,5$; lớn nhất 7; $27/8=3{,}375$; ba truy vấn từ Ví dụ 4.1 (cảm biến nhiệt độ) | Đặc tả trạng thái, cập nhật, trả lời |
| 1.2 Hình mô hình dòng | hình `mo-hinh-dong.svg` | A00 | Dòng viết ngược 5, 3, 0, 4, 7, 2, 5, 1, $x_1=1$ sát bộ xử lý (quy ước MMDS) | Nối thành phần định nghĩa với hệ thống |
| 1.3 Vết chạy và thuật toán mẫu | Ví dụ 08.2; Thuật toán 08.2 (bất biến, trường hợp biên $r=0$, bảng chi phí) | A05 (ghi chú), A02 | Vết $M$, $T$ (ký hiệu cục bộ) | Lập vết, đọc bất biến |
| 1.4 Chi phí theo từng phần tử | Định nghĩa 08.3; bảng ba truy vấn | A02 | 1 từ/1 so sánh; 2 từ/2 phép cộng; $24+3$ từ/4 phép (bộ đệm vòng, tổng chạy, vị trí ghi, số đếm $\min(r,24)$); $\lceil\log_2(r+1)\rceil$ bit: 4 bit khi $r=8$, 29 bit khi $r=315\,360\,000$ | Đếm bốn đại lượng |
| 1.5 Nhầm lẫn, thực hành | Nhận xét 08.4, 08.5 | A02 (ghi chú) | MMDS §4.1.4 tr.135; nguồn ngẫu nhiên: băm ở Mục 2, 4, số ngẫu nhiên ở Mục 3 | Phân biệt hữu hạn/nhỏ hơn lịch sử, trạng thái/mẫu |
| 1.6 Bài tập: trạng thái của phương sai | Bài tập 08.1 (hint, solution) | A06 | $r,\sum x_i,\sum x_i^2$; $\sum x_i^2=129$; $\sigma_8^2=129/8-(27/8)^2=4{,}734375$; câu hỏi do học phần dựng | Chọn trạng thái cỡ hằng cho một thống kê mới |
| (chuyển đi) Bảng giữ/bỏ theo người dùng | Ví dụ, hình `bang-theo-nguoi-dung.svg`, bài tập; bản nháp `scratchpad/note-moved-table.md` | K01B (mạch 3) | An, Bình, An, Chi; số rút 0, 7, 4 (học phần dựng); MMDS §4.2.2 tr.137 | Mục 2, chờ viết; nhu cầu bỏ bảng nhãn → hàm băm |

Chu trình rút gọn của Mục 1: không có định lý; tính đúng của thuật toán mẫu nêu bằng dòng "Bất biến." trong Thuật toán 08.2 (quy nạp hai bước). Bộ đếm chung đã dùng: 08.1–08.5; Ví dụ 08.1–08.2; Bài tập 08.1. Số âm tiết Mục 1: 2 730 ở bản đầu (đã chấp nhận), 2 812 sau lượt sửa (thêm bảng chi phí ba truy vấn và bài tập phương sai, bỏ §1.5 cũ).

**Mục 2 (mạch 3).** Thứ tự ghi chú: nhu cầu (MMDS §4.2.1) → ví dụ dẫn nhập An → mệnh đề sai lệch → nhầm lẫn → phương án bảng nhãn → trực giác hàm băm và hình → định nghĩa → ví dụ giải ba ngưỡng → thuật toán → mệnh đề nhất quán và xác suất, phản ví dụ → "Trong thực hành" → chọn khóa và bài tập → chi phí, cỡ mẫu kỳ vọng, khóa nhiều bộ, bài tập ngưỡng → ngưỡng giảm dần (cầu nối) → đoạn kết mục sang hồ chứa.

| Phần ghi chú | `note-topic-id` | Khối, số hiệu | Trang deck | Dữ kiện, ký hiệu |
|---|---|---|---|---|
| Mở mục | — | — | KT | Dòng (người dùng, truy vấn tìm kiếm, thời điểm), ngân sách $1/10$ (MMDS tr.136) |
| 2.1 Sai lệch của lấy mẫu từng bộ | `lec-08-topic-03` | Ví dụ 08.3; Mệnh đề 08.6 (bốn phần, chứng minh bốn bước, điều kiện $9u+18d=0$); Nhận xét 08.7 | K01, K09 | An: $1/100$, $18/100$, $81/100$, $1/10$, $1/19$; $d/(10u+19d)$; $u=d=1$: $1/29$; tỷ lệ $p$ tổng quát $dp/(u+(2-p)d)$ (suy trực tiếp, ghi chú bổ sung) |
| 2.2 Mẫu nhất quán theo khóa | `lec-08-topic-04` | Ví dụ 08.4 (bảng nhãn, năm bộ, 3 hàng), hình `bang-theo-nguoi-dung.svg`; hình `bam-theo-nguoi-dung.svg`; Định nghĩa 08.8; Ví dụ 08.5 (ba ngưỡng $a=1,5,8$: 3, 4, 5 bộ); Thuật toán 08.9; Mệnh đề 08.10 (a)(b) và ba phản ví dụ; Nhận xét 08.11 (Trong thực hành) | K01B, K02, K04, K05 | Dòng năm bộ dùng chung: (An, đồ thị), (Bình, lọc), (An, băm), (An, đồ thị), (Chi, lọc); An 0, Bình 7, Chi 4; số ngăn $b=10$, ngưỡng $a=1$; tỷ lệ lặp của An trên mẫu $1/2$; $10^8\cdot16=1{,}6\cdot10^9$ byte (giả định học phần); ví dụ 30% của slide MMDS chỉ nhắc trong văn |
| 2.3 Chọn khóa theo đơn vị thống kê | `lec-08-topic-05` | bảng MMDS §4.2.3; quy trình ba bước; Bài tập 08.2 (khóa (người dùng, thời điểm)) | K06 | Lời giải dùng Mệnh đề 08.6, $1/29$ |
| 2.4 Chi phí và cỡ mẫu | (thuộc `lec-08-topic-04`) | Hệ quả 08.12 ($ar/b$); Ví dụ 08.6 (khóa $10^6$ bộ, $a/b=1/5$, kỳ vọng $200\,200$); Bài tập 08.3 (ngưỡng 20%) | K07, K08 | Chi phí mỗi bộ: 1 băm, 1 so sánh |
| 2.5 Ngưỡng băm khi ngân sách cố định | `lec-08-topic-06` | Thuật toán 08.13 (dọn dạng nhảy: $v$ lớn nhất qua chỉ mục có thứ tự, $\tau\gets v-1$; xóa $\le r$, số lần dọn $\le$ số giá trị băm phân biệt, tra $O(\log G)$); Ví dụ 08.7 ($G=3$, $\tau$: 9 → 6 ở $r=4$, 6 → 3 ở $r=5$, mẫu An ×3); Mệnh đề 08.14 (bất biến, quy nạp, kiểm cho bản nhảy) | K07 (ghi chú) | MMDS §4.2.4 tr.138; $B,t$ của sách $\to b,\tau$; $G$ là ký hiệu cục bộ cho ngân sách |

Bộ đếm sau Mục 2: chung 08.6–08.14; Ví dụ 08.3–08.7; Bài tập 08.2–08.3. Tiểu mục 2.4 (chi phí và cỡ mẫu) được thêm, nên ngưỡng băm chuyển sang 2.5 (bản đồ chủ đề ở ghi chú và outline đã đổi). Số âm tiết Mục 2: 4 179 ở bản đầu, 4 627 sau lượt sửa theo rà lại mạch 3 (dòng năm bộ, bảng chi phí của Thuật toán 08.13 dạng nhảy, đoạn về độc lập giữa các khóa); khung giao 3 000–4 000. Hình `key-sampling.svg` (30%) không còn được ghi chú hay deck dùng.

**Mục 3 (mạch 4).** Thứ tự ghi chú: nhu cầu (giới hạn cỡ của mẫu theo khóa, Ví dụ 08.6) → ví dụ dẫn nhập $s=2$ trên dòng mười phần tử → ý tưởng (một số $j$ gộp hai quyết định) → vết hai ô → định nghĩa → thuật toán → định lý $s/r$ (quy nạp năm bước) và hình bước $r+1=5$ → phản ví dụ → mệnh đề tập con đều (bổ sung) → chi phí và số lần ghi → nhầm lẫn, "Trong thực hành", bảng so sánh, bài tập → đoạn kết sang câu hỏi thành viên.

| Phần ghi chú | `note-topic-id` | Khối, số hiệu | Trang deck | Dữ kiện, ký hiệu |
|---|---|---|---|---|
| Mở mục | — | — | RT | Khóa $10^6$ bộ (Ví dụ 08.6); cỡ kỳ vọng $ar/b$ |
| 3.1 Mẫu cỡ cố định và ý tưởng | `lec-08-topic-07` | Ví dụ 08.8; đoạn trực quan; Ví dụ 08.9; hình `reservoir-trace.svg` | R00, R01, R03 | Dòng a x c y z k c d e g (slide MMDS Streams 1 tr.18), $2/5$, $2/7$; $j=2,4,1$ (học phần dựng), hồ cuối [z, c]; xác suất nhận $2/3$, $2/4$, $2/5$ |
| 3.2 Đặc tả và thuật toán | (thuộc `lec-08-topic-07`) | Định nghĩa 08.15; Thuật toán 08.16 (biên $r\le s$, $s=1$) | R04 | $W[1..s]$, $s$, $r$, $j$ |
| 3.3 Xác suất $s/r$ | `lec-08-topic-08` | Định lý 08.17 (bốn phần; chứng minh: cơ sở, giả thiết quy nạp, phần tử mới, phần tử cũ có dẫn độc lập của $j$, cỡ); hình `reservoir-step.svg`; hai phản ví dụ; Mệnh đề 08.18 (mọi tập con cỡ $s$ xác suất $1/\binom rs$, bổ sung) | R05, R06, R07 | $W_r$ ký hiệu cục bộ; $E_i$ biến cố bị thay (thay `\text{bị thay}` cũ); $\frac24\cdot\frac45=\frac25$; phản ví dụ phụ thuộc: $\Pr[x_3\in W_4]=1/6$; liệt kê $r=4,s=2$: 12 kết cục, mỗi cặp 2 lần |
| 3.4 Chi phí | (thuộc `lec-08-topic-08`) | Mệnh đề 08.19 (RAM, $\Theta(s)$, $O(1)$, số lần ghi kỳ vọng với cận tích phân); Ví dụ 08.10 ($s=100$, $r=10^6$: $920{,}5$ lần thay, tổng $1\,020{,}5$, cận $1\,020{,}0$ và $1\,021{,}0$) | R08 | — |
| 3.5 Nhầm lẫn, thực hành, so sánh | (thuộc `lec-08-topic-08`) | Nhận xét 08.20, 08.21; bảng so sánh; Bài tập 08.4 (An 10 bộ trong $1\,000$, $s=100$: kỳ vọng 1; giữ trọn với xác suất $\approx6{,}6\cdot10^{-11}$) | R09 | — |

Bộ đếm sau Mục 3: chung 08.15–08.21; Ví dụ 08.8–08.10; Bài tập 08.4. Bản đồ chủ đề đổi: `lec-08-topic-07` là 3.1–3.2, `lec-08-topic-08` là 3.3–3.5 (ghi chú và outline). Số âm tiết Mục 3: 3 111 ở bản đầu, 3 291 sau lượt sửa theo rà lại mạch 4 (đối chiếu quy tắc ngưỡng với mẫu theo khóa; "độc lập với các lần rút trước"; mô hình chi phí của Định nghĩa 08.3 thay mô hình RAM; phép tính hai trường hợp của slide MMDS tr.21; Nhận xét 08.20 tính tỷ số các số đếm kỳ vọng với $p_2=\frac{s(s-1)}{r(r-1)}$; biến vị trí $\ell$ thay $y$ trong chứng minh Mệnh đề 08.18). Từ "thời điểm" trong bộ (người dùng, truy vấn, thời gian) đổi thành "thời gian" ở mọi chỗ của ghi chú, khớp deck và "time" của MMDS.

Mã trang, thời lượng và nhãn quy trình chỉ tồn tại trong planning, không xuất hiện trong ghi chú công khai; `note-topic-id` là chú thích HTML mà viewer kiểm rồi ẩn.

## Lượt duyệt từng mạch (2026-10-28)

Căn cứ: `AGENTS.md` §"Mẫu RevealJS bắt buộc" và §"Văn phong và mật độ"; quyết định ký hiệu và thứ tự của điều phối viên ngày 2026-10-28; báo cáo rà deck cùng ngày. Âm tiết đếm bằng script kiểm deck (bỏ tiêu đề, KaTeX, giả mã, hình, số trong bảng và ghi chú). Số "trước" lấy từ lần đo trước bước chuyển CSS; số "sau" đo trên deck đã sửa. Mục này thay các dòng P00–P03 ở "Trang phần giảng" và "Bổ sung trang tiêu đề mạch".

### Mạch 1. Mở đầu

**Bản đồ mạch.**

| Loại | Chức năng | Vào | Ra | Đóng góp | Trang tiêu đề mạch |
|---|---|---|---|---|---|
| giới thiệu | Nêu bài toán dòng dữ liệu, kết quả kế thừa, ký hiệu cả bài, mục tiêu, dàn bài và câu trả lời có điều kiện của từng mạch | Bài 01 (hai bài toán dòng: giữ mẫu truy vấn, lọc thư); Bài 02, 05 (hàm băm tất định); xác suất cơ bản, tuyến tính kỳ vọng; giới hạn $(1-1/n)^n\approx e^{-1}$ (MMDS §1.3.5); quy nạp | Nhu cầu "lấy mẫu, lọc dòng chưa biết độ dài, không lưu cả dòng"; khái niệm trạng thái (dữ liệu giữ lại giữa hai lần đọc); ký hiệu $x_i,r,t,K(t),s,W,S,m,n,k$; bốn câu trả lời có điều kiện mà mạch 2–5 chứng minh, trong đó mẫu theo khóa tăng theo dòng (khoảng $r/10$ bộ) và chỉ hồ chứa giữ cỡ mẫu cố định | Đặt mọi ký hiệu trước lần dùng đầu; thay tình huống P01 cũ (vượt trần) bằng trang "Vấn đề trung tâm" có số liệu MMDS và điều kiện của từng kết quả | Bìa P00 đóng vai trang mở mạch |

Thứ tự trang: P00 → P04 → P02 → P03 → P01. Không có trang tiêu đề mạch riêng (mạch mở đầu).

**Từng trang.**

| Trang | Mục đích | Hành động của sinh viên | Đối tượng trung tâm | Dữ kiện, ký hiệu kế thừa | Sản phẩm học tập và bằng chứng | Quyết định và lý do | Âm tiết (dòng, max dòng) trước → sau | Phút |
|---|---|---|---|---|---|---|---|---:|
| P00 | Tên bài, học phần, học kỳ, đơn vị và câu luận đề | Đọc luận đề, nhận ba cấu trúc của bài | Câu luận đề: băm khóa giữ trọn nhóm, hồ chứa giữ mẫu cỡ cố định, mảng bit loại hầu hết khóa ngoài tập | Bài 01 (hai bài toán dòng, nêu trong ghi chú) | Nêu được ba cấu trúc và câu hỏi mỗi cấu trúc phục vụ; bằng chứng: câu hỏi tự kiểm tra ở phần tổng kết | sửa: thêm `p.supporting-text` theo mẫu bìa. Lượt rà lại: bỏ "Với bộ nhớ cố định" vì sai với mẫu theo khóa tỷ lệ cố định (mẫu tăng theo dòng, MMDS §4.2.4 tr.138); câu còn 20 âm tiết, không cần ngoại lệ. Dòng học phần "Bài 08 · …" khớp chân trang; dòng học kỳ như Bài 03, 07; ghi chú nối Bài 01, ghi "Bài 09", ghi công MMDS | 32 (2, 11) → 51 (4, 20); ghi chú 65 → 98 | 0,5 |
| P04 | Nhắc lại kết quả dùng lại và đặt ký hiệu cả bài | Đối chiếu ba kết quả nhắc lại với kiến thức đã học; ghi ký hiệu | Hàm băm tất định; tích xác suất của $\ell$ biến cố độc lập; $(1-1/n)^n\approx e^{-1}$; ký hiệu $x_i$ (mỗi phần tử là một bộ $t$), $K(t)$, $r$; hồ chứa (reservoir) $W$, $s$; $S,m,n,k$ | Bài 02 (phân hoạch theo khóa), Bài 05 (hàm băm thay hoán vị); MMDS §1.3.5 | Dùng đúng ký hiệu ở mọi mạch sau; bằng chứng: câu hỏi ở các mạch 3–5 dùng $r,s,n,m,k$ không cần định nghĩa lại | thêm: trang bắt buộc còn thiếu. Lượt rà lại: câu hàm băm có động từ chính; độc lập dạng $\ell$ biến cố (Bloom cần tích $km$ và $k$ biến cố); nêu quan hệ phần tử–bộ; thêm "(reservoir)" ở lần dùng đầu. Ghi chú định nghĩa trạng thái, nêu Bloom filter là mảng bit trả lời "chắc chắn không thuộc"/"có thể thuộc", tuyến tính kỳ vọng và quy nạp, để giữ mặt trang ≤ 60 | — → 57 (5, 17); ghi chú — → 139 | 2 |
| P02 | Ba mục tiêu quan sát được, mỗi mục có sản phẩm kiểm được | Đọc ba mục tiêu và sản phẩm tương ứng | Đặc tả và chọn khóa; lập vết và chứng minh hồ chứa với $r\ge s$; xây dựng, truy vấn, định cỡ Bloom filter | $s,r,S,n,m,k$ từ P04 | Bằng chứng: câu hỏi cuối mạch 2, 3, 4, 5; Bài tập 4.2.1, 4.3.1–4.3.3; câu hỏi tự kiểm tra ở phần tổng kết (mạch 6 sẽ bổ sung) | sửa: tiêu đề "Mục tiêu học tập"; danh sách đánh số; "xác suất nhận nhầm khóa ngoài $S$" thay "dương giả" chưa định nghĩa. Lượt rà lại: mục 2 dùng "phần tử đã đọc" thay "vị trí" (tránh nhầm với ô của $W$) và thêm $r\ge s$; "Xây dựng và truy vấn"; ghi chú gộp ba câu "kiểm nó" thành một câu liệt kê | 45 (3, 16) → 56 (3, 20); ghi chú 41 → 133 | 1 |
| P03 | Dàn bài 7 mạch, tên khớp trang tiêu đề mạch và `#/N`; tài liệu đọc trước | Định vị các mạch; ghi mục đọc trước | Danh sách 1–7; MMDS Chương 4, §§4.1–4.3, tr.131–142 | Tên mạch như trang tiêu đề mạch (không đổi) | Bằng chứng: số trên trang tiêu đề mạch khớp `#/2`…`#/7` (script kiểm deck) | sửa: chuyển sau mục tiêu; hai cột `ex-grid2` như Bài 07; dòng "Đọc trước:" theo định dạng Bài 02–07. Lượt rà lại: ghi chú bỏ "bộ nhớ không tăng theo $r$", nêu trạng thái quyết định cỡ hằng nhưng cỡ mẫu tăng theo dòng | 25 (7, 6) → 39 (8, 14); ghi chú 117 → 134 | 0,5 |
| P01 | Vấn đề trung tâm: nhu cầu một dòng và câu trả lời có điều kiện của mạch 2–5 | Nối mỗi dòng với mạch sẽ chứng minh nó và với giả thiết của nó | Nhu cầu "lấy mẫu, lọc dòng chưa biết độ dài, không lưu cả dòng"; đọc một lần, trả lời từ trạng thái; hàm băm đều, xác suất $1/10$, mẫu $\approx r/10$ bộ; số ngẫu nhiên đều, độc lập, $s/r$ khi $r\ge s$; Bloom filter $8\cdot10^9$ bit, sáu hàm băm đều, độc lập, $10^9$ khóa, nhận nhầm $\approx2\%$ | MMDS §4.2.1 tr.136 (bộ (người dùng, truy vấn, thời gian), ngân sách $1/10$); §4.3.1 tr.139 ($10^9$ địa chỉ, 1 GB) | Bằng chứng: trang trả lời vấn đề trung tâm ở phần tổng kết nhắc lại bốn dòng này với số liệu | sửa: thay tình huống cũ bằng trang "Vấn đề trung tâm". Lượt rà lại: mỗi dòng là câu trần thuật có điều kiện, không còn cụm tự đặt trước dấu hai chấm; dòng lấy mẫu theo khóa nêu cỡ mẫu tăng theo dòng. Số 6 hàm băm do học phần chọn (MMDS §4.3.1 dùng một, Ví dụ 4.4 dùng hai): số nguyên gần $k^*=8\ln2\approx5{,}545$; $p(6)=0{,}021577<p(5)=0{,}021679$. Xếp loại trang đối chiếu (trần 80): lý do và số đo ở đoạn dưới | 72 (3, 20) → 72 (5, 17); ghi chú 44 → 150 | 2,5 |

Tổng mạch 1: 6,5 phút, bằng tổng cũ (P00 0, P03 0,5, P01 4, P02 2); tổng phần giảng giữ 120 phút.

Ngoại lệ mật độ P01: trang được xếp loại trang đối chiếu, trần 80 âm tiết, vì `AGENTS.md` đòi câu trả lời có điều kiện của cả bốn mạch nội dung cùng dòng nhu cầu có giới hạn tài nguyên, và mỗi câu trả lời phải mang giả thiết của nó (hàm băm đều; số ngẫu nhiên đều, độc lập, $r\ge s$; hàm băm đều, độc lập, xấp xỉ mũ). Mục tiêu điều phối là ≤ 65. Trước: 72 âm tiết (bản đầu, 3 dòng), lượt sửa thứ nhất 57 (thiếu điều kiện); sau: 72 (5 dòng, max 17 âm tiết mỗi dòng). Vượt mục tiêu 7 âm tiết; bỏ thêm sẽ phải bỏ một giả thiết hoặc số liệu MMDS.

### Mạch 2. Mô hình tính toán trên dòng

**Bản đồ mạch.**

| Loại | Chức năng | Vào | Ra | Đóng góp | Trang tiêu đề mạch |
|---|---|---|---|---|---|
| khái niệm/mô hình | Đặc tả thuật toán dòng (đọc một lượt, trả lời từ trạng thái), đo chi phí theo từng phần tử trên ba truy vấn của cùng một dòng, kiểm bằng bài tập phương sai | Mạch 1: nhu cầu "lấy mẫu, lọc dòng chưa biết độ dài, không lưu cả dòng"; khái niệm trạng thái; ký hiệu $x_i,r,t,K(t)$ | Định nghĩa thuật toán dòng; mô hình từ máy và bốn đại lượng chi phí; yêu cầu bộ nhớ nhỏ hơn lịch sử, mạch 3 dùng để loại phương án bảng theo người dùng | Chu trình đủ cho khái niệm: nhu cầu "Muốn …" và ví dụ có số (A05) trước hình thức hóa (A00); chi phí trên cùng ba truy vấn (A02); bài tập kiểm (A06) | AT (`id="mach-2"`), điểm vào mạch 2 |

Thứ tự trang: AT → A05 → A00 → A02 → A06. Bỏ A01 (gộp vào A00) và A03 (nội dung đã lên trang Vấn đề trung tâm). A04 chuyển sang mạch 3 thành K01B, sau K01 (theo thứ tự MMDS §4.2.1 → §4.2.2: lý do lấy mẫu theo người dùng đến trước phương án bảng). Chu trình rút gọn: bước "thuật toán và tính đúng" không áp dụng vì mạch đặt một mô hình; ba truy vấn của A05 đóng vai thuật toán mẫu, đếm chi phí ở A02.

**Câu hỏi trước khi sửa (theo báo cáo rà deck và lượt rà lại mạch 1).**

| Trang cũ | Trang muốn nói | Phục vụ chủ đề mạch? | Vấn đề còn lại | Quyết định |
|---|---|---|---|---|
| AT | Điểm vào mạch 2 | có | Lời dẫn "trạng thái hữu hạn" không phân biệt được gì; cụm khóa "Hợp đồng", "Mẫu, hồ chứa, bộ lọc" xem trước khái niệm chưa học; ghi chú không nêu kết quả kế thừa | sửa |
| A00 | Sơ đồ mô hình dòng | có | Trang chỉ có hình; hình đặt "truy vấn" làm đích của "kết quả", thiếu truy vấn thường trực/tức thời, bộ nhớ làm việc, kho lưu trữ không dùng để trả lời | sửa và gộp A01 |
| A01 | Đặc tả thuật toán dòng | có | Tiêu đề "Hợp đồng"; "trạng thái hữu hạn" thiếu chính xác; câu "trước khi dòng tiếp tục quá xa" mơ hồ | gộp vào A00 |
| (thiếu) | Ví dụ dẫn nhập có số | — | Mạch không có ví dụ trước hình thức hóa | thêm A05 |
| A02 | Bốn đại lượng chi phí | có | Tiêu đề kể so sánh; ô bảng là câu hỏi; thiếu "Mô hình:"; ghi chú lấy tài liệu làm chủ ngữ | sửa |
| A03 | Xem trước ba cấu trúc | một phần | Ba khái niệm xuất hiện đột ngột; trùng trang Vấn đề trung tâm và bảng tổng kết | bỏ |
| A04 | Chọn cấu trúc theo truy vấn | không | Kiểm điều chưa học; nhãn "Sản phẩm:"; "Đáp án" | lượt 1: thay bằng câu hỏi bảng giữ/bỏ theo người dùng (MMDS §4.2.2); lượt rà lại: chuyển sang mạch 3 (K01B) vì nhu cầu giữ trọn người dùng chỉ có ngữ cảnh sau K01 |
| (thiếu sau khi chuyển A04) | Kiểm mô hình dòng | — | Mạch cần trang kiểm tra | thêm A06 |

**Từng trang.**

| Trang | Mục đích | Hành động của sinh viên | Đối tượng trung tâm | Dữ kiện, ký hiệu kế thừa | Sản phẩm học tập và bằng chứng | Quyết định và lý do | Âm tiết (dòng, max dòng) trước → sau | Phút |
|---|---|---|---|---|---|---|---|---:|
| AT | Điểm vào mạch 2 | Nhận nhiệm vụ của mạch | Lời dẫn "Muốn trả lời truy vấn trên dòng chưa biết độ dài, phải giữ trạng thái nhỏ hơn lịch sử."; cụm khóa "Trạng thái theo truy vấn · Mô hình dòng · Chi phí mỗi phần tử · Trạng thái của phương sai" | Nhu cầu và ký hiệu từ mạch 1 | Nêu được ba việc của mạch | sửa: ràng buộc thật là bộ nhớ nhỏ hơn lịch sử; cụm khóa chỉ gọi tên nội dung của mạch; ghi chú nêu kết quả kế thừa và đầu ra trao mạch 3 (yêu cầu bộ nhớ dùng để loại bảng theo người dùng) | 39 (2, 21) → 37 (2, 19); ghi chú 98 → 94 | 0,5 |
| A05 | Nhu cầu, quy mô và ví dụ có số trước hình thức hóa | Tính trạng thái và kết quả của ba truy vấn sau 8 số | Quy mô một triệu cảm biến độ cao mặt biển, 3,5 TB mỗi ngày; dòng $1,5,2,7,4,0,3,5$; giá trị lớn nhất 7; trung bình $27/8=3{,}375$; cửa sổ 24 số | MMDS Hình 4.1 (tr.132), Ví dụ 4.1 (tr.134), §4.1.2 (tr.133) | Bảng trạng thái theo truy vấn; bằng chứng: ba hàng của bảng chi phí A02 và bài tập A06 dùng lại cùng dòng | thêm. Lượt rà lại: tiêu đề "dòng cảm biến" và câu quy mô ghi đúng cảm biến độ cao mặt biển (10 số mỗi giây, 3,5 TB thuộc cảm biến có GPS; cảm biến nhiệt độ của sách gửi một số mỗi giờ); câu quy mô đưa lên trước dữ liệu nhỏ. Tự tính lại: tổng 27; lớn nhất 7; $10^6\cdot10\cdot4\cdot86\,400=3{,}456\cdot10^{12}$ byte | — → 59 (6, 17); ghi chú — → 150 | 3 |
| A00 | Định nghĩa thuật toán dòng và mô hình hệ thống | Đọc hình: nối từng thành phần với một dòng định nghĩa | Hình `mo-hinh-dong.svg`; Định nghĩa., Đầu vào:, Đầu ra: (thường trực chạy liên tục, tức thời hỏi một lần), Giả thiết: | Dòng hiện lại trong hình theo quy ước MMDS (phần tử gần bộ xử lý đến trước), viết "5, 3, 0, 4, 7, 2, 5, 1", nhãn "$x_1=1$ đến trước" chỉ vào phần tử sát bộ xử lý | Phân biệt truy vấn thường trực và tức thời, bộ nhớ làm việc và kho lưu trữ; bằng chứng: bài tập A06 dùng truy vấn thường trực | sửa và gộp A01. Lượt rà lại: đảo thứ tự viết dòng trên hình để khớp $x_1=1,\ldots,x_8=5$; giải nghĩa hai loại truy vấn trên mặt trang; định nghĩa nêu "trả lời từ trạng thái giữ lại"; ghi chú theo MMDS §4.1.3 ("kết quả vào thời điểm định trước") | A00 5 (0, 0) + A01 54 (4, 17) → 57 (4, 18); ghi chú 44 + 39 → 150 | 3 |
| A02 | Chi phí của thuật toán dòng trên ba truy vấn | Đọc và đếm chi phí từng truy vấn | Mô hình từ máy (word); bảng `Truy vấn \| Bộ nhớ (từ) \| Cập nhật mỗi phần tử \| Lượt đọc \| Sai số`: giá trị lớn nhất 1 / 1 phép so sánh; trung bình 2 / 2 phép cộng; cửa sổ 24 số $24+3$ / 4 phép với bộ đệm vòng; công việc sau $r$ phần tử | Ba truy vấn của A05; ký hiệu $r$ | Đếm được chi phí từng truy vấn; bằng chứng: bài tập A06 và các trang chi phí mạch 3–5 | sửa. Lượt rà lại: dựng lại theo hàng là ba truy vấn (so sánh ba công cụ trên cùng dữ liệu), bỏ cột "Giá trị lớn nhất" dễ hiểu nhầm. Số đếm: cửa sổ giữ 24 số, tổng chạy, vị trí ghi, số đếm $\min(r,24)$ = 27 từ; mỗi phần tử 4 phép (trừ số cũ khi $r>24$ hoặc tăng số đếm khi $r\le24$, cộng số mới, ghi đè, tăng vị trí modulo 24) | 54 (4, 15) → 58 (5, 17); ghi chú 38 → 146 | 3 |
| A03 | — | — | — | — | — | bỏ: ba dòng trả lời đã nằm ở trang Vấn đề trung tâm; bảng đối chiếu thuộc mạch tổng kết | 40 → — | 0 |
| A06 | Bài tập kiểm mô hình dòng | Chọn trạng thái cỡ hằng cho phương sai; tính $\sigma_8^2$ | Phương sai mọi số đã đọc (chia $r$); dòng $1,5,2,7,4,0,3,5$ hiện lại trên trang | Truy vấn thường trực (A00); trạng thái tổng và số đếm (A05, A02) | Lời giải trong ghi chú: trạng thái $r,\sum x_i,\sum x_i^2$ (3 từ), cập nhật 3 phép; $\sigma_8^2=129/8-(27/8)^2=4{,}734375$ | thêm (theo quyết định của điều phối viên, thay A04 đã chuyển). Câu hỏi do học phần dựng trên dòng của MMDS Hình 4.1, cùng kiểu truy vấn trung bình của Ví dụ 4.1. Tự kiểm: $\sum x_i^2=1+25+4+49+16+0+9+25=129$; $129/8=16{,}125$; $(27/8)^2=11{,}390625$; hiệu $4{,}734375$ | — → 28 (5, 15); ghi chú — → 100 | 2,5 |

Tổng mạch 2: 12 phút (trước: AT 0,5, A00 2,5, A01 3, A02 3, A03 2, A04 2 = 13). K01B (A04 cũ) mang 2,5 phút sang mạch 3; phân bổ lại khi duyệt mạch 3. Tổng phần giảng tạm là 121,5 phút.

Hình: `img/lec-08/mo-hinh-dong.svg` (mới, thay `stream-model.svg` trên deck; dòng trên viết theo quy ước MMDS kèm nhãn $x_1$) và `img/lec-08/bang-theo-nguoi-dung.svg` (mới, nay ở K01B). `stream-model.svg` giữ nguyên vì ghi chú bài giảng còn dùng; việc thay hình trong ghi chú thuộc tác tử viết ghi chú.

**K01B (chuyển từ A04, thuộc mạch 3).** Bảng giữ hoặc bỏ theo người dùng (MMDS §4.2.2, tr.137), đặt sau K01 và trước K02. Nội dung giữ nguyên; ghi chú đổi "mà không lưu gì" thành "mà không lưu bảng nhãn". Số rút 0, 7, 4 do học phần dựng. Âm tiết 56 (6, 18), ghi chú 116. Biên tập sâu (câu "Nhu cầu", gộp câu hỏi, khớp số rút với $h$ của K02) làm ở lượt mạch 3.

### Mạch 3. Lấy mẫu theo khóa

**Bản đồ mạch.**

| Loại | Chức năng | Vào | Ra | Đóng góp | Trang tiêu đề mạch |
|---|---|---|---|---|---|
| thuật toán | Chỉ ra sai lệch của mẫu từng bộ, nêu phương án bảng và giới hạn của nó, thay bảng bằng hàm băm với ngưỡng, chứng minh nhất quán và xác suất $a/b$, chọn khóa, đếm chi phí | Mạch 2: thuật toán dòng trả lời từ trạng thái nhỏ hơn lịch sử; trạng thái cỡ hằng (bài tập phương sai); dòng (người dùng, truy vấn tìm kiếm, thời gian) từ trang Vấn đề trung tâm | Mẫu nhất quán theo khóa, xác suất $a/b$ theo cách chọn $h$; cỡ mẫu kỳ vọng $ar/b$ tăng theo dòng, là nhu cầu của mạch hồ chứa | Chu trình cụm thuật toán đủ bước: ví dụ tính tay (K01) → sai lệch tổng quát (K09) → phương án trước và giới hạn (K01B, dòng đầu K02) → ý tưởng so với bảng và chạy một bước (K02) → Đầu vào/Giả thiết/Đầu ra ngay trước giả mã (K04) → tính đúng (K05) → áp dụng (K06) → chi phí (K07) → kiểm tra (K08) | KT (`id="mach-3"`), điểm vào mạch 3 |

Thứ tự trang: KT → K01 → K09 → K01B → K02 → K04 → K05 → K06 → K07 → K08. Bỏ K00 (nhu cầu vào K01) và K03 (đặc tả gộp vào K04). K09 là ID mới cho trang sai lệch tổng quát. Tỷ lệ $1/10$ ($b=10$, $a=1$) dùng xuyên mạch: số rút ở K01B và giá trị băm ở K02 trùng nhau (An 0, Bình 7, Chi 4), nên hai phương án cho cùng mẫu và An được giữ ở cả hai. Không giữ ví dụ 30% của slide MMDS trên mặt trang (chỉ nêu trong ghi chú K02, K04) vì tỷ lệ $1/10$ là tình huống của MMDS §4.2.1 và của trang Vấn đề trung tâm.

**Câu hỏi trước khi sửa.**

| Trang cũ | Trang muốn nói | Phục vụ chủ đề mạch? | Vấn đề còn lại | Quyết định |
|---|---|---|---|---|
| KT | Điểm vào mạch 3 | có | Lời dẫn 22 âm tiết; ghi chú liệt kê trang, chưa nhận đầu ra mạch 2 | sửa |
| K00 | Nhu cầu giữ quan hệ lặp | có | `h1` cũ, tiêu đề là câu, trùng vai KT, dòng 26 âm tiết, không có số | bỏ |
| K01 | Mẫu từng bộ cho $d/(10x+19d)$ | có | Không có ví dụ tính tay; thẻ màu là tín hiệu chính; câu chốt phủ định khó hiểu | tách: K01 thành ví dụ An, thêm K09 tổng quát |
| K01B | Bảng giữ/bỏ theo người dùng | có | Hai câu hỏi rời; "Nhu cầu" chưa nói truy vấn tìm kiếm | sửa nhẹ |
| K02 | Một khóa một quyết định, ví dụ 30% | có | Tiêu đề là câu; trang chỉ có hình; ý "băm thay bảng" không có trên mặt trang; tỷ lệ 30% lệch $1/10$ của K01B | sửa, hình mới |
| K03 | Đặc tả mẫu tỷ lệ $a/b$ | có | KaTeX trong tiêu đề; chưa dùng Đầu vào/Đầu ra | gộp vào K04 |
| K04 | Giả mã | có | Tiêu đề là câu dùng khái niệm chưa giới thiệu; "Điều kiện dừng" gượng; ghi chú chỉ đường | sửa |
| K05 | Nhất quán và xác suất | có | Tiêu đề là câu; nhãn "Lập luận."; dòng 25 âm tiết | sửa |
| K06 | Khóa theo đơn vị thống kê | có | Ba thẻ chung chung; câu hỏi lặp đề; "Đáp án" | sửa |
| K07 | Chi phí và cỡ mẫu | có | Tiêu đề tương phản; thiếu "Mô hình:" và bảng đếm; "khóa nặng" chưa định nghĩa | sửa |
| K08 | Kiểm ngưỡng và khóa $10^6$ bộ | có | Tiêu đề chung chung; "Đáp án" | sửa |

**Từng trang.**

| Trang | Mục đích | Hành động của sinh viên | Đối tượng trung tâm | Dữ kiện, ký hiệu kế thừa | Sản phẩm học tập và bằng chứng | Quyết định và lý do | Âm tiết (dòng, max dòng) trước → sau | Phút |
|---|---|---|---|---|---|---|---|---:|
| KT | Điểm vào mạch 3 | Nhận nhiệm vụ của mạch | Lời dẫn "Muốn ước lượng tỷ lệ truy vấn lặp của mỗi người dùng, phải giữ hoặc bỏ trọn từng người."; năm cụm khóa | Đầu ra mạch 2 | Nêu được vì sao phải giữ trọn từng người | sửa: lời dẫn 19 âm tiết; ghi chú nhận đầu ra mạch 2 và trao cỡ mẫu tăng theo dòng cho mạch 4 | 39 (2, 22) → 39 (2, 20); ghi chú 99 → 94 | 0,5 |
| K01 | Ví dụ tính tay của sai lệch | Tính xác suất giữ hai, một bộ "đồ thị" và xác suất có điều kiện | An: "đồ thị" hai lần, "băm" một lần; tỷ lệ lặp $1/2$; $1/100$, $18/100$, $1/10$; $1/19$ | Tỷ lệ $1/10$ của trang Vấn đề trung tâm | Bảng xác suất; bằng chứng: K09 dùng cùng $u=d=1$ | sửa: ví dụ có số trước công thức; dữ kiện An do học phần dựng | 53 (4, 25) → 56 (6, 17); ghi chú 92 → 118 | 3 |
| K09 | Sai lệch tổng quát | Đọc bảng số đếm kỳ vọng, rút $d/(10u+19d)$ | Bảng `Loại \| Trong dòng \| Kỳ vọng thấy hai lần \| Kỳ vọng thấy một lần`; $\dfrac{d}{10u+19d}\ne\dfrac{d}{u+d}$; $u=d=1$: $1/29$ | MMDS tr.136–137; $u$ thay $s$ của sách | Công thức sai lệch; bằng chứng: lời giải K06 dùng lại | thêm (ID mới). Câu "tỷ số các số đếm kỳ vọng" ở ghi chú; ghi chú giải thích $1/29$ khác $1/19$ | — → 31 (5, 16); ghi chú — → 112 | 3 |
| K01B | Phương án trước: bảng nhãn | Trả lời bảng tăng theo gì, khi nào vượt bộ nhớ | Bảng An 0 giữ, Bình 7 bỏ, Chi 4 bỏ | Tỷ lệ $1/10$; mô hình dòng | Lời giải: tăng theo số người dùng phân biệt, tối đa $r$ | sửa nhẹ: "Nhu cầu" nói "truy vấn tìm kiếm"; gộp hai câu hỏi thành một | 56 (6, 18) → 58 (5, 18); ghi chú 116 → 112 | 2,5 |
| K02 | Ý tưởng băm thay bảng, chạy một bước | So bảng và hàm băm; đọc giá trị băm | Giới hạn có số: $10^8$ người dùng × 16 byte = 1,6 GB (giả định); "tương tự bảng nhưng không lưu"; $h(\text{An})=0$ giữ cả hai bộ | Số rút của K01B | Nêu được vì sao băm cho cùng nhãn; bằng chứng: Mệnh đề thứ nhất ở K05 | sửa: tiêu đề "Hàm băm thay bảng nhãn"; hình mới `bam-theo-nguoi-dung.svg` (tỷ lệ $1/10$, giá trị băm trùng số rút). `key-sampling.svg` giữ nguyên vì ghi chú bài giảng còn dùng | 0 (0, 0) → 38 (3, 15); ghi chú 52 → 124 | 3 |
| K04 | Thuật toán | Đọc Đầu vào, Giả thiết, Đầu ra, giả mã | `LẤY-MẪU-THEO-KHÓA(t; a, h)`; phép quyết định là so sánh với $a$ | $h$, $b$, $a$ | Viết được đặc tả và giả mã | sửa và gộp K03: đặc tả ngay trước giả mã; bỏ "Điều kiện dừng"; ghi chú nêu biên $a=0$, $a=b$, lý do dùng "<", khóa nhiều thành phần | K03 37 (3, 18) + K04 20 (1, 20) → 45 (4, 14); ghi chú 85 + 39 → 104 | 3 |
| K05 | Tính đúng | Đọc hai mệnh đề và chứng minh | Nhất quán tất định; xác suất $a/b$ theo cách chọn $h$ | Đặc tả K04 | Chứng minh được hai mệnh đề; bằng chứng: câu hỏi K08 | sửa: tiêu đề "Tính đúng: lấy mẫu theo khóa"; "Chứng minh." thay "Lập luận."; hệ quả tỷ lệ lặp đúng nằm trong ghi chú để giữ mật độ | 56 (3, 25) → 51 (4, 16); ghi chú 44 → 120 | 3 |
| K06 | Chọn khóa | Ghép thống kê với khóa; trả lời câu hỏi khóa (người dùng, thời gian) | Bảng ba thống kê theo MMDS §4.2.3 | Sai lệch K09 | Lời giải: không, vì mỗi bộ một khóa, quay về mẫu từng bộ | sửa: bỏ ba thẻ; câu hỏi không lặp đề, không lộ Bài tập 4.2.1; "Lời giải" | 60 (3, 12) → 52 (6, 17); ghi chú 38 → 112 | 2,5 |
| K07 | Chi phí | Đếm phép toán mỗi bộ và sau $r$ bộ | Bảng thành phần; cỡ mẫu kỳ vọng $ar/b$; hạ ngưỡng (MMDS §4.2.4) | Mô hình từ máy của mạch 2 | Đếm được chi phí; bằng chứng: trang so sánh với hồ chứa ở mạch 4 | sửa: tiêu đề "Chi phí: lấy mẫu theo khóa"; "Mô hình:" đầu trang; bảng đếm; "khóa nặng" thay bằng "khóa nhiều bộ"; ngưỡng $\tau$ của §4.2.4 trong ghi chú | 39 (2, 18) → 46 (6, 14); ghi chú 48 → 129 | 2 |
| K08 | Kiểm tra | Chọn điều kiện ngưỡng; nêu bảo đảm cho khóa $10^6$ bộ | Câu hỏi ngưỡng $<20$ hay $\le20$ | K04, K05 | Lời giải: $<20$ cho đúng 20 giá trị; khóa giữ trọn hoặc bỏ trọn; không bảo đảm 20% số bộ | sửa: tiêu đề "Ngưỡng băm và khóa nhiều bộ"; câu hỏi tách ba dòng; "Lời giải" | 28 (0, 0) → 32 (4, 19); ghi chú 36 → 81 | 1,5 |

Tổng mạch 3: 24 phút (trước: KT 0,5, K00 2,5, K01 4, K01B 2,5, K02 3, K03 3, K04 3, K05 3, K06 3, K07 2, K08 2 = 28,5). Tổng phần giảng tạm: 117 phút; 3 phút còn lại phân bổ khi duyệt mạch 4–5 (mạch Bloom filter có nhiều trang nhất).

Số đã tự tính: $\frac1{10}\cdot\frac1{10}=\frac1{100}$; $2\cdot\frac1{10}\cdot\frac9{10}=\frac{18}{100}$; $\Pr[\text{không giữ bộ nào}]=\frac{81}{100}$, tổng ba trường hợp bằng 1; $\frac{1/100}{19/100}=\frac1{19}$; $\frac{1/100}{1/10+19/100}=\frac{1}{29}$; $10u+19d=u+d\iff 9u+18d=0$; $10^8\cdot16=1{,}6\cdot10^9$ byte; kỳ vọng cỡ mẫu $\sum_{\text{bộ}}\Pr[\text{giữ}]=ar/b$; với $\{0,\ldots,99\}$, $h<20$ có 20 giá trị, $h\le20$ có 21.

Dữ kiện do học phần dựng: dòng năm bộ (An, “đồ thị”), (Bình, “lọc”), (An, “băm”), (An, “đồ thị”), (Chi, “lọc”), trong đó An có đúng ba bộ của K01; giá trị băm $h(\text{An})=0$, $h(\text{Bình})=7$, $h(\text{Chi})=4$ (trùng số rút ở K01B); giả định $10^8$ người dùng, 16 byte mỗi hàng; câu hỏi K06 và K08.

**Sửa sau lượt rà lại mạch 3 (2026-10-28).** Các số đo dưới đây thay cột âm tiết của bảng trên.

| Trang | Thay đổi | Âm tiết (dòng, max dòng); ghi chú |
|---|---|---|
| A06 (mạch 2) | Ghi chú thêm câu nối sang mạch 3: truy vấn theo từng nhóm phải nhớ truy vấn đã gặp của từng người, trạng thái tăng theo dòng | 28 (5, 15); ghi chú 100 → 141 |
| K01 | Mặt trang định nghĩa tỷ lệ lặp ("1 trong 2 truy vấn được gõ lại"); cột "Được giữ"; câu chốt nêu rõ biến cố điều kiện | 56 (6, 18); ghi chú 118 |
| K09 | Mẫu số đủ ba số hạng $u/10+d/100+18d/100$; cột "Kỳ vọng còn hai bản / một bản"; câu chốt nêu lý do $1/29\ne1/19$ | 38 (5, 16); ghi chú 112 |
| K01B | Hình dùng dòng năm bộ, An đủ ba bộ; bảng ba hàng sau năm bộ; ghi chú: mẫu chứa đủ ba bộ của An, tỷ lệ lặp trên mẫu $1/2$ | 58 (5, 18); ghi chú 122 |
| K02 | Dòng giới hạn nêu bảng tăng không chặn; hình năm bộ, ba bộ của An in đậm; "cả ba bộ của An vào mẫu"; ghi chú thêm "không có thời gian ra đĩa"; hình đổi từ `stream-short` sang `stream-figure` để chữ trong hình ≥ 22 px | 40 (3, 16); ghi chú 144 |
| K04 | Gọi tên "số ngăn $b$", "ngưỡng $a$"; "đưa t vào mẫu" thay "phát vào dòng mẫu"; Đầu ra "mẫu gồm…"; câu đọc giả mã nêu điều còn mở (tính đều do cách chọn $h$) | 50 (4, 17); ghi chú 111 |
| K05 | Ghi chú: mẫu chứa đủ ba bộ của An và cho $1/2$ | 51 (4, 16); ghi chú 126 |
| K06 | "Khóa nhận diện đơn vị…"; câu hỏi "có cho đúng tỷ lệ truy vấn lặp của từng người không?"; lời giải nêu giả thiết thêm: giá trị băm của các khóa khác nhau độc lập | 55 (6, 19); ghi chú 136 |
| K07 | Bỏ dòng nguồn trên mặt trang; câu chốt nêu tỷ lệ khóa giảm dần khi hạ ngưỡng | 51 (6, 19); ghi chú 129 |
| K08 | Nhãn "Câu hỏi:" đứng trước câu hỏi thật | 33 (3, 19); ghi chú 81 |

Giả mã K04: dấu tiếng Việt lệch trên ảnh chụp do phông monospace của máy chụp, giống Bài 07; không xử lý theo quyết định của điều phối viên. Giữ "thời gian" (không đổi sang "thời điểm") để khớp bộ (người dùng, truy vấn, thời gian) dùng trên toàn deck.

### Mạch 4. Lấy mẫu hồ chứa

**Bản đồ mạch.**

| Loại | Chức năng | Vào | Ra | Đóng góp | Trang tiêu đề mạch |
|---|---|---|---|---|---|
| thuật toán | Nêu nhu cầu mẫu cỡ cố định, ý tưởng hồ chứa, chạy tay vết hai ô, giả mã có đặc tả, chứng minh bất biến $s/r$ bằng quy nạp, đếm chi phí, so với mẫu theo khóa | Mạch 3: mẫu theo khóa có cỡ kỳ vọng $ar/b$ tăng theo dòng; hạ ngưỡng làm tỷ lệ khóa đổi; khóa $10^6$ bộ | Hồ chứa $W$ đúng $s$ ô; với $r\ge s$, mỗi phần tử đã đọc nằm trong $W$ với xác suất $s/r$ (xác suất của từng phần tử riêng lẻ); chi phí $\Theta(s)$ bộ nhớ, $O(1)$ mỗi phần tử; không giữ trọn theo khóa | Chu trình cụm thuật toán đủ bước: giới hạn có số và nhu cầu (R00) → ý tưởng so với mẫu theo khóa (R01) → chạy tay (R03) → Đầu vào/Đầu ra ngay trước giả mã (R04) → tính đúng: mệnh đề, cơ sở, giả thiết quy nạp (R05) và hai nửa bước quy nạp (R06, R07) → chi phí (R08) → so sánh và câu hỏi kiểm (R09) | RT (`id="mach-4"`), điểm vào mạch 4 |

Thứ tự trang: RT → R00 → R01 → R03 → R04 → R05 → R06 → R07 → R08 → R09. Gộp R02 (đặc tả) vào R04. Bảng so sánh cũ của R01 chuyển xuống R09 (ID mới), sau khi hồ chứa đã được định nghĩa và chứng minh, ghép với câu hỏi kiểm; R01 thành trang ý tưởng. Lý do không đưa bảng so sánh vào trang chi phí: trang chi phí đếm bước của một thuật toán, còn bảng so sánh đối chiếu hai thuật toán theo đơn vị, cỡ mẫu và bảo đảm. Sách MMDS 3e không có bài tập hồ chứa; câu hỏi R09 do học phần dựng.

**Câu hỏi trước khi sửa.**

| Trang cũ | Trang muốn nói | Phục vụ chủ đề mạch? | Vấn đề còn lại | Quyết định |
|---|---|---|---|---|
| RT | Điểm vào mạch 4 | có | "Xác suất biên" chưa giải nghĩa; ghi chú liệt kê trang, chạm trần 100 | sửa |
| R00 | Bảo đảm $s/r$ | có | `h1` cũ; nêu kết quả trước vấn đề; dòng 29 âm tiết; không có ví dụ số | sửa: trang nhu cầu có giới hạn và ví dụ số |
| R01 | So sánh với mẫu theo khóa | một phần | Dùng $\min(r,s)$, $s/r$ trước khi hồ chứa được định nghĩa; ghi chú siêu bình luận | sửa: thành trang ý tưởng; bảng so sánh chuyển sang R09 |
| R03 | Vết $s=2$ | có | KaTeX trong tiêu đề; quy tắc $j$ chỉ có trong hình; chữ hình 21 đơn vị | sửa |
| R02 | Đặc tả theo tiền tố | có | Tiêu đề khó hiểu; ghi chú "vết chạy vừa trình bày" | gộp vào R04 |
| R04 | Giả mã | có | Tiêu đề là câu; giả mã nhận $r$ từ ngoài, không khởi tạo; không có Đầu vào/Đầu ra; dùng $S$ | sửa |
| R05 | Bất biến và cơ sở | có | Tiêu đề không theo dạng "Tính đúng:"; thiếu giả thiết về $j$; dòng 25 âm tiết | sửa |
| R06 | Phần tử mới | có | Không nhắc $j$ đều trên $\{1,\ldots,r+1\}$; tiêu đề là câu | sửa, thêm hình |
| R07 | Phần tử cũ | có | KaTeX trong tiêu đề; câu đầu sai ngữ pháp; không phát biểu giả thiết quy nạp và tính độc lập | sửa, thêm hình |
| R08 | Chi phí và câu hỏi $s=100$, $r=1\,000$ | có | Tiêu đề là câu; thiếu "Mô hình:" và bảng; "Đáp án"; ghi chú biên soạn | sửa: trang chi phí; câu hỏi chuyển sang R09 |

**Từng trang.**

| Trang | Mục đích | Hành động của sinh viên | Đối tượng trung tâm | Dữ kiện, ký hiệu kế thừa | Sản phẩm học tập và bằng chứng | Quyết định và lý do | Âm tiết (dòng, max dòng) trước → sau | Phút |
|---|---|---|---|---|---|---|---|---:|
| RT | Điểm vào mạch 4 | Nhận nhiệm vụ của mạch | Lời dẫn "Muốn giữ đúng $s$ phần tử khi chưa biết độ dài dòng, phải thay ngẫu nhiên theo vị trí." | Đầu ra mạch 3 | — | sửa: bỏ "xác suất biên"; ghi chú nêu "xác suất của từng phần tử riêng lẻ", nhận đầu ra mạch 3, trao mạch 5 | 34 (2, 21) → 37 (2, 19); ghi chú 100 → 89 | 0,5 |
| R00 | Nhu cầu mẫu cỡ cố định | Tính xác suất cần cho từng phần tử với $s=2$ | Giới hạn: khóa $10^6$ bộ chiếm $10^6$ ô; ví dụ $2/5$, $2/7$; cách lưu cả dòng | Khóa $10^6$ bộ (mạch 3); $s$, $r$ (P04) | Nêu được yêu cầu $s/r$ | sửa: tiêu đề "Mẫu cỡ cố định"; giới hạn có số trước nhu cầu; ví dụ slide MMDS tr.18 | 37 (1, 29) → 53 (4, 15); ghi chú 65 → 101 | 2,5 |
| R01 | Ý tưởng | So hồ chứa với mẫu theo khóa; đọc quy tắc rút $j$ | "Tương tự … Khác …"; quy tắc $j$; trực quan $s/r$ và ô chọn đều | Mẫu theo khóa | Phát biểu quy tắc bằng lời | sửa: thay bảng so sánh bằng trang ý tưởng; quy tắc $j$ lên mặt trang trước vết | 33 (4, 10) → 55 (4, 18); ghi chú 26 → 91 | 3 |
| R03 | Chạy tay | Lập vết $s=2$ trên $a,x,c,y,z$ với $j=$ –, –, 2, 4, 1 | Hình `reservoir-trace.svg`; hồ cuối $[z,c]$ | Quy tắc R01 | Vết; bằng chứng: hình nhỏ ở R04, ví dụ ở R06 | sửa: tiêu đề "Ví dụ: vết chạy hồ chứa hai ô"; dòng dữ kiện và dòng kết luận; chữ hình tăng lên 26–28 đơn vị | 14 (1, 14) → 13 (2, 7); ghi chú 76 → 72 | 3 |
| R04 | Thuật toán | Đọc Đầu vào/Đầu ra, giả mã; đối chiếu với hình nhỏ | `HỒ-CHỨA(x₁, x₂, …; s)` 8 dòng, tự đếm $r$, mảng $W$; hình `reservoir-mini.svg` | Vết R03 hiện lại bằng hình nhỏ | Viết được giả mã; bằng chứng: chứng minh R05–R07 | sửa và gộp R02: đặc tả ngay trước giả mã; $W$ thay $S$; dòng đọc giả mã nêu phép quyết định | R02 34 (2, 18) + R04 24 → 35 (3, 15); ghi chú 36 + 69 → 103 | 3,5 |
| R05 | Tính đúng | Đọc mệnh đề, cơ sở, giả thiết quy nạp | Mệnh đề với giả thiết $j$ đều, độc lập; cơ sở $r=s$; cỡ đúng $s$ | Giả mã R04 | Phát biểu được bất biến | sửa: tiêu đề "Tính đúng: lấy mẫu hồ chứa"; giả thiết quy nạp hiện rõ | 47 (3, 25) → 56 (5, 16); ghi chú 31 → 88 | 2 |
| R06 | Nửa thứ nhất bước quy nạp | Tính $\Pr[x_{r+1}\in W]$ | Công thức $s/(r+1)$; hình `reservoir-step.svg` ($r+1=5$, $s=2$) | $j$ đều trên $\{1,\ldots,r+1\}$ nêu lại trên trang | $2/5$ khớp $z$ của vết | sửa: tiêu đề "Chứng minh: bất biến hồ chứa, phần tử mới"; thêm hình | 19 (2, 10) → 13 (3, 7); ghi chú 30 → 62 | 2,5 |
| R07 | Nửa thứ hai bước quy nạp | Nhân giả thiết quy nạp với xác suất không bị thay | Giả thiết quy nạp hiện rõ; $\Pr[\text{bị thay}\mid x_i\in W]=1/(r+1)$; tính độc lập của $j$ | Hình `reservoir-step.svg` | $\frac{s}{r}(1-\frac1{r+1})=\frac{s}{r+1}$; ví dụ $\frac24\cdot\frac45=\frac25$ trong ghi chú | sửa: tiêu đề "Chứng minh: bất biến hồ chứa, phần tử cũ"; không KaTeX trong tiêu đề | 16 (2, 15) → 24 (4, 14); ghi chú 40 → 141 | 3 |
| R08 | Chi phí | Đếm bước mỗi phần tử và sau $r$ phần tử | "Mô hình: RAM…"; bảng tăng $r$, rút $j$, ghi $W$; $\Theta(s)$ bộ nhớ, $O(1)$ mỗi phần tử | Mô hình từ máy (mạch 2) | Đếm được chi phí; số lần ghi kỳ vọng $\approx s(1+\ln\frac rs)$ trong ghi chú | sửa: tiêu đề "Chi phí: lấy mẫu hồ chứa"; bỏ "Đáp án" và ghi chú biên soạn | 48 (2, 24) → 37 (5, 13); ghi chú 58 → 78 | 2 |
| R09 | So sánh và kiểm tra | Đối chiếu hai cách lấy mẫu; tính kỳ vọng số bộ của An | Bảng theo khóa ↔ hồ chứa; câu hỏi $r=1\,000$, An 10 bộ, $s=100$ | Mẫu theo khóa (mạch 3) | Lời giải: $10\cdot0{,}1=1$ bộ; không giữ trọn | thêm (ID mới): bảng so sánh cũ đặt sau định nghĩa; câu hỏi không chỉ thay số | — → 46 (7, 18); ghi chú — → 101 | 3 |

Tổng mạch 4: 25 phút (trước: RT 0,5, R00 2,5, R01 2, R03 3, R02 3, R04 4, R05 3, R06 2, R07 3, R08 3 = 26). Tổng phần giảng tạm: 116 phút; 4 phút phân bổ cho mạch 5 khi duyệt (các trang mới B05B, phi tiêu và định nghĩa dương giả theo báo cáo rà deck).

Số đã tự tính: vết $[a]\to[a,x]\to[a,c]\to[a,c]\to[z,c]$; xác suất nhận $c$, $y$, $z$ lần lượt $2/3$, $2/4$, $2/5$; ở $r+1=5$, $s=2$: nhận $2/5$, bỏ $3/5$, phần tử cũ bị thay $1/5$, còn lại $4/5$, $\frac24\cdot\frac45=\frac25$; $\frac{s}{r}(1-\frac1{r+1})=\frac{s}{r}\cdot\frac{r}{r+1}=\frac{s}{r+1}$; $s=100$, $r=1\,000$: $0{,}1$, kỳ vọng $10\cdot0{,}1=1$; số lần rút $r-s$; số lần ghi kỳ vọng $s+\sum_{k=s+1}^{r}s/k\approx s(1+\ln(r/s))$.

Hình: `reservoir-mini.svg` (mới, R04), `reservoir-step.svg` (mới, R06, R07), `reservoir-trace.svg` (sửa cỡ chữ 21–25 → 26–28, không đổi nội dung; ghi chú bài giảng cũng dùng hình này).

**Sửa sau lượt rà lại mạch 4 (2026-10-28).** Các số đo dưới đây thay cột âm tiết của bảng trên.

| Trang | Thay đổi | Âm tiết (dòng, max dòng); ghi chú |
|---|---|---|
| RT | Lời dẫn bỏ KaTeX: "Muốn giữ số phần tử cố định khi chưa biết độ dài dòng, phải thay ngẫu nhiên theo vị trí." | 39 (2, 20); ghi chú 89 |
| R00 | "nếu được giữ"; "sao cho"; tên phần tử a, x, c, y, z viết chữ đứng; câu ví dụ và câu "lưu cả $r$ phần tử" gọn lại | 58 (4, 18); ghi chú 101 |
| R01 | So sánh đúng với mẫu theo khóa: giống ở quy tắc ngưỡng ($j\le s$ thay cho $h(K)<a$), khác ở chỗ $j$ rút lại ở mỗi vị trí và phần tử đã giữ có thể bị thay | 58 (4, 18); ghi chú 101 |
| R03 | Tên phần tử chữ đứng trên mặt trang và ghi chú; "phần tử x và y không còn" | 24 (2, 13); ghi chú 76 |
| R04 | "số rút đều, độc lập với các lần rút trước và $W$" (lần dùng đầu nói rõ) | 37 (3, 16); ghi chú 104 |
| R05 | "độc lập với các lần rút trước"; ghi chú nêu "và vì thế với nội dung $W$" | 58 (5, 18); ghi chú 97 |
| R06 | Tiêu đề "Chứng minh: xác suất có mặt, phần tử mới"; dòng ví dụ không còn ngụ ý một lần chạy kiểm được xác suất; alt nêu điều kiện của $4/5$ | 24 (3, 18); ghi chú 62 |
| R07 | Tiêu đề "Chứng minh: xác suất có mặt, phần tử cũ"; bỏ hình (trùng R06), thay bằng dòng "Ví dụ. $s=2$, $r=4$: $\frac24\cdot\frac45=\frac25$"; ghi chú mô tả đúng phép tính của slide MMDS tr.21: $(1-\frac{s}{r+1})+\frac{s}{r+1}\cdot\frac{s-1}{s}=\frac{r}{r+1}$ | 27 (5, 14); ghi chú 154 (chứng minh, dưới mức 250) |
| R08 | Mô hình đếm như mạch 2–3 (phép toán mỗi phần tử, rút một số đều tính 1 phép, từ máy); bỏ "RAM"; ô ghi $W$: kỳ vọng $\approx s(1+\ln\frac rs)$; câu kết nêu trường hợp xấu nhất | 49 (5, 20); ghi chú 85 |
| R09 | Bỏ hàng "Đơn vị chọn" (hàng "Nhất quán theo khóa" đã hàm ý), còn 6 dòng | 41 (6, 18); ghi chú 101 |

Hình: `reservoir-step.svg` ghi điều kiện cho $4/5$ ("khi xᵢ đang ở ô 1, xᵢ còn lại với xác suất 4/5"), desc khớp; `reservoir-mini.svg` desc thêm "x và a bị thay".

CSS: thêm vào khối `.lecture-stream` biến `--r-code-font` (Consolas, "SF Mono", "Liberation Mono", "Noto Mono", "Courier New", monospace) để giả mã hiển thị đúng dấu tiếng Việt; phông mặc định `monospace` phân giải thành DejaVu Sans Mono trên máy kiểm và tách dấu. Đã kiểm K04, R04, B04 đúng dấu, không tràn khung; Bài 02, 03 không có phần tử `.lecture-stream`, không lỗi. Bài 07 có cùng lỗi phông; để nâng thành lớp chung ở lượt sau.

Thời lượng: mạch 4 giữ 25 phút; tổng phần giảng tạm 116 phút. Mạch 5 (Bloom filter) và mạch 6 (tổng kết) nhận 4 phút còn lại khi duyệt.
