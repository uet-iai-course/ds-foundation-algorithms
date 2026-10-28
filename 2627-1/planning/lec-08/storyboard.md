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
| 2. Mô hình tính toán trên dòng | AT, A00–A04 | Mục 1 | `lec-08-topic-02` | chờ viết |
| 3. Lấy mẫu theo khóa | KT, K00–K08 | Mục 2.1–2.4 | `lec-08-topic-03`…`06` | chờ viết |
| 4. Lấy mẫu hồ chứa | RT, R00–R08 | Mục 3.1–3.5 | `lec-08-topic-07`, `08` | chờ viết |
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
