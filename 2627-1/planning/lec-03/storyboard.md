# Bài 03 — Storyboard triển khai

Trạng thái: Hoàn tất bảy phần, 63 slide (59 slide giảng trong 120 phút và bốn bài tập trong 60 phút), ghi chú tự học và mã Python đã kiểm định. Bản mới thay cấu trúc deck cũ theo yêu cầu.

## Phạm vi và mục tiêu

- Tên bài: **PageRank: mô hình và tính toán**, Bài 03 theo thứ tự đề xuất trong `sources/source.md`; tiếp nối phép nhân ma trận–véc tơ và MapReduce của Bài 02.
- Nguồn chính: MMDS 3e Chương 5, mục 5.1–5.2. Đối chiếu `sources/reference-slides/mmds/ch05-linkanalysis1.pdf` và `sources/reference-slides/stanford-cs246/09-pagerank.pdf`.
- Sinh viên năm 2: biết đồ thị có hướng, xác suất cơ bản và đại số tuyến tính; không giả định đã học chuỗi Markov hoặc cơ sở dữ liệu.
- Đầu ra: giải thích ý nghĩa điểm; lập phép cập nhật; xử lý nút cụt và bẫy liên kết; chạy lặp, kiểm kết quả; mô tả phép tính theo khối/MapReduce; tính chi phí cơ bản và chuyển thuật toán thành Python.
- Để Bài 04 xử lý PageRank theo chủ đề, liên kết rác, TrustRank và HITS. Không mở thêm phần hệ thống Hadoop; dùng lại Bài 02 khi cần.

## Bảy phần của bài giảng

| Phần | Tên trên mục lục | Loại phần | Thời lượng chính dự kiến |
|---|---|---|---:|
| 1 | Giới thiệu bài học | Giới thiệu và động lực | 10 phút |
| 2 | Bài toán Xếp hạng trang web | Phát biểu bài toán, ví dụ và trực giác | 18 phút |
| 3 | Mô hình và thuật toán PageRank | Hoàn thiện mô hình, thuật toán và tính đúng | 28 phút |
| 4 | Tính PageRank trên đồ thị lớn | Biểu diễn và thuật toán phân tán | 22 phút |
| 5 | Chi phí và lợi ích của cách tính | Đánh giá chi phí | 15 phút |
| 6 | Thực hành tính PageRank | Thực hành | 20 phút |
| 7 | Tổng kết và bài tập vận dụng | Tổng kết, kiểm tra, recitation | 7 phút + 60 phút bài tập |

Tổng giảng chính 120 phút; recitation 60 phút. Bản triển khai có 63 slide, phân bổ theo bảy phần: 6, 8, 16, 10, 9, 7, 7. Phần 6 có nhãn **Thực hành**; phần chứng minh nâng cao hoặc tối ưu ngoài mạch chính, nếu giữ, có nhãn **Đọc thêm**, ghi thời gian riêng. Không chuyển điều kiện đúng hoặc bước cần để code sang đọc thêm.

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

## Storyboard triển khai phần 5

# Storyboard Phần 5 — Chi phí và lợi ích của cách tính (Lecture 03)

Tệp: s05.html, s05.css. 9 slide, 15 phút (1, 2, 2, 2, 2, 2, 1, 1, 2).
Nguồn chính: MMDS 5.2, trang 190–194; quy ước chi phí I, H, C theo MMDS 2.5.1 (source-cost-conventions.md); số liệu đã kiểm trong checked-blocks.txt.

## Quy ước ký hiệu (định nghĩa trước khi dùng, dùng nhất quán toàn phần; Markdown chỉ $...$/$$...$$)

- $n$ trang, $m$ liên kết, $k$ dải mỗi chiều, $p$ máy.
- $S$: dung lượng lưu đĩa (byte) của biểu diễn đồ thị. $S_{\text{dense}}=8n^2$; $S_{\text{adj}}\approx 4(n+m)$; $S_{\text{blocks}}=88$ byte cho ví dụ (định dạng khác $S_{\text{adj}}$, nhấn mạnh ở slide 02/04).
- $B$: bộ nhớ RAM một tác vụ cần giữ; $B_{\text{task}}\approx 16n/k+B_{\text{buf}}$.
- $W$: tổng thời gian tính tuần tự theo mô hình giây/cạnh, không phụ thuộc $p$; $W=m\cdot c_e$ cho pha tính đóng góp.
- $T$: thời gian; $c_e>0$ giây/cạnh (giả định). Không dùng τ làm thời gian; τ đã là ngưỡng dừng ở phần 3.
- $I$: đầu vào các Map (byte); $H$: đầu vào Reduce sau Combine (byte); $C=I+H$ — giữ ký hiệu chi phí của Bài 02. Ví dụ: $I=152$, $H=84$ (96 không Combine), $C=236$ (248 không Combine).
- $Q$: byte qua mạng vật lý; $Q$ có thể bằng $I$ hoặc $C$ trong tình huống cụ thể, không đồng nhất về bản chất. $T_{\text{shuffle}}\ge Q/b_{\text{eff}}$, $b_{\text{eff}}$ byte/giây.
- $L$: tổng số vòng đã chạy; $t$: chỉ số vòng. $T_{\text{job}}=T_{\text{setup}}+\sum_t T_{\text{round},t}$.
- Ví dụ chạy xuyên suốt: đồ thị MMDS Hình 5.1, $n=4$, $m=8$, $k=2$, 4 khối, $h=7$ bản ghi nguồn, $q=7$ bản ghi khóa sau Combine. Không nút cụt, mọi đích có inlinks → bỏ seed và δ khỏi ví dụ đếm chi phí core.
- Mọi công thức byte/runtime là mô hình giả định suy từ cấu trúc thuật toán, ghi rõ trong notes; không trình bày như benchmark hay số đo Google.

## Slide

### lec03-s05-01 — 5 · Chi phí và lợi ích của cách tính (1 phút)
- Mục đích: SV gọi tên và phân biệt bốn đại lượng S, B, W, T.
- Câu chốt: bốn đại lượng đo bốn thứ khác nhau; T có thể giảm khi chia việc giữa các máy.
- Trung tâm: 4 cards nhỏ với icon SVG native (đĩa, RAM, phép cộng, đồng hồ).
- Nguồn: MMDS 5.2, trang 190–194.
- Vào: cơ chế chia khối, Map, Combine, Reduce của phần 4. Ra: bộ ký hiệu cho cả phần.
- Tiên quyết: phần 4; ký hiệu n, m, k từ phần 2–4.
- Ghi chú soạn: L được định nghĩa tại slide thời gian cả công việc.

### lec03-s05-02 — Dung lượng biểu diễn đồ thị (2 phút)
- Mục đích: SV tính S_dense và S_adj, giải thích vì sao thưa tiết kiệm khi m≪n².
- Câu chốt: biểu diễn thưa giảm dung lượng từ bậc n² xuống bậc n+m.
- Trung tâm: bảng so sánh 128 vs 48 byte (n=4, m=8).
- Nguồn: MMDS 5.2.1, trang 190; công thức byte là diễn giải từ cấu trúc định dạng.
- Vào: bảng nguồn–bậc–đích phần 4. Ra: nền so sánh với S_blocks ở slide 04.
- Tiên quyết: quy ước float 8 byte, int 4 byte (nêu trên mặt slide).
- Ghi chú soạn: hai biểu thức trong bảng là cùng luận điểm, được phép. Nhấn mạnh 48 byte là biểu diễn toàn cục, không phải S_blocks (khối lặp bậc toàn cục và mã nguồn). Notes đã nói không tính object/header Python.

### lec03-s05-03 — Bộ nhớ của một tác vụ (2 phút)
- Mục đích: SV tính B_task cho một tác vụ khối và nêu đánh đổi theo k.
- Câu chốt: tác vụ chỉ giữ hai dải vector cộng buffer; tăng k giảm RAM nhưng tăng lặp đọc vector.
- Trung tâm: SVG hai dải r_b, z_a và buffer B_buf, nhãn đọc được.
- Nguồn: MMDS 5.2.4, trang 192–194; mô hình giả định.
- Vào: tác vụ M_ab giữ dải vào r_b và dải tích lũy z_a (phần 4). Ra: cơ sở cho I ở slide 04.
- Tiên quyết: giả sử k chia hết n (nêu trên slide).

### lec03-s05-04 — Dữ liệu đầu vào các tác vụ (2 phút)
- Mục đích: SV tính I = S_blocks + 8kn và chỉ ra phạm vi của I.
- Câu chốt: I là tổng đầu vào các Map của block product một vòng, không phải byte qua mạng.
- Trung tâm: công thức I và thẻ ví dụ 88 + 64 = 152 byte.
- Nguồn: MMDS 2.5.1 (định nghĩa chi phí tác vụ); MMDS 5.2.3–5.2.4; checked-blocks.txt.
- Vào: B_task và cấu trúc khối. Ra: I là một nửa của C ở slide 05.
- Tiên quyết: định dạng bản ghi nguồn 4 + bậc 4 + đích 4 byte (chi tiết numeric trong notes, mặt slide giữ I = 88 + 64).
- Ghi chú soạn: h = 7 bản ghi nguồn trải 4 khối (2+2+2+1); S_blocks = 8h + 4m = 88. I chưa gồm δ, seed, đầu ra, I/O job khác. Không đồng nhất I với byte mạng.

### lec03-s05-05 — Combine giảm dữ liệu cần gộp (2 phút)
- Mục đích: SV tính H trước/sau Combine và phân biệt H với Q.
- Câu chốt: Combine giảm H từ 96 xuống 84 byte (12,5% của H, không phải của runtime); H là tổng đầu vào Reduce sau Combine, chưa đương nhiên là Q.
- Trung tâm: SVG hai bản ghi D gộp thành một; bảng 96 vs 84 byte.
- Nguồn: MMDS 5.2.3, trang 192; checked-blocks.txt.
- Vào: Map/Combine phần 4; I ở slide 04. Ra: C = I + H = 236 byte (248 không Combine) — giữ ký hiệu chi phí Bài 02; C chưa gồm δ/Δ/seed/điều phối toàn vòng.
- Tiên quyết: khóa là trang đích, record key 4 + value 8 byte.
- Ghi chú soạn: đếm trên cả 4 khối; Trong cùng M21, A và B tạo hai cặp (D,1/12), (D,1/8), gộp thành (D,5/24). Q chỉ bằng 84/96 nếu mọi record ra Map đều qua mạng, không nén, không retry, không overhead. T_net ≥ Q/b_eff để ở slide 07. Trên đồ thị mẫu không nút cụt nên seed/δ không nằm trong ví dụ đếm core.

### lec03-s05-06 — Thời gian khi tăng số máy (2 phút)
- Mục đích: SV tính T_map theo p và giải thích vì sao tăng tốc 8/3 chứ không phải 4.
- Câu chốt: $W = 8c_e$ không đổi; cận tổng quát $T_{\text{map}}\ge \max(W/p, w_{\max})$, không đẳng thức mọi trường hợp; ở đây $3c_e$ vì khối 3 cạnh là nút cổ chai.
- Trung tâm: một dòng chạy tuần tự và bốn dòng máy bắt đầu đồng thời (8c_e so với 3c_e).
- Nguồn: mô hình tính theo MMDS 5.2.2–5.2.5; c_e tham số giả định.
- Vào: W từ slide 01; công việc bốn khối 2, 2, 3, 1 c_e. Ra: T_map là một số hạng của T_round ở slide 07.
- Tiên quyết: mô hình bỏ I/O và scheduling (nêu trên slide).
- Ghi chú soạn: bài áp dụng p=2 — xếp 3+1 và 2+2 được 4c_e, nêu trong notes. Không đặt hai công thức ngang nhau gây stress; cận dưới nằm trong caption.

### lec03-s05-07 — Dữ liệu qua mạng và băng thông (1 phút)
- Mục đích: tính cận thời gian truyền từ lượng byte và băng thông.
- Câu chốt: Q phụ thuộc vị trí dữ liệu/tác vụ, không đồng nhất I,H,C.
- Trung tâm: T_shuffle ≥ Q/b_eff, định nghĩa đơn vị trước công thức.
- Nguồn: MMDS 2.5.1 và 5.2, mô hình truyền dữ liệu đơn giản.
- Vào: H sau Combine. Ra: số hạng truyền mạng trong thời gian vòng.
- Tiên quyết: byte, giây và các pha phần 4.
- Ví dụ: Q=84 chỉ khi mọi bản ghi phải qua mạng, bỏ nén và phần phụ trội; không phải cận dưới vô điều kiện.

### lec03-s05-08 — Thời gian một vòng và cả công việc (1 phút)
- Mục đích: cộng thời gian các pha và các vòng dưới giả định rõ.
- Câu chốt: thêm máy không giảm đồng đều mọi pha.
- Trung tâm: công thức tổng thời gian một vòng, nhãn giải thích từng thời gian; toàn công việc cộng các vòng và khởi tạo.
- Nguồn: MMDS 5.2 và mô hình pha của bài.
- Vào: T_map và truyền mạng. Ra: câu hỏi áp dụng, rồi kiểm chứng bằng code.
- Tiên quyết: pha delta, Map, chuyển/nhóm, Reduce, đồng bộ. Định nghĩa L và T_setup tại đây.
- Notes: pha chồng nhau dùng max; không tự đặt thời gian pha chưa được cho, không giả định số vòng cố định.

### lec03-s05-09 — Câu hỏi kiểm tra (2 phút)
- Mục đích: SV tự giải ba bài bằng công thức vừa lập.
- Câu chốt (thuần Việt, đúng 1 câu): biểu diễn thưa giảm lưu trữ, trong khối giảm RAM, thêm máy có thể giảm T_map nhưng không giảm mọi chi phí.
- Trung tâm: 3 câu hỏi; đáp án trong notes.
- Nguồn: các công thức slide 02–07.
- Vào: toàn phần. Ra: nối sang phần 6 — chạy kết quả trên đồ thị nhỏ (không phải benchmark).
- Đáp án notes: 32 byte + buffer; 3c_e (tăng tốc 8/3); không suy được I=Q vì I gồm dữ liệu cục bộ và Q phụ thuộc placement, nén, retry, overhead.

## Quyết định sau kiểm tra của điều phối

Bản nháp có sơ đồ Combine sai khối và sai phân số, timeline không thể hiện bốn máy song song, W chưa thống nhất đơn vị, tỷ số dung lượng thiếu hệ số2 và chưa đưa C lên slide. Đã sửa trước khi gửi sáu reviewer. Ba hình chính được vẽ lại bằng render_cost.py thành cost-memory.svg, cost-combine.svg, cost-timeline.svg. Tách slide runtime thành mạng và thời gian cả vòng, tổng thời lượng vẫn15phút. Các ví dụ phân số và byte đối chiếu bằng Fraction. Không coi Q=84 là cận dưới vô điều kiện. Ghi chú bỏ thuật ngữ tiếng Anh không cần và thông tin chỉ dành cho tác giả. Công thức C chỉ tính phép nhân theo khối, không toàn bộ vòng.

## Storyboard triển khai phần 6

# Storyboard Phần 6 — Thực hành tính PageRank (Lecture 03)

Outer: `pagerank-practice`, 7 slide `pr-slide`, id `lec03-s06-01..07`. Tổng 20 phút: 2, 2, 4, 4, 3, 3, 2. Mọi slide có badge Thực hành; dùng CSS của deck (s01.css) và s06.css mới chỉ trong `#pagerank-practice`. Mã là trung tâm của mọi slide, không thêm hình trang trí.

## s06-01 — 6 · Thực hành tính PageRank (2 phút)
- Mục đích: sinh viên nêu được bốn sản phẩm (r tổng 1, trạng thái dừng, số vòng, Δ) và môi trường cần có.
- Câu chốt: đi từ dữ liệu tới chương trình chạy được và kiểm bằng số, một máy, Python 3 chuẩn.
- Trung tâm: hai card — sản phẩm và môi trường; link `materials/lec-03/code/pagerank.py`.
- Tiên quyết: công thức cập nhật đầy đủ phần 3.
- Nối vào: từ kết quả lý thuyết phần 3. Nối ra: dữ liệu cụ thể ở slide sau.
- Nguồn: MMDS 5.1.5; cấu trúc mã của phần này.

## s06-02 — Dữ liệu và giao diện hàm (2 phút)
- Mục đích: đọc được giao diện `pagerank(adj, beta, tol, max_iter)` và điều kiện vào của `adj`.
- Câu chốt: dict chuỗi A→đích, giữ mọi nút, cạnh trùng phải gộp; kiểm tra đầy đủ nằm trong tệp.
- Trung tâm: khối mã dict adj + liệt kê 4 giá trị trả về.
- Tiên quyết: bảng lưu liên kết ra phần 4 (lec03-s04-02).
- Nối vào: giao diện phần 3. Nối ra: mã `step` dùng đúng dữ liệu này.
- Nguồn: MMDS Hình 5.1; đặc tả phần 3.
- Ghi chú soạn: validation đầy đủ để trong tệp, chỉ nêu điều kiện trên caption; không nhét hết lên slide.

## s06-03 — Mã cập nhật một vòng (4 phút)
- Mục đích: đối chiếu từng dòng của `step` với ba thành phần của công thức cập nhật.
- Câu chốt: phần theo liên kết, bước nhảy và bù nút cụt đều dùng điểm cũ; `step` không mutate `r`.
- Trung tâm: khối mã `step` 12 dòng (dưới 30 dòng), khớp chính xác mã chạy trong pagerank.py.
- Tiên quyết: công thức r^{t+1} (lec03-s03-08), quy tắc bù nút cụt (lec03-s03-07).
- Nối vào: δ và common từ công thức. Nối ra: vòng lặp gọi `step`.
- Nguồn: MMDS 5.1.5; slidelec03-s03-08.

## s06-04 — Mã lặp và điều kiện dừng (4 phút)
- Mục đích: theo dõi được vòng lặp, tính Δ và phát hiện trạng thái "hết vòng chưa đạt".
- Câu chốt: tol là ngưỡng độ thay đổi giữa hai vòng, không phải chặn sai số so với nghiệm.
- Trung tâm: khối mã lặp 12 dòng (n, khởi tạo r0 đều, iterations, converged, vòng for, tính Δ, break khi Δ ≤ tol) với r0 đều.
- Tiên quyết: định nghĩa Δ_t (lec03-s03-12).
- Nối vào: một vòng đã có. Nối ra: lệnh chạy thật ở slide sau.
- Nguồn: thuật toán lec03-s03-11, 12.
- Ghi chú soạn: code validation nằm riêng trong tệp, không đưa lên slide.

## s06-05 — Chạy chương trình (3 phút)
- Mục đích: chạy được lệnh đúng từ thư mục 2627-1 và đọc đầu ra JSON.
- Câu chốt: groundtruth base là A = 9/28 ≈ 0.321429, B = C = D = 19/84 ≈ 0.226190.
- Trung tâm: khối lệnh CLI + giá trị hội tụ mong đợi.
- Tiên quyết: giao diện hàm và mô hình cập nhật.
- Nối vào: mã đã đọc xong. Nối ra: các phép kiểm.
- Nguồn: MMDS Hình 5.1; practice-README.md.
- Ghi chú soạn: Mã đã chạy: 20 vòng, delta≈5.4975583e-9; kết quả hiển thị và README khớp.

## s06-06 — Kiểm chứng kết quả (3 phút)
- Mục đích: thực hiện được ba phép kiểm (tổng/dấu, một bước base, một bước dead) với dung sai 1e-12.
- Câu chốt: một bước base cho 7/20 và 13/60; một bước dead cho 1/5 và 4/15 — khớp bảng phần 3.
- Trung tâm: bảng ba phép kiểm và quy tắc abs tolerance.
- Tiên quyết: bảng một vòng và nút cụt phần 3.
- Nối vào: chạy đã xong. Nối ra: câu hỏi kiểm tra về lỗi lập trình.
- Nguồn: MMDS Hình 5.1, 5.3; bảng lec03-s03-09, 10.
- Ghi chú soạn: kiểm toàn node cụt và selfloop đặt trong README/notes, không thêm slide.

## s06-07 — Câu hỏi kiểm tra (2 phút)
- Mục đích: giải thích và sửa ba lỗi: mutate r trong vòng for, bỏ node không inlinks, gán converged True khi hết max_iter.
- Câu chốt: ba lỗi đối ứng ba thành phần vừa xây — một vòng, tập nút, điều kiện dừng.
- Trung tâm: danh sách ba tình huống lỗi; đáp án trong notes.
- Tiên quyết: slides 03–04 của phần này.
- Nối vào: chương trình đã kiểm. Nối ra: tổng kết phần; bài tiếp theo của bài giảng.
- Nguồn: tổng hợp từ phần 3 và mã phần này.

## Đối chiếu nhãn và dữ kiện
- Hướng cạnh nguồn→đích: A→B,C,D; B→A,D; C→A; D→B,C (base); dead bỏ C→A; trap thay C→A bằng C→C — nhất quán pagerank.py, slides, README.
- 7/20, 13/60 (base, một vòng) và 1/5, 4/15 (dead, một vòng) khớp bảng lec03-s03-09/10.
- Groundtruth hội tụ 9/28 và 19/84 lấy từ dữ kiện bài; iterations=20, delta≈5.4975583e-9 đã chạy kiểm chứng.
- beta = 0.8 = 4/5 nhất quán với phần 3.

## Trạng thái sau sáu reviewer
- materials/lec-03/code/pagerank.py đã đồng bộ và khớp hệt bản gốc pagerank.py; test chạy lại trên chính đường dẫn materials, không đổi logic, không thay giá trị 20 vòng, delta≈5.4975583e-9.
- Notes đã rà: không còn mã slide nội bộ lec03-sXX, không lời hẹn "primary điền", không chỉ dẫn người soạn.
- Văn xuôi dùng "véc tơ", "từ điển"; giữ `dict` trong code/thuật ngữ Python.

## Storyboard triển khai phần 7

# Storyboard Phần 7 — Tổng kết và bài tập vận dụng (Lecture 03)

Outer: `summary-exercises`, 7 slide `pr-slide`, id `lec03-s07-01..07`.
Tổng kế hoạch 120 + 60: phần giảng 7 phút (2 + 2 + 3), recitation 60 phút (15 + 15 + 15 + 15).
CSS mới trong s07.css chỉ scoped `#summary-exercises`; không override `.pr-slide` toàn bài.
Thời lượng 15 phút/bài chỉ ở storyboard, không xuất hiện trên mặt slide hay notes.

## s07-01 — 7 · Tổng kết và bài tập vận dụng (2 phút)
- Mục đích: sinh viên nêu được chuỗi liên kết → chia điểm → lặp có bước nhảy → xếp hạng, và giới hạn của xếp hạng theo liên kết.
- Câu chốt: PageRank là một tín hiệu xếp hạng bên cạnh mức phù hợp truy vấn.
- Trung tâm: hai card — chuỗi kết quả đã xây và giới hạn cần nhớ.
- Vai trò: mở phần, đóng vòng động lực của bài giảng.
- Tiên quyết: toàn bộ các phần 2–6.
- Nối vào: kết quả công thức phần 3. Nối ra: công thức gọn ở slide sau.
- Nguồn: MMDS chương 5 (tổng hợp).

## s07-02 — Các bước tính PageRank (2 phút)
- Mục đích: sinh viên trình bày được quy trình tính trong một công thức cập nhật và ba bước.
- Câu chốt: r^{t+1} = βM0r^t + ((1−β)+βδ^t)u; ba bước là lập ma trận chia theo bậc ra (toàn cục), bù nút cụt và bước nhảy, lặp tới ngưỡng; sau khi dừng kiểm tổng điểm và trạng thái dừng.
- Trung tâm: công thức cập nhật có chỉ số vòng t+1 + ba bước.
- Vai trò: hình thức hóa — thu gọn chương trình thành công thức.
- Tiên quyết: M0 theo cột nguồn (lec03-s03-02), bù nút cụt và teleport (lec03-s03-06..08), Δ và τ (lec03-s03-11..12).
- Nối vào: công thức đầy đủ phần 3. Nối ra: bài tập 1–2 giải hệ từ M0.
- Nguồn: MMDS 5.1.4, 5.1.5.
- Ghi chú soạn: chỉ một công thức trung tâm, không nhét toàn chương vào bảng.

## s07-03 — Câu hỏi kiểm tra (3 phút)
- Mục đích: sinh viên trả lời được 4 yêu cầu ngắn đo bậc nguồn, phân biệt nút cụt/bẫy, lý do khớp phân tán–tuần tự, giới hạn tăng tốc theo tỉ lệ máy.
- Câu chốt: bốn câu đối ứng bốn khối kiến thức của bài — mô hình, hai hiệu chỉnh, tính đúng phân tán, chi phí.
- Trung tâm: hai card, mỗi card hai câu.
- Vai trò: kiểm tra; đáp án nằm trong notes, mặt slide không có đáp án hay lời tự hỏi tự trả lời.
- Tiên quyết: phần 3 (mô hình, hiệu chỉnh) và phần 5 (chi phí, tăng tốc).
- Nguồn: phần 3 và phần 5 của bài giảng.

## s07-04 — Bài tập 1: Điểm theo liên kết (15 phút recitation)
- Mục đích: tính PageRank từng trang không bước nhảy (taxation) của Hình 5.7.
- Nguồn: NGUYÊN MMDS 5.1.7, Bài 5.1.1, trang 187–188, Hình 5.7; đề và đồ thị giữ nguyên, link MMDS trên slide.
- Dữ kiện giữ nguyên: a→a, b, c; b→a, c; c→b, c — 7 cạnh, khuyên ở a và c; không nút cụt.
- Output: điểm của 3 trang với tổng bằng 1 và cách tính.
- Câu chốt: giải r = M0r với M0 theo cột nguồn và điều kiện tổng 1 cho (3/13, 4/13, 6/13).
- Hình: `ex-fig-57.svg` vẽ đúng 7 cạnh, khuyên a và c rõ ràng, mũi tên dừng ở biên nút.
- Lời giải trong notes: lập cột a (1/3 tại hàng a,b,c), cột b (1/2 tại hàng a,c), cột c (1/2 tại hàng b,c); hệ ba phương trình + điều kiện tổng; giải r_a = 3r_b/4, r_c = 3r_b/2, điều kiện tổng cho r_b = 4/13; kiểm bằng thay vào từng phương trình.
- Đường giải: notes trình bày đường giải sạch, không để lại vết rà trong quá trình soạn.
- Lưu ý sư phạm: graph không nút cụt, có chu trình và khuyên; hội tụ trên ví dụ này không suy ra mọi graph hội tụ — có thể giải hệ tuyến tính thay vì lặp.
- Thang chấm (notes): ma trận 3đ, hệ + điều kiện 3đ, nghiệm 2đ, kiểm thế vào 2đ.

## s07-05 — Bài tập 2: Thêm bước nhảy (15 phút recitation)
- Mục đích: tính PageRank của cùng Hình 5.7 với β = 0.8.
- Nguồn: NGUYÊN MMDS 5.1.7, Bài 5.1.2, trang 188, cùng Hình 5.7; giữ nguyên đề, link MMDS trên slide.
- Dữ kiện giữ nguyên: cùng 7 cạnh; không nút cụt nên δ = 0.
- Output: điểm của 3 trang; phương trình r = 0.8 M0 r + (1/15)·1.
- Câu chốt: kết quả (7/27, 25/81, 35/81), kiểm lại bằng thế vào từng phương trình.
- Hình: `ex-fig-57.svg` giữ hiển thị đủ.
- Lời giải trong notes: hai phương trình đã khử 11a−6b=1 và 2a+21b=7 (từ hệ ba phương trình + điều kiện tổng); nghiệm duy nhất (7/27, 25/81, 35/81); kiểm thế vào: r_a qua 210/810, r_b qua 250/810, r_c qua 350/810; tổng 81/81.
- Ghi chú soạn: mọi phép rút gọn trong notes phải truy được phép tính; đường giải sạch, không để vết rà soạn thảo.
- Thang chấm (notes): phương trình với β và phần chung 3đ, giải hệ 4đ, kiểm nghiệm cùng chuẩn hóa 3đ.

## s07-06 — Bài tập 3: Ngưỡng lưu ma trận thưa (15 phút recitation)
- Mục đích: thiết lập được ngưỡng tỷ lệ ô 1 để cách liệt kê tọa độ tiết kiệm hơn cách đặc.
- Nguồn: NGUYÊN MMDS 5.2.6, Bài 5.2.1, trang 195; không thêm n/dữ liệu mới; ký hiệu m = số ô 1, ρ = m/n² chỉ giúp đặc tả, không đổi đề.
- Dữ kiện: ma trận Boolean n×n; đặc = n² bit; thưa = 2m·⌈log₂n⌉ bit (2 số nguyên mỗi ô 1).
- Câu chốt: thưa tiết kiệm khi ρ < 1/(2⌈log₂n⌉), điều kiện ngặt với n ≥ 2; trường hợp bằng nhau chưa tiết kiệm; n = 1 là mô hình suy biến (⌈log₂1⌉ = 0) nên so sánh chỉ có nghĩa từ n ≥ 2.
- Lời giải trong notes: hai biểu thức dung lượng, bất đẳng thức 2m⌈log₂n⌉ < n², rút ngưỡng ρ < 1/(2⌈log₂n⌉).
- Thang chấm (notes): hai biểu thức 4đ, bất đẳng thức và ngưỡng 4đ, điều kiện ngặt + bằng nhau 2đ.

## s07-07 — Bài tập 4: Biểu diễn đồ thị (15 phút recitation)
- Mục đích: biểu diễn ma trận chuyển của Hình 5.4 và Hình 5.7 bằng cách mục 5.2.1 (bảng nguồn / bậc ra / đích).
- Nguồn: NGUYÊN MMDS 5.2.6, Bài 5.2.2, trang 195; Hình 5.4 trang 184 và Hình 5.7 trang 188; link MMDS trên slide.
- Dữ kiện giữ nguyên — Fig 5.4: A→B,C,D; B→A,D; C→E; D→B,C; E không có liên kết ra (bậc ra 3, 2, 1, 2, 0). Fig 5.7: a→a,b,c; b→a,c; c→b,c (bậc ra 3, 2, 2).
- Output: hai bảng nguồn, bậc ra, toàn bộ đích; E được liệt kê với danh sách rỗng.
- Câu chốt: hai bảng khớp 8 cạnh Fig 5.4 và 7 cạnh Fig 5.7, kể cả hai khuyên.
- Hình: `ex-fig-54.svg` và `ex-fig-57.svg` vẽ đúng từng cạnh theo chiều nguồn→đích; nhãn Fig 5.4 chữ hoa A–E, Fig 5.7 chữ thường a–c theo nguồn.
- Lời giải trong notes: đầy đủ bảng dữ liệu cả hai hình; nhắc bậc ra của a, b, c là 3, 2, 2; bài không yêu cầu tính PageRank của đồ thị 5 nút.
- Thang chấm (notes): bảng 5.4 (gồm E rỗng) 4đ, bảng 5.7 (gồm khuyên) 4đ, ghi rõ nguồn ảnh 2đ.

## Đối chiếu nhãn và dữ kiện trước bàn giao
- Fig 5.7 (script `render_exercises.py`, hàm fig57): 7 cạnh a→a (selfloop), a→b, a→c, b→a, b→c, c→b, c→c (selfloop) — mỗi cạnh một mũi tên riêng, không gộp cặp ngược chiều; khuyên a và c là cung riêng thấy rõ, mũi tên dừng ở biên nút.
- Fig 5.4 (hàm fig54): 8 cạnh A→B, A→C, A→D, B→A, B→D, D→B, D→C, C→E; E không có cạnh ra.
- Kết quả: (3/13, 4/13, 6/13) không taxation; (7/27, 25/81, 35/81) với β = 0.8 — khớp source-section7.md.
- Ba kết quả beta tổng 81/81; raw tổng 13/13 — kiểm tổng đã làm bằng tay trên từng phương trình.
- Script render chỉ dùng stdlib và `Path(__file__).resolve().parent`; hàm `node(x, y, name)` đúng chữ ký; chưa chạy script, primary thực thi và xem render trước khi duyệt.
- CSS: s07.css scoped `#summary-exercises` toàn bộ; caption 26px, body 28px, nhãn SVG ≥ 28px trong hình 1 cột lớn.


## Sửa trước khi rà độc lập

Điều phối đối chiếu nguồn và sửa hình5.7 bỏ cạnh c→a không có trong sách; khuyên không bị cắt và hàm selfloop gọi đúng chữ ký. Lời giải5.1.1/2 viết lại các bước khử hệ chính xác, không giữ phép biến đổi sai hoặc suy diễn bốn ẩn. Đáp số được chuyển khỏi mặt bài tập vào notes. Bài5.2.1 chỉ yêu cầu mô hình theo n,m,không thêm ví dụ n=1024. Hình5.4 có8cạnh,Hình5.7 có7cạnh. Tổng kết dùng công thức cập nhật có chỉ số vòng và đúng mô hình bù nút cụt; bỏ câu quảng cáo vô nghĩa, không khẳng định mọi điểm dồn vào một bẫy. Thời lượng7+60phút chỉ trongstoryboard; notes có lời giải/thangchấm.

## Bản đồ chủ đề ghi chú tự học


## lec03-note-01 — Giới thiệu bài học
- Vai trò: cốt lõi, xác định tín hiệu liên kết trong bài toán tìm kiếm; mục tiêu và kiến thức đầu vào.
- Kết nối: Bài 02 về nhân ma trận–véc tơ và MapReduce → bài toán xếp hạng ở chủ đề 02.
- Sản phẩm học tập: phân biệt điểm theo liên kết với mức phù hợp truy vấn.
- Nguồn: MMDS 5.1.1–5.1.2; bộ trang chiếu public `lecture-03-pagerank-mo-hinh-va-tinh-toan.html`, phần s01 (lec03-s01-01…06).
- Chu trình rút gọn: phần định hướng, chưa có thuật toán để chứng minh hay phân tích chi phí.

## lec03-note-02 — Bài toán Xếp hạng trang web
- Vai trò: cốt lõi; đầu vào/đầu ra, đồ thị A–D, so sánh đếm cạnh vào với chia điểm theo bậc ra.
- Kết nối: nhu cầu tìm kiếm → vết chạy một vòng → hình thức hóa ở chủ đề 03.
- Sản phẩm học tập: tính được (3/8,5/24,5/24,5/24), phân biệt điểm sau một vòng với nghiệm cuối.
- Nguồn: MMDS 5.1.2, Hình 5.1, Ví dụ 5.1–5.2; bộ trang chiếu public `lecture-03-pagerank-mo-hinh-va-tinh-toan.html`, phần s02 (lec03-s02-01…08).
- Chu trình: đặc tả rồi ví dụ và trực giác; mô hình, thuật toán và chứng minh đầy đủ chuyển sang chủ đề 03 để xử lý nút cụt và bẫy.

## lec03-note-03 — Mô hình đầy đủ: nút cụt, bước nhảy, thuật toán, chứng minh
- Mục tiêu: lập ma trận theo cột nguồn, hiểu phép nhân truyền điểm; phát biểu quy tắc $r^{t+1}=\beta M_0r^t+((1-\beta)+\beta\delta^t)u$; phân biệt nút cụt/bẫy; chứng minh bảo toàn khối lượng và hội tụ (bất đẳng thức tam giác + chuỗi hình học + Cauchy, không Banach); đọc thuật toán với $\tau$, $T_{\max}$, trạng thái trả về.
- Vai trò: cơ chế và lập luận đúng trọng tâm của bài.
- Kết nối vào – ra: vào từ note-02; ra cho phần 4 (chia khối phải tái lập đúng quy tắc này) và phần 6 (code cài đúng công thức).
- Nguồn: MMDS 5.1 và hai bộ slide tham khảo (MMDS 5.1.3–5.1.5, trang 182–187; vết Fraction đã kiểm; chỉ định chứng minh co); bộ trang chiếu public `lecture-03-pagerank-mo-hinh-va-tinh-toan.html`, phần s03.
- Slides liên quan: phần s03, slide lec03-s03-01…lec03-s03-16 (nút cụt, bẫy, teleport, bù δ, quy tắc đầy đủ, bảng một vòng, bảo toàn, hội tụ, thuật toán, dừng).
- Ngoại lệ: quy tắc bù δ khác công thức taxation thiếu khối lượng ở sách trang 186–187 — nguồn là slide MMDS 42/52, Stanford 45/54; cận hậu nghiệm β/(1−β)Δ chỉ đọc thêm; không dùng Banach.

## lec03-note-04 — Tính trên đồ thị lớn: biểu diễn thưa và MapReduce theo khối
- Mục tiêu: lập bảng nguồn–bậc ra–đích; chia $M_0$ thành $k^2$ khối với k dải; đặc tả Map/Combine/Reduce và pha δ; giải thích bản ghi seed (i,0) và snapshot r bất biến; chứng minh tính đúng của cách chia khối.
- Vai trò: tổ chức dữ liệu/phân tán.
- Kết nối vào – ra: vào từ note-03 (quy tắc cập nhật); ra cho phần 5 (chi phí các cấu trúc này).
- Nguồn: MMDS 5.2 (MMDS 5.2.1–5.2.5, Ví dụ 5.7–5.8, Hình 5.11–5.14, trang 190–194); bộ trang chiếu public `lecture-03-pagerank-mo-hinh-va-tinh-toan.html`, phần s04.
- Slides liên quan: phần s04, slide s04-02…s04-09.
- Ngoại lệ: bậc ra trong khối là bậc toàn cục; δ tính một lần; không khẳng định associativity tuyệt đối của float; biến thể 5.2.5 (một hàng khối/tác vụ) chỉ đọc thêm.

## lec03-note-05 — Chi phí: S, B, I/H/C, Q, W, T
- Mục tiêu: tính $S_{\text{dense}}=8n^2$, $S_{\text{adj}}\approx4(n+m)$, $B_{\text{task}}\approx16n/k+B_{\text{buf}}$, $I=152$, $H=84/96$, $C=236/248$ trên n=4, m=8, k=2; phân biệt I với Q, W với T; tăng tốc 8/3 do tác vụ nặng nhất.
- Vai trò: đánh giá và so sánh phương án.
- Kết nối vào – ra: vào từ note-04; ra cho phần 7 bài 5.2.1 (đếm bit cùng kiểu lập luận).
- Nguồn: Quy ước chi phí trong storyboard phần 5 (MMDS 2.5.1 trang 53–54); bộ trang chiếu public `lecture-03-pagerank-mo-hinh-va-tinh-toan.html`, phần s05.
- Slides liên quan: phần s05, slide s05-01…s05-09.
- Ngoại lệ: mọi bytecount là định dạng giả định, không phải Python object size/benchmark; không đồng nhất C với Q; không dùng con số 1Gbps như số liệu hiện nay; c_e là tham số giả định, không dùng τ để kẻ thời gian; T_round/T_job giả thiết các pha không chồng nhau.

## lec03-note-06 — Thực hành: mã pagerank.py
- Mục tiêu: chạy được `pagerank.py`; hiểu `step` là dịch trực tiếp quy tắc phần 3; kiểm tổng ≈1, điểm không âm, một bước tính tay (7/20, 13/60 và 1/5, 4/15); phân biệt δ trong step với Δ dừng; phân biệt số thực lý tưởng với float.
- Vai trò: kiểm chứng công thức.
- Kết nối vào – ra: vào từ note-03; ra cho thói quen kiểm chứng ở các bài sau.
- Nguồn: materials/lec-03/code/pagerank.py, practice-README.md, kết quả kiểm mã ghi trong review-log.md (base 20 vòng, dead 12, trap 34 tại β=0.8, tol=1e-8); bộ trang chiếu public `lecture-03-pagerank-mo-hinh-va-tinh-toan.html`, phần s06.
- Slides liên quan: phần s06, slide s06-01…s06-07.
- Ngoại lệ: chỉ dùng giá trị CLI đã được kiểm, không bịa số vòng; không dùng đồ thị 4 nút để chứng minh speedup; so sánh float bằng dung sai.

## lec03-note-07 — Bài tập và tài liệu
- Mục tiêu: giải được bốn bài MMDS 5.1.1, 5.1.2, 5.2.1, 5.2.2; trình bày lời giải có kiểm nghiệm và chuẩn hóa.
- Vai trò: vận dụng và đánh giá.
- Kết nối vào – ra: vào từ note-03 (bài 1–2), note-05 (bài 3), note-04 (bài 4); ra cho các bài sau về link analysis.
- Nguồn: MMDS 5.1.1–5.1.2, 5.2.1–5.2.2 (bài tập) (nghiệm đã kiểm bằng khử Gauss phân số: 3/13, 4/13, 6/13 và 7/27, 25/81, 35/81); bộ trang chiếu public `lecture-03-pagerank-mo-hinh-va-tinh-toan.html`, phần s07; đề giữ nguyên Hình 5.4 và 5.7.
- Slides liên quan: phần s07, slide s07-04…s07-07.
- Ngoại lệ: hình 5.7 có 5 cạnh giữa các nút + 2 khuyên = 7 cạnh (không cộng kép); hình 5.4 có 8 cạnh; 5.7c không trỏ tới a; bài 5.2.2 không yêu cầu tính PageRank; bài 5.1.2 phương trình của b là 15b=4a+6c+1 (không phải 11b); kết luận tài liệu cuối chỉ dẫn chiếu cụ thể (mmds.org, chương/trang), không tuyên bố trạng thái trang web hiện thời.


## Cập nhật trình bày theo CSS chung (2026-09-17)

Giữ nguyên 63 slide, nội dung và thời lượng. Trang bìa dùng `title-slide` cùng `lecture-title`, `course-name`, `term-name`; mục lục dùng `agenda-slide`. Các trang nội dung dùng lớp động lực/mô hình, ví dụ, chi phí hoặc thực hành đã dùng ở Lecture 02. Cỡ chữ và khoảng cách đặt trong `lecture-style.css`; bố cục PageRank có scope riêng trong cùng tệp. Không giữ khối `<style>` hoặc cỡ chữ nội dòng trong HTML Lecture 03.


## Điều chỉnh trực quan sau đối chiếu Lecture 02 (2026-09-17)

Bản phân tích và quyết định: [visual-revision.md](visual-revision.md). Giữ 63 slide, bảy phần và thời lượng; thay cách thể hiện của 21 slide dưới đây. Nguồn, giả thiết và notes hiện có vẫn áp dụng. Các hàng này thay mô tả bố cục cũ tại đúng ID; không tạo slide mới.

| Mã slide | Mục đích và câu chốt | Trung tâm thể hiện; kết nối vào–ra |
|---|---|---|
| lec03-s01-06 | Nối công cụ đã học với bài toán mới: từ liên kết cần xây quy tắc tính điểm. | Luồng đồ thị → quy tắc → lặp → điểm; chuẩn bị đặc tả phần 2. |
| lec03-s02-02 | Phân biệt dữ liệu đồ thị và điểm chuẩn hóa đầu ra. | Hai vùng có mũi tên; giữ miền, cạnh trùng và đồng hạng. |
| lec03-s03-02 | Lập đúng cột từ các cạnh ra: cột là nguồn, hàng là đích. | Ba cạnh A nối đúng hàng B,C,D trong cột A; hình mới visual-column-a.svg. |
| lec03-s03-03 | Tính cùng một vòng từ điểm cũ. | Bảng điểm cũ/mới nối ví dụ chia điểm với phép nhân ma trận. |
| lec03-s03-04 | Xác định phần điểm bị thiếu khi có nút cụt. | Đồ thị C cụt và thanh 3/4 + phần thiếu 1/4; dẫn tới phép bù. |
| lec03-s03-08 | Ghép ba nguồn thành điểm mới của một trang. | Ba số hạng KaTeX có dấu cộng và vùng kết quả; không lặp lại bằng bullet. |
| lec03-s03-12 | Tính được độ thay đổi giữa hai vòng. | Bảng r1/r2/chênh lệch, phân biệt một trang với ba trang B,C,D. |
| lec03-s03-13 | Giải thích bảo toàn tổng từ ba thành phần. | Công thức tổng quát; thanh ví dụ 3/5 + 1/5 + 1/5 ghi rõ beta/delta. |
| lec03-s03-14 | Hiểu hệ số co đo khoảng cách giữa hai phân phối. | Hai trạng thái qua cùng F; bất đẳng thức và chứng minh notes giữ nguyên. |
| lec03-s03-15 | Nhận ra khóa trang đích trong phép cộng đóng góp. | Bản ghi → nhóm khóa A → tổng 3/8; nối sang tổ chức dữ liệu lớn. |
| lec03-s04-03 | Đọc các phần tử thực thuộc mỗi khối. | Ma trận 4×4 cắt sau B ở hai chiều; hai dải nguồn được cấp tới đúng tác vụ. |
| lec03-s04-04 | Giữ bậc toàn cục khi chia danh sách đích. | Bản ghi A phân sang M11/M21; hàng A được nhấn trong hai bảng. |
| lec03-s04-05 | Chạy Map và Combine trên khối M21. | Giả mã và bảng đầu vào → các cặp Map → các cặp Combine; gộp hai đóng góp cho D. |
| lec03-s04-06 | Cấp đủ dữ liệu để Reduce tạo điểm mọi trang. | Hai nhánh chuẩn bị delta và bản ghi 0; giả mã gộp cuối, phần chung đúng một lần. |
| lec03-s04-08 | Giải thích tại sao chia khối không đổi tổng. | Đẳng thức tổng quát và ví dụ hai tập nguồn cộng tại A; giữ giả thiết điểm cũ cố định. |
| lec03-s05-04 | Tự suy ra I=152 byte từ bốn tác vụ. | Bảng kích thước từng khối và dải điểm; không đồng nhất I với lưu lượng mạng. |
| lec03-s05-07 | Phân biệt đầu vào Reduce với dữ liệu thực sự qua mạng. | Combine ở máy 1 gửi cục bộ hoặc tới máy 2; chỉ nhánh qua mạng góp vào Q. |
| lec03-s05-08 | Ghép thời gian các pha theo giả thiết không chồng nhau. | Timeline có nhãn công việc từng pha; độ dài ô không phải số đo. |
| lec03-s06-02 | Nối dữ liệu dict với các đối số của hàm cập nhật. | Dải adj + r + beta → step → new, giữ giao diện pagerank và điều kiện vào. |
| lec03-s06-04 | Theo dõi điều kiện dừng trong mã. | Mã nguyên vẹn cạnh hai vòng đầu, Delta 0,2 rồi 0,08; chưa đạt 1e-8. |
| lec03-s07-02 | Thu hồi vòng tính bằng đầu vào, thao tác và phép kiểm. | Pipeline có vòng quay lại, công thức véc tơ và kiểm tổng/dấu/trạng thái dừng. |

Bảng và vết chạy mới đều suy trực tiếp từ đồ thị MMDS Hình 5.1 và định dạng byte đã quy định; không đổi bài tập nguồn. Các hình mới có script tái sinh `img/lec-03/scripts/render_visual_revision.py`. Chỉ thêm bố cục có phạm vi Lecture 03 trong CSS chung, không giảm cỡ chữ.


Sau rà soát, s05-05 bổ sung tên gọi C là tổng đầu vào Map và Reduce ngay trong caption; s05-04 định nghĩa Sblocks và nhắc mỗi dải điểm được đọc k lần; s06-04 đặt nhãn `delta đo Δ` cạnh vết chạy. Đây là biên tập làm rõ ký hiệu, không đổi dữ kiện, mã hoặc mục tiêu. Tổng số slide có thay đổi là 22.
