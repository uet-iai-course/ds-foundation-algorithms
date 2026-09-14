# Tiêu chuẩn biên soạn slide bài giảng

Tài liệu này quy định cách xây dựng và rà soát nội dung slide của học phần **Giải thuật nền tảng của Khoa học dữ liệu** cho sinh viên năm 2. Dùng khi lập storyboard, soạn từng phần và kiểm tra bản trình chiếu.

Đọc cùng [AGENTS.md](AGENTS.md). Phạm vi học thuật, tài liệu nguồn, thời lượng, cấu trúc tệp và quy trình phát hành tuân theo chỉ dẫn của bài đang làm và AGENTS.md. Tiêu chuẩn này cụ thể hóa yêu cầu về cách dạy và cách thể hiện; các ngoại lệ phải có lý do trong storyboard và nhật ký rà soát.

## 1. Đối tượng xem là sinh viên năm 2

### Kiến thức có thể giả định

Xác định tiên quyết từ đề cương trước khi soạn. Có thể dựa vào kiến thức lập trình, vòng lặp, hàm, mảng, toán rời rạc và các phép tính đại số tuyến tính, xác suất cơ bản đã được học. Với kiến thức cần dùng nhưng dễ quên, nhắc lại ngay trước bước sử dụng.

Không mặc định sinh viên đã biết hệ phân tán, đại số quan hệ, mô hình chi phí I/O hoặc thuật ngữ của một hệ xử lý dữ liệu. Mỗi khái niệm như vậy cần có đối tượng cụ thể, thao tác minh họa và tên gọi trước khi tham gia vào lập luận.

### Mức độ cần đạt

Sau một cụm nội dung trọng tâm, sinh viên cần thực hiện được các việc sau:

- Nêu đầu vào, đầu ra và điều kiện áp dụng.
- Theo dõi một ví dụ nhỏ, tính được trạng thái kế tiếp và kết quả cuối.
- Giải thích ý tưởng, đọc giả mã và viết lại các bước chính.
- Nêu lập luận đúng và chỉ ra giả thiết được sử dụng.
- Tính chi phí trong mô hình đã chọn, rồi giải thích giới hạn của kết luận.

Giữ độ chính xác của định nghĩa và thuật toán, nhưng chia bước suy luận theo lượng kiến thức mới cần tiếp nhận. Chứng minh dài có thể tách thành nhiều trang hoặc chuyển chi tiết sang ghi chú; trên slide vẫn phải có giả thiết, kết luận và bước suy luận quyết định. Nội dung đọc thêm phải được định vị rõ, không trở thành tiên quyết ngầm của phần bắt buộc.

### Ngôn ngữ và ký hiệu

- Viết tiếng Việt ngắn, trực tiếp; dùng nhất quán một thuật ngữ cho một khái niệm.
- Giải thích viết tắt khi xuất hiện lần đầu. Chỉ giữ tiếng Anh khi cần cho tên riêng, tên thuật toán hoặc thuật ngữ chưa có cách dịch ổn định.
- Định nghĩa ký hiệu ngay nơi dùng: ý nghĩa, miền giá trị, kích thước và đơn vị khi có.
- Dùng cùng tên biến, chỉ số và dữ kiện qua hình, ví dụ, giả mã và phân tích chi phí. Nếu đổi ký hiệu, nói rõ sự tương ứng.
- Câu hỏi tương tác phải có nhiệm vụ cụ thể, dùng nhãn **“Câu hỏi:”**; đáp án hoặc hướng giải đặt trong ghi chú diễn giả.

## 2. Mỗi slide có mục đích rõ ràng trong mạch xây dựng kiến thức

### Mục đích phải quan sát được

Mỗi slide có **một mục đích học tập chính**, diễn đạt bằng việc sinh viên làm được sau khi xem. “Giới thiệu MapReduce” còn quá rộng. “Xác định khóa để các đóng góp cho cùng một kết quả được nhóm lại” cho biết slide cần xây điều gì và kiểm tra ra sao.

Mục đích được ghi trong storyboard. Trên mặt slide, tiêu đề gọi đúng khái niệm, thao tác hoặc kết quả trung tâm; không hiển thị nhãn quy trình hay câu mô tả mục đích nội bộ.

Một slide cần trả lời được ba câu trong quá trình soạn:

1. Sinh viên dùng kiến thức hoặc kết quả nào từ phần trước để đọc trang này?
2. Trang này bổ sung được điều gì?
3. Kết quả ấy được dùng ở bước nào tiếp theo hoặc để hoàn thành mục tiêu nào?

Nếu một trang chỉ đổi cách diễn đạt mà không tạo bước tiến, gộp hoặc bỏ. Nếu trang có hai mục đích đòi hai lập luận riêng, tách trang.

### Mạch của phần lớn và cụm khái niệm

Phần mở đầu gồm tiêu đề bài giảng, nội dung bài và mục tiêu học tập. Các phần lớn sau đó đi theo mạch của nguồn đã chọn và yêu cầu cụ thể của giảng viên. Mỗi phần có điểm vào, sản phẩm học tập và câu nối sang phần sau. Phần kết luận thu hồi bài toán mở đầu và cho sinh viên sử dụng kết quả đã xây dựng.

Với khái niệm hoặc thuật toán trọng tâm, dùng mạch:

**Tình huống dữ liệu → vấn đề → trực giác → ví dụ chạy tay → hình thức hóa → thuật toán và lập luận đúng → ứng dụng, chi phí → kiểm tra.**

Tình huống phải nêu dữ liệu, đầu ra cần tạo và giới hạn tính toán có liên quan. Dùng lại tình huống trong ví dụ, lựa chọn thuật toán hoặc đánh giá chi phí; chỉ dùng con số quy mô có nguồn.

Tám bước trên không đồng nghĩa tám slide. Có thể gộp những bước phục vụ cùng một luận điểm nếu vẫn đọc được. Với khái niệm phụ, ghi rõ chu trình rút gọn và lý do. Với một hệ thống hoặc cơ chế lưu trữ, có thể giải thích bằng vai trò, trạng thái và điều kiện hoạt động; không tạo giả mã hoặc định lý khi không áp dụng.

### Thông tin tối thiểu trong storyboard

| Trường | Nội dung cần ghi |
|---|---|
| Mã và tiêu đề | Mã duy nhất; tiêu đề dự kiến trên mặt slide |
| Mục đích | Một việc sinh viên làm được sau trang này |
| Vai trò trong mạch | Nêu vấn đề, xây trực giác, chạy ví dụ, hình thức hóa, giải thích cơ chế, chứng minh, đánh giá hoặc kiểm tra |
| Kiến thức đầu vào | Khái niệm, ký hiệu hoặc kết quả đã được thiết lập |
| Nội dung và cách thể hiện | Hình, bảng, giả mã, công thức hoặc thao tác cụ thể cần thấy |
| Kết nối vào–ra | Trang trước cung cấp gì; trang này tạo gì cho phần sau |
| Kiểm tra và ghi chú | Nhiệm vụ khi cần; đáp án, giải thích, lỗi dễ mắc và câu chuyển |
| Nguồn | Tệp, mục, trang; phân biệt trích nguồn với áp dụng hoặc điều chỉnh |
| Thời lượng | Thời gian dự kiến trong kế hoạch, tính cả tương tác |

**Điều kiện đạt:** người rà chỉ ra được đóng góp của từng trang và không phải tự bổ sung một khái niệm bị thiếu để nối hai trang liên tiếp.

## 3. Slide về thuật toán

### Nội dung bắt buộc của cả cụm thuật toán

Một thuật toán trọng tâm phải có bài toán, trực giác, ví dụ, đặc tả, giả mã, lập luận đúng, điều kiện dừng, trường hợp biên và phân tích chi phí. Các thành phần này được phân bổ qua một cụm slide; không ép toàn bộ lên một trang.

| Thành phần | Yêu cầu thể hiện |
|---|---|
| Bài toán | Nêu dữ liệu vào, kết quả cần tạo và giới hạn khiến cần thuật toán |
| Trực giác | Giải thích thao tác quyết định: nhóm, chia, chọn, cập nhật, loại bỏ hoặc dùng lại dữ liệu |
| Ví dụ dẫn nhập | Theo dõi một trường hợp nhỏ trước khi khái quát giả mã |
| Đặc tả | Nêu kiểu, kích thước, chỉ số, điều kiện trước và điều kiện sau |
| Giả mã | Thấy được khởi tạo, bước xử lý, điều kiện lặp/dừng và kết quả trả về |
| Tính đúng | Nêu mệnh đề, giả thiết và lập luận bảo đảm kết quả |
| Trường hợp biên | Xử lý các trường hợp ảnh hưởng tính đúng hoặc làm thuật toán không áp dụng được |
| Chi phí | Gắn số thao tác và lượng dữ liệu với đúng bước trong giả mã |

Các giả thiết quyết định kết luận phải hiện trên mặt slide liên quan. Ghi chú diễn giả mở rộng giải thích và chứng minh; không phải nơi duy nhất chứa điều kiện để thuật toán đúng.

### Cách trình bày giả mã

- Ưu tiên giả mã độc lập với ngôn ngữ khi cú pháp cài đặt không phải mục tiêu học tập.
- Dùng tên biến có nghĩa và thụt lề rõ. Giải thích các phép toán phụ chưa được định nghĩa.
- Đặt ví dụ hoặc trạng thái liên quan cạnh đoạn mã đang xét. Khi tô sáng một dòng, chỉ rõ nó đọc gì, thay đổi gì hoặc phát kết quả nào.
- Tách đoạn mã dài theo các bước có chức năng rõ. Giữ đủ ngữ cảnh và trạng thái truyền giữa các trang.
- Với thuật toán phân tán, phân biệt hàm người dùng viết, việc hệ thống thực hiện, tác vụ và máy. Chỉ rõ nơi lưu hoặc nơi nhận dữ liệu khi điều đó ảnh hưởng kết quả hay chi phí.

### Cách trình bày tính đúng

Mở đầu bằng mệnh đề cần chứng minh. Sau đó nêu ý tưởng và các bước then chốt. Với bất biến vòng lặp, phải có khởi tạo, duy trì và kết luận khi dừng. Với đệ quy, phải có cơ sở và bước giảm về bài toán nhỏ hơn. Ví dụ chạy đúng chỉ minh họa cơ chế; bảo đảm cho mọi đầu vào cần lập luận riêng.

Chọn chi tiết theo loại thuật toán:

| Loại | Chi tiết cần làm rõ |
|---|---|
| Chia để trị | Cách chia, cơ sở, cách ghép, tiến triển và truy hồi chi phí |
| Tham lam | Lựa chọn cục bộ, tính khả thi và căn cứ cho kết luận tối ưu nếu có |
| Quy hoạch động | Ý nghĩa trạng thái, cơ sở, chuyển trạng thái, thứ tự tính và khôi phục nghiệm khi cần |
| Ngẫu nhiên | Nguồn ngẫu nhiên, đại lượng kỳ vọng/xác suất và giả thiết độc lập khi sử dụng |

**Điều kiện đạt:** sinh viên xác định được dữ liệu mỗi bước cần, chạy được bước tiếp theo và giải thích vì sao kết quả thỏa đặc tả. Không chỉ nhớ tên thuật toán hoặc đọc lại giả mã.

## 4. Slide về ví dụ

### Chọn ví dụ để làm rõ cơ chế

Ví dụ cần đủ nhỏ để chạy tay và đủ cấu trúc để bộc lộ ý tưởng trọng tâm. Chọn dữ kiện từ nguồn của bài. Nếu áp dụng thuật toán nguồn lên một phần dữ liệu hoặc cụ thể hóa ví dụ ký hiệu, ghi rõ cách làm và căn cứ; không gọi dữ kiện do người soạn chọn là dữ kiện trích nguyên văn.

Ưu tiên dùng cùng một ví dụ qua nhiều bước: trực giác, giả mã, tính đúng và chi phí. Chỉ đổi ví dụ khi cần thể hiện một cơ chế hoặc trường hợp khác; nói rõ điểm thay đổi. Bài tập recitation phải tuân quy định giữ dữ kiện và yêu cầu toán học của nguồn trong AGENTS.md.

### Cấu trúc của một vết chạy

| Bước | Sinh viên cần nhìn thấy |
|---|---|
| Dữ kiện | Toàn bộ phần đầu vào đang xét, quy ước và kết quả cần tìm |
| Trạng thái ban đầu | Giá trị khởi tạo, cấu trúc dữ liệu hoặc cách phân chia |
| Thao tác | Dòng giả mã hoặc phép biến đổi được áp dụng |
| Trạng thái sau | Giá trị thay đổi, phần giữ nguyên và đầu ra trung gian |
| Kết quả | Đối chiếu với yêu cầu và điều kiện của bài toán |

Thể hiện ít nhất một bước trung gian đủ chi tiết để người học tính lại. Với thao tác lặp, làm đầy đủ bước đầu, cho sinh viên dự đoán một bước tương tự, rồi mới rút gọn phần còn lại. Ghi rõ các bước đã lược.

### Bố cục nên dùng

- **Trước–sau:** hai trạng thái cùng tỷ lệ, cùng vị trí đối tượng; đánh dấu phần thay đổi.
- **Bảng vết chạy:** mỗi hàng là một bước; các cột ghi biến hoặc trạng thái cần theo dõi.
- **Giả mã–trạng thái:** một bên là đoạn mã ngắn, một bên là dữ liệu của bước đang xét.
- **Nhiều trang liên tiếp:** giữ nguyên khung, dữ kiện và nhãn; mỗi trang thực hiện thêm một phép biến đổi.

Các phép cộng, tích, chỉ số hoặc nhóm trung gian cần được viết ra khi chúng chính là điều đang dạy. Với dữ liệu chỉ là phần trích của nguồn, kết luận phải giới hạn trên phần trích ấy. Ví dụ số dùng để minh họa thuật toán không được trình bày như kết quả thực nghiệm.

**Điều kiện đạt:** người học có thể tự tái tạo vết chạy từ dữ kiện hiển thị, biết mỗi giá trị trung gian đến từ đâu và nhận ra bước nào thể hiện ý tưởng của thuật toán. Người soạn phải tự tính lại vết chạy trước khi duyệt.

## 5. Slide về đánh giá chi phí

### Nêu mô hình trước khi tính

Mỗi phân tích phải xác định rõ các thành phần sau trước công thức kết luận:

| Thành phần | Cần chốt |
|---|---|
| Đại lượng đánh giá | Thời gian, số phép toán, bộ nhớ, số khối I/O, byte truyền hoặc số lượt quét |
| Tham số kích thước | Số phần tử, số phần tử khác không, số đỉnh/cạnh, kích thước bản ghi, số tác vụ… theo thuật toán |
| Đơn vị | Phép toán, phần tử, bản ghi chuẩn hóa, byte hoặc khối; chuyển đổi đơn vị khi cần |
| Quy tắc đếm | Một thao tác nào được tính một lần; đọc lặp, sao chép và trung gian được tính ra sao |
| Phạm vi | Một bước, một tác vụ, một công việc hay toàn bộ thuật toán |
| Trường hợp | Xấu nhất, trung bình, kỳ vọng hoặc khấu hao; nêu giả thiết tương ứng |

Với bộ nhớ, phân biệt đầu vào đang giữ, bộ nhớ phụ và đầu ra. Với dữ liệu phân tán, phân biệt tổng chi phí với tải của tác vụ nặng nhất. Với phép toán trên số có độ dài thay đổi, nói rõ đang đếm phép toán đơn vị hay tính cả chi phí theo độ dài biểu diễn.

### Mạch trình bày phép tính

**Đơn vị và giả thiết → đánh dấu nơi phát sinh chi phí → đếm từng bước → lập bảng → cộng tổng → thay số → diễn giải kết luận.**

Dùng lại thuật toán và ví dụ vừa học. Mỗi số hạng phải truy được về một dòng giả mã, một lần đọc, một bản sao hoặc một bước xử lý trong hình. Trình bày biểu thức đếm trước, rồi mới rút gọn bằng ký hiệu tiệm cận khi phù hợp.

Mẫu bảng:

| Bước | Số lần thực hiện | Chi phí mỗi lần | Đóng góp |
|---|---:|---:|---:|
| Đọc dữ liệu | $a$ | $c_1$ | $ac_1$ |
| Xử lý hoặc gửi trung gian | $b$ | $c_2$ | $bc_2$ |
| Tổng trong phạm vi đã chọn | | | $ac_1+bc_2$ |

Đây là mẫu trình bày, không phải mô hình mặc định cho mọi thuật toán. Tên bước và phạm vi tổng phải thay bằng đúng thuật toán đang dạy.

### Đơn vị và giả thiết phải nhất quán

Nếu $I$ là số byte đầu vào và có $m$ cặp trung gian, mỗi cặp dài $B$ byte, phần trung gian là $mB$ byte. Chỉ được viết $I+mB$ nếu mô hình đã quy định cộng hai phần đó. Không cộng trực tiếp số byte với số cặp. Nếu các cặp có độ dài khác nhau, dùng tổng độ dài thực hoặc nêu giả thiết chuẩn hóa.

Khi dùng mô hình chi phí đầu vào tác vụ của MMDS ở Bài 02, ghi rõ chi phí tác vụ là kích thước đầu vào và tổng là tổng trên các tác vụ. Không tự cộng thêm đầu ra cuối hoặc đếm trung gian theo một quy ước khác mà giữ nguyên tên mô hình. Các bài khác phải xác lập mô hình phù hợp với nguồn của mình.

### So sánh phương án

- So sánh trên cùng bài toán, dữ liệu và mô hình; ghi rõ điều kiện thay đổi giữa hai phương án.
- Nêu giả thiết về kích thước trung gian, phân bố khóa hoặc tính thưa trước khi thay số.
- Khi giải bất đẳng thức, kiểm tra riêng điểm bằng nhau, điều kiện nguyên và miền tham số.
- Tách kết luận về lượng dữ liệu, số phép toán và thời gian thực. Tổng chi phí thấp hơn chưa đủ chứng minh chạy nhanh hơn.
- Kiểm tra tính khả thi theo bộ nhớ, lệch tải và kích thước đầu ra khi chúng ảnh hưởng lựa chọn.

**Điều kiện đạt:** sinh viên giải thích được từng số hạng, tự thay một bộ tham số hợp lệ và nêu được điều kiện mà kết luận so sánh còn đúng. Công thức cuối không được xuất hiện như một kết quả cần học thuộc.

## 6. Cách thể hiện trực quan các khái niệm

### Chọn hình theo quan hệ cần giải thích

Trước khi vẽ, xác định đối tượng và quan hệ người học cần nhìn thấy. Hình phải hỗ trợ một phép đọc cụ thể: theo dữ liệu, tìm phần tử cùng nhóm, xác định phụ thuộc, theo một phép cập nhật hoặc so sánh các đại lượng.

| Khái niệm hoặc thao tác | Cách thể hiện | Nhãn cần có |
|---|---|---|
| Luồng dữ liệu | Các trạng thái nối bằng mũi tên | Dữ liệu đi qua, phép biến đổi, nơi nhận |
| Nhóm theo khóa | Bảng hoặc các vùng chứa nhóm | Khóa, phần tử trong nhóm, quy tắc gán |
| Ma trận–vector | Hàng, cột, ô hoặc dải tương ứng | Chỉ số, kích thước, phần tử đang nhân/cộng |
| Cấu trúc cây hoặc đồ thị | Đỉnh, cạnh, vùng được duyệt | Ý nghĩa cạnh, hướng và trọng số khi có |
| Bộ nhớ và sao chép | Các vùng lưu trữ với cùng nhãn dữ liệu | Bản gốc/bản sao, vị trí, số lần nhận |
| Bất biến | Trạng thái trước–sau có phần được giữ nguyên | Thuộc tính bảo toàn và phần thay đổi |
| Quan hệ hình học | Hình, miền hoặc tọa độ phù hợp | Trục, miền xét, điều kiện và đối tượng được so sánh |
| Chi phí theo tham số | Bảng hoặc đồ thị từ dữ liệu/công thức đã nêu | Trục, đơn vị, miền tham số và nguồn |

Không dùng cùng một kiểu hộp–mũi tên cho mọi khái niệm. Một bảng thường phù hợp hơn sơ đồ khi người học cần so sánh các giá trị chính xác; giả mã phù hợp hơn hình khi cần đọc điều kiện điều khiển.

### Quy tắc vẽ và chuyển trạng thái

- Giữ vị trí và tên của cùng một đối tượng qua các trạng thái liên tiếp.
- Dùng màu nhất quán theo vai trò, kèm chữ, hình dạng hoặc kiểu nét; không truyền ý nghĩa chỉ bằng màu.
- Mũi tên phải có nghĩa xác định: dữ liệu di chuyển, quan hệ phụ thuộc hoặc phép biến đổi. Dùng nhãn khi có thể nhầm các nghĩa này.
- Khi một phần tử được sao chép, hình phải cho thấy các bản sao tương ứng. Khi nhiều phần tử được gộp, phải thấy đóng góp và kết quả gộp.
- Giữ tỷ lệ có ý nghĩa, chỉ số và giá trị nguồn. Ghi rõ hình khái niệm khi kích thước hình không biểu diễn độ lớn dữ liệu.
- Chú thích hình nêu quan hệ hoặc kết quả cần đọc, thay vì chỉ lặp tên hình.

Chỉ dùng hiệu ứng xuất hiện từng bước khi nó giúp theo dõi đúng thứ tự suy luận. Dữ kiện cần so sánh phải còn nhìn thấy. Nếu hai trạng thái cần xem đồng thời hoặc bản in phải giữ được vết chạy, dùng bố cục trước–sau hoặc các trang riêng.

### Khả năng đọc và nền kỹ thuật

- Mỗi trang có một hình, bảng, công thức hoặc đoạn giả mã làm trọng tâm. Các thành phần phụ giải thích trực tiếp trọng tâm ấy.
- Giữ chữ thân bài từ `0.75em` trở lên theo mẫu học phần. Không thu nhỏ chữ để chứa thêm nội dung; tách trang hoặc chuyển diễn giải phụ sang ghi chú. Chú thích nhỏ tuân ngoại lệ và kiểm tra khả năng đọc trong AGENTS.md.
- Giữ gạch đầu dòng ngắn, mỗi ý không quá hai dòng ở khung 16:9. Nhãn hình phải đọc được ở kích thước trình chiếu thực tế.
- Dùng SVG cho hình kỹ thuật; có mô tả thay thế cụ thể. Dựng công thức bằng KaTeX, bảng bằng HTML và giả mã bằng khối mã.
- Kế thừa [mẫu slide](2627-1/lecture-template.html) và [CSS học phần](2627-1/lecture-style.css), giữ khung 1280 × 720 và thư viện cục bộ.
- Kiểm tra ảnh, công thức, tương phản, cắt chữ, chồng lấn và điều hướng bàn phím trên bản render thực. Kiểm tra cả màn hình rộng, màn hình hẹp và bản in khi có phát hành dạng in.

**Điều kiện đạt:** người học đọc được đối tượng, quan hệ và phép biến đổi từ hình; hình khớp với dữ liệu, công thức và giả mã của cùng cụm. Người rà phải xem hình đã render, không suy luận chất lượng hiển thị chỉ từ văn bản hoặc mã nguồn.

## Phiếu kiểm tra trước khi duyệt

- [ ] Mỗi slide có một mục đích học tập và vai trò trong mạch được ghi ở storyboard.
- [ ] Mọi tiên quyết và ký hiệu đã được thiết lập trước nơi dùng.
- [ ] Các cụm thuật toán có đủ đặc tả, ví dụ, giả mã, lập luận đúng, dừng, biên và chi phí.
- [ ] Ví dụ có dữ kiện và trạng thái trung gian tính lại được; phân biệt rõ nguồn và phần áp dụng.
- [ ] Mô hình chi phí, đơn vị, phạm vi và giả thiết xuất hiện trước phép tính.
- [ ] Mỗi số hạng chi phí truy được về một bước; các kết luận so sánh giữ đủ điều kiện.
- [ ] Hình, giả mã, bảng và lời giải dùng cùng dữ kiện, chỉ số và thuật ngữ.
- [ ] Các câu hỏi đo đúng mục tiêu, có đáp án hoặc hướng dẫn trong ghi chú.
- [ ] Bản render đọc được, không tràn hoặc chồng lấn; hình và liên kết hoạt động.
- [ ] Sai khác với nguồn và ngoại lệ có lý do, vị trí và quyết định xử lý trong nhật ký.

Ghi kết quả rà bằng **vị trí → vấn đề → bằng chứng → cách sửa**. Với lỗi mạch viết, nêu rõ kiến thức đầu vào bị thiếu hoặc kết quả chưa được nối sang bước tiếp theo. Với lỗi nội dung hoặc hình thức, chỉ ra dữ kiện, phép tính, nhãn hoặc thành phần hiển thị cụ thể cần sửa.
