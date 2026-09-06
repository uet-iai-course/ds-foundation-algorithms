# Storyboard Bài 1

## Bản triển khai theo kế hoạch ngày 2026-09-06

Tuyến mới: ứng dụng cụ thể → giới hạn cần xử lý → đặc tả và thuộc tính giải thuật → nội dung học phần → sự chuẩn bị của sinh viên → giới hạn suy luận và bài tập. HTML và ghi chú đã theo tuyến này và đạt kiểm định; nhật ký ghi bằng chứng cùng giới hạn công cụ.

Bản ER-001: 45 trang giảng, 120 phút; sáu trang bài tập kể cả trang chuyển phần, 60 phút. Bảy phần ngoài A, B, C, D, E, F, R. P00/P01 mở bài, không đặt ví dụ chưa có ngữ cảnh. Bỏ A08/A09; A01–A07 tự nêu nhiệm vụ, đầu vào–đầu ra và trở ngại bằng hình. E04 vẫn cuối phần giảng. Bản này thay phần A của bản 53 trang; B–R không đổi ở ER-001; ER-002 dưới đây thay phần B.

## Vai trò và kết nối giữa các mạch

| Mạch | Kiến thức đầu vào | Vai trò và sản phẩm | Kết nối vào → ra |
|---|---|---|---|
| A | Tệp, bản ghi, liên kết web; véc-tơ được giải thích là dãy số | P00/P01 định vị buổi học; bảy nhiệm vụ phân biệt đầu vào, đầu ra và khó khăn | Mục tiêu học → thống kê kho web → sắp kết quả và tìm tương đồng → dòng yêu cầu |
| B | Tệp, bản ghi, truy vấn cơ bản | Nhận diện trạng thái dòng, khôi phục và truy cập chọn lọc | Từ tìm kiếm kho tĩnh → danh mục giới hạn cần phân tích trong C |
| C | Vòng lặp, bảng ánh xạ, độ phức tạp | Hoàn tất một chu trình giải thuật; lập khung chi phí và bảo đảm | Từ giới hạn của A/B → ngôn ngữ để đọc bản đồ học phần |
| D | Khung đánh giá của C | Xác định năm mạch, tên phương pháp và lý do học | Từ nhu cầu → nội dung sẽ học → kiến thức phải chuẩn bị |
| E | Bản đồ chương trình, nền tảng cá nhân | Tự nhận diện phần cần ôn; nêu sản phẩm và trách nhiệm học tập | Từ danh mục thuật toán → cách học và kiểm chứng kết luận |
| F | Tổ hợp, xác suất độc lập, tuyến tính kỳ vọng | Phân biệt đúng theo mô hình với suy luận có căn cứ; áp lại khung chọn giải thuật | Từ trách nhiệm dữ liệu → bài tập kiểm tra mô hình |
| R | F02–F03, gợi ý công thức và dữ kiện nguồn | Giải các biến thể và giải thích giới hạn của phép tìm mẫu trùng | Dùng mô hình đã có → sản phẩm có thể chấm |

Câu nối giữa các mạch được thể hiện cả trên trang mở phần và trong lời giảng:

- A→B: “Kho web còn sinh dòng truy vấn, cần lưu trữ và phục vụ nhiều loại tra cứu. Mỗi công việc đặt thêm một giới hạn.”
- B→C: “Các ví dụ vừa gặp yêu cầu khác nhau về bộ nhớ, thời gian truy cập và kết quả. Ta dùng tổng byte theo máy chủ để phân tích một lời giải đầy đủ.”
- C→D: “Khung đặc tả và chi phí giúp xác định vai trò của từng phương pháp trong học phần.”
- D→E: “Mỗi mạch dùng một phần kiến thức nền khác nhau. Sinh viên cần biết phần nào đã có và phần nào phải ôn trước khi học.”
- E→F: “Một chương trình chạy đúng vẫn có thể dẫn đến kết luận sai nếu giả thiết về dữ liệu không phù hợp.”
- F→R: “Các bài tập tiếp theo thay đổi quy mô và tiêu chuẩn trùng để kiểm tra chính mô hình vừa dùng.”

## Bản đồ từng trang

Mã V trỏ tới danh mục hình bên dưới, đồng thời cung cấp nguồn và dữ kiện. Thời lượng gồm câu kiểm tra, chuyển ý và thời gian quan sát hình; không hiển thị trên trang chiếu. Tên thuật toán chuyên biệt chỉ được giới thiệu có hệ thống từ mạch D.

| Mã trang | Tiêu đề trang chiếu | Luận điểm, hoạt động và sản phẩm | Nguồn/hình | Phút | Nối sang trang sau |
|---|---|---|---|---:|---|
| L01-P00 | Bài toán dữ liệu lớn và mô hình thuật toán | Nhận diện bài, học phần và học kỳ | source.md | 1 | Nội dung buổi học |
| L01-P01 | Nội dung buổi học | Ứng dụng → phân tích thuật toán → nội dung và cách học; mục tiêu khái quát trước ví dụ | source.md | 2 | Nhiệm vụ thống kê kho web |
| L01-A01 | Tính tổng kích thước trang web theo máy chủ | Bốn bản ghi → tổng 55/25/0; hình tệp vượt bộ nhớ; phân biệt kích thước trang và lưu lượng | V01; bảng HTML dùng lại C02 | 3 | Kho có thể chia trên nhiều máy |
| L01-A02 | Đếm số lần xuất hiện của từng từ | Cùng từ ở nhiều phần kho → tổng toàn kho; gom dữ liệu qua mạng gây nút thắt, lỗi máy cần tránh đếm trùng | V02 | 3 | Kho tìm kiếm còn cần sắp kết quả |
| L01-A03 | Tính điểm quan trọng của trang web | Trang và liên kết → điểm hỗ trợ sắp kết quả; phụ thuộc điểm buộc đọc/cập nhật nhiều vòng | V03 | 3 | Điểm chung chưa phân biệt chủ đề |
| L01-A04 | Ưu tiên kết quả tìm kiếm theo chủ đề | Jaguar + chủ đề ô tô → ưu tiên trang về xe; điểm riêng cho mỗi người tốn lưu trữ | V04 | 3 | Điểm liên kết có thể bị thao túng |
| L01-A05 | Hạn chế liên kết rác trong xếp hạng | Cụm cùng bên kiểm soát đẩy điểm t; cần hạn chế ảnh hưởng lên kết quả | V05 | 3 | Kết quả tìm kiếm còn có bản sao |
| L01-A06 | Tìm các cặp tài liệu gần trùng | Nội dung chung và phần sửa; một triệu tài liệu sinh $499\,999\,500\,000$ cặp cần xét nếu so tất cả | V06 | 4 | Đổi từ mọi cặp sang một truy vấn |
| L01-A07 | Tìm đoạn tài liệu bằng véc-tơ truy vấn | Truy vấn và đoạn tài liệu mã hóa cùng cách → k đoạn gần theo khoảng cách; mỗi truy vấn quét lại kho lớn | V07 | 3 | Truy vấn đến nối tiếp tạo dòng |
| L01-B00 | Xử lý dòng dữ liệu, lưu trữ và truy vấn | Giới thiệu ba nhóm: dòng, nén, xử lý và truy vấn trên đĩa; mỗi nhóm gắn đầu ra và giới hạn | V07–V09; MMDS4.1 | 1 | Dòng truy vấn và dòng thư có nhiệm vụ khác nhau |
| L01-B01 | Giữ mẫu truy vấn và lọc thư đến | Lưu hết lịch sử tốn bộ nhớ. Tra danh sách lớn trên đĩa cho từng thư làm tăng thời gian xử lý. | V08 | 3 | Đếm người dùng và lượt truy cập |
| L01-B02 | Đếm người dùng và lượt truy cập gần đây | Đếm người dùng cần nhận ra lần quay lại. Thống kê gần đây phải bỏ ảnh hưởng của bản ghi hết hạn mà vẫn cập nhật kịp. | V09 | 3 | Dữ liệu cần giữ lại còn chiếm dung lượng |
| L01-B10 | Nén dữ liệu để lưu và khôi phục | Một số đếm không khôi phục dữ liệu; nén văn bản và ảnh có yêu cầu khác nhau | V09–V11; MMDS4; Nelson–Gailly3,11 | 1 | Nén văn bản khôi phục nguyên vẹn |
| L01-B03 | Lưu văn bản với ít dung lượng hơn | Lược bỏ tùy ý làm mất văn bản gốc. Mã và thông tin phụ trợ phải đủ để giải mã, nhưng cũng chiếm dung lượng. | V10 | 3 | Dữ liệu ảnh có thể có đặc tả khác |
| L01-B04 | Giảm dung lượng ảnh với sai số cho phép | Gộp các giá trị điểm ảnh làm mất chi tiết. Cần kiểm cả dung lượng mã và sai khác của ảnh khôi phục. | V11 | 2 | Dữ liệu đã lưu vẫn cần tổ chức để xử lý |
| L01-B11 | Xử lý và truy vấn dữ liệu trên đĩa | Định nghĩa khối đọc ghi và phần tệp vừa bộ nhớ; phân biệt sắp, tra, nối | V11–V16; DSC15 | 1 | Tệp đầu vào và đầu ra của phép sắp |
| L01-B05 | Sắp xếp tệp lớn theo khóa | Không thể nạp trọn tệp để sắp như một mảng trong bộ nhớ. Đọc và ghi lại nhiều lần làm tăng chi phí dù số so sánh ít. | V12 | 3 | Tệp có thứ tự hỗ trợ truy cập chọn lọc |
| L01-B06 | Tìm hồ sơ giảng viên theo mã hoặc lương | Quét cả bảng cho mỗi yêu cầu đọc nhiều dữ liệu thừa. Nếu dùng chỉ mục, phải cập nhật nó khi mã hoặc lương thay đổi. | V13 | 2 | Từ khóa cần một cách ánh xạ khác |
| L01-B07 | Tìm tài liệu chứa đồng thời hai từ khóa | Đọc từng tài liệu cho mỗi truy vấn lặp lại công việc trên cả kho. Cần tìm được nơi xuất hiện của từng từ mà không quét lại hết. | V14 | 2 | Vùng không gian không phải danh sách từ |
| L01-B08 | Tìm đối tượng giao vùng trên bản đồ | Kiểm mọi hình trên bản đồ tốn công. Lọc theo hộp bao giảm ứng viên, nhưng hộp bao giao vùng chưa đủ kết luận về hình thật. | V15 | 2 | Truy vấn cũng có thể kết hợp hai bảng |
| L01-B09 | Ghép sinh viên với các môn đã đăng ký | Hai bảng chiếm 100 và 400 khối; bộ nhớ chỉ có 20 khối. Quét bảng đăng ký lại cho từng sinh viên sẽ đọc cùng dữ liệu nhiều lần. | V16 | 3 | Gom các giới hạn thành khung phân tích |
| L01-C01 | Các giới hạn cần phân tích | Dùng lại V01, V02, V06, V16 để tách chi phí tính, trạng thái, khối và mạng | Các nguồn V01/V02/V06/V16 | 4 | Phân tích trọn một ví dụ nhỏ |
| L01-C02 | Một tổng đang chạy cho mỗi máy chủ | Trực giác giữ bảng theo khóa; vết bốn bản ghi với các trạng thái 40; 40/25; 55/25; 55/25/0 | V01; bảng vết bằng HTML | 4 | Từ trạng thái tới đặc tả |
| L01-C03 | Đặc tả xác định kết quả phải trả | Miền, đầu vào/ra, điều kiện trước/sau; phân biệt bài toán với cách biểu diễn | Stanford 62; đặc tả trong outline | 2 | Viết thao tác đáp ứng đặc tả |
| L01-C04 | Quét và cập nhật bảng tổng | Giả mã: bảng rỗng, duyệt, khởi tạo khóa mới, cộng; dừng sau $n$ bản ghi | V01; giả mã văn bản | 2 | Cần giải thích đúng với mọi tiền tố |
| L01-C05 | Bất biến tiền tố | Tập khóa và tổng đều đúng; khởi tạo, duy trì, kết thúc; xử lý dãy rỗng và kích thước 0 | V01, C03–C04 | 3 | Tính đúng đi cùng điều kiện khả thi |
| L01-C06 | Một lượt quét và bộ nhớ theo số khóa | $O(h)$ trạng thái; $O(n)$ kỳ vọng với bảng băm; $T_{\rm quét}\ge D/v$; hỏi trường hợp bảng tổng không vừa bộ nhớ | MMDS tr.13; BHK PDF 10; V01 | 3 | Các tác vụ truy vấn còn có chi phí khác |
| L01-C07 | Độ trễ, xây dựng và cập nhật | Dùng lại V07/V08/V13: chi phí xử lý toàn bộ, một truy vấn, một cập nhật và xây chỉ mục khác nhau | Các bài 07, 08, 13 | 3 | Nêu cả đầu ra được bảo đảm |
| L01-C08 | Điều kiện đúng và chất lượng kết quả | So sánh khôi phục đúng V10; ứng viên V06; độ thu hồi V07; lọc V08; hỏi bảo đảm phải giữ trong từng trường hợp | Các nguồn V06–V11/V15 | 4 | Từ yêu cầu tới nội dung học phần |
| L01-D00 | Từ yêu cầu đến nhóm phương pháp | Các giới hạn đã nhận diện → nhóm công cụ sẽ học; không liệt kê lại 14 bài | source.md; C01/C07/C08 | 1 | Mục tiêu học phần rồi bản đồ năm nhóm |
| L01-D01 | Học phần và năng lực cần đạt | Năng lực toàn học phần: giải thích/lựa chọn, thiết kế/triển khai, tự học/trách nhiệm; mục tiêu riêng Bài 01 đã đặt ở P01 | source.md phần I–II; mục tiêu trong outline | 2 | Xem cách tổ chức để đạt các kết quả đó |
| L01-D02 | Năm mạch của học phần | Năm nhóm bài liền nhau; mỗi nhóm gắn một ứng dụng đã xem; tách thứ tự học với tiên quyết | source.md phần B; hình H19 | 2 | Mạch phân tán và đồ thị |
| L01-D03 | Xử lý phân tán và xếp hạng | Bài 02–04: MapReduce, PageRank và các biến thể; ví dụ V02–V05 → thuộc tính trong outline | V02–V05 | 3 | Mạch biểu diễn và tìm tương đồng |
| L01-D04 | Tương đồng và hàng xóm gần | Bài 05–07: Shingling/MinHash, LSH, HNSW/PQ; nêu đầu ra mỗi bước | V06–V07 | 3 | Mạch trạng thái nhỏ trên dòng |
| L01-D05 | Dòng dữ liệu và cửa sổ | Bài 08–09: mẫu, Bloom, các phác thảo và DGIM; đại lượng cần ước lượng → cấu trúc | V08–V09 | 2 | Mạch dung lượng và khôi phục |
| L01-D06 | Nén dữ liệu và từ điển | Bài 10–11: Huffman/số học, LZ, JPEG; phân biệt hai yêu cầu khôi phục | V10–V11 | 2 | Mạch tổ chức và truy vấn trên đĩa |
| L01-D07 | Lưu trữ, chỉ mục và kết nối | Bài 12–15: sắp ngoài → chỉ mục → truy vấn chuyên biệt/nối; chỉ nhấn tên đại diện, danh mục đầy đủ trong ghi chú | V12–V16 | 3 | Các mạch cần nền tảng khác nhau |
| L01-E01 | Kiến thức cần có và cần ôn | Tiên quyết chính thức và nền xác suất, đồ thị, véc-tơ, CSDL; tự xác định phần cần ôn | source.md phần I; mục tiêu bài 02–15 | 3 | Chuyển kiến thức thành sản phẩm |
| L01-E02 | Kỹ năng cần rèn | Đặc tả, vết chạy, chứng minh, chi phí, cài đặt và đo; liên hệ CLO1–CLO3 | source.md phần II; V01 | 3 | Sản phẩm cần có nguồn và giả thiết rõ |
| L01-E03 | Học tập và xử lý dữ liệu có trách nhiệm | Đọc trước, tự học, phản biện, hợp tác, ghi nguồn/đóng góp, báo sai số và hạn chế, trách nhiệm dữ liệu | source.md CLO4 và yêu cầu học phần | 3 | Dùng mẫu trùng để kiểm chứng trách nhiệm suy luận |
| L01-F01 | Kiểm chứng kết luận từ dữ liệu | Trách nhiệm dữ liệu → liệt kê đúng mẫu trùng chưa đủ kết luận có phối hợp | MMDS 1.2; V05 | 3 | Xem một mô hình trùng ngẫu nhiên |
| L01-F02 | Mô hình ngẫu nhiên cho hồ sơ lưu trú | $P,T,H,q$; cùng khách sạn từng ngày, có thể khác giữa hai ngày; mô hình độc lập và chọn đều | V17, MMDS 1.2.3 tr.7 | 5 | Đếm phép thử trước khi thay số |
| L01-F03 | Kỳ vọng số biến cố trùng | Chỉ báo cho cặp người–cặp ngày; cộng kỳ vọng; phân biệt xấp xỉ 250.000 với kết quả tổ hợp xấp xỉ 249.750 | V17; MMDS tr.7–8 | 4 | Áp lại cả khung tính toán lẫn giả thiết |
| L01-F04 | Khung phân tích một lời giải | Câu hỏi: dùng V01 hoặc V06 nêu đầu ra, biểu diễn, giới hạn, bảo đảm và bài sẽ cung cấp phương pháp | V01/V06; source.md | 3 | Đọc và ôn kiến thức cho MapReduce |
| L01-E04 | Chuẩn bị cho bài MapReduce | Ôn khóa–giá trị, phép nhóm, bất biến; đọc MMDS Ch2; nêu cách dùng slide và ghi chú | source.md Bài 02 | 2 | Bài tập dùng lại mô hình hồ sơ lưu trú và kỳ vọng |
| L01-R00 | Bài tập củng cố | Dùng lại mô hình lưu trú để thay quy mô/tiêu chuẩn rồi xét giỏ hàng; không hiện đáp số | MMDS tr.8 | 0 | Dựng ba biến thể |
| L01-R01 | Ba biến thể của hồ sơ lưu trú | Bài 1.2.1(a–c): đọc đủ đề, dựng mô hình; gợi ý cho người cần bằng thừa số và bảng ký hiệu | V17; MMDS 1.2.1 tr.8 | 10 | Tính a, b |
| L01-R02 | Thay đổi số ngày và số người | a: 2.000 ngày; b: 2 tỷ người, 200.000 khách sạn; mỗi biến thể độc lập | V17; MMDS 1.2.1(a,b) | 15 | Đổi tiêu chuẩn trùng |
| L01-R03 | Yêu cầu trùng trong ba ngày | Phần c: giữ quy mô gốc, yêu cầu ba ngày; nộp công thức, giá trị, diễn giải | V17; MMDS 1.2.1(c) | 10 | Chuyển mô hình sang giỏ hàng |
| L01-R04 | Trùng tập mặt hàng | 100 triệu người, 100 lượt/người/năm, mỗi lượt 10 trong 1.000 mặt hàng; giữ giả thuyết nguồn và chú thích 3 | V18; MMDS 1.2.2 tr.8 | 10 | Hoàn tất lời giải rồi phản biện |
| L01-R05 | Giải thích kết quả và giới hạn | Hoàn tất/chữa 1.2.2; nộp số phép thử, xác suất, kỳ vọng và kết luận dưới giả thiết | V18; MMDS 1.2.2 | 15 | Kết thúc bằng giới hạn suy luận |

## Chu trình học tập và phạm vi rút gọn

| Cụm | Tình huống → vấn đề → trực giác | Ví dụ → hình thức → cơ chế/lập luận | Chi phí, kiểm tra và lý do gộp |
|---|---|---|---|
| Quét–cộng dồn, cốt lõi | A01 đặt dữ liệu/đầu ra; C01 nhắc ngân sách; C02 nêu bảng tổng | C02 chạy bốn bản ghi; C03 đặc tả; C04 giả mã; C05 bất biến | C06 chi phí và điều kiện bảng vừa bộ nhớ; F04 thu hồi. Đủ tám bước; bất biến tiền tố được nói đủ ba bước, không thay bằng trực giác |
| V02–V16, khảo sát ứng dụng | A02–B09 mỗi trang có đầu vào, đầu ra, cách trực tiếp và giới hạn; hình gợi một hướng xử lý | Không chạy giả mã hay chứng minh chuyên biệt trong Bài 01; D03–D07 định vị nơi sẽ học | C01/C07/C08 nêu phép đo và bảo đảm; F04 kiểm tra lựa chọn. Chu trình rút gọn vì mục tiêu là nhận diện nhu cầu, không làm chủ thuật toán bài sau |
| V17, mô hình xác suất | F01 đặt nhu cầu kiểm tra kết luận; F02 dựng tình huống và trực giác về nhiều phép thử | F02 nêu giả thiết trước xác suất; F03 định nghĩa biến đếm, cộng kỳ vọng và thay số | R01–R03 thay quy mô; thuật toán/chi phí triển khai không áp dụng vì đây là phép đếm mô hình |
| V18, bài tập nguồn | R04 giữ đề và giả thuyết, đặt dữ kiện mua hàng | Người học dựng mô hình; R05 chữa và kiểm tra ý nghĩa biến đếm | Không biến thành bài học khai phá tập phổ biến hoặc thuật toán phát hiện con người |
| D/E, giới thiệu khóa học | Dựa ứng dụng và khung C | Nêu chương trình, tiên quyết và sản phẩm; không thêm định lý | Người học tự đánh giá phần cần ôn; tám bước giải thuật không áp dụng cho thông tin học phần |

Câu kiểm tra trên mặt trang dùng nhãn “Câu hỏi:”. Mã trang, V/H và nhãn quy trình chỉ ở tệp kế hoạch. Chi tiết thời lượng nằm ở storyboard và hướng dẫn tổ chức; lời giảng không đọc các mã nội bộ.

## Đặc tả hình cho mọi ví dụ

Toàn bộ 19 tệp dưới đây đã được dựng trong 2627-1/img/lec-01/. V01/V17/H19 thay hình cùng tên; 16 tệp còn lại được thêm mới. Các tài sản bài khác chỉ làm nguồn tham khảo, không sửa. Hai SVG cũ về giao thoa lĩnh vực và thể tích gần biên được giữ nhưng không còn dùng trong tuyến mới. Bản đồ H19 dùng chung với index nên phải kiểm định cả hai nơi.

Bố cục ER-001 phần A: câu nêu bài toán, hình đối tượng/đầu ra/trở ngại, thẻ khó khăn; A01 ghép bảng HTML với hình bộ nhớ. ER-002 áp dụng cùng nguyên tắc cho B; C–R giữ nguyên. Hình định tính là sơ đồ, không phải kết quả đo. SVG có role, title/desc, nhãn tiếng Việt và nét/hình hỗ trợ màu; bảng, công thức, giả mã bằng HTML/KaTeX.

| Ví dụ / hình | Tệp dự kiến | Dữ liệu, bố cục và quan hệ phải giữ | Kết luận hình và văn bản thay thế dự kiến | Nguồn / tài sản tham khảo | Chỗ dùng lại |
|---|---|---|---|---|---|
| V01 / H01 | kho-nhat-ky-bo-nho.svg | Tệp trên đĩa không vừa bộ nhớ; mũi tên nạp toàn bộ bị chặn. SVG 600×360 để đọc trong cột. Bảng HTML dùng lại bốn bản ghi C02, tổng 55/25/0; không vẽ bảng trong SVG | Tệp lớn buộc đổi cách đọc và trạng thái giữ lại | Stanford intro62; MMDS1.3.4 tr13 | A01, C01–C06, E02, F04 |
| V02 / H02 | ung-dung-tong-hop-phan-tan.svg | Từ w ở hai phần kho; gom toàn bộ tài liệu qua mạng về một máy để đếm. Không gán số đếm | Mạng và một máy nhận trở thành nút thắt; phần chữ nêu lỗi chạy lại | MMDS Ch2 slide8–13,20; sách2.1–2.2.6 | A02, C01, D03 |
| V03 / H03 | ung-dung-xep-hang-web.svg | Giữ y→y,a; a→y,m; m→a. Hộp là trang, đầu ra điểm từng trang hỗ trợ sắp kết quả; dải đọc/cập nhật/lặp | Điểm phụ thuộc nhau, chi phí phát sinh nhiều vòng; không gán điểm/thứ hạng | MMDS5.1–5.2; Link Analysis1:18–21,48,53 | A03, C01, D03 |
| V04 / H04 | ung-dung-truy-van-theo-chu-de.svg | Jaguar có bốn nghĩa; chủ đề ô tô đã biết dẫn tới mục tiêu ưu tiên trang về xe | Một từ chưa chốt đầu ra; thẻ khó khăn nêu chi phí bộ điểm riêng theo người | MMDS5.3.1 tr195–196 | A04, C08, D03 |
| V05 / H05 | ung-dung-lien-ket-thao-tung.svg | Giữ ba nhóm Hình5.16; khoanh nét đứt t và trang hỗ trợ cùng bên kiểm soát; nhóm có thể tác động→t; t↔mỗi hỗ trợ | Nhiều liên kết cùng bên tạo có thể đẩy điểm; cần hạn chế ảnh hưởng | MMDS5.4.1–5.4.4/Hình5.16 | A05, D03, F01 |
| V06 / H06 | ung-dung-tai-lieu-gan-trung.svg | Hai tài liệu có phần chung/phần sửa; bốn biểu tượng nối đủ sáu cặp không hướng; công thức bằng KaTeX. Bỏ chuỗi chữ ký chưa định nghĩa | Đầu ra là cặp; xét tất cả tăng theo số cặp. Nét minh họa định tính, không đo tương đồng | MMDS3.1–3.4; Stanford03-lsh14 | A06, C01/C08, D04, F04 |
| V07 / H07 | ung-dung-truy-hoi-vec-to.svg | Truy vấn dạng véc-tơ được so với các đoạn tài liệu đã mã hóa; đầu ra k đoạn gần. Bỏ chỉ mục/độ thu hồi khỏi hình | Mỗi truy vấn quét lại kho, tính nhiều khoảng cách; không gán tọa độ hay kết quả giả | BIODS271 PDF16–18; Princeton08:2–5 | A07, C07–C08, D04 |
| V08 / H08 | ung-dung-dong-truy-van.svg | Hai nhiệm vụ tách biệt: nhật ký truy vấn tạo mẫu theo người dùng; thư đến được kiểm địa chỉ theo danh sách cho phép. | Minh họa định tính yêu cầu bài toán; không gán kết quả hoặc số đo mới | MMDS 4.1–4.3; Streams 1 slide 6; lec-08/stream-model.svg, bloom-pipeline.svg | B01, C07–C08, D05 |
| V09 / H09 | ung-dung-thong-ke-cua-so.svg | Trục thời gian tách các lượt truy cập quá cũ khỏi cửa sổ gần đây; đếm người dùng khác nhau phân biệt với đếm lượt. | Minh họa định tính yêu cầu bài toán; không gán kết quả hoặc số đo mới | MMDS 4.4–4.7, Hình 4.2–4.4; UMass Count-Min; lec-09/decision-map.svg | B02, C08, D05 |
| V10 / H10 | ung-dung-nen-van-ban.svg | Văn bản gốc được lưu thành dữ liệu mã và thông tin giải mã; đầu ra phải khôi phục nguyên vẹn chuỗi. | Minh họa định tính yêu cầu bài toán; không gán kết quả hoặc số đo mới | Nelson–Gailly Ch3/9; CMU LZ logic11–14; Bài11 Z00; lec-11/two-contracts.svg | B03, C08, D06 |
| V11 / H11 | ung-dung-nen-anh.svg | Các mức sáng gần nhau được gộp về mức đại diện; chi tiết mức sáng bị mất nên ảnh khôi phục có thể khác ảnh gốc. | Minh họa định tính yêu cầu bài toán; không gán kết quả hoặc số đo mới | Nelson–Gailly Ch11; CMU lossy logic2–16; lec-11/two-contracts.svg; Bài11 J00–J06 | B04, C08, D06 |
| V12 / H12 | ung-dung-sap-xep-ngoai.svg | Các bản ghi được đổi từ thứ tự bất kỳ sang khóa tăng dần; tệp đầu vào lớn không thể nạp trọn vào bộ nhớ. | Minh họa định tính yêu cầu bài toán; không gán kết quả hoặc số đo mới | DSC Ch15 slide 17–23; lec-12/external-sort.svg, kway-merge.svg | B05, C01, D07 |
| V13 / H13 | ung-dung-tra-cuu-khoa.svg | Hai yêu cầu: tìm theo một mã và tìm lương trong đoạn kín; đầu ra là hồ sơ thỏa điều kiện, không phải toàn bảng. | Minh họa định tính yêu cầu bài toán; không gán kết quả hoặc số đo mới | DSC Ch14 slide 3–16; Bài13 mở bài; sơ đồ hóa đặc tả truy vấn | B06, C07, D07 |
| V14 / H14 | ung-dung-tim-tu-khoa.svg | Hai từ khóa phải cùng có mặt trong mỗi tài liệu kết quả; tài liệu chỉ chứa một từ không thỏa điều kiện. | Minh họa định tính yêu cầu bài toán; không gán kết quả hoặc số đo mới | DSC Ch31 tr.13–16, slide 14–16; lec-14/text-index.svg, inverted-disk.svg | B07, D07 |
| V15 / H15 | ung-dung-truy-van-khong-gian.svg | Vùng cần tìm Q giao hộp bao A và B của hai nhóm đối tượng; phải kiểm đối tượng trong cả hai nhóm trước khi trả kết quả. | Minh họa định tính yêu cầu bài toán; không gán kết quả hoặc số đo mới | DSC Ch24 slide 17, 21–24; Auburn PDF 10–13; lec-14/rtree.svg, filter-refine.svg | B08, C08, D07 |
| V16 / H16 | ung-dung-noi-bang.svg | Hồ sơ sinh viên và lượt đăng ký được ghép bằng mã sinh viên; một sinh viên có thể tạo nhiều kết quả ứng với nhiều lượt đăng ký. | Minh họa định tính yêu cầu bài toán; không gán kết quả hoặc số đo mới | DSC Ch15 slide 24, 28, 40; lec-15/join-usecase.svg | B09, C01, D07 |
| V17 / H17 | phep-thu-va-duong-tinh-gia.svg | Cặp người × cặp ngày → biến cố cùng khách sạn; giữ giả thiết $P,T,H,q$. Khi sang ba ngày đổi khung bộ ngày; không vẽ người bị gán nhãn phạm tội. Công thức và kết quả bằng KaTeX | Nhiều phép thử có thể tạo nhiều biến cố ngẫu nhiên. Alt: “Một cặp người và một bộ ngày xác định một phép thử về trùng khách sạn.” | MMDS 1.2.3–1.2.4 tr.7–8; SVG Bài 01 hiện có cần rà/sửa | F02–F03, R01–R03 |
| V18 / H18 | ung-dung-trung-gio-hang.svg | Người → các lượt mua → tập 10 trong 1.000 mặt hàng → so cặp lượt của hai người khác nhau. Số 100 triệu và 100 lượt/năm giữ nguyên; không vẽ sản phẩm mới cụ thể | Phải đếm đúng đối tượng và giữ giả thuyết nguồn. Alt: “Hai lượt mua của hai người được so sánh theo tập mười mặt hàng đã chọn.” | MMDS 1.2.2 và chú thích 3, tr.8; sơ đồ hóa đề bài | R04–R05 |
| Bản đồ / H19 | ban-do-hoc-phan.svg | Bài 01 → năm nhóm liên tiếp 2–4,5–7,8–9,10–11,12–15. Mỗi nhóm một ví dụ đã xem; danh sách thuật toán đầy đủ nằm trang D03–D07, không nhét vào SVG | Nhóm nội dung có nhiệm vụ và nền tảng chung. Alt: “Bài một cung cấp nền chung cho năm mạch gồm các bài hai đến mười lăm.” | source.md phần B; SVG Bài 01 hiện đang dùng ở index | D02; cần rà tác động index khi triển khai |

Không yêu cầu một hình minh họa cho từng tên thuật toán trong danh mục D. Phải có hình cho mọi tình huống đang kể; danh mục này bao phủ V01–V18. Những trang dùng lại ví dụ phải dùng lại dữ kiện và hình, không tạo phiên bản số liệu khác.

## Dữ kiện số và lời giải cần bảo toàn

- V06: $N=10^6$, $\binom N2=499\,999\,500\,000\approx5\times10^{11}$. Đây là phép đếm mô hình. Bỏ ví dụ tốc độ “một triệu so sánh/giây” khỏi Bài 01 để tránh nhầm với đo thực nghiệm.
- V01: vết hiện có cho a.vn:55, b.vn:25, c.vn:0. Nguồn lược đồ là Stanford62; dữ liệu nhỏ là minh họa đã có của học phần. C05 phải kiểm cả khóa c.vn có tổng0.
- V17: $P=10^9,T=1000,H=10^5,q=0{,}01$; chọn khách sạn đều có điều kiện đã đi; độc lập giữa người/ngày trong mô hình. Đặt $X$ là số biến cố cặp người–cặp ngày:
  $$\mathbb E[X]=\binom P2\binom T2\left(\frac{q^2}{H}\right)^2.$$
  Kết quả tổ hợp là $249\,749{,}99975025$; làm tròn $249\,750$, nguồn dùng xấp xỉ $250\,000$. Không gọi số làm tròn là giá trị chính xác.
- R02a thay riêng $T=2000$; R02b thay riêng $P=2\times10^9,H=2\times10^5$. R03 giữ quy mô gốc và dùng $\binom T3(q^2/H)^3$. Các đáp số, phép tính và lập luận nằm trong ghi chú diễn giả khi triển khai.
- V18: các lượt mua chọn đều, độc lập những tập 10 phần tử theo mô hình giải bài; hai người khác nhau, mỗi người 100 lượt. Với $Y$ đếm cặp lượt của hai người có cùng tập:
  $$\mathbb E[Y]=\frac{\binom{10^8}{2}\,100^2}{\binom{1000}{10}}.$$
  Giữ giả thuyết của đề/chú thích3 khi kết luận; không suy xác suất có điều kiện về danh tính chỉ từ kỳ vọng. Công thức là lời giải trong ghi chú, không hiện trước lúc chữa.

Phần F gồm 3 phút về giả thiết và trách nhiệm, 9 phút dựng mô hình xác suất và kỳ vọng, 3 phút kết luận và 2 phút chuẩn bị MapReduce. Recitation giữ nguyên yêu cầu toán học, chỉ dịch và chia bước như bản trước. Vì phần lý thuyết xác suất giảm, R01 dành phần đầu để dựng lại mô hình; gợi ý phân tầng gồm bảng ký hiệu, số phép thử, xác suất một phép thử. R04 có sơ đồ đơn vị người/lượt/tập để tránh nhầm. Hai bài này đo mô hình hóa và diễn giải; các mục tiêu về tài nguyên và bản đồ khóa học được kiểm tra ở C06, C08, E01 và F04, không tuyên bố recitation đánh giá đủ mọi mục tiêu.

## Lịch sử ánh xạ từ bản trước và ghi chú

| Cụm hiện có | Quyết định cho lần triển khai | Nơi đích / tác động |
|---|---|---|
| P00–P01 của bản trước | Quyết định mở thẳng A01 đã được thay theo yêu cầu mới | P00/P01 mới mở bài; D01 chỉ giữ mục tiêu toàn học phần |
| A00–A08 | Giữ tình huống, vết, đặc tả, giả mã, bất biến; giảm thời lượng | A01 và C01–C06 |
| B00–B07 | Gộp năm tầng trên ví dụ; chuyển hai nghĩa mô hình/lọc thư khỏi tuyến chính | C03–C06; ghi chú đọc thêm nếu giữ |
| C00–C05 | Khai triển theo ứng dụng, thêm mạng, độ trễ và cập nhật | C01/C06–C08 |
| D00–D05 | Rút phần giảng, giữ giả thiết và hỗ trợ bài tập | F01–F03, R01–R03 |
| E00–E04 | Chuyển cao chiều sang đọc thêm; mở rộng bản đồ và sự chuẩn bị | V07, D01–E04, F04 |
| R00–R05 | Giữ đề và lời giải; thêm hình giỏ hàng và hỗ trợ tiên quyết | R00–R05 mới |
| Ghi chú N01–N10 | Cần biên tập lại lời mở, thứ tự và câu nối; giữ lập luận/lời giải còn dùng | Theo ánh xạ chủ đề bên dưới |

| note-topic-id dự kiến | Vai trò trong ghi chú tương lai | Trang tương ứng | Vào → ra |
|---|---|---|---|
| L01-N01 | cốt lõi: ứng dụng tổng hợp và tìm kiếm, định nghĩa đầu ra trước ví dụ | P00/P01, A01–A07 theo thứ tự bảng | Bối cảnh/đích học → loại dữ liệu → nhu cầu đầu ra |
| L01-N02 | cốt lõi: dòng, khôi phục, lưu trữ và truy vấn | B01–B09 | Đầu ra → giới hạn trạng thái/truy cập |
| L01-N03 | cốt lõi: đặc tả, vết, giả mã và chứng minh quét–cộng dồn | C02–C06 | Giới hạn → một lời giải đầy đủ |
| L01-N04 | cốt lõi: khung đánh giá chi phí và bảo đảm | C01, C07–C08 | Lời giải → tiêu chí so sánh |
| L01-N05 | cốt lõi: bản đồ học phần và thuật ngữ theo vai trò | D00–D07 | Tiêu chí → nhóm phương pháp |
| L01-N06 | cốt lõi: tiên quyết, kỹ năng và hành vi học tập | E01–E03; E04 ở cuối F | Nhóm phương pháp → kiến thức/kỹ năng/trách nhiệm → chuẩn bị bài tiếp theo |
| L01-N07 | cầu nối: giả thiết, kỳ vọng và giới hạn suy luận | F01–F03 | Trách nhiệm → mô hình kiểm chứng |
| L01-N08 | cốt lõi: tự kiểm và hai bài tập có gợi ý/lời giải | F04, R01–R05 | Mô hình → sản phẩm có thể kiểm tra |

Ánh xạ này đã được áp dụng cho ghi chú. Những chủ đề đọc thêm chỉ được định tuyến ở cuối, không tạo mã mới trong tuyến chính.

## Điều kiện kiểm định khi triển khai

Kế hoạch được chốt khi đủ 14 bài, 18 ví dụ có đặc tả hình, mỗi trang có vai trò/nguồn/câu nối, thời lượng $25+26+25+18+9+17=120$ và $10+15+10+10+15=60$. Kiểm tra số trang 45+6=51, bảy phần ngoài, các mã duy nhất. R00 được tính trong 51 trang nhưng chỉ chuyển phần, không tính vào 60 phút làm bài của R01–R05.

Rà lại toàn bộ bài vì mở bài và luận điểm đã đổi. Kiểm thử RevealJS/ghi chú/SVG ở 1280×720, màn hình hẹp, bàn phím và bản in; nguồn, hình, KaTeX và tài nguyên cục bộ; rà năm góc nhìn độc lập và xử lý lỗi bắt buộc. H19 dùng chung với index phải được kiểm tra tại trang chỉ mục. Kết quả thực thi nằm trong review-log, không suy đạt chỉ từ đặc tả này.

## Khuôn ghi chú và quyết định triển khai

| note-topic-id | Đầu vào → sản phẩm → nối ra | Thành phần áp dụng và phần không áp dụng |
|---|---|---|
| L01-N01 | Tệp, tập hợp, đồ thị/véc-tơ → phân biệt bảy đầu ra → thêm nhu cầu dòng/lưu trữ | Vai trò, đặc tả, ví dụ/hình, giới hạn, kiểm tra. Không có giả mã/chứng minh chuyên biệt vì chỉ khảo sát ứng dụng Bài 02–07 |
| L01-N02 | Các đầu ra đã gặp → phân biệt khôi phục, truy cập, cửa sổ → khung tài nguyên | Định nghĩa trước minh họa, hình và điều kiện. Không có định lý hoặc giả mã mới của Bài 08–15 |
| L01-N03 | V01, vòng lặp/bảng → đặc tả, vết, bất biến và chi phí → so sánh lời giải | Đầy đủ vai trò, đặc tả, ví dụ, trực giác, mệnh đề, giả mã, chứng minh, biên, chi phí, kiểm tra. Trực quan là trạng thái bảng, không ép hình học |
| L01-N04 | Lời giải cụ thể → phân biệt năm tầng, chi phí và bảo đảm → đọc chương trình | Bảng so sánh gắn ví dụ; không có định lý/giả mã vì đây là khung phân tích |
| L01-N05 | Khung đánh giá → tên/vai trò/thuộc tính của 14 bài → chuẩn bị | Bản đồ và bảng 14 bài. Không áp dụng chứng minh/giả mã cho thông tin chương trình |
| L01-N06 | Bản đồ và nền cá nhân → kế hoạch ôn, sản phẩm, hành vi → trách nhiệm suy luận | Tiên quyết, kỹ năng, tự chẩn đoán, chuẩn bị Bài 02. Không áp dụng định lý/thuật toán |
| L01-N07 | Tổ hợp, độc lập, kỳ vọng → biến đếm/giá trị đúng → bài tập | Vai trò, mô hình, hình, suy diễn và giới hạn. Không có thuật toán/cận triển khai vì chỉ đếm theo mô hình |
| L01-N08 | Mô hình nền → lời giải hai bài nguồn → giới hạn khi diễn giải | Đề, hình, gợi ý, lời giải và kiểm tra. Lập luận chỉ báo cho xác suất có trùng giữ từ bản cũ, được chứng minh một bước; không thêm thuật toán phát hiện người |

Bố cục ứng dụng được điều chỉnh từ hình hai phần ba chiều rộng sang hình toàn chiều ngang phía trên, ba thẻ dữ liệu/kết quả/giới hạn ở dưới để giữ chữ trong SVG dễ đọc. Mỗi trang vẫn có một luận điểm. H15 giữ vị trí tương đối A/B/Q, chỉ dịch cả nhóm hình khi vẽ lại; không tự thêm hình học thật. H10 giữ đúng chuỗi, không thêm mã hoặc tỷ lệ nén. H19 giữ năm nhóm và tên bài; danh mục phương pháp ở D03–D07 và bảng ghi chú.

Ghi chú diễn giả không đọc mã nội bộ hoặc phút. Thời lượng tổ chức giữ ở bảng từng trang: R01 dựng mô hình10, R02 giải(a,b)15, R03 giải(c)10, R04 dựng giỏ hàng10, R05 hoàn tất/chữa15 phút; R00 chuyển phần không tính. Các lời giải và hướng chấm ở đúng trang bài tập. Không phát sinh mã trình diễn.

## Tiêu chí riêng cho trang mở đầu và cầu nối

Sáu trang P00/P01/B00/B10/B11/D00 mở bài hoặc kết nối các cụm. Chúng không có thuật toán hay định lý mới, nên không áp dụng chu trình giả mã–chứng minh riêng. P00 nhận diện bài; P01 nêu sản phẩm học tập; các trang còn lại xác định sự thay đổi đầu ra hoặc tài nguyên. Không thêm SVG trang trí. A08/A09 đã bỏ theo ER-001; phần giới thiệu dùng ngữ cảnh và câu nối ngay trong các ví dụ.

C01 gộp điểm vào phần C với khung tài nguyên; E01 nối chương trình với nền kiến thức; F01 nối trách nhiệm với suy luận; R00 nối mô hình lưu trú với bài tập. E04 nằm sau F04 để chỉ giao chuẩn bị bài kế tiếp khi kết thúc lập luận. Quill rà toàn bộ đường vào–ra và hai trang lân cận mỗi phía. No-ai-slop áp dụng lên mặt trang, alt, notes và Markdown; giữ nguồn, giả thiết, cảnh báo kỹ thuật và lời giải/chấm bài, bỏ lời dặn vẽ/soạn và giải trình lịch sử biên tập khỏi học liệu.

## ER-002 — bố cục và quyết định triển khai

B00 giới thiệu toàn phần; B01–B02 xét dữ liệu đang đến; B10 mở nhu cầu nén trước B03–B04; B11 định nghĩa truy cập theo khối trước B05–B09. Giữ 12 trang và thứ tự để bảo toàn ánh xạ với Bài08–15. Phần B 26 phút; tổng giảng120 và recitation60 không đổi. A và C–R giữ nguyên nội dung.

Điều phối giữ đề xuất planner về ba cụm và các trang mở cụm; sửa đề xuất giữ hình cũ vì hình cũ giới thiệu cơ chế trước bài toán. B01 dùng hai hàng cho hai đầu vào khác nhau, không coi thư và truy vấn là một dòng. B02 chuyển mômen sang ghi chú sau các đại lượng dễ hiểu. B03–B09 giữ đặc tả và nguồn; hình tập trung đầu vào, điều kiện đầu ra và trở ngại.

Các ví dụ này là khảo sát nhu cầu, không phải các thuật toán trọng tâm phải chứng minh trong Bài01. Đặc tả và khó khăn được nêu trên mặt; cơ chế và bảo đảm chi tiết chuyển tới bài tương ứng. C01 thu hồi chi phí, C07–C08 thu hồi cập nhật và điều kiện đúng. Kiểm tra ứng dụng ở F04 dùng lại khung ấy.

Nguồn bổ sung được chọn trong nguồn đã có: MMDS4.2 tr136–138 lấy mẫu theo người dùng và4.3 tr139 lọc thư; DSC14:6,10 hồ sơ giảng viên theo mã/lương; CMU lossy trang logic3 gộp mức sáng. Không thêm bộ dữ liệu. Vạch ở V12 chỉ mã hóa thứ tự tương đối, giữ đa tập trước/sau; dải sáng V11 là sơ đồ định tính, không mô phỏng chất lượng hoặc tỷ lệ nén. V15 giữ hình hộp bao nên chưa có đối tượng thật hoặc kết quả cuối; ghi rõ giới hạn trên hình và notes. Sửa quy mô student/takes về DSC15 slide24.

Writer tạo bản nháp B00/B01 và hình hai hàng trong thư mục tạm. Điều phối giữ ý ba nhóm và hai bài toán, không nhập nguyên văn: bản nháp thiếu B02, bỏ nhầm data-slide-id/notes và còn nhãn hình chật; bản tích hợp khôi phục cấu trúc mẫu và biên tập đầy đủ. Không thay đổi CSS chung.
