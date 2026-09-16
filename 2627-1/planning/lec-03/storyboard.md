# Lecture 03 — Đề xuất xây dựng lại từ đầu

Trạng thái: đang triển khai bảy phần theo yêu cầu giảng viên. Phần 1 có sáu slide đã kiểm định và storyboard chi tiết bên dưới; các phần 2–7 còn ở kế hoạch. Chưa hoàn tất toàn deck. Bản mới không lấy cấu trúc, slide hay ghi chú cũ làm khuôn.

## Phạm vi và mục tiêu

- Tên bài: **PageRank: mô hình và tính toán**, Bài 03 theo thứ tự đề xuất trong `sources/source.md`; tiếp nối phép nhân ma trận–véc tơ và MapReduce của Bài 02.
- Nguồn chính: MMDS 3e Chương 5, mục 5.1–5.2. Đối chiếu `sources/reference-slides/mmds/ch05-linkanalysis1.pdf` và `sources/reference-slides/stanford-cs246/09-pagerank.pdf`.
- Sinh viên năm 2: biết đồ thị có hướng, xác suất cơ bản và đại số tuyến tính; không giả định đã học chuỗi Markov hoặc cơ sở dữ liệu.
- Đầu ra: giải thích ý nghĩa điểm; lập phép cập nhật; xử lý nút cụt và bẫy liên kết; chạy lặp, kiểm kết quả; mô tả phép tính theo khối/MapReduce; tính chi phí cơ bản và chuyển thuật toán thành Python.
- Để Bài 04 xử lý PageRank theo chủ đề, liên kết rác, TrustRank và HITS. Không mở thêm phần hệ thống Hadoop; dùng lại Bài 02 khi cần.

## Bảy section đề xuất

| Phần | Tên trên mục lục | Loại phần | Thời lượng chính dự kiến |
|---|---|---|---:|
| 1 | Giới thiệu bài học | Giới thiệu và động lực | 10 phút |
| 2 | Bài toán Xếp hạng trang web | Phát biểu bài toán, ví dụ và trực giác | 18 phút |
| 3 | Mô hình và thuật toán PageRank | Hoàn thiện mô hình, thuật toán và tính đúng | 28 phút |
| 4 | Tính PageRank trên đồ thị lớn | Biểu diễn và thuật toán phân tán | 22 phút |
| 5 | Chi phí và lợi ích của cách tính | Đánh giá chi phí | 15 phút |
| 6 | Thực hành tính PageRank | Thực hành | 20 phút |
| 7 | Tổng kết và bài tập vận dụng | Tổng kết, kiểm tra, recitation | 7 phút + 60 phút bài tập |

Tổng giảng chính 120 phút; recitation 60 phút. Chưa chốt số slide trước khi lập storyboard chi tiết. Phần 6 có nhãn **Thực hành**; phần chứng minh nâng cao hoặc tối ưu ngoài mạch chính, nếu giữ, có nhãn **Đọc thêm**, ghi thời gian riêng. Không chuyển điều kiện đúng hoặc bước cần để code sang đọc thêm.

### 1. Giới thiệu bài học

**Mạch:** tiêu đề → nội dung → mục tiêu → nhiều trang cùng liên quan một truy vấn → nhu cầu một tín hiệu xếp hạng từ liên kết → đồ thị lớn và phép nhân ma trận–véc tơ đã học.

Trình bày bài toán đầu vào là đồ thị các trang và liên kết, đầu ra là một điểm cho mỗi trang. Phân biệt mức độ quan trọng theo liên kết với mức độ khớp truy vấn. Dùng hình trang web và đồ thị nhỏ; nêu quy mô có nguồn như ví dụ minh họa trong sách, không biến số liệu lịch sử thành hiện trạng Google.

**Sinh viên làm được:** nhận diện dữ liệu, đầu ra và giới hạn của việc dùng ma trận đặc. **Nối sang phần 2:** cần quy tắc biến liên kết thành điểm, chưa cần đưa chuỗi Markov hoặc vector riêng lên slide mở bài.

### 2. Bài toán Xếp hạng trang web

**Mạch:** tình huống xếp hạng → mô tả và đặc tả bài toán → đồ thị ví dụ → tính theo số liên kết vào → chia và nhận điểm → giới hạn của cách tính ban đầu → kiểm tra, nối sang PageRank.

Phần này làm rõ bài toán và xây trực giác bằng phép tính tay. Người lướt ngẫu nhiên, ma trận chuyển, phương trình cân bằng và thuật toán lặp đầy đủ chuyển sang đầu phần 3, sau khi sinh viên đã thấy dữ liệu và cách truyền điểm.

| Slide dự kiến | Nội dung và mục đích | Cách thể hiện |
|---|---|---|
| Bài toán Xếp hạng trang web | Từ một tập trang và các liên kết, tính điểm quan trọng theo cấu trúc liên kết để sắp thứ tự các trang. Phân biệt điểm quan trọng toàn cục với độ khớp một truy vấn cụ thể. | Hình tập trang và liên kết đi vào một bảng thứ hạng; không điền điểm chưa được giải thích |
| Đầu vào và đầu ra | Đầu vào $G=(V,E)$, $n=|V|$, $m=|E|$; cạnh $j\to i$ là trang $j$ trỏ tới $i$. Đầu ra là điểm $r_i\geq0$ cho mỗi trang, quy ước $\sum_i r_i=1$, và thứ tự giảm dần theo điểm; cho phép đồng hạng. Điều kiện chuẩn hóa chưa xác định duy nhất cách chấm điểm; PageRank ở phần 3 sẽ cung cấp quy tắc. | Hai vùng đầu vào–đầu ra, công thức ngắn và nhãn gắn đúng trang; giải thích $n,m,r_i$ ngay khi xuất hiện |
| Ví dụ: Bốn trang web | Đọc đồ thị A, B, C, D của MMDS Hình 5.1; xác định liên kết ra và vào để có đủ dữ kiện tính tay. | Đồ thị lớn với mũi tên rõ; danh sách cạnh ngắn bên cạnh, chưa đưa ma trận |
| Xếp hạng bằng số liên kết vào | Tính được mỗi trang đều có hai liên kết vào, nên cách đếm này cho bốn trang đồng hạng. Đây là quy tắc ban đầu để so sánh, chưa phải PageRank. | Cùng đồ thị và bảng đếm; nhấn rằng đếm liên kết chưa xét điểm của trang nguồn và số đích nó chia sẻ |
| Ví dụ: Chia điểm rồi cộng tại đích | Mỗi trang bắt đầu với $1/4$ điểm và chia đều cho các liên kết ra. Tính một vòng đồng thời từ điểm cũ; theo dõi các phần đóng góp và kiểm tra tổng điểm mới bằng 1. | Một slide tập trung phép tính ở A; một slide tiếp nếu cần để trình bày toàn bộ bảng kết quả. Dùng nhãn phân số trên cạnh, không ghép công thức ma trận vào cùng hình |
| Câu hỏi kiểm tra | Tính lại điểm của D từ các trang trỏ tới D; giải thích vì sao A nhận nhiều điểm hơn dù số liên kết vào bằng các trang khác. | Giữ dữ liệu đồ thị, yêu cầu ngắn; đáp án ở notes. Chốt nhu cầu xác định điểm ổn định và xử lý đồ thị có cấu trúc khác |

**Dữ kiện và phép tính đã kiểm tra:** MMDS Hình 5.1, Ví dụ 5.1–5.2, trang 178–180. Các liên kết: $A\to B,C,D$; $B\to A,D$; $C\to A$; $D\to B,C$. Có $n=4$, $m=8$; bậc ra lần lượt là $3,2,1,2$; mỗi trang có hai liên kết vào.

Khởi tạo $r_A=r_B=r_C=r_D=1/4$. A gửi $1/12$ tới mỗi đích; B và D gửi $1/8$ tới mỗi đích; C gửi toàn bộ $1/4$ tới A. Kết quả một vòng:

| Trang | Các đóng góp nhận được | Điểm mới |
|---|---|---:|
| A | $1/8+1/4$ | $3/8=9/24$ |
| B | $1/12+1/8$ | $5/24$ |
| C | $1/12+1/8$ | $5/24$ |
| D | $1/12+1/8$ | $5/24$ |

Tổng bằng 1; thứ tự sau vòng này là A đứng trước B, C, D đồng hạng. Ghi rõ đây là **kết quả một vòng**, chưa phải điểm PageRank cuối cùng. Không dùng các điểm vừa cập nhật để tính tiếp trang khác trong cùng vòng.

**Sinh viên làm được:** phát biểu đầu vào–đầu ra, đọc đồ thị, tính quy tắc đếm liên kết và một vòng chia/cộng điểm, giải thích sự khác nhau giữa hai cách. **Nối sang phần 3:** dùng chính ví dụ này để định nghĩa mô hình tổng quát và điểm ổn định, sau đó kiểm tra nút cụt và bẫy liên kết.

### 3. Mô hình và thuật toán PageRank

**Mạch:** khái quát ví dụ chia điểm → người lướt ngẫu nhiên → ma trận chuyển và phương trình cân bằng → nút cụt, bẫy liên kết → xử lý từng hiện tượng → quy tắc đầy đủ → thuật toán lặp → ví dụ → tính đúng, hội tụ và dừng → kiểm tra.

Chốt quy ước $M_{ij}$ mô tả chuyển từ trang $j$ tới trang $i$, $r$ là vector cột; dựng từng cột từ ví dụ phần 2 trước khi viết $r=Mr$. Chưa khẳng định phép lặp luôn hội tụ trên mọi đồ thị. Phần hình thức hóa này được chuyển từ phần 2 theo yêu cầu tập trung phần 2 vào bài toán và ví dụ. Thời lượng 18/28 phút của hai phần là dự kiến, cần rà lại khi chốt storyboard từng slide để phần 3 không quá tải.

Dùng các biến thể của Hình 5.1: bỏ cạnh ra của C (Hình 5.3) hoặc thay bằng khuyên tại C (Hình 5.6). Mỗi hiện tượng có hình và bảng điểm riêng. Phân biệt phân phối lại điểm tại nút cụt với xác suất chuyển ngẫu nhiên ở mọi bước.

Chọn một quy ước thống nhất cho cả bài: từ nút cụt chuyển đều tới mọi trang; thêm xác suất chuyển ngẫu nhiên $1-\beta$, với $0<\beta<1$. Sau trực giác mới viết công thức đầy đủ. Ký hiệu $M$ cho ma trận đã xử lý nút cụt, hoặc đổi tên rõ ràng khi cần phân biệt ma trận ban đầu. Không trộn công thức mất khối lượng của sách với diễn giải phân phối xác suất có tổng 1.

Giả mã gồm đầu vào, khởi tạo, một vòng cập nhật, kiểm tra thay đổi và giới hạn vòng lặp. Chứng minh cơ bản giải thích bảo toàn tổng điểm, không âm và tính đúng của một bước; điều kiện hội tụ phải nêu đủ. Không mở đầu bằng định lý phổ, chéo hóa ma trận hoặc cận sai số hậu nghiệm. Phân biệt ngưỡng thay đổi giữa hai vòng với bảo đảm sai số so với nghiệm; nếu chỉ dùng ngưỡng thực hành phải nói rõ.

**Sinh viên làm được:** hoàn thành một vòng PageRank có nút cụt, giải thích vai trò của tham số và đọc được thuật toán đủ để cài đặt. **Nối sang phần 4:** giữ nguyên phép cập nhật, thay biểu diễn và cách tổ chức tính toán.

### 4. Tính PageRank trên đồ thị lớn

**Mạch:** ma trận thưa → danh sách liên kết ra → cập nhật theo cạnh → ma trận/đồ thị chia khối → một vòng MapReduce → gộp cục bộ → chuyển kết quả sang vòng tiếp theo.

Nguồn MMDS 5.2.1–5.2.4; liên hệ trực tiếp bài nhân ma trận–véc tơ của Lecture 02. Đặt đồ thị, một bản ghi danh sách kề và khối ma trận tương ứng cạnh nhau qua các slide, không đặt toàn bộ trên một trang.

Đặc tả phải chỉ rõ Map nhận khối dữ liệu nào, điểm vòng cũ được cung cấp ra sao, `yield` gửi đóng góp cho khóa trang đích nào và Reduce cộng gì. Với quy ước xử lý nút cụt của phần 3, phải chỉ ra pha tính tổng điểm nút cụt và cách đưa nó vào cập nhật; không giả vờ một Reduce tự biết tổng toàn cục. Giữ thông tin cấu trúc đồ thị và cả trang không nhận đóng góp cho vòng tiếp theo. Combine chỉ gộp phần đóng góp cộng được; không gộp nhầm bản ghi cấu trúc.

Hình là luồng của một vòng lặp, có nhãn dữ liệu vào–ra từng pha; vết chạy dùng lại đồ thị nhỏ. Chi tiết chiến lược phân khối khác ở MMDS 5.2.5 đề xuất đọc thêm, không đưa các thuật toán Join/CSDL vào mạch chính.

**Sinh viên làm được:** ánh xạ phép cập nhật thành các pha, giải thích dữ liệu cần giữ giữa hai vòng. **Nối sang phần 5:** đếm công việc và dữ liệu của chính cách tính vừa đặc tả.

### 5. Chi phí và lợi ích của cách tính

**Mạch:** đại lượng cần đo → mô hình và đơn vị → ma trận đặc so với biểu diễn thưa → chi phí mỗi vòng → nhiều vòng → truyền thông, bộ nhớ và giới hạn song song hóa.

Định nghĩa $n$ trang, $m$ cạnh, $t$ vòng, số tác vụ/tài nguyên và độ dài bản ghi khi cần. Bảng đếm nối mỗi số hạng với quét cạnh, lưu vector, truyền khối hoặc gộp đóng góp. So sánh chi phí tính cập nhật đặc và thưa theo cùng mô hình số học; không cộng số byte với số cạnh. Phân biệt bộ nhớ lưu đồ thị với bộ nhớ phụ của một tác vụ.

Thời gian hoàn thành có tải tác vụ nặng nhất, số đợt chạy và các pha phụ thuộc; không mặc định chia tổng phép toán cho số máy. Minh họa cục bộ/gộp trước truyền bằng dữ liệu phần 4. Nêu rõ số liệu là tính từ ví dụ, giả định hay đo thực nghiệm; không biến phần này thành danh sách ký hiệu từ sách.

**Sinh viên làm được:** lập phép đếm theo $n,m,t$, tính một ví dụ và giải thích vì sao thêm máy hoặc Combine chưa chắc giảm thời gian theo cùng tỷ lệ. **Nối sang phần 6:** kiểm tra thuật toán và quan sát số vòng trên một chương trình nhỏ.

### 6. Thực hành tính PageRank

**Mạch:** dữ liệu đồ thị → kết quả mong đợi → biểu diễn Python → hàm cập nhật một vòng → vòng lặp và dừng → chạy → đối chiếu với chạy tay.

Đề xuất Python trên một máy để tập trung vào thuật toán theo hoạt động của buổi gốc 4; chưa cần cài một framework mới. Mã từng slide phải nối với đặc tả phần 3 và biểu diễn thưa phần 4. Giữ cả các trang chỉ xuất hiện ở đích, xử lý nút cụt và trạng thái vòng cũ/mới riêng.

Dùng lại Hình 5.1 và biến thể đã học, kiểm tổng điểm gần 1, không âm, một bước khớp tính tay và điều kiện dừng. Không gọi kết quả trên đồ thị nhỏ là benchmark tăng tốc. Nếu cần thực hành phân tán sau này, mở rộng từ môi trường Compose của Lecture 02; đó là phương án tùy chọn, chưa thuộc triển khai hiện tại.

**Sinh viên làm được:** viết, chạy và kiểm tra chương trình từ đặc tả; giải thích từng đoạn mã. **Nối sang phần 7:** tự lựa chọn biểu diễn và giải các bài nguồn.

### 7. Tổng kết và bài tập vận dụng

Tổng kết bằng chuỗi đồ thị → điểm trên liên kết → sửa mô hình → lặp → biểu diễn thưa/MapReduce → chi phí. Có bảng phân biệt vai trò mô hình, thuật toán, biểu diễn và hệ thống; kết bằng giới hạn của điểm xếp hạng toàn cục để nối Bài 04, chưa giảng biến thể.

Mỗi phần nội dung chính có câu hỏi kiểm tra ngắn. Recitation dự kiến 60 phút từ MMDS, giữ dữ kiện và đồ thị nguồn:

| Bài nguồn | Việc thực hiện | Thời gian dự kiến |
|---|---|---:|
| 5.1.1, trang 187–188 | Tính PageRank Hình 5.7 không có bước chuyển ngẫu nhiên | 15 phút |
| 5.1.2, trang 188 | Tính trên cùng đồ thị với $\beta=0.8$ | 15 phút |
| 5.2.1, trang 195 | Tìm ngưỡng mật độ để biểu diễn thưa tiết kiệm bộ nhớ | 15 phút |
| 5.2.2, trang 195 | Biểu diễn ma trận chuyển của Hình 5.4 và 5.7 theo mục 5.2.1 | 15 phút |

Chốt thời gian sau khi chạy lại lời giải. Không tự thêm yêu cầu code vào đề bài nguồn; phần thực hành có mục tiêu riêng. Lời giải và hướng dẫn chấm sẽ nằm trong notes khi soạn deck.

## Quyết định nguồn và các điểm cần kiểm tra khi soạn

- MMDS Chương 5 là trục và nguồn bài tập. Slide MMDS và Stanford tương đương ở các cụm chính; ưu tiên MMDS. Trực quan ba nút của slide không bắt buộc dùng nếu đồ thị bốn nút trong sách giúp nối ví dụ với bài tập tốt hơn.
- Mô hình/truyền điểm: sách 5.1.1–5.1.2, Hình 5.1, Ví dụ 5.1–5.2. Sửa cách phát biểu hội tụ thiếu điều kiện không chu kỳ trong phần mô hình chưa có bước chuyển ngẫu nhiên; không lặp lại tuyên bố tổng quát sai.
- Nút cụt, bẫy và quy tắc đủ: sách 5.1.3–5.1.5; MMDS slide PDF 38–44, 52; Stanford 41–47, 54. Chọn cách xử lý nút cụt bảo toàn tổng 1 được cả hai bộ slide hỗ trợ; ghi khác biệt với cách taxation cho ma trận thiếu khối lượng ở sách trang 186–187.
- Biểu diễn/tính lớn: sách 5.2.1–5.2.5, trang 190–194; MMDS slide 53–59, Stanford 55–62. Giữ mô hình byte hoặc bit rõ; không áp quy ước số nguyên 4 byte cho chỉ số vượt miền biểu diễn. Các số về RAM từ slide là giả định minh họa nguồn, không phải giới hạn phần cứng hiện nay.
- Soạn từ đầu sau khi duyệt section. Ghi chú bài giảng và hình cũ chưa được đồng bộ với đề xuất; giữ tệp để rà tác động, không dùng làm nguồn chuẩn hay công bố như bản mới.


## Storyboard chi tiết phần 1 — đã kiểm định


Phạm vi: sáu slide, id/introduction. Nguồn chính: MMDS 5.1.1 (trang 176–177), 5.1.6 (trang 187), 5.2.1 (trang 190); quy mô giả định theo Stanford CS246 trang PDF 51. Thời lượng tổng: 10 phút.

## lec03-s01-01 — Trang tiêu đề
- **Id:** lec03-s01-01
- **Tiêu đề:** PageRank: mô hình và tính toán
- **Mục đích:** Định vị bài học trong học phần.
- **Câu chốt:** Bài này xây thước đo quan trọng của trang web dựa trên liên kết và cách tính nó hiệu quả.
- **Trung tâm visual:** Không có hình trang trí.
- **Tiên quyết:** Lecture 02 (phép nhân ma trận–véctơ, MapReduce).
- **Nối vào–ra:** Vào từ MapReduce; ra nối tới phần giới thiệu bài học.
- **Nguồn chính:** MMDS Chương 5 mở đầu.
- **Thời lượng:** 0.5 phút.

## lec03-s01-02 — Nội dung bài học
- **Id:** lec03-s01-02
- **Tiêu đề:** Nội dung
- **Mục đích:** Cho sinh viên thấy tuyến bảy phần của bài.
- **Câu chốt:** Bài đi từ trực giác liên kết, ví dụ tính tay, mô hình/thuật toán, tính trên đồ thị lớn, chi phí, thực hành, rồi tổng kết/bài tập.
- **Trung tâm visual:** Danh sách; hiện chỉ hiển thị "Giới thiệu bài học" vì đang xây từng phần.
- **Tiên quyết:** Slide tiêu đề.
- **Nối vào–ra:** Ra nối tới slide mục tiêu.
- **Nguồn chính:** storyboard-approved.md (tuyến bảy phần).
- **Thời lượng:** 0.5 phút.

## lec03-s01-03 — Mục tiêu học tập
- **Id:** lec03-s01-03
- **Tiêu đề:** Mục tiêu học tập
- **Mục đích:** Nêu ba việc sinh viên làm được sau bài.
- **Câu chốt:** Sinh viên lập được quy tắc tính điểm từ liên kết, tính điểm và chi phí trên đồ thị thưa, và kiểm chứng bằng chương trình Python.
- **Trung tâm visual:** Ba gạch đầu dòng.
- **Tiên quyết:** Không có thuật ngữ chưa định nghĩa (không nêu nút cụt, Markov, eigenvector).
- **Nối vào–ra:** Ra nối tới phần nội dung chính, đối chiếu với slide kết bài.
- **Nguồn chính:** MMDS 5.1, 5.2.
- **Thời lượng:** 1 phút.

## lec03-s01-04 — Xếp hạng các trang kết quả
- **Id:** lec03-s01-04
- **Tiêu đề:** Xếp hạng các trang kết quả
- **Mục đích:** Đặt PageRank vào vị trí đúng trong máy tìm kiếm: một tín hiệu đo độ quan trọng theo liên kết, không phải độ khớp truy vấn, cũng không phải thuật toán xếp hạng duy nhất.
- **Câu chốt:** Độ khớp quyết định trang nào liên quan; PageRank là tín hiệu độ quan trọng đo theo liên kết, hướng tới bước tính điểm.
- **Trung tâm visual:** `img/lec-03/intro-ranking.svg` — sơ đồ truy vấn → các trang liên quan → sắp thứ tự, nhãn vai trò liên kết.
- **Tiên quyết:** Không đưa số liệu trang hay ví dụ lịch sử bịa.
- **Nối vào–ra:** Vào từ mục tiêu; ra tạo nhu cầu đo độ quan trọng → slide quy mô.
- **Nguồn chính:** MMDS 5.1.1 (từ khóa và xếp hạng), 5.1.6 (PageRank là một tín hiệu).
- **Thời lượng:** 2.5 phút.

## lec03-s01-05 — Giới hạn của ma trận đặc
- **Id:** lec03-s01-05
- **Tiêu đề:** Giới hạn của ma trận đặc
- **Mục đích:** Cho thấy vì sao không thể lưu ma trận liên kết dày đặc ở quy mô web; chỉ cần lưu liên kết thực (đồ thị thưa).
- **Câu chốt:** Với n = 10⁹ trang giả định, ma trận đặc cần 8 EB — không phù hợp với RAM một máy thông thường; web thưa nên chỉ lưu liên kết thực.
- **Trung tâm visual:** `img/lec-03/intro-scale.svg` — lưới ô thưa, phần lớn ô trống.
- **Tiên quyết:** Luỹ thừa, đơn vị byte; quy ước 8 byte/ô ghi rõ là quy ước, không phải benchmark Google.
- **Nối vào–ra:** Vào từ nhu cầu đo quan trọng; ra làm tiền đề phần chi phí đồ thị thưa.
- **Nguồn chính:** MMDS 5.2.1 (biểu diễn thưa); quy mô giả định Stanford CS246 trang PDF 51.
- **Thời lượng:** 3 phút.

## lec03-s01-06 — Từ phép nhân đến bài toán xếp hạng
- **Id:** lec03-s01-06
- **Tiêu đề:** Từ phép nhân đến bài toán xếp hạng
- **Mục đích:** Nối công cụ Lecture 02 với bài toán: xác định đầu ra cần tạo (một điểm mỗi trang, thứ tự theo điểm), giữ điểm quan trọng ≠ độ khớp.
- **Câu chốt:** Từ dữ liệu trang và liên kết, kết quả cần tạo là một điểm cho mỗi trang và thứ tự theo điểm; phần 2 mô tả bài toán và ví dụ tính tay.
- **Trung tâm visual:** Hai thẻ đối chiếu công cụ đã học và bài toán sẽ giải; một câu hỏi đầu ra.
- **Tiên quyết:** Lecture 02: nhân ma trận–véctơ, MapReduce.
- **Nối vào–ra:** Vào từ slide quy mô; ra chuyển sang phần 2.
- **Nguồn chính:** Liên hệ công cụ Lecture02 với mục tiêu Bài03 trong sources/source.md; không có số liệu mới ở slide chuyển tiếp.
- **Thời lượng:** 2.5 phút.

## Tài sản
- `render_intro.py` — tạo `intro-ranking.svg`, `intro-scale.svg` ngay thư mục này; SVG chỉ là sơ đồ/nhãn, công thức dùng HTML+KaTeX trên slide.
- Liên kết nguồn trên slide: http://www.mmds.org (nội dung MMDS); không tải asset bên ngoài.
