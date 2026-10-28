# Hướng dẫn giảng dạy chi tiết Bài 08: Dòng dữ liệu – Mô hình, lấy mẫu và lọc

Bản đánh giá do người dùng gửi ngày 2026-10-28, ghi lại nguyên nội dung để làm căn cứ cho lượt biên tập theo bản đánh giá. Đã bỏ các phần rác của trang gốc (biểu tượng trang, phần còn lại của widget tương tác và biểu đồ, nút "Sao chép") và đổi ký hiệu toán sang `$…$`, `$$…$$`. Đánh số slide 1–58 theo thứ tự deck tại commit `b24a2a3`. Quyết định chấp nhận hoặc bác bỏ từng đề xuất ghi ở `review-log.md`, mục "Lượt biên tập theo bản đánh giá giảng dạy (2026-10-28)".

Học phần: Giải thuật nền tảng của Khoa học dữ liệu (Data Science – Algorithms Foundation)
Tài liệu: Bài giảng Lecture 08 (`2627-1/lecture-08-dong-du-lieu-mo-hinh-lay-mau-va-loc.html`)
Phạm vi: 58 slide, bao gồm lý thuyết, chứng minh, ví dụ và bài tập. Nội dung đã được đối chiếu với phiên bản bài giảng trực tuyến hiện tại.

Tôi sẽ phân tích từng slide theo ba mục:

- Giải thích để giảng: Bản chất khái niệm, diễn giải công thức và cách trình bày với sinh viên.
- Nên bổ sung: Kiến thức nền, ví dụ trực quan, những chỗ dễ hiểu sai hoặc cần làm rõ.
- Prompt chỉnh sửa: Yêu cầu cụ thể để cải thiện chính slide đó, không chỉ thay đổi hình thức.

## Định hướng chung của bài giảng

Bài này có một tư tưởng xuyên suốt:

> Khi dữ liệu đến liên tục và không thể lưu toàn bộ, thuật toán phải quyết định giữ lại thông tin gì để vẫn trả lời được câu hỏi cần thiết.

Ba phương pháp chính trả lời ba nhu cầu khác nhau.

| Phương pháp | Câu hỏi giải quyết | Bảo đảm quan trọng |
| --- | --- | --- |
| Key-based sampling | Làm sao giữ trọn dữ liệu của một nhóm được chọn? | Cùng khóa, cùng quyết định |
| Reservoir sampling | Làm sao giữ một mẫu có kích thước cố định? | Mỗi vị trí có xác suất $s/r$ |
| Bloom filter | Làm sao kiểm tra nhanh một khóa có thể thuộc tập không? | Không âm giả trong điều kiện chuẩn |

Đề xuất cách giảng: Đi từ vấn đề thực tế → giải pháp đơn giản nhưng không phù hợp → ý tưởng thuật toán → chứng minh → phân tích chi phí → trường hợp áp dụng. Đặc biệt, không nên đưa công thức xác suất lên trước khi sinh viên hiểu thuật toán đang giải quyết vấn đề gì.

# Phần I. Mở đầu và mô hình tính toán trên dòng

## Slide 1. Dòng dữ liệu: mô hình, lấy mẫu và lọc

**Giải thích để giảng**

Mở đầu bằng việc phân biệt hai kiểu dữ liệu.

Dữ liệu tĩnh, chẳng hạn một tệp CSV chứa một triệu bản ghi, có thể được đọc nhiều lần, sắp xếp và xử lý theo lô.

Ngược lại, dữ liệu dòng (data stream) có thể đến không ngừng. Ví dụ:

- Mỗi lượt tìm kiếm trên Google tạo một sự kiện.
- Mỗi giao dịch ngân hàng tạo một bản ghi.
- Camera và cảm biến liên tục phát sinh dữ liệu.

Điểm khó không nhất thiết là một phần tử lớn, mà là tổng số phần tử có thể lớn vô hạn và tốc độ đến không do thuật toán quyết định.

**Nên bổ sung**

Đưa ra câu hỏi mở đầu: “Nếu mỗi giây hệ thống nhận một triệu sự kiện, liệu có thể giữ toàn bộ trong RAM để cuối ngày xử lý không?”

Sau đó nhấn mạnh ba mục tiêu: giữ trọn nhóm, giữ mẫu có kích thước cố định và kiểm tra thành viên.

**Prompt chỉnh sửa**

> Thiết kế lại slide mở đầu thành sơ đồ trực quan: bên trái là dòng sự kiện đến liên tục, ở giữa là bộ xử lý với RAM giới hạn, bên phải là ba đầu ra Key Sampling, Reservoir Sampling và Bloom Filter. Mỗi đầu ra có một câu mô tả và biểu tượng riêng. Giữ tiêu đề tiếng Việt, thuật ngữ tiếng Anh đặt dưới. Hạn chế văn bản trang trí.

## Slide 2. Tiên quyết và quy ước

**Giải thích để giảng**

Có ba kiến thức toán học nền tảng cần nhắc lại.

Thứ nhất, hàm băm là hàm xác định: cùng đầu vào luôn sinh cùng kết quả. Điều này khác với việc rút một số ngẫu nhiên mới cho mỗi lần xuất hiện.

Thứ hai, khi các biến cố độc lập:

$$P(A\cap B)=P(A)P(B).$$

Thứ ba, giới hạn:

$$\left(1-\frac1n\right)^n\longrightarrow e^{-1}$$

giúp xấp xỉ xác suất ở Bloom filter khi $n$ lớn.

**Nên bổ sung**

Giải thích một phân biệt rất quan trọng:

- Deterministic hashing: Một khóa luôn nhận cùng kết quả.
- Randomized hash function: Hàm băm được chọn từ một họ hàm ngẫu nhiên, nhưng sau khi chọn phải giữ cố định.
- Random draw: Mỗi lần xử lý phần tử có thể tạo một số ngẫu nhiên mới.

Phân biệt này chính là nền tảng của sự khác nhau giữa lấy mẫu theo khóa và hồ chứa.

**Prompt chỉnh sửa**

> Chia slide thành ba khối: Hàm băm, Xác suất độc lập và Xấp xỉ hàm mũ. Mỗi khối có một ví dụ số đơn giản. Thêm bảng ký hiệu $r,s,n,m,k,K(t)$ ở cuối slide, tránh nhầm số hàm băm $k$ với khóa $K$.

## Slide 3. Mục tiêu học tập

**Giải thích để giảng**

Sinh viên cần đạt ba mức năng lực:

1. Hiểu mô hình dòng dữ liệu và lựa chọn trạng thái phù hợp.
2. Cài đặt và chứng minh tính đúng của thuật toán lấy mẫu.
3. Phân tích và định cỡ Bloom filter.

Nên nói rõ rằng học thuộc công thức không đủ. Sinh viên phải biết các giả thiết làm cho công thức đúng.

Ví dụ, công thức $s/r$ không còn được bảo đảm nếu các số ngẫu nhiên của hồ chứa được sinh theo một quy tắc thiên lệch, phụ thuộc vào trạng thái.

**Nên bổ sung**

Đưa ví dụ về sản phẩm học tập: sinh viên phải có khả năng viết giả mã, chạy tay thuật toán, chứng minh một bất biến và lựa chọn giải pháp cho tình huống thực tế.

**Prompt chỉnh sửa**

> Chuyển ba mục tiêu thành ba Learning Outcomes có động từ đánh giá được: Đặc tả, Chứng minh, Thiết kế/Định cỡ. Với mỗi mục tiêu thêm một sản phẩm cụ thể: sơ đồ trạng thái, chứng minh xác suất, tính toán cấu hình Bloom filter.

## Slide 4. Nội dung

**Giải thích để giảng**

Giải thích sự liên kết giữa các phần.

Mô hình dòng cung cấp ràng buộc về bộ nhớ và thời gian. Lấy mẫu theo khóa giải quyết việc bảo toàn quan hệ nhóm, nhưng không khống chế được số phần tử. Hồ chứa giải quyết vấn đề giới hạn số phần tử, nhưng không bảo toàn nhóm. Bloom filter chuyển sang một câu hỏi khác: kiểm tra thành viên.

**Nên bổ sung**

Dùng một dòng dữ liệu duy nhất để dẫn dắt toàn bộ bài, ví dụ `(userID, query, timestamp)`.

Từ dòng này, đặt ba yêu cầu:

- Chọn ngẫu nhiên 10% người dùng và giữ mọi truy vấn của họ.
- Giữ đúng 1.000 sự kiện để khảo sát.
- Kiểm tra userID có nằm trong tập người dùng được phép hay không.

**Prompt chỉnh sửa**

> Thay danh sách mục lục tuyến tính bằng sơ đồ tiến trình có ba nhánh giải pháp xuất phát từ cùng một dòng dữ liệu. Hiển thị câu hỏi mà từng thuật toán trả lời, không chỉ tên chủ đề.

## Slide 5. Vấn đề trung tâm

**Giải thích để giảng**

Slide này chứa các kết quả mà sinh viên chưa học. Không nên yêu cầu họ hiểu ngay các con số $1/10$, $s/r$, hoặc 2%.

Hãy biến chúng thành những câu hỏi dự đoán:

- Chọn 10% bản ghi có giống chọn 10% người dùng không?
- Không biết tổng độ dài dòng, có thể giữ đúng $s$ phần tử được không?
- Một mảng bit có thể thay thế tập chứa hàng tỷ khóa không?

Sau bài học, quay lại trả lời những câu hỏi này.

**Nên bổ sung**

Làm rõ hai loại bảo đảm:

- Bảo đảm tất định: cùng khóa nhận cùng quyết định; Bloom filter chuẩn không có âm giả.
- Bảo đảm xác suất: xác suất giữ một khóa, một vị trí, hoặc tỷ lệ dương giả.

**Prompt chỉnh sửa**

> Thiết kế slide như ba câu hỏi thách thức, tạm ẩn lời giải và công thức. Mỗi câu có một hình minh họa nhỏ. Chuyển các kết quả $1/10$, $s/r$ và 2% sang slide tổng kết để tạo hiệu ứng quay lại vấn đề mở đầu.

## Slide 6. Mô hình tính toán trên dòng

**Giải thích để giảng**

Đây là slide chuyển phần, cần giới thiệu khái niệm state.

Một thuật toán thông thường có thể đọc dữ liệu, lưu kết quả trung gian rồi quét lại khi cần.

Thuật toán dòng phải cập nhật trạng thái khi mỗi phần tử đến:

$$state_r=Update(state_{r-1},x_r).$$

Sau đó:

$$answer_r=Query(state_r).$$

Đây là dạng trừu tượng phù hợp với hầu hết các thuật toán trong bài.

**Nên bổ sung**

Phân biệt ba đối tượng: dòng đầu vào, trạng thái giữ trong bộ nhớ và kết quả truy vấn. Không nên đồng nhất trạng thái với toàn bộ dữ liệu đã ghi ra đĩa.

**Prompt chỉnh sửa**

> Thêm sơ đồ chung $x_r \rightarrow Update \rightarrow state_r \rightarrow Query \rightarrow answer_r$. Dùng hai mũi tên: trạng thái cũ đi vào Update và trạng thái mới được giữ để xử lý phần tử tiếp theo. Làm nổi bật cơ chế một lượt.

## Slide 7. Ví dụ: ba truy vấn trên dòng cảm biến

**Giải thích để giảng**

Dòng đầu vào:

$$1,5,2,7,4,0,3,5.$$

Giả sử sau mỗi phần tử, chúng ta cần trả lời một trong ba truy vấn.

Truy vấn lớn nhất: Chỉ cần giữ biến `max`. Mỗi phần tử mới được so sánh với giá trị đang giữ. Sau tám phần tử, kết quả là 7.

Truy vấn trung bình: Giữ hai biến:

$$sum=27,\qquad count=8.$$

Suy ra:

$$mean=\frac{27}{8}=3{,}375.$$

Truy vấn trung bình 24 giá trị gần nhất: Phải biết phần tử nào sẽ rời cửa sổ khi có phần tử mới, vì vậy cần lưu thêm 24 giá trị trong một bộ đệm.

**Nên bổ sung**

Một nhận xét quan trọng: yêu cầu truy vấn quyết định lượng thông tin cần nhớ.

Trung bình của toàn bộ lịch sử chỉ cần tổng và số đếm, nhưng trung bình của một cửa sổ trượt lại cần giữ các giá trị cũ để loại chúng đúng lúc.

**Prompt chỉnh sửa**

> Bố trí ba truy vấn thành ba hàng song song trên cùng dòng dữ liệu. Sau mỗi phần tử, minh họa trạng thái được cập nhật. Làm rõ: Max giữ 1 số, Mean giữ 2 số, Sliding Mean giữ bộ đệm vòng 24 số. Thêm tính toán $27/8=3{,}375$.

## Slide 8. Mô hình dòng dữ liệu

**Giải thích để giảng**

Đọc hình theo hướng dữ liệu đi vào bộ xử lý.

Các dòng có thể đồng thời gửi phần tử đến. Bộ xử lý duy trì trạng thái trong bộ nhớ làm việc hữu hạn.

Hai loại truy vấn:

- Standing query: Truy vấn thường trực, luôn được cập nhật theo dòng.
- Ad-hoc query: Truy vấn tức thời trên trạng thái hiện có.

Ví dụ standing query là số lượt tìm kiếm trong mỗi phút; ad-hoc query là hỏi giá trị thống kê ngay tại thời điểm hiện tại.

Điểm quan trọng là không giả định có thể đọc lại toàn bộ dòng để trả lời.

**Nên bổ sung**

Phân biệt mô hình thuật toán dòng với hệ thống xử lý dòng thực tế như Apache Flink hoặc Spark Structured Streaming. Hệ thống thực tế có thể có kho lưu trữ, checkpoint và khả năng phát lại; mô hình lý thuyết đang xét không dựa vào những khả năng đó.

**Prompt chỉnh sửa**

> Vẽ lại hình kiến trúc bằng bốn thành phần: Input Streams, Stream Processor, Working Memory và Output. Phân biệt standing query với ad-hoc query bằng hai vị trí truy vấn khác nhau. Ghi rõ kho lưu trữ không được đọc lại trong mô hình thuật toán đang xét.

## Slide 9. Chi phí: thuật toán dòng

**Giải thích để giảng**

Với thuật toán dòng, không chỉ quan tâm tổng thời gian $O(N)$, mà còn phải xét mỗi phần tử đến tốn bao nhiêu thời gian.

Bốn tiêu chí:

| Tiêu chí | Câu hỏi |
| --- | --- |
| Bộ nhớ | Lưu bao nhiêu trạng thái? |
| Update time | Mỗi phần tử tốn bao nhiêu phép toán? |
| Passes | Có phải đọc lại dữ liệu không? |
| Accuracy | Kết quả chính xác hay xấp xỉ? |

Ví dụ, bộ đệm vòng 24 phần tử chỉ cần 24 ô dữ liệu và một số biến quản lý. Khi phần tử thứ 25 đến, ghi đè ô cũ nhất, trừ giá trị cũ khỏi tổng rồi cộng giá trị mới.

**Nên bổ sung**

Phân biệt hai kiểu độ phức tạp:

$$\text{Total time}=O(r),\qquad \text{Update time}=O(1).$$

Hai biểu thức không mâu thuẫn: thuật toán xử lý tổng cộng $r$ phần tử, nhưng mỗi lần cập nhật có chi phí hằng số.

Cũng nên lưu ý $O(1)$ bộ nhớ thường được tính theo từ máy; bộ đếm $r$ về mặt bit vẫn cần $O(\log r)$ bit.

**Prompt chỉnh sửa**

> Giữ bảng bốn tiêu chí chi phí, nhưng bổ sung bên dưới một bộ đệm vòng 4 ô để minh họa cách cửa sổ trượt hoạt động. Thêm chú thích “$O(1)$ thời gian mỗi phần tử không có nghĩa tổng thời gian $O(1)$”.

## Slide 10. Bài tập: trạng thái của phương sai

**Giải thích để giảng**

Đây là slide rất tốt để chứng minh rằng không phải thống kê nào cũng cần lưu toàn bộ dữ liệu.

Định nghĩa phương sai tổng thể:

$$\sigma_r^2=\frac1r\sum_{i=1}^r(x_i-\bar x_r)^2.$$

Khai triển:

$$\begin{aligned} \sigma_r^2 &=\frac1r\sum_{i=1}^r (x_i^2-2x_i\bar x_r+\bar x_r^2)\\ &=\frac1r\sum x_i^2 -2\bar x_r\frac1r\sum x_i+\bar x_r^2\\ &=\frac1r\sum x_i^2-\bar x_r^2. \end{aligned}$$

Vậy chỉ cần giữ ba đại lượng:

$$r,\qquad S_1=\sum x_i,\qquad S_2=\sum x_i^2.$$

Với dòng ví dụ:

$$r=8,\quad S_1=27,\quad S_2=129.$$

Kết quả:

$$\sigma_8^2=\frac{129}{8}-\left(\frac{27}{8}\right)^2 =\boxed{4{,}734375}.$$

**Nên bổ sung**

Đây là công thức chính xác trong số học thực, nhưng khi lập trình với số thực dấu phẩy động, phép trừ hai số lớn gần nhau có thể gây mất độ chính xác số học. Có thể giới thiệu thuật toán Welford như kiến thức mở rộng về tính phương sai trực tuyến ổn định số.

**Prompt chỉnh sửa**

> Chia bài tập thành hai slide hoặc hai bước xuất hiện: bước 1 yêu cầu sinh viên tìm trạng thái cần lưu, bước 2 khai triển công thức và tính phương sai. Thêm bảng cập nhật $r,S_1,S_2$ sau từng giá trị. Đưa Welford vào ghi chú mở rộng, không làm nặng slide chính.

# Phần II. Lấy mẫu theo khóa (Key-based Sampling)

Đây là phần đầu tiên cần giảng sâu. Sinh viên phải hiểu rằng lấy mẫu bản ghi và lấy mẫu đối tượng tạo ra bản ghi là hai bài toán khác nhau.

## Slide 11. Lấy mẫu theo khóa

**Giải thích để giảng**

Giả sử hệ thống tìm kiếm muốn thống kê một người dùng thường lặp lại bao nhiêu truy vấn.

Nếu một người tìm “đồ thị” hai lần và “băm” một lần, việc giữ một phần các bản ghi có thể làm chúng ta hiểu sai hành vi của họ.

Vì thế, đơn vị lấy mẫu thích hợp không phải là từng bản ghi mà là người dùng.

Ý tưởng: chọn một tập người dùng, sau đó giữ toàn bộ sự kiện của những người đã chọn.

**Nên bổ sung**: Phân biệt element sampling với cluster sampling. Trong trường hợp này, một người dùng là một cụm, bao gồm tất cả bản ghi của người đó.

**Prompt chỉnh sửa**

> Thêm hình hai cấp: người dùng → các truy vấn của người dùng. Minh họa lấy mẫu từng bản ghi làm mất một số truy vấn, còn lấy mẫu theo người dùng giữ nguyên cả nhóm. Dùng cùng bộ dữ liệu ở các slide tiếp theo.

## Slide 12. Ví dụ: ba bộ truy vấn của An

**Giải thích để giảng**

An có ba bản ghi:

$$(\text{An, đồ thị}),\ (\text{An, băm}),\ (\text{An, đồ thị}).$$

Có hai truy vấn phân biệt và một truy vấn được lặp lại. Tỷ lệ cần tính:

$$R=\frac12.$$

Giả sử mỗi bản ghi được lấy độc lập với xác suất $p=0{,}1$.

Hai lần tìm “đồ thị” đều được giữ với xác suất:

$$P(\text{giữ cả hai})=p^2=0{,}01.$$

Chỉ giữ đúng một lần:

$$P(\text{giữ đúng một}) =2p(1-p)=0{,}18.$$

Ít nhất một lần được giữ:

$$P(\text{ít nhất một})=0{,}01+0{,}18=0{,}19.$$

Vì vậy:

$$P(\text{giữ cả hai}\mid\text{ít nhất một}) =\frac{0{,}01}{0{,}19} =\boxed{\frac1{19}}.$$

Ý nghĩa: Trong những trường hợp truy vấn “đồ thị” xuất hiện trong mẫu, phần lớn trường hợp chỉ xuất hiện một lần, khiến một truy vấn lặp bị nhìn nhận nhầm thành truy vấn không lặp.

**Nên bổ sung**

Dùng cây xác suất gồm bốn trường hợp: giữ cả hai, giữ lần đầu, giữ lần hai, bỏ cả hai. Đặc biệt giải thích vì sao trường hợp giữ đúng một có hệ số 2.

**Prompt chỉnh sửa**

> Thay bảng xác suất thuần văn bản bằng cây xác suất hai tầng cho hai lần tìm “đồ thị”. Đánh dấu nhóm có đủ hai bản ghi là 1%, nhóm chỉ có một là 18%, và nhóm không có bản ghi nào là 81%. Giải thích trực quan xác suất có điều kiện $1/19$.

## Slide 13. Sai lệch của mẫu từng bộ

**Giải thích để giảng**

Đây là phần tổng quát hóa ví dụ trước.

Giả sử một người có:

- $u$ truy vấn phân biệt xuất hiện đúng một lần;
- $d$ truy vấn phân biệt xuất hiện đúng hai lần.

Tỷ lệ thực:

$$R=\frac{d}{u+d}.$$

Nếu lấy độc lập từng bản ghi với xác suất $p$, số truy vấn kỳ vọng còn đủ hai bản là:

$$E[N_2]=dp^2.$$

Số truy vấn kỳ vọng chỉ còn một bản là:

$$E[N_1]=up+2dp(1-p).$$

Tỷ số giữa các số đếm kỳ vọng:

$$R_{\text{approx}} =\frac{dp^2}{up+dp^2+2dp(1-p)} =\frac{dp}{u+(2-p)d}.$$

Với $p=0{,}1$:

$$\boxed{R_{\text{approx}}=\frac{d}{10u+19d}}.$$

Nếu $u=d=1$:

$$R_{\text{thực}}=\frac12,\qquad R_{\text{approx}}=\frac1{29}.$$

Điểm phải giải thích thật rõ: $1/29$ là tỷ số của các số đếm kỳ vọng, không phải kỳ vọng chính xác của tỷ lệ quan sát được trong từng mẫu. Không được viết $E[N_2/(N_1+N_2)]=1/29$.

**Nên bổ sung**

Cho sinh viên thử $p=1$, lúc đó công thức trở về:

$$\frac{d}{u+d}.$$

Đây là cách kiểm tra công thức hợp lý. Với $p$ nhỏ, hai lần xuất hiện của một truy vấn rất khó cùng được giữ.

**Prompt chỉnh sửa**

> Biên tập lại slide thành bốn bước suy luận: tỷ lệ gốc, kỳ vọng truy vấn còn hai bản, kỳ vọng truy vấn còn một bản và tỷ số thu được. Phân biệt nổi bật “tỷ số các kỳ vọng” với “kỳ vọng của tỷ số”. Thêm ví dụ $u=d=1$ và $p=0{,}1$, tránh gọi $1/29$ là kỳ vọng chính xác của tỷ lệ mẫu.

## Slide 14. Bảng giữ hoặc bỏ theo người dùng

**Giải thích để giảng**

Giải pháp trực tiếp là khi gặp người dùng lần đầu, rút một quyết định ngẫu nhiên rồi lưu nó.

Ví dụ:

| Người dùng | Quyết định |
| --- | --- |
| An | Giữ |
| Bình | Bỏ |
| Chi | Bỏ |

Các bản ghi của An đến sau không phải rút lại; chỉ tra bảng và giữ tất cả.

Cách làm này bảo đảm nhất quán, nhưng bảng tăng theo số lượng người dùng phân biệt $D$:

$$Memory=O(D).$$

Nếu dòng có số người dùng mới tăng liên tục, bảng quyết định không còn phù hợp với yêu cầu bộ nhớ hạn chế.

**Nên bổ sung**

Phân biệt số người dùng phân biệt $D$ với số bản ghi $r$. Một người có thể tạo hàng triệu bản ghi, nhưng bảng vẫn chỉ chứa một hàng cho người đó.

**Prompt chỉnh sửa**

> Thêm hoạt cảnh năm sự kiện đi qua bảng quyết định. Sự kiện đầu của mỗi người làm bảng tăng một hàng; các sự kiện sau chỉ tra bảng. Hiển thị bộ đếm số hàng $D$ và kết luận “Đúng về thống kê, nhưng bộ nhớ tăng theo số khóa”.

## Slide 15. Hàm băm thay bảng nhãn

**Giải thích để giảng**

Đây là ý tưởng chính của key-based sampling.

Thay vì nhớ quyết định của mỗi người, dùng một hàm băm cố định:

$$h:\mathcal K\rightarrow\{0,1,\ldots,9\}.$$

Quy tắc:

$$\text{Giữ }t\iff h(K(t))=0.$$

Giả sử:

$$h(\text{An})=0,\quad h(\text{Bình})=7,\quad h(\text{Chi})=4.$$

Cả ba lần xuất hiện của An đều nhận cùng giá trị 0, vì vậy cùng được giữ.

Bản chất toán học: Hàm băm thay một bảng quyết định có thể rất lớn bằng một hàm xác định có mô tả nhỏ.

**Nên bổ sung**

Hàm băm không phải phép rút ngẫu nhiên mới mỗi lần xuất hiện. Tính ngẫu nhiên nằm ở việc lựa chọn hàm băm hoặc seed ban đầu; tính nhất quán đến từ việc giữ nguyên hàm này.

**Prompt chỉnh sửa**

> Đặt hình “bảng quyết định” và “hàm băm cố định” cạnh nhau. Cho năm sự kiện giống hệt ở slide 14 chạy qua hai phương án và thu được cùng kết quả. Hiển thị rõ $h(\text{An})=0$ ở tất cả lần xuất hiện, nhấn mạnh không lưu bảng theo người dùng.

## Slide 16. Thuật toán: lấy mẫu theo khóa

**Giải thích để giảng**

Tổng quát hóa từ 10% thành tỷ lệ $a/b$.

Hàm băm:

$$h:\mathcal K\rightarrow\{0,1,\ldots,b-1\}.$$

Quy tắc:

$$\boxed{h(K(t))<a}.$$

Nếu có $b$ giá trị đồng khả năng và đúng $a$ giá trị được chọn, xác suất chọn một khóa là:

$$P(\text{giữ khóa})=\frac ab.$$

Ví dụ $a=3,b=10$, giữ các giá trị 0, 1 và 2, tức 30% xác suất chọn mỗi khóa.

Giả mã:

```
KEY_SAMPLE(t, a, h):
    key = K(t)
    if h(key) < a:
        emit(t)
```

**Nên bổ sung**

Nhấn mạnh dấu `<` thay vì `<=`. Với $a=3$, điều kiện `<=3` nhận bốn giá trị 0, 1, 2, 3, tức 40%.

Hai trường hợp biên:

- $a=0$: Không giữ gì.
- $a=b$: Giữ tất cả.

**Prompt chỉnh sửa**

> Đưa giả mã ở trung tâm, bên cạnh là thanh 10 ngăn đánh số 0–9, tô đúng ba ngăn 0–2. Minh họa trường hợp $a=3,b=10$ và cảnh báo lỗi `<` so với `<=`. Giữ rõ giả thiết hàm băm đều và cố định.

## Slide 17. Tính đúng: lấy mẫu theo khóa

**Giải thích để giảng**

Có hai mệnh đề riêng biệt phải chứng minh.

Mệnh đề 1 — Tính nhất quán

Nếu hai bộ có cùng khóa:

$$K(t)=K(t'),$$

thì:

$$h(K(t))=h(K(t')).$$

Do đó:

$$h(K(t))<a \iff h(K(t'))<a.$$

Vì vậy cả hai được giữ hoặc cả hai bị bỏ.

Đây là tính chất tất định, không cần giả thiết hàm băm phân bố đều.

Mệnh đề 2 — Xác suất lựa chọn

Nếu mỗi giá trị băm đồng khả năng:

$$P(h(K)=j)=\frac1b,$$

thì:

$$P(h(K)<a) =\sum_{j=0}^{a-1}\frac1b =\boxed{\frac ab}.$$

Đây là tính chất xác suất, cần giả thiết hàm băm đủ đều.

**Nên bổ sung**

Sinh viên dễ nhầm rằng “giữ 10% khóa” có nghĩa mỗi lần chạy giữ chính xác 10% số khóa. Thực tế, xác suất 10% áp dụng cho từng khóa theo việc chọn hàm băm; số khóa thực tế được chọn có thể dao động.

**Prompt chỉnh sửa**

> Chia slide thành hai định lý với hai nhãn: “Nhất quán — tất định” và “Tỷ lệ lựa chọn — xác suất”. Dưới mỗi định lý ghi giả thiết, chứng minh ngắn và ví dụ. Thêm chú thích 10% không đồng nghĩa chính xác 10% số khóa trong một lần chạy.

## Slide 18. Chọn khóa lấy mẫu

**Giải thích để giảng**

Việc chọn khóa là quyết định về mặt thống kê, không chỉ về mặt lập trình.

Nguyên tắc:

$$\boxed{\text{Khóa phải nhận diện đơn vị được thống kê.}}$$

Ví dụ:

| Thống kê mong muốn | Khóa phù hợp |
| --- | --- |
| Tỷ lệ truy vấn lặp của một người | `userID` |
| Số người sử dụng một từ khóa tìm kiếm | `query` |
| Số lần một người lặp lại cùng một truy vấn | `(userID, query)` |

Giải thích trường hợp sai:

Nếu dùng `(userID, timestamp)`, mỗi truy vấn của cùng một người thường có khóa khác nhau. Do đó những truy vấn của cùng người không còn được buộc giữ hoặc bỏ cùng nhau.

**Nên bổ sung**

Đưa thêm trường hợp khóa quá thô: sử dụng `country` thay vì `userID`. Khi đó cùng quốc gia được chọn hoặc loại cùng nhau, có thể làm mẫu mất tính đa dạng và có phương sai lớn.

**Prompt chỉnh sửa**

> Chuyển bảng thành bài tập kéo-thả hoặc ghép cặp giữa ba thống kê và ba loại khóa. Thêm hai trường hợp chọn sai: khóa quá chi tiết `(userID,time)` và khóa quá thô `country`. Yêu cầu sinh viên giải thích thông tin nào bị phá vỡ.

## Slide 19. Chi phí: lấy mẫu theo khóa

**Giải thích để giảng**

Mỗi bản ghi chỉ cần:

1. Một lần tính hàm băm.
2. Một lần so sánh.
3. Có thể ghi bản ghi vào mẫu.

Chi phí xử lý:

$$T_{\text{update}}=O(1)$$

nếu chi phí băm khóa được coi là hằng số.

Trạng thái quyết định cỡ hằng, nhưng dữ liệu mẫu đã lưu có thể tăng không giới hạn.

Với $r$ bản ghi và xác suất giữ mỗi khóa là $a/b$:

$$E[|Sample_r|]=\frac ab r.$$

Công thức đúng theo tuyến tính kỳ vọng ngay cả khi các bản ghi cùng khóa không được chọn độc lập.

**Nên bổ sung**

Giải thích phân biệt cực kỳ quan trọng:

- Bộ nhớ của bộ quyết định lấy mẫu có thể là $O(1)$.
- Bộ nhớ nếu giữ toàn bộ bản ghi được chọn trong RAM không phải $O(1)$.

Một khóa rất lớn được chọn có thể khiến mẫu vượt ngân sách dù kỳ vọng kích thước mẫu vẫn hợp lý.

**Prompt chỉnh sửa**

> Tách bảng chi phí thành hai phần: chi phí quyết định và chi phí lưu mẫu. Minh họa một khóa có tần suất rất lớn làm mẫu tăng đột biến. Nhấn mạnh $\mathbb E[|Sample|]=(a/b)r$ là kỳ vọng, không phải giới hạn bộ nhớ.

## Slide 20. Ngưỡng băm và khóa nhiều bộ

**Giải thích để giảng**

Cho hàm băm trả về một trong 100 giá trị từ 0 đến 99.

Muốn chọn 20% khóa, phải dùng:

$$h(K)<20.$$

Tập giá trị được giữ gồm 0 đến 19, đúng 20 giá trị.

Nếu một khóa xuất hiện một triệu lần, thuật toán chỉ có hai khả năng: giữ cả một triệu bản ghi hoặc bỏ toàn bộ.

Đó là lý do lấy mẫu theo khóa bảo toàn nhóm nhưng không bảo đảm kích thước mẫu.

**Nên bổ sung**

Đặt câu hỏi: “Nếu cần giữ tối đa 1.000 bản ghi, liệu chỉ hạ ngưỡng băm có bảo đảm không vượt 1.000 không?”

Câu trả lời là không nếu vẫn bắt buộc giữ trọn từng khóa. Đây là mâu thuẫn giữa yêu cầu giữ nhóm nguyên vẹn và giới hạn kích thước cứng, dẫn tự nhiên sang reservoir sampling.

**Prompt chỉnh sửa**

> Thêm thanh băm 100 ngăn và trường hợp một người dùng có một triệu bản ghi. Đối chiếu hai kết quả: đúng 20% xác suất chọn khóa, nhưng số bản ghi thực tế không cố định. Kết thúc bằng câu hỏi chuyển tiếp: “Làm sao giữ chính xác $s$ vị trí?”

# Phần III. Lấy mẫu hồ chứa (Reservoir Sampling)

Phần này nên tập trung vào hai câu hỏi: tại sao phải thay phần tử cũ và tại sao quy tắc thay lại tạo ra xác suất $s/r$?

## Slide 21. Lấy mẫu hồ chứa

**Giải thích để giảng**

Bài toán thay đổi: bây giờ bộ nhớ chỉ đủ giữ $s$ phần tử, không được vượt quá.

Nếu biết trước dòng dài $N$, ta có thể chọn ngẫu nhiên $s$ vị trí trong $N$ vị trí. Nhưng khi dòng đang đến, chưa biết $N$ là bao nhiêu.

Reservoir sampling giải quyết chính ràng buộc này.

**Nên bổ sung**

Dùng ví dụ một bảng khảo sát chỉ có 100 chỗ. Ban đầu giữ 100 người đầu tiên; khi có người thứ 101, cần cho người này một cơ hội công bằng để được chọn, thay vì tự động loại.

**Prompt chỉnh sửa**

> Minh họa dòng phần tử không có điểm kết thúc và một hồ chứa có đúng $s$ ô. Trực quan hóa sự khác biệt giữa “giữ 10% dòng” và “giữ đúng 100 phần tử”. Đặt câu hỏi: “Làm sao công bằng với cả phần tử đến sớm và đến muộn?”

## Slide 22. Mẫu cỡ cố định

**Giải thích để giảng**

Sau khi đã thấy $r$ phần tử và $r\ge s$, mỗi phần tử phải có cơ hội như nhau:

$$\boxed{P(x_i\in W)=\frac sr}.$$

Với $s=2$:

- Sau 5 phần tử: mỗi phần tử có xác suất $2/5$.
- Sau 7 phần tử: mỗi phần tử có xác suất $2/7$.

Xác suất của phần tử cũ phải giảm khi dòng dài ra, vì tổng số ô giữ lại không đổi.

**Nên bổ sung**

Dùng phép kiểm tra trực giác:

$$\sum_{i=1}^rP(x_i\in W)=r\frac sr=s.$$

Đây là kỳ vọng số vị trí được chọn, đúng bằng sức chứa của hồ.

**Prompt chỉnh sửa**

> Thêm sơ đồ bảy phần tử cạnh hồ chứa hai ô. Hiển thị xác suất $2/5$ tại mốc năm phần tử và $2/7$ tại mốc bảy phần tử. Trực quan hóa xác suất giảm theo độ dài dòng trong khi kích thước hồ không đổi.

## Slide 23. Ý tưởng lấy mẫu hồ chứa

**Giải thích để giảng**

Thuật toán thực hiện hai giai đoạn.

Khi $r\le s$, lưu trực tiếp phần tử thứ $r$ vào ô thứ $r$.

Khi $r>s$, sinh:

$$j\sim Uniform\{1,2,\ldots,r\}.$$

Nếu $j\le s$, phần tử mới thay phần tử trong ô $j$. Nếu $j>s$, loại phần tử mới.

Tại sao quy tắc này hợp lý?

Vì có đúng $s$ giá trị nhận trong $r$ giá trị đồng khả năng:

$$P(j\le s)=\frac sr.$$

Một lần rút số đã giải quyết cả hai việc: quyết định có nhận phần tử mới không và xác định ô bị thay.

**Nên bổ sung**

So sánh với phương án hai bước tương đương:

1. Nhận phần tử mới với xác suất $s/r$.
2. Nếu nhận, chọn đều một trong $s$ ô để thay.

Phương án dùng một số nguyên $j$ gọn hơn, nhưng có cùng phân phối.

**Prompt chỉnh sửa**

> Làm sơ đồ quyết định: sinh số $j$ từ 1 đến $r$, kiểm tra $j\le s$, sau đó thay ô $j$ hoặc bỏ phần tử. Dùng hai màu khác nhau cho các giá trị $j$ dẫn đến nhận và loại. Thêm xác suất $s/r$ ngay cạnh nhánh nhận.

## Slide 24. Ví dụ: vết chạy hồ chứa hai ô

**Giải thích để giảng**

Cho dòng:

$$a,x,c,y,z$$

và $s=2$. Các giá trị ngẫu nhiên lần lượt là $j=2,4,1$ từ bước 3.

| Bước $r$ | Phần tử | Số $j$ | Hồ chứa sau bước |
| --- | --- | --- | --- |
| 1 | a | — | [a, —] |
| 2 | x | — | [a, x] |
| 3 | c | 2 | [a, c] |
| 4 | y | 4 | [a, c] |
| 5 | z | 1 | [z, c] |

Ở bước 3, $j=2$, nên c thay ô thứ 2.

Ở bước 4, $j=4>s$, nên y bị bỏ.

Ở bước 5, $j=1$, nên z thay ô thứ 1.

**Nên bổ sung**

Phân biệt xác suất của thuật toán với kết quả của một lần chạy.

Sau năm phần tử, hồ là `[z,c]`, nhưng điều đó không có nghĩa z và c có xác suất cao hơn các phần tử khác. Trong các lần chạy khác, hồ có thể chứa các cặp khác.

(Bản gốc kèm một minh họa vết chạy tương tác năm bước; không chép lại.)

**Prompt chỉnh sửa**

> Chuyển vết chạy từ bảng tĩnh thành hoạt cảnh năm bước, mỗi bước chỉ làm thay đổi ô liên quan. Hiển thị $r$, phần tử mới, $j$, điều kiện $j\le2$ và trạng thái hồ. Làm rõ dãy $j$ là một lần thực thi minh họa, không phải một định luật xác suất.

## Slide 25. Thuật toán: lấy mẫu hồ chứa

**Giải thích để giảng**

Giả mã đầy đủ:

```
RESERVOIR(stream, s):
    W = []
    r = 0

    for x in stream:
        r = r + 1

        if r <= s:
            W[r] = x
        else:
            j = UniformInteger(1, r)

            if j <= s:
                W[j] = x
```

Có hai bất biến cần quan tâm:

- Kích thước: $|W|=\min(r,s)$.
- Xác suất: với $r\ge s$, mỗi vị trí đã thấy có xác suất $s/r$ ở trong hồ.

Thuật toán không cần biết độ dài cuối cùng của dòng.

**Nên bổ sung**

Xét $s=1$: sau phần tử thứ $r$, nhận phần tử mới với xác suất $1/r$.

Đây là trường hợp đơn giản nhất để sinh viên hiểu thuật toán trước khi chứng minh trường hợp tổng quát.

**Prompt chỉnh sửa**

> Trình bày giả mã có đánh số dòng, sử dụng đúng chỉ số bắt đầu từ 1. Đánh dấu đoạn khởi tạo, đoạn nhận $s$ phần tử đầu và đoạn thay ngẫu nhiên. Thêm ví dụ biên $s=1$ với xác suất $1/r$.

## Slide 26. Tính đúng: lấy mẫu hồ chứa

**Giải thích để giảng**

Bất biến cần chứng minh là:

$$\forall i\le r,\qquad P(x_i\in W_r)=\frac sr.$$

Chứng minh bằng quy nạp theo $r$.

Cơ sở: Khi $r=s$, tất cả $s$ phần tử đầu được giữ:

$$P(x_i\in W_s)=1=\frac ss.$$

Bước quy nạp: Giả sử sau $r$ phần tử, mệnh đề đúng. Khi phần tử thứ $r+1$ đến, phải chứng minh xác suất cho hai loại:

- Phần tử mới $x_{r+1}$.
- Mọi phần tử cũ $x_i$, với $i\le r$.

Tại sao tách hai loại? Vì phần tử mới đi vào từ ngoài hồ, còn phần tử cũ có thể bị thay thế.

**Nên bổ sung**

Một phương pháp chứng minh mạnh hơn cũng đúng với thuật toán này: trong điều kiện rút số đều và độc lập, mỗi tập con gồm $s$ vị trí trong $r$ vị trí có cùng xác suất

$$\frac1{\binom rs}.$$

Đây là tính chất uniform sample without replacement. Nó mạnh hơn việc chỉ bảo đảm xác suất biên $s/r$. Có thể đưa thành phần mở rộng cho sinh viên khá.

**Prompt chỉnh sửa**

> Chuyển slide thành cấu trúc chứng minh quy nạp: mệnh đề, cơ sở $r=s$, giả thiết tại $r$, hai trường hợp tại $r+1$. Thêm sơ đồ phân nhánh phần tử mới/phần tử cũ. Đưa tính đều của mọi tập con kích thước $s$ vào ô mở rộng.

## Slide 27. Chứng minh: xác suất có mặt, phần tử mới

**Giải thích để giảng**

Ở thời điểm $r+1$, thuật toán sinh:

$$j\sim Uniform\{1,\ldots,r+1\}.$$

Phần tử mới được nhận nếu $j\le s$.

Do đó:

$$\boxed{P(x_{r+1}\in W_{r+1})=\frac{s}{r+1}}.$$

Ví dụ $s=2,r+1=5$, có năm giá trị có thể rút:

$$j\in\{1,2,3,4,5\}.$$

Hai giá trị 1, 2 nhận phần tử mới, nên xác suất bằng $2/5$.

Phần chứng minh này không cần giả thiết quy nạp về các phần tử cũ.

**Nên bổ sung**

Làm rõ sau khi nhận, phần tử mới chắc chắn nằm trong hồ ngay sau bước đó; không có lần thay thứ hai trong cùng bước.

**Prompt chỉnh sửa**

> Vẽ năm ô đồng khả năng $j=1,\ldots,5$; đánh dấu hai ô nhận và ba ô loại. Đặt công thức $2/5$ bên cạnh, sau đó tổng quát hóa thành $s/(r+1)$. Không dùng bảng dài.

## Slide 28. Chứng minh: xác suất có mặt, phần tử cũ

**Giải thích để giảng**

Đây là bước quan trọng nhất của chứng minh hồ chứa.

Xét một phần tử cũ $x_i$.

Theo giả thiết quy nạp:

$$P(x_i\in W_r)=\frac sr.$$

Nếu $x_i$ đang nằm trong hồ, nó chỉ bị thay khi $j$ trúng đúng ô chứa nó.

Trong $r+1$ giá trị có thể rút của $j$, chỉ có một giá trị làm điều đó:

$$P(\text{bị thay}\mid x_i\in W_r)=\frac1{r+1}.$$

Vì thế xác suất sống sót:

$$P(\text{sống sót}\mid x_i\in W_r) =1-\frac1{r+1} =\frac r{r+1}.$$

Nhân hai xác suất:

$$\begin{aligned} P(x_i\in W_{r+1}) &=P(x_i\in W_r)\, P(\text{sống sót}\mid x_i\in W_r)\\ &=\frac sr\frac r{r+1}\\ &=\boxed{\frac{s}{r+1}}. \end{aligned}$$

Như vậy phần tử cũ và phần tử mới đều có xác suất đích như nhau.

**Nên bổ sung**

Giải thích kỹ vì sao xác suất bị thay là $1/(r+1)$, không phải $s/(r+1)$.

- $s/(r+1)$: xác suất có một ô nào đó bị thay.
- $1/(r+1)$: xác suất ô cụ thể đang chứa $x_i$ bị thay.

Đây là lỗi sinh viên rất dễ mắc.

**Prompt chỉnh sửa**

> Tách chứng minh thành hai bước rõ ràng: xác suất đang có trong hồ và xác suất sống sót. Dùng sơ đồ hồ $s$ ô, khoanh riêng một ô chứa $x_i$. Phân biệt trực quan $s/(r+1)$ là xác suất nhận phần tử mới, còn $1/(r+1)$ là xác suất thay đúng ô đang xét.

## Slide 29. Chi phí: lấy mẫu hồ chứa

**Giải thích để giảng**

Mỗi phần tử chỉ cần tăng biến đếm $r$, có thể rút một số $j$, và có thể thay một ô.

Vì vậy, trong mô hình RAM chuẩn:

$$T_{\text{update}}=O(1),\qquad Memory=O(s).$$

Số lần ghi phần tử vào hồ sau $r>s$ có kỳ vọng:

$$E[\text{số lần ghi}] =s+\sum_{i=s+1}^{r}\frac si.$$

Với số điều hòa $H_r=\sum_{i=1}^r1/i$:

$$E[\text{số lần ghi}] =s+s(H_r-H_s) \approx s\left(1+\ln\frac rs\right).$$

Điều này cho thấy số phần tử phải ghi lại thấp hơn rất nhiều so với tổng số phần tử đến khi $r$ lớn.

**Nên bổ sung**

Cận $O(1)$ giả định phép sinh số nguyên đều trong $\{1,\ldots,r\}$ và truy cập mảng có chi phí hằng số. Trong cài đặt thực tế, cần bảo đảm bộ sinh không tạo thiên lệch do phép lấy modulo không phù hợp.

**Prompt chỉnh sửa**

> Tóm tắt chi phí trong hai chỉ số chính: $O(1)$ cập nhật và $O(s)$ ô nhớ. Chuyển công thức tổng số lần ghi kỳ vọng sang phần mở rộng, minh họa bằng biểu đồ số phần tử đã đọc và số lần thực sự thay ô.

## Slide 30. Hồ chứa và mẫu theo khóa

**Giải thích để giảng**

So sánh hai giải pháp:

| Tiêu chí | Mẫu theo khóa | Hồ chứa |
| --- | --- | --- |
| Đơn vị chọn | Khóa | Vị trí |
| Kích thước mẫu | Không cố định | Cố định |
| Bảo toàn nhóm | Có | Không |
| Xác suất | $a/b$ mỗi khóa | $s/r$ mỗi vị trí |

Bài toán trên slide: Có 1.000 bản ghi, An xuất hiện 10 lần, hồ chứa kích thước 100.

Gọi $X_i$ là biến chỉ báo bản ghi thứ $i$ của An có trong hồ.

$$E[X_i]=\frac{100}{1000}=0{,}1.$$

Theo tính tuyến tính của kỳ vọng:

$$E\left[\sum_{i=1}^{10}X_i\right] =10(0{,}1)=\boxed{1}.$$

Nghĩa là trung bình trong các lần chạy, khoảng một bản ghi của An được giữ, chứ không phải đủ mười bản ghi.

**Nên bổ sung**

Kỳ vọng bằng 1 không có nghĩa mỗi lần chạy đều có đúng một bản ghi của An. Có thể không có bản ghi nào hoặc có nhiều bản ghi.

Hồ chứa chọn đều theo vị trí, không có nghĩa tự động đại diện tốt cho từng nhóm hiếm hay cho phân phối hiện tại khi dòng có hiện tượng concept drift.

**Prompt chỉnh sửa**

> Thêm hình một người dùng có 10 sự kiện nằm rải trong 1.000 sự kiện; hồ chứa lấy 100 vị trí. Đặt hai câu hỏi riêng: kỳ vọng số sự kiện của An và xác suất giữ nguyên cả nhóm. Kết luận bằng tiêu chí lựa chọn giữa hai thuật toán, không dùng một thuật toán thay thế thuật toán kia.

# Phần IV. Lọc thành viên bằng Bloom Filter

Phần này có hai ý tưởng sinh viên cần hiểu trước khi học công thức:

1. Bit bằng 0 có giá trị kết luận mạnh hơn bit bằng 1.
2. Thêm hàm băm giúp giảm nhầm lẫn, nhưng đồng thời làm mảng bit nhanh đầy hơn.

## Slide 31. Lọc thành viên bằng Bloom filter

**Giải thích để giảng**

Hai thuật toán trước đều dùng để chọn mẫu. Bloom filter có nhiệm vụ khác: kiểm tra một khóa có thể thuộc tập $S$ hay không.

Ví dụ một hệ thống có hàng tỷ địa chỉ được phép, nhưng không thể giữ tất cả trong RAM.

Bloom filter lưu một biểu diễn nhỏ của tập, chấp nhận đôi khi trả lời “có thể thuộc” cho khóa thực sự không thuộc.

**Nên bổ sung**

Đưa ví dụ thực tế: trước khi truy vấn cơ sở dữ liệu trên đĩa hoặc qua mạng, kiểm tra Bloom filter để tránh những truy vấn chắc chắn không tìm thấy kết quả.

**Prompt chỉnh sửa**

> Thiết kế slide chuyển tiếp với hai loại câu hỏi: “Chọn phần tử nào?” của sampling và “Khóa này có thuộc tập không?” của Bloom filter. Thêm minh họa Bloom filter đứng trước cơ sở dữ liệu chính xác.

## Slide 32. Lọc theo danh sách cho phép

**Giải thích để giảng**

Có $m=10^9$ địa chỉ, mỗi địa chỉ khoảng 20 byte.

Nếu lưu trực tiếp:

$$10^9\times20=20\times10^9\text{ byte},$$

tức khoảng 20 GB dữ liệu thô, chưa kể chi phí cấu trúc dữ liệu.

Nhưng RAM cho bộ lọc chỉ có 1 GB:

$$n=8\times10^9\text{ bit}.$$

Bài toán: dùng 1 GB để tránh phải tra đĩa cho phần lớn địa chỉ không hợp lệ.

**Nên bổ sung**

Phân biệt việc dùng Bloom filter làm bộ lọc sơ bộ với dùng nó làm nguồn xác thực duy nhất. Trường hợp thuộc danh sách cho phép vẫn cần kiểm tra chính xác trước quyết định có yêu cầu độ tin cậy tuyệt đối.

**Prompt chỉnh sửa**

> Chuyển tình huống 20 GB dữ liệu và 1 GB RAM thành sơ đồ tỷ lệ kích thước. Minh họa hai lộ trình: không có Bloom filter phải tra đĩa cho mọi thư, có Bloom filter chỉ các khóa “có thể thuộc” mới tra đĩa.

## Slide 33. Ý tưởng Bloom filter

**Giải thích để giảng**

Khởi tạo mảng:

$$B[0],B[1],\ldots,B[n-1]=0.$$

Khi thêm khóa $x$, tính $k$ hàm băm:

$$h_1(x),h_2(x),\ldots,h_k(x).$$

Sau đó đặt các bit tương ứng thành 1.

Khi truy vấn $y$:

- Nếu có ít nhất một vị trí $h_i(y)$ đang bằng 0, kết luận chắc chắn không thuộc.
- Nếu tất cả bằng 1, chỉ kết luận có thể thuộc.

Vì nhiều khóa khác nhau có thể cùng đặt một bit bằng 1, không thể suy luận ngược từ bit 1 ra thành viên thực.

**Nên bổ sung**

Dùng hình ảnh nhiều chìa khóa cùng bật một công tắc: công tắc đang bật không cho biết chìa khóa cụ thể nào đã bật nó.

**Prompt chỉnh sửa**

> Vẽ mảng bit 12–16 ô. Cho hai khóa lần lượt đặt bit thông qua hai hàm băm. Minh họa một khóa truy vấn gặp bit 0 và một khóa truy vấn có tất cả bit bằng 1. Ghi rõ hai kết quả: Definitely Not Present và Possibly Present.

## Slide 34. Ví dụ: Bloom filter 11 bit, thêm ba khóa

**Giải thích để giảng**

Mảng có 11 bit, chỉ số từ 0 đến 10.

Hai hàm băm được xây bằng cách tách các vị trí bit lẻ/chẵn trong biểu diễn nhị phân rồi lấy modulo 11.

Ba khóa được thêm:

| Khóa | $h_1(x)$ | $h_2(x)$ |
| --- | --- | --- |
| 25 | 5 | 2 |
| 159 | 7 | 0 |
| 585 | 9 | 7 |

Các bước:

1. Thêm 25: đặt bit 5 và 2.
2. Thêm 159: đặt bit 7 và 0.
3. Thêm 585: đặt bit 9 và 7.

Bit 7 đã bằng 1 khi thêm 585, do đó không có thay đổi tại vị trí này.

Mảng cuối:

```
Index: 0 1 2 3 4 5 6 7 8 9 10
Bit:   1 0 1 0 0 1 0 1 0 1  0
```

**Nên bổ sung**

Giải thích rõ phép tách bit. Ví dụ $159=10011111_2$, đếm vị trí từ phải bắt đầu tại 1:

- Các bit vị trí lẻ ghép lại thành $0111_2=7$.
- Các bit vị trí chẵn ghép lại thành $1011_2=11$, lấy modulo 11 được 0.

Phép băm này là ví dụ minh họa trong tài liệu, không phải một cách băm được khuyến nghị cho hệ thống thực tế.

**Prompt chỉnh sửa**

> Tách ví dụ thành ba bước thêm khóa. Mỗi bước hiển thị số nhị phân, hai giá trị băm và trạng thái mảng 11 bit. Đánh dấu bit 7 bị va chạm khi thêm 585. Cố định thứ tự chỉ số 0–10 từ trái sang phải trong toàn bộ hình.

## Slide 35. Ví dụ: Bloom filter 11 bit, kiểm tra hai khóa

**Giải thích để giảng**

Bây giờ kiểm tra khóa 118:

$$h_1(118)=3,\quad h_2(118)=5.$$

Bit 3 bằng 0, nên:

$$118\notin S.$$

Không cần kiểm tra tiếp.

Tiếp theo, khóa 29:

$$h_1(29)=7,\quad h_2(29)=2.$$

Cả hai bit đều bằng 1. Bloom filter trả lời “có thể thuộc”.

Nhưng tập đã thêm chỉ gồm $\{25,159,585\}$, không có 29.

Vậy 29 là một false positive.

**Nên bổ sung**

Đây là slide nên yêu cầu sinh viên tự trả lời trước khi hiện đáp án. Đặc biệt làm rõ rằng hai vị trí của 29 có thể được bật bởi những khóa khác nhau; không cần tồn tại một khóa nào trước đó có cùng cả hai vị trí băm.

**Prompt chỉnh sửa**

> Đặt hai truy vấn 118 và 29 dưới cùng một mảng bit. Làm nổi bật bit 3 bằng 0 của 118, và hai bit 7, 2 bằng 1 của 29. Với 29, ghi “Dương giả: khóa không thuộc tập nhưng qua bộ lọc”. Dùng hiệu ứng xuất hiện từng bước để sinh viên dự đoán.

## Slide 36. Đặc tả Bloom filter

**Giải thích để giảng**

Dùng các ký hiệu:

- $n$: Số bit của mảng.
- $m$: Số khóa phân biệt đã thêm.
- $k$: Số hàm băm.

Hai loại lỗi:

| Thực tế | Bloom trả lời | Loại |
| --- | --- | --- |
| Thuộc $S$ | Có thể thuộc | Đúng |
| Không thuộc $S$ | Chắc chắn không thuộc | Đúng |
| Không thuộc $S$ | Có thể thuộc | Dương giả |
| Thuộc $S$ | Chắc chắn không thuộc | Âm giả |

Bloom filter chuẩn không phát sinh âm giả nếu tuân thủ các giả thiết vận hành.

**Nên bổ sung**

Sinh viên thường nhầm false positive là khóa hợp lệ bị loại. Hãy giải thích nhãn “positive” ở đây có nghĩa bộ lọc trả về kết quả có thể thuộc.

**Prompt chỉnh sửa**

> Thêm ma trận kết quả 2×2 giữa thành viên thực tế và kết quả Bloom filter. Đánh dấu false positive và false negative rõ ràng. Dùng các thuật ngữ “dương giả”, “âm giả” nhất quán với phần Machine Learning.

## Slide 37. Thuật toán: xây Bloom filter

**Giải thích để giảng**

Giả mã:

```
BUILD_BLOOM(S, n, h):
    B = [0] * n

    for x in S:
        for i in 1..k:
            B[h_i(x)] = 1

    return B
```

Mỗi khóa cần $k$ phép băm, tổng cộng:

$$T_{\text{build}}=\Theta(km).$$

Bộ nhớ mảng:

$$Memory=n\text{ bit}.$$

Việc đặt lại một bit vốn đã bằng 1 không gây vấn đề.

**Nên bổ sung**

Nhấn mạnh rằng $m$ là số khóa phân biệt, vì thêm lặp lại một khóa vào Bloom filter chuẩn không thay đổi trạng thái sau lần thêm đầu.

**Prompt chỉnh sửa**

> Giữ giả mã ngắn và thêm một ví dụ hai khóa cùng đặt chung một bit. Đánh dấu phép OR logic $B[h_i(x)]\leftarrow1$. Chốt chi phí xây dựng $km$ lần băm và $n$ bit bộ nhớ.

## Slide 38. Thuật toán: kiểm tra thành viên

**Giải thích để giảng**

Thuật toán:

```
QUERY_BLOOM(y, B, h):
    for i in 1..k:
        if B[h_i(y)] == 0:
            return DEFINITELY_NOT

    return POSSIBLY_PRESENT
```

Điều kiện dừng sớm rất quan trọng. Chỉ cần một bit bằng 0 là đã có đủ thông tin để kết luận.

Trong trường hợp xấu nhất, thuật toán cần kiểm tra $k$ bit:

$$T_{\text{query}}=O(k).$$

**Nên bổ sung**

Bloom filter thường được dùng trong hệ thống có tỷ lệ truy vấn không tìm thấy cao, vì những truy vấn này có thể được loại sớm mà không cần truy cập dữ liệu đắt tiền.

**Prompt chỉnh sửa**

> Chuyển giả mã truy vấn thành lưu đồ có nút quyết định “Bit đang xét bằng 0?”. Nhánh Yes trả về chắc chắn không thuộc ngay; nhánh No tiếp tục đến hàm băm kế tiếp. Thêm ví dụ 118 dừng ở bit đầu tiên và 29 phải đọc đủ hai bit.

## Slide 39. Tính đúng: không có âm giả

**Giải thích để giảng**

Cho $x\in S$.

Khi xây dựng, với mỗi hàm băm:

$$B[h_i(x)]\leftarrow1.$$

Nếu các bit không bị xóa hoặc đặt về 0, những vị trí này vẫn bằng 1 tại thời điểm truy vấn.

Khi kiểm tra $x$, thuật toán sẽ không gặp bit 0. Vì vậy:

$$\boxed{x\in S\Longrightarrow Bloom(x)=\text{Possibly Present}.}$$

Đây là chứng minh tất định, không cần giả thiết hàm băm phân bố đều.

**Nên bổ sung**

Giải thích tại sao không thể xóa trực tiếp một khóa bằng cách đặt tất cả bit của nó về 0.

Nếu hai khóa dùng chung một bit, việc xóa một khóa có thể làm khóa còn lại bị âm giả.

Có thể nhắc đến Counting Bloom Filter, sử dụng bộ đếm thay cho bit để hỗ trợ xóa, như kiến thức mở rộng.

**Prompt chỉnh sửa**

> Trình bày chứng minh không âm giả bằng ba bước: thêm khóa → các bit bằng 1 → truy vấn cùng hàm băm. Thêm một phản ví dụ xóa bit chung dẫn đến âm giả. Ghi rõ giả thiết không xóa bit và dùng cùng hàm băm, cùng trạng thái đã cập nhật.

## Slide 40. Xác suất một bit bằng 1

**Giải thích để giảng**

Đây là bước đầu tiên trong phân tích xác suất Bloom filter.

Xét một bit cố định $B[c]$.

Mỗi phép băm chọn đều một trong $n$ vị trí. Xác suất không chọn bit $c$:

$$1-\frac1n.$$

Có $m$ khóa, mỗi khóa dùng $k$ hàm băm, tổng cộng $km$ lần chọn vị trí.

Nếu các lần chọn độc lập:

$$P(B[c]=0)=\left(1-\frac1n\right)^{km}.$$

Do đó:

$$\boxed{q=P(B[c]=1) =1-\left(1-\frac1n\right)^{km}}.$$

Với $n$ lớn:

$$q\approx1-e^{-km/n}.$$

**Nên bổ sung**

Sử dụng mô hình ném phi tiêu:

- $n$ bia tương ứng $n$ bit.
- $km$ phi tiêu tương ứng $km$ lần băm.
- Một bia chưa trúng phi tiêu tương ứng bit còn bằng 0.

Cho ví dụ nhỏ: có 8 bit và 4 lần băm.

$$P(B[c]=0)=\left(\frac78\right)^4 \approx0{,}586.$$

**Prompt chỉnh sửa**

> Thêm minh họa ném $km$ phi tiêu vào $n$ bia. Dẫn công thức xác suất bit không trúng một lần, không trúng $km$ lần rồi lấy phần bù. Phân biệt rõ công thức hữu hạn chính xác dưới mô hình độc lập và công thức xấp xỉ mũ.

## Slide 41. Xác suất dương giả

**Giải thích để giảng**

Khóa $y\notin S$ tạo ra $k$ vị trí băm.

Nếu cả $k$ vị trí đều bằng 1, Bloom filter cho kết quả dương giả.

Xấp xỉ chuẩn:

$$p_{FP}\approx q^k.$$

Thay biểu thức của $q$:

$$p_{FP}\approx \left[ 1-\left(1-\frac1n\right)^{km} \right]^k.$$

Với $n$ lớn:

$$\boxed{p_{FP}\approx(1-e^{-km/n})^k.}$$

Tại sao chỉ là xấp xỉ?

Vì trạng thái các bit trong mảng không độc lập hoàn toàn. Các vị trí truy vấn cũng có thể trùng nhau.

Một biểu thức chính xác hơn dưới mô hình băm ngẫu nhiên độc lập là:

$$p_{FP} =E\left[\left(\frac Xn\right)^k\right],$$

trong đó $X$ là số bit bằng 1 sau khi xây dựng mảng. Nói chung:

$$E\left[\left(\frac Xn\right)^k\right] \ne \left(E\left[\frac Xn\right]\right)^k.$$

**Nên bổ sung**

Phân biệt mật độ bit kỳ vọng $q$ với xác suất dương giả. Với $k=1$, hai giá trị trùng nhau. Với $k>1$, xác suất dương giả phụ thuộc việc toàn bộ các vị trí băm cùng bằng 1.

Có thể đưa phần phụ thuộc xác suất và bất đẳng thức Jensen vào ghi chú nâng cao, không bắt buộc mọi sinh viên phải chứng minh.

**Prompt chỉnh sửa**

> Chia slide thành hai tầng: tầng chính dẫn công thức dương giả thông dụng $p_{FP}\approx(1-e^{-km/n})^k$; tầng mở rộng giải thích vì sao $q^k$ là xấp xỉ, với $X$ là số bit 1. Không dùng dấu bằng chính xác giữa $p_{FP}$ và $q^k$.

## Slide 42. Ảnh hưởng của số hàm băm

**Giải thích để giảng**

Tăng số hàm băm $k$ có hai tác động đối nghịch.

Tác động có lợi: một khóa ngoài tập phải vượt qua nhiều phép kiểm tra hơn.

Tác động bất lợi: mỗi khóa được thêm sẽ đặt thêm nhiều bit thành 1, khiến mảng nhanh đầy.

Khi $k$ rất lớn:

$$q=1-e^{-km/n}\longrightarrow1.$$

Suy ra:

$$p(k)=(1-e^{-km/n})^k\longrightarrow1.$$

Tức là gần như mọi truy vấn đều được trả lời “có thể thuộc”.

**Nên bổ sung**

Đây là một ví dụ điển hình về bài toán tối ưu cân bằng hai yếu tố đối nghịch. Không thể tăng số hàm băm vô hạn để cải thiện độ chính xác.

**Prompt chỉnh sửa**

> Dùng đồ thị dạng chữ U của xác suất dương giả theo $k$. Chú thích bên trái “quá ít phép kiểm tra”, bên phải “mảng bit bão hòa”. Đánh dấu vùng tối ưu ở giữa. Bổ sung đồ thị nhỏ cho tỷ lệ bit 1 tăng dần theo $k$, nếu không làm slide quá tải.

## Slide 43. Số hàm băm tối ưu

**Giải thích để giảng**

Cần tìm $k$ làm nhỏ nhất:

$$p(k)=(1-e^{-km/n})^k.$$

Lấy logarit để dễ đạo hàm:

$$\ell(k)=\ln p(k) =k\ln(1-e^{-km/n}).$$

Đặt:

$$\rho=\frac mn.$$

Đạo hàm:

$$\ell'(k) =\ln(1-e^{-k\rho}) +\frac{k\rho}{e^{k\rho}-1}.$$

Giải điểm dừng và kiểm tra dấu đạo hàm cho kết quả:

$$\boxed{k^*=\frac nm\ln2.}$$

Ý nghĩa rất đẹp: Ở số hàm băm tối ưu, xác suất một bit còn bằng 0 xấp xỉ $1/2$.

$$e^{-k^*m/n}=\frac12.$$

Do đó khoảng một nửa số bit bằng 1.

**Nên bổ sung**

Cho sinh viên hiểu $k^*$ là nghiệm liên tục của mô hình xấp xỉ. Trong thực tế $k$ phải là số nguyên dương; cần so sánh hai số nguyên lân cận, không chỉ làm tròn máy móc.

Phần chứng minh đạo hàm đổi dấu sẽ được giải đầy đủ ở slide 58.

**Prompt chỉnh sửa**

> Trình bày quá trình tối ưu thành ba bước: lấy logarit, tính đạo hàm, suy ra $k^*=(n/m)\ln2$. Bên cạnh công thức kết quả, vẽ mảng bit với khoảng 50% ô được bật để minh họa ý nghĩa điểm tối ưu. Đưa phần xét dấu đạo hàm dài sang slide bài tập cuối.

## Slide 44. Ví dụ: tám bit mỗi khóa

**Giải thích để giảng**

Với:

$$n=8\times10^9,\qquad m=10^9,$$

ta có:

$$\frac nm=8.$$

Số hàm băm tối ưu liên tục:

$$k^*=8\ln2\approx5{,}545.$$

So sánh $k=5$ và $k=6$:

$$p(5)=(1-e^{-5/8})^5\approx0{,}02168,$$

$$p(6)=(1-e^{-6/8})^6\approx0{,}02158.$$

Vậy chọn:

$$\boxed{k=6,\qquad p_{FP}\approx2{,}16\%.}$$

Ý nghĩa ứng dụng: Trong các địa chỉ không thuộc danh sách cho phép, khoảng 2,16% vẫn vượt qua Bloom filter và phải được kiểm tra chính xác.

Con số này không phải tỷ lệ thư rác trong toàn bộ dòng, cũng không phải xác suất một địa chỉ thực sự thuộc danh sách khi Bloom trả lời dương tính.

**Nên bổ sung**

Làm rõ số bit trên mỗi khóa:

$$\frac nm=8\text{ bit/khóa}.$$

Đây là đại lượng quan trọng hơn tổng $n$ và $m$ khi so sánh các cấu hình cùng tỷ lệ.

(Bản gốc kèm biểu đồ xác suất dương giả theo số hàm băm $k=1,\ldots,10$ theo xấp xỉ $p(k)=(1-\exp(-k/8))^k$; không chép lại.)

**Prompt chỉnh sửa**

> Giữ biểu đồ xác suất dương giả theo $k=1,\ldots,10$, dùng trục tung dạng phần trăm. Đánh dấu $k^*=5{,}545$ bằng đường nét đứt và tô nổi hai điểm $k=5,6$. Thêm phép thay số hoàn chỉnh cho $p(6)$ và kết luận chọn sáu hàm băm.

## Slide 45. Chi phí: Bloom filter

**Giải thích để giảng**

Chi phí xây dựng:

$$T_{\text{build}}=O(km).$$

Chi phí truy vấn trường hợp xấu:

$$T_{\text{query}}=O(k).$$

Bộ nhớ:

$$Memory=n\text{ bit}.$$

Bây giờ xét tình huống số khóa tăng gấp đôi nhưng vẫn giữ 1 GB RAM:

$$m=2\times10^9,\qquad n=8\times10^9.$$

Số bit trên mỗi khóa giảm từ 8 xuống 4.

Nếu vẫn giữ $k=6$:

$$p(6)=(1-e^{-6/4})^6\approx0{,}2198.$$

Tỷ lệ dương giả tăng lên gần 22%.

Tính lại:

$$k^*=4\ln2\approx2{,}77.$$

Nên chọn $k=3$, cho:

$$p(3)\approx0{,}1469.$$

**Nên bổ sung**

Khi số khóa tăng mà số bit không tăng tương ứng, chất lượng Bloom filter suy giảm. Việc thay đổi $k$ còn đòi hỏi thiết kế lại hoặc tái xây dựng bộ lọc cho đúng bộ hàm băm mới.

**Prompt chỉnh sửa**

> Tạo bảng so sánh hai kịch bản: một tỷ khóa và hai tỷ khóa, đều có 1 GB RAM. Hiển thị bit/khóa, $k$ tối ưu và xác suất dương giả. Dùng hai đường cong trên cùng hệ trục để làm rõ sự xuống cấp khi tập khóa tăng nhưng bộ nhớ không đổi.

# Phần V. Tổng kết và chuyển tiếp

## Slide 46. Tổng kết và chuyển tiếp

**Giải thích để giảng**

Đây là thời điểm quay lại câu hỏi mở đầu: “Vì sao không thể sử dụng một thuật toán chung để xử lý mọi yêu cầu trên dòng dữ liệu?”

Ba thuật toán khác nhau vì chúng giữ những loại thông tin khác nhau:

- Lấy mẫu theo khóa giữ nguyên cấu trúc nhóm.
- Hồ chứa giữ một số phần tử cố định.
- Bloom filter nén thông tin thành viên vào mảng bit.

**Nên bổ sung**

Nêu rõ hai thuộc tính không thể tùy tiện đánh đổi: sự nhất quán theo khóa và giới hạn kích thước cứng. Nếu một khóa chứa nhiều phần tử hơn dung lượng hồ, không thể vừa giữ trọn khóa đó vừa không vượt giới hạn.

**Prompt chỉnh sửa**

> Thiết kế slide chuyển tiếp thành ba câu hỏi lớn tương ứng ba thuật toán. Dùng cùng ví dụ dòng truy vấn đã sử dụng từ đầu bài, không thêm một tình huống mới.

## Slide 47. Kết quả và giả thiết không được bỏ

**Giải thích để giảng**

Tôi đề xuất sử dụng slide này như một bảng ghép giữa định lý và giả thiết.

| Kết quả | Giả thiết quan trọng |
| --- | --- |
| Cùng khóa cùng quyết định | Hàm băm giữ cố định |
| Xác suất giữ khóa $a/b$ | Băm đều |
| Xác suất hồ chứa $s/r$ | Số rút đều, độc lập với lịch sử |
| Bloom không âm giả | Không xóa bit cần thiết; cùng hàm băm |
| Công thức dương giả xấp xỉ | Mô hình băm đều, độc lập |
| $k^*=(n/m)\ln2$ | Tối ưu công thức xấp xỉ |

Điểm cần nhấn mạnh: tính đúng của một kết quả không thể tách khỏi các giả thiết tạo ra nó.

**Nên bổ sung**

Hỏi sinh viên: “Nếu dùng hàm băm không đều thì điều gì còn đúng?” Đáp án: sự nhất quán theo khóa vẫn đúng, nhưng xác suất lựa chọn $a/b$ không còn được bảo đảm.

**Prompt chỉnh sửa**

> Rút gọn bảng thành ba thuật toán, mỗi thuật toán có hai cột: Bảo đảm và Giả thiết. Thêm một phản ví dụ ngắn cho mỗi nhóm khi bỏ một giả thiết. Đặt công thức ở vị trí dễ đọc, không dồn tất cả vào một ô.

## Slide 48. Thuật toán, bảo đảm và chi phí

**Giải thích để giảng**

Sinh viên cần so sánh trên cùng một hệ tiêu chí.

| Thuật toán | Bộ nhớ | Chi phí cập nhật/truy vấn |
| --- | --- | --- |
| Theo khóa | $O(1)$ trạng thái quyết định | $O(1)$ mỗi bản ghi |
| Hồ chứa | $O(s)$ ô | $O(1)$ mỗi bản ghi |
| Bloom filter | $n$ bit | $O(k)$ mỗi khóa |

Lưu ý: bộ nhớ $O(1)$ của mẫu theo khóa chưa tính nơi lưu các bản ghi được xuất ra.

Bloom filter có thể nhận thêm khóa theo thời gian bằng cách đặt thêm bit, nhưng xác suất dương giả sẽ tăng nếu $n$ và $k$ không được thiết kế cho tổng số khóa dự kiến.

**Nên bổ sung**

Yêu cầu sinh viên so sánh cả memory complexity, update complexity và error guarantee, không chỉ một chỉ số.

**Prompt chỉnh sửa**

> Tạo bảng so sánh ba thuật toán có cùng bốn cột: Đơn vị xử lý, Bộ nhớ, Chi phí và Bảo đảm. Chú thích riêng bộ nhớ của bộ quyết định theo khóa và bộ nhớ lưu mẫu, tránh thể hiện sai là toàn bộ mẫu chỉ dùng $O(1)$.

## Slide 49. Câu trả lời cho vấn đề trung tâm

**Giải thích để giảng**

Quay lại ba câu hỏi của phần mở đầu.

Thứ nhất, khi cần giữ đầy đủ dữ liệu của 10% người dùng, dùng hàm băm theo `userID`.

Thứ hai, khi chỉ có $s$ ô nhớ, dùng reservoir sampling để sau $r$ phần tử, mỗi vị trí được giữ với xác suất $s/r$.

Thứ ba, khi cần lọc nhanh tập một tỷ địa chỉ, dùng Bloom filter với 8 bit/khóa và khoảng sáu hàm băm để có tỷ lệ dương giả xấp xỉ 2,16%.

**Nên bổ sung**

Chỉnh cách diễn đạt về $1/29$: đây là tỷ số của các số đếm kỳ vọng trong ví dụ mẫu từng bản ghi, không phải tỷ lệ luôn quan sát được của người dùng An.

**Prompt chỉnh sửa**

> Trả lời trực tiếp ba câu hỏi ở slide mở đầu. Mỗi câu có một thuật toán và một kết quả số. Sửa cách diễn đạt $1/29$ thành “tỷ số các số đếm kỳ vọng trong mẫu” và phân biệt với tỷ lệ gốc $1/2$.

## Slide 50. Câu hỏi tự kiểm tra, câu 1–2

**Giải thích để giảng**

Câu 1: Muốn giữ 5% người dùng, hàm băm nhận giá trị 0–99.

Điều kiện:

$$h(userID)<5.$$

Lấy 5% từng bản ghi là không phù hợp nếu cần giữ quan hệ giữa các lần truy vấn của cùng một người dùng.

Câu 2: Hồ chứa kích thước $s=50$, đã xử lý $r=1000$ phần tử.

Xác suất phần tử thứ 7 vẫn nằm trong hồ:

$$P(x_7\in W_{1000}) =\frac{50}{1000} =\boxed{0{,}05}.$$

Để chứng minh, cần giả thiết các số rút đều và độc lập với lịch sử trước đó.

**Nên bổ sung**

Yêu cầu sinh viên giải thích tại sao phần tử thứ 7 và phần tử thứ 999 có xác suất được giữ bằng nhau, dù thời điểm đến rất khác nhau.

**Prompt chỉnh sửa**

> Chuyển hai câu hỏi thành bài kiểm tra nhanh trên lớp: hiển thị câu hỏi trước, đáp án và giải thích xuất hiện ở lần bấm tiếp theo. Bổ sung câu hỏi phụ về sự công bằng giữa phần tử đến sớm và đến muộn.

## Slide 51. Câu hỏi tự kiểm tra, câu 3–4

**Giải thích để giảng**

Câu 3: Bloom filter có thể loại nhầm khóa đã thêm không?

Trong mô hình chuẩn, không. Khi xây dựng, tất cả các bit băm của khóa đã được đặt thành 1 và không bị xóa sau đó.

Câu 4: Nếu tăng gấp đôi $n$, giữ nguyên $m$, điều gì xảy ra?

Số hàm băm tối ưu:

$$k^*=\frac nm\ln2$$

tăng gấp đôi.

Tại điểm tối ưu liên tục:

$$p(k^*)=2^{-k^*}.$$

Vì vậy xác suất dương giả tối ưu mới bằng bình phương giá trị cũ.

Ví dụ từ 8 bit/khóa lên 16 bit/khóa:

$$0{,}0214^2\approx0{,}00046.$$

Tức giảm từ khoảng 2,14% xuống 0,046% theo công thức tối ưu liên tục.

**Nên bổ sung**

Đây là vị trí tốt để giới thiệu công thức định cỡ ngược. Nếu cần tỷ lệ dương giả mục tiêu $p$, số bit trên mỗi khóa xấp xỉ:

$$\boxed{\frac nm\approx-\frac{\ln p}{(\ln2)^2}}.$$

Ví dụ mục tiêu 1% cần khoảng 9,59 bit/khóa, với khoảng 7 hàm băm.

**Prompt chỉnh sửa**

> Bổ sung phép tính khi tăng gấp đôi số bit trên mỗi khóa và biểu đồ so sánh FPR. Trong ghi chú mở rộng, thêm công thức định cỡ $n/m=-\ln(p)/(\ln2)^2$ và ví dụ tỷ lệ dương giả mục tiêu 1%.

## Slide 52. Nguồn và tài liệu đọc

**Giải thích để giảng**

Giải thích vai trò của từng nguồn thay vì chỉ liệt kê.

Tài liệu chính là Mining of Massive Datasets. Các phần tương ứng:

- §4.1: Mô hình dòng dữ liệu.
- §4.2: Lấy mẫu dòng và chọn khóa.
- §4.3: Bloom filter.
- §4.5.5: Reservoir sampling.

Các slide MMDS và bài giảng Stanford CS246 bổ sung hình minh họa, ví dụ và bài tập.

**Nên bổ sung**

Đưa đường dẫn tài liệu đọc và ghi rõ mục nào là bắt buộc, mục nào nâng cao. Các chứng minh xác suất có thể đọc lại trong ghi chú bài giảng.

**Prompt chỉnh sửa**

> Biên tập slide tài liệu thành danh mục ngắn có liên kết: sách chính, slide MMDS, bài giảng CS246, ghi chú tiếng Việt. Gắn phần nội dung tương ứng cho từng nguồn, dùng kích thước chữ đủ đọc khi trình chiếu.

# Phần VI. Bài tập vận dụng

## Slide 53. Bài tập vận dụng

**Giải thích để giảng**

Đây là phần chuyển từ việc hiểu thuật toán sang việc sử dụng thuật toán.

Bốn bài tập kiểm tra bốn năng lực:

- Chọn khóa theo đơn vị thống kê.
- Tính xác suất dương giả.
- Phân tích cách tổ chức mảng bit.
- Tối ưu số hàm băm bằng giải tích.

**Nên bổ sung**

Cho sinh viên phân biệt câu hỏi cần chứng minh với câu hỏi chỉ cần thay số. Đặc biệt bài tối ưu số hàm băm không thể chỉ ghi công thức có sẵn nếu yêu cầu chứng minh.

**Prompt chỉnh sửa**

> Chuyển phần giới thiệu bài tập thành bảng bốn bài với kiến thức được kiểm tra và độ khó dự kiến. Đánh dấu bài chọn khóa và tính xác suất là cơ bản, bài chia mảng và tối ưu bằng đạo hàm là nâng cao.

## Slide 54. Bài tập: chọn khóa lấy mẫu

**Giải thích để giảng**

Bảng:

`Grades(university, courseID, studentID, grade)`

Chú ý mã học phần và mã sinh viên chỉ duy nhất trong phạm vi một trường.

Ý a: Ước lượng số sinh viên trung bình của một học phần, theo từng trường.

Đơn vị thống kê là một học phần trong một trường, nên khóa:

$$\boxed{(\text{university},\text{courseID})}.$$

Ý b: Tỷ lệ sinh viên có điểm trung bình từ 3,5 trở lên.

Muốn tính điểm trung bình của một sinh viên, phải giữ toàn bộ điểm của người đó, nên khóa:

$$\boxed{(\text{university},\text{studentID})}.$$

Ý c: Tỷ lệ học phần có ít nhất một nửa sinh viên đạt A.

Phải giữ đầy đủ các điểm của từng học phần để biết tỷ lệ A, nên khóa:

$$\boxed{(\text{university},\text{courseID})}.$$

**Nên bổ sung**

Giải thích tại sao luôn phải có `university`: mã sinh viên 123 ở trường A và mã sinh viên 123 ở trường B có thể thuộc hai người khác nhau.

Cũng cần phân biệt thống kê số sinh viên trung bình theo học phần với thống kê tỷ lệ bản ghi điểm: hai đại lượng không giống nhau nếu số sinh viên mỗi học phần khác nhau.

**Prompt chỉnh sửa**

> Chia bài tập thành ba câu trên ba màn hình hoặc ba bước xuất hiện. Mỗi câu yêu cầu xác định đơn vị thống kê trước rồi mới chọn khóa. Thêm phản ví dụ mã sinh viên trùng nhau ở hai trường. Hiển thị khóa đáp án dưới dạng tuple rõ ràng.

## Slide 55. Bài tập: dương giả với ba và bốn hàm băm

**Giải thích để giảng**

Cho:

$$\frac nm=8.$$

Dùng:

$$p(k)=(1-e^{-k/8})^k.$$

Với $k=3$:

$$p(3)=(1-e^{-3/8})^3 \approx\boxed{0{,}0306}.$$

Với $k=4$:

$$p(4)=(1-e^{-4/8})^4 \approx\boxed{0{,}0240}.$$

Tăng từ ba lên bốn hàm băm làm giảm xác suất dương giả từ khoảng 3,06% xuống 2,40%.

Tuy nhiên, không thể kết luận rằng tăng thêm hàm băm luôn tốt, vì khi vượt quá vùng tối ưu, mảng bit sẽ bão hòa.

**Nên bổ sung**

Yêu cầu sinh viên dự đoán kết quả trước khi tính và liên hệ với đồ thị ở slide 44.

**Prompt chỉnh sửa**

> Tạo hai cột phép tính cho $k=3$ và $k=4$, cùng cấu trúc thay số. Đưa kết quả về phần trăm và đánh dấu cấu hình tốt hơn. Thêm chú thích rằng đây là giá trị xấp xỉ từ mô hình Bloom filter.

## Slide 56. Bài tập: chia mảng bit

**Giải thích để giảng**

Bài toán so sánh hai cách dùng tổng cộng $n$ bit.

Phương án A: Một mảng chung $n$ bit, có $k$ hàm băm.

Phương án B: Chia thành $k$ mảng, mỗi mảng $n/k$ bit, mỗi hàm băm dùng một mảng riêng.

Trong phương án B, mỗi mảng nhận $m$ lần băm. Xác suất một bit không được đặt là:

$$\left(1-\frac{k}{n}\right)^m.$$

Xác suất một bit đã được đặt:

$$1-\left(1-\frac{k}{n}\right)^m.$$

Do các mảng được xây bằng các hàm băm độc lập, xác suất dương giả của phương án chia mảng:

$$\boxed{ p_{\text{split}}= \left[1-\left(1-\frac{k}{n}\right)^m\right]^k }.$$

Với mảng chung, phép xấp xỉ dựa trên mật độ bit là:

$$p_{\text{shared,approx}}= \left[1-\left(1-\frac1n\right)^{km}\right]^k.$$

Khi $n$ lớn, cả hai tiến gần tới:

$$(1-e^{-km/n})^k.$$

**Nên bổ sung**

Giải thích chi tiết vì sao công thức mảng chia có thể được viết chính xác dưới mô hình băm độc lập, trong khi công thức $q^k$ của mảng chung là xấp xỉ.

Với ví dụ $n=64,m=8,k=4$:

$$p_{\text{split}}\approx0{,}0265.$$

Mảng chung có xác suất dương giả chính xác theo mô hình ngẫu nhiên khoảng 0,0254; dạng $q^k$ cho khoảng 0,0246.

Các đại lượng này gần nhau, nhưng không được đồng nhất.

**Prompt chỉnh sửa**

> Dùng hai sơ đồ đặt cạnh nhau: một mảng 64 bit với bốn hàm băm và bốn mảng 16 bit với một hàm băm/mảng. Dẫn công thức của phương án chia mảng từ xác suất một bit bằng 0. Phân biệt xác suất chính xác theo mô hình chia mảng với xấp xỉ $q^k$ của mảng chung.

## Slide 57. Bài tập: số hàm băm tối ưu

**Giải thích để giảng**

Yêu cầu tìm giá trị $k$ tối thiểu hóa:

$$p(k)=(1-e^{-km/n})^k.$$

Hướng dẫn sinh viên đặt:

$$\rho=\frac mn$$

và lấy logarit:

$$\lambda(k)=\ln p(k) =k\ln(1-e^{-k\rho}).$$

Vì logarit là hàm tăng, giá trị làm nhỏ nhất $p(k)$ cũng làm nhỏ nhất $\lambda(k)$.

Lấy đạo hàm:

$$\lambda'(k) =\ln(1-e^{-k\rho}) +\frac{k\rho e^{-k\rho}}{1-e^{-k\rho}}.$$

Đến đây, sinh viên cần tìm nghiệm của $\lambda'(k)=0$ và chứng minh đó là cực tiểu.

**Nên bổ sung**

Nhắc lại rằng giải phương trình đạo hàm bằng 0 chỉ tìm được điểm dừng; chưa đủ để kết luận cực tiểu toàn cục.

**Prompt chỉnh sửa**

> Biên tập thành slide bài tập với gợi ý theo ba mức: lấy logarit, tính đạo hàm, kiểm tra dấu đạo hàm. Không hiển thị đáp án $k^*$ ngay. Để sinh viên thử trước khi chuyển sang slide lời giải.

## Slide 58. Bài tập: số hàm băm tối ưu — lời giải

**Giải thích để giảng**

Đây là chứng minh đầy đủ, nên trình bày chậm và cho sinh viên thấy rõ tại sao nghiệm tìm được là cực tiểu toàn cục.

Ta có:

$$\lambda(k)=k\ln(1-e^{-k\rho}).$$

Đặt:

$$z=k\rho,\qquad \theta=e^{-z}.$$

Suy ra:

$$z=-\ln\theta.$$

Đạo hàm:

$$\lambda'(k) =\ln(1-\theta)+\frac{z\theta}{1-\theta}.$$

Thay $z=-\ln\theta$:

$$\lambda'(k) = \frac{(1-\theta)\ln(1-\theta)-\theta\ln\theta}{1-\theta}.$$

Đặt:

$$\phi(\theta) =(1-\theta)\ln(1-\theta)-\theta\ln\theta.$$

Vì $1-\theta>0$, dấu của $\lambda'(k)$ chính là dấu của $\phi(\theta)$.

Ta có:

$$\phi\left(\frac12\right)=0.$$

Ngoài ra:

$$\phi(1-\theta)=-\phi(\theta).$$

Xét đạo hàm bậc hai:

$$\phi''(\theta) =\frac1{1-\theta}-\frac1\theta.$$

Trên $(0,1/2)$:

$$\phi''(\theta)<0.$$

Vì $\phi(0^+)=\phi(1/2)=0$, tính lõm chặt cho:

$$\phi(\theta)>0,\qquad 0<\theta<1/2.$$

Do tính phản đối xứng:

$$\phi(\theta)<0,\qquad 1/2<\theta<1.$$

Mặt khác:

$$\theta=e^{-k\rho}$$

giảm khi $k$ tăng.

Vì vậy:

- Với $k<(\ln2)/\rho$, ta có $\theta>1/2$, nên $\lambda'(k)<0$.
- Với $k>(\ln2)/\rho$, ta có $\theta<1/2$, nên $\lambda'(k)>0$.

Hàm giảm rồi tăng, do đó đạt cực tiểu toàn cục duy nhất tại:

$$\boxed{k^*=\frac{\ln2}{\rho}=\frac nm\ln2}.$$

Thay vào công thức xác suất:

$$e^{-k^*m/n}=\frac12,$$

nên:

$$\boxed{p(k^*)=2^{-k^*}}.$$

Vì số hàm băm là số nguyên, sau cùng phải so sánh hai giá trị nguyên gần $k^*$, bảo đảm $k\ge1$.

**Nên bổ sung**

Tôi đề xuất không đặt toàn bộ chứng minh này trong một màn hình trình chiếu. Có thể chia thành hai slide:

- Slide 58A: Tìm nghiệm đạo hàm bằng 0 và suy ra $k^*$.
- Slide 58B: Chứng minh dấu đạo hàm âm trước, dương sau $k^*$, kết luận cực tiểu toàn cục.

Cách tách này giúp sinh viên nhận ra sự khác nhau giữa tìm điểm dừng và chứng minh tối ưu.

**Prompt chỉnh sửa**

> Tách lời giải thành hai slide có cùng ký hiệu $\rho,z,\theta,\phi$. Slide đầu dẫn đạo hàm và nghiệm $k^*$; slide sau dùng dấu của $\phi$ để chứng minh cực tiểu toàn cục. Giữ đầy đủ giả thiết, không nhảy bước từ đạo hàm bằng 0 sang kết luận cực tiểu. Kết thúc bằng quy tắc chọn $k$ nguyên.

# Những điểm tôi đề xuất chỉnh sửa ưu tiên

Sau khi xem nội dung toàn bài, có sáu điểm đáng ưu tiên về mặt sư phạm và độ chính xác toán học.

| Slide | Vấn đề | Đề xuất |
| --- | --- | --- |
| 12–13 | Dễ nhầm $1/19$, $1/29$ và kỳ vọng của tỷ lệ | Thêm cây xác suất, giải thích rõ điều kiện và tỷ số các kỳ vọng |
| 15–17 | Dễ nhầm băm cố định với rút số ngẫu nhiên liên tục | Thêm sơ đồ so sánh hai cơ chế |
| 26–28 | Chứng minh reservoir còn trừu tượng | Thêm hình thay ô cụ thể và diễn giải xác suất có điều kiện |
| 40–41 | Dễ coi $q^k$ là xác suất chính xác | Phân biệt xác suất biên của một bit với xấp xỉ xác suất dương giả |
| 43, 57–58 | Chứng minh cực tiểu có nhiều bước | Tách tìm điểm dừng và chứng minh dấu đạo hàm |
| 44–45 | Có công thức nhưng chưa làm rõ tác động thực tế | So sánh các cấu hình theo bit/khóa, FPR và chi phí truy vấn |

Một bổ sung đặc biệt hữu ích là giải thích rằng reservoir sampling chuẩn thực ra có bảo đảm mạnh hơn xác suất biên $s/r$: với số ngẫu nhiên đều và độc lập, thuật toán tạo một tập con kích thước $s$ được chọn đều từ $r$ vị trí. Có thể dùng điều này để liên hệ với lấy mẫu ngẫu nhiên đơn không hoàn lại.

## Prompt chung để chỉnh sửa toàn bộ bộ slide

Sử dụng prompt sau làm chỉ dẫn chung, sau đó áp dụng prompt riêng của từng slide ở trên. Có thể dùng với công cụ chỉnh sửa slide hoặc tác nhân lập trình đang quản lý mã nguồn bài giảng.

> **Vai trò:** Chuyên gia thuật toán, xác suất và thiết kế bài giảng đại học.
>
> **Mục tiêu:** Chỉnh sửa Lecture 08 để sinh viên hiểu được lý do ra đời, cách hoạt động, chứng minh tính đúng, độ phức tạp và giới hạn của từng thuật toán.
>
> **Nguyên tắc biên tập:**
>
> 1. Mỗi slide tập trung vào một thông điệp chính.
> 2. Giải thích trực quan trước công thức toán học.
> 3. Ưu tiên ví dụ nhỏ có thể chạy tay.
> 4. Phân biệt rõ giả thiết, định lý, chứng minh và kết luận.
> 5. Giữ chính xác ký hiệu và điều kiện biên.
> 6. Không đồng nhất kỳ vọng với giá trị luôn xảy ra, hoặc xấp xỉ với đẳng thức chính xác.
> 7. Chứng minh dài có thể chia thành nhiều bước, nhưng không được bỏ bước suy luận.
> 8. Thiết kế trình chiếu 16:9, phông chữ đủ lớn, bố cục thoáng và nhất quán.
> 9. Không thêm hình minh họa trang trí không phục vụ việc giải thích thuật toán.
> 10. Bổ sung ghi chú giảng viên và câu hỏi tương tác khi có giá trị sư phạm.
>
> **Đầu ra:** Slide đã chỉnh sửa, ghi chú thuyết trình, và danh sách thay đổi về nội dung hoặc công thức.
>
> **Áp dụng:** Kết hợp các yêu cầu này với prompt riêng tương ứng từng slide.

## Gợi ý tổ chức thời lượng giảng dạy

Với 58 slide và yêu cầu giải thích chứng minh, tôi đề xuất chia thành hai buổi, thay vì cố gắng trình bày tất cả trong một tiết.

### Buổi 1 — Mô hình dòng và hai thuật toán lấy mẫu

Slide 1–30, 90 phút: 15 phút mở đầu và mô hình dòng; 35 phút lấy mẫu theo khóa; 30 phút reservoir sampling và chứng minh; 10 phút thực hành chạy tay.

### Buổi 2 — Bloom filter và bài tập

Slide 31–58, 90 phút: 20 phút cấu trúc và ví dụ Bloom filter; 25 phút xác suất dương giả; 20 phút tối ưu số hàm băm; 25 phút tổng kết và giải bài tập.

Ba hoạt động nên yêu cầu sinh viên tự làm tại lớp: chạy tay một vết reservoir sampling, tự tính dương giả của khóa 29 trong ví dụ Bloom 11 bit, và tự suy ra $k^*=(n/m)\ln2$ trước khi xem lời giải.

Như vậy, bài giảng không chỉ truyền đạt ba thuật toán, mà còn giúp sinh viên nắm được một phương pháp thiết kế thuật toán xử lý dòng: xác định truy vấn cần trả lời → chọn trạng thái cần lưu → xây dựng quy tắc cập nhật → chứng minh bảo đảm → phân tích chi phí và sai số.
