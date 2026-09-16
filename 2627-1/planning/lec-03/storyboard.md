# Lecture 03 — Đề xuất xây dựng lại từ đầu

Trạng thái: đang triển khai bảy phần theo yêu cầu giảng viên. Phần 1–4 có 40 slide đã kiểm định và storyboard chi tiết bên dưới; các phần 5–7 đang triển khai. Chưa hoàn tất toàn deck. Bản mới không lấy cấu trúc, slide hay ghi chú cũ làm khuôn.

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


## Storyboard Phần 2 — "2 · Bài toán Xếp hạng trang web" (Lecture 03)

Trạng thái: đã triển khai theo `storyboard-approved.md` (phần 2 đã sửa) và `source-section2.md`.
8 slide, `id`/`data-slide-id` từ `lec03-s02-01` đến `lec03-s02-08`, mỗi slide là một
inner `<section class="pr-slide">` trong `<section id="web-ranking-problem">`.
Thời lượng: 1/2/2/2/3/3/3/2 = 18 phút.
Hình sinh bằng `render_problem.py`: `graph-pages.svg`, `graph-inlinks.svg`,
`graph-distribute.svg`, `graph-receive.svg`. Style dùng lại `s01.css` (lớp `.pr-slide`);
bổ sung `s02.css` cho cỡ tiêu đề phần và bảng.
Phân vai: phần này chỉ chứa **chuỗi bài toán và trực giác** (phát biểu bài toán, đọc đồ thị,
đếm, chia/cộng điểm); hình thức hóa, chứng minh và thuật toán lặp ở **phần 3**.

| Slide | Mục đích | Câu chốt | Trung tâm | Kiến thức đầu vào | Nối vào–ra | Nguồn | Thời lượng |
|---|---|---|---|---|---|---|---|
| lec03-s02-01 | Phát biểu bài toán: từ mạng liên kết tìm điểm quan trọng rồi sắp thứ tự | Bài toán biến dữ liệu trang/cạnh thành điểm/thứ tự cho mỗi trang | Đồ thị `graph-pages.svg` bên trái; thẻ HTML điểm và thứ hạng bên phải | Nhu cầu tín hiệu xếp hạng từ liên kết của phần 1 (slide s01-04, s01-06) | Vào: kết thúc phần 1; Ra: đặc tả đầu vào–đầu ra slide 02 | storyboard-approved phần 2, mạch | 1 phút |
| lec03-s02-02 | Đặc tả đầu vào–đầu ra của bài toán | Đầu vào $G=(V,E)$, cạnh $j\to i$; đầu ra $r_i\ge 0$, tổng bằng 1, sắp giảm dần, cho phép đồng hạng; chuẩn hóa chưa xác định cách chấm điểm | Hai thẻ đầu vào–đầu ra với công thức ngắn (KaTeX) | Đồ thị có hướng, ký hiệu tập hợp; không giả định CSDL/Markov | Ra: quy ước ký hiệu $n,m,r_i$ dùng cho mọi slide sau; PageRank chốt mô hình ở phần 3 | MMDS 5.1.2 mở đầu | 2 phút |
| lec03-s02-03 | Đọc đồ thị ví dụ, xác định liên kết ra/vào đủ để tính tay | Bốn trang A→B,C,D; B→A,D; C→A; D→B,C; $n=4$, $m=8$ | `graph-pages.svg` (A B trên, C D dưới, 8 mũi tên, 2 chiều tách đường cong) + bảng bậc ra | Ký hiệu $n,m$, cạnh có hướng của slide 02 | Ra: dữ kiện dùng chung phần 2–6 | MMDS Hình 5.1, trang 178 | 2 phút |
| lec03-s02-04 | Tính quy tắc đếm liên kết vào và thấy giới hạn | Mỗi trang đều có 2 liên kết vào nên 4 trang đồng hạng; cách đếm coi mọi liên kết cùng trọng lượng | `graph-inlinks.svg` (2 cạnh vào A đậm) + bảng đếm cả 4 trang | Bảng liên kết ra slide 03 | Ra: động cơ cho quy tắc chia điểm slide 05; không tuyên bố PageRank | MMDS 5.1.2, Ví dụ 5.1 | 2 phút |
| lec03-s02-05 | Hiểu quy tắc chia điểm theo liên kết ra | Mỗi trang chia đều điểm cho các đích; A chia 3 → 1/12 mỗi cạnh; B, D chia 2 → 1/8; C chia 1 → 1/4; tổng phần chia bằng điểm cũ | `graph-distribute.svg`: A phóng to, ba nhãn 1/12 | Điểm khởi tạo 1/4; bậc ra bảng slide 03 | Ra: các phần đóng góp dùng ở slide 06–07 (bảng đóng góp của B, D, C để ở notes/slide 06 tránh quá tải) | MMDS 5.1.2, Ví dụ 5.2 | 3 phút |
| lec03-s02-06 | Cộng các phần đến tại một trang, tránh lỗi chia theo bậc vào | A nhận 1/8 từ B (chia cho bậc ra 2) và 1/4 từ C (bậc ra 1) ⇒ điểm mới 3/8 | `graph-receive.svg`: 2 nguồn B, C → A, nhãn đúng | Quy tắc chia slide 05 | Ra: dòng A của bảng kết quả slide 07 | MMDS Ví dụ 5.2 | 3 phút |
| lec03-s02-07 | Trình bày kết quả một vòng cho cả bốn trang, kiểm tra tổng | A: 1/8+1/4=9/24; B=C=D: 1/12+1/8=5/24; tổng 1; thứ tự A>B=C=D; đây 1 vòng từ điểm cũ đồng đều, tính đồng thời, chưa phải PageRank cuối | Bảng vết chạy (đóng góp → điểm mới), không kèm đồ thị | Kết quả A slide 06; quy tắc chia slide 05 | Ra: căn cứ câu hỏi slide 08; đầu vào cho khái niệm điểm ổn định ở phần 3 | MMDS Ví dụ 5.2, trang 180 | 3 phút |
| lec03-s02-08 | Kiểm tra mục tiêu phần và nối sang phần 3 | Ba yêu cầu (đầu vào/đầu ra; tự tính D; giải thích A cao hơn dù bậc vào bằng nhau); đáp án ở notes; phần 3 cần quy tắc tổng quát, điểm ổn định, xử lý đồ thị khác | Danh sách 3 nhiệm vụ dưới nhãn “Câu hỏi:”; lời chuyển sang phần 3 ở notes | Toàn bộ phép tính slide 02–07 | Ra: chuyển sang phần 3 (mô hình, thuật toán, tính đúng) | MMDS 5.1.2, Ví dụ 5.1–5.2 (dữ kiện; câu hỏi tự soạn) | 2 phút |

## Ghi chú chung

- Notes mỗi slide 80–130 từ, tiếng Việt thuần, không mã slide/thời lượng/hướng dẫn tác giả; câu hỏi có nhãn "Câu hỏi:".
- Không dùng ma trận, chuỗi Markov, vector riêng, xác suất chuyển ngẫu nhiên trên mặt slide; các khái niệm này ở phần 3.
- Không tuyên bố kết quả một vòng là PageRank cuối; nhãn "kết quả một vòng" xuất hiện trên slide 07.
- Phân biệt với cụm trực giác: chứng minh hội tụ, điều kiện đúng và thuật toán lặp thuộc phần 3, đã phân vai trong storyboard-approved.
- Script `render_problem.py` ghi SVG vào thư mục hiện tại khi chạy trong /tmp/lec03-rebuild; khi copy vào `scripts/` của bài, dùng `.parent.parent` để output về thư mục hình. Không sửa SVG thủ công.
- Ghi công: nguồn MMDS 5.1.2, Hình 5.1, Ví dụ 5.1–5.2, trang 178–180, http://www.mmds.org.


## Storyboard Phần 3 — Lecture 03: Mô hình và thuật toán PageRank

- Tệp slide: `s03.html`; style: `s03.css`; hình: `render_model.py` sinh `model-*.svg`.
- Slide 01–16, inner `class="pr-slide"`, `id`/`data-slide-id` = `lec03-s03-01..16`, trong outer `section id="pagerank-model"`.
- Tổng thời lượng: 1+2+2+1+2+2+2+2+2+2+2+2+1+2+1+2 = **28 phút** (đã kiểm).
- Nguồn gốc: MMDS 5.1.2–5.1.5, trang 178–187; slide MMDS 42/52, Stanford 45/54 cho bù điểm nút cụt; chứng minh hội tụ từ nguồn phân tích `source-section3.md`.
- Quy tắc nội dung: mỗi slide một ý chính, không nhét đồng thời hình + giả mã + công thức; mọi phân số đã tự tính lại (vết tính Fraction khớp `source-section3.md`).

| Mã slide | Tiêu đề | Mục đích (SV làm được) | Câu chốt | Trung tâm | Tiên quyết | Nối vào–ra | Nguồn | Thời lượng |
|---|---|---|---|---|---|---|---|---|
| lec03-s03-01 | 3 · Mô hình và thuật toán PageRank | Diễn giải trực giác người đọc chọn đều liên kết ra; đọc r_i là xác suất ở trang i | Lặp phép chia điểm của phần 2 nhiều lần tạo thành mô hình di chuyển | Hình nút j chia r_j/d_j cho các đích | Kết quả một vòng phần 2 (s02-05..07) | Vào: một vòng phần 2. Ra: nhu cầu ma trận hóa | MMDS 5.1.2, tr.178–179 | 1 |
| lec03-s03-02 | Ma trận liên kết | Lập được cột của M0 cho một trang, đúng quy ước cột nguồn / hàng đích | (M0)_ij = 1/d_j nếu j→i, cột j là nguồn, hàng i là đích | Công thức định nghĩa M0 + hình cột A | Bậc ra d_j (s02-03) | Vào: một vòng chia điểm. Ra: viết phép cập nhật dạng nhân ma trận | MMDS 5.1.2–5.1.3, tr.178–182 | 2 |
| lec03-s03-03 | Lặp phép truyền điểm | Chạy tay r^1 = M0 r^0 và nêu mục tiêu tìm r* | r^{t+1} = M0 r^t; mục tiêu là điểm không đổi sau cập nhật; r^1 khớp phần 2 | Công thức lặp + hai vector r0→r1 | Slide 02 | Vào: ma trận M0. Ra: trường hợp mà lặp thô hỏng (04, 05) | MMDS 5.1.2, Ví dụ 5.2, tr.178–179 | 2 |
| lec03-s03-04 | Trang không có liên kết ra | Chỉ ra điểm bị mất khi có nút cụt và vì sao phép chia không xác định | Nút cụt làm phép chia của nó không xác định, một vòng thô mất đúng δ điểm | Hình biến thể C nút cụt + phép tính tổng 3/4 | Slide 03 | Vào: lặp thô. Ra: nhu cầu phân phối lại (07) | MMDS 5.1.4, Ví dụ 5.3, tr.182–183 | 1 |
| lec03-s03-05 | Bẫy liên kết | Nhận diện bẫy một nút và giải thích điểm dồn về C khi lặp thô | Bẫy là nhóm có liên kết ra nhưng không trỏ ra ngoài; lặp thô dồn điểm về bẫy | Hình vòng lặp C→C | Slide 03, 04 | Vào: nút cụt (đối chiếu). Ra: nhu cầu bước nhảy (06) | MMDS 5.1.5, Ví dụ 5.5, tr.185–186 | 2 |
| lec03-s03-06 | Bước nhảy ngẫu nhiên | Mô tả hai nhánh di chuyển tại một bước với β và 1−β | Với xác suất 1−β nhảy đều tới trang bất kỳ; không mất điểm, chỉ đổi nơi đến; chưa xử lý nút cụt | Hình hai nhánh β / 1−β | Slide 05 | Vào: bẫy. Ra: thành phần (1−β)/n trong quy tắc (08) | MMDS 5.1.5, tr.186 | 2 |
| lec03-s03-07 | Phân phối lại điểm ở nút cụt | Định nghĩa δ và giải thích bù βδ/n cho mỗi trang | Điểm gom δ từ nút cụt được chia đều βδ/n; khác bước nhảy áp dụng ở mọi trang | Định nghĩa δ + sơ đồ bù βδ/n (không phải liên kết thật) | Slide 04, 06 | Vào: nút cụt + bước nhảy. Ra: quy tắc đầy đủ (08) | MMDS 5.1.4–5.1.5, tr.183–187; slide MMDS 42/52, Stanford 45/54 | 2 |
| lec03-s03-08 | Quy tắc cập nhật đầy đủ | Gọi tên ba thành phần của công thức và áp dụng từng thành phần | r_i^{t+1} = βΣ r_j/d_j + ((1−β)+βδ)/n; ba thành phần cùng dùng điểm cũ | Một công thức trung tâm + 3 chú thích ngắn | Slide 02, 06, 07 | Vào: β, δ, bước nhảy. Ra: hai ví dụ số (09, 10) | MMDS 5.1.5, tr.186–187; phân biệt taxation thiếu khối lượng trong notes | 2 |
| lec03-s03-09 | Ví dụ: Một vòng có bước nhảy | Tính r^1 trên đồ thị gốc với β=4/5 và δ=0 | A: β·3/8+1/20=7/20; B,C,D: 13/60; tổng 1; khác phần 2 vì có β | Bảng 4 cột: βM0r, (1−β)/n, r^1 | Slide 03, 08 | Vào: quy tắc. Ra: vết số dùng cho Δ ở slide 12 | MMDS 5.1.5, tr.186–187; vết Fraction của bài | 2 |
| lec03-s03-10 | Ví dụ: Một vòng có nút cụt | Tính r^1 khi C cụt, dùng thành phần chung (1−β+βδ)/n | Thành phần chung 1/10; A: 1/5; B,C,D: 4/15; tổng 1 — δ được hoàn lại đầy đủ | Bảng ngắn với cột "Chung" | Slide 04, 08, 09 | Vào: bù δ. Ra: xác nhận bảo toàn (13) | Biến thể từ MMDS Ví dụ 5.3; quy tắc từ MMDS 5.1.5; slide MMDS 42/52, Stanford 45/54 | 2 |
| lec03-s03-11 | Thuật toán tính PageRank | Đọc giả mã, nêu đặc tả vào/ra và vị trí tính Δ trước khi gán r | Thuật toán cập nhật theo danh sách cạnh, dừng khi Δ≤τ hoặc hết Tmax, báo đúng trạng thái | Khối giả mã ~15 dòng (data-trim, language-plaintext) | Slide 08; Δ được định nghĩa ngay trong giả mã | Vào: quy tắc + ngưỡng. Ra: chi phí theo cạnh (15) | Quy tắc MMDS 5.1.5; cấu trúc dừng theo đặc tả phần này | 2 |
| lec03-s03-12 | Độ thay đổi và điều kiện dừng | Tính Δ_t và kết luận dừng cho τ, Tmax cho trước | Δ_t là tổng thay đổi giữa hai vòng, không phải sai số với nghiệm; τ là ngưỡng dừng, Tmax là giới hạn số vòng | Công thức Δ_t + vết r^1, r^2, Δ=2/25 | Slide 09, 11 | Vào: vết số slide 09. Ra: điều kiện dừng đã dùng ở 11 | Đặc tả phần này; số liệu từ vết phân số trên ví dụ MMDS 5.1 | 2 |
| lec03-s03-13 | Bảo toàn tổng điểm | Phát biểu mệnh đề bất biến và giải thích vì sao phần theo liên kết chỉ còn β(1−δ) | Nếu r^t≥0, tổng 1 thì r^{t+1}≥0, tổng 1; ba đóng góp β(1−δ)+βδ+(1−β)=1 | Một đẳng thức tổng ba thành phần, chú thích vai trò dưới mỗi số hạng | Slide 07, 08 | Vào: quy tắc. Ra: nền cho định lý hội tụ (14) | Lập luận từ quy tắc MMDS 5.1.5, tr.186–187 | 1 |
| lec03-s03-14 | Hội tụ của mô hình đầy đủ | Phát biểu kết luận hội tụ và ý nghĩa bất đẳng thức co ‖F(x)−F(y)‖₁ ≤ β‖x−y‖₁ | Với n≥1, β∈(0,1), nhảy đều + bù nút cụt: r* duy nhất — PageRank của mô hình đầy đủ — và dãy lặp hội tụ; không khẳng định cho lặp thô | Một công thức co ánh xạ + caption; chứng minh đầy đủ trong notes | Slide 08, 13 | Vào: bất biến + co. Ra: nền tin cậy cho thuật toán 11 | Chứng minh từ source-section3.md; mô hình MMDS 5.1.5, tr.186–187 | 2 |
| lec03-s03-15 | Từ thuật toán đến dữ liệu lớn | Nối cấu trúc "chia theo cạnh, cộng tại đích" với khuôn MapReduce Bài 2 | Chỉ cần danh sách cạnh, không ma trận dày đặc; một pha phát đóng góp, một pha cộng theo đích | Hình model-collect.svg: hai nguồn B, C trỏ vào A, cộng 1/8+1/4=3/8 | Slide 11; MapReduce Bài 2 | Vào: giả mã theo cạnh. Ra: phần4 tính trên đồ thị lớn | MMDS 5.2 mở đầu (liên hệ, notes ghi rõ dựa trên phép cập nhật) | 1 |
| lec03-s03-16 | Câu hỏi kiểm tra | Tự làm 3 câu: lập cột M0, đối chiếu nút cụt vs bẫy, kiểm dừng | Ba câu kiểm quy ước ma trận, hai trường hợp đặc biệt và quyết định dừng | Danh sách 3 câu hỏi nhãn "Câu hỏi:" | Slide 02–12 | Vào: toàn phần 3. Ra: bài tập/kết phần | MMDS 5.1.2–5.1.5, Ví dụ 5.1–5.6, tr.178–187; đáp án trong notes | 2 |

## Ghi chú sản xuất

- Hình do `render_model.py` sinh tại thư mục chạy script; slide tham chiếu `img/lec-03/model-*.svg` (như quy ước s01/s02). Tích hợp: copy SVG vào `img/lec-03/`.
- `render_model.py` dùng hàm vẽ cạnh nội bộ; tự vẽ đúng self-loop C→C (slide 05) và nút cụt C (slide 04, 07). Không ghi đè tài sản khác.
- Ma trận M0 không hiển thị 4×4 đầy đủ trên slide 02 để giữ một ý chính; sinh viên tự lập các cột còn lại (notes). Nếu muốn thêm 4×4 sau, dùng thứ tự A, B, C, D cùng nhãn hàng/cột rõ.
- Slide 11 dùng `language-plaintext` (không tô màu cú pháp sai), `data-trim`; lưu ý gán `r = new` chỉ sau khi tính Δ.
- Các điểm khẳng định cẩn trọng đã giữ: không nói lặp thô luôn hội tụ (03, 05, 14); Δ không phải sai số với nghiệm (12); kết luận hội tụ chỉ cho mô hình đầy đủ (14).

### Kiểm bản nháp và quyết định của điều phối

Sửa hình cột A thành các cạnh RA A; bù nút cụt tới cả bốn trang, kể cả C. Cột C bằng không không có nghĩa hàng C bằng không: C vẫn nhận từ A,D. Sửa hàng C của bảng ví dụ và toàn bộ lời giải liên quan. Δ giữa vòng1 và2 là 1/25+3×1/75=2/25. Quy tắc trong sách với nút cụt khác quy tắc bù đang dùng; ghi đúng khác biệt. Thuật toán quét n+m, không chỉ m. Giữ chuẩn một và chứng minh co trong notes, không đưa Banach lên mặt slide. Rút câu hỏi cuối, bỏ thông tin quy trình khỏi notes. Bỏ hình thanh tổng để công thức bảo toàn làm trung tâm; dành hai phút cho ý tưởng hội tụ.

Hình chuyển tiếp phần3 dùng model-collect.svg với nhãn “tổng đóng góp 3/8”, không tái dùng nhãn “điểm mới 3/8” của phần2 để tránh nhầm với PageRank đầy đủ 7/20. Quan hệ B→A1/8 và C→A1/4 giữ nguyên.


## Storyboard triển khai phần 4

# Storyboard Phần 4 — Tính PageRank trên đồ thị lớn (Lecture 03)

Phạm vi: MMDS 5.2.1 (tr.190), 5.2.3 (tr.191–192), 5.2.4 (tr.192–194); tổng quan thưa MMDS slide 53 (tương đương Stanford 55, ưu tiên MMDS). 10 slide `lec03-s04-01..10`, outer `id="large-graph"`. 22 phút, thứ tự phút: 1, 2, 3, 2, 3, 3, 3, 2, 1, 2. Phần 5 sẽ phân tích chi phí chi tiết; phần này chỉ nêu giới hạn RAM và không đưa con số chi phí vào mạch chính (gộp hàng block 5.2.5 chỉ xuất hiện trong notes slide 09 như một lựa chọn).

Ký hiệu chung theo phần 3: $M_0$ ma trận liên kết (cột $j$ nguồn, hàng $i$ đích), $(M_0)_{ij}=1/d_j$ khi có cạnh $j\to i$; $d_j$ là bậc ra toàn cục; $\delta=\sum_{j:d_j=0}r_j$; công thức $r_i^{t+1}=\beta\sum_{j:j\to i}r_j^t/d_j+((1-\beta)+\beta\delta^t)/n$. Dữ kiện đồ thị: A→B,C,D (d=3); B→A,D (d=2); C→A (d=1); D→B,C (d=2). Bảng đóng góp $k^2$ đã kiểm Fraction trong checked-blocks.txt (m=8, n=4, k=2; M11: A,d3,[B]; B,d2,[A]; M12: C,d1,[A]; D,d2,[B]; M21: A,d3,[C,D]; B,d2,[D]; M22: D,d2,[C]).

Quyết định riêng của phần này (không phải trích nguồn, ghi rõ): bù $\delta$ và bộ bản ghi khởi tạo $(i,0)$ là bước hoàn thiện để đưa mô hình phần 3 vào cấu trúc MapReduce của MMDS; lập luận tính đúng (slide 08) xây từ cách chia khối đã chọn. Không dùng con số n=10 tỷ với id 4 byte (tràn); phần5 nêu định dạng và phạm vi mã trang trước khi tính byte.

Hình SVG do render_large.py ghi cạnh script (bản phát hành ghi vào thư mục hình của bài), tên model `rlarge-*.svg`, primary sẽ chạy script và đặt vào `img/lec-03/` theo đúng đường dẫn trong s04.html.

---

## lec03-s04-01 — “4 · Tính PageRank trên đồ thị lớn” (1 phút)

- **Mục đích**: SV chỉ ra vì sao ma trận đặc không phù hợp khi $m\ll n^2$ và nêu hai nhiệm vụ của phần (cách lưu, cách chia việc).
- **Câu chốt**: thông tin thực chỉ là $m$ cạnh; lưu cả ô 0 là lãng phí khi ma trận thưa.
- **Vai trò**: mở phần, nêu vấn đề.
- **Đầu vào**: phép cập nhật đầy đủ phần 3 (slide s03-08).
- **Nội dung**: h1; nhiệm vụ tổ chức lưu trữ và tính toán; card nêu $n$ trang, $m$ liên kết, so sánh ma trận đặc chứa cả 0 với danh sách liên kết (không benchmark, không số byte).
- **Kết nối**: vào từ phần 3; ra cho slide 02 (cách lưu thưa).
- **Kiểm tra/notes**: không đưa số liệu liên kết trung bình như hiện trạng Web; nhấn $m\ll n^2$.
- **Nguồn**: MMDS 5.2, tr.189–190.

## lec03-s04-02 — “Lưu các liên kết ra” (2 phút)

- **Mục đích**: SV đọc bảng (nguồn, $d_j$, đích) và suy ra giá trị $1/d_j$ của ô khác không.
- **Câu chốt**: mỗi cột chỉ cần bậc ra và danh sách đích; không cần lưu từng $1/d_j$.
- **Vai trò**: giải thích cơ chế biểu diễn thưa.
- **Đầu vào**: định nghĩa $d_j$, cột nguồn của $M_0$ (s03-02).
- **Nội dung**: bảng MMDS Fig 5.11 đúng A d3 BCD; B d2 AD; C d1 A; D d2 BC. Nút cụt giữ bản ghi $d_j=0$, danh sách rỗng. Ví dụ 4 node không quá thưa — chỉ minh họa cách ghi.
- **Kết nối**: vào slide 01; ra cho slide 04 (bản ghi trong khối).
- **Nguồn**: MMDS 5.2.1, Ví dụ 5.7, Fig 5.11, tr.190.

## lec03-s04-03 — “Chia ma trận và véc tơ thành khối” (3 phút)

- **Mục đích**: SV chỉ ra tác vụ $M_{ab}$ nhận dải $r_b$ nào và đóng góp cho dải đầu ra $a$ nào.
- **Câu chốt**: chia hai chiều thành $k^2$ khối để mỗi tác vụ chỉ giữ dải đầu vào và dải tích lũy đầu ra trong RAM.
- **Vai trò**: trực giác → hình thức hóa cách chia.
- **Đầu vào**: $z=M_0r$; giới hạn RAM nêu ở slide 01.
- **Nội dung**: dòng định nghĩa đầu tiên: đặt $z=M_0r$; chia $r$ thành $k$ dải và $M_0$ thành $k^2$ khối; ví dụ $k=2$, nguồn A,B và C,D. SVG `rlarge-blocks-grid.svg`: hai khung nét đứt nhóm khối theo cột nguồn — khung cột 1 chứa $M_{11},M_{21}$, khung cột 2 chứa $M_{12},M_{22}$; $r_1$ (nguồn A,B) và $r_2$ (nguồn C,D) có mũi tên thẳng vào khung cột tương ứng, nhãn nguồn đặt ngay trong hộp $r$; mỗi hàng khối có một mũi tên gộp về dải $z_a$ tương ứng. Khung nét đứt chỉ nhóm, không là cạnh dữ liệu. Ma trận đọc stream, không ôm nguyên block.
- **Kết nối**: vào slide 02; ra cho slide 04 (khối cụ thể) và 05 (map/combine).
- **Notes**: động lực: nếu chỉ chia cột, đầu ra véc tơ $z$ dài bằng $r$ nên combining tại task không vừa RAM → truy cập đĩa dồn dập; chia 2 chiều khắc phục.
- **Nguồn**: MMDS 5.2.3, Fig 5.12, tr.191–192.

## lec03-s04-04 — “Dữ liệu trong một khối” (2 phút)

- **Mục đích**: SV viết đúng bản ghi của một khối, giữ bậc toàn cục và đặt mỗi cạnh vào đúng một khối.
- **Câu chốt**: bậc ra trong khối là bậc toàn cục; mỗi cạnh thuộc đúng một khối.
- **Vai trò**: đặc tả biểu diễn khối, ví dụ nhỏ.
- **Đầu vào**: bảng Fig 5.11 (slide 02), lưới khối (slide 03).
- **Nội dung**: 2 card phóng $M_{11}$ (A d3 → B; B d2 → A) và $M_{21}$ (A d3 → C,D; B d2 → D), đúng Fig 5.14(a),(c). Toàn cục $d_A=3$ giữ nguyên ở cả hai. $M_{12}$ (C d1 A; D d2 B) và $M_{22}$ (D d2 C) chỉ trong notes; không nhét bảng 4 khối vào slide.
- **Kết nối**: vào slide 03; ra cho slide 05 (Map nhận khối và dải điểm, duyệt từng bản ghi).
- **Nguồn**: MMDS 5.2.4, Ví dụ 5.8, Fig 5.13–5.14, tr.192–193.

## lec03-s04-05 — “Map và Combine trên một khối” (3 phút)

- **Mục đích**: SV theo dõi một bản ghi nguồn qua Map và Combine, viết được cặp (khóa, giá trị) phát ra.
- **Câu chốt**: Map tạo $(i, r_j/d_j)$ cho mỗi đích; Combine chỉ gộp tổng tại tác vụ, đầu ra thô chưa nhân $\beta$.
- **Vai trò**: giả mã cơ chế.
- **Đầu vào**: bản ghi khối (slide 04), dải $r_b$ (slide 03).
- **Nội dung**: mã sáu dòng `data-trim language-plaintext` (map, combine); dùng yield tạo một bản ghi cho mỗi đích, đúng một lần qua task — không giả định mọi id có trong khối (chi tiết ở notes slide 06).
- **Kết nối**: vào slide 04; ra cho slide 06 (reduce + δ).
- **Notes**: tổng trong toán học kết hợp/giao hoán; số thực máy tính có rounding → kiểm bằng tolerance.
- **Nguồn**: MMDS 5.2.3, tr.191–192.

## lec03-s04-06 — “Reduce và điểm ở nút cụt” (3 phút)

- **Mục đích**: SV tính được đầu ra Reduce cho một id, kể cả id không có in-link.
- **Câu chốt**: Reduce trả $\beta z_i+((1-\beta)+\beta\delta)/n$; bản ghi khởi tạo $(i,0)$ bảo đảm mọi nút có bản ghi đầu ra.
- **Vai trò**: hoàn thiện thuật toán với trường hợp biên nút cụt.
- **Đầu vào**: đầu ra Combine (slide 05); $\delta$ phần 3.
- **Nội dung**: $\delta$ là tổng điểm của CHỈ các trang không có liên kết ra, mỗi trang nguồn được tính đúng một lần (không cộng điểm mọi trang), rồi gửi giá trị tới các tác vụ Reduce; mã Reduce(i,L_i), L_i là danh sách đóng góp hoặc tổng từng phần; bản ghi khởi tạo $(i,0)$.
- **Kết nối**: vào slide 05; ra cho slide 07 (ví dụ gộp).
- **Notes**: có thể vẽ sơ đồ pipeline δ → common term + grouped contributions → Reduce; mỗi nút phải có bản ghi đầu ra; công thức đầy đủ đã có ở s03-08.
- **Nguồn**: mô hình phần 3 (hoàn thiện của người soạn) + MMDS 5.2.2–5.2.3.

## lec03-s04-07 — “Ví dụ: Gộp hai khối tại A” (3 phút)

- **Mục đích**: SV tính lại $z_A$ và $r_A^1$ từ đóng góp của hai khối khác nhau.
- **Câu chốt**: hai khối cùng phát tới khóa A, gộp trước khi nhân $\beta$ và cộng phần chung.
- **Vai trò**: vết chạy ví dụ.
- **Đầu vào**: dữ liệu khối $M_{11}$, $M_{12}$; $r^0$ đều 1/4; $\beta=4/5$; đồ thị gốc ($\delta=0$).
- **Nội dung**: SVG `rlarge-merge-a.svg` (2 task → A) + HTML: B→A cho 1/8, C→A cho 1/4; nhóm [1/8, 1/4]; $z_A=3/8$; $r_A^1=7/20$.
- **Kết nối**: vào slide 06; ra cho slide 08 (tính đúng tổng quát).
- **Notes**: ba đích còn lại có $z=5/24$, $r=13/60$. Không đưa 1/5 (thuộc biến thể nút cụt, đồ thị khác).
- **Nguồn**: MMDS Ví dụ 5.7–5.8 cho dữ liệu khối; phép tính vòng khớp bảng s03-09.

## lec03-s04-08 — “Tính đúng của cách chia khối” (2 phút)

- **Mục đích**: SV nêu được vì sao kết quả phân tán bằng phép cập nhật tuần tự.
- **Câu chốt**: mỗi cạnh tạo $r_j/d_j$ đúng một lần; Combine và Reduce chỉ đổi nhóm tổng.
- **Vai trò**: lập luận đúng.
- **Đầu vào**: map/combine (05), reduce/δ (06).
- **Nội dung**: gọi $V_b$ là tập trang nguồn trong dải b; đặc tả kết quả phân tán = cập nhật tuần tự trên số thực chính xác; đẳng thức $\sum_{b=1}^{k}\sum_{j\in V_b:j\to i}r_j/d_j=\sum_{j:j\to i}r_j/d_j$; δ đếm 1 lần; common chỉ cộng 1 lần/i sau group.
- **Kết nối**: vào slide 07; ra cho slide 09 (tổ chức vòng).
- **Notes** (~120 từ): input snapshot cố định; không retry double count (hệ thống chọn đầu ra task thành công như Bài 2); không claim associativity cho floating point.
- **Nguồn**: MMDS 5.2.3–5.2.4; lập luận hoàn thiện của mô hình đã chọn.

## lec03-s04-09 — “Tổ chức một vòng tính” (1 phút)

- **Mục đích**: SV sắp xếp đúng thứ tự các giai đoạn của một vòng.
- **Câu chốt**: snapshot $r^t$ chốt trước, véc tơ mới chỉ dùng khi vòng xong; $k^2$ là số task, không phải số máy.
- **Vai trò**: tổng hợp quy trình.
- **Đầu vào**: tất cả các bước trước.
- **Nội dung**: SVG `rlarge-round-pipeline.svg` (sáu giai đoạn; trường hợp 2 máy / 4 tác vụ nêu ở caption): snapshot $r^t$ → δ aggregation + block tasks → Combine → chuyển và nhóm theo khóa → final reduce → Δ global → $r^{t+1}$.
- **Kết nối**: vào slide 08; ra cho câu hỏi kiểm tra và phần 5.
- **Notes**: toàn graph/$d_j$ giữ cho vòng sau (không xóa list kề trong reduce); δ giá trị chạy song song block product nhưng phải xong trước final reduce. Gộp hàng block (5.2.5) là lựa chọn khác, chỉ nêu ở notes, không bắt SV nắm thêm.
- **Nguồn**: MMDS 5.2.2–5.2.4, tr.191–194.

## lec03-s04-10 — “Câu hỏi kiểm tra” (2 phút)

- **Mục đích**: SV tự kiểm 3 điểm: bậc toàn cục trong khối, bản ghi khởi tạo/common cho đích không in-link, phân biệt task và máy.
- **Câu chốt**: ba câu phủ ba quyết định chính của phần.
- **Vai trò**: kiểm tra.
- **Nội dung**: 3 câu trên slide; đáp án trong notes: A ghi d=3 trong $M_{21}$; đích không in-link nhận phần chung $(1-\beta+\beta\delta)/n$ qua bản ghi khởi tạo $(i,0)$; $k^2=4$ task trên 2 máy (mỗi máy 2 tác vụ là một cách phân bổ).
- **Kết nối**: ra — phần 5 nhu cầu so RAM / bytes / runtime; hộp source-note đã ghi chuyển tiếp.
- **Nguồn**: tổng hợp phần 4.

---

## Kiểm tra chéo đã làm

- Chiều nguồn→đích nhất quán: bảng theo cột nguồn, $(M_0)_{ij}$ từ $j$ đến $i$; $M_{11}$ đích A/B, $M_{21}$ đích C/D khớp Fig 5.14(a)/(c) và checked-blocks.txt.
- Số học: 1/8 + 1/4 = 3/8; (4/5)(3/8) + 1/20 = 3/10 + 1/20 = 7/20 ✓ (khớp Fraction step 1 phần 3).
- Không có con số chi phí (byte/RAM/runtime) trên slide core; phần 5 đảm nhận. Không dùng id 4 byte với n=10 tỷ.
- Font: thân ≥28, mã 24, caption 26, formula KaTeX HTML; SVG role="img" + alt; CSS mới bọc trong `#large-graph`, không đụng `.pr-slide` toàn bài, không lặp s01.css.
- Không có câu hướng dẫn tác giả trong notes hay mặt slide.

### Điều chỉnh sau bản nháp

Sửa chữ và khái niệm đột ngột (giá trị delta, bản ghi khởi tạo); Map nhận cả khối, duyệt bản ghi rồi yield; Reduce nhận danh sách có thể gồm tổng từng phần. Bổ sung tập $V_b$ để công thức tổng không dùng chỉ số b như tập hợp. Giữ Combine trước khi chuyển/nhóm dữ liệu. Mỗi dải điểm được k tác vụ dùng, không đồng nhất k lần đọc với k lần truyền mạng. Bỏ câu hỏi tu từ và số liệu trung bình Web không cần thiết. Script hình bản nháp có hàm chữ sai tham số và ghi vào thư mục con ngoài đường dẫn tích hợp; điều phối đã sửa, vẽ rõ dải nguồn cấp cho cả cột khối và hàng khối gộp về dải đích.
