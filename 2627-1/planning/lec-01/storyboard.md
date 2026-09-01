# Storyboard Bài 1

## Hành trình khái niệm

Tình huống xuyên suốt là kho nhật ký web không vừa bộ nhớ. Dữ liệu gồm các cặp $(u_i,s_i)$, đầu ra là tổng byte theo máy chủ, giới hạn là $M<D$ và cận truyền dữ liệu là $D/b$. Tình huống được dùng lại trong vết chạy, đặc tả, giả mã, chứng minh, phân tích chi phí và câu kiểm tra. Phần Bonferroni chuyển từ giới hạn tính toán sang giới hạn thống kê: nhiều phép thử có thể sinh nhiều biến cố trùng ngẫu nhiên. Phần số chiều lớn chỉ định tuyến, không đặt thêm mục tiêu đánh giá.

Chu trình của thuật toán quét–cộng dồn:

| Bước | Mã trang | Kiến thức đầu vào | Sản phẩm và dữ kiện truyền tiếp |
|---|---|---|---|
| Tình huống dữ liệu lớn | A01 | Tệp và bộ nhớ | $(u,s)$, tổng theo máy chủ, $M<D$ |
| Vấn đề và trực giác | A01–A03 | Quét tuần tự | Cận $D/b$ và một tổng đang chạy cho mỗi máy chủ |
| Ví dụ chạy tay | A04 | Bảng ánh xạ | Bốn bản ghi tự dựng và toàn bộ trạng thái trung gian |
| Hình thức hóa | A05 | Dữ kiện A04 | $s_i\in\mathbb{N}_0$, đầu vào, đầu ra, điều kiện trước/sau, ràng buộc truy cập riêng |
| Thuật toán | A06 | Đặc tả A05 | Giả mã một lượt quét |
| Lập luận đúng | A07 | Giả mã A06 | Bất biến gồm tập khóa và giá trị; khởi tạo, duy trì, kết thúc |
| Ứng dụng và chi phí | A08 | $n,h,D,M,b$ | Kỳ vọng $O(n)$ dưới giả thiết bảng băm, $O(h)$ bộ nhớ, một lượt, sai số 0 |
| Kiểm tra | A06, A08 | Toàn bộ cụm | Theo dõi cập nhật và nhận diện điều kiện không khả thi |

Không gộp hoặc đảo bước trong cụm trọng tâm. A03 chỉ định tuyến các dạng dữ liệu trong hai phút. Cụm B dùng lại kho nhật ký trước khi đưa ví dụ lọc thư để giảm chuyển ngữ cảnh.

## Storyboard từng trang

| Mã | Tiêu đề | Chức năng và nội dung | Nguồn | Thời lượng | Câu nối |
|---|---|---|---|---:|---|
| P00 | Bài toán dữ liệu lớn và mô hình thuật toán | Đặt kho nhật ký web làm bối cảnh | MMDS tr.1,13; Stanford 2–4,62 | 2 | Từ học phần sang mục tiêu |
| P01 | Mục tiêu học tập | Bốn sản phẩm đánh giá được; cao chiều chỉ định tuyến | `source.md`, Bài 1 | 3 | Mục tiêu đi vào kho nhật ký |
| A00 | Dữ liệu vượt khỏi bộ nhớ | Mở phần về mô hình truy cập | MMDS tr.13; BHK tr.9–12 | 2 | Đi vào tình huống cụ thể |
| A01 | Kho nhật ký không vừa một máy | Dữ liệu, đầu ra, $M<D$ và hình một lượt quét | Stanford 62; MMDS tr.13 | 5 | Từ giới hạn bộ nhớ sang cận quét |
| A02 | Một lần quét đã là một chi phí | $D,b,T_{\text{quét}}$ | MMDS tr.13 | 4 | Xem nhanh các dạng dữ liệu |
| A03 | Dữ liệu lớn có nhiều hình dạng | Nhiều bản ghi, chiều, liên kết, liên tục | Stanford 7–8; BHK tr.9–12 | 2 | Trở lại nhật ký và chạy tay |
| A04 | Một lượt quét đủ để cộng dồn | Vết bốn bản ghi tự dựng từ lược đồ nguồn | Stanford 62 | 4 | Dùng trạng thái để đặc tả |
| A05 | Đặc tả xác định kết quả cần trả | $s_i\in\mathbb{N}_0$; tách ràng buộc truy cập | Stanford 62 | 4 | Đặc tả dẫn đến giả mã |
| A06 | Thuật toán giữ một tổng cho mỗi máy chủ | Giả mã, dừng và trường hợp biên trong ghi chú | Stanford 62 | 4 | Giả mã cần chứng minh |
| A07 | Bất biến tiền tố chứng minh tính đúng | Tập khóa, giá trị, ba bước chứng minh, dừng sau n bước | Dựng từ A05–A06 | 4 | Tính đúng chưa đủ để khả thi |
| A08 | Một lượt quét đổi lấy bảng theo máy chủ | Ba chi phí, một bảo đảm, giả thiết bảng băm | MMDS tr.13 | 3 | Tách các tầng của lời giải |
| B00 | Từ bài toán đến kết quả | Mở phần: đúng toán học có thể chưa khả thi | MMDS tr.1–4 | 2 | Năm tầng lời giải |
| B01 | Năm tầng trả lời năm câu khác nhau | Bài toán, biểu diễn, thuật toán, cài đặt, kết quả | MMDS tr.1–4 | 4 | Đặt bài toán trong ba miền |
| B02 | Ba miền cùng giải quyết bài toán dữ liệu lớn | Giải thuật, học máy và hệ thống; dùng lại kho nhật ký | Stanford 7; MMDS tr.1 | 4 | Trở lại cách triển khai |
| B03 | Kho nhật ký tách bài toán khỏi cách triển khai | Đặc tả ổn định, triển khai phụ thuộc giới hạn | Tổng hợp A05–A08 | 2 | Phân loại sản phẩm mô hình hóa |
| B04 | Hai loại sản phẩm mô hình hóa | Mô hình thống kê và mô hình dữ liệu theo truy vấn | MMDS tr.2–4 | 2 | Hai sản phẩm thường gặp |
| B05 | Tóm tắt và trích đặc trưng | Ví dụ nguồn ở mức biển chỉ đường | MMDS tr.3–5 | 2 | Một ví dụ học và dùng mô hình |
| B06 | Mô hình và giải thuật trong lọc thư | Dịch Ví dụ 1.1; định nghĩa e là thư, w là từ | MMDS tr.2 | 2 | Kiểm tra phân loại sản phẩm |
| B07 | Phân loại sản phẩm tính toán | Câu hỏi phân loại phân phối ước lượng từ mẫu | MMDS tr.2–5 | 1 | Chuyển sang mô hình chi phí |
| C00 | Mô hình chi phí | Mở phần; khai triển bộ xử lý trung tâm | MMDS tr.13 | 2 | Bỏ giả định đầu vào ở bộ nhớ |
| C01 | Bộ nhớ chính không phải giả định mặc định | So sánh truy cập lặp và dữ liệu ngoài bộ nhớ | BHK tr.10; MMDS tr.13 | 5 | Phân loại chi phí và bảo đảm |
| C02 | Ba chi phí và một bảo đảm | Tính toán, bộ nhớ, truy cập; sai số là bảo đảm | MMDS tr.13 | 5 | Đặc tả chính xác và xấp xỉ |
| C04 | Kết quả chính xác và kết quả xấp xỉ | Hai loại đặc tả | MMDS tr.3–4 | 4 | Chốt phép đánh đổi |
| C05 | Phép đánh đổi phải nằm trong đặc tả | Giữ, giảm, chấp nhận; câu hỏi khi O(h) không vừa bộ nhớ | MMDS tr.3–4,13 | 3 | Nhiều dữ liệu tăng số phép thử |
| D00 | Tín hiệu giả trong dữ liệu lớn | Mở phần về nhiều phép thử | MMDS tr.5–6 | 2 | Đặt tình huống trước công thức |
| D01 | Mẫu trùng trong hồ sơ lưu trú | $P,T,H,q$; mỗi người mỗi ngày xác suất q, độc lập; cùng khách sạn từng ngày, có thể khác qua ngày | MMDS tr.7 | 5 | Phát biểu mô hình ngẫu nhiên |
| D02 | Mô hình ngẫu nhiên xác định xác suất trùng | Độc lập giữa người/ngày; chọn đều có điều kiện | MMDS tr.7 | 5 | Đếm phép thử và cộng kỳ vọng |
| D03 | Đếm biến cố trùng bằng kỳ vọng | $E[X]=\binom P2\binom T2(q^2/H)^2$; Bonferroni phi hình thức, không union bound | MMDS tr.6–8 | 6 | Thay dữ kiện cơ sở |
| D04 | Kỳ vọng khoảng 250.000 biến cố trùng | 249.750 biến cố; cặp người chỉ xấp xỉ khi hiếm | MMDS tr.8 | 6 | Kiểm tra độ nhạy không giải bài tập |
| D05 | Thay đổi quy mô quan sát | Ba thẻ chỉ nêu dữ kiện; hỏi số phép thử và xác suất đổi thế nào | MMDS Bài 1.2.1, tr.8 | 6 | Định tuyến số chiều lớn |
| E00 | Số chiều lớn đổi trực giác | Mở phần và giới hạn phạm vi | BHK tr.12,17–21 | 2 | Khoảng cách là một tổng |
| E01 | Khoảng cách là tổng của nhiều thành phần | Công thức, giả thiết và câu kiểm tra theo $d$ | BHK Ch.2 | 4 | Phân biệt với hiện tượng thể tích |
| E02 | Thể tích tập trung gần biên | Hình BHK 2.2, nêu trước độ dày 1/d, cầu nối và câu kiểm tra | BHK PDF tr.17 | 4 | Định tuyến học phần |
| E03 | Bản đồ 15 bài theo năm nhóm | Gộp 15 bài thành năm nhóm liền nhau: 2–4, 5–7, 8–9, 10–11, 12–15; Bài 1 là nền chung | MMDS tr.17–18; Stanford 10; `source.md` | 3 | Chốt cách chọn mô hình |
| E04 | Chọn mô hình theo điểm nghẽn | Bốn phép kiểm tra; kết luận phần giảng | MMDS Ch.1; BHK Ch.1–2 | 2 | Chuyển sang bài tập nguồn |
| R00 | Bài tập củng cố | Trang chuyển phần dọc | MMDS Bài 1.2.1–1.2.2, tr.8 | 0 | Đọc toàn bộ Bài 1.2.1 |
| R01 | Bài 1.2.1: ba thay đổi của hồ sơ lưu trú | Ba thay đổi quy mô cần phân tích riêng; sản phẩm là ba công thức | MMDS Bài 1.2.1(a–c), tr.8 | 10 | Tính phần a, b |
| R02 | Tăng số ngày và số người | Hoạt động cá nhân rồi đối chiếu; hai giá trị | MMDS Bài 1.2.1(a,b), tr.8 | 15 | Tính phần c |
| R03 | Yêu cầu trùng trong ba ngày | Làm và trình bày; không lộ đáp số trong giảng | MMDS Bài 1.2.1(c), tr.8 | 10 | Chuyển sang giỏ hàng |
| R04 | Trùng giỏ hàng | Khôi phục giả thuyết nguồn bằng ngôn ngữ trung tính; đủ sản phẩm | MMDS Bài 1.2.2 và chú thích 3, tr.8 | 10 | Hoàn thiện lời giải trước khi chữa |
| R05 | Chữa Bài 1.2.2 | Định nghĩa $X$ là số cặp lượt mua; đáp án chỉ trong ghi chú | MMDS Bài 1.2.2, tr.8 | 15 | Kết thúc bằng giới hạn mô hình |

## Cấu trúc bảy section ngoài

Bộ trang giữ đúng bảy section ngoài: P mở đầu; A, B, C, D là các mạch nội dung; E là định tuyến và kết luận phần giảng; R là bài tập và kết luận thực hành.

| Section | Vai | Chức năng | Kết nối vào | Kết nối ra | Đóng góp mục tiêu |
|---|---|---|---|---|---|
| P | Mở đầu | Đặt tình huống và bốn mục tiêu | Từ học phần sang buổi học | Vào mạch A | Khung đánh giá |
| A | Mạch nội dung | Chu trình quét–cộng dồn từ tình huống đến chi phí | Từ mục tiêu P01 | Sang B để tách tầng lời giải | Mục tiêu 1 |
| B | Mạch nội dung | Năm tầng và hai loại sản phẩm mô hình hóa | Từ chi phí A08 | Sang C để định lượng chi phí | Mục tiêu 2 |
| C | Mạch nội dung | Ba chi phí, một bảo đảm, đặc tả xấp xỉ | Từ phân loại B07 | Sang D khi chi phí tính toán chưa đủ | Mục tiêu 3 |
| D | Mạch nội dung | Nhiều phép thử và biến cố trùng kỳ vọng | Từ phép đánh đổi C05 | Sang E để tổng hợp kiểm tra mô hình | Mục tiêu 4 |
| E | Định tuyến và kết luận phần giảng | Số chiều lớn chỉ định tuyến; bản đồ 15 bài; bốn câu kiểm tra mô hình | Từ dữ kiện D05 | Sang R để làm bài tập | Củng cố cả bốn mục tiêu |
| R | Bài tập và kết luận thực hành | Hai bài MMDS chia năm mốc hoạt động | Từ kết luận E04 | Kết thúc bằng kiểm tra giả thiết mô hình | Mục tiêu 4 và 1 |

## Bản đồ chu trình rút gọn cho B–E

| Cụm | Tình huống và vấn đề | Trực giác, ví dụ và hình thức hóa | Cơ chế, chi phí và kiểm tra | Bước không áp dụng hoặc được gộp |
|---|---|---|---|---|
| B | B03 dùng lại kho nhật ký để tách đặc tả khỏi triển khai | B04–B06 phân biệt hai loại sản phẩm và minh họa lọc thư | B07 kiểm tra phân loại rồi chuyển sang chi phí | Không có thuật toán trọng tâm hay chứng minh mới; B06 chỉ minh họa khâu học và khâu chạy |
| C | C00–C01 đặt vấn đề dữ liệu ở ngoài bộ nhớ | C02 nêu ba chi phí và một bảo đảm; C04 hình thức hóa đặc tả xấp xỉ | C05 kiểm tra phép đánh đổi | Không có ví dụ chạy tay, thuật toán hay chứng minh mới vì cụm khai triển trực tiếp chi phí của A08 |
| D | D01 đặt tình huống hồ sơ lưu trú | D02 nêu mô hình ngẫu nhiên; D03 hình thức hóa kỳ vọng; D04 thay số | D05 kiểm tra độ nhạy rồi chuyển sang kết luận | Thuật toán và chứng minh không áp dụng vì nội dung là phép đếm kỳ vọng, không phải thuật toán |
| E | E00 đặt vấn đề số chiều lớn | E01 hình thức hóa khoảng cách; E02 minh họa thể tích gần biên | E03 định tuyến học phần; E04 kiểm tra và kết luận | Không có thuật toán hay chứng minh; cụm chỉ định tuyến nên không mở thêm ví dụ chạy tay ngoài hình BHK |

## Kiểm tra thời lượng

Phần giảng: $5+32+19+19+30+15=120$ phút.

Phần bài tập: $10+15+10+10+15=60$ phút. R00 chỉ chuyển phần.

## Storyboard ghi chú bài giảng

| `note-topic-id` | Vai trò và kết nối vào–ra | Kiến thức đầu vào | Sản phẩm học tập | Thành phần trình bày áp dụng |
|---|---|---|---|---|
| N01 | Đặt kho nhật ký ngoài bộ nhớ; dẫn sang giới hạn RAM | Tệp và bộ nhớ | Nhận diện đầu vào, đầu ra, $D>M$ và trạng thái cần giữ | Vai trò, đặc tả sơ bộ, hình và kiểm tra |
| N02 | Giải thích vì sao mô hình RAM không đủ; dẫn sang đặc tả một lượt quét | N01; truy cập tuần tự | Phân biệt truy cập ngẫu nhiên với truyền tuần tự | Vai trò, chi phí truy cập và kiểm tra |
| N03 | Hoàn tất chu trình thuật toán trọng tâm; dẫn sang các tầng lời giải | Bảng băm, vòng lặp, N02 | Đặc tả, vết chạy, bất biến, giả mã, chi phí và biên | Đủ tám thành phần; ví dụ đứng sau đặc tả theo quy tắc ghi chú |
| N04 | Tách năm tầng của lời giải; dẫn sang hai nghĩa của mô hình | N03 | Phân loại bài toán, biểu diễn, thuật toán, cài đặt và kết quả | Vai trò, định nghĩa, ví dụ và kiểm tra; không có định lý mới |
| N05 | Phân biệt mô hình thống kê với mô hình theo truy vấn; dẫn sang mô hình chi phí | Xác suất cơ bản, N04 | Xác định đúng sản phẩm mô hình hóa | Vai trò, định nghĩa, ví dụ và kiểm tra; không có thuật toán mới |
| N06 | Đặt ba chi phí và một bảo đảm; dẫn sang giới hạn thống kê | Độ phức tạp, N03–N05 | Phân tích tính toán, bộ nhớ, truy cập và sai số | Vai trò, đặc tả chi phí, ví dụ và kiểm tra |
| N07 | Dựng mô hình biến cố trùng; dẫn sang bài tập nguồn | Tổ hợp, xác suất độc lập, tuyến tính kỳ vọng | Tính và diễn giải kỳ vọng số biến cố trùng | Vai trò, định nghĩa, ví dụ, mệnh đề kỳ vọng và kiểm tra; không có thuật toán |
| N08 | Luyện thay đổi quy mô và kiểm tra giả thiết; dẫn sang cao chiều | N07; bất đẳng thức Markov cơ bản | Giải MMDS 1.2.1–1.2.2 và nêu giới hạn mô hình | Bài tập, gợi ý, lời giải và kiểm tra; Markov chỉ là cầu nối |
| N09 | Định tuyến trực giác số chiều lớn; dẫn sang bản đồ học phần | Véc-tơ, khoảng cách Euclid | Nhận diện tổng theo chiều và thể tích gần biên | Vai trò, định nghĩa, trực quan, hình và kiểm tra; không có chứng minh hay thuật toán |
| N10 | Đặt Bài 1 trong năm nhóm bài; kết thúc bằng tiêu chí chọn mô hình | N01–N09 | Dùng bốn phép kiểm tra cho một lời giải dữ liệu lớn | Bản đồ, ứng dụng và kiểm tra; không thêm mệnh đề học thuật |

Các chủ đề N02, N09 và N10 là `cầu nối`; không có chủ đề `bổ sung`. BHK PDF trang 18–21 là `đọc thêm`. Ghi chú dùng cùng dữ kiện và ký hiệu với bộ trang chiếu; khác biệt duy nhất về thứ tự là đặc tả đứng trước ví dụ chạy tay, đúng chu trình dành cho tài liệu tự học.

## Điều chỉnh nguồn

- C03 đã bỏ và gộp trước đây; mã C03 không tái sử dụng, dãy mã C nhảy từ C02 sang C04.
- Bỏ MMDS TF.IDF, băm, chỉ mục và luật lũy thừa khỏi Bài 1 vì các nội dung này thuộc bài sau.
- Bỏ Stanford 11–31 logistics; chỉ giữ trang chiếu 62 làm ngoại lệ trong khoảng 32–70.
- B03 là trang tổng hợp: dựng lại tình huống kho nhật ký từ A05–A08, không có nguồn riêng.
- Hoạt động khảo sát dữ liệu thực từ đề cương được thay bằng bài tập trực tiếp MMDS ở R01–R05, vì đề cương không cấp bộ dữ liệu và bài tập MMDS đạt cùng mục tiêu dựng mô hình xác suất.
- Chỉ dùng Stanford trang chiếu 62 trong khoảng 32–70; bỏ toàn bộ 32–61 và 63–70. Ví dụ bốn bản ghi được tự dựng từ lược đồ trang 62 để chạy tay và được ghi rõ là không phải dữ liệu thực nghiệm.
- Gộp bản đồ 15 bài thành năm nhóm bài liền nhau theo `source.md`; sửa các nhóm rời rạc cũ thành 2–4, 5–7, 8–9, 10–11 và 12–15.
- Chia MMDS Bài 1.2.1 thành các mốc R01–R03 và Bài 1.2.2 thành R04–R05; chỉ dịch, chia bước và chuyển đáp án vào ghi chú diễn giả.
- Ở R04, thay nhãn con người nhạy cảm bằng “nhóm cần phát hiện” nhưng giữ nguyên giả thuyết toán học trong bài và chú thích 3.
- Thu gọn phần số chiều lớn thành định tuyến; phân biệt rõ tổng khoảng cách ở E01 với thể tích gần biên ở E02.
