# Nhật ký rà soát Bài 6

## Quyết định nguồn và biên tập

- MMDS là nguồn chính cho §3.4, các độ đo, vân tay và ba bài tập. Stanford CS246 bài 04 chỉ cung cấp cách trình bày từ họ cơ sở đến khuếch đại ở §§3.6–3.7; mọi công thức đã đối chiếu sách.
- Sửa lỗi trên slide MMDS: giá trị dùng trong phép tính là $s=0.3=30\%$, không phải $0.3\%$. Lỗi này đã được điều phối viên xác minh trực tiếp trên slide MMDS trang 50.
- Không dùng xấp xỉ $(1/b)^{1/r}$ như đẳng thức. Deck suy ra $s_{1/2}=(1-2^{-1/b})^{1/r}$ và xấp xỉ lớn-$b$ là $(\ln2/b)^{1/r}$.
- Định nghĩa họ LSH dùng xác suất theo $h\sim F$, $\alpha_1>\alpha_2$; không phát biểu gì cho $d_1<d<d_2$.
- Khóa dải là $(\ell,\text{toàn bộ vector dải})$. Nếu hiện thực bằng mã băm, phải kiểm tra hai khóa có bằng nhau hay không; không dùng giả thiết “đủ nhiều ngăn” thay cho tính đúng.
- Cosin dùng pháp tuyến đẳng hướng, có thể lấy Gaussian; vector $\{\pm1\}^d$ chỉ là xấp xỉ. Trường hợp tích vô hướng bằng 0 có quy tắc gán cố định; với Gaussian liên tục, biến cố này có xác suất 0 cho vector khác 0 cố định.
- Euclid dùng độ dịch độc lập $u\sim U[0,a)$ để không trùng với ngưỡng hậu kỳ $\tau$. Công thức $\max(0,1-|\delta|/a)$ chỉ là xác suất theo $u$ khi hướng chiếu đã cố định; xác suất đầy đủ còn lấy trung bình theo hướng Gaussian. Nguồn: MMDS §§3.7.4–3.7.5 và Datar et al., 2004, DOI `10.1145/997817.997857`. Gaussian là trường hợp riêng của họ phân phối ổn định dùng cho chuẩn L2; không thêm công thức Datar ngoài nguồn đã có.
- Ví dụ vân tay được gọi là phép tính trong mô hình MMDS, dựa trên giả thiết độc lập; không mô tả là kết quả thực nghiệm hiện thời. Kết quả “không” đi vào ngăn đơn riêng, không vào một ngăn “không” chung.
- Không tuyên bố diện tích dưới đường cong chữ S là tỷ lệ lỗi của kho dữ liệu; đó chỉ là xác suất có điều kiện theo một cặp có độ tương đồng $s$.
- Không tuyên bố thời gian $O(1)$ hay $O(N)$ nếu thiếu mô hình ngăn. Chi phí ghi theo $A=\sum_B\binom{|B|}{2}$ và trường hợp xấu $\Theta(bN^2)$.
- Với $p=br$ cố định, tăng $r$ và giảm $b$ làm $q(s)$ giảm với mọi $0<s<1$: va chạm sai giảm nhưng xác suất bỏ sót tăng ở mọi mức tương đồng chưa bằng 1.

## Sai khác có chủ ý

- Tách thuật toán tạo ứng viên khỏi phân tích xác suất. Thứ tự đã sửa thành luồng trực giác → vết chạy → kiểu và giả mã → bất biến giai đoạn sinh cặp → chi phí, bộ nhớ và đối chiếu hậu kỳ.
- Bài tập được dịch và chia thành nhiều trang để đủ thời lượng; dữ kiện và yêu cầu toán học giữ nguyên. Mọi đáp án và hướng dẫn chấm chỉ ở notes.
- Chỉ đưa ba họ Hamming, cosin và Euclid có trong phạm vi; không thêm HNSW, PQ hoặc nội dung Bài 7.
- Cấu trúc section: gộp P+M thành mở bài, gộp B+Q thành phân dải và xác suất, giữ A, giữ F, gộp D+V thành ứng dụng/độ đo, tách C00 thành section kết luận riêng, R riêng. Không đổi `data-slide-id`.

## Xử lý phản biện sau bản nháp

- **Chặn bàn giao — B02:** đổi vector dải 3 của $D_3$ từ $(6,3)$ thành $(6,9)$. Sau sửa, chỉ $D_1,D_2$ trùng trọn dải 2; hai cặp còn lại không trùng trọn dải nào. Ghi chú không còn mâu thuẫn với bảng.
- **Nghiêm trọng — A01–A04:** A01 chuyển từ kiểu dữ liệu sang luồng trực giác; A02 giữ vết chạy; A03 gom điều kiện trước, kiểu khóa và giả mã; A04 chỉ phát biểu bất biến trên $t$ ngăn đã được gom xong. Ghi chú A04 tách rõ giai đoạn một xây ngăn và giai đoạn hai sinh cặp.
- **Nghiêm trọng — A05:** bỏ lời giải hai công việc MapReduce khỏi phần giảng. Trang tách chi phí tạo ứng viên thực tế $\Theta(pN+A)$, kỳ vọng $\Theta(pN+\mathbb E[A])$ dưới mô hình bảng băm, bộ nhớ khóa tham chiếu $O(bN+|C|)$, khả năng $O(pN)$ khi vật hóa khóa và chi phí đối chiếu chữ ký $O(p|C|)$. Thiết kế hai công việc vẫn là nhiệm vụ của Bài tập 3.4.4.
- **Nghiêm trọng — Q04:** chỉ gọi $q(s)$ là đường cong chữ S khi $b>1$ và $r>1$; mô tả thay thế là đường xác suất.
- **Nghiêm trọng — F01–F05:** thêm MMDS Ví dụ 3.18 trước định nghĩa; dùng $\rho$ cho xác suất va chạm để không trùng $p=br$; F05 chỉ kiểm tra nghĩa AND/OR và không đưa chuỗi số hoặc đáp án của Bài tập 3.6.1.
- **Nghiêm trọng — D01–D04:** dùng $m$ cho số chiều; thêm điều kiện $x,y\ne0$ và pháp tuyến bất biến quay cho công thức cosin; thay độ dịch $\tau$ bằng $u$ ở Euclid; hạ tuyên bố Euclid về xác suất có điều kiện theo hướng chiếu và bổ sung nguồn Datar et al.
- **Trung bình — hậu kiểm:** phân biệt rõ đối chiếu chữ ký chỉ cho ước lượng MinHash, còn đối chiếu tập shingle hoặc dữ liệu gốc mới cho Jaccard chính xác; đồng bộ M00, M02, A05 và C00.
- **Trung bình — F02, D03–D04, R07–R08:** bổ sung miền $0\le\alpha_2<\alpha_1\le1$; đưa $v\sim\mathcal N(0,I_m)$ và tính độc lập với $u$ lên mặt trang; nêu rõ độc lập giữa ô, giữa hai dấu khác ngón và giữa các hàm OR theo mô hình bài tập.
- **Nghiêm trọng — V01:** bỏ các xác suất cơ sở, kết quả OR 1024 và AND của hai nhóm. Trang chỉ nêu chiều đánh đổi; toàn bộ phép tính vẫn thuộc Bài tập 3.8.2.
- **Trung bình — bài tập:** R02 không chấm yêu cầu xử lý va chạm mã băm như một mục ngoài đề; R06 bỏ yêu cầu chứng minh không giao hoán và chỉ chấm hai công thức (c), (d) của nguồn. Các khung chia bước không đổi dữ kiện hoặc yêu cầu toán học.
- **Trung bình — thuật ngữ và mạch học phần:** Việt hóa `band` thành “dải”, `bucket` thành “ngăn”, `exact` thành “đầy đủ”; P00 viết đầy đủ băm nhạy cảm cục bộ trước LSH; thêm P02 nêu hành trình; C00 nối sang Bài 7 nhưng không dạy trước HNSW hoặc PQ.
- **Khả năng đọc:** tăng cỡ chữ và Việt hóa nhãn ở các SVG phân dải, khóa dải, đường xác suất, AND/OR, luồng ứng viên và Euclid. Không đổi dữ liệu hoặc quan hệ hình học.
- **Không đồng nhất hai cách hậu kiểm:** chữ ký MinHash đầy đủ chỉ cho ước lượng Jaccard; tập shingle hoặc dữ liệu gốc mới cho Jaccard chính xác. LSH chỉ sinh ứng viên.

## Xử lý phản biện vòng cuối (năm vai độc lập)

- **Planner:** tái cấu trúc thành 7 section ngoài kể cả recitation theo quyết định điều phối; outline mô tả 6 mạch giảng + recitation với chức năng và kết nối vào–ra, tổng 120 + 60 phút, kết luận C00 là section riêng. Quyết định: **sửa** outline và HTML.
- **Source analysis:** bổ sung phạm vi nguồn §§3.6–3.8; F01 thống nhất trích dẫn “MMDS §3.6.2, Ví dụ 3.18, trang 105” trong HTML và storyboard; D03 giữ Gaussian là trường hợp L2 của họ phân phối ổn định, không thêm công thức Datar ngoài nguồn đã có. Quyết định: **sửa**.
- **Storyboard audit:** khai báo chu trình F rút gọn ở D00–D04 và V00–V01 vì là khung tổng quát đã dựng ở F00–F05 và chi phí đã ở A05; bổ sung hành trình mở bài/kết luận với đầu vào–ra; sửa tuyên bố “P01 được dùng lại ở A05” thành ghi chú phân vai (P01 mở tình huống, A05 định lượng chi phí). Quyết định: **sửa** storyboard.
- **Rà mạch (Quill):** B01 trả lời rõ câu hỏi B00; A02 ghi rõ là ví dụ nhỏ khác ví dụ B02; P01 notes tách phép tính thành các câu ngắn; D00 đổi “cùng khoảng chiếu” thành “cùng ngăn chiếu độ rộng $a$”; Q02 notes đổi “gần 1/3000” thành “gần 1/2800”; Q06 dùng ≈0.047 hoặc 0.0475 và giữ ghi nhận lỗi slide MMDS trang 50 đã được điều phối viên xác minh trực tiếp; B06 dành định lượng $q(s)$ cho phần Q; V01 không nêu 0.2/0.8 trên mặt trang, chỉ nói “giả thiết mô hình của sách”; R00 thêm hướng dẫn làm trước rồi mới mở notes; A05/R00 nối MapReduce Bài 2 với recitation. Quyết định: **sửa** HTML. Mệnh đề đơn điệu của B06 được hiệu chỉnh ở lượt rà toán sau.
- **Kiểm định kỹ thuật:** đồng bộ khoa-band.svg với B02 $r=2$: D1, D2 (4,1), D3 (4,9), khóa (2,(4,1)); sửa desc and-or.svg thành “một trừ (một trừ rho) mũ b”; đổi title euclid-dich.svg từ “Bucket” thành “Ngăn”; xóa thời lượng khỏi notes R04, R06, R09 (thời lượng chỉ ở storyboard). Quyết định: **sửa** SVG và HTML. Bác đề xuất thêm Jaccard distance, HNSW, PQ ngoài phạm vi.

## Năm báo cáo độc lập của vòng rà hoàn tất

### Góc nhìn sinh viên

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa và quyết định |
|---|---|---|---|---|
| nghiêm trọng | D00–D04 | Mục tiêu nói “áp dụng” ba họ nhưng cụm chỉ giải thích điều kiện và không có bài tập đánh giá. | Phần bài tập chỉ kiểm tra MapReduce, AND/OR và vân tay. | Hạ mục tiêu về “giải thích và so sánh điều kiện”; **đã sửa** outline và storyboard, giữ đúng sản phẩm học tập trong `sources/source.md`. |
| trung bình | M01, B/A | Ký hiệu tập $C_i$, cột $D_i$ và tập ứng viên $C$ dễ lẫn. | Ba vai trò khác nhau dùng chữ gần nhau. | **Giữ** ký hiệu nguồn nhưng ghi rõ $C$ là tập cặp ở M00/B03 và dùng $D_i$ nhất quán trong ví dụ; không đổi ký hiệu sẽ gây sai ánh xạ nguồn. |
| trung bình | Q05–Q06 | Khai triển ngưỡng nửa chiếm tải nhưng chưa hỗ trợ trực tiếp một quyết định tham số. | Q06 chỉ kiểm tra lại giá trị $q(0.3)$, chưa buộc chọn hướng đổi $b,r$. | Chuyển khai triển lớn-$b$ vào notes; Q06 yêu cầu quyết định tăng $r$/giảm $b$ với $p$ cố định và nêu cái giá; **đã sửa**. |
| trung bình | A05 | Một trang đồng thời chứa nhiều cận thời gian, bộ nhớ, hậu kiểm và câu hỏi MapReduce. | Thân trang có hai biến thể bộ nhớ cùng bốn cận. | Giữ cận quyết định trên mặt trang, chuyển cận kỳ vọng và vật hóa khóa vào notes; **đã sửa**. |
| trung bình | A05, R00–R04 | Hợp đồng MapReduce của Bài 2 được nhắc quá ngắn. | R01 đi thẳng vào hai công việc. | R00 tái kích hoạt map → trộn/nhóm → reduce; notes A05 nêu số bản ghi và dung lượng trung gian; **đã sửa**. |
| nhẹ | R05–R06 | Công thức lồng AND/OR khó theo dõi nếu chỉ viết biểu thức cuối. | Chuỗi (d) có bốn phép biến đổi. | Yêu cầu ghi giá trị trung gian và dùng $z_1,z_2,z_3$ trong đáp án; **đã sửa**. |

### Chuyên gia giải thuật và khoa học dữ liệu

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa và quyết định |
|---|---|---|---|---|
| trung bình | D00–D04 | Ba họ độ đo chưa khép vòng từ điều kiện va chạm tới quyết định AND/OR. | Cụm dừng ở bảng điều kiện; không có kiểm tra chọn cấu hình riêng. | Hạ mục tiêu “áp dụng”; D04 nối các va chạm cơ sở sang OR–AND ở V00–V01; **đã sửa**. |
| trung bình | A05, R00–R04 | Phân tích hệ thống thiếu chi phí truyền thông trung gian. | Chỉ có thời gian cục bộ và bộ nhớ. | Notes A05 phân biệt $bN+A$ bản ghi với $\Theta(pN+A)$ từ truyền; khóa rút gọn vẫn phải đối chiếu vector đầy đủ; **đã sửa**. |
| trung bình | Q06, recitation | Mục tiêu chọn $b,r$ chưa được đánh giá trực tiếp. | Không bài tập nguồn nào yêu cầu một cặp số mới. | Không bịa dữ kiện; biến Q06 thành kiểm tra quyết định hướng đổi $b,r$ từ chính công thức $q(s)$; **đã sửa**. |
| nhẹ | Q00–V01 | Phần cuối dày nếu tiếp tục giữ động từ “áp dụng” cho ba họ. | F, D và V chiếm phần cuối của 120 phút. | Dùng động từ “giải thích và so sánh điều kiện”, giữ chu trình rút gọn; **đã sửa**. |

### Độ chính xác toán học và thuật toán

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa và quyết định |
|---|---|---|---|---|
| trung bình | M01 | Phân bố đều của một hàm băm không đủ cho đẳng thức MinHash. | Đẳng thức chính xác cần hoán vị ngẫu nhiên đều hoặc tính chất minwise phù hợp. | Nêu đúng hoán vị ngẫu nhiên đều và tách họ băm thực hành; **đã sửa**. |
| trung bình | A05 | $O(bN+|C|)$ chưa được gắn nhãn bộ nhớ phụ trợ. | Lưu đầu vào $\Sigma$ đã cần $\Theta(pN)$. | Gắn nhãn bộ nhớ phụ trợ và ghi riêng lưu đầu vào; **đã sửa**. |
| trung bình | R07 | “Mỗi hàm chọn ba ô độc lập” không đủ để biện minh các tích xác suất. | Phép tính dùng độc lập giữa ba ô, giữa hai dấu khác ngón và giữa các phép băm ở tầng OR/AND. | Phát biểu từng lớp độc lập trên mặt trang và notes; **đã sửa**. |
| nhẹ | D02 | Pháp tuyến $\{\pm1\}^m$ dễ bị hiểu là cho cùng đẳng thức góc. | Phân phối này không bất biến quay trong trường hợp tổng quát. | Nêu không có đẳng thức tổng quát, chỉ là cách xấp xỉ thực dụng dưới giả thiết; **đã sửa**. |
| nhẹ | D01, D03 | Miền tham số chưa hiện đủ. | Hamming cần $0\le d_1<d_2\le m$; Euclid cần $a>0$. | Bổ sung miền trong notes D01 và trên mặt D03–D04; **đã sửa**. |

### Phản biện học thuật và giảng dạy

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa và quyết định |
|---|---|---|---|---|
| nghiêm trọng | Q06 | Mục tiêu chọn $b,r$ chưa được người học thực hiện. | Câu hỏi cũ chỉ yêu cầu nhận ra $q(0.3)$. | Thay bằng quyết định hướng tăng $r$/giảm $b$ với $p$ cố định và yêu cầu nêu cái giá; **đã sửa**. |
| trung bình | D03–D04 | Công thức Euclid xuất hiện mà không có vết chạy riêng. | Cụm độ đo là chu trình rút gọn, thời lượng không dành cho một ví dụ số mới. | **Không thêm dữ kiện** ngoài nguồn; giữ hình chiếu–ngăn làm trực giác, nêu rõ lý do chu trình rút gọn trong storyboard và hạ mục tiêu khỏi “áp dụng”. |
| trung bình | D04→V00 | Chuyển từ điều kiện ba họ sang vân tay đột ngột. | Không có câu nối cho vai trò OR–AND. | Notes D04 nối phép va chạm cơ sở sang ghép OR–AND ở mô hình vân tay; storyboard ghi đầu ra D04 → V00; **đã sửa**. |
| trung bình | R05–R06 | Ký hiệu $s$ đổi vai so với $\rho$ trong phần giảng. | F03–F05 dùng $\rho$ cho xác suất va chạm. | Đổi toàn bộ R05–R06 sang $\rho$; **đã sửa**. |
| nhẹ | R00–R01 | Tiên quyết MapReduce chưa được khôi phục trước nhiệm vụ thiết kế. | Bài tập bắt đầu bằng khóa–giá trị của hai công việc. | R00 nhắc lại hợp đồng map → trộn/nhóm → reduce; **đã sửa**. |

### Kết nối và mạch viết

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa và quyết định |
|---|---|---|---|---|
| trung bình | P02 | Vai trò trong mạch: báo hành trình; kết nối vào: nút thắt P01; kết nối ra: M00. Trang chưa báo phần họ LSH, độ đo và vân tay. | Ba thẻ cũ chỉ có lọc, định lượng, đối chiếu. | Thêm chặng “Tổng quát” bao gồm họ LSH, AND/OR và ba độ đo; **đã sửa**. |
| trung bình | D04→V00 | Vai trò trong mạch: D04 chốt điều kiện, V00 mở ví dụ; kết nối vào đúng nhưng kết nối ra chưa có. | Hai trang không giải thích vì sao vân tay theo sau ba độ đo. | Thêm câu nối phép va chạm cơ sở → OR–AND trong notes D04 và storyboard; **đã sửa**. |
| trung bình | C00→R00 | Vai trò trong mạch: C00 thu hồi bài; kết nối vào: V01; kết nối ra cũ: Bài 7, khiến recitation thành phần phụ. | R00 nằm ngay sau C00 nhưng không được báo trước. | C00 dẫn trực tiếp vào ba bài tập rồi mới nói Bài 7; **đã sửa**. |
| nhẹ | C00 | Kết luận chưa thu hồi các con số mở bài. | $10^6$ chữ ký và gần $5\cdot10^{11}$ cặp không trở lại. | Nối các số mở bài với $pN,A,|C|$; **đã sửa**. |
| nhẹ | A05→F00 | Vai trò trong mạch: A05 chốt hệ thống; kết nối ra F00 mờ vì câu hỏi MapReduce hứa nội dung không đến ngay. | Phần kế tiếp tổng quát hóa họ LSH, bài MapReduce ở cuối. | Chuyển câu hỏi khỏi mặt A05; notes báo giữ thiết kế cho recitation rồi nối sang F00; **đã sửa**. |

Kết quả hợp nhất: không còn vấn đề `chặn bàn giao` hoặc `nghiêm trọng`. Các đề xuất trung bình đã được áp dụng, trừ yêu cầu thêm vết chạy Euclid: quyết định không thêm dữ kiện ngoài nguồn và điều chỉnh mục tiêu cùng storyboard để phản ánh chu trình rút gọn.

## Rà lại toán sau chỉnh sửa

- **Mức độ: trung bình; trang chiếu: B06, Q06; vấn đề:** mô tả cũ dè dặt sai về tính đơn điệu khi $p$ cố định. **Bằng chứng:** với $q(s)=1-(1-s^r)^{p/r}$, tăng $r$ làm $q(s)$ giảm với mọi $0<s<1$. **Đề xuất sửa và quyết định:** bỏ “thường” và “không đơn điệu”; nêu rõ xác suất bỏ sót tăng ở mọi $s<1$ và phải tính $q$ tại các mức cần bảo vệ; **đã sửa** HTML, storyboard và nhật ký.
- **Mức độ: trung bình; trang chiếu: A05; vấn đề:** số bản ghi trung gian chưa được phân biệt với dung lượng truyền. **Bằng chứng:** hai công việc phát $bN+A$ bản ghi, nhưng mỗi khóa dải đầy đủ chứa $\Theta(r)$ thành phần, nên dung lượng theo số từ là $\Theta(brN+A)=\Theta(pN+A)$. **Đề xuất sửa và quyết định:** ghi cả hai đại lượng; nếu dùng mã băm rút gọn, vẫn đối chiếu vector đầy đủ để xử lý va chạm mã; **đã sửa** HTML, outline, storyboard và nhật ký.
- Không đổi số trang, thứ tự trang hoặc câu chuyển; phạm vi rà mạch không mở rộng.

## Giới hạn điều phối mô hình của vòng rà này

- Cầu nối OpenRouter đã xác nhận bằng một smoke test chỉ đọc `AGENTS.md`: `requested_model = observed_model = z-ai/glm-5.3-flash`, nhà cung cấp `OpenRouter`.
- Lần thử chuyển payload Bài 6 cho reviewer OpenRouter bị chính sách hạ tầng từ chối. Không đọc hoặc gửi tệp `.env`, không tìm cách vượt chính sách.
- Vì vậy năm báo cáo ở vòng hoàn tất này do năm reviewer Codex cục bộ, chỉ đọc và độc lập thực hiện. Metadata OpenRouter ở các vòng trước vẫn được giữ riêng bên dưới; không dùng nó để mô tả sai runtime của vòng này.

## Metadata của vòng OpenRouter trước

- Mô hình được yêu cầu và quan sát được: `z-ai/glm-5.3-flash`, nhà cung cấp OpenRouter.

## Rà lại sau chỉnh sửa

- Hai tác tử chỉ đọc độc lập đã rà toàn bộ mạch và các cụm toán–thuật toán bị ảnh hưởng. Cả hai có metadata runtime `requested_model = observed_model = z-ai/glm-5.3-flash`, nhà cung cấp OpenRouter.
- Rà mạch xác nhận 7 section ngoài, đủ 120 + 60 phút, kết luận thu hồi vấn đề mở đầu và không còn lỗi chặn bàn giao hoặc nghiêm trọng. Đã sửa cách mô tả đếm mạch trong outline/storyboard: sáu mạch giảng tương ứng sáu section ngoài, trong đó hai mạch ghép được tách thành tám cụm khi lập bảng.
- Rà toán xác nhận B02 và SVG cùng dùng $r=2$; các công thức $q(s)$, ngưỡng một nửa, chi phí $A$, định nghĩa LSH, AND/OR, phép băm Euclid và toàn bộ đáp án R01–R09 đều đúng. Không cần đổi công thức hoặc dữ kiện.
- Góp ý nhẹ về A02 được áp dụng: ghi chú nói rõ ví dụ mở rộng các vector dải đã quen sang tập chỉ số cột khác, tránh tuyên bố đây là bộ dữ liệu hoàn toàn khác.
- Điều phối viên loại ba mã trang nội bộ còn lọt vào mặt trang hoặc ghi chú; kiểm tra lại không còn mã dạng chữ cái–hai chữ số ngoài thuộc tính `data-slide-id`.
- Rà ảnh Playwright lần đầu phát hiện nội dung bị cắt ở trang chia dải và trang Euclid. Đã bỏ câu hiển thị lặp ở trang chia dải; rút tiêu đề Euclid, giảm chiều cao hình, thu gọn công thức và chuyển giải thích xác suất điều kiện vào ghi chú. Hai thay đổi không đổi dữ kiện hoặc kết luận toán học.

## Tài sản và công cụ

- Mười hình được vẽ lại thành SVG cục bộ trong `img/lec-06/`; không dùng raster hoặc tài nguyên mạng.
- Dự án Codex Slides: `20260827182308-b-i-6-t-m-c-p-t-ng-ng-b-ng-lsh-bmts`.
- Codex Slides trong trình duyệt biên tập chưa khả dụng trong môi trường tác tử này; không tuyên bố đã rà trực quan bằng Codex Slides. Kiểm định RevealJS cục bộ được ghi sau khi chạy.

## Kiểm định đã chạy

- Bộ kiểm tra tĩnh ban đầu xác nhận 39 trang giảng, 10 trang recitation, 49 `data-slide-id` duy nhất và 49 notes. Sau phản biện thêm P02; kết quả kiểm định lại được ghi bên dưới.
- Storyboard khớp thứ tự HTML; tổng thời lượng tính lại là 120 + 60 phút.
- Mười SVG đọc được bằng trình phân tích XML, có `role`, `title`, `desc`; mọi đường dẫn tài sản tồn tại.
- Không tìm thấy ảnh raster, URL tài nguyên từ xa hoặc phụ thuộc mạng cốt lõi.
- `python3 -m reloadserver 8765` không chạy vì môi trường thiếu mô-đun `reloadserver`. Điều phối viên dùng `/tmp/reloadserver.py 8765` làm máy chủ dự phòng trên đúng cổng.
- `git diff --check` không báo lỗi ở bản nháp; không sửa `index.html`, CSS hoặc tệp ngoài phạm vi Bài 6.

## Kiểm định lại sau chỉnh sửa

- Kiểm tra tĩnh xác nhận 40 trang giảng và 10 trang recitation; 50 `data-slide-id` duy nhất; mỗi trang có đúng một khối ghi chú; thứ tự HTML khớp storyboard.
- Tổng thời lượng tính từ storyboard là 120 phút giảng và 60 phút recitation; thời lượng không còn xuất hiện trên mặt trang hoặc notes.
- Mười tham chiếu SVG đều tồn tại. Mỗi SVG đọc được bằng trình phân tích XML và có `role="img"`, `title`, `desc`; không có tham chiếu raster hoặc tài nguyên mạng cốt lõi.
- Tính lại B02 cho đúng một cặp ứng viên; đối chiếu các công thức $q(s)$, ngưỡng một nửa, AND/OR, Hamming, cosin, Euclid có độ dịch và các đáp án recitation.
- Tự kiểm theo `no-ai-slop/eval.md`: không có từ cấm, lời dẫn rỗng, câu hỏi tu từ hoặc kết luận lặp; thuật ngữ và ký hiệu được dùng nhất quán theo rà mạch Quill.
- `git diff --check` không báo lỗi. Không sửa `index.html`, CSS chung hoặc tệp ngoài Bài 6.
- Hai tái kiểm độc lập xác nhận không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng`; các mục trung bình về mô hình chi phí, hậu kiểm, miền xác suất, nguồn ngẫu nhiên Euclid và giả thiết độc lập đã được vá.
- Playwright duyệt đủ 50 trang ở `1280 × 720` và `800 × 600`: không có lỗi tải hoặc lỗi JavaScript; điều hướng dọc/ngang bằng bàn phím hoạt động. Bộ dò hình học chỉ báo các dương tính giả quen thuộc ở H1/KaTeX. Điều phối viên đã xem năm contact sheet và ảnh nguyên kích thước của các trang thay đổi; sau hai vòng sửa, không còn nội dung bị cắt hoặc chồng lấn.
- Dự án Codex Slides vẫn ở trạng thái nháp với 0 trang; `generated/outline.md` và `generated/brief.md` đọc được. Lần tải HTML cuối hiện tại vào Design Files tiếp tục trả lỗi HTTP 500. Liên kết workspace được tạo nhưng bề mặt Browser nội bộ không khả dụng trong phiên tác tử, nên không tuyên bố đã rà trực quan bằng Codex Slides. Rà trực quan RevealJS cục bộ là kiểm định hiển thị cuối.
