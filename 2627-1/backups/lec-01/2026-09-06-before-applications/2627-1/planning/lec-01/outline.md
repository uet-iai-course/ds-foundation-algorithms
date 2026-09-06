# Bài 1: Bài toán dữ liệu lớn và mô hình thuật toán

## Trạng thái và yêu cầu ngày 2026-09-06

Đây là kế hoạch thay thế cho lần triển khai tiếp theo. Yêu cầu: mở bằng ví dụ và ứng dụng từ Bài 02–15, từ đó rút ra nhiều mặt của nhu cầu giải thuật; sau đó giới thiệu học phần, nội dung sẽ học, thuộc tính cần đánh giá và sự chuẩn bị của sinh viên. Mỗi ví dụ có đặc tả hình trong storyboard.

Phạm vi lần này là ba tệp kế hoạch. HTML, ghi chú bài giảng, SVG và chỉ mục công khai vẫn theo bản đã phát hành; các mã trang mới dưới đây chưa tồn tại trong HTML. Giữ số bài, tên bài và đường dẫn theo thứ tự đề xuất của nguồn cấp học phần. Bài 01 ánh xạ buổi gốc 1.

## Luận điểm và sản phẩm học tập

Một yêu cầu như tổng hợp nhật ký, tìm tài liệu gần trùng hoặc nối hai bảng chỉ trở thành lời giải khả thi khi xác định được đầu ra, cách biểu diễn, giới hạn tài nguyên và chất lượng cần bảo đảm. Quy mô còn nằm ở số cặp phải xét, số chiều, số liên kết, tốc độ dữ liệu đến và số truy vấn.

Sau Bài 01, sinh viên có thể:

1. Nêu đầu vào, đầu ra và giới hạn chính của các tình huống đã khảo sát.
2. Phân biệt đặc tả bài toán, biểu diễn, thuật toán, cài đặt và kết quả đo.
3. Theo dõi một thuật toán quét–cộng dồn; giải thích bất biến, điều kiện bộ nhớ và chi phí một lượt quét.
4. So sánh các yêu cầu về tính toán, bộ nhớ, đọc/ghi, truyền thông, độ trễ và bảo đảm kết quả.
5. Đặt các thuật toán sẽ học vào năm mạch của học phần; nêu kiến thức cần ôn và sản phẩm học tập cần tạo.
6. Phân biệt kết quả tính đúng theo mô hình với kết luận có căn cứ về dữ liệu; nêu giới hạn của phép tìm mẫu trùng.

Mục tiêu 1–4 thực hiện sản phẩm Bài 01 trong nguồn cấp học phần. Mục tiêu 5 triển khai yêu cầu giới thiệu học phần của người dùng. Mục tiêu 6 giữ cầu nối từ MMDS Chương 1 sang bài tập và trách nhiệm xử lý dữ liệu. Bài 01 chưa yêu cầu sinh viên cài đặt những thuật toán chỉ mới được giới thiệu tên.

## Sáu mạch giảng và phần bài tập

| Mạch | Vai trò, đầu vào và đầu ra | Phút |
|---|---|---:|
| A. Tổng hợp và tìm kiếm dữ liệu web | Mở trực tiếp bằng tổng byte theo máy chủ; đi qua phân tán, xếp hạng, gần trùng và véc-tơ; tạo các yêu cầu đầu ra khác nhau | 22 |
| B. Dòng dữ liệu, nén và truy vấn | Mở rộng từ kho tĩnh sang dữ liệu đến liên tục, yêu cầu khôi phục và truy cập chọn lọc; tạo danh mục giới hạn | 23 |
| C. Yêu cầu đối với giải thuật | Tổng hợp giới hạn, hoàn tất ví dụ quét–cộng dồn và lập khung đánh giá một lời giải | 25 |
| D. Nội dung học phần | Dùng khung đánh giá để giới thiệu học phần, năm mạch và nhóm thuật toán ở Bài 02–15 | 20 |
| E. Chuẩn bị và cách học | Nối mỗi mạch với kiến thức đầu vào, kỹ năng cần rèn và hành vi học tập có trách nhiệm | 15 |
| F. Giả thiết và kết luận | Dùng mẫu trùng để phân biệt tính đúng với suy luận; quay lại ứng dụng mở bài và chốt cách phân tích | 15 |
| **Phần giảng** | **39 trang dự kiến; sáu phần giảng, tổng bảy phần ngoài khi tính R** | **120** |
| R. Bài tập củng cố | MMDS 1.2.1–1.2.2; năm hoạt động có gợi ý và lời giải trong ghi chú diễn giả | 60 |

R là phần dọc thứ bảy sau phần giảng; có sáu trang kể cả trang chuyển phần không tính thời lượng. Tổng dự kiến 45 trang, bảy phần ngoài. Hai mạch A–B dùng 16 tình huống ngắn, mỗi tình huống chỉ làm rõ dữ liệu → kết quả → giới hạn. Cơ chế chi tiết của các thuật toán chuyên biệt thuộc Bài 02–15.

## Bản đồ nguồn từ Bài 02–15

Các ví dụ V01–V18 và hình tương ứng được đặc tả trong storyboard. Bảng sau là danh mục nội dung để soạn; không đưa nguyên bảng 14 hàng lên một trang chiếu.

| Bài | Ứng dụng và đầu ra | Nhu cầu được rút ra | Nội dung sẽ học và thuộc tính cần đánh giá | Nguồn chi tiết truy nguyên |
|---:|---|---|---|---|
| 02 | V02: tổng hợp kho tài liệu phân tán thành số lần xuất hiện theo từ; nối với V01 tổng byte theo máy chủ | Chia việc gần dữ liệu; hạn chế truyền thông, lệch tải và làm lại khi máy hỏng | MapReduce, map/nhóm/reduce, bộ kết hợp, phân vùng; bảo toàn đóng góp, chi phí truyền, khôi phục tác vụ | MMDS 2.1–2.2.6, 2.5.1; slide Ch2: 4, 8–20; Stanford 01-intro: 32–49, 62 |
| 03 | V03: đồ thị liên kết → điểm xếp hạng trang | Dùng cấu trúc thưa, tính lặp và kiểm tra dừng | PageRank, phép lặp, xử lý nút cụt/bẫy nhện, một vòng phân tán; điều kiện hội tụ và chi phí mỗi vòng | MMDS 5.1–5.2; slide Link Analysis 1: 18–21, 48, 53; Bài 03 A00–B02 |
| 04 | V04: truy vấn “jaguar” theo ngữ cảnh; V05: cụm thao túng liên kết | Đầu ra phải phù hợp chủ đề và cách tạo liên kết | PageRank theo chủ đề, TrustRank, khối lượng rác, HITS; giả thiết tín hiệu, phạm vi đồ thị, giới hạn diễn giải | MMDS 5.3.1, tr.195–196; 5.4, Hình 5.16; 5.5; Bài 04 T00, S00–S03 |
| 05 | V06: phát hiện tài liệu gần trùng | Giảm kích thước biểu diễn; xác định độ tương đồng trước khi so sánh | Shingling, độ đo Jaccard, MinHash; bảo toàn xác suất tương đồng dưới giả thiết hoán vị đều | MMDS 3.1–3.3; slide Ch3: 15–16, 24, 32–35; Stanford 03-lsh: 14, 26–28 |
| 06 | V06: tạo cặp ứng viên rồi kiểm tra tương đồng | Tránh xét mọi cặp; kiểm soát ứng viên giả và bỏ sót | Băm nhạy cảm cục bộ (LSH), phân dải, khuếch đại; xác suất ứng viên và chi phí đối chiếu | MMDS 3.4, Ví dụ 3.10, 3.6–3.8; slide MMDS/Stanford LSH đã ánh xạ |
| 07 | V07: véc-tơ truy vấn → các véc-tơ gần | Cân đối độ thu hồi, độ trễ, bộ nhớ và xây dựng chỉ mục | HNSW, lượng tử hóa tích (PQ), IVF-PQ; phân biệt bảo đảm lý thuyết với chất lượng đo trên truy vấn | BIODS 271 PDF 17–18; Princeton lớp 8: 2–5, 8–33, lớp 9: 7–19; bài báo HNSW/PQ |
| 08 | V08: dòng truy vấn → mẫu hoặc quyết định lọc | Không biết trước độ dài; không lưu toàn bộ lịch sử | Lấy mẫu theo khóa, lấy mẫu hồ chứa, Bloom filter; phân phối mẫu, bộ nhớ, cập nhật, sai số một phía theo điều kiện | MMDS 4.1–4.3, tr.133–142; Streams 1: 3–10; Bài 08 A00–A01, B02 |
| 09 | V09: dòng sự kiện → số khóa, tần suất, mômen hoặc số sự kiện gần đây | Đại lượng truy vấn quyết định trạng thái và cách quên dữ liệu | Flajolet–Martin, Count-Min Sketch, AMS, DGIM, suy giảm mũ; loại sai số, phạm vi thời gian, bộ nhớ | MMDS 4.4–4.7, tr.142–159, Hình 4.2–4.4; UMass CS514 Lecture 10 cho Count-Min |
| 10 | V10: văn bản → dòng bit khôi phục đúng | Tiết kiệm dung lượng/truyền tải và đồng bộ giải mã | Huffman tĩnh, Huffman thích nghi, mã hóa số học; độ dài mã, chi phí mô hình, khôi phục đúng | Nelson–Gailly Ch3–5; PDF 31–37, 67–85, 96–104; Bài 10 H00 |
| 11 | V10: chuỗi lặp; V11: kho ảnh cho phép gần đúng | Khai thác lặp; chốt mức khôi phục phù hợp dữ liệu | LZ77, LZ78, LZW; JPEG dựa trên DCT; chi phí trạng thái, đồng bộ từ điển, sai số tái tạo | Nelson–Gailly Ch8–9, 11; CMU LZ logic 11–14 và lossy 2–16; Bài 11 Z00, J00–J06 |
| 12 | V12: sắp tệp lớn hơn bộ nhớ | Giảm lượt đọc/ghi khối; quản lý các dãy và bộ đệm | Sắp xếp trộn ngoài bộ nhớ, chọn thay thế; số lượt trộn, bộ nhớ, trạng thái đầu ra | Database System Concepts 7e (DSC), Ch15 slide 17–23; Ch12–13; Wisconsin PDF 16–20 |
| 13 | V13: tra khóa hoặc khoảng trên bảng lớn | Truy cập chọn lọc; trả giá cho xây dựng và cập nhật | B-Tree, B+-Tree, băm tĩnh, chỉ mục bitmap; loại truy vấn, I/O, cập nhật và dung lượng | DSC Ch14 slide 3–16, 17–59, 71–75; Ch24 slide 11–15 |
| 14 | V14: tìm từ khóa; V15: tìm đối tượng trong vùng | Chọn cấu trúc theo miền và truy vấn; phân biệt lọc với đáp án | Chỉ mục đảo, R-tree, kd-tree, ball tree, Z-order; điều kiện cắt nhánh, độ đầy đủ, tinh lọc | DSC Ch31 tr.13–16, slide 14–16; Ch24 slide 17, 21–24; Cornell PDF 1–5; Auburn PDF 10–13 |
| 15 | V16: nối student và takes theo ID | Tái sử dụng dữ liệu đọc vào; giữ đủ cặp trùng khóa | Nối vòng lặp theo bản ghi/khối/chỉ mục, Sort-Merge, Hash, Grace Hash; điều kiện bộ nhớ, lệch phân hoạch, I/O | DSC Ch15 slide 24–40; Bài 15 P01, M00 |

Bài 01 chỉ giới thiệu vai trò và tiêu chí đánh giá của các tên trên. Jaccard là độ đo; MapReduce là mô hình xử lý; chỉ mục là cấu trúc dữ liệu; Spark và Faiss là phần mềm hỗ trợ khi bài tương ứng đề cập. Không giới thiệu HyperLogLog chuẩn, Rejection Sampling, DiskANN hoặc chủ đề ngoài phạm vi đã chốt.

## Nhiều mặt của nhu cầu giải thuật

| Mặt cần đánh giá | Bằng chứng từ ứng dụng | Thuộc tính mong đợi, có điều kiện |
|---|---|---|
| Khối lượng tính toán | V06 có $N(N-1)/2$ cặp; V03 có đồ thị thưa | Khai thác cấu trúc hoặc giảm ứng viên; nêu rõ tham số và trường hợp chi phí |
| Bộ nhớ làm việc | V01, V07–V09, V12, V16 | Trạng thái vừa ngân sách; phân biệt kích thước đầu vào và trạng thái |
| Đọc/ghi và số lượt quét | V01, V12–V16 | Tận dụng đọc tuần tự, truyền khối và tái sử dụng; ghi đơn vị và giả thiết bộ đệm |
| Truyền thông và phối hợp | V02, V03 | Giảm dữ liệu trung gian, cân bằng tải, xét số vòng đồng bộ; phối hợp với hệ thống để khôi phục tác vụ |
| Độ trễ và tốc độ cập nhật | V07–V09, V13–V15 | Trả lời/cập nhật trong ngân sách; tính cả chi phí xây và duy trì chỉ mục |
| Dung lượng và khôi phục | V10–V11 | Tính cả dữ liệu phụ trợ; khôi phục đúng hoặc nêu phép đo sai số được chấp nhận |
| Đúng đặc tả và chất lượng xấp xỉ | V04–V09, V15–V16 | Nêu điều kiện đúng, xác suất sai, độ thu hồi hoặc giới hạn tinh lọc phù hợp từng phương pháp |
| Giá trị của kết luận | V05, V17–V18 | Kiểm tra giả thiết, số phép thử và giới hạn suy luận; không suy danh tính hay ý định từ mẫu trùng |

Không cộng bộ nhớ, thời gian và sai số thành một con số nếu chưa định nghĩa mục tiêu tối ưu. Không hứa mọi thuật toán đều vừa nhanh, vừa nhỏ, vừa chính xác tuyệt đối. Thuộc tính khôi phục lỗi cần được phân chia giữa thuật toán và môi trường thực thi.

## Năm mạch học phần

Thứ tự giữ nguyên: Bài 02–04 phân tán và xếp hạng → Bài 05–07 tương đồng và hàng xóm gần → Bài 08–09 dòng và cửa sổ → Bài 10–11 nén → Bài 12–15 lưu trữ, chỉ mục và kết nối. Đây là thứ tự giảng; quan hệ tiên quyết là các nhánh sau, không phải mỗi nhóm phụ thuộc toàn bộ nhóm trước:

- Bài 01 → 02 → 03 → 04.
- Bài 01 → 05 → 06 → 07; Bài 02 hỗ trợ cách tính phân tán khi cần.
- Bài 01 → 08 → 09.
- Bài 01 → 10 → 11.
- Bài 01 → 12 → 13 → 14; Bài 12–13 → 15.

MMDS Chương 1 là nền, Chương 2→5→3→4 dẫn ba mạch đầu. Nelson–Gailly cung cấp nén; DSC cung cấp lưu trữ và truy vấn. BHK Chương 1–2 giúp nhận diện giới hạn mô hình RAM và dữ liệu nhiều chiều. Không dùng danh mục chủ đề rộng hơn của Stanford để mở rộng học phần.

## Kiến thức, kỹ năng và thái độ

| Mặt | Cần có hoặc ôn khi bắt đầu | Sau học phần: sản phẩm có thể kiểm tra |
|---|---|---|
| Kiến thức | Tiên quyết chính thức UET.CS1058; cấu trúc dữ liệu, phân tích độ phức tạp, cơ sở dữ liệu, xác suất; ôn đồ thị, véc-tơ và đại số tuyến tính cho mạch tương ứng | Giải thích đặc tả, cơ chế và giả thiết của phương pháp (CLO1); phân tích bài toán để chọn mô hình và giải thuật (CLO2) |
| Kỹ năng | Lập trình Python hoặc C++; đọc giả mã và tài liệu chuyên ngành tiếng Anh; theo dõi vết vòng lặp | Viết đặc tả, chạy ví dụ, lập luận đúng, phân tích chi phí; thiết kế và triển khai giải pháp, đo hiệu suất cùng độ chính xác (CLO3) |
| Thái độ | Chủ động đọc trước, tự học, hợp tác và đặt vấn đề với giả thiết | Ghi nguồn và đóng góp; báo cáo dữ liệu, giả thiết, sai số và hạn chế; thu thập, xử lý, chia sẻ dữ liệu có trách nhiệm (CLO4) |

Cụ thể hóa cách học bằng các sản phẩm: bản đặc tả, vết chạy nhỏ, luận điểm chứng minh, bảng chi phí và báo cáo thử nghiệm có thể kiểm tra lại. Bài 01 cho sinh viên tự đối chiếu phần còn thiếu; không yêu cầu biết trước MapReduce, PageRank, HNSW hoặc các cấu trúc dòng.

Chuẩn bị Bài 02: đọc MMDS Chương 2 theo tài liệu đã chỉ định; ôn ánh xạ khóa–giá trị, phép nhóm, phép cộng kết hợp/giao hoán và bất biến. Không phát sinh bài lập trình hoặc phần mềm bắt buộc trong lần lập kế hoạch này.

Giới thiệu mã UET.DSE2053, 3 tín chỉ và CLO1–CLO4 từ đề cương. Nếu trình bày đánh giá, chỉ dùng ba trọng số đã ghi 20%/20%/60%; chưa diễn giải “TL”, số giờ tự học hoặc phân bổ CLO cuối kỳ còn mâu thuẫn. Không sao chép lịch, quy chế hay chính sách Stanford.

## Quyết định đối với chủ đề

| Chủ đề | Nhãn | Quyết định và lý do |
|---|---|---|
| Các ứng dụng V01–V16 | cốt lõi | thêm, tách theo đầu ra; thực hiện trực tiếp yêu cầu mới, mỗi ví dụ dẫn đến một yêu cầu và được dùng lại ở C/D |
| Quét–cộng dồn | cốt lõi | giữ, rút từ mạch 32 phút của kế hoạch cũ thành chu trình minh họa trong C; vẫn đủ vết, đặc tả, giả mã, bất biến, chi phí và biên |
| Năm tầng lời giải | cốt lõi | gộp vào C03–C06 trên cùng ví dụ; bỏ cụm khảo sát riêng 19 phút |
| Khung chi phí và bảo đảm | cốt lõi | mở rộng theo các ứng dụng, tách I/O khỏi truyền thông và thêm độ trễ/cập nhật |
| Bản đồ chương trình và sự chuẩn bị | cốt lõi | thêm mạch D/E; tránh dồn 14 bài vào một trang cuối |
| Nhiều phép thử, V17–V18 | cầu nối | giữ ở F/R; lấp tiên quyết trực tiếp cho bài tập và cụ thể hóa trách nhiệm suy luận |
| Hai nghĩa của mô hình; ví dụ lọc thư | đọc thêm | lược khỏi tuyến giảng mới; không cần để hiểu khung đặc tả–chi phí |
| Thể tích gần biên, chứng minh cao chiều | đọc thêm | chuyển khỏi tuyến chính; V07 đủ định vị số chiều và chuẩn bị cho Bài 05–07 |
| Thuật toán chi tiết của Bài 02–15 | đọc thêm trong Bài 01 | chuyển về đúng bài; ở đây chỉ nêu vai trò, đầu ra và thuộc tính mong đợi |

Các chủ đề thêm đều lấy từ nguồn và bài đã có; không thêm mệnh đề học thuật chưa có nguồn. Nguồn phân tích độc lập và quyết định bác/giữ của điều phối viên được ghi trong review-log.

## Ký hiệu và điều kiện của ví dụ xuyên suốt

- $n$: số bản ghi; $h$: số máy chủ phân biệt; $D$: số byte đầu vào; $M$: số byte bộ nhớ khả dụng; $v$: tốc độ đọc byte/giây.
- Đổi tên băng thông cũ $b$ thành $v$ trong kế hoạch để tránh lẫn số khối; khi triển khai phải đồng bộ HTML, ghi chú và hình cùng lúc.
- Đầu vào $L=((u_i,s_i))_{i=1}^n$, $s_i\in\mathbb N_0$; đầu ra $S[u]=\sum_{i:u_i=u}s_i$. Bản ghi hợp lệ; kiểu tổng không tràn; truy cập tuần tự.
- Bất biến gồm đúng tập khóa đã xuất hiện và đúng tổng trên tiền tố. Dừng sau $n$ bản ghi. Dãy rỗng, khóa lặp và kích thước 0 đều có xử lý.
- Chi phí kỳ vọng $O(n)$ nếu bảng băm có thao tác kỳ vọng $O(1)$; $O(h)$ mục trạng thái; một lượt quét; $T_{\rm quét}\ge D/v$ trong mô hình chỉ tính truyền dữ liệu. Bảng tổng phải vừa bộ nhớ.
- Trong V16 dùng $M_{\rm khối}=20$ khối để phân biệt với $M$ byte; quy ước là của riêng ví dụ.
- V17 giữ $P,T,H,q$: số người, số ngày, số khách sạn và xác suất lưu trú mỗi ngày. Biến đếm là biến cố cặp người–bộ ngày, không đồng nhất với số cặp người phân biệt.

## Hướng đồng bộ ghi chú khi triển khai

Ghi chú hiện có N01–N10 chưa đổi. Lần triển khai sau cần đặt vai trò/đặc tả của từng ứng dụng trước ví dụ theo chu trình tự học, rồi theo cùng thứ tự ứng dụng → nhu cầu → chương trình → chuẩn bị → giới hạn suy luận. Giữ toàn bộ lập luận quét–cộng dồn và lời giải bài tập có nguồn; tách nội dung cao chiều thành đọc thêm. Rà N01–N03, N06–N10, lời mở bài, câu kết, ký hiệu băng thông và mọi dẫn liên kết trang.

Nguồn quy trình: [bản đồ học phần](../../../sources/source.md), [slide tham khảo](../../../sources/reference-slides/README.md). Đặc tả từng trang và từng hình nằm trong [storyboard](storyboard.md); trạng thái rà soát nằm trong [nhật ký](review-log.md).
