# Storyboard Bài 8

Mục hiện hành: **Lượt duyệt từng mạch (2026-10-28)**, cùng các thay đổi ghi ở **Lượt biên tập theo bản đánh giá giảng dạy (2026-10-28)** và **Trang bài toán đầu mạch (2026-10-29)** ở cuối tệp; khi các mục khác nhau, mục sau cùng được áp dụng. Các mục trước giữ làm lịch sử; khi mâu thuẫn, mục hiện hành được áp dụng.

## Hành trình khái niệm

- **Lấy mẫu theo khóa:** tình huống P01 → vấn đề K00–K01 → trực giác và ví dụ K02 → đặc tả K03 → thuật toán K04 → lập luận đúng K05 → ứng dụng K06, chi phí K07 → kiểm tra K08.
- **Lấy mẫu hồ chứa:** tình huống P01, R00 → phân biệt mục tiêu R01 → ví dụ chạy tay R03 → đặc tả R02 → thuật toán R04 → bất biến và chứng minh R05–R07 → chi phí, giả thiết ngẫu nhiên và kiểm tra R08.
- **Bloom filter:** tình huống B00 → khó khăn chính và lỗi một phía B13 → vị trí trong hệ thống B02 → trực giác và ví dụ B05 → đặc tả B01 → thuật toán B03–B04 → bảo đảm B06 → hình thức hóa và xác suất B07–B11 → chi phí, giới hạn và kiểm tra B12.

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
| Bloom filter | tình huống B00; vấn đề B13 (thêm 2026-10-29), B02; trực giác–ví dụ B05; hình thức B01; thuật toán B03–B04; đúng B06; xác suất–chi phí B07–B11; kiểm tra B12 | $S,m,n,k,h_i$ → “chắc chắn không” hoặc “có thể thuộc” | ví dụ 11 bit truyền chỉ số, va chạm và hai câu trả lời sang đặc tả/giả mã; $q$ ở B07 truyền sang FPR B08 và tối ưu B10 | trực giác và ví dụ gộp B05; ứng dụng và kiểm tra gộp B12 | Ví dụ cụ thể được khái quát thành hợp đồng, rồi phân tích tỷ lệ dương giả. | 44 |
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

Lịch sử, thay bằng mục "Mạch 7" của lượt duyệt 2026-10-28: X00 và X05 đã bỏ, thêm X04B; số phút và lời giải hiện hành ghi ở mục đó.

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

Cập nhật 2026-10-28. Ghi chú được viết lại thành chương giáo trình theo `AGENTS.md` §"Tiêu chuẩn giáo trình cho ghi chú bài giảng", lần lượt theo mạch của deck. Mã chủ đề cũ `L08-N01`…`L08-N11` được thay bằng `lec-08-topic-01`…`lec-08-topic-17` (ánh xạ cũ → mới ở `outline.md`, mục "Bản đồ chủ đề cho ghi chú tự học"). ~~Trong thời gian chuyển tiếp, các mục cũ chưa viết lại vẫn nằm sau phần đầu chương và chưa mang `note-topic-id`.~~ Đã giải trừ 2026-10-28: toàn chương đã viết lại, đủ 17 `note-topic-id`.

**Ánh xạ mạch deck → phần ghi chú → chủ đề.**

| Mạch deck | `data-slide-id` | Phần ghi chú | `note-topic-id` | Trạng thái |
|---|---|---|---|---|
| 1. Mở đầu | P00, P04, P02, P03, P01 | Giới thiệu chương, Mục tiêu học tập, Kiến thức tiên quyết, Bảng ký hiệu, Bản đồ chủ đề | `lec-08-topic-01` (Kiến thức tiên quyết); các phần còn lại không mang mã | đã viết 2026-10-28 |
| 2. Mô hình tính toán trên dòng | AT, A05, A00, A02, A06 | Mục 1.1–1.6 | `lec-08-topic-02` | đã viết 2026-10-28, sửa sau rà lại mạch 2 |
| 3. Lấy mẫu theo khóa | KT, K01, K09, K01B, K02, K04, K05, K06, K07, K08 | Mục 2.1–2.5 | `lec-08-topic-03`…`06` | đã viết 2026-10-28 |
| 4. Lấy mẫu hồ chứa | RT, R00, R10, R01, R03, R04, R05, R06, R07, R08, R09 | Mục 3.1–3.5 | `lec-08-topic-07`, `08` | đã viết 2026-10-28 |
| 5. Lọc thành viên bằng Bloom filter | BT, B00, B13, B02, B05, B05A, B05B, B01, B03, B04, B06–B12 | Mục 4.1–4.7 | `lec-08-topic-09`…`12` | đã viết 2026-10-28 |
| 6. Tổng kết và chuyển tiếp | CT, C00, C03, C01, C04, C05, C02 | Mục 5.1–5.2, Tình huống áp dụng và ứng dụng, Tóm tắt chương | `lec-08-topic-13`…`15` | đã viết 2026-10-28 |
| 7. Bài tập vận dụng | XT, X01, X02, X03, X04, X04B (X00, X05 đã bỏ) | Bài tập củng cố; Hướng dẫn đọc thêm và tài liệu tham khảo | `lec-08-topic-16`, `17` | đã viết 2026-10-28 |

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

~~Điều kiện công bố (điều phối viên, 2026-10-28): số mục dẫn chiếu trong Mục tiêu học tập và Bản đồ chủ đề theo cấu trúc mới (Mục 1–5, 2.1–2.4, 3.1–3.5, 4.1–4.6) chưa khớp thân bài cũ; phải kiểm lại toàn bộ sau khi mạch 2–7 được viết lại.~~ Đã giải trừ 2026-10-28: mạch 2–7 của ghi chú đã viết lại; trạng thái hiện hành ở đoạn "Trạng thái toàn chương".

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
| 3.1 Mẫu cỡ cố định và ý tưởng | `lec-08-topic-07` | Ví dụ 08.8; đoạn trực quan; Ví dụ 08.9; hình `reservoir-trace.svg` | R00, R10, R01, R03 | Dòng a x c y z k c d e g (slide MMDS Streams 1 tr.18), $2/5$, $2/7$; $j=2,4,1$ (học phần dựng), hồ cuối [z, c]; xác suất nhận $2/3$, $2/4$, $2/5$ |
| 3.2 Đặc tả và thuật toán | (thuộc `lec-08-topic-07`) | Định nghĩa 08.15; Thuật toán 08.16 (biên $r\le s$, $s=1$) | R04 | $W[1..s]$, $s$, $r$, $j$ |
| 3.3 Xác suất $s/r$ | `lec-08-topic-08` | Định lý 08.17 (bốn phần; chứng minh: cơ sở, giả thiết quy nạp, phần tử mới, phần tử cũ có dẫn độc lập của $j$, cỡ); hình `reservoir-step.svg`; hai phản ví dụ; Mệnh đề 08.18 (mọi tập con cỡ $s$ xác suất $1/\binom rs$, bổ sung) | R05, R06, R07 | $W_r$ ký hiệu cục bộ; $E_i$ biến cố bị thay (thay `\text{bị thay}` cũ); $\frac24\cdot\frac45=\frac25$; phản ví dụ phụ thuộc: $\Pr[x_3\in W_4]=1/6$; liệt kê $r=4,s=2$: 12 kết cục, mỗi cặp 2 lần |
| 3.4 Chi phí | (thuộc `lec-08-topic-08`) | Mệnh đề 08.19 (RAM, $\Theta(s)$, $O(1)$, số lần ghi kỳ vọng với cận tích phân); Ví dụ 08.10 ($s=100$, $r=10^6$: $920{,}5$ lần thay, tổng $1\,020{,}5$, cận $1\,020{,}0$ và $1\,021{,}0$) | R08 | — |
| 3.5 Nhầm lẫn, thực hành, so sánh | (thuộc `lec-08-topic-08`) | Nhận xét 08.20, 08.21; bảng so sánh; Bài tập 08.4 (An 10 bộ trong $1\,000$, $s=100$: kỳ vọng 1; giữ trọn với xác suất $\approx6{,}6\cdot10^{-11}$) | R09 | — |

Bộ đếm sau Mục 3: chung 08.15–08.21; Ví dụ 08.8–08.10; Bài tập 08.4. Bản đồ chủ đề đổi: `lec-08-topic-07` là 3.1–3.2, `lec-08-topic-08` là 3.3–3.5 (ghi chú và outline). Số âm tiết Mục 3: 3 111 ở bản đầu, 3 291 sau lượt sửa theo rà lại mạch 4 (đối chiếu quy tắc ngưỡng với mẫu theo khóa; "độc lập với các lần rút trước"; mô hình chi phí của Định nghĩa 08.3 thay mô hình RAM; phép tính hai trường hợp của slide MMDS tr.21; Nhận xét 08.20 tính tỷ số các số đếm kỳ vọng với $p_2=\frac{s(s-1)}{r(r-1)}$; biến vị trí $\ell$ thay $y$ trong chứng minh Mệnh đề 08.18). Từ "thời điểm" trong bộ (người dùng, truy vấn, thời gian) đổi thành "thời gian" ở mọi chỗ của ghi chú, khớp deck và "time" của MMDS.

**Mục 4 (mạch 5).** Thứ tự ghi chú: nhu cầu (MMDS §4.3.1: $10^9$ địa chỉ, từ 20 GB, 1 GB $=8\cdot10^9$ bit) → ý tưởng một hàm băm, nhận xét bit 0, khoảng $1/8$ lọt qua → ví dụ 11 bit (thêm, kiểm tra, dương giả 29) → định nghĩa → hai thuật toán → định lý không âm giả và phản ví dụ → mô hình phi tiêu, bổ đề mật độ bit → mệnh đề $p_{FP}=\mathbb E[(X/n)^k]\ge q^k\ge p(k)$ → ví dụ MMDS $k=1,2$ và ví dụ ba mức xấp xỉ trên 11 bit → hai lực của $k$ → định lý $k^*$ (chứng minh năm bước) → hệ quả số nguyên → ví dụ tám bit mỗi khóa → giới hạn, nhầm lẫn, "Trong thực hành", bài tập → đoạn kết sang Mục 5.

| Phần ghi chú | `note-topic-id` | Khối, số hiệu | Trang deck | Dữ kiện, ký hiệu |
|---|---|---|---|---|
| 4.1 Lọc theo danh sách cho phép | `lec-08-topic-09` | đoạn nhu cầu, trực quan; hình `bloom-pipeline.svg` | BT, B00, B02 | $m=10^9$, $n=8\cdot10^9$; một hàm: khoảng $1/8$ |
| 4.2 Ví dụ 11 bit | (thuộc 09) | Ví dụ 08.11 (thêm 25, 159, 585), hình `bloom-11bit-them.svg`; Ví dụ 08.12 (118 bị loại, 29 dương giả), hình `bloom-11bit-mini.svg` | B05, B05B | $(5,2)$, $(7,0)$, $(9,7)$; $118\to(3,5)$, $29\to(7,2)$ (học phần chọn); mảng 10100101010 |
| 4.3 Đặc tả và thuật toán | (thuộc 09) | Định nghĩa 08.22 (Bloom filter, dương giả, âm giả); Thuật toán 08.23 (xây), 08.24 (kiểm tra) | B01, B03, B04 | khóa chèn $v$ (thêm vào bảng ký hiệu), khóa truy vấn $y$; vị trí bit $c$ |
| 4.4 Không âm giả | `lec-08-topic-10` | Định lý 08.25 (bốn điều kiện), chứng minh hai bước; bốn phản ví dụ trên mảng 11 bit | B06 | $h_1+1\bmod11$ làm 25 đọc $B[6]=0$; mảng tạm 00100101000 làm 159 bị loại |
| 4.5 Mật độ bit và xác suất dương giả | `lec-08-topic-11` | Ví dụ 08.13 ($(7/8)^4\approx0{,}586$); Bổ đề 08.26; Mệnh đề 08.27 ($p_{FP}=\mathbb E[(X/n)^k]$, Jensen, $p(k)\le q^k\le p_{FP}$); Ví dụ 08.14 ($0{,}1175$; $0{,}048929$, sách in $0{,}0493$); Ví dụ 08.15 (11 bit: $0{,}1768\le0{,}1897\le0{,}1951$; $(5/11)^2=0{,}2066$) | B07, B08 | $X$, $q$, $p_{FP}$, $p(k)$ |
| 4.6 Số hàm băm tối ưu | `lec-08-topic-12` | đoạn hai lực, $p(k)\to1$; Định lý 08.28 (đổi biến $\rho,z,\theta$, $\lambda=\ln p$, $\phi$; năm bước); "Ý nghĩa:"; Hệ quả 08.29; Ví dụ 08.16; hình `fpr-curve.svg` | B09, B10, B11 | $k^*=8\ln2\approx5{,}545$; $p(5)=0{,}021679$, $p(6)=0{,}021577$; $2^{-k^*}=0{,}02142$; slide MMDS in khoảng 0,0235 |
| 4.7 Giới hạn, nhầm lẫn, thực hành | (thuộc 12) | đoạn chi phí và ba giới hạn; Nhận xét 08.30, 08.31; Bài tập 08.5 | B12 | $n/m=4$: $p(6)=0{,}2198$, $k^*=2{,}77$, $p(2)=0{,}1548$, $p(3)=0{,}1469$ |

Bộ đếm sau Mục 4: chung 08.22–08.31; Ví dụ 08.11–08.16; Bài tập 08.5. Bài tập 4.3.1–4.3.3 của MMDS không đặt ở Mục 4 (thuộc phần bài tập, lượt mạch 7); lời giải 4.3.3 sẽ dẫn về Định lý 08.28. Biến giá trị băm cục bộ ở Mục 2 đổi từ $v$ sang $c$ để $v$ chỉ là khóa chèn. Bản đồ chủ đề: `lec-08-topic-12` là 4.6–4.7. Hình `bloom-11bit.svg` không còn được ghi chú hay deck dùng. Số âm tiết Mục 4: 4 223 ở bản đầu, 4 337 sau lượt sửa theo rà lại mạch 5 (tương quan âm hai bit nêu đúng chiều; câu hướng chứng minh và dòng kiểm số cho Định lý 08.28; mật độ bit 0,1175 → 0,2212 ở Ví dụ 08.14; slide MMDS Streams 2 tr.14 viết sai công thức).

**Mạch 6 → Mục 5, Tình huống, Tóm tắt.**

| Phần ghi chú | `note-topic-id` | Khối, số hiệu | Trang deck | Dữ kiện |
|---|---|---|---|---|
| 5.1 Kết quả, giả thiết và chi phí | `lec-08-topic-13` | bảng kết quả–giả thiết–công thức (9 hàng, có số hiệu); bảng thuật toán–đầu vào–bảo đảm–chi phí (5 hàng, thêm Thuật toán 08.13); quy trình ba bước | CT, C00, C03 | — |
| 5.2 Trả lời vấn đề trung tâm | (thuộc 13) | ba câu có điều kiện; Ví dụ 08.17 (bốn yêu cầu: mẫu theo khóa, hồ chứa $s=1\,000$, Bloom filter, chưa có → Bài 09); đoạn kết sang Bài 09 | C01 | $1/29$; $s/r$; $p(6)\approx0{,}0216$ |
| Tình huống áp dụng và ứng dụng | `lec-08-topic-14` | Tình huống 08.1 (ngân sách $G=10^8$, $r=3\cdot10^9$, tỷ lệ $\approx1/30$, $\tau+1\approx1{,}43\cdot10^8$); 08.2 ($10^9$ địa chỉ, $k=6$, $\approx21\,600$ trong $10^6$ thư); 08.3 (vi phạm: gỡ $1\,000$ địa chỉ bằng xóa bit, kỳ vọng tới $\approx4\,500$ âm giả vì $6(m-1)k/n\approx4{,}5$; danh sách gấp đôi: $p(6)=0{,}2198$, $\approx219\,800$ lần tra, chọn $k=3$); ứng dụng ở ghi chú Bài 09 Mục 2 và Mục 5 | C01 (ghi chú), C02 | số người dùng, số truy vấn, số thư là giả định của học phần |
| Tóm tắt chương | `lec-08-topic-15` | đoạn bảy câu; kết quả theo Mục 1–5; công thức và thuật toán cần nhớ; giả thiết hay bị bỏ quên | C00–C03 | — |

Câu hỏi tự kiểm tra C04 (ngưỡng 5%: $h<5$, $\frac{d}{20u+39d}$; hồ chứa $s=50$, $r=1\,000$: $0{,}05$) và C05 (không âm giả; gấp đôi $n$: $k^*$ gấp đôi, $p(k^*)$ bình phương, $0{,}0214\to4{,}6\cdot10^{-4}$) không đặt ở Mục 5; chúng sẽ thành bài tập mức nhận biết trong "Bài tập củng cố" ở lượt mạch 7. Dẫn chiếu "Mục k" trong phần đầu chương, mục tiêu, bản đồ chủ đề và đoạn kết các mục đã được kiểm khớp thân bài (Mục 1.1–5.2); điều kiện chặn công bố về số mục được giải trừ cho phần đã viết. Còn chờ mạch 7: "## 11. Bốn bài tập từ giáo trình MMDS" cũ (dùng $x=k\rho$, $t=e^{-x}$, $p_k$, "FPR", "Hướng dẫn chấm"), bài tập 4.3.1–4.3.3 mà Mục tiêu 3 dẫn tới, mục "Bài tập củng cố" (`lec-08-topic-16`), "Hướng dẫn đọc thêm và tài liệu tham khảo" (`lec-08-topic-17`) thay "Tóm tắt nguồn" cũ (còn `https://www.mmds.org`). Số âm tiết: Mục 5 1 184, Tình huống 1 215, Tóm tắt 730 (tổng 3 129); cả tệp 21 883. Sau lượt sửa theo rà lại mạch 6: Mục 5 1 200, Tình huống 1 281, Tóm tắt 732; Mục 3 thêm dẫn MMDS §4.5.5 (tr.148–149) và hộp tr.150 (3 369); cả tệp 22 062. Tình huống 08.1 nêu Mệnh đề 08.10(b) chỉ đúng gần đúng với ngưỡng giảm dần (điều kiện: mỗi khóa rất ít bộ so với $G$); Tình huống 08.3(b) dẫn về Bài tập 08.5 thay vì chép lời giải.

**Mạch 7 → Bài tập củng cố, Tham khảo.**

| Bài tập | Mức | Trang deck / nguồn | Mục tiêu | Số kiểm |
|---|---|---|---|---|
| 08.6 Ngưỡng 5% và mẫu từng bộ | nhận biết | C04 câu 1 | 1 | $h<5$; $d/(20u+39d)$, $u=d=1$: $1/59$ |
| 08.7 Xác suất có mặt trong hồ chứa | nhận biết | C04 câu 2 | 2 | $50/1\,000=0{,}05$ |
| 08.8 Âm giả sau khi thêm khóa | nhận biết | C05 câu 3 | 3 | gỡ 585 làm 159 bị loại |
| 08.9 Gấp đôi số bit | nhận biết | C05 câu 4 | 3 | $k^*$: $5{,}545\to11{,}09$; $p(k^*)$: $0{,}0214\to4{,}6\cdot10^{-4}$ |
| 08.10 Ba và bốn hàm băm | tính toán | X02; MMDS 4.3.1, §4.3.4, tr.141 | 3 | $p(3)=0{,}030579$, $p(4)=0{,}023969$ |
| 08.11 Chia mảng bit | tính toán | X03; MMDS 4.3.2, tr.141 (quy ước $k\mid n$, băm đều độc lập của học phần) | 3 | $n=64,m=8,k=4$: chia $0{,}026450$, $q^k$ $0{,}024556$, chính xác $0{,}025354$; $n=8\cdot10^9,m=10^9,k=4$: trùng 9 chữ số, $0{,}023968650\ldots$ |
| 08.12 Số hàm băm tối ưu | chứng minh | X04, X04B; MMDS 4.3.3, tr.142 | 3 | dẫn về Định lý 08.28, Hệ quả 08.29; $p(5)>p(6)$ |
| 08.13 Chọn khóa lấy mẫu | vận dụng | X01; MMDS 4.2.1, §4.2.5, tr.138 | 1 | (university, courseID); (university, studentID); (university, courseID) |
| 08.14 Hồ chứa cho từng khóa | vận dụng (mở rộng) | MMDS hộp tr.150; Định lý 08.17 | 2 | $s/r_K$; tối đa $sN_K$ bộ; tỷ lệ lặp đúng chỉ khi $r_K\le s$ |

Tham khảo (`lec-08-topic-17`): MMDS 3e Chương 4 với ánh xạ mục ↔ phần của chương; slide MMDS Streams 1–2; CS246 2026 (Leskovec); Ullman 2017; CLRS §2.1; đọc tiếp Bài 09 và Blum–Hopcroft–Kannan §6.1; ghi công http://www.mmds.org. Mục tiêu 3 ở đầu chương đổi dẫn chiếu thành "Bài tập 08.10–08.12".

**Trạng thái toàn chương (2026-10-28).** Đủ 17 `note-topic-id`, mỗi mã một lần. Bộ đếm chung 08.1–08.31 liên tục; Ví dụ 08.1–08.17; Bài tập 08.1–08.14; Tình huống 08.1–08.3; mọi dẫn chiếu "Mục k" và số hiệu khối đều trỏ tới khối có thật. Không còn "Đáp án", "Hướng dẫn chấm", "FPR", "Mục này", "Chương này", `https://www.mmds`, `\text{bị`, $x=k\rho$, $p_k$, mã `L08-N`. Âm tiết: đầu chương 2 938 (giới thiệu và mục tiêu 574, tiên quyết, ký hiệu, bản đồ 2 364), Mục 1 2 819, Mục 2 4 627, Mục 3 3 369, Mục 4 4 341, Mục 5 1 200, Tình huống 1 281, Tóm tắt 732, Bài tập 1 735, Tham khảo 412; toàn chương 23 454. Hình `key-sampling.svg`, `bloom-11bit.svg`, `stream-model.svg` không còn được ghi chú dùng.

**Lượt sửa cuối trước công bố (theo kiểm định cuối F1–F14 và rà lại mạch 7).** Thêm hình `img/lec-08/cau-truc-chuong.svg` và đoạn mở Mục 1 (bài toán của ghi chú Bài 01, số liệu MMDS tr.133 và tr.139, việc chương xây dựng) cùng đoạn đọc hình (F6). Chữ một nghĩa (F1): chỉ số tổng ở Mệnh đề 08.19, Ví dụ 08.10 đổi $k\to i$; tỷ lệ giữ $p\to\eta$ (Nhận xét 08.7, Bài tập 08.6), $p,p_2\to\eta_1,\eta_2$ (Nhận xét 08.20); tập vị trí $T,T'\to A,A'$ (Mệnh đề 08.18); thêm dòng quy ước ký hiệu cục bộ ($M$, $T$, $G$, $W_r$, $E_i$, $A$, $\ell$, $\rho$, $z$, $\theta$, $\lambda$, $\phi$, $c$, $\eta$). F7: câu trực quan đặt trước Định nghĩa 08.1; đoạn 1.2 mở bằng việc đặt thành phần định nghĩa vào hình. F9: đoạn "**Trong thực hành.**" không đánh số sau Mệnh đề 08.14 (giữ nguyên bộ đếm); danh sách "Bỏ …" sau Mệnh đề 08.27 (vị trí truy vấn trùng một khóa của $S$ cho xác suất 1; $h_1=\cdots=h_k$ cho $\approx0{,}1175$ thay $0{,}0216$). F10: năm câu no-ai-slop. F11: "Ở Bài 02, hàm phân phối …". F12: "trang chiếu MMDS (slide)" lần đầu, "trang chiếu" sau đó. F13: bỏ câu nối lặp ở ranh giới Mục 2/3 và 3/4. F14: bỏ "định cỡ cho 1% là bổ sung". Rà lại mạch 7: Ullman ghi năm 2017; Blum–Hopcroft–Kannan ghi bản ngày 04/01/2018 (tệp trong `sources/`), §6.1, tr.181; lời giải 4.2.1(a) "theo kỳ vọng"; MMDS §1.3.5, tr.13–14. Đồng bộ deck: X04B ($z=-\ln\theta$ trong lời giải Bài tập 08.12), B06 (điều kiện 3 và 4 tự thỏa trong mô hình). Kiểm lại toàn chương: 17 `note-topic-id` duy nhất; bộ đếm chung 08.1–08.31, Ví dụ 08.1–08.17, Bài tập 08.1–08.14, Tình huống 08.1–08.3 liên tục; mọi dẫn chiếu Mục và khối khớp; chuỗi cấm bằng 0; liên kết deck HTTP 200. Số âm tiết toàn chương: 24 159.

**Lượt biên tập theo bản đánh giá giảng dạy (2026-10-28), Mục 1 ↔ mạch 2.** Không thêm khối đánh số. §1.4, sau đoạn bộ đệm vòng: đoạn vết cửa sổ 4 số trên dòng $1,5,2,7,4$ (học phần dựng) khi $x_5=4$ đến: bộ đệm $[1,5,2,7]\to[4,5,2,7]$, tổng $15-1+4=18$, ghi tiếp ô 1 → ô 2, bất biến hai phần, trả lời $18/4=4{,}5$; hình `trang-thai-cap-nhat.svg` (trang A07) với đoạn đọc hình nối phép cập nhật và phép trả lời của Định nghĩa 08.1. Bài tập 08.1, lời giải (b): bảng $r,\sum x_i,\sum x_i^2$ sau từng số (1/1/1, 6/26, 8/30, 15/79, 19/95, 19/95, 22/104, 27/129). Đoạn "**Trong thực hành.**" không đánh số sau Bài tập 08.1: cộng $10^9$, float64, công thức $\frac1r\sum x_i^2-\bar x_r^2$ trả $0{,}0$ (hai số $\approx1{,}00000000675\cdot10^{18}$, khoảng cách float64 liền nhau 128); phương pháp Welford (1962) với $V_r$ (ký hiệu cục bộ, tránh $M$ của Mục 1) cho $V_8=37{,}875$, $\sigma_8^2=4{,}734375$ trên dòng gốc và $4{,}7343749866$ trên dòng cộng $10^9$ (chạy lại bằng Python). Tài liệu tham khảo thêm Welford (1962), *Technometrics* 4(3), 419–420, ghi là bổ sung ngoài nguồn chính. Các hàng slide 6–10 khác của kế hoạch không ảnh hưởng ghi chú. Kiểm lại: 17 mã chủ đề, bộ đếm liên tục, dẫn chiếu khớp; toàn chương 24 858 âm tiết.

**Lượt bản đánh giá, Mục 2 ↔ mạch 3.** Không thêm khối đánh số. Ví dụ 08.3: hình `cay-hai-bo-do-thi.svg` sau bảng và đoạn đọc cây (bốn lá $1/100$, $9/100$, $9/100$, $81/100$; hệ số 2 từ hai lá "giữ, bỏ" và "bỏ, giữ"; có mặt $19/100$; chỉ lá đầu có đủ hai bản). Nhận xét 08.7: kiểm $\eta=1$ cho $d/(u+d)$; $1/29=\frac{1/100}{1/10+19/100}$ là tỷ số hai kỳ vọng, tỷ lệ trên mẫu không xác định khi mẫu không có truy vấn của An. Mở §2.2: "cụm" (người dùng cùng mọi bộ). Sau Mệnh đề 08.10: số khóa được giữ trong một lần chạy là ngẫu nhiên, $a/b$ là xác suất cho từng khóa. Nhận xét 08.11: $h$ chọn ngẫu nhiên một lần trước dòng rồi cố định, khác hồ chứa rút số mới mỗi phần tử (Mục 3). Mục 2: 4 966 âm tiết; toàn chương 25 233.

**Lượt bản đánh giá, Mục 3 ↔ mạch 4.** Không thêm khối đánh số. Nhận xét 08.20: gạch đầu dòng phân biệt $s/(r+1)$ (nhận $x_{r+1}$, có một ô bị thay) với $1/(r+1)$ (thay đúng ô của $x_i$). Bài tập 08.4, lời giải: kỳ vọng 1 không có nghĩa đúng một bộ mỗi lần; $\Pr[\text{không bộ nào của An}]=\binom{990}{100}/\binom{1000}{100}\approx0{,}347$ (Mệnh đề 08.18; tính lại 0,346928). Trường hợp biên $s=1$ (Thuật toán 08.16) và phép kiểm $5\cdot\frac25=2=s$ (Ví dụ 08.8) đã có. Nhận xét 08.21: hồ chứa chọn đều trên toàn lịch sử; ưu tiên gần đây cần cửa sổ (ghi chú Bài 09, Mục 6 DGIM và Mục 8 suy giảm mũ). Mục 3: 3 512 âm tiết; toàn chương 25 376.

**Lượt bản đánh giá, Mục 4 ↔ mạch 5.** Không thêm khối đánh số. Sau Định nghĩa 08.22: bảng 2×2 (thực tế × trả lời) và câu nghĩa của "dương", "âm", "giả". Ví dụ 08.13: hình `phi-tieu-8-bia.svg` (kết cục do học phần chọn: bit 1, 4, 4, 6, ba bit bằng 1) và câu đọc hình; kỳ vọng $8(1-(7/8)^4)=3{,}31$ giữ ở "Kiểm tra lại". Phản ví dụ điều kiện 1 của Định lý 08.25: mảng 10100101010 thành 10100100000, 159 đọc bit 7, 0 thành âm giả. Alt và đoạn đọc `fpr-curve.svg` theo nhãn hai vùng. Sau "Ý nghĩa:" của Định lý 08.28: mảng 11 bit $k^*=(11/3)\ln2\approx2{,}54$, 5/11 bit bằng 1. Ví dụ 08.16: $0{,}0216$ là xác suất cho một địa chỉ ngoài $S$ cố định, không phải tỷ lệ thư rác hay xác suất một địa chỉ đã qua bộ lọc thuộc $S$. Nhận xét 08.31: đổi $k$ phải xây lại mảng. Mục 4: 4 807 âm tiết; toàn chương 25 682.

**Lượt bản đánh giá, Mục 5, tình huống, bài tập ↔ mạch 6.** Không thêm khối đánh số. Mục 5.1 mở bằng câu phân biệt bảo đảm tất định (Mệnh đề 08.10(a), Định lý 08.25) và bảo đảm xác suất ($a/b$, $s/r$, $p(k)$). Mục 5.2: "tỷ số hai số đếm kỳ vọng là $1/29$"; câu "khóa nhiều bộ hơn $s$: không cấu trúc nào vừa giữ trọn khóa vừa giữ cỡ ≤ $s$", dẫn Bài tập 08.14. Nhận xét 08.31: định cỡ ngược $n/m=-\ln p/(\ln2)^2$; $p=0{,}01$: $9{,}59$ bit/khóa, $k^*=6{,}64$, $p(7)=0{,}01004$; 10 bit/khóa với $k=7$: $0{,}0082$ (tính lại 0,0081937). Bài tập 08.7: thêm bộ thứ 999, $s/r$ không phụ thuộc vị trí. Mục 5: 1 341 âm tiết; toàn chương 25 888.

**Lượt bản đánh giá, Bài tập củng cố ↔ mạch 7.** Không thêm khối đánh số. Bài tập 08.10 (X02B): thêm "không suy ra càng nhiều hàm băm càng tốt; $k>k^*$ thì $p$ tăng". Bài tập 08.11 (X03, X03B): hình `chia-mang-bit.svg` và câu đọc hình trong gợi ý; lời giải nêu $h_i(y)$ đều trong mảng con thứ $i$, $k$ phép kiểm độc lập nên tích chính xác; mảng chung chính xác là $\mathbb E[(X/n)^k]$, $q^k$ là cận dưới. Bài tập 08.12 (X04B–X04C): đạo hàm theo quy tắc tích, bước thay $z=-\ln\theta$, điểm dừng $\theta=1/2$ chưa đủ cho cực tiểu toàn cục. Bài tập 08.13 (X01B): đơn vị trước rồi khóa; phản ví dụ mã sinh viên 123 ở hai trường (ví dụ của học phần). Bài tập củng cố: 2 066 âm tiết; toàn chương 26 182.

**Lượt trang bài toán đầu mạch (2026-10-29).** Không thêm khối đánh số. Sáu hình bài toán của deck vào ghi chú, mỗi hình kèm đoạn đọc hình nêu nguồn số liệu và dữ kiện do học phần dựng; alt theo `desc` của SVG. Mục 1, sau đoạn mở: `bai-toan-cam-bien.svg` (dòng $1,5,2,7,4,0,3,5$ của MMDS Hình 4.1, tr.132; 3,5 TB mỗi ngày, §4.1.2, tr.133). Mục 2, sau đoạn mở: `bai-toan-ty-le-lap.svg` (dòng năm bộ do học phần dựng, tỷ lệ lặp của An $1/2$; tỉ lệ 10 : 1 theo §4.1.2, tr.133 và §4.2.1, tr.136). Mục 3.1, sau Ví dụ 08.8: `bai-toan-mau-co-dinh.svg` (bảy phần tử theo trang chiếu MMDS Streams 1, tr.18; $2/5$ và $2/7$; đơn vị là vị trí). Mục 4.1, trước đoạn trực quan: `bai-toan-loc-thu.svg` (20 GB so với 1 GB $=8\cdot10^9$ bit, §4.3.1, tr.139). Mục 5, sau đoạn mở: `hai-dong-ba-cau-hoi.svg` (hai dòng, ba câu hỏi; bảng Mục 5.1 và câu trả lời Mục 5.2 ghép câu hỏi với cấu trúc). Bài tập 08.13, trong đề: `grades-hai-truong.svg` (CS101 từ đề MMDS, U1/U2 là tên đặt chỗ, mã 123 do học phần đặt). Kiểm lại: 17 mã chủ đề, bộ đếm liên tục, dẫn chiếu khớp; 20 hình tải được ở khổ rộng và hẹp; toàn chương 27 265 âm tiết.

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

Ngoại lệ số dòng P03 (ghi 2026-10-28 theo kiểm định cuối): trang Nội dung có 8 dòng (danh sách 7 mạch bắt buộc theo `AGENTS.md` §"Mẫu RevealJS bắt buộc", hai cột `ex-grid2`, cộng dòng "Đọc trước:"), vượt trần 6 dòng. Không tách vì danh sách mạch phải nằm trọn một trang và khớp `#/N`. Âm tiết 39 → 40 sau khi thêm MMDS §4.5.5, tr.148–150 vào "Đọc trước:"; dòng dài nhất 15.

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

Dữ kiện do học phần dựng: dòng năm bộ (An, “đồ thị”), (Bình, “lọc”), (An, “băm”; từ 2026-10-29 là “đệ quy”), (An, “đồ thị”), (Chi, “lọc”), trong đó An có đúng ba bộ của K01; giá trị băm $h(\text{An})=0$, $h(\text{Bình})=7$, $h(\text{Chi})=4$ (trùng số rút ở K01B); giả định $10^8$ người dùng, 16 byte mỗi hàng; câu hỏi K06 và K08.

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

### Mạch 5. Lọc thành viên bằng Bloom filter

**Bản đồ mạch.**

| Loại | Chức năng | Vào | Ra | Đóng góp | Trang tiêu đề mạch |
|---|---|---|---|---|---|
| thuật toán và chi phí | Nêu giới hạn tra $S$ trực tiếp, ý tưởng mảng bit, chạy tay 11 bit (thêm và kiểm tra, có một dương giả), đặc tả và định nghĩa dương giả/âm giả, giả mã xây và kiểm tra, chứng minh không có âm giả, xác suất một bit bằng 1 và xác suất dương giả, ảnh hưởng của $k$, $k^*$, ví dụ tám bit mỗi khóa, chi phí | Mạch 4: hai phép lấy mẫu trả lời câu hỏi về phân phối; tình huống lọc thư của trang Vấn đề trung tâm | Bloom filter với bảo đảm không âm giả, $p_{FP}\approx p(k)=(1-e^{-km/n})^k$, $k^*=(n/m)\ln2$, định cỡ cho $10^9$ địa chỉ trong $8\cdot10^9$ bit; chi phí $km$ / $k$ / $n$ bit | Chu trình cụm thuật toán đủ bước: giới hạn có số (B00) → ý tưởng so với mạch 3 và nhận xét cấu trúc (B02) → chạy tay (B05, B05B) → đặc tả và định nghĩa ngay sau ví dụ dương giả (B01) → giả mã (B03, B04) → tính đúng (B06) → phân tích xác suất (B07, B08) → ảnh hưởng của $k$ và tối ưu (B09–B11) → chi phí và câu hỏi (B12) | BT (`id="mach-5"`) |

Thứ tự trang: BT → B00 → B02 → B05 → B05B → B01 → B03 → B04 → B06 → B07 → B08 → B09 → B10 → B11 → B12. B05B là ID mới. Đầu vào/Đầu ra đặt ở B01, ngay trước hai trang giả mã. Chứng minh đầy đủ của $k^*$ (kể cả bước xét dấu) để ở lời giải bài tập và ghi chú bài giảng; B10 chỉ phát biểu và nêu hướng chứng minh, để không giải trước Bài tập 4.3.3. B09 không dùng Bài tập 4.3.2 (phần bài tập giao bài đó).

**Câu hỏi trước khi sửa.**

| Trang cũ | Trang muốn nói | Phục vụ chủ đề mạch? | Vấn đề còn lại | Quyết định |
|---|---|---|---|---|
| BT | Điểm vào mạch 5 | có | Lời dẫn "hữu hạn", "dương giả" chưa định nghĩa, cấu trúc "đổi A lấy B"; cụm khóa "Không âm giả" | sửa |
| B00 | Tình huống $10^9$ địa chỉ, 1 GB | có | `h1` cũ; tiêu đề mở bằng tên thuật toán; thiếu giới hạn có số; dòng 33 âm tiết | sửa |
| B02 | Bloom filter đứng trước tra cứu chính xác | có | Chỉ có hình (hình lỗi tô đen nhánh loại); tiêu đề ẩn dụ; thiếu ý tưởng so với cái đã biết và nhận xét cấu trúc | sửa, sửa hình |
| B05 | Ví dụ 11 bit | có | Định nghĩa $h_1,h_2$ dồn một dòng 35 âm tiết; không có bước tính tay; không có dương giả; tiêu đề là câu | tách: B05 thêm khóa, B05B kiểm tra |
| B01 | Đặc tả | có | Chưa có Đầu vào/Đầu ra; chưa định nghĩa dương giả, âm giả | sửa |
| B03 | Giả mã xây | có | KaTeX trong tiêu đề; câu "va chạm" dùng dữ kiện không hiện | sửa |
| B04 | Giả mã kiểm tra | có | Tiêu đề là câu; ghi chú ngắn | sửa |
| B06 | Không âm giả | có | Bốn điều kiện chồng nhau, điều kiện ghi đồng thời ngoài trình độ; chứng minh chỉ ở ghi chú | sửa |
| B07 | Xác suất bit bằng 0 | có | Tiêu đề "Mật độ bit hữu hạn" khó hiểu; thiếu trực quan phi tiêu và số | sửa |
| B08 | Xác suất dương giả | có | Dẫn chiếu "trang trước"; đoạn 52 âm tiết; "iid" | sửa |
| B09 | Tăng $k$ giảm rồi tăng | có | Câu hỏi là Bài tập 4.3.2, không có lời giải | sửa: câu hỏi riêng có lời giải |
| B10 | Dẫn xuất $k^*$ | có | Giải trọn Bài tập 4.3.3; $p(k)$ chưa định nghĩa | sửa: phát biểu, Ý nghĩa, hướng chứng minh |
| B11 | $k=6$ với $n/m=8$ | có | KaTeX trong tiêu đề; không nhắc $n$, $m$ của tình huống | sửa, sửa hình |
| B12 | Chi phí, giới hạn, câu hỏi | có | Tiêu đề tương phản; "FPR"; câu hỏi ngầm dùng $k=2$; "Đáp án" | sửa |

**Từng trang.**

| Trang | Mục đích | Hành động của sinh viên | Đối tượng trung tâm | Dữ kiện, ký hiệu kế thừa | Sản phẩm học tập và bằng chứng | Quyết định và lý do | Âm tiết (dòng, max dòng) trước → sau | Phút |
|---|---|---|---|---|---|---|---|---:|
| BT | Điểm vào mạch 5 | Nhận nhiệm vụ | Lời dẫn "Muốn loại sớm khóa ngoài tập bằng mảng bit cỡ cố định, phải chấp nhận một phần nhận nhầm." | Đầu ra mạch 4; tình huống lọc thư | — | sửa: không "hữu hạn", không thuật ngữ chưa định nghĩa trên mặt trang; ghi chú nêu thuật ngữ tiếng Anh | 36 (2, 22) → 39 (2, 20); ghi chú 92 → 90 | 0,5 |
| B00 | Giới hạn cách trực tiếp | Tính cỡ $S$ so với bộ nhớ | $10^9$ địa chỉ × 20 byte ≥ 20 GB; 1 GB = $8\cdot10^9$ bit | Trang Vấn đề trung tâm | Nêu được vì sao không lưu $S$ | sửa: tiêu đề "Lọc theo danh sách cho phép"; MMDS §4.3.1 tr.139 | 40 (1, 33) → 38 (4, 12); ghi chú 59 → 79 | 2,5 |
| B02 | Ý tưởng | So với lấy mẫu theo khóa; đọc nhận xét bit 0 | "Tương tự … Khác …"; Nhận xét bit 0 ⇒ $y\notin S$; hình luồng lọc | Hàm băm thay bảng (mạch 3) | Phát biểu nhận xét cấu trúc | sửa; hình `bloom-pipeline.svg` sửa lỗi tô đen nhánh loại, nhánh loại nét đứt, chữ 26 | 0 (0, 0) → 45 (4, 13); ghi chú 39 → 95 | 2,5 |
| B05 | Chạy tay thêm khóa | Tính $h_1,h_2$ của 159; đọc trạng thái mảng | $h_1,h_2$ của Ullman; bảng trạng thái $00000000000\to\ldots\to10100101010$ | — | Mảng cuối; bằng chứng: B05B dùng mảng này | sửa và tách: hình mới `bloom-11bit-them.svg` (trạng thái sau từng khóa, bit vừa đặt khung đậm) | 35 (1, 35) → 33 (4, 14); ghi chú 108 → 77 | 3 |
| B05B | Chạy tay kiểm tra | Kiểm 118 và 29 | Mảng $10100101010$ (hình nhỏ); 118 → (3, 5) loại; 29 → (7, 2) có thể thuộc | Mảng cuối của B05 hiện lại bằng hình | Một dương giả cụ thể | thêm (ID mới); khóa 29 do học phần chọn | — → 21 (3, 13); ghi chú — → 78 | 3 |
| B01 | Đặc tả và định nghĩa | Đọc Đầu vào/Đầu ra; định nghĩa dương giả, âm giả | $S$, $m$, $n$, $B$, $h_i$, $y$; dương giả, âm giả | Ví dụ 11 bit nêu lại bằng số ($n=11$, $k=2$, $m=3$, khóa 29) | Gọi đúng tên hai loại lỗi | sửa: định nghĩa ngay sau ví dụ dương giả | 37 (2, 24) → 51 (5, 14); ghi chú 52 → 102 | 2,5 |
| B03 | Giả mã xây | Đọc giả mã | `XÂY-BLOOM(S; n, h₁,…,hₖ)`; khóa $v$ | B01 | Chi phí $km$ | sửa: tiêu đề "Thuật toán: xây Bloom filter"; dòng đọc giả mã; khóa đặt tên $v$ để không trùng $x_i$ | 28 (1, 13) → 27 (2, 18); ghi chú 39 → 62 | 2,5 |
| B04 | Giả mã kiểm tra | Đọc giả mã; nêu phép quyết định | `KIỂM-TRA-BLOOM(y; B, h₁,…,hₖ)` | B01 | Chi phí xấu nhất $k$ | sửa: tiêu đề "Thuật toán: kiểm tra thành viên" | 26 (1, 10) → 24 (2, 14); ghi chú 26 → 53 | 2,5 |
| B06 | Tính đúng | Đọc giả thiết, mệnh đề, chứng minh | Không có âm giả; khóa 29 làm phản ví dụ cho chiều ngược | B03 (bit chỉ đổi 0 → 1) | Chứng minh được mệnh đề | sửa: hai giả thiết thay bốn điều kiện chồng nhau; chứng minh trên mặt trang | 46 (6, 11) → 53 (4, 19); ghi chú 35 → 93 | 3 |
| B07 | Xác suất một bit bằng 1 | Tính $q$ với $k=1$ | Mô hình phi tiêu; $(1-1/n)^{km}\approx e^{-km/n}$; $q$; $0{,}1175$ | $(1-1/n)^n\approx e^{-1}$ (P04) | Tính được $q$ | sửa: tiêu đề mới; trực quan phi tiêu; ví dụ số. Không thêm hình phi tiêu (đủ chữ và công thức; số nhỏ $(7/8)^4\approx0{,}586$ để trong ghi chú) | 25 (2, 18) → 35 (5, 16); ghi chú 40 → 98 | 3 |
| B08 | Xác suất dương giả | Phân biệt hai xấp xỉ; tính $p(1)$, $p(2)$ | $p_{FP}\approx q^k\approx p(k)$ | $q$ (nêu lại trong công thức) | Tính được $p(k)$ | sửa: bỏ "trang trước", "iid"; tách dòng; ghi chú nêu $p_{FP}\ge q^k$ và số $0{,}0493$ in trong sách | 52 (1, 52) → 29 (5, 15); ghi chú 64 → 92 | 3,5 |
| B09 | Ảnh hưởng của $k$ | Giải thích hai lực; trả lời giới hạn $k\to\infty$ | Hai thẻ; $p(1)$, $p(6)$, $p(10)$ | $p(k)$ | Lời giải: $p(k)\to1$ vì $q\to1$ | sửa: câu hỏi riêng có lời giải; không dùng Bài tập 4.3.2 | 46 (2, 12) → 26 (5, 12); ghi chú 47 → 76 | 2,5 |
| B10 | Số hàm băm tối ưu | Đọc mệnh đề, ý nghĩa, quy tắc số nguyên | $k^*=(n/m)\ln2$; tại $k^*$ một nửa số bit bằng 1; $p(k^*)=2^{-k^*}$ | $p(k)$ | Áp được quy tắc số nguyên | sửa: không giải trọn Bài tập 4.3.3 trên mặt trang; ghi chú nêu đạo hàm và yêu cầu bước xét dấu | 19 (2, 13) → 39 (4, 15); ghi chú 73 → 93 | 3,5 |
| B11 | Ví dụ định cỡ | Đọc đường cong; so $p(5)$, $p(6)$ | $n=8\cdot10^9$, $m=10^9$; hình `fpr-curve.svg` có vạch $k^*$ | Tình huống lọc thư nêu lại bằng số | Chọn được $k=6$ | sửa: tiêu đề "Ví dụ: tám bit mỗi khóa"; hình thêm vạch $k^*\approx5{,}545$, chữ 26 | 0 (0, 0) → 9 (3, 6); ghi chú 64 → 73 | 2,5 |
| B12 | Chi phí và câu hỏi | Đếm chi phí; giải câu hỏi định cỡ lại | Bảng xây/kiểm tra/bộ nhớ; Lưu ý; câu hỏi $2\cdot10^9$ địa chỉ, $k=6$ | B03, B04, B10 | Lời giải: $p(6)\approx0{,}2198$; $k=3$ tốt hơn | sửa: tiêu đề "Chi phí: Bloom filter"; bỏ "FPR", "Đáp án"; câu hỏi có $k$ rõ | 48 (2, 19) → 61 (8, 17); ghi chú 62 → 74 | 3 |

Trang chi phí B12 có 61 âm tiết, 8 dòng: trong trần 80 âm tiết và 8 dòng của bảng chi phí.

Tổng mạch 5: 40,5 phút (trước 44). Tổng phần giảng tạm: 113 phút với mạch 6 cũ (5 phút); mạch 6 cần khoảng 12 phút để tổng về 120.

Số đã tự tính: $25=11001_2\to(5,2)$; $159=10011111_2\to(7,0)$; $585=1001001001_2\to(9,7)$ (bit chẵn $10010_2=18\equiv7$); $118=1110110_2\to(3,5)$ (bit lẻ $1110_2=14\equiv3$); $29=11101_2\to(7,2)$; mảng $00100100000\to10100101000\to10100101010$; $(7/8)^4=0{,}5862$; $1-e^{-1/8}=0{,}117503$ (chính xác $0{,}1175031$); $(1-e^{-1/4})^2=0{,}048929$; $p(5)=0{,}021679$; $p(6)=0{,}021577$; $p(10)=0{,}034191$; $k^*=8\ln2=5{,}5452$; $2^{-5{,}545}=0{,}021416$; với $n/m=4$: $p(6)=0{,}21983$, $k^*=2{,}7726$, $p(2)=0{,}15482$, $p(3)=0{,}14689$, $p(4)=0{,}15966$.

Dữ kiện do học phần dựng: khóa 29; câu hỏi B09 và B12.

Hình: `bloom-11bit-them.svg` (mới, B05), `bloom-11bit-mini.svg` (mới, B05B), `bloom-pipeline.svg` (sửa lỗi tô đen nhánh loại, nét đứt, chữ 26), `fpr-curve.svg` (thêm vạch $k^*$, chữ 26). `bloom-11bit.svg` giữ nguyên vì ghi chú bài giảng còn dùng; không vẽ `bloom-darts.svg`.

**Sửa sau lượt rà lại mạch 5 (2026-10-28).** Các số đo dưới đây thay cột âm tiết của bảng trên.

| Trang | Thay đổi | Âm tiết (dòng, max dòng); ghi chú |
|---|---|---|
| B02 | Hình `bloom-pipeline.svg`: khung "tra cứu chính xác" nới rộng để chữ không chạm viền | 45 (4, 13); ghi chú 95 |
| B05B | Chú thích hình khớp nét vẽ ("khung đậm: bit 7, 2 của khóa 29; nét đứt: bit 3 của khóa 118"); cột Bit của 118 ghi "0 (dừng)", khớp phép dừng sớm ở B04 | 22 (3, 13); ghi chú 84 |
| B01 | Đầu ra nêu cả mảng $B$ sau khi xây | 55 (5, 18); ghi chú 102 |
| B07 | Chỉ số bit $c$ (khớp Bổ đề 08.26 của ghi chú bài giảng), "xét bit $c$" ở dòng mô hình | 38 (5, 16); ghi chú 98 |
| B08 | Xấp xỉ thứ nhất: $p_{FP}=\mathbb E[(X/n)^k]\ge q^k$ (Jensen); xấp xỉ thứ hai: $p(k)\le q^k$. Bỏ lý do sai "các vị trí có thể trùng". Ghi chú khớp Mệnh đề 08.27 | 25 (5, 8); ghi chú 123 |
| B09 | Hai thẻ "Tăng $k$ giúp" / "Tăng $k$ hại", không dựa vào màu viền | 28 (5, 12); ghi chú 76 |
| B10 | Dòng "Chứng minh." nêu điểm dừng duy nhất và xét dấu hai phía; ghi chú dùng $z=k\rho$, $\theta=e^{-z}$ (khớp Định lý 08.28) | 42 (4, 18); ghi chú 104 |
| B11 | Câu chốt "Chọn $k=6$; giá trị liên tục nhỏ nhất là $2^{-5{,}545}\approx0{,}0214$"; ghi chú: slide CS246 tr.32–33; số 0,0235 của slide Streams 2 tr.14 đến từ công thức viết sai $(1-e^{-1/6})^2$ | 11 (3, 8); ghi chú 79 |
| B12 | Dòng "Lưu ý" chuyển vào ghi chú (giới hạn của Bloom filter) | 45 (7, 15); ghi chú 96 |

### Mạch 6. Tổng kết và chuyển tiếp

**Bản đồ mạch.**

| Loại | Chức năng | Vào | Ra | Đóng góp | Trang tiêu đề mạch |
|---|---|---|---|---|---|
| tổng kết | Đối chiếu kết quả, giả thiết, bảo đảm và chi phí của ba cấu trúc; trả lời vấn đề trung tâm bằng số; tự kiểm tra ba mục tiêu; nguồn và nối sang Bài 09 | Mạch 2–5: mô hình dòng; mẫu theo khóa ($a/b$, nhất quán); hồ chứa ($s/r$); Bloom filter (không âm giả, $p(k)$, $k^*$) | Lựa chọn có điều kiện theo câu hỏi; bốn câu tự kiểm tra có lời giải; tài liệu đọc, liên kết ghi chú bài giảng, liên kết Bài 09 | Không có khái niệm mới | CT (`id="mach-6"`) |

Thứ tự trang: CT → C00 → C03 → C01 → C04 → C05 → C02. C03, C04, C05 là ID mới. Tên mạch giữ "Tổng kết và chuyển tiếp" (khớp P03).

**Câu hỏi trước khi sửa.**

| Trang cũ | Trang muốn nói | Phục vụ chủ đề mạch? | Vấn đề còn lại | Quyết định |
|---|---|---|---|---|
| CT | Điểm vào mạch 6 | có | Lời dẫn 22 âm tiết; cụm khóa "Nguồn và phạm vi" | sửa |
| C00 | So sánh ba cấu trúc theo đơn vị, bảo đảm, sai số | một phần | `h1` cũ; tiêu đề là câu; không theo mẫu `Kết quả \| Giả thiết không được bỏ \| Công thức hoặc thuật toán`; "dưới giả thiết đã nêu" | sửa: bảng theo mẫu, sáu hàng cho mạch 2–5 |
| (thiếu) | Bảng thuật toán bốn cột | — | Bắt buộc với bài nhiều thuật toán | thêm C03 |
| C01 | Áp lại ba cấu trúc vào dòng truy vấn | một phần | Không có số; ghép Bloom filter vào dòng truy vấn; tiêu đề kể tiến trình | sửa: câu trả lời có điều kiện, có số |
| (thiếu) | Câu hỏi tự kiểm tra | — | Trang bắt buộc | thêm C04, C05 |
| C02 | Nguồn và phạm vi | có | Tiêu đề khác mẫu; thiếu tác giả, năm, trang; thiếu liên kết ghi chú và dòng nối Bài 09; ghi chú biên soạn | sửa |

**Từng trang.**

| Trang | Mục đích | Hành động của sinh viên | Đối tượng trung tâm | Dữ kiện, ký hiệu kế thừa | Sản phẩm học tập và bằng chứng | Quyết định và lý do | Âm tiết (dòng, max dòng) trước → sau | Phút |
|---|---|---|---|---|---|---|---|---:|
| CT | Điểm vào mạch 6 | Nhận nhiệm vụ | Lời dẫn "Muốn chọn cấu trúc cho từng câu hỏi trên dòng, phải đối chiếu giả thiết, bảo đảm và chi phí." | Đầu ra mạch 5 | — | sửa | 33 (2, 22) → 37 (2, 20); ghi chú 90 → 83 | 0,5 |
| C00 | Kết quả và giả thiết | Nêu giả thiết không được bỏ của từng kết quả | Bảng sáu hàng (thuật toán dòng; mẫu theo khóa; xác suất có mặt; không âm giả; xác suất dương giả; $k^*$) | Mạch 2–5 | Nêu được hệ quả khi bỏ từng giả thiết (ghi chú) | sửa; bảng tổng kết, trần 80 | 53 (3, 14) → 67 (6, 14); ghi chú 29 → 108 | 2,5 |
| C03 | Thuật toán, bảo đảm, chi phí | Đối chiếu bốn thuật toán | Bảng `Thuật toán \| Đầu vào \| Bảo đảm \| Chi phí` | Các trang chi phí K07, R08, B12 | Chọn thuật toán theo chi phí và bảo đảm | thêm; bảng tổng kết, trần 80 | — → 61 (4, 18); ghi chú — → 117 | 2,5 |
| C01 | Trả lời vấn đề trung tâm | Nối mỗi câu trả lời với kết quả đã chứng minh | Lưu $1/10$; $10^9$ địa chỉ, $8\cdot10^9$ bit, $k=6$, khoảng 2%; $1/29$; $s/r$ | Trang Vấn đề trung tâm (số liệu nhắc lại trên trang) | Câu trả lời có điều kiện; ghi chú nêu kết quả dùng cho từng câu | sửa; trang đối chiếu (trần 80) như P01 vì mỗi câu mang giả thiết và số | 55 (3, 20) → 63 (4, 19); ghi chú 36 → 106 | 2 |
| C04 | Tự kiểm tra, câu 1–2 | Trả lời, nêu kết quả đã dùng | Câu 1: giữ 5% người dùng và lý do không lấy từng bộ (mục tiêu 1); câu 2: hồ chứa $s=50$, $r=1\,000$ (mục tiêu 2) | Dữ kiện trên trang | Lời giải: $h(K)<5$, $\frac{d}{20u+39d}$; $0{,}05$ với giả thiết | thêm; câu hỏi do học phần dựng | — → 44 (3, 18); ghi chú — → 91 | 2 |
| C05 | Tự kiểm tra, câu 3–4 | Trả lời, nêu kết quả đã dùng | Câu 3: không âm giả và giả thiết; câu 4: gấp đôi $n$ (mục tiêu 3) | Dữ kiện trên trang | Lời giải: không, khi mảng chỉ đọc; $k^*$ gấp đôi, $p(k^*)$ bình phương | thêm; câu hỏi do học phần dựng | — → 34 (3, 18); ghi chú — → 99 | 1,5 |
| C02 | Nguồn và tài liệu đọc | Ghi nguồn; mở ghi chú; xem bài sau | MMDS 3e (2020) Chương 4 §§4.1–4.3 tr.131–142; slide MMDS Streams 1–2; CS246 (2026); Ullman (2017); mmds.org; liên kết ghi chú; liên kết Bài 09 | `sources/source.md` dòng 401, 423, 443 (Bài 9) | — | sửa; ghi chú nêu trang nào dùng nguồn nào, bỏ ghi chú biên soạn | 34 (4, 14) → 52 (6, 18); ghi chú 76 → 101 | 1 |

Ngoại lệ mật độ: C00 (67), C03 (61) là bảng tổng kết, trần 80; C01 (63) là trang đối chiếu như P01, trần 80, vì mỗi câu trả lời phải mang giả thiết và số của tình huống mở đầu. Trước: C00 53, C01 55; sau: 67, 63.

Kiểm liên kết: `material-viewer.html?doc=materials/lec-08/lecture-note.md&deck=lecture-08-dong-du-lieu-mo-hinh-lay-mau-va-loc.html` và `lecture-09-dong-du-lieu-dem-momen-va-cua-so.html` trả HTTP 200 trên máy chủ cục bộ. Deck Bài 09 chưa được duyệt theo chuẩn hiện hành và chưa có trên `index.html`.

Số đã tự tính: với tỷ lệ $p$, mẫu từng bộ cho $\frac{p^2d}{pu+2p(1-p)d+p^2d}=\frac{pd}{u+(2-p)d}$; $p=0{,}1$ cho $\frac{d}{10u+19d}$, $p=0{,}05$ cho $\frac{d}{20u+39d}$; $50/1\,000=0{,}05$; $n/m=16$: $k^*=16\ln2=11{,}09$, $2^{-11{,}09}=4{,}59\cdot10^{-4}=0{,}0214^2$.

**Thời lượng toàn bài (phần giảng).**

| Mạch | Phút |
|---|---:|
| 1. Mở đầu | 6,5 |
| 2. Mô hình tính toán trên dòng | 12 |
| 3. Lấy mẫu theo khóa | 24 |
| 4. Lấy mẫu hồ chứa | 25 |
| 5. Lọc thành viên bằng Bloom filter | 40,5 |
| 6. Tổng kết và chuyển tiếp (CT 0,5; C00 2,5; C03 2,5; C01 2; C04 2; C05 1,5; C02 1) | 12 |
| Tổng | 120 |

Phần bài tập (mạch 7) giữ 60 phút, duyệt ở lượt sau.

**Sửa sau lượt rà lại mạch 6 (2026-10-28).** Các số đo dưới đây thay cột âm tiết của bảng trên.

| Trang | Thay đổi | Âm tiết (dòng, max dòng); ghi chú |
|---|---|---|
| C00 | Hàng xác suất dương giả thêm "$y\notin S$ cố định"; hàng số hàm băm tối ưu ghi "$k$ thực; tối ưu cho dạng mũ $p(k)$" | 74 (6, 14); ghi chú 108; bảng tổng kết, trần 80 |
| C01 | "$1/29$" gắn với An; câu hồ chứa thêm $r\ge s$; tách câu Bloom filter: không âm giả khi mảng chỉ được đọc (không cần xác suất), khoảng 2% khi băm đều, độc lập; ghi chú thu hồi dòng mô hình dòng của trang vấn đề trung tâm | 76 (5, 20); ghi chú 143; trang đối chiếu, trần 80 |
| C04 | Câu 1 "$h$ nhận giá trị trong"; câu 2 hỏi giả thiết dùng ở bước quy nạp; lời giải nêu tính đều dùng ở hai nửa, tính độc lập dùng ở nửa phần tử cũ | 45 (3, 19); ghi chú 121 |
| C02 | Nguồn thêm MMDS §4.5.5, tr.148–150; ghi chú bỏ câu sai "sách không trình bày thuật toán này", thay bằng §4.5.5 tr.148–149 và hộp tr.150 | 53 (6, 18); ghi chú 122 |
| K01 | "tỷ lệ truy vấn tìm kiếm lặp" để tách nghĩa với truy vấn gửi bộ xử lý ở mạch 2 | 60 (6, 19); ghi chú 118 |
| R00, R01, R04, R05, R07, R08 (ghi chú) | Thêm nguồn MMDS §4.5.5, tr.148–149 bên cạnh slide Streams 1; R07 ghi phép tính sống sót là của cả sách tr.149 và slide tr.21 | R07 ghi chú 159 (chứng minh) |

Đối chiếu sách: MMDS 3e §4.5.5 "Dealing With Infinite Streams" (tr.148–149) trình bày chọn vị trí $n+1$ với xác suất $s/(n+1)$, bỏ đều một trong $s$ biến và chứng minh quy nạp; hộp "A General Stream-Sampling Problem" (tr.150) nối với lấy mẫu theo khóa. Bài tập §4.5.6 (4.5.1–4.5.6) đều về mômen, nên ghi chú R09 "sách MMDS không có bài tập hồ chứa" vẫn đúng. Thuật ngữ bộ dùng thống nhất "(người dùng, truy vấn, thời gian)" trên toàn deck; "thời điểm" chỉ còn trong ghi chú A00 với nghĩa "thời điểm định trước".

### Mạch 7. Bài tập vận dụng

**Bản đồ mạch.**

| Loại | Chức năng | Vào | Ra | Đóng góp | Trang tiêu đề mạch |
|---|---|---|---|---|---|
| bài tập | Vận dụng đặc tả mẫu theo khóa, công thức dương giả và số hàm băm tối ưu trên bốn bài MMDS | Mạch 3 (chọn khóa theo đơn vị thống kê), mạch 5 ($p(k)$, $k^*$), mạch 6 (bảng kết quả và giả thiết) | Lời giải bốn bài, tiêu chí đối chiếu trong ghi chú; lời giải mẫu Bài tập 4.3.3 trên trang | Không có khái niệm mới | XT (`id="mach-7"`) |

Thứ tự trang: XT → X01 → X02 → X03 → X04 → X04B. Bỏ X00 và X05 (điều phối lớp); danh sách bốn bài chuyển vào ghi chú XT, tiêu chí đối chiếu chuyển vào ghi chú từng bài. X04B là ID mới (lời giải mẫu, cùng tiêu đề với X04).

**Câu hỏi trước khi sửa.**

| Trang cũ | Trang muốn nói | Phục vụ chủ đề mạch? | Vấn đề còn lại | Quyết định |
|---|---|---|---|---|
| XT | Điểm vào phần bài tập | có | Lời dẫn 22 âm tiết có nhận xét biên soạn "với dữ kiện giữ nguyên" | sửa |
| X00 | Giới thiệu bốn bài, phiếu nộp | một phần | Chỉ dẫn biên soạn và điều phối lớp; trùng XT | bỏ |
| X01 | Ex.4.2.1 chọn khóa | có | Tiêu đề số bài; câu 36 âm tiết; không có "Câu hỏi:"; "Sản phẩm:"; ý (a)–(c) đánh số 1–3 | sửa |
| X02 | Ex.4.3.1 ba và bốn hàm băm | có | Tiêu đề số bài; hai thẻ chỉ chứa $k$; "Sản phẩm:"; ký hiệu $p_3$, $p_4$ | sửa |
| X03 | Ex.4.3.2 chia mảng bit | có | Tiêu đề số bài; dòng 23 âm tiết; giả thiết $k$ chia hết $n$ của học phần chưa ghi rõ; ghi chú thiếu chiều so sánh | sửa |
| X04 | Ex.4.3.3 số hàm băm tối ưu | có | Tiêu đề số bài; "Sản phẩm:"; lời giải chỉ ở ghi chú | sửa, thêm X04B |
| X05 | Phiếu nộp | không | Trang hành chính | bỏ |

**Đối chiếu đề với sách (MMDS 3e, bản văn bản chương 4).**
- Ex.4.2.1, tr.138: "Suppose we have a stream of tuples with the schema Grades(university, courseID, studentID, grade). Assume universities are unique, but a courseID is unique only within a university … and likewise, studentID's are unique only within a university … Suppose we want to answer certain queries approximately from a 1/20th sample of the data. For each of the queries below, indicate how you would construct the sample. That is, tell what the key attributes should be. (a) For each university, estimate the average number of students in a course. (b) Estimate the fraction of students who have a GPA of 3.5 or more. (c) Estimate the fraction of courses where at least half the students got "A."" Deck dịch đủ dữ kiện; bỏ ví dụ "CS101".
- Ex.4.3.1, tr.141: "For the situation of our running example (8 billion bits, 1 billion members of the set S), calculate the false-positive rate if we use three hash functions? What if we use four hash functions?" Deck giữ nguyên dữ kiện.
- Ex.4.3.2, tr.141: "Suppose we have n bits of memory available, and our set S has m members. Instead of using k hash functions, we could divide the n bits into k arrays, and hash once to each array. As a function of n, m, and k, what is the probability of a false positive? How does it compare with using k hash functions into a single array?" Quy ước "$k$ chia hết $n$; các hàm băm đều, độc lập" là của học phần, ghi trên trang bằng nhãn "Quy ước:" và trong ghi chú.
- Ex.4.3.3, tr.142: "As a function of n, the number of bits and m the number of members in the set S, what number of hash functions minimizes the false-positive rate?" Deck thêm "dùng dạng $p(k)$ với $k$ thực, rồi chọn $k$ nguyên", là cách hiểu chuẩn của câu hỏi theo công thức ở tr.141; không đổi nhiệm vụ.

**Từng trang.**

| Trang | Mục đích | Hành động của sinh viên | Đối tượng trung tâm | Dữ kiện kế thừa | Sản phẩm học tập và bằng chứng | Quyết định và lý do | Âm tiết (dòng, max dòng) trước → sau | Phút (đề, làm, chữa) |
|---|---|---|---|---|---|---|---|---:|
| XT | Điểm vào phần bài tập | Nhận bốn bài | Lời dẫn "Muốn chọn khóa lấy mẫu và định cỡ Bloom filter, phải áp dụng đặc tả và công thức dương giả." | Mạch 3, 5, 6 | — | sửa | 26 (2, 22) → 35 (2, 20); ghi chú 85 → 86 | 0,5 |
| X01 | Ex.4.2.1 | Chọn khóa cho (a)–(c) | Lược đồ Grades; mẫu $1/20$ | Quy tắc chọn khóa theo đơn vị (K06) | Ba khóa; tiêu chí trong ghi chú | sửa; đề bài thực hành, trần 80; danh sách a–c (lớp `stream-alpha`) | 78 (5, 36) → 70 (6, 18); ghi chú 59 → 154 | 14,5 (2; 8; 4,5) |
| X02 | Ex.4.3.1 | Tính $p(3)$, $p(4)$ | $n=8\cdot10^9$, $m=10^9$ | $p(k)$ (B08) | $0{,}0306$; $0{,}0240$ | sửa; ký hiệu $p(k)$ | 25 (4, 16) → 30 (3, 16); ghi chú 37 → 54 | 10 (1; 6; 3) |
| X03 | Ex.4.3.2 | Dẫn công thức mảng chia, so với mảng chung | $n$, $m$, $k$; quy ước $k\mid n$ | Mô hình phi tiêu (B07); Bernoulli | $[1-(1-k/n)^m]^k\ge q^k$; ví dụ số trong ghi chú | sửa; ghi chú nêu chiều so sánh | 49 (4, 23) → 51 (5, 16); ghi chú 85 → 154 | 15 (2; 8; 5) |
| X04 | Ex.4.3.3 | Tìm $k$ tối ưu, chứng minh cực tiểu, quy tắc số nguyên | $p(k)$ | B10 (phát biểu, không có chứng minh trên trang) | Lời giải ở X04B | sửa | 44 (6, 14) → 29 (3, 19); ghi chú 101 → 86 | 12 (2; 10; —) |
| X04B | Lời giải mẫu Ex.4.3.3 | Đối chiếu bài làm | Đổi biến $\rho$, $z$, $\theta$; $\lambda'=\phi(\theta)/(1-\theta)$; xét dấu; quy tắc số nguyên | Định lý 08.28, Hệ quả 08.29 của ghi chú bài giảng | Chứng minh đủ ý | thêm; 1 công thức hiển thị (hai dòng `aligned`) | — → 28 (5, 8); ghi chú — → 88 | 8 (chữa) |

Tổng phần bài tập: 60 phút.

Số đã tự tính: $p(3)=(1-e^{-3/8})^3=0{,}030579$; $p(4)=(1-e^{-1/2})^4=0{,}023969$; mảng chia với $n=64$, $m=8$, $k=4$: $[1-(1-4/64)^8]^4=0{,}026450$, $q^k=[1-(1-1/64)^{32}]^4=0{,}024556$, giá trị chính xác của mảng chung $\mathbb E[(X/n)^k]=0{,}025354$ (tính bằng phân phối số bit 1), dạng mũ $0{,}023969$; với $n=8\cdot10^9$, $m=10^9$, $k=4$: mảng chia $0{,}0239686508395$, $q^k$ $0{,}0239686508256$ (trùng chín chữ số có nghĩa); $\phi(1/2)=0$; $k^*=8\ln2=5{,}545$, $p(5)=0{,}021679>p(6)=0{,}021577$.

CSS: thêm `.reveal.course-deck.lecture-stream ol.stream-alpha { list-style-type: lower-alpha; }` (theme ghi đè `type="a"`).

### Lượt sửa cuối (2026-10-28, sau rà lại mạch 7 và kiểm định cuối)

| Trang | Thay đổi | Lý do | Âm tiết (dòng, max dòng) trước → sau; ghi chú |
|---|---|---|---|
| P03 | "Đọc trước:" thêm "; §4.5.5, tr.148–150" | Mạch 4 dùng MMDS §4.5.5 | 39 (8, 14) → 40 (8, 15); ngoại lệ số dòng ghi ở mạch 1 |
| K01B | Alt của hình đổi sang năm bộ, khớp hình và ghi chú bài giảng | Kiểm định cuối F8 | không đổi mặt trang (58) |
| B05 | Ghi chú: "(CS246, 2017, tr.5–8)" thay ngày cụ thể | Ngày chỉ có trong siêu dữ liệu PDF | ghi chú 77 → 77 |
| B06 | Ghi chú: nêu Định lý 08.25 của ghi chú bài giảng có thêm hai điều kiện (hàm băm tất định; truy vấn sau khi mọi phép ghi đã xong), tự thỏa trong mô hình của bài; mặt trang giữ hai giả thiết và nhãn "Mệnh đề." | Kiểm định cuối F3 | 53 (4, 19) không đổi; ghi chú → 141 |
| X01 | Dữ kiện (lược đồ, tính duy nhất của mã) lên trước "Câu hỏi:"; ghi chú (a) "theo kỳ vọng, khoảng $1/20$ số học phần" | Rà lại mạch 7 | 70 (6, 18) → 68 (6, 20); ghi chú 154 → 157 |
| X02 | Dữ kiện lên trước "Câu hỏi:" | Cùng mẫu với X01 | 30 (3, 16) → 30 (3, 18) |
| X03 | Dữ kiện lên trước "Câu hỏi:" | Cùng mẫu với X01 | 51 (5, 16) → 51 (5, 18) |
| X04 | Ghi chú bỏ câu điều phối lớp, còn "Lời giải mẫu ở trang kế tiếp, cùng tiêu đề." | Rà lại mạch 7 | 29 không đổi; ghi chú 86 → 78 |
| X04B | Ghi phép thay $z=-\ln\theta$ và tính chất "lõm chặt" trên mặt trang | Rà lại mạch 7 | 28 (5, 8) → 33 (5, 11); ghi chú 88 |

Kiểm lại số lớn của Bài tập 4.3.2 ($n=8\cdot10^9$, $m=10^9$, $k=4$) bằng số thập phân 40 chữ số: mảng chia $0{,}0239686508395$, $q^k$ $0{,}0239686508256$, trùng chín chữ số có nghĩa như ghi chú X03 nói.

## Lượt biên tập theo bản đánh giá giảng dạy (2026-10-28)

Căn cứ: `planning/lec-08/danh-gia-giang-day.md` (58 slide; số slide ánh xạ sang ID theo thứ tự deck trước lượt này) và kế hoạch đã được điều phối viên duyệt (quyết định chung, bảng 58 mục, kế hoạch theo mạch, danh sách hình mới). Quyết định chung áp dụng ở mọi mạch: không `fragment`, không hoạt cảnh; trang tiêu đề mạch không hình, không câu hỏi; không đưa nội dung ngoài nguồn lên mặt trang (Flink/Spark, Welford); giữ ví dụ xuyên suốt và bảng tổng kết bắt buộc. Mạch 1 giữ nguyên (đã duyệt).

### Mạch 2. Mô hình tính toán trên dòng

Thứ tự trang: AT → A05 → A00 → **A07** → A02 → A06. A07 là ID mới (định nghĩa trạng thái, phép cập nhật, phép trả lời; vết cửa sổ 4 số). Hình mới `img/lec-08/trang-thai-cap-nhat.svg` (viewBox 1180×324, chữ 28, ô số 32; hiển thị ở `stream-short`, tỷ lệ 0,833, chữ ≈ 23 px trong khung 1280×720; chỉ số dưới $x_5$, $x_6$ ≈ 18 px).

| Trang | Đề xuất của bản đánh giá | Quyết định | Thay đổi | Âm tiết (dòng, max dòng) trước → sau; ghi chú | Phút |
|---|---|---|---|---|---:|
| AT | Sơ đồ $x_r\to$ cập nhật $\to$ trạng thái $\to$ trả lời, phân biệt dòng vào/trạng thái/kết quả | chấp nhận nội dung, không trên AT (trang tiêu đề mạch không hình) | Cụm khóa: «Trạng thái theo truy vấn · Mô hình dòng · Phép cập nhật · Chi phí mỗi phần tử · Phương sai» (cụm cuối rút gọn để dòng ≤ 20); ghi chú nêu phép cập nhật và phép trả lời | 37 (2, 19) → 37 (2, 19); ghi chú 94 → 100 (bỏ vế "truy vấn quyết định trạng thái cần giữ", đã có ở A05) | 0,5 |
| A05 | Vết từng phần tử, ba hàng song song; thêm $27/8$ | giữ mặt trang (59/60, 6 dòng; $27/8$ đã có; vết từng phần tử ở Ví dụ 08.2 của ghi chú bài giảng) | Ghi chú: câu cơ chế cửa sổ rút còn lý do (số rời cửa sổ phải được trừ khỏi tổng); cơ chế chạy tay chuyển sang A07 | 59 (6, 17) → 59 (6, 17); ghi chú 150 → 142 | 3 → 2,5 |
| A00 | Vẽ lại bốn thành phần; phân biệt mô hình lý thuyết với Flink/Spark | giữ; bác bỏ Flink/Spark (ngoài nguồn) | Ghi chú: bỏ "chẳng hạn mỗi khi có phần tử mới" và vế "$x_1=1$ sát bộ xử lý"; gộp câu bộ nhớ làm việc; thêm câu nối «Phép cập nhật đặc tả cách trạng thái đổi khi phần tử mới đến.» | 57 (4, 18) → 57 (4, 18); ghi chú 150 → 143 | 3 |
| A07 | (từ S6) phân biệt dòng vào, trạng thái, kết quả; vòng trạng thái quay lại; (từ S9) bộ đệm vòng 4 ô | thêm | Định nghĩa trạng thái và phép trả lời; phép cập nhật; ví dụ cửa sổ 4 số trên $1,5,2,7,4$ khi $x_5=4$ đến; hình; dòng kết «Cỡ trạng thái không tăng theo $r$.» Ghi chú: thành phần trạng thái, bất biến (tổng bằng tổng bộ đệm; ô ghi tiếp chứa số cũ nhất), vết $15-1+4=18$, trả lời $4{,}5$, nối bốn phép sang bảng chi phí. Không dùng ký hiệu $\sigma$ cho trạng thái | — → 50 (4, 20); ghi chú — → 151 | 2 |
| A02 | Tổng $O(r)$ khác cập nhật $O(1)$; bộ đếm $O(\log r)$ bit; bộ đệm vòng 4 ô dưới bảng | một phần: dòng tổng công việc và $\lceil\log_2(r+1)\rceil$ bit đã có; bộ đệm vòng chạy tay ở A07, không thêm hình vào A02 | Ghi chú: bỏ câu mở "Mỗi hàng đếm chi phí…"; câu bốn phép thêm «như vết cửa sổ 4 số khi $x_5=4$ đến» | 58 (5, 17) → 58 (5, 17); ghi chú 146 → 142 | 3 → 2,5 |
| A06 | Chia hai bước, bảng cập nhật $r,S_1,S_2$; mất chữ số; Welford | giữ mặt trang (trang "Câu hỏi" có lời giải trong ghi chú); Welford không lên mặt trang (quyết định điều phối viên; chỉ ghi chú bài giảng, do tác tử ghi chú) | không đổi | 28 (5, 15); ghi chú 141 | 2,5 |

Tổng mạch 2: 13 phút (cũ 12). Phần giảng tạm là 120,5 phút theo số ghi (thực 120 vì mạch 5 cộng cột là 40, không phải 40,5); cân lại đúng 120 khi biên tập mạch 5 theo kế hoạch.

Chu trình học của A07: nhu cầu (A05: trạng thái chọn theo truy vấn) → định nghĩa (A07) → ví dụ chạy tay (hình) → bất biến và lý do cập nhật đúng (ghi chú) → chi phí (A02) → kiểm tra (A06).

Ghi chú bài giảng: §1.4 cần vết cửa sổ 4 số và hình `trang-thai-cap-nhat.svg` (tác tử ghi chú; tạm lệch cho tới khi ghi chú cập nhật).

Sửa nhẹ sau rà lại mạch 2 (2026-10-28): nhãn hình "số đếm 4" đổi thành "số trong bộ đệm 4" (sau 5 số vẫn là 4, tức $\min(r,4)$; khung trạng thái rộng 400, khối cập nhật 260; chữ hiển thị ≈ 23 px); ghi chú A07 nêu số trong bộ đệm bằng $\min(r,4)$ và nguồn: dãy $1,5,2,7,4$ là năm số đầu của dòng MMDS Hình 4.1, cỡ cửa sổ 4 do học phần chọn. Thứ tự định nghĩa → ví dụ → hình trong A07 giữ nguyên: A05 ngay trước đã cho trực quan có số, và định nghĩa viết bằng lời.

### Mạch 3. Lấy mẫu theo khóa

Thứ tự trang không đổi: KT → K01 → K09 → K01B → K02 → K04 → K05 → K06 → K07 → K08. Hình mới `img/lec-08/cay-hai-bo-do-thi.svg` thay bảng ba hàng ở K01 (viewBox 1180×426, chữ 28, nhãn cạnh 26; hiển thị cao 360 trong khung 1280×720, tỷ lệ 0,845, chữ ≈ 24 px, nhãn cạnh ≈ 22 px). Lá "đủ hai bản" khung kép, lá "vắng mặt" khung nét đứt, nên không dựa vào màu.

| Trang | Đề xuất của bản đánh giá | Quyết định | Thay đổi | Âm tiết (dòng, max dòng) trước → sau; ghi chú | Phút |
|---|---|---|---|---|---:|
| KT | Lấy mẫu phần tử và lấy mẫu cụm; hình hai cấp người dùng → truy vấn | bác bỏ hình (trang tiêu đề mạch); một phần ở ghi chú | Ghi chú thêm «Mỗi người dùng cùng mọi bộ của người đó tạo thành một cụm; lấy mẫu theo khóa chọn hoặc bỏ cả cụm.»; bỏ vế nhắc bài tập phương sai để giữ ≤ 100 | 39 (2, 20) không đổi; ghi chú 94 → 99 | 0,5 |
| K01 | Cây xác suất bốn trường hợp, giải thích hệ số 2, trực quan $1/19$ | chấp nhận | Bảng → hình cây; câu chốt «…xác suất có đủ hai bản là $(1/100)/(19/100)=1/19$.» Dòng «Bộ “băm” được giữ với xác suất $1/10$» của kế hoạch đặt vào ghi chú (dòng "Muốn …" đã nói mỗi bộ giữ với $1/10$; chỗ dành cho hình). Ghi chú: hệ số 2 từ hai lá "giữ, bỏ" và "bỏ, giữ", mỗi lá $9/100$ | 60 (6, 19) → 49 (3, 19); ghi chú 118 → 132 | 3 |
| K09 | Kiểm $p=1$; phân biệt tỷ số các kỳ vọng với kỳ vọng của tỷ số | chấp nhận | Dòng cuối: «Với $u=d=1$: tỷ số hai số đếm kỳ vọng là $1/29$, không phải $1/2$; khác $1/19$ vì tính cả “băm”.» Ghi chú thêm dạng tổng quát với tỷ lệ giữ $\eta$ (ký hiệu của ghi chú bài giảng; $p$ đã dùng cho xác suất dương giả) và kiểm $\eta=1$ cho $d/(u+d)$ | 38 (5, 16) → 42 (5, 16); ghi chú 112 → 136 | 3 |
| K01B | Hoạt cảnh năm sự kiện, bộ đếm số người dùng phân biệt | bác bỏ hoạt cảnh; giữ | Ghi chú thêm «một người dùng có $10^6$ bộ vẫn chỉ chiếm một hàng» | 58 (5, 18) không đổi; ghi chú 122 → 133 | 2,5 |
| K02 | Ngẫu nhiên nằm ở việc chọn $h$; nhất quán do $h$ cố định | một phần | Thêm dòng «$h$ được chọn ngẫu nhiên một lần trước dòng, rồi cố định.» sau dòng "Hàm băm $h$ tương tự bảng…"; dòng cuối «Giữ bộ khi $h=0$; $h(\text{An})=0$ nên cả ba bộ của An vào mẫu.» chuyển vào ghi chú (hình đã thể hiện; trang chật ở 1600×900); ghi chú bỏ vế "không có thời gian ra đĩa" (đã có ở K01B) | 40 (3, 16) → 41 (3, 16); ghi chú 144 → 141 | 3 |
| K04 | Thanh 10 ngăn; `<` và `≤`; biên $a=0$, $a=b$ | giữ (biên ở ghi chú; tỷ lệ của bài là $1/10$) | không đổi | 50 (4, 17); ghi chú 111 | 3 |
| K05 | Nhãn tất định/xác suất; giả thiết "đủ đều" | một phần | Nhãn «**Mệnh đề (tất định).**» và «**Mệnh đề (xác suất).**»; «Với mọi $h$ cố định, …»; ghi chú thêm «Số khóa được giữ trong một lần chạy là ngẫu nhiên; $a/b$ là xác suất cho từng khóa.» | 51 (4, 16) → 56 (4, 19); ghi chú 126 → 144 | 3 |
| K06 | Kéo-thả ghép cặp; khóa quá thô | giữ; bác bỏ kéo-thả | không đổi | 55 (6, 19); ghi chú 136 | 2,5 |
| K07 | Tách chi phí quyết định và lưu mẫu | giữ (đã tách hàng) | không đổi | 51 (6, 19); ghi chú 129 | 2 |
| K08 | Thanh 100 ngăn; câu chuyển tiếp dạng hỏi | giữ (thanh lộ lời giải; câu hỏi tu từ bị cấm; giới hạn ở R00) | không đổi | 33 (3, 19); ghi chú 81 | 1,5 |

Tổng mạch 3: 24 phút (không đổi).

Ghi chú bài giảng: Ví dụ 08.3 cần hình cây và một câu đọc hình; Nhận xét 08.7 thêm kiểm $\eta=1$; Nhận xét 08.11 hoặc đoạn sau Mệnh đề 08.10 thêm câu "số khóa được giữ là ngẫu nhiên" và câu hạt giống nếu chưa có (tác tử ghi chú).

### Mạch 4. Lấy mẫu hồ chứa

Thứ tự trang không đổi: RT → R00 → R01 → R03 → R04 → R05 → R06 → R07 → R08 → R09. Không hình mới (sơ đồ quyết định $j$ và ô của phần tử cũ đã có trong `reservoir-step.svg` ở R06).

| Trang | Đề xuất của bản đánh giá | Quyết định | Thay đổi | Âm tiết (dòng, max dòng) trước → sau; ghi chú | Phút |
|---|---|---|---|---|---:|
| RT | Bảng khảo sát 100 chỗ; hình dòng và hồ $s$ ô; câu hỏi công bằng | bác bỏ (trang tiêu đề mạch; số 100 chỗ tự đặt thay ví dụ MMDS) | không đổi | 39 (2, 20); ghi chú 89 | 0,5 |
| R00 | $\sum_i\Pr[x_i\in W]=s$; sơ đồ bảy phần tử | một phần (ghi chú; số đã trên mặt trang, R03 có hình vết) | Ghi chú thêm «Kiểm: sau $r=5$, $5\cdot\frac25=2=s$, đúng số ô.»; nguồn tách: MMDS §4.5.5 đặt bài toán, dòng a x c y z k c d e g chỉ ở slide Streams 1 tr.18 | 58 (4, 18) không đổi; ghi chú 105 → 113 | 2,5 |
| R01 | Phương án hai bước; sơ đồ quyết định $j$ hai màu | giữ (dòng Trực quan đã là phương án hai bước; sơ đồ trùng R06; màu không là tín hiệu duy nhất) | không đổi | 58 (4, 18); ghi chú 104 | 3 |
| R03 | [z, c] không có xác suất cao hơn; hoạt cảnh | một phần (ghi chú); bác bỏ hoạt cảnh | Ghi chú thêm «[z, c] là một kết cục; ở lần rút khác hồ có thể chứa cặp khác, và sau $r=5$ mỗi phần tử có cùng xác suất $2/5$.» | 24 (2, 13) không đổi; ghi chú 76 → 103 | 3 |
| R04 | $s=1$; đánh số dòng giả mã | một phần (không đánh số dòng) | Thêm «**Trường hợp biên:** $s=1$ giữ một phần tử, nhận $x_r$ với xác suất $1/r$.» ở cột phải, dưới hình nhỏ (dòng đọc giả mã giữ dưới khối); ghi chú thay vế lặp mặt trang bằng «MMDS §4.5.5 dùng cơ chế này để chọn vị trí các biến của phương pháp AMS (Bài 09); với $s=1$, mỗi vị trí được chọn với xác suất $1/r$.» | 37 (3, 16) → 48 (4, 16); ghi chú 107 → 129 | 3,5 |
| R05 | Mọi tập con cỡ $s$ đồng khả năng; ô mở rộng | một phần (ghi chú; mặt trang 58/60) | Ghi chú thêm «Mạnh hơn, mọi tập $s$ vị trí trong $r$ vị trí có cùng xác suất $1/\binom rs$; chứng minh ở Mệnh đề 08.18 của ghi chú bài giảng.» | 58 (5, 18) không đổi; ghi chú 102 → 130 | 2 |
| R06 | Phần tử mới chắc chắn trong hồ sau khi nhận | giữ (hình và $s/(r+1)$ đã có) | không đổi | 24 (3, 18); ghi chú 62 | 2,5 |
| R07 | Phân biệt $s/(r+1)$ với $1/(r+1)$ | chấp nhận (một dòng; trước lượt này chỉ có câu "bị thay đúng khi $j$ bằng ô chứa nó, một trong $r+1$ giá trị", chưa có phân biệt) | Thêm «**Lưu ý:** $s/(r+1)$ là xác suất nhận $x_{r+1}$; khi $x_i\in W$, $1/(r+1)$ là xác suất $j$ trúng ô của $x_i$.» (xác suất có điều kiện); ghi chú bỏ câu ví dụ trùng dòng Ví dụ trên mặt trang | 27 (5, 14) → 40 (6, 14); ghi chú 159 → 134 | 3 |
| R08 | "Mô hình RAM chuẩn"; biểu đồ đọc/ghi | giữ (mô hình đếm phép toán đã sửa ở lượt trước; biểu đồ không có dữ liệu nguồn) | không đổi | 49 (5, 20); ghi chú 88 | 2 |
| R09 | Kỳ vọng 1 khác "đúng một bộ"; nhóm hiếm; phân phối thay đổi theo thời gian | một phần (ghi chú); phân phối thay đổi theo thời gian không lên deck | Ghi chú thêm «Kỳ vọng 1 cũng không có nghĩa mỗi lần chạy có đúng một bộ của An: vì mọi tập 100 vị trí đồng khả năng, xác suất hồ không chứa bộ nào của An là $\binom{990}{100}/\binom{1000}{100}\approx0{,}347$.» (tính lại: $0{,}346928$) | 41 (6, 18) không đổi; ghi chú 101 → 137 | 3 |

Tổng mạch 4: 25 phút (không đổi).

Ghi chú bài giảng: Nhận xét 08.20 thêm gạch đầu dòng phân biệt $s/(r+1)$ và $1/(r+1)$; lời giải Bài tập 08.4 thêm $\Pr[\text{không bộ nào của An}]\approx0{,}347$; Nhận xét 08.21 (tùy chọn) thêm câu hồ chứa chọn đều trên cả lịch sử, mẫu giai đoạn gần đây cần cửa sổ (Bài 09) (tác tử ghi chú).

### Mạch 5. Lọc thành viên bằng Bloom filter

Thứ tự trang: BT → B00 → B02 → B05 → **B05A** → B05B → B01 → B03 → B04 → B06 → B07 → B08 → B09 → B10 → B11 → B12. B05A là ID mới (trang câu hỏi, cùng tiêu đề với trang lời giải B05B). Hình mới: `bloom-11bit-mang.svg` (mảng trơn, không lộ vị trí của 118 và 29; viewBox 760×176, chữ 28, hiển thị ở `stream-mini`, chữ ≈ 24 px) và `phi-tieu-8-bia.svg` (bốn phi tiêu vào tám bia, một kết cục do học phần chọn; viewBox 1180×168, chữ 28, hiển thị ≈ 25 px; bit bị trúng có khung đậm và chữ đậm). Hình sửa: `fpr-curve.svg` thêm nhãn hai vùng «k < k*: thêm phép thử, p giảm» và «k > k*: mảng đầy hơn, p tăng» (ba dòng mỗi bên để không cắt đường cong), desc và alt B11 cập nhật.

| Trang | Đề xuất của bản đánh giá | Quyết định | Thay đổi | Âm tiết (dòng, max dòng) trước → sau; ghi chú | Phút |
|---|---|---|---|---|---:|
| BT | Hai loại câu hỏi; minh họa Bloom trước CSDL | bác bỏ (trang tiêu đề mạch) | không đổi | 39 (2, 20); ghi chú 90 | 0,5 |
| B00 | Sơ đồ tỷ lệ 20 GB/1 GB; hai lộ trình | giữ (trang trí; lộ trình lọc ở B02) | không đổi | 38 (4, 12); ghi chú 79 | 2,5 |
| B02 | Mảng 12–16 ô; nhãn tiếng Anh | giữ (ví dụ 11 bit làm việc này) | không đổi | 45 (4, 13); ghi chú 95 | 2,5 |
| B05 | Ba bước, va chạm bit 7 | giữ (đã đủ) | không đổi | 33 (4, 14); ghi chú 77 | 3 |
| B05A | Sinh viên tự trả lời trước; không hiện từng bước bằng hiệu ứng | thêm (trang kế tiếp thay hiệu ứng) | «$h_1$, $h_2$ lần lượt ghép các bit ở vị trí lẻ, chẵn của khóa (đếm từ phải, từ 1), rồi lấy modulo 11.»; hình mảng trơn; «**Câu hỏi:** với $118=1110110_2$ và $29=11101_2$, tính $(h_1,h_2)$; bộ lọc trả lời gì cho mỗi khóa?» Ghi chú: gợi ý cách ghép bit, nguồn 118 (Ullman tr.8) và 29 (học phần) | — → 32 (3, 19); ghi chú — → 98 | 2 |
| B05B | Hai vị trí của 29 do hai khóa khác nhau bật | giữ làm trang lời giải; ghi chú một câu | Dòng đầu trang «**Lời giải:** 118 bị loại ngay ở bit 3; 29 chưa được thêm nhưng vẫn qua bộ lọc, một trường hợp nhận nhầm.» thay câu kết cũ; ghi chú thêm «không cần khóa nào của $S$ có cả hai vị trí 7 và 2» | 22 (3, 13) → 28 (3, 20); ghi chú 84 → 98 | 3 → 1,5 |
| B01 | Ma trận 2×2 thực tế × kết quả; nghĩa của "dương" | chấp nhận (bảng HTML) | Đầu ra rút gọn; «**Định nghĩa.** Hai ô lỗi gọi là âm giả (false negative) và dương giả (false positive).» và bảng 2×2 (hàng $y\in S$, $y\notin S$; cột hai câu trả lời; ô "dương giả, như khóa 29"); dòng ví dụ 11 bit chuyển vào ghi chú; ghi chú thêm nghĩa của "dương" | 55 (5, 18) → 49 (5, 16); ghi chú 102 → 134 | 2,5 |
| B03 | Hai khóa chung một bit; $m$ là số khóa phân biệt | một phần | Dòng đọc giả mã: «Phép duy nhất là đặt bit thành 1; 159 và 585 cùng đặt bit 7, bit đó vẫn là 1.» Ghi chú thêm «$m$ là số khóa phân biệt; thêm lại một khóa đã có không đổi mảng.», bỏ câu bit 7 (nay trên mặt trang) | 27 (2, 18) → 25 (2, 15); ghi chú 62 → 63 | 2,5 |
| B04 | Lưu đồ; ví dụ 118 dừng sớm, 29 đọc đủ | một phần (không lưu đồ) | Thêm «**Ví dụ.** 118 dừng ở bit 3; 29 đọc cả bit 7 và bit 2.»; ghi chú thay câu ví dụ trùng bằng «Khóa 118 bị loại sau một lần băm, nên bit 5 của nó không cần đọc.» | 24 (2, 14) → 33 (3, 14); ghi chú 53 → 43 | 2,5 |
| B06 | Phản ví dụ xóa bit chung; Counting Bloom filter | chấp nhận phản ví dụ; bác bỏ Counting Bloom filter (ngoài nguồn) | Thay dòng Lưu ý bằng «**Ví dụ.** Xóa 585 bằng cách đặt bit 9, 7 về 0: truy vấn 159 gặp $B[7]=0$, thành âm giả.» (tự kiểm: mảng thành $10100100000$). Ghi chú: câu xóa bit bằng lời thay bằng câu đọc ví dụ; chiều ngược (khóa 29) chuyển vào ghi chú; rút vế thừa ở câu Định lý 08.25, câu này mở bằng «Định lý 08.25 của ghi chú bài giảng có thêm hai điều kiện» | 53 (4, 19) → 55 (4, 19); ghi chú 141 → 148 | 3 |
| B07 | Minh họa $km$ phi tiêu vào $n$ bia | chấp nhận (đổi quyết định lượt trước: hình cho thấy trùng bia) | Hình `phi-tieu-8-bia.svg` dưới dòng Trực quan (`stream-mini`); bỏ dòng Ví dụ $k=1$ (trùng $p(1)\approx0{,}1175$ ở B08; câu "khớp dạng mũ tới sáu chữ số" chuyển sang ghi chú B08); ghi chú thêm $8(1-(7/8)^4)\approx3{,}31<4$ và đọc hình | 38 (5, 16) → 36 (4, 16); ghi chú 98 → 105 | 3 |
| B08 | Lý do "vị trí truy vấn trùng nhau" (sai) | giữ; lý do sai không đưa vào | Ghi chú thêm «Với $n/m=8$, $k=1$, $q$ chính xác là $0{,}1175031$, khớp dạng mũ tới sáu chữ số.» (chuyển từ B07); mặt trang giữ $p(1)\approx0{,}1175$ | 25 (5, 8); ghi chú 123 → 138 | 3,5 |
| B09 | Đồ thị chữ U, nhãn hai vùng | giữ B09; nhãn vùng đặt trên `fpr-curve.svg` (B11) | không đổi | 28 (5, 12); ghi chú 76 | 2,5 |
| B10 | Dẫn đạo hàm; mảng 50% bit; ký hiệu $\ell$; "slide 58" | giữ mặt trang (không giải trước Bài tập 4.3.3) | Ghi chú thêm «Ở mảng 11 bit ($n=11$, $m=3$), $k^*=(11/3)\ln2\approx2{,}54$; với $k=2$ gần $k^*$, mảng cuối có 5 trong 11 bit bằng 1, gần một nửa.» | 42 (4, 18) không đổi; ghi chú 104 → 127 | 3,5 → 3 |
| B11 | Thay số $p(5)$, $p(6)$; trục phần trăm | một phần (bác bỏ trục phần trăm) | Dòng công thức: «$p(5)=(1-e^{-5/8})^5\approx0{,}0217,\ p(6)=(1-e^{-6/8})^6\approx0{,}0216$»; $k^*$ chuyển vào dòng cuối «$k^*=8\ln2\approx5{,}545$: chọn $k=6$; …»; ghi chú thêm nghĩa của $0{,}0216$ | 11 (3, 8) không đổi; ghi chú 79 → 114 | 2,5 |
| B12 | Bảng hai kịch bản; đổi $k$ đòi xây lại | một phần (bảng lộ lời giải) | Ghi chú thêm «đổi $k$ phải xây lại mảng với bộ hàm băm mới, vì các bit đã đặt theo bộ hàm cũ» | 45 (7, 15) không đổi; ghi chú 96 → 116 | 3 → 2,5 |

Tổng mạch 5: 39,5 phút (B05A 2, B05B 1,5 sau rà lại; tổng hai trang vẫn 3,5). Cột phút trước lượt này cộng được 40 (ghi nhầm 40,5).

**Thời lượng toàn bài sau lượt này:** mạch 1 6,5; mạch 2 13; mạch 3 24; mạch 4 25; mạch 5 39,5; mạch 6 12; phần giảng **120 phút**. Phần bài tập 60 phút (cân lại ở mạch 7). Ghi chú "tạm 120,5" ở tiểu mục Mạch 2 đã được giải trừ.

Số đã tự tính: $118=1110110_2\to(14\bmod11,5)=(3,5)$; $29=11101_2\to(7,2)$; xóa 585 cho mảng $10100100000$, 159 đọc $B[7]=0$; $(7/8)^4=0{,}5862$, $8(1-(7/8)^4)=3{,}3105$; $p(5)=0{,}021679$, $p(6)=0{,}021577$; $(11/3)\ln2=2{,}5415$.

Ghi chú bài giảng (tác tử ghi chú): sau Định nghĩa 08.22 thêm bảng 2×2 và câu về nghĩa của "dương"; Ví dụ 08.13 chèn `phi-tieu-8-bia.svg` và câu đọc hình; §4.6 cập nhật alt của `fpr-curve.svg` (nhãn hai vùng); Nhận xét 08.31 thêm câu đổi $k$ phải xây lại; tùy chọn: câu mảng 11 bit gần nửa bit 1 sau "Ý nghĩa:" của Định lý 08.28.

### Mạch 6. Tổng kết và chuyển tiếp

Thứ tự trang không đổi: CT → C00 → C03 → C01 → C04 → C05 → C02. Không hình mới. Hai bảng tổng kết giữ cấu trúc bắt buộc của `AGENTS.md` (bác bỏ đổi cột).

| Trang | Đề xuất của bản đánh giá | Quyết định | Thay đổi | Âm tiết (dòng, max dòng) trước → sau; ghi chú | Phút |
|---|---|---|---|---|---:|
| CT | Quay lại câu hỏi "Vì sao…?" (deck không có); ba câu hỏi lớn | bác bỏ (trang tiêu đề mạch; tiêu đề dạng hỏi bị cấm) | không đổi | 37 (2, 20); ghi chú 83 | 0,5 |
| C00 | Rút thành ba thuật toán × Bảo đảm/Giả thiết; "độc lập với lịch sử"; "không xóa bit cần thiết" | giữ mặt trang (cấu trúc bắt buộc; cách viết hiện hành chính xác hơn); một phần ở ghi chú | Ghi chú thêm «Hai loại bảo đảm: tất định (cùng khóa cùng quyết định; không âm giả) và xác suất ($a/b$, $s/r$, $p(k)$).» (nhắc từ mạch 1) | 74 (6, 14) không đổi (ngoại lệ trần 80 đã ghi); ghi chú 108 → 128 | 2,5 |
| C03 | Bốn cột Đơn vị/Bộ nhớ/Chi phí/Bảo đảm | giữ (cấu trúc bắt buộc; bộ nhớ quyết định và bộ nhớ mẫu đã tách) | không đổi | 61 (4, 18); ghi chú 117 | 2,5 |
| C01 | $1/29$ là tỷ số các số đếm kỳ vọng | chấp nhận | Dòng mạch 3: «Với $h$ đều, băm người dùng giữ trọn mỗi người với xác suất $1/10$; mẫu từng bộ cho tỷ số kỳ vọng $1/29\ne1/2$.» Ghi chú: «$1/29$, tỷ số hai số đếm kỳ vọng»; thêm «khi một khóa có nhiều bộ hơn $s$, không cấu trúc nào vừa giữ trọn khóa đó vừa giữ cỡ mẫu không quá $s$» (ý từ slide 46); rút câu mở và vế thừa để giữ ≤ 150 | 76 (5, 20) → 78 (5, 20), vẫn trong ngoại lệ trần 80; ghi chú 143 → 146 | 2 |
| C04 | Công bằng giữa bộ thứ 7 và bộ thứ 999; "lần bấm" | một phần (không hiệu ứng) | Câu 2: «Hồ chứa $s=50$, $r=1\,000$: bộ thứ 7 và thứ 999 ở trong hồ với xác suất nào? Giả thiết nào dùng ở quy nạp?» (20 âm tiết). Lời giải: «$0{,}05$ cho cả bộ thứ 7 và bộ thứ 999 … $s/r$ không phụ thuộc vị trí $i$». Lời giải câu 1 đổi ký hiệu tỷ lệ giữ $p$ → $\eta$ (thống nhất K09; $p$ dành cho xác suất dương giả) | 45 (3, 20) → 46 (3, 20); ghi chú 121 → 138 | 2 |
| C05 | Định cỡ ngược $n/m\approx-\ln p/(\ln2)^2$; biểu đồ so | một phần (ghi chú; mạch kết luận không thêm khái niệm mới lên mặt trang); bác bỏ biểu đồ | Ghi chú thêm «Định cỡ ngược: từ $p(k^*)=2^{-k^*}$ và $k^*=(n/m)\ln2$ được $n/m=-\ln p/(\ln2)^2$; mục tiêu $p=0{,}01$ cần khoảng $9{,}59$ bit mỗi khóa và $k^*\approx6{,}64$; với $k=7$ nguyên, $p(7)\approx0{,}01004$, hơi trên 1%, còn 10 bit mỗi khóa với $k=7$ cho $0{,}0082$.» | 34 (3, 18) không đổi; ghi chú 99 → 136 | 1,5 |
| C02 | Đường dẫn; mục bắt buộc/nâng cao | giữ mặt trang (thêm nhãn làm vượt 6 dòng); một phần ở ghi chú | Câu cuối ghi chú (tài liệu làm chủ ngữ) thay bằng «Đọc thêm trong ghi chú bài giảng: Mệnh đề 08.18 (mọi tập con cỡ $s$ đồng khả năng) và lời giải đủ bước của số hàm băm tối ưu.» | 53 (6, 18) không đổi; ghi chú 122 → 137 | 1 |

Tổng mạch 6: 12 phút (không đổi). Phần giảng: 120 phút.

Số đã tự tính: $-\ln0{,}01/(\ln2)^2=9{,}5851$; $k^*=9{,}5851\ln2=6{,}6439$; với $n/m=9{,}5851$: $p(6)=0{,}010143$, $p(7)=0{,}010039$; với $n/m=10$, $k=7$: $p(7)=0{,}008194$; $s/r=50/1\,000=0{,}05$.

Ghi chú bài giảng (tác tử ghi chú): Nhận xét 08.31 (Trong thực hành) thêm đoạn định cỡ ngược với các số trên, không tạo Hệ quả mới; Bài tập 08.7 thêm "và bộ thứ 999" vào đề; Mục 5.2 kiểm câu $1/29$ dùng "tỷ số các số đếm kỳ vọng"; Mục 5.1 kiểm có câu hai loại bảo đảm.

Sửa nhỏ C01 sau rà lại mạch 6 (2026-10-28): dòng mạch 3 thành «Với $h$ đều, giữ trọn mỗi người dùng với xác suất $1/10$; mẫu từng bộ: tỷ số hai số đếm kỳ vọng $1/29\ne1/2$.» (20 âm tiết; $u=d=1$ của An nêu trong ghi chú); dòng Bloom filter thành «Với mảng chỉ đọc và cùng hàm băm, Bloom filter không loại địa chỉ hợp lệ.»; dòng đầu rút thành «Dòng truy vấn chỉ lưu $1/10$; $10^9$ địa chỉ thư được phép.» để giữ trần 80. C01: 77 → 78 (5, 20).

### Mạch 7. Bài tập vận dụng

Thứ tự trang: XT → X01 → **X01B** → X02 → **X02B** → X03 → **X03B** → X04 → X04B → **X04C**. Bốn ID mới là trang lời giải, cùng tiêu đề với đề, mở bằng nhãn "Lời giải:" (X04C tiếp X04B, tiêu đề thêm ", xét dấu"; X04B thêm ", điểm dừng"). Đề giữ nguyên dữ kiện và nhiệm vụ của MMDS. Hình mới `img/lec-08/chia-mang-bit.svg` (viewBox 1180×192, chữ 28, nhãn 26; hiển thị ở `stream-short` cao ≈ 187, tỷ lệ ≈ 0,98): trái một mảng 64 bit với $h_1$–$h_4$ trúng bất kỳ đâu ($h_2$, $h_3$ trùng một bit); phải bốn mảng 16 bit, mỗi $h_i$ một mảng; bit bị trúng nền đậm, có mũi tên chỉ tới. Hình chỉ dựng đề, không lộ lời giải.

| Trang | Đề xuất của bản đánh giá | Quyết định | Thay đổi | Âm tiết (dòng, max dòng) trước → sau; ghi chú | Phút (đề; làm; chữa) |
|---|---|---|---|---|---:|
| XT | Bảng bốn bài với kiến thức, độ khó | bác bỏ mặt trang (trang tiêu đề mạch); một phần ở ghi chú | Ghi chú viết gọn danh sách bốn bài và thêm «Hai bài đầu là vận dụng trực tiếp; hai bài sau đòi chứng minh, và sách đánh dấu 4.3.3 là bài khó.» (≤ 100) | 35 (2, 20) không đổi; ghi chú 86 → 89 | 0,5 |
| X01 | Xác định đơn vị trước; khóa dạng bộ; phản ví dụ mã trùng | giữ đề | Ghi chú chỉ còn gợi ý, nhắc mẫu lấy theo giá trị băm của khóa và trỏ trang lời giải | 68 (6, 20) không đổi (ngoại lệ trần 80 đã ghi); ghi chú 157 → 67 | 12 (2; 8; 2) |
| X01B | (như trên) | thêm | «**Lời giải:** xác định đơn vị mà thống kê gộp, rồi lấy khóa nhận diện đơn vị đó.» / (a) «đơn vị học phần: khóa (university, courseID);» (b) «đơn vị sinh viên: khóa (university, studentID);» (c) «đơn vị học phần: khóa (university, courseID).» / «Mã sinh viên 123 ở hai trường có thể là hai người, nên khóa luôn có university.» Ghi chú: lời giải chi tiết (chuyển từ X01), mã 123 là ví dụ của học phần | — → 51 (5, 18); ghi chú — → 171 (lời giải, dưới mức khoảng 250) | 2,5 |
| X02 | Dự đoán trước; hai cột phép tính; phần trăm | giữ đề | Ghi chú: gợi ý, dữ kiện MMDS, trỏ trang lời giải | 30 (3, 18) không đổi; ghi chú 54 → 70 | 8 (1; 5; 2) |
| X02B | (như trên) | thêm (không dùng màu, không đổi sang phần trăm) | «**Lời giải:** dùng $p(k)=(1-e^{-km/n})^k$ với $km/n=k/8$.» / «Ba hàm băm: $p(3)=(1-e^{-3/8})^3\approx0{,}0306$.» / «Bốn hàm băm: $p(4)=(1-e^{-4/8})^4\approx0{,}0240$.» / «Bốn hàm băm cho xác suất nhỏ hơn vì $3<4<k^*\approx5{,}55$; hai số là giá trị của dạng mũ $p(k)$.» Ghi chú: tiêu chí đối chiếu; không suy ra "càng nhiều càng tốt" | — → 27 (4, 17); ghi chú — → 85 | 2 |
| X03 | Hai sơ đồ cạnh nhau; dẫn công thức; chính xác/xấp xỉ | chấp nhận hình | Hình `chia-mang-bit.svg` dưới dòng "Thay $k$ hàm băm…"; ghi chú: quy ước, đọc hình, gợi ý, trỏ trang lời giải | 51 (5, 18) không đổi; ghi chú 154 → 76 | 12 (2; 8; 2) |
| X03B | (như trên) | thêm | «**Lời giải:** mảng con có $n/k$ bit và nhận $m$ phi tiêu; một bit còn 0 với xác suất $(1-k/n)^m$.» / công thức `aligned` $p_{\text{chia}}$ và $q^k$ / «Các mảng con độc lập, nên $p_{\text{chia}}$ đúng chính xác; $q^k$ của mảng chung chỉ là xấp xỉ.» / «Theo bất đẳng thức Bernoulli, $(1-1/n)^k\ge1-k/n$, nên $p_{\text{chia}}\ge q^k$; khi $n$ lớn, cả hai gần $(1-e^{-km/n})^k$.» / «**Ví dụ.** $n=64$, $m=8$, $k=4$: mảng chia $0{,}0265$; $q^k=0{,}0246$; mảng chung chính xác $0{,}0254$.» Ghi chú: lý do chính xác/xấp xỉ, chiều Bernoulli, số lớn, tiêu chí | — → 50 (5, 16); ghi chú — → 129 | 3 |
| X04 | Gợi ý ba mức; không hiện $k^*$ | chấp nhận | Thêm «**Gợi ý:** lấy logarit, tính đạo hàm theo $k$, rồi xét dấu đạo hàm ở hai phía điểm dừng.»; ghi chú bỏ phần gợi ý trùng, trỏ hai trang lời giải | 29 (3, 19) → 46 (4, 19); ghi chú 78 → 78 | 11 (2; 9; —) |
| X04B | Tách điểm dừng / xét dấu; không nhảy bước | chấp nhận tách | Tiêu đề «Bài tập: số hàm băm tối ưu, điểm dừng». «**Lời giải:** đặt $\rho=m/n$, $z=k\rho$, $\theta=e^{-z}$ (xác suất một bit bằng 0); $\lambda=\ln p=k\ln(1-\theta)$.» / `aligned` ba dòng (đạo hàm theo $k\rho$, rồi theo $\theta$, rồi $\phi$) / «Bước cuối thay $z=-\ln\theta$; dấu của $\lambda'(k)$ là dấu của $\phi(\theta)$, vì $1-\theta>0$.» / «$\phi(1/2)=0$: điểm dừng tại $\theta=1/2$, tức $k^*=(\ln2)/\rho=(n/m)\ln2$.» / «Điểm dừng chưa đủ để kết luận cực tiểu toàn cục; cần xét dấu $\phi$ ở hai phía.» | 33 (5, 11) → 38 (5, 17); ghi chú 88 → 69 | 4,5 |
| X04C | (như trên) | thêm | Tiêu đề «Bài tập: số hàm băm tối ưu, xét dấu». Năm dòng: $\phi''<0$ trên $(0,1/2)$, lõm chặt, $\phi>0$ ở giữa; $\phi(1-\theta)=-\phi(\theta)$; $k<k^*\iff\theta>1/2\iff\lambda'<0$; $p(k^*)=2^{-k^*}$; quy tắc số nguyên, $n/m=8$ chọn 6. Ghi chú: tính liên tục, nghiệm duy nhất, kiểm số, khớp Định lý 08.28 và Hệ quả 08.29 | — → 29 (5, 9); ghi chú — → 100 | 4,5 |

Tổng phần bài tập: 0,5 + 12 + 2,5 + 8 + 2 + 12 + 3 + 11 + 4,5 + 4,5 = **60 phút**, 10 trang; mỗi bài giữ tổng phút cũ (X01 14,5; X02 10; X03 15; X04 + lời giải 20), phần chữa chuyển sang trang lời giải.

**Thời lượng toàn bài sau lượt biên tập theo bản đánh giá:** phần giảng 120 phút (6,5 + 13 + 24 + 25 + 39,5 + 12), phần bài tập 60 phút. Deck 64 trang, 7 mạch; số `span.strand-number` và `#/N` không đổi.

Số đã tự tính: $p(3)=0{,}030579$, $p(4)=0{,}023969$; $n=64$, $m=8$, $k=4$: mảng chia $0{,}026450$, $q^k=0{,}024556$, mảng chung chính xác $\mathbb E[(X/n)^k]=0{,}025354$ (phân phối số bit 1 khi ném 32 phi tiêu vào 64 bia, phân số chính xác); $8\ln2=5{,}5452$; đạo hàm $\frac{d}{dk}k\ln(1-e^{-k\rho})=\ln(1-e^{-k\rho})+\frac{k\rho e^{-k\rho}}{1-e^{-k\rho}}$ đã kiểm bằng quy tắc tích.

Ghi chú bài giảng (tác tử ghi chú): Bài tập 08.11 chèn `chia-mang-bit.svg` vào đề hoặc gợi ý, kèm câu đọc hình; đối chiếu lời giải Bài tập 08.13 (chọn khóa) với X01B, Bài tập 08.10 với X02B, Bài tập 08.12 (số hàm băm tối ưu) với X04B–X04C.

Sửa nhẹ sau rà lại mạch 7 (2026-10-28): `chia-mang-bit.svg` tách nhãn «$h_2$» và «$h_3$» hai bên hai mũi tên vào bit 30 (khớp alt), nâng lên khỏi mép mảng; ghi chú X04B câu cuối thành «Còn phải chứng minh $\phi$ không có nghiệm nào khác trong $(0,1)$ và xét dấu ở hai phía.»; ghi chú X04C thêm «Từ $\phi'(\theta)=-\ln(1-\theta)-\ln\theta-2$ được $\phi''(\theta)=\frac1{1-\theta}-\frac1\theta$, âm khi $\theta<1/2$.» (đã kiểm đạo hàm); ghi chú X02 thêm gợi ý dự đoán trước khi tính ($k=4$ gần $k^*\approx5{,}5$ hơn); ghi chú X01B ý (a) phân biệt trung bình theo học phần với tỷ lệ tính trên bản ghi điểm và nêu mẫu từng bản ghi chỉ còn khoảng $1/20$ số sinh viên mỗi học phần. X04C không thêm nhãn "Lời giải (tiếp):" (không thuộc danh sách nhãn; hậu tố tiêu đề ", xét dấu" đã nói rõ).

## Trang bài toán đầu mạch (2026-10-29)

Căn cứ: yêu cầu người dùng 2026-10-29 ("với mỗi mạch, sau slide tiêu đề nên có một slide nêu vấn đề/bài toán, có minh hoạ trực quan để làm rõ vấn đề cần giải quyết") và kế hoạch đã duyệt (`scratchpad/plan-problem-08.md`). Trang tiêu đề mạch giữ nguyên, không hình. Trang ngay sau mỗi trang tiêu đề mạch nêu bài toán theo khuôn: nhu cầu, dữ liệu có số, ràng buộc, hình, câu nêu vì sao cách trực tiếp hỏng hoặc dòng "Câu hỏi:". Mỗi trang này là bước "vấn đề" của khái niệm đầu mạch. Số liệu chỉ lấy từ dữ kiện đã có (MMDS §4.1.2, §4.2.1, §4.3.1, Hình 4.1; slide Streams 1 tr.18; Ex.4.2.1; dòng năm bộ của học phần). Ba trang mới A08, K10, C06; ba trang có thêm hình R00, B00, X01. Deck 64 → 67 trang; số `span.strand-number` và `#/N` không đổi.

| Mạch | Trang | Mục đích | Thay đổi | Âm tiết (dòng, max dòng) trước → sau; ghi chú | Phút trước → sau |
|---|---|---|---|---|---:|
| 2 | AT | điểm vào mạch 2 | Ghi chú nêu bài toán đầu mạch (ba truy vấn trên dòng cảm biến), rút câu chi phí | 37 (2, 19) không đổi; ghi chú 100 → 100 | 0,5 |
| 2 | **A08** «Truy vấn trên dòng cảm biến» | vấn đề: ba truy vấn thường trực sau mỗi số, bộ nhớ nhỏ hơn lịch sử | thêm; hình `bai-toan-cam-bien.svg` | — → 54 (4, 17); ghi chú — → 114 | — → 1,5 |
| 2 | A05 «Ví dụ: trạng thái của ba truy vấn» | ví dụ: trạng thái chọn theo truy vấn | đổi tiêu đề; bỏ dòng "Muốn …" và dòng quy mô (lên A08); dòng mở và dòng kết mới; ghi chú bỏ câu quy mô | 59 (6, 17) → 43 (5, 13); ghi chú 142 → 98 | 2,5 → 1,5 |
| 2 | A00 | định nghĩa và mô hình | không đổi chữ; A08 đã đặt ràng buộc đọc một lần | 57; ghi chú 143 | 3 → 2,5 |
| 3 | KT | điểm vào mạch 3 | Ghi chú nêu bài toán đầu mạch, rút câu cụm | 39 (2, 20) không đổi; ghi chú 99 → 97 | 0,5 |
| 3 | **K10** «Tỷ lệ truy vấn lặp trên mẫu» | vấn đề: tỷ lệ lặp của mỗi người khi chỉ lưu $1/10$ | thêm; hình `bai-toan-ty-le-lap.svg` | — → 51 (4, 16); ghi chú — → 98 | — → 1,5 |
| 3 | K01 | phương án giữ từng bộ và sai lệch | hai dòng đầu thay bằng «Giữ mỗi bộ độc lập với xác suất $1/10$; xét hai bộ “đồ thị” của An.»; ghi chú bỏ câu định nghĩa tỷ lệ lặp (lên K10) | 49 (3, 19) → 27 (2, 15); ghi chú 132 → 109 | 3 → 2,5 |
| 3 | K01B | bảng nhãn | không đổi chữ; dòng năm bộ đã giới thiệu ở K10 | 58; ghi chú 133 | 2,5 → 2 |
| 4 | R00 «Mẫu cỡ cố định» | vấn đề: mẫu đúng $s$ phần tử, mỗi phần tử $s/r$ | thêm hình `bai-toan-mau-co-dinh.svg`; dòng "Muốn …" thành «**Nhu cầu:** …»; dòng Ví dụ dùng dòng bảy phần tử; ghi chú thêm câu đọc hình | 58 (4, 18) → 55 (4, 15); ghi chú 113 → 144 | 2,5 (giữ) |
| 4 | R09 | so sánh và câu hỏi | không đổi chữ; câu hỏi một phép tính | 41; ghi chú 137 | 3 → 2,5 |
| 5 | B00 «Lọc theo danh sách cho phép» | vấn đề: $S$ không vừa bộ nhớ, tra đĩa quá chậm | thêm hình `bai-toan-loc-thu.svg` giữa dòng bộ nhớ và dòng tra đĩa; ghi chú thêm câu đọc hình | 38 (4, 12) không đổi; ghi chú 79 → 111 | 2,5 (giữ) |
| 5 | B03 | giả mã xây | không đổi chữ; ví dụ 11 bit đã chạy tay việc đặt bit | 25; ghi chú 63 | 2,5 → 2 |
| 6 | CT | điểm vào mạch 6 | Ghi chú nêu trang nhắc lại hai dòng và ba câu hỏi | 37 (2, 20) không đổi; ghi chú 83 → 95 | 0,5 |
| 6 | **C06** «Hai dòng và ba câu hỏi» | nhắc lại bài toán trung tâm bằng hình, không khái niệm mới | thêm; hình `hai-dong-ba-cau-hoi.svg`; «**Câu hỏi:**» ghép câu hỏi với cấu trúc, lời giải ở các bảng và C01 | — → 32 (3, 17); ghi chú — → 107 | — → 1 |
| 6 | C01 | câu trả lời | bỏ dòng mở «Dòng truy vấn chỉ lưu $1/10$; $10^9$ địa chỉ thư được phép.» (C06 đã nêu); ghi chú câu mở nối với ba câu hỏi | 78 (5, 20) → 69 (4, 20), trong ngoại lệ trần 80; ghi chú 146 → 148 | 2 → 1,5 |
| 7 | X01 | đề MMDS 4.2.1 | thêm hình `grades-hai-truong.svg` (`stream-mini`) giữa dòng lược đồ và dòng "Câu hỏi:"; chữ đề giữ nguyên; ghi chú thêm câu đọc hình và nguồn tên | 68 (6, 20) không đổi; ghi chú 67 → 99 | 12 (giữ) |

**Hình mới** (Arial 28, `role="img"`, `<title>`, `<desc>`, alt cụ thể; tín hiệu bằng khung đậm, nét đứt, nhãn chữ):
- `bai-toan-cam-bien.svg` (1180×330, `stream-short`, chữ ≈ 23 px): dòng tám số $x_1$–$x_8$ theo thứ tự đến; lưới ba truy vấn × tám thời điểm, mọi ô "?"; cột cao "lịch sử của $10^6$ cảm biến ≈ 3,5 TB mỗi ngày, tăng theo r" so với cột thấp nét đứt "bộ nhớ cố định". Không vẽ bộ xử lý và kho (thuộc hình MMDS ở A00).
- `bai-toan-ty-le-lap.svg` (1180×300, `stream-short`, ≈ 25 px): dòng năm bộ, ba bộ của An khung đậm; khối "bộ của An: đồ thị 2 lần, băm 1 lần, tỷ lệ lặp 1/2"; hai thanh tỷ lệ 10 : 1 "dòng" và "lưu được 1/10" (nét đứt), "giữ 1/10 nào?". Không vẽ phương án nào.
- `bai-toan-mau-co-dinh.svg` (1180×262, `stream-short`, ≈ 27 px): dòng a, x, c, y, z, k, c, vị trí 1–7, hai chữ c khung đậm và ngoặc "hai phần tử khác nhau"; vạch nét đứt sau vị trí 5 và 7 với "mỗi phần tử 2/5", "2/7"; hồ W hai ô "?", "cỡ không đổi khi dòng dài thêm".
- `bai-toan-loc-thu.svg` (1180×280, `stream-short`, ≈ 27 px): hai cột chung đáy tỷ lệ 20 : 1 ("$S$: $10^9$ địa chỉ × từ 20 byte, ≥ 20 GB" và "bộ nhớ chính 1 GB = $8\cdot10^9$ bit"); ba thư đến → "địa chỉ ∈ S?" → nét đứt "quá chậm" → "đĩa: tra S cho mỗi thư". Không vẽ bộ lọc (thuộc B02).
- `hai-dong-ba-cau-hoi.svg` (1180×290, `stream-short`, ≈ 26 px): hai dòng (truy vấn, thư) với số; ba hộp câu hỏi (1)–(3) nối từ dòng tương ứng; không tên cấu trúc, không số kết quả.
- `grades-hai-truong.svg` (1180×176, `stream-mini`, ≈ 24 px): trường U1 và U2, mỗi trường có "học phần CS101" và "sinh viên 123"; hai đường nét đứt "cùng mã …: hai … khác nhau". Không ghi khóa nào.

**Thời lượng toàn bài:**

| Mạch | Trước | Sau |
|---|---:|---:|
| 1 Mở đầu | 6,5 | 6,5 |
| 2 Mô hình tính toán trên dòng | 13 | 13 |
| 3 Lấy mẫu theo khóa | 24 | 24,5 |
| 4 Lấy mẫu hồ chứa | 25 | 24,5 |
| 5 Bloom filter | 39,5 | 39 |
| 6 Tổng kết và chuyển tiếp | 12 | 12,5 |
| **Phần giảng** | **120** | **120** |
| 7 Bài tập vận dụng | 60 | 60 |

Lý do bớt: A05 và K01 nhường phần nhu cầu và dữ kiện cho trang bài toán; A00 không phải đặt lại ràng buộc đọc một lần; K01B dùng dòng năm bộ đã giới thiệu; R09 là câu hỏi một phép tính; B03 là giả mã bốn dòng mà ví dụ 11 bit đã chạy tay; C01 bỏ dòng mở trùng C06.

Ghi chú bài giảng (tác tử ghi chú; hiện các hình mới chỉ có trên deck): §1 đoạn mở, sau đoạn quy mô $3{,}46\cdot10^{12}$ byte, chèn `bai-toan-cam-bien.svg` và đoạn đọc hình; §2 đoạn mở chèn `bai-toan-ty-le-lap.svg` và câu đọc hình (nguồn "vài trăm triệu" là §4.1.2, tr.133); §3.1 sau Ví dụ 08.8 chèn `bai-toan-mau-co-dinh.svg`; §4.1 sau đoạn tình huống chèn `bai-toan-loc-thu.svg`; §5 đoạn mở chèn `hai-dong-ba-cau-hoi.svg`; Bài tập 08.13 chèn `grades-hai-truong.svg` vào đề kèm câu đọc hình. Ví dụ 08.1 có thể giữ tên cũ. Không tạo khối đánh số mới.

Sửa nhẹ sau rà lại các trang bài toán (2026-10-29): bớt chữ lặp nhãn hình, để hình nói thay.

| Trang | Thay đổi | Âm tiết (dòng, max dòng) trước → sau |
|---|---|---|
| K10 | Dòng dữ liệu rút thành «Dòng bộ (người dùng, truy vấn, thời gian); chỉ lưu $1/10$.» (quy mô ở hình); dòng An thay bằng định nghĩa «Tỷ lệ lặp: số truy vấn gõ lại chia cho số truy vấn khác nhau; với An là $1/2$.» | 51 (4, 16) → 53 (4, 18) |
| R00 | Dòng Ví dụ rút thành «**Ví dụ.** $s=2$: hình cho xác suất cần đạt sau 5 và 7 phần tử.» | 55 (4, 15) → 51 (4, 15) |
| B00 | Hai dòng cỡ $S$ và bộ nhớ gộp thành «$S$: $10^9$ địa chỉ, từ 20 GB; bộ nhớ chính 1 GB.» | 38 (4, 12) → 29 (3, 12) |
| C06 | Bỏ dòng mở (số đã ghi trên hình; ghi chú nêu nguồn) | 32 (3, 17) → 16 (2, 16) |
| C01 | Gạch đầu dòng thứ nhất tách hai: «Với $h$ đều, giữ trọn mỗi người dùng với xác suất $1/10$.» và «Mẫu từng bộ, với ba bộ của An: tỷ số hai số đếm kỳ vọng $1/29\ne1/2$.» (nêu điều kiện $u=d=1$ trên mặt trang) | 69 (4, 20) → 74 (5, 20), trong ngoại lệ trần 80 |

## Sửa K01 và K10 theo phản hồi người dùng (2026-10-29)

Căn cứ: phản hồi người dùng 2026-10-29 về K01 («giữ với bỏ nghĩa là gì, slide chưa rõ»). Mặt trang K01 dùng «giữ», hình cây dùng nhãn «giữ»/«bỏ», nhưng không trang nào nói bộ được giữ thì ghi vào mẫu, bộ bị bỏ thì không ghi vào mẫu; cơ chế rút số chỉ có ở K01B. Thứ tự trang và thời lượng không đổi. Âm tiết đếm bằng token tách theo khoảng trắng, bỏ tiêu đề, KaTeX, hình và ghi chú (script `syl_k01.py` trong scratchpad; cho K01 cũ 28 và K10 54, hơn số ghi ở bảng trên 1 đơn vị do khác cách tách token).

| Mạch | Trang | Quyết định | Thay đổi | Âm tiết (dòng, max dòng) trước → sau; ghi chú |
|---|---|---|---|---|
| 3 | K01 «Ví dụ: ba bộ truy vấn của An» | sửa (hai lượt: bản đầu, rồi sáu phát hiện của người rà lại được điều phối viên chấp nhận) | Dòng mở thay bằng hai dòng: «Với mỗi bộ, rút độc lập một số đều trong $\{0,\ldots,9\}$; xét hai bộ “đồ thị” của An.» và «**Quy ước:** số $0$ thì giữ, tức ghi bộ vào mẫu; số khác thì bỏ, tức không ghi vào mẫu.» (song song với cơ chế rút theo người dùng ở K01B; một cặp động từ «ghi vào mẫu», vì Định nghĩa 08.1 cho phép ghi dòng vào kho lưu trữ); câu chốt bỏ chữ «có» thừa. Ghi chú: câu tình huống rút còn nguồn (K10 đã nêu tình huống); thêm mẫu nằm trong bộ nhớ làm việc, bộ bị bỏ không vào bộ nhớ làm việc, dòng đọc một lượt và kho lưu trữ không được đọc để trả lời nên bộ bị bỏ không lấy lại được; bốn lá ứng với hai lựa chọn giữ/bỏ của mỗi bộ, độc lập cho phép nhân xác suất hai nhánh; bộ «băm» cũng vào mẫu với xác suất $1/10$; thay câu lặp $1/19$ bằng «khi “đồ thị” có trong mẫu, xác suất chỉ có một bản là $18/19$». Tiêu đề «ba bộ» giữ: K10 vừa vẽ đủ ba bộ, quy tắc rút áp cho mọi bộ, ghi chú nêu bộ «băm», K09 dùng cả ba. Hình `cay-hai-bo-do-thi.svg` giữ: dòng **Quy ước:** đứng ngay trên hình đã giải nghĩa nhãn; thêm dòng chú thích vào hình làm viewBox cao hơn, ảnh bị chặn ở 360 px nên chữ hình nhỏ đi (từ ≈ 24 px xuống ≈ 22 px). | `syl_k01.py`: 28 (2, 15) → 48 (3, 19); `check08.py`: 27 → 46; trong trần 60, trên mục tiêu 40 vì thêm dòng phạm vi xét theo yêu cầu rà lại; ghi chú 109 → 133 token |
| 3 | K10 «Tỷ lệ truy vấn lặp trên mẫu» | sửa | Câu hỏi «giữ $1/10$ nào để tỷ lệ của An trên mẫu vẫn là $1/2$?» thành «lưu $1/10$ nào vào mẫu để tỷ lệ của An vẫn là $1/2$?»: động từ «lưu» khớp dòng «chỉ lưu $1/10$» và nhãn hình «lưu được: 1/10»; định nghĩa giữ/bỏ cho một bộ xuất hiện ở K01; câu dẫn trang tiêu đề mạch (KT) dùng giữ/bỏ cho người dùng. Ghi chú: «ví dụ kế tiếp thử cách giữ từng bộ» thành «ví dụ kế tiếp thử lấy mẫu từng bộ». Hình `bai-toan-ty-le-lap.svg`: chữ «giữ 1/10 nào?» thành «lưu 1/10 nào?», `<desc>` và alt (deck, ghi chú bài giảng) đồng bộ. | 54 (4, 18) → 54 (4, 18); ghi chú 98 không đổi |

Ghi chú bài giảng (`lec-08-topic-03`, §2 đoạn mở và §2.1): câu hỏi của mục thành «lưu $1/10$ nào của dòng để tỷ lệ của An tính trên mẫu vẫn là $1/2$»; sau câu nêu cách rút số cho mỗi bộ thêm hai câu «Bộ được giữ thì được ghi vào mẫu, nằm trong bộ nhớ làm việc; bộ bị bỏ thì không vào bộ nhớ làm việc. Vì mỗi phần tử được đọc đúng một lần, khi nó đến, và kho lưu trữ không được đọc để trả lời (Định nghĩa 08.1), thuật toán không lấy lại được bộ bị bỏ.»; alt hình `bai-toan-ty-le-lap.svg` đổi «giữ» thành «lưu».

## Sửa mạch 3 theo phản hồi người dùng (2026-10-29)

Căn cứ: phản hồi người dùng 2026-10-29 («mạch Lấy mẫu theo khóa vẫn khó hiểu, cần giải thích kĩ hơn»); báo cáo đọc theo góc nhìn sinh viên và quyết định của điều phối viên cùng ngày. Mục tiêu: mỗi khái niệm (tỷ số hai số đếm kỳ vọng, đổi đơn vị rút, chọn $h$ một lần, khóa, ngăn, ngưỡng, $a/b$) có ví dụ số trên dòng năm bộ trước khi được dùng. Deck 67 → 71 trang; bốn trang mới nằm trong ngăn xếp dọc của mạch 3, nên `span.strand-number` và `#/N` của mọi trang tiêu đề mạch không đổi. Âm tiết đo bằng `check08.py` (cột «syl»; bỏ tiêu đề, KaTeX, hình, giả mã, ô số của bảng; tính cả tiêu đề cột bảng); số «trước» đo trên bản deck ngay trước lượt này.

**Bản đồ mạch.**

| Loại | Chức năng | Vào | Ra | Đóng góp | Trang tiêu đề mạch |
|---|---|---|---|---|---|
| thuật toán | Chỉ ra sai lệch của mẫu từng bộ bằng số đếm trên 100 người như An, đổi đơn vị rút sang người dùng, thay bảng bằng hàm băm chọn một lần trước dòng, định nghĩa khóa, ngăn, ngưỡng, chạy vết với $a=5$, chứng minh nhất quán và $a/b$, chọn khóa, đếm chi phí | Mạch 2: thuật toán dòng trả lời từ trạng thái nhỏ hơn lịch sử; dòng (người dùng, truy vấn, thời gian), tỷ lệ $1/10$ từ trang Vấn đề trung tâm | Mẫu nhất quán theo khóa, mỗi khóa xác suất $a/b$ theo phép rút $h$; người được giữ là mẫu ngẫu nhiên của người dùng nên tỷ lệ lặp tính trên họ đại diện cho người dùng điển hình; cỡ mẫu kỳ vọng $ar/b$ tăng theo dòng, là nhu cầu của mạch hồ chứa | Bài toán (K10) → ví dụ tính tay (K01) → số đếm kỳ vọng có số (K11) → tổng quát (K09) → phương án trước, «tương tự … nhưng …» (K01B) → giới hạn bảng và ý tưởng băm (K02) → trực quan phép chọn $h$ (K12) → khái niệm khóa, ngăn, ngưỡng có số (K13) → Đầu vào/Đầu ra, giả mã (K04) → vết (K14) → tính đúng (K05) → áp dụng (K06) → chi phí (K07) → kiểm tra (K08) | KT (`id="mach-3"`), điểm vào mạch 3 |

Thứ tự: KT → K10 → K01 → **K11** → K09 → K01B → K02 → **K12** → **K13** → K04 → **K14** → K05 → K06 → K07 → K08.

Dữ kiện do học phần dựng (mới): 100 người dùng, mỗi người ba bộ như An; họ hàm $h_\omega(\text{tên})=(\text{mã}+\omega)\bmod10$, $\omega$ rút đều một lần trên $\{0,\ldots,9\}$, mã An 7, Bình 4, Chi 1, $\omega=3$ cho $h=0,7,4$ (khớp số rút và giá trị băm đã có); ngưỡng $a=5$ của vết; $r=10^9$ ở K07. Truy vấn mẫu “băm” đổi thành “đệ quy” (tránh nhầm với «hàm băm $h$»; deck, `bai-toan-ty-le-lap.svg`, `bang-theo-nguoi-dung.svg`, `bam-theo-nguoi-dung.svg`, mọi alt và `<desc>`). Ghi chú bài giảng đổi ở giai đoạn sau.

**Từng trang.**

| Trang | Mục đích | Hành động của sinh viên | Đối tượng trung tâm | Quyết định và lý do | Âm tiết (dòng, dòng dài nhất) trước → sau; ghi chú GV | Phút |
|---|---|---|---|---|---|---:|
| KT | Điểm vào mạch 3 | Nhận nhiệm vụ | Lời dẫn «Muốn ước lượng tỷ lệ truy vấn lặp của người dùng điển hình, phải giữ hoặc bỏ trọn từng người.» (20 âm tiết); cụm khóa «Sai lệch của mẫu từng bộ · Bảng nhãn · Hàm băm chọn một lần · Ngăn và ngưỡng · Chọn khóa» | sửa: đại lượng ước lượng là người dùng điển hình (MMDS §4.2.1 «typical user»), không phải «mỗi người dùng» (9/10 người bị bỏ trọn); cụm khóa theo trang mới | 39 (2, 20) → 38 (2, 20); 97 → 95 | 0,5 |
| K10 | Bài toán đầu mạch | Đọc hình, định nghĩa tỷ lệ lặp | Dòng năm bộ; An «đồ thị» ×2, «đệ quy» ×1 | sửa: «Nhu cầu:» nói người dùng điển hình; định nghĩa «số truy vấn khác nhau được gõ từ hai lần, chia cho số truy vấn khác nhau» (bỏ «với An là $1/2$», hình đã ghi); tiêu đề hình «bộ theo thứ tự đến, ghi (người dùng, truy vấn), lược thời gian» khớp chữ ba thành phần; ghi chú GV nêu vì sao phải lấy mẫu (giữ chính xác số lần gõ của mọi người tăng theo dòng). Trên mục tiêu 40: bốn dòng đều cần cho bài toán | 53 (4, 18) → 55 (4, 20); 98 → 137 | 1,5 |
| K01 | Ví dụ tính tay sai lệch | Tính bốn lá và xác suất có điều kiện | Hai bộ «đồ thị» | sửa: dòng 1 gọi tên «Mẫu từng bộ:»; dòng cuối nêu hệ quả «Khi “đồ thị” có mặt, xác suất chỉ có một bản là $18/19$: An trông như không gõ lại.»; $1/19$ vào ghi chú GV. Dòng **Quy ước:** giữ nguyên (phản hồi người dùng trước). Trên mục tiêu 40: dòng quy ước và dòng hệ quả đều bắt buộc | 46 (3, 19) → 55 (3, 20); 133 → 126 | 2,5 |
| K11 | Đọc tỷ số hai số đếm kỳ vọng bằng số nguyên | Tính số người kỳ vọng mỗi trường hợp, rồi $1/29$ | Bảng `Trường hợp trong mẫu \| Xác suất mỗi người \| Số người kỳ vọng`: 1, 18, 10 | thêm: tỷ lệ lặp trên mẫu cho chính An trước công thức tổng quát; $1/29$ gắn với tử số (thấy lặp) và mẫu số (có mặt); ghi chú GV: 18 : 1, $1/29<1/19$ vì 10 lần «đệ quy», luật số lớn | — → 47 (5, 18); — → 140 | 2 |
| K09 | Tổng quát $d/(10u+19d)$ | Đọc bảng số đếm, so với tỷ lệ thật | Bảng $u$, $d$; công thức | sửa: dòng mở nêu giả thiết «không truy vấn nào hơn hai lần»; dòng cuối gọi tên tử số, mẫu số, tỷ lệ thật $d/(u+d)$ và $u=d=1$ cho $1/29$ (bỏ «khác $1/19$ vì tính cả “băm”»); ghi chú GV giữ $9u+18d=0$, dạng $\eta$, nguyên nhân hai bản quyết định riêng | 42 (5, 16) → 45 (5, 18); 136 → 119 | 1,5 |
| K01B | Phương án trước: bảng nhãn | So mẫu từng bộ với rút theo người | Bảng An 0 giữ, Bình 7 bỏ, Chi 4 bỏ | sửa: dòng giới hạn có số và nguyên nhân «quyết định riêng hai bản “đồ thị”: $1/29$ thay vì $1/2$»; «Tương tự mẫu từng bộ, nhưng rút một số cho mỗi người dùng, không cho mỗi bộ.»; **Diễn giải:** An «giữ» nên mẫu đủ ba bộ, $1/2$. Câu hỏi «bảng tăng theo đại lượng nào?» chuyển vào ghi chú GV kèm lời giải (K02 trả lời ở dòng đầu). Trên mục tiêu 40: đủ ba bước giới hạn, ý tưởng, kiểm | 58 (5, 18) → 59 (4, 17); 133 → 113 | 2 |
| K02 | Ý tưởng băm thay bảng | Nối với băm khóa ở Bài 02 | Hình năm bộ qua $h$ | sửa: dòng 1 «Bảng không bị chặn: một hàng mỗi người dùng, $10^8$ người cần 1,6 GB bộ nhớ làm việc.»; thêm **Nhắc lại:** Bài 02 băm khóa đưa mọi cặp cùng khóa tới cùng tác vụ Reduce; dòng «$h$ được chọn ngẫu nhiên một lần trước dòng, rồi cố định» (lượt bản đánh giá) chuyển sang K12, nơi nó được mở rộng thành ví dụ; ghi chú GV: không ra đĩa mỗi bộ, hàm băm biến chuỗi tên thành số | 41 (3, 16) → 48 (3, 18); 141 → 132 | 2 |
| K12 | Trực quan «xác suất theo phép chọn $h$» và tính cố định | Đọc bảng họ $h_\omega$: mỗi hàng một số 0; cột $\omega=3$ | Bảng HTML 4 hàng × 11 cột, số 0 in đậm, cột «3 (chọn)» | thêm: nguồn ngẫu nhiên là lần rút $\omega$ trước dòng (nối Bài 06), sau đó $h$ cố định; ghi chú GV nói rõ họ này chỉ cho mỗi khóa đều trên các ngăn, không cho các khóa độc lập (người cùng số dư đi cùng nhau; An, Bình, Chi không bao giờ cùng có $h=0$), thực hành dùng hạt giống | — → 28 (5, 16); — → 147 | 2,5 |
| K13 | Khái niệm khóa, ngăn, ngưỡng, $a/b$ | Đọc hình 10 ngăn, kiểm $3/10$ trên họ $h_\omega$ | Hình `ngan-va-nguong.svg` | thêm: định nghĩa khóa trước K04; «ngăn không chứa dữ liệu, khác thùng ở Bài 06» (MMDS §4.2.2); ví dụ $a=3$ (30% của slide MMDS Streams 1 tr.15–16) là bước tổng quát, không thay $1/10$; khác quyết định bác «tỷ lệ 30%» và «thanh 10 ngăn» trước đây vì phản hồi người dùng 2026-10-29 và vì K08, C04, X01 cần $a\ne1$ | — → 49 (4, 19); — → 134 | 2 |
| K04 | Đặc tả và giả mã | Đọc Đầu vào, Giả thiết, Đầu ra | `LẤY-MẪU-THEO-KHÓA(t; a, h)` | sửa câu cuối: «xác suất $a/b$ đến từ lần rút $h$ trước dòng» thay «tính đều do cách chọn $h$» | 50 (4, 17) → 53 (4, 20); 111 không đổi | 2 |
| K14 | Vết thuật toán | Đọc từng bước, tính tỷ lệ lặp trên mẫu | Bảng vết 5 bước, $a=5$ | thêm (cùng tiêu đề K04 theo AGENTS §Trang thuật toán): An $1/2$, Chi $0$, Bình vắng trọn; ghi chú GV: hai trong ba người được giữ, số người được giữ ngẫu nhiên; người được giữ đại diện cho người dùng điển hình | — → 35 (7, 16), bảng vết trong trần 8; — → 119 | 1,5 |
| K05 | Tính đúng | Đọc hai mệnh đề | Nhất quán; $a/b$ | giữ mặt trang; ghi chú GV thêm hai phản ví dụ (rút lại $\omega$ giữa dòng; hàm luôn trả 0) và câu đại diện cho người dùng điển hình | 56 (4, 19) không đổi; 144 → 146 | 2 |
| K06 | Chọn khóa | Ghép thống kê với khóa | Bảng ba thống kê | sửa: hàng đầu «tỷ lệ lặp của người dùng điển hình»; câu hỏi dùng cùng đại lượng; ghi chú GV thêm ví dụ khóa truy vấn (hai bộ «lọc» của Bình, Chi) | 55 (6, 19) không đổi; 136 → 138 | 2 |
| K07 | Chi phí | Đếm phép toán mỗi bộ | Bảng thành phần | sửa: hàng tham số «$\omega$ của $h$; $a$, $b$»; dòng cuối «Cỡ mẫu tăng theo dòng: $r=10^9$, $a/b=1/10$ cho kỳ vọng $10^8$ bộ.»; câu hạ ngưỡng (MMDS §4.2.4) chỉ còn trong ghi chú GV và ghi chú bài giảng §2.5 | 51 (6, 19) → 41 (6, 14); 129 → 136 | 1,5 |
| K08 | Kiểm tra | Chọn $<$ hay $\le$; khóa $10^6$ bộ | — | giữ | 33 (3, 19) | 1,5 |

Tổng mạch 3: **27 phút** (trước 24,5: KT 0,5; K10 1,5; K01 2,5; K09 3; K01B 2; K02 3; K04 3; K05 3; K06 2,5; K07 2; K08 1,5). K09, K02, K04, K05, K06, K07 giảm vì phần số đã chuyển sang K11, K12, K13.

Trang ngoài mạch 3 sửa theo cùng quyết định:

| Trang | Thay đổi | Âm tiết trước → sau |
|---|---|---|
| P01 | «mẫu có $\approx r/10$ bộ» → «mẫu có kỳ vọng $r/10$ bộ» (khớp K07, K08) | 72 → 74, trong ngoại lệ trần 80 đã ghi |
| C06 | Hình `hai-dong-ba-cau-hoi.svg` (chữ, `<desc>`) và alt: «(1) tỷ lệ truy vấn lặp của mỗi người dùng» → «(1) tỷ lệ lặp của người dùng điển hình» (cùng đại lượng với K10) | 16 không đổi |
| P04 | Dòng nhắc lại thứ nhất: «hàm băm cho cùng giá trị với cùng khóa (Bài 02, 05); Bài 06 rút hàm từ một họ.» | 57 (5, 17) → 60 (5, 18), bằng trần 60; trên mục tiêu 40 từ trước vì là trang tiên quyết năm dòng |

**Thời lượng toàn bài** (bớt 2,5 phút ở mạch 4–6 theo quyết định của điều phối viên):

| Trang | Phút trước → sau | Lý do |
|---|---:|---|
| R01 | 3 → 2,5 | Ngưỡng trên một số đều đã dạy ở K12–K13 |
| B04 | 2,5 → 2 | Khóa 118 và 29 đã chạy tay ở B05A–B05B |
| B09 | 2,5 → 2 | Trang câu hỏi, lời giải trong ghi chú GV |
| B11 | 2,5 → 2 | Mặt trang 11 âm tiết |
| C03 | 2,5 → 2 | Hàng lấy mẫu theo khóa nay quen với sinh viên |

| Mạch | Trước | Sau |
|---|---:|---:|
| 1 Mở đầu | 6,5 | 6,5 |
| 2 Mô hình tính toán trên dòng | 13 | 13 |
| 3 Lấy mẫu theo khóa | 24,5 | 27 |
| 4 Lấy mẫu hồ chứa | 24,5 | 24 |
| 5 Bloom filter | 39 | 37,5 |
| 6 Tổng kết và chuyển tiếp | 12,5 | 12 |
| **Phần giảng** | **120** | **120** |
| 7 Bài tập vận dụng | 60 | 60 |

Số đã tự tính: $\frac1{10}\cdot\frac1{10}=\frac1{100}$, $2\cdot\frac1{10}\cdot\frac9{10}=\frac{18}{100}$, $\frac{18/100}{19/100}=\frac{18}{19}$; trên 100 người: $1$, $18$, $10$, $\frac{1}{29}$, trong dòng $\frac{100}{200}$; $(7+\omega)\bmod10$: $7,8,9,0,1,2,3,4,5,6$ (số 0 tại $\omega=3$), Bình số 0 tại $\omega=6$, Chi tại $\omega=9$; với $\omega=3$: $0,7,4$; $(7+\omega)\bmod10<3\iff\omega\in\{3,4,5\}$; $<5\iff\omega\in\{3,\ldots,7\}$; vết $a=5$: 4 bộ, An $1/2$, Chi $0$; $10^9\cdot\frac1{10}=10^8$.

Ghi chú bài giảng (giai đoạn sau): đổi «băm» → «đệ quy» khi là truy vấn mẫu; §2.1 thêm phép đếm trên 100 người; §2.2 thêm câu nối Bài 02, bảng $h_\omega$ và đoạn đọc bảng, «ngăn không chứa dữ liệu», ví dụ $a=3$, hình `ngan-va-nguong.svg`; Ví dụ 08.5 thêm tỷ lệ lặp trên mẫu với $a=5$; bảng ký hiệu thêm $\omega$; không thêm khối đánh số.

Sửa sau kiểm của điều phối viên (2026-10-29): K12 bảng $h_\omega$ dùng lớp mới `table.stream-even` trong khối CSS Bài 08 của `lecture-style.css`, phạm vi `.reveal.course-deck.lecture-stream` (`table-layout: fixed`, cột đầu 22%, ô số căn giữa); chỉ K12 dùng lớp này nên không deck nào khác bị ảnh hưởng. Ô đầu thành «Người (mã) / $\omega$», tiêu đề cột là $0,\ldots,9$, cột được chọn in đậm $\mathbf 3$ (thay «3 (chọn)», để mười cột đều nhau); dòng kết thành «Mỗi hàng có đúng một số $0$: xác suất $1/10$. Chọn $\omega=3$: cả ba bộ của An có $h=0$, đều được giữ.» K12: 28 → 30 âm tiết (5 dòng, dòng dài nhất 18). Đã xem 1600×900 và 390×844.

**Ghi chú bài giảng, lượt mạch 3 (2026-10-29).** Không thêm khối đánh số; `note-topic-id` không đổi (`lec-08-topic-03` cho §2.1, `lec-08-topic-04` cho §2.2 và §2.4). Thay đổi:
- toàn chương: truy vấn mẫu "băm" → "đệ quy" (§2 đoạn mở, Ví dụ 08.3, đoạn sau Mệnh đề 08.6, Ví dụ 08.4, Ví dụ 08.7, alt ba hình); đại lượng "tỷ lệ truy vấn lặp của người dùng điển hình" ở cuối Mục 1, đoạn mở §2, bảng chọn khóa §2.3, Bài tập 08.2, đoạn đọc hình §5, Ví dụ 08.17 (a); tiên quyết và đoạn mở Mục 1 viết "mức lặp truy vấn theo người dùng";
- bảng ký hiệu thêm $\omega$; $h_\omega$; quy ước số liệu ghi mã 7, 4, 1 do học phần dựng;
- §2 đoạn mở: định nghĩa người dùng điển hình; đoạn đọc hình nói hình lược thời gian;
- §2.1 sau Mệnh đề 08.6: phép đếm trên 100 người như An (bảng 1, 18, 10; $1/29$; luật số lớn cho tỷ lệ gộp); Nhận xét 08.7 trỏ tới phép đếm này;
- §2.2: Diễn giải Ví dụ 08.4 nêu đơn vị rút đổi từ bộ sang người dùng; câu nối Bài 02; hai đoạn mới về họ $h_\omega(\text{tên})=(\text{mã}+\omega)\bmod10$ với bảng Markdown, đọc bảng và phạm vi của họ (mỗi khóa đều, không độc lập giữa khóa, trỏ Nhận xét 08.11); đoạn sau Định nghĩa 08.8 thêm ngăn không chứa dữ liệu, khác thùng Bài 06, ví dụ $a=3$ ($\omega\in\{3,4,5\}$), hình `ngan-va-nguong.svg` và đoạn đọc hình; Ví dụ 08.5 Diễn giải thêm tỷ lệ lặp trên mẫu với $a=5$; đoạn sau Mệnh đề 08.10 thêm câu đại diện cho người dùng điển hình và ví dụ $h_\omega$ với $a=1$.
Số token tách theo khoảng trắng: 27 325 → 28 544, trong khoảng 12 000–32 000. KaTeX: `\text{người}` gây cảnh báo thiếu metric chữ «ờ», nên deck, ghi chú, outline, storyboard dùng $h_\omega(\text{tên})$, khớp nhãn «h(tên)» của hình băm.

**Sửa theo hai lượt rà lại mạch 3 (2026-10-29).** Âm tiết theo `check08.py` (trước → sau).

| Trang | Thay đổi | Âm tiết (dòng, dòng dài nhất); ghi chú GV |
|---|---|---|
| K01 | Dòng cuối «…xác suất chỉ một bản là $18/19$: mẫu tính nó là truy vấn gõ một lần.» (bỏ văn nói); ghi chú: bộ được giữ ghi nối tiếp vào mẫu, là đầu ra | 55 → 57 (3, 20); 126 → 119 |
| K10 | Ghi chú bỏ câu chỉ đường | 55; 137 → 124 |
| K11 | Dòng kết gọi tên tử/mẫu: «Tỷ số hai số đếm kỳ vọng, thấy lặp trên có mặt: …» | 47 → 52 (5, 18); 140 |
| K09 | «$d>0$»; ghi chú nêu giữ mỗi bộ độc lập với $1/10$ | 45; 119 → 130 |
| K01B | Rút hai dòng: «Tương tự, nhưng rút một số cho mỗi người dùng, không cho mỗi bộ.», «Gặp một người lần đầu: số $0$ ghi “giữ”, số khác ghi “bỏ”; bộ sau tra bảng.» | 59 → 55 (4, 16); 113 |
| K02 | Dòng 1 nêu lý do bỏ bảng: «Bảng phải tra ở mỗi bộ nên nằm trong bộ nhớ làm việc, tăng không chặn: $10^8$ người cần 1,6 GB.»; ghi chú: mẫu chỉ ghi nối tiếp, là đầu ra; bỏ câu chỉ đường | 48 → 51 (3, 19); 132 → 144 |
| K12 | Thêm «**Nhu cầu:** $h(\text{An})=0$ là số cố định; xác suất $1/10$ nằm ở lần chọn $h$.»; dòng quy tắc thêm «giữ khi $h=0$; mã là số hiệu người dùng»; cột $\omega=3$ khung đậm hai bên (lớp `stream-pick` trong `table.stream-even`, phạm vi `.lecture-stream`), ba số 0 in đậm; ghi chú: điểm yếu của họ là người cùng số dư luôn cùng được giữ hoặc cùng bị bỏ. **Ngoại lệ 7 dòng** (2 dòng chữ, hàng tiêu đề $\omega$ và 3 hàng bảng giá trị, dòng kết): bảng giá trị của họ hàm cần hàng tiêu đề để đọc cột; 48 âm tiết, dưới trần 60 | 30 (5) → 48 (6 theo script, 7 theo AGENTS, 18); 147 → 141 |
| K13 | «**Định nghĩa.** Khóa $K(t)$ là một hoặc vài thành phần của bộ $t$ mà quyết định giữ hoặc bỏ dựa vào.»; «$h$ đưa mỗi khóa, ở đây là người dùng, vào …; ngăn không chứa dữ liệu, khác thùng Bài 06.»; ghi chú bỏ tham chiếu trang. Định nghĩa khóa giữ ở K13, không chuyển lên K02 hay K01B: K02 thêm dòng thứ tư thì trang kèm hình lớn chật ở 1600×900 (đã ghi ở lượt bản đánh giá) và vượt 60 âm tiết (ước 59–61); K01B đã ở 55 với bốn dòng cạnh hình | 49 → 53 (4, 20); 134 → 136 |
| K14 | Tiêu đề «Thuật toán: lấy mẫu theo khóa, vết trên năm bộ»; thêm «**Ý nghĩa:** mỗi người vào mẫu với cùng xác suất $a/b$ và mang đủ mọi bộ.»; ghi chú: lý do $a=5$ (ngưỡng nhận cả Chi), bỏ khẳng định «mẫu ngẫu nhiên … đại diện cho người dùng điển hình», nêu giả thiết độc lập giữa khóa cần cho từng lần chạy, họ $h_\omega$ không có. Bảng vết 6 hàng (trong trần 8) và 3 dòng chữ | 35 → 49 (8, 16); 119 → 147 |
| K05 | Ghi chú: thay khẳng định đại diện bằng «mỗi người vào mẫu với cùng xác suất $a/b$ và mang đủ mọi bộ, nên tổng theo người tính trên mẫu chia cho $a/b$ có kỳ vọng bằng tổng thật» | 56; 146 → 145 |
| K06 | Dòng mở «Khóa nhận diện đơn vị mà thống kê gộp: tỷ lệ lặp gộp các bộ theo từng người dùng.»; ghi chú nguồn «ba khóa theo MMDS §4.2.3, cột thống kê do học phần ghép», bỏ ví dụ «quốc gia». **Ngoại lệ trần 80 (bảng so sánh ba thống kê với khóa)**: 63 âm tiết (`check08.py`, tính cả tiêu đề cột và chữ trong ô), 6 dòng, dòng dài nhất 19 | 55 → 63 (6, 19); 138 → 134 |
| K07 | Hàng «hạt giống $\omega$ của $h$; $a$, $b$»; dòng kết «Trạng thái quyết định cỡ hằng; mẫu là đầu ra, tăng theo dòng: …»; ghi chú: họ độc lập từng cặp cần $O(1)$ từ, hàm hoàn toàn ngẫu nhiên không lưu được cỡ hằng; mẫu chỉ ghi nối tiếp | 41 → 50 (6, 17); 136 → 146 |
| A06 | Ghi chú: «tỷ lệ truy vấn lặp của người dùng điển hình» | 28; 142 |

K04: miền của $h$ đã có ở dòng «Đầu vào:» («hàm $h$ từ khóa vào $\{0,\ldots,b-1\}$»), nên chữ ký giả mã giữ `(t; a, h)`.

Ghi chú bài giảng (cùng lượt): §2.1 «Bộ được giữ thì được ghi nối tiếp vào mẫu, là đầu ra của thuật toán…; Phép quyết định không lưu gì theo bộ, nên trạng thái quyết định có cỡ hằng.» (khớp Định nghĩa 08.1: trạng thái trong bộ nhớ làm việc, mỗi phần tử đọc một lần, kho lưu trữ không đọc để trả lời); đoạn sau Mệnh đề 08.10 viết lại thành hai đoạn: kỳ vọng của tổng theo người và người bị bỏ trọn không làm sai tỷ lệ của người được giữ; đại diện trong từng lần chạy cần tập trung, độc lập từng cặp là đủ (Chebyshev), MMDS ngầm dùng giả thiết mạnh hơn, họ $h_\omega$ không độc lập từng cặp (người cùng số dư); §2.2 bỏ ví dụ An–Bình–Chi không cùng được giữ, «chúng ta rút $\omega$», «mã số, tức một số hiệu nguyên», chú thích ngăn và ngưỡng trước Định nghĩa 08.8; Ví dụ 08.5 «không làm sai tỷ lệ của người được giữ»; Mục 5.1 «tỷ lệ truy vấn lặp của người dùng điển hình, tính từ các truy vấn của từng người». Số token 28 544 → 28 674.

**Sửa theo lượt kiểm lại độ chính xác (2026-10-29).** Mẫu là một phần trạng thái trong bộ nhớ làm việc, tăng theo dòng, trong ngân sách $1/10$ dòng mà bài toán cho (MMDS §4.2.1), khớp Định nghĩa 08.1, A00, Nhận xét 08.4 («mẫu … là trạng thái gồm các phần tử được chọn»), Thuật toán 08.13 và ghi chú C03; trạng thái quyết định (hạt giống của $h$, $a$, $b$) có cỡ hằng. Bỏ mọi chỗ gọi mẫu là «đầu ra ghi nối tiếp».

| Trang / vị trí | Thay đổi | Âm tiết; ghi chú GV |
|---|---|---|
| K02 | Dòng 1: «Bảng là trạng thái ngoài mẫu, tra ở mỗi bộ, tăng không chặn theo số người dùng: $10^8$ người cần 1,6 GB.»; ghi chú: mẫu cũng là trạng thái tăng theo dòng nhưng nằm trong ngân sách $1/10$, bảng là phần thêm ngoài ngân sách; bỏ câu lặp Bài 02 | 51 → 52 (3, 20); 144 → 136 |
| K07 | Dòng kết: «Trạng thái quyết định cỡ hằng; mẫu là phần trạng thái tăng theo dòng: …»; ghi chú: mẫu là phần trạng thái trong ngân sách $1/10$ | 50 → 51 (6, 18); 146 → 149 |
| K01 | Ghi chú: «Bộ được giữ được ghi vào mẫu, một phần trạng thái trong bộ nhớ làm việc» | 57; 119 → 123 |
| K14 | Ghi chú: «… đủ nếu thêm giả thiết các khóa nhận giá trị băm độc lập từng cặp; MMDS coi $h$ là bộ sinh số ngẫu nhiên, mạnh hơn giả thiết này …»; bỏ câu lặp mặt trang | 49; 147 → 146 |
| Ghi chú bài giảng §2.1 | Mẫu là phần trạng thái trong ngân sách $1/10$; phần trạng thái quyết định cỡ hằng | — |
| Ghi chú bài giảng §2.2 | Bảng là trạng thái thêm ngoài ngân sách mẫu, tra ở mỗi bộ, không bị chặn | — |
| Ghi chú bài giảng, đoạn hai sau Mệnh đề 08.10 | Thêm tập trung của mỗi tổng theo người quanh $a/b$ lần tổng thật; Chebyshev áp cho cả hai đại lượng khi giá trị theo người bị chặn | — |

## Động lực và khó khăn của mạch 3 (2026-10-29)

Căn cứ: phản hồi người dùng 2026-10-29 về mạch 3 («vấn đề ở đây là "tại sao phải giải quyết vấn đề đó", động lực để giải bài toán đó là gì, khó khăn chính ở đâu?») và chẩn đoán của điều phối viên cùng ngày. Trước lượt này mạch mở bằng KT rồi K10 với «Nhu cầu: ước lượng tỷ lệ truy vấn lặp…»: không trang nào nói vì sao phải lấy mẫu (truy vấn tức thời chưa biết trước, MMDS §4.1.3, tr.134; §4.2.1, tr.136), và cái khó (nhiều bộ cùng người rải rác, quyết định khi bộ đến) chỉ hiện ra gián tiếp ở K01. Deck 71 → 72 trang; K15 nằm trong ngăn xếp dọc của mạch 3, nên `span.strand-number` và `#/N` của mọi trang tiêu đề mạch không đổi.

**Quy ước đếm âm tiết của mục này:** số đo bằng `check08.py`: tách token theo khoảng trắng, giữ token có chữ cái; **tính cả nhãn in đậm** («Nhắc lại:», «Nhu cầu:», «Câu hỏi:») và tiêu đề cột bảng; bỏ tiêu đề trang, KaTeX, hình, giả mã, ô bảng chỉ có số và ghi chú GV. Cột «dòng» đếm `p`, `li`, hàng bảng, khối câu hỏi; «dòng dài nhất» đếm cùng cách. «Trước» đo trên HEAD 56b5f0d.

Thuật ngữ: dùng lại «truy vấn tức thời (ad-hoc query)» và «truy vấn thường trực (standing query)» đã định nghĩa ở A00 và trong bảng thuật ngữ của outline; không thêm «truy vấn tùy ý» để tránh hai tên tiếng Việt cho một khái niệm. «Tùy ý» chỉ xuất hiện như tính từ thường trong ghi chú GV và ghi chú bài giảng («câu hỏi tùy ý», theo MMDS «arbitrary queries»).

Thứ tự: KT → **K15** → K10 → K01 → K11 → K09 → K01B → K02 → K12 → K13 → K04 → K14 → K05 → K06 → K07 → K08.

Chuỗi lý do của đầu mạch: mạch 2 cho trạng thái riêng cỡ hằng cho truy vấn thường trực (K15, dòng «Nhắc lại:») → nghiên cứu người dùng điển hình bằng truy vấn tức thời, chưa biết khi bộ đến; dòng có vài trăm triệu bộ mỗi ngày (hình K15), nên cần mẫu $1/10$ đại diện cho cả dòng (K15) → thống kê cụ thể là tỷ lệ lặp, phụ thuộc hai bản “đồ thị” ở $r=1$ và $r=4$; bộ $r=1$ phải được quyết định khi đến vì giữ tạm mọi bộ là lưu cả dòng (K10) → quyết định độc lập từng bộ cắt rời hai bản (K01, K11, K09) → quyết định theo người cần bảng nhãn tăng theo số người (K01B) → «Nhu cầu: mọi bộ của một người nhận cùng quyết định, không lưu nhãn theo người» được gỡ bằng hàm băm (K02, K12).

| Trang | Mục đích | Hành động của sinh viên | Đối tượng trung tâm | Quyết định và lý do | Âm tiết (dòng, dòng dài nhất) trước → sau; ghi chú GV | Phút trước → sau |
|---|---|---|---|---|---|---:|
| KT | Điểm vào mạch 3 | Nhận nhiệm vụ | Lời dẫn «Muốn trả lời truy vấn tức thời về người dùng điển hình, phải giữ hoặc bỏ trọn từng người.» (19 âm tiết); cụm khóa «Truy vấn tức thời · Sai lệch của mẫu từng bộ · Hàm băm chọn một lần · Ngăn và ngưỡng · Chọn khóa» | sửa: lời dẫn nêu nhu cầu trả lời truy vấn tức thời; cụm khóa thêm «Truy vấn tức thời», bỏ «Bảng nhãn» (bước trung gian, vẫn ở K01B); ghi chú GV mở bằng «Mạch 2 dựng trạng thái riêng cỡ hằng cho truy vấn thường trực», rồi nhu cầu mẫu, khó khăn, ba phương án và giới hạn chuyển sang mạch hồ chứa | 38 (2, 20) → 39 (2, 20); 95 → 99 | 0,5 |
| **K15** «Mẫu cho truy vấn tức thời» | Bước «trường hợp sử dụng dữ liệu lớn» và «vấn đề» của cả mạch: vì sao phải lấy mẫu | Đọc hình: quyết định lúc dòng chạy, câu hỏi về sau | Hình `mau-truy-van-tuc-thoi.svg`: dòng bộ (người dùng, truy vấn, thời gian), vài trăm triệu bộ mỗi ngày → khi bộ đến: giữ hoặc bỏ → mẫu $1/10$ dòng; bộ bị bỏ không lấy lại được (khung nét đứt); ba truy vấn tức thời chỉ vào mẫu: tỷ lệ lặp của người dùng điển hình (MMDS §4.2.1), số truy vấn của mỗi người trong tháng (thống kê theo người dùng, do học phần đặt), câu hỏi khác chưa biết trước (khung nét đứt) | thêm. Mặt trang: «**Nhắc lại:** truy vấn thường trực như giá trị lớn nhất, phương sai có trạng thái riêng cỡ hằng.» / «**Nhu cầu:** nghiên cứu hành vi người dùng điển hình bằng truy vấn tức thời, chưa biết khi bộ đến.» / hình / «Không dựng được trạng thái riêng, không lưu được cả dòng, nên cần mẫu $1/10$ đại diện cho cả dòng.» Ghi chú GV: MMDS §4.1.3 (không lưu cả dòng thì không trả lời được câu hỏi tùy ý), §4.2.1 (tập con đại diện về mặt thống kê, truy vấn tức thời trên mẫu, ngân sách $1/10$), §4.1.2 (quy mô); ngay cả tỷ lệ lặp biết trước cũng cần trạng thái tăng theo dòng; mỗi câu hỏi đến sau các quyết định giữ hoặc bỏ của những bộ nó dùng. **Trên mục tiêu 40**: ba dòng là ba mắt của chuỗi lý do (kết quả kế thừa, nhu cầu mới, yêu cầu về mẫu); bỏ một dòng thì mất một mắt; quy mô đã chuyển vào hình | — → 56 (3, 20); — → 145 | — → 1,5 |
| K10 «Tỷ lệ truy vấn lặp trên mẫu» | Bài toán cụ thể và khó khăn chính | Đọc hình: hai bản “đồ thị” ở $r=1$, $r=4$; đọc ràng buộc | Hình `bai-toan-ty-le-lap.svg` sửa: bỏ hai thanh dòng/ngân sách (quy mô nay ở K15), thêm nhãn $r=1,\ldots,5$ dưới năm bộ, ngoặc nối hai bản “đồ thị”, khối «An: “đồ thị” 2 lần, “đệ quy” 1 lần / tỷ lệ lặp của An: 1/2» và khối «lưu được: 1/10 dòng / bộ r = 1: giữ hoặc bỏ khi đến, / trước khi bộ r = 4 đến» (dòng «bộ đã bỏ không lấy lại được» chỉ còn ở hình K15) | sửa. Bỏ dòng «Dòng bộ (người dùng, truy vấn, thời gian); chỉ lưu $1/10$.» (dạng bộ và ngân sách đã ở K15); định nghĩa tỷ lệ lặp lên trước hình, bỏ chữ «được»; thêm sau hình «Bộ $r=1$ phải được quyết định khi đến: giữ tạm mọi bộ là lưu cả dòng.» (lý do hình chưa có); dòng «Câu hỏi:» giữ nguyên. Ghi chú GV: nguồn typical user, dạng bộ, lần gõ lại có thể đến bất kỳ lúc nào trong tháng nên giữ tạm là lưu cả tháng, bộ đã giữ vẫn bỏ được về sau (MMDS §4.2.4, tr.138) còn bộ đã bỏ thì mất. **Trên mục tiêu 40** từ trước (55); bốn dòng: nhu cầu, định nghĩa, khó khăn, câu hỏi | 55 (4, 20) → 58 (4, 19); 124 → 148 | 1,5 |
| K02 «Hàm băm thay bảng nhãn» | Nêu mâu thuẫn và cách gỡ | Đối chiếu yêu cầu với hình băm | Dòng «Nhu cầu:» và giới hạn của bảng | sửa. Mặt trang: «**Nhu cầu:** mọi bộ của một người nhận cùng quyết định, không lưu nhãn theo người.» / «Bảng nhãn tăng theo số người dùng, tra ở mỗi bộ: $10^8$ người cần 1,6 GB.» / «Tương tự phép băm khóa ở Bài 02, $h$ trên tên người dùng thay bảng: cùng tên luôn cho cùng giá trị.» Dòng «**Nhắc lại:** Bài 02 băm khóa…» chuyển vào ghi chú GV để giữ ba dòng cạnh hình (bốn dòng thì vượt 60 âm tiết và chật ở 1600×900); «Tương tự» nay nêu rõ phép băm khóa Bài 02. Ghi chú GV mở bằng mâu thuẫn (mẫu từng bộ không nhớ gì nhưng cắt rời các bộ cùng người; bảng nhãn giữ trọn nhưng nhớ một nhãn mỗi người), rồi câu Bài 02, cỡ 1,6 GB, không ra đĩa (MMDS §4.2.2), bộ sinh số ngẫu nhiên, mẫu trong ngân sách còn bảng ngoài ngân sách. K01B không đổi mặt trang | 52 (3, 20) → 48 (3, 20); 136 → 139 | 2 |
| K01B | Phương án bảng nhãn | — | — | giữ mặt trang; bớt phút vì K10 đã đặt khó khăn và K02 nêu mâu thuẫn | 55 không đổi | 2 → 1,5 |
| K09 | Tổng quát $d/(10u+19d)$ | — | — | giữ; bớt phút vì K11 đã tính $1/29$ trên cùng bảng với $u=d=1$, K09 chỉ thay số bằng chữ | 45 không đổi | 1,5 → 1 |
| K05 | Tính đúng | — | — | giữ; bớt phút vì K14 đã cho thấy ba bộ của An cùng quyết định trên vết, hai chứng minh mỗi cái một dòng | 56 không đổi | 2 → 1,5 |

Tổng mạch 3: 0,5 + 1,5 + 1,5 + 2,5 + 2 + 1 + 1,5 + 2 + 2,5 + 2 + 2 + 1,5 + 1,5 + 2 + 1,5 + 1,5 = **27 phút** (KT, K15, K10, K01, K11, K09, K01B, K02, K12, K13, K04, K14, K05, K06, K07, K08), không đổi. Phần giảng 120 phút (6,5 + 13 + 27 + 24 + 37,5 + 12), phần bài tập 60 phút.

Ghi chú bài giảng (`note-topic-id` không đổi; không thêm khối đánh số):
- cuối Mục 1: bỏ câu nêu lại tỷ lệ lặp và $1/10$ (nay ở đầu Mục 2), thay bằng «Ở Mục 2, chúng ta xét những câu hỏi chưa biết trước, khi trạng thái phải là một mẫu các phần tử của dòng và cách chọn mẫu quyết định câu trả lời có đúng không.»;
- đoạn mở Mục 2, năm đoạn văn và hai hình: (1) động lực: truy vấn thường trực của Mục 1 được đăng ký trước nên có trạng thái riêng, cỡ hằng; máy tìm kiếm cần truy vấn tức thời (Định nghĩa 08.1) về người dùng điển hình, đặt ra về sau; không lưu cả dòng thì không trả lời được mọi câu hỏi tùy ý (MMDS §4.1.3); cửa sổ trượt một tháng (§4.1.3) chứa cả dòng của tháng, vượt ngân sách; cách dùng ở đây là mẫu đại diện về mặt thống kê trong ngân sách $1/10$ (§4.2.1); (2) hình `mau-truy-van-tuc-thoi.svg` và đoạn đọc hình (câu hỏi số truy vấn của mỗi người trong tháng do học phần đặt; mỗi câu hỏi đến sau các quyết định của những bộ nó dùng; cách chọn mẫu chỉ dựa được vào loại câu hỏi dự kiến); (3) câu hỏi tỷ lệ lặp, người dùng điển hình, vì sao ngay cả câu hỏi biết trước này cũng cần trạng thái tăng theo dòng; (4) hình `bai-toan-ty-le-lap.svg` đã sửa và đoạn đọc hình; (5) khó khăn chính: nhiều bộ cùng người rải rác, quyết định khi bộ đến (giữ tạm là lưu cả dòng; bộ đã giữ vẫn bỏ được ở Mục 2.5, MMDS §4.2.4, bộ đã bỏ thì mất), quyết định độc lập (Mục 2.1) đối lập quyết định nhất quán bằng bảng (Mục 2.2), cần cả hai tính chất, «chúng ta dùng hàm băm đó ở Mục 2.2».
- Số token tách theo khoảng trắng: 28 751 → 29 430.

**Lượt sửa theo rà lại (2026-10-29)**, điều phối viên chấp nhận 1 nghiêm trọng, 5 trung bình, 7 nhẹ; bảng trên đã ghi trạng thái sau lượt này. Thay đổi so với bản đầu của mục: K15 «Nhắc lại:» dùng «truy vấn thường trực … phương sai … trạng thái riêng» (51 → 56 âm tiết; ghi chú KT cùng kiểu); K15 «Nhu cầu:» thêm mục đích «nghiên cứu hành vi»; dòng cuối K15 thành yêu cầu «nên cần mẫu …»; hình K15 thay «số người gõ mỗi truy vấn?» (thống kê theo khóa truy vấn) bằng «số truy vấn của mỗi người trong tháng?»; K10 dòng sau hình nêu lý do quyết định khi đến (56 → 58); hình K10 bỏ dòng «bộ đã bỏ không lấy lại được» và gộp khối của An còn ba dòng (viewBox 1180×330); K02 tách nhu cầu và giới hạn bảng, chuyển «Nhắc lại: Bài 02» vào ghi chú GV (48, 3 dòng); ghi chú GV K10 thêm «cả tháng» và nguồn §4.2.4; ghi chú bài giảng sửa như danh sách trên.

Số đã tự kiểm: hai bản “đồ thị” ở vị trí 1 và 4 của dòng (An, đồ thị), (Bình, lọc), (An, đệ quy), (An, đồ thị), (Chi, lọc); $10^8\cdot16=1{,}6\cdot10^9$ byte; tổng phút mạch 3 bằng 27.

## Động lực và khó khăn của mạch 4 (2026-10-29)

Căn cứ: yêu cầu giảng viên 2026-10-29 (mỗi mạch trả lời trên mặt trang ba câu: vì sao phải giải bài toán, động lực có số và nguồn, khó khăn chính); kế hoạch của tác tử lập kế hoạch và quyết định điều phối viên cùng ngày (quy mô có nguồn thay $10^9$ của K07; R10 là bảng so sánh, trần 80; giữ «ước lượng mômen (Bài 09)»; $p=2/5$ là lựa chọn của học phần). Âm tiết đếm bằng `check08.py` (token có chữ cái, tính cả nhãn; bỏ tiêu đề, KaTeX, hình, ô chỉ có số; dòng = `p`, `li`, hàng thân bảng; ghi chú GV = token sau khi KaTeX dựng). Số «trước» đo trên HEAD `ae156a5`.

Chuỗi lý do của đầu mạch: mạch 3 cho mẫu theo khóa có cỡ kỳ vọng $ar/b$, tăng vài chục triệu bộ mỗi ngày với $a/b=1/10$ và vài trăm triệu truy vấn mỗi ngày (MMDS §4.1.2, tr.133; §4.2.4, tr.138) → nhu cầu mẫu đúng $s$ phần tử, ở mọi $r\ge s$ mỗi phần tử đã đọc có mặt với xác suất $s/r$ (slide Streams 1 tr.12, 18), dùng để chọn vị trí cho ước lượng mômen (MMDS §4.5.5, tr.148–149) và chặn mỗi khóa ở $s$ ô (khung tr.150) (R00) → ba cách trực tiếp đều hỏng trên dòng a, x, c, y, z, k, c; khó khăn: mục tiêu $s/r$ đổi ở mỗi bước với $r$ chưa biết, nên phần tử đã giữ phải bị bỏ dần trong khi phần tử đã bỏ không lấy lại được (R10) → một số $j$ đều gộp nhận và thay (R01).

| Trang | Mục đích | Hành động của sinh viên | Đối tượng trung tâm | Quyết định và lý do | Âm tiết (dòng, dòng dài nhất) trước → sau; ghi chú GV | Phút trước → sau |
|---|---|---|---|---|---|---:|
| RT | Điểm vào mạch 4 | Nhận nhiệm vụ | Lời dẫn giữ nguyên; cụm khóa «Mẫu cỡ cố định · Ba cách trực tiếp · Vết hai ô · Bất biến quy nạp · So với mẫu theo khóa» | sửa: cụm khóa thêm «Ba cách trực tiếp», bỏ «Chi phí», «Bất biến và quy nạp» rút thành «Bất biến quy nạp» để dòng khóa ≤ 20; ghi chú GV bỏ chủ ngữ «Mạch này», nêu nhiệm vụ $s/r$ ở mọi $r\ge s$, ba cách vi phạm, kết quả giao cho mạch 5 | 39 (2, 20) → 40 (2, 20); 89 → 99 | 0,5 |
| R00 «Mẫu cỡ cố định» | Bước «trường hợp sử dụng dữ liệu lớn» và «vấn đề» của cụm hồ chứa | Đọc giới hạn có số, nhu cầu, hai ứng dụng; đọc hình $2/5$, $2/7$ | Ba dòng: «**Nhắc lại:** với $a/b=1/10$, cỡ kỳ vọng của mẫu theo khóa tăng vài chục triệu bộ mỗi ngày.» / «**Nhu cầu:** ở mọi $r\ge s$, giữ đúng $s$ phần tử, mỗi phần tử đã đọc có mặt với xác suất $s/r$.» / «Mẫu này chọn vị trí cho ước lượng mômen (Bài 09) và chặn mỗi khóa ở $s$ ô.»; hình `bai-toan-mau-co-dinh.svg` giữ | sửa: dòng khóa $10^6$ bộ (số học phần dựng) thay bằng quy mô có nguồn; bỏ dòng «Ví dụ.» (hình ghi «hồ W: 2 ô») và dòng «Lưu cả…» (chuyển vào bảng R10). Ghi chú GV: §4.2.4 (giữ mãi), §4.1.2 (quy mô), hạ ngưỡng vẫn bỏ trọn khóa $10^6$ bộ, AMS §4.5.5, khung tr.150 với $s$ ô mỗi khóa đã chọn (không phải tổng), slide tr.12, 18. **Trên mục tiêu 40**: ba dòng là ba mắt của chuỗi lý do (kết quả kế thừa, nhu cầu, ứng dụng) | 51 (4, 15) → 50 (3, 18); 144 → 149 | 2,5 |
| **R10** «Ví dụ: ba cách giữ mẫu hai ô» | Bước «vấn đề»: vì sao cách hiển nhiên hỏng, khó khăn chính | So ba cách ở $r=5$ và $r=7$ với xác suất cần đạt; đọc mâu thuẫn | Bảng `ex-table stream-compact`: lưu cả dòng, rút sau (đúng; tốn 5 ô / 7 ô); giữ 2 phần tử đầu (a, x: 1; còn lại: 0); giữ từng phần tử với xác suất $2/5$ (đúng, $\Pr[\lvert W\rvert>2]\approx0{,}32$ / sai, $\approx0{,}58$). Hai dòng: «Mục tiêu $s/r$ đổi ở mỗi bước với $r$ chưa biết, và phải đạt ở mọi bước chỉ với $s$ ô.» / «Phần tử đã giữ phải có lúc bị bỏ; phần tử đã bỏ không lấy lại được.» | thêm (mã mới; R02 đã dùng trong lịch sử nên không tái dùng). Ghi chú GV: cách 1 là lời giải «không thực tế» của slide tr.18; cách 2 là chọn vị trí một lần cho mãi mãi, thiên về vị trí đầu (§4.5.5, tr.148); cách 3 là mẫu từng bộ với $p=2/5$ do học phần chọn, phân phối nhị thức; cách «chờ lâu mới chọn» của MMDS (tr.148–149); nhận xét độ dài biết trước. **Ngoại lệ mật độ**: trang bảng so sánh, trần 80; 65 âm tiết vượt mục tiêu 40 và trần 60 của trang nội dung thường. Bỏ dòng mâu thuẫn thì còn khoảng 50 nhưng mất nửa khó khăn chính trên mặt trang, nên giữ theo quyết định điều phối viên | — → 65 (5, 18); — → 150 | — → 2 |
| R01 | Ý tưởng | — | — | giữ mặt trang; ghi chú GV mở bằng «Việc thay phần tử đã giữ đáp ứng yêu cầu bỏ dần khi $s/r$ giảm.» nối dòng mâu thuẫn của R10; bớt phút vì R10 đã cho thấy phải thay phần tử đã giữ | 58 (4, 18) không đổi; 104 → 119 | 2,5 → 2 |
| R03 | Vết hai ô | — | — | giữ; bớt phút vì dòng a, x, c, y, z đã quen từ R00 và R10 | 24 không đổi | 3 → 2,5 |
| R04 | Thuật toán | — | — | giữ; bớt phút vì hình nhỏ nhắc lại vết R03 | 48 không đổi | 3,5 → 3 |
| R06 | Phần tử mới | — | — | giữ; bớt phút vì trang chỉ có một công thức và một hình | 24 không đổi | 2,5 → 2 |

Tổng mạch 4: 0,5 + 2,5 + 2 + 2 + 2,5 + 3 + 2 + 2 + 3 + 2 + 2,5 = **24 phút** (RT, R00, R10, R01, R03, R04, R05, R06, R07, R08, R09), không đổi. Phần giảng 120 phút (6,5 + 13 + 27 + 24 + 37,5 + 12), phần bài tập 60 phút. Deck 72 → 73 trang; số mạch, `span.strand-number` và `#/N` của trang tiêu đề mạch không đổi (RT tại `#/4/1`, R10 tại `#/4/3`).

Ghi chú bài giảng (`lec-08-topic-07` không đổi; không thêm khối đánh số). Đoạn mở Mục 3 viết lại thành ba đoạn: (1) giới hạn kế thừa: Hệ quả 08.12, §4.2.4 tr.138 (giữ mãi), quy mô §4.1.2 tr.133 nhân $1/10$, Ví dụ 08.6, Thuật toán 08.13 hạ ngưỡng nhưng bỏ trọn khóa có hơn $G$ bộ; (2) hai ứng dụng: AMS (§4.5.5, tr.148–149, Bài 09) và chặn mỗi khóa ở $s$ với $s$ ô mỗi khóa đã chọn (khung tr.150); ràng buộc của slide Streams 1 tr.12, 18; vì sao xác suất chung phải là $s/r$; thay câu «Nhiều phân tích chỉ cần một mẫu đại diện…» (quy cho nguồn mơ hồ, «mẫu đại diện» nói như đã đạt); (3) «Khó khăn chính nằm ở …»: mục tiêu đổi theo $r$ chưa biết, $s$ ô và một bộ đếm; nhận xét độ dài biết trước; ba cách trực tiếp và cách chờ lâu của MMDS; từ $r$ sang $r+1$ phần tử đã giữ phải bị bỏ với xác suất xác định, phần tử đã bỏ mất, phần tử mới vào với $s/(r+1)$. Ví dụ 08.8: phần Tính thêm cách 2 và cách 3 với $N\sim$ nhị thức, hai khối `aligned` cho $\Pr[N>2]$; Diễn giải thêm một câu; Kiểm tra lại cộng ba xác suất ở $r=5$ bằng 1. Số token tách theo khoảng trắng: 29 430 → 30 053.

Số đã tự kiểm: $\binom52(0{,}4)^2(0{,}6)^3=0{,}3456$; $\Pr[N>2]=0{,}2304+0{,}0768+0{,}01024=0{,}31744$; $\Pr[N<2]=0{,}07776+0{,}2592=0{,}33696$; tổng $=1$; ở $r=7$: $0{,}0279936+0{,}1306368+0{,}2612736=0{,}419904$, $\Pr[N>2]=0{,}580096$, $\mathrm E[N]=2{,}8$; vài trăm triệu nhân $1/10$ là vài chục triệu; tổng phút mạch 4 bằng 24. Trích dẫn đối chiếu `ch4.txt`: «biased in favor of early positions» và «unreliable estimate» ở §4.5.5 (tr.148–149), khung «A General Stream-Sampling Problem» ở tr.150, «the sample will grow… forever» ở §4.2.4 (tr.138); slide Streams 1 tr.12 «At any time k», tr.18 «main memory size constraint», «Don't know length of stream in advance», «Impractical solution».

**Lượt sửa theo rà lại mạch 4 (2026-10-29)**, điều phối viên chấp nhận 4 trung bình, 10 nhẹ; không có lỗi chặn hay nghiêm trọng. Bảng trên giữ bản đầu; số đo sau lượt này thay cột âm tiết của RT, R00, R10.

| Trang | Thay đổi | Âm tiết (dòng, dòng dài nhất); ghi chú GV |
|---|---|---|
| RT | Ghi chú GV: «bỏ trọn một khóa vượt ngân sách» thay «bỏ trọn khóa nhiều bộ»; «quy nạp theo $r$ cho $s/r$» | 40 (2, 20) không đổi; 99 → 99 |
| R00 | «Nhắc lại:» tách hai dòng: «**Nhắc lại:** mẫu theo khóa có cỡ kỳ vọng $ar/b$.» / «Vài trăm triệu bộ mỗi ngày với $a/b=1/10$ thêm vài chục triệu bộ mỗi ngày.» (phần kế thừa và phép tính); dòng ứng dụng: «Mẫu này chọn $s$ vị trí cho ước lượng mômen (Bài 09); một hồ mỗi khóa giữ không quá $s$ bộ.» Hình `bai-toan-mau-co-dinh.svg`: nhãn «r = 5: cần 2/5», «r = 7: cần 2/7», «hồ W: s = 2 ô»; `<desc>`, alt deck và alt ghi chú bài giảng đồng bộ. Ghi chú GV: khung tr.150 «tối đa $s$ bộ mỗi khóa»; bỏ vế «các bộ không có cùng xác suất». **Trên mục tiêu 40**, dưới trần 60 | 50 (3, 18) → 58 (4, 18); 149 → 148 |
| R10 | Thêm dòng dữ kiện «Dòng a, x, c, y, z, k, c; $N$: số phần tử giữ.»; hàng 2 thêm «sai;» ở hai ô; hàng 3 dùng $N$ thay $\lvert W\rvert$ (tránh trái nghĩa với «hồ W: s = 2 ô» của R00): «đúng $2/5$; $\Pr[N\ne2]\approx0{,}65$» / «sai; $\Pr[N\ne2]\approx0{,}74$»; ô hàng 1 «đúng; 5 ô», «đúng; 7 ô»; dòng khó khăn: «Mục tiêu $s/r$ phải đạt ở mọi $r$, giảm sau mỗi phần tử, với $s$ ô, bộ đếm $r$, độ dài dòng chưa biết.» Hai câu kết không gộp được thành một câu ≤ 20 âm tiết, nên giữ hai dòng: dòng ràng buộc và một câu kết. Ghi chú GV: «một dạng của cách chọn vị trí một lần cho mãi mãi»; số nhị thức theo $N$ ($\Pr[N=2]$, $\Pr[N>2]$, $\Pr[N<2]$ ở $r=5$; $\Pr[N>2]$, kỳ vọng ở $r=7$); bỏ câu về phần tử a. **Ngoại lệ mật độ**: bảng so sánh, trần 80; 78 âm tiết, 6 dòng | 65 (5, 18) → 78 (6, 20); 150 → 134 |

Số tự kiểm thêm: $\Pr[N\ne2]=1-0{,}3456=0{,}6544\approx0{,}65$ ở $r=5$; $\Pr[N=2]=21\cdot0{,}16\cdot0{,}07776=0{,}2612736$, $\Pr[N\ne2]=0{,}7387264\approx0{,}74$ ở $r=7$.

Ghi chú bài giảng: đoạn 2 «chạy một hồ chứa riêng cho từng khóa, giữ tối đa $s$ phần tử cho mỗi khóa»; đoạn 3 mở bằng «mục tiêu $s/r$ giảm sau mỗi phần tử và phải đạt ở mọi $r$, trong khi độ dài dòng không biết trước và bộ nhớ chỉ có $s$ ô cùng bộ đếm $r$»; «ba cách trực tiếp khác đều không đạt (Ví dụ 08.8)»; «một dạng của cách chọn vị trí một lần cho mãi mãi»; «xác suất có mặt của mỗi phần tử đã đọc giảm từ $s/r$ xuống $s/(r+1)$»; alt hình đồng bộ nhãn mới. Số token: 30 053 → 30 058.

## Động lực và khó khăn của mạch 2 (2026-10-29)

Căn cứ: yêu cầu giảng viên 2026-10-29 (mỗi mạch trả lời trên mặt trang ba câu: vì sao phải giải bài toán, động lực có số và nguồn, khó khăn chính); kế hoạch của tác tử lập kế hoạch và quyết định điều phối viên cùng ngày (chấp nhận toàn bộ). Trước lượt này A08 nêu nhu cầu và quy mô nhưng không trang nào nói các bài trước còn thiếu gì (dữ liệu đã lưu, đọc lại được), không nêu mục đích của mạng cảm biến, và khó khăn chỉ hiện ra thành hai sự kiện rời («Giả thiết:» và «Lưu cả dòng cần khoảng 3,5 TB…»); dãy số và «3,5 TB mỗi ngày» lặp chữ của hình. Âm tiết đếm bằng `check08.py` (bỏ tiêu đề, KaTeX, hình, ô số; tính cả nhãn); ghi chú GV đếm token theo khoảng trắng; «trước» đo trên HEAD e3a3564. Deck vẫn 73 trang; số mạch, `span.strand-number` và `#/N` không đổi (AT tại `#/2/1`, A08 tại `#/2/2`).

Chuỗi lý do của đầu mạch (khớp mặt trang sau lượt rà lại): Bài 02 tính trung bình từ tổng và số đếm, trên tệp đọc lại được (A08, «Nhắc lại:») → nhu cầu tìm hiểu đại dương qua độ cao mặt biển (MMDS §4.1.2, tr.133) → mỗi dòng có 10 số mỗi giây và cần ba truy vấn trên hình (truy vấn của Ví dụ 4.1, tr.134, do học phần đặt lên dòng độ cao), khoảng 3,5 TB mỗi ngày trên hình → trả lời dùng số đã qua; giữ hết một triệu dòng vượt bộ nhớ, đọc kho lưu trữ quá chậm (§4.1.1, tr.132; §4.1.4, tr.135) → mỗi truy vấn giữ một trạng thái riêng chọn trước (A05).

Lệch có chủ ý: trang bài toán A08 mở bằng «**Nhắc lại:**» trước «**Nhu cầu:**», theo tiền lệ K15 và R00; dòng nhắc lại nêu kết quả của bài trước mà mạch này đổi giả thiết (tệp đọc lại được).

| Trang | Mục đích | Quyết định và lý do | Âm tiết (dòng, dòng dài nhất) trước → sau; ghi chú GV | Phút trước → sau |
|---|---|---|---|---:|
| AT | Điểm vào mạch 2 | giữ mặt trang; ghi chú GV câu đầu «Bài 02–07 xử lý dữ liệu đã lưu; mạch mở đầu đặt nhu cầu lấy mẫu và lọc mà không lưu cả dòng, cùng ký hiệu $x_i$, $r$.»; câu cuối «… loại bảng nhãn theo người dùng» (khớp K02) | 37 (2, 19) không đổi; 100 → 100 | 0,5 |
| A08 «Truy vấn trên dòng cảm biến» | Bước «trường hợp sử dụng dữ liệu lớn» và «vấn đề» của mạch: vì sao, động lực, khó khăn | sửa. Mặt trang: «**Nhắc lại:** Bài 02 tính trung bình từ tổng và số đếm, trên tệp đọc lại được.» / «**Nhu cầu:** tìm hiểu đại dương bằng ba truy vấn trên hình.» / «Có một triệu dòng cùng lúc, mỗi dòng 10 số mỗi giây.» / hình `bai-toan-cam-bien.svg` (không đổi) / «Trả lời dùng số đã qua; giữ hết thì vượt bộ nhớ, đọc kho lưu trữ thì quá chậm.» Bỏ «**Giả thiết:**» (A00 phát biểu hình thức), bỏ dãy số và «3,5 TB mỗi ngày» (có trên hình). «số đã qua», không «mọi số», vì truy vấn cửa sổ chỉ cần 24 số cuối; «một triệu dòng» khớp ghi chú GV (một cảm biến 3,5 MB/ngày vừa bộ nhớ, khó từ nhiều dòng). Ghi chú GV: mất nếu không xử lý ngay (tr.131), nhịp do nguồn (§4.1.1), quy mô và mục đích (§4.1.2), một cảm biến 3,5 MB vừa bộ nhớ, khó khăn từ một triệu dòng (§4.1.4), kho lưu trữ không dùng để trả lời (§4.1.1), nguồn dãy và truy vấn; bỏ câu «Hai cột…» và «Bài toán còn mở…» (mặt trang đã nêu) | 54 (4, 17) → 55 (4, 19) → 57 (4, 20) sau rà lại, trên mục tiêu 40 từ trước, dưới trần 60; 114 → 147 → 150 | 1,5 → 2 |
| A05 | Ví dụ ba trạng thái | giữ; dòng mở nay là chỗ đầu tiên viết dãy bằng chữ; hàng «tổng và số đếm» dùng lại «Nhắc lại:» của A08 | 43 (5, 13) không đổi; 98 | 1,5 |
| A02 | Chi phí | giữ; bớt phút vì A07 đã chạy tay bốn phép của cửa sổ | 58 (5, 17) không đổi; 142 | 2,5 → 2 |
| A06 | Bài tập phương sai | giữ mặt trang; ghi chú GV câu nối thay bằng «Các truy vấn của mạch này biết trước khi dòng chạy; truy vấn tức thời về người dùng điển hình thì chưa biết khi phần tử đến, nên mạch sau giữ một mẫu.» (khớp «Nhắc lại:» và «Nhu cầu:» của K15) | 28 (5, 15) không đổi; 142 → 133 → 134 | 2,5 |

Tổng mạch 2: 0,5 + 2 + 1,5 + 2,5 + 2 + 2 + 2,5 = **13 phút** (AT, A08, A05, A00, A07, A02, A06), không đổi. Phần giảng 120 phút (6,5 + 13 + 27 + 24 + 37,5 + 12), phần bài tập 60 phút.

Trang ngoài mạch 2 (theo quyết định điều phối viên, chỉ ghi chú GV):

| Trang | Thay đổi | Ghi chú GV trước → sau |
|---|---|---|
| P00 | «mẫu đại diện có cỡ cố định» → «mẫu cỡ cố định trong đó mọi phần tử đã đọc có cùng xác suất có mặt» (không nói yêu cầu như đã đạt) | 98 → 108 |
| C06 | «ba mạch giữa: tỷ lệ lặp theo người dùng» → «ba mạch lấy mẫu theo khóa, hồ chứa và Bloom filter: tỷ lệ lặp của người dùng điển hình» | 107 → 117 |

Ghi chú bài giảng (`lec-08-topic-02` không đổi; không thêm khối đánh số). Đoạn «Một triệu cảm biến…» trước hình `bai-toan-cam-bien.svg` thay bằng hai đoạn: (1) động lực: Bài 02–07 xử lý dữ liệu đã lưu, MMDS tr.131 «available when and if we want it»; Bài 02 cặp (tổng, số lượng), trích một lần rồi gọi tổng và số đếm; phần tử không xử lý hoặc lưu ngay thì mất (tr.131); nhịp do nguồn, khác hệ quản trị cơ sở dữ liệu (§4.1.1, tr.132; câu này chuyển lên từ đoạn sau Định nghĩa 08.1 để không lặp); nguồn dòng và mục đích theo §4.1.2, tr.133–134: một triệu cảm biến để tìm hiểu đại dương (3,5 MB một cảm biến, 3,5 TB cả mạng mỗi ngày), «sore throat» theo dõi lây lan virus, tỷ lệ nhấp báo tin mới hoặc liên kết hỏng; ba truy vấn Ví dụ 4.1; (2) «Khó khăn chính nằm ở chỗ…»: câu trả lời dùng số đã qua; một cảm biến vừa bộ nhớ, khó từ một triệu dòng (§4.1.4, tr.135); kho lưu trữ không dùng để trả lời (§4.1.1); xử lý kịp nhịp đến (§4.1.4); phép đếm do học phần tính: $864\,000$ số mỗi ngày, tính lại trung bình sau mỗi số tốn $\sum_{r=1}^{864\,000}(r-1)\approx3{,}73\cdot10^{11}$ phép cộng, giữ tổng và số đếm tốn khoảng $1{,}7\cdot10^6$; kết bằng câu chọn trạng thái trước khi phần tử đầu tiên đến (giữ từ bản cũ). Số token tách theo khoảng trắng: 30 058 → 30 427 (bản đầu), trong khoảng 12 000–32 000.

Số đã tự kiểm: $10\cdot4\cdot86\,400=3\,456\,000$ byte ≈ 3,5 MB; nhân $10^6$ được $3{,}456\cdot10^{12}$ byte ≈ 3,5 TB; $10\cdot86\,400=864\,000$; $864\,000\cdot863\,999/2=373\,247\,568\,000\approx3{,}73\cdot10^{11}$; $2\cdot864\,000=1\,728\,000\approx1{,}7\cdot10^6$; tổng phút mạch 2 bằng 13. Trích dẫn đối chiếu `ch4.txt`: tr.131 (đầu Chương 4), §4.1.1 tr.132, §4.1.2 tr.133–134, Ví dụ 4.1 tr.134, §4.1.4 tr.135.

Kiểm: `check08.py` (73 trang, không lỗi console, không yêu cầu mạng ngoài, không tràn khung; cờ SYL>60 chỉ ở các trang ngoại lệ đã ghi từ trước, không đổi); ảnh A08 ở 1600×900 và 390×844 đã xem; `notecheck08.py` (rộng, hẹp, in: không `.katex-error`, không tràn ngang, không lỗi).

**Sửa theo rà lại mạch 2 (2026-10-29)**, điều phối viên chấp nhận 3 trung bình, 10 nhẹ; không có lỗi chặn hay nghiêm trọng. Bảng trên giữ bản đầu; số đo sau lượt này ghi ở cột âm tiết.

| Vị trí | Thay đổi | Âm tiết; ghi chú GV |
|---|---|---|
| A08 mặt trang | «**Nhu cầu:** tìm hiểu đại dương qua độ cao mặt biển.» / «Mỗi dòng có 10 số mỗi giây và cần ba truy vấn trên hình.» (không gán ba truy vấn cho mục đích của sách) / dòng cuối có chủ ngữ: «Trả lời dùng số đã qua; giữ hết một triệu dòng vượt bộ nhớ, đọc kho lưu trữ quá chậm.»; dòng «Nhắc lại:» giữ nguyên | 55 (4, 19) → 57 (4, 20) |
| A08 ghi chú GV | mở bằng «Bài 02 gọi cặp này là (tổng, số lượng).»; «Dữ liệu một ngày của một cảm biến, 3,5 MB, vừa bộ nhớ chính; bộ nhớ làm việc không chứa được mọi dữ liệu của mọi dòng (§4.1.1, tr.132)» (theo «cannot store all the data from all the streams»); Ví dụ 4.1 viết cho cảm biến nhiệt độ gửi một số mỗi giờ, 24 số là một ngày, học phần đặt lên dòng độ cao và giữ cỡ cửa sổ 24; bỏ câu đọc dấu hỏi | 147 → 150 |
| A06 ghi chú GV | «Các truy vấn của mạch này được đặt trước khi dòng chạy» | 133 → 134 |
| Ghi chú bài giảng, đoạn động lực | câu Bài 02 (tổng, số lượng) chuyển xuống đoạn khó khăn để «giả thiết đó» quy chiếu đúng câu MMDS tr.131; bỏ «Dòng nảy sinh tự nhiên ở nhiều nơi»; «dòng lượt nhấp (click), hàng tỷ lượt mỗi ngày ở các trang của Yahoo!, số lượt nhấp vào một liên kết tăng đột ngột …» (§4.1.2, tr.133–134); Ví dụ 4.1 viết cho cảm biến nhiệt độ một số mỗi giờ, cửa sổ 24 số ứng với một ngày; học phần đặt ba truy vấn lên dòng độ cao, giữ cỡ cửa sổ 24 | — |
| Ghi chú bài giảng, đoạn khó khăn | bỏ lặp 3,5 MB: «Dữ liệu một ngày của một cảm biến vừa bộ nhớ chính»; thêm §4.1.1, tr.132 (bộ nhớ làm việc không chứa mọi dữ liệu của mọi dòng); câu Bài 02 đặt cạnh phép đếm «giữ tổng và số đếm tốn hai phép cộng mỗi số»; «Hai phép đếm này do học phần tính» | — |
| Ghi chú bài giảng, đoạn đọc hình | «Việc của mục là điền …» → «Bài toán đặt ra: điền các ô của lưới mà không giữ cả cột lịch sử.» | — |

Số token ghi chú bài giảng: 30 058 → 30 482. Kiểm sau lượt này: `check08.py` (73 trang, không lỗi console, không yêu cầu mạng ngoài, không tràn; cờ SYL>60 không đổi), ảnh A08 1600×900 và 390×844 đã xem, `notecheck08.py` rộng, hẹp, in không lỗi.

## Động lực và khó khăn của mạch 5 (2026-10-29)

Căn cứ: yêu cầu giảng viên 2026-10-29 (mỗi mạch trả lời trên mặt trang ba câu: vì sao phải giải bài toán, động lực có số và nguồn, khó khăn chính); kế hoạch của tác tử lập kế hoạch mạch 5 và quyết định điều phối viên cùng ngày (thêm B13 «Lỗi một phía của bộ lọc»; số 80% thư rác chỉ ở ghi chú, ghi là số MMDS dẫn lại; phương án giữ $1/20$ của $S$ là lập luận của học phần, kèm điều kiện cận trên; không viết «cách duy nhất», nêu các lựa chọn của §4.4.1; không thêm số mili giây).

Chuỗi lý do của đầu mạch: mạch 3–4 bỏ phần lớn bộ và trả lời trên phần giữ lại → lọc thư cần một quyết định cho từng thư và không được chặn thư từ $S$, dùng để chặn thư rác (MMDS §4.3, §4.3.1, tr.139) → ba cách trực tiếp: bảng lưu $S$ cần từ 20 GB (trang chiếu MMDS Streams 2 tr.4), tra đĩa mỗi thư (§4.1.4, tr.135), giữ $1/20$ của $S$ thì mọi thư ngoài $S$ vẫn tra đĩa (học phần) → khó khăn chính: 8 bit mỗi địa chỉ so với từ 160 bit, nên chọn phía được sai: “chắc chắn không thuộc” luôn đúng, “có thể thuộc” được phép sai (lỗi một phía), xác suất nhận nhầm giảm khi tăng số bit mỗi địa chỉ → B02: bit 0 cho “chắc chắn không thuộc”; một hàm băm cho chưa đến $1/8$ địa chỉ ngoài $S$ qua bộ lọc.

Âm tiết theo `check08.py` (đếm cả nhãn; không tính tiêu đề, KaTeX, hình); ghi chú GV đếm theo khoảng trắng.

| Trang | Mục đích | Hành động của sinh viên | Đối tượng trung tâm | Quyết định và lý do | Âm tiết (dòng, dòng dài nhất) trước → sau; ghi chú GV | Phút trước → sau |
|---|---|---|---|---|---|---:|
| BT | Điểm vào mạch 5 | Nhận nhiệm vụ | Lời dẫn «Muốn lọc theo tập lớn hơn bộ nhớ nhiều lần, phải cho phép nhận nhầm một phần khóa ngoài tập.»; cụm khóa «Lỗi một phía · Mảng bit và hàm băm · Xác suất nhận nhầm · Số hàm băm tối ưu» | sửa: lời dẫn nêu khó khăn trước giải pháp; bỏ khóa «Không bỏ sót khóa của tập» (trùng nghĩa với lỗi một phía, giữ dòng khóa ≤ 20); ghi chú GV nêu 8 bit so với 160 bit | 39 (2, 20) → 37 (2, 20); 90 → 97 | 0,5 |
| B00 «Lọc theo danh sách cho phép» | Bước «trường hợp sử dụng dữ liệu lớn» và «vấn đề»: vì sao phải lọc, vì sao cách hiển nhiên không dùng được | Đọc kế thừa, nhu cầu; đọc hình 20 : 1 và nhánh tra đĩa; đọc dòng giữ $1/20$ | «**Nhắc lại:** lấy mẫu được bỏ phần lớn bộ; câu hỏi được trả lời trên phần giữ lại.» / «**Nhu cầu:** chặn thư rác; mỗi thư đến chỉ qua khi địa chỉ gửi thuộc danh sách tin cậy $S$.» / hình / «Nếu chỉ giữ $1/20$ của $S$, địa chỉ không thấy vẫn có thể thuộc $S$, nên mọi thư ngoài $S$ phải tra đĩa.» | sửa: bỏ hai dòng lặp nhãn hình (cỡ $S$, bộ nhớ; tra đĩa quá chậm); hình `bai-toan-loc-thu.svg` đổi nhãn cột cao thành «bảng lưu S: 10⁹ địa chỉ», `<title>`, `<desc>`, alt deck và ghi chú đồng bộ; ghi chú GV: §4.3 (tiêu chuẩn tính từ bộ và tiêu chuẩn thành viên), 80% do sách dẫn lại, bảng băm (Streams 2 tr.4), §4.1.4 tr.135, dòng $1/20$ là lập luận của học phần (nhiều nhất $1/20$, chưa kể phần phụ của bảng), §4.4.1 tr.142, ở bài toán đếm phần tử phân biệt (nhiều máy, mỗi máy một hoặc vài dòng; gom theo khối đĩa) | 29 (3, 12) → 55 (3, 19); 111 → 142 | 2,5 |
| **B13** «Lỗi một phía của bộ lọc» | Bước «vấn đề»: khó khăn chính, phía được sai, cái giá và cách kiểm soát | Đọc phép chia 8 bit; nêu câu trả lời nào phải luôn đúng | «Bộ nhớ có 8 bit mỗi địa chỉ; một địa chỉ cần từ 160 bit.» / «**Nhu cầu:** “chắc chắn không thuộc” luôn đúng, để không chặn thư nào từ $S$.» / «Một số địa chỉ ngoài $S$ được phép nhận “có thể thuộc”, tức lỗi một phía (one-sided error).» / «Xác suất nhận nhầm giảm khi tăng số bit mỗi địa chỉ.» | thêm (mã mới, chưa dùng); không hình (tỷ lệ 160 : 8 trùng 20 : 1 của B00, sơ đồ hai câu trả lời ở B02); gộp vào B00 hoặc B02 vượt trần 60 (62–69 âm tiết) và dồn hai ý trung tâm. Ghi chú GV: phép tính 8 bit và 160 bit; câu «không lưu được» là nhận xét, bài không chứng minh; chặn nhầm không chấp nhận được, cho qua thì tra đĩa hoặc thư rác vào hộp thư (§4.3.1); chiều ngược với giữ $1/20$; điều kiện không xóa bit, cùng hàm băm, cùng mảng; xác suất cho một địa chỉ ngoài $S$ cố định, không phải tỷ lệ thư rác | — → 54 (4, 17); — → 149 | — → 1,5 |
| B02 | Ý tưởng | — | Dòng cuối «Với một hàm băm và 8 bit mỗi địa chỉ, chưa đến $1/8$ địa chỉ ngoài $S$ qua bộ lọc.» | sửa: dòng cũ «Chỉ khóa qua bộ lọc mới cần tra $S$ trên đĩa.» lặp nhãn hình, chuyển vào ghi chú GV; ghi chú GV thêm $1-e^{-1/8}\approx0{,}1175$ (Ví dụ 4.3, tr.141); bớt phút vì yêu cầu sai một phía đã đặt ở B13 | 45 (4, 13) → 52 (4, 17); 95 → 137 | 2,5 → 2 |
| B01 | Đặc tả, định nghĩa | — | — | giữ; bớt phút vì hai loại lỗi đã mô tả bằng lời ở B13 | 49 (5, 16) không đổi; 134 | 2,5 → 2 |
| B10 | Số hàm băm tối ưu | — | — | giữ; bớt phút vì trang chỉ phát biểu, chứng minh đầy đủ ở X04 | 42 (4, 18) không đổi; 127 | 3 → 2,5 |

Tổng mạch 5: 0,5 + 2,5 + 1,5 + 2 + 3 + 2 + 1,5 + 2 + 2 + 2 + 3 + 3 + 3,5 + 2 + 2,5 + 2 + 2,5 = **37,5 phút** (BT, B00, B13, B02, B05, B05A, B05B, B01, B03, B04, B06, B07, B08, B09, B10, B11, B12), không đổi. Phần giảng 120 phút (6,5 + 13 + 27 + 24 + 37,5 + 12), phần bài tập 60 phút. Deck 73 → 74 trang; số mạch, `span.strand-number` và `#/N` của trang tiêu đề mạch không đổi (BT tại `#/5/1`, B13 tại `#/5/3`).

Ghi chú bài giảng (`lec-08-topic-09` không đổi; không thêm khối đánh số). Đoạn mở Mục 4 viết lại thành đoạn động lực: lấy mẫu trả lời trên phần giữ lại, còn lọc phải quyết định từng thư; MMDS §4.3, tr.139 (tiêu chuẩn tính từ bộ và tiêu chuẩn thành viên); chặn thư rác, 80% là số sách dẫn lại từ một số báo cáo (§4.3.1); hệ đăng ký nhận tin (publish–subscribe, trang chiếu MMDS Streams 2, tr.5) và quảng cáo đã xem (CS246 ngày 26/02/2026, tr.24). Mục 4.1, sau đoạn đọc hình: hai đoạn «Khó khăn chính nằm ở …»: (1) ba cách trực tiếp (bảng băm, tr.4; tra đĩa, §4.1.4 tr.135; giữ $1/20$ của $S$, lập luận của học phần, nhiều nhất $1/20$ chưa kể phần phụ) và hai lựa chọn của §4.4.1, tr.142, nêu cho bài toán đếm phần tử phân biệt (thêm máy, mỗi máy một hoặc vài dòng; gom theo khối đĩa; cái giá là số máy hoặc độ trễ); (2) 8 bit so với 160 bit, chọn phía được sai, thuật ngữ **lỗi một phía** (one-sided error) lần đầu, xác suất cho một địa chỉ ngoài $S$ cố định không phải tỷ lệ thư rác, dẫn tới Mục 4.5–4.6, bộ lọc nối tầng (cascade, §4.3.1, tr.139–140). Alt và đoạn đọc hình `bai-toan-loc-thu.svg` thêm «bảng lưu». Tài liệu tham khảo: MMDS thêm §4.4.1, tr.142; CS246 2026 thêm tr.23–24. Số token toàn chương 30 482 → 31 181 (Mục 4: 5 060 → 5 724), dưới trần 32 000.

Số đã tự kiểm: $10^9\cdot20$ byte $=2\cdot10^{10}$ byte = 20 GB; 1 GB $=8\cdot10^9$ bit; $8\cdot10^9/10^9=8$; $20\cdot8=160$; $160/8=20=20/1$; $1-e^{-1/8}=0{,}117503<1/8$; với $k$ cố định, $(1-e^{-k/r})^k$ giảm theo $r=n/m$ (ví dụ $k=1$: $0{,}2212$, $0{,}1175$, $0{,}0606$ ở $r=4,8,16$; $k=6$: $0{,}2198$, $0{,}0216$, $0{,}00094$); tổng phút mạch 5 bằng 37,5. Trích dẫn đối chiếu `ch4.txt`: §4.3 và §4.3.1 tr.139 («It is especially hard, when that set is too large to store in main memory»; «about 80% according to some reports»; «a cascade of filters, each of which would eliminate 7/8th of the remaining spam», sang tr.140); §4.1.4 tr.135 («without access to secondary storage or with only rare accesses»); §4.4.1 tr.142, bài toán đếm phần tử phân biệt («We could use more machines, each machine handling only one or several of the streams … batch stream elements»); Ví dụ 4.3 tr.141.

**Lượt sửa theo rà lại mạch 5 (2026-10-29)**, điều phối viên chấp nhận 5 trung bình, 12 nhẹ; không có lỗi chặn hay nghiêm trọng. Bảng trên giữ bản đầu; số đo sau lượt này thay cột âm tiết.

| Trang | Thay đổi | Âm tiết (dòng, dòng dài nhất); ghi chú GV | Phút |
|---|---|---|---:|
| BT | Dòng dẫn «Muốn lọc trong bộ nhớ nhỏ hơn tập nhiều lần, phải cho phép nhận nhầm một phần khóa ngoài tập.»; ghi chú GV «thường dài từ 160 bit». Dòng khóa giữ «Xác suất nhận nhầm» (dương giả chưa định nghĩa ở trang tiêu đề mạch); ghi chú GV B01 thêm «dương giả (còn gọi là nhận nhầm)» để nối với B08 | 37 (2, 20); 98 | 0,5 |
| B00 | Dòng cuối tách hai, nối với «Nhắc lại:»: «Lấy mẫu $1/20$ của $S$: địa chỉ vắng trong mẫu vẫn có thể thuộc $S$.» / «Mọi thư từ địa chỉ ngoài mẫu phải tra đĩa.»; ghi chú GV: §4.4.1 sửa thành tr.142, ghi rõ ngữ cảnh đếm phần tử phân biệt, «mỗi máy xử lý một hoặc vài dòng» | 58 (4, 19); 150 | 2,5 |
| B13 | Dòng 1 «1 GB cho $10^9$ địa chỉ: 8 bit mỗi địa chỉ; một địa chỉ thường dài từ 160 bit.»; dòng 3–4 thay bằng bảng `ex-table` 2×2 (cột «Mẫu $1/20$ của $S$» và «Bộ lọc cần»; hàng «“thuộc” / “có thể thuộc”»: luôn đúng | có thể sai với địa chỉ ngoài $S$; hàng «“không thuộc”»: không chắc, phải tra đĩa | luôn đúng) và dòng «Bộ lọc chỉ sai ở hàng trên, gọi là lỗi một phía (one-sided error).». Tiêu đề cột trái viết «Mẫu» thay «Giữ» để khớp B00. Ghi chú GV: bỏ câu về chứng minh, không thêm lập luận bất khả; «chứng minh ở trang Tính đúng: không có âm giả»; câu nối «Mạch tính xác suất một địa chỉ ngoài $S$ cố định bị nhận nhầm theo số bit mỗi địa chỉ và số hàm băm» đặt ở ghi chú GV vì mặt trang hết chỗ. **Ngoại lệ mật độ:** trang có bảng so sánh, trần 80; 54 → 63 âm tiết, 5 dòng (hai hàng bảng), dòng dài nhất 15 | 63 (5, 15); 144 | 1,5 |
| B02 | Dòng cuối «Với một hàm băm và 8 bit mỗi địa chỉ, địa chỉ ngoài $S$ qua bộ lọc với xác suất chưa đến $1/8$.» (bỏ «mỗi» trước «địa chỉ ngoài» để dòng ≤ 20 âm tiết) | 55 (4, 20); 137 | 2 |

Tổng mạch 5 vẫn 37,5 phút. Ghi chú bài giảng: §4.4.1 sửa thành tr.142 ở đoạn khó khăn và tài liệu tham khảo («§4.3, tr.139–142: Mục 4 (Ví dụ 4.3–4.4) và Bài tập 08.10–08.12. §4.4.1, tr.142: …»); ngữ cảnh đếm phần tử phân biệt và «mỗi máy xử lý một hoặc vài dòng» thay câu nhiều máy cũ, bỏ «ít nhất 20 máy»; «thường dài từ 20 byte», «thường dài từ 160 bit»; thêm «cùng khoảng $19/20$ thư hợp lệ (nếu thư hợp lệ đến đều từ các địa chỉ của $S$)»; câu «Đổi lại, mỗi địa chỉ ngoài $S$ cố định được cho qua với một xác suất; xác suất này không phải tỷ lệ thư rác.»; «Mục 4.5–4.7»; đoạn trực quan «hơi ít hơn $1/8$ số bit bằng 1 (khoảng $0{,}1175$, Ví dụ 08.14, …)»; gộp đoạn đọc hình `bai-toan-loc-thu.svg` vào đoạn khó khăn, bỏ lặp 20 GB/1 GB, rút câu §4.3 và câu ứng dụng. Số token toàn chương 31 181 → 31 032 (Mục 4: 5 724 → 5 575).
