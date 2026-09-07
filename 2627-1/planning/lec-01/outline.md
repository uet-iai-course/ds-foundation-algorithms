# Bài 1: Bài toán dữ liệu lớn và mô hình thuật toán

## ER-004 — kế hoạch được duyệt ngày 2026-09-07

Bốn phần còn lại là D/E/F/R; A–C giữ nguyên. Điều phối đã đọc nguồn cấp học phần, ánh xạ, toàn bộ Stanford01-intro và MMDS1.2 tr.6–8. Reader lập kế hoạch82151 và nguồn67108 hoàn tất: requested_model và observed_model đều z-ai/glm-5.3-flash, provider OpenRouter.

Giữ đề xuất năm nhóm chương trình, nhánh tiên quyết, mô hình lưu trú và bài tập đúng nguồn. Bác đề xuất D chỉ có tên bài/thuộc tính: yêu cầu mới cần lý giải và minh họa. D giới thiệu ý tưởng và công dụng bằng ví dụ A/B/C; không dạy trước giả mã/chứng minh chuyên biệt của Bài02–15. Bác dùng lại nhật ký trong E02 vì C đã chuyển sang cặp gần trùng.

| Phần / chủ đề | Quyết định và vai trò | Mạch, sản phẩm và hình |
|---|---|---|
| D / nội dung học phần, cốt lõi | sửa và tách ba trang quá tải; không mở rộng danh mục | Nhu cầu → năm nhóm → cơ chế đại diện → bảo đảm. D00–D10 theo thứ tự storyboard; sơ đồ chữ ký/ứng viên, chỉ mục véc-tơ, trạng thái dòng; ví dụ cũ giữ dữ kiện |
| E / chuẩn bị học, cốt lõi và cầu nối | thêm mở phần; thay nhắc nhật ký bằng Jaccard | Kiến thức → vận dụng → sản phẩm → trách nhiệm; hình giao3/hợp8, vết chạy và báo cáo có điều kiện |
| F / giới hạn suy luận, cốt lõi | thêm mở phần, tách xác suất khỏi kỳ vọng | Bài toán lưu trú → mô hình nền → một ngày/hai ngày → đơn vị đếm → kỳ vọng → giới hạn. Giữ P,T,H,q; không đồng nhất biến cố với cặp người |
| R / bài tập nguồn, cốt lõi | sửa mở phần, thêm cầu sang tập mặt hàng | Mô hình → đổi quy mô → đổi tiêu chuẩn → đổi dữ liệu. Giữ MMDS1.2.1(a–c),1.2.2 và chú thích3; không đặt bài mới |

D17/E9/F16 và R60 phút; toàn giảng120 phút. Thời lượng được phân lại trong từng phần khi tách trang. Mọi khái niệm trên trang có nghĩa/công dụng và ví dụ hoặc hình; danh mục chi tiết trong ghi chú là tài liệu định vị bài sau, không yêu cầu học thuộc tại Bài01. Thuật ngữ được giải thích khi xuất hiện.

Dẫn nguồn MMDS và Stanford tương đương về mô hình và nhu cầu; ưu tiên MMDS cho nội dung, dùng Stanford39–43 đối chiếu đếm từ. Các mạch nén/lưu trữ theo nguồn đã ánh xạ Nelson–Gailly/CMU và DSC. Không lấy chương trình, đánh giá hay quy định riêng của Stanford thay đề cương UET.

Theo quill: rà thứ tự khái niệm, đầu vào/đầu ra từng phần và hai trang lân cận; F thay kết luận nên rà toàn bài. Theo no-ai-slop: bỏ lời dành cho người soạn, tiêu đề kể tiến trình và danh sách tên thiếu nghĩa; giữ giả thiết và nguồn. Không tạo quill.json. Mỗi phần qua storyboard, năm reviewer độc lập, writer sửa riêng, kiểm định trình duyệt rồi commit/push. Codex Slides hiện nháp0trang; dùng RevealJS cục bộ theo giới hạn đã báo.

### E — triển khai ER-004

Phần E có6trang/9phút: E00mở phần → E01nền theo nhóm → E05vận dụngtậphợp → E02sản phẩm → E06báocáo → E03trách nhiệm. Toàn bài66trang,7phần,120+60phút. N06cốt lõi theo CLO1–CLO4, nối N05→N07; định nghĩa kỹ năng trước ví dụ trong ghi chú; slide lấy lại giao3/hợp8 và recall3/5 đã giải thích. Thêm hoc-tap-san-pham.svg; tái dùng hai hình nguồn, không có số đo mới. Không áp chu trình giải thuật đầy đủ cho thông tin cách học, nhưng có vận dụng và sản phẩm kiểm tra được. Writer8112 soạn mở phần; điều phối giữ ba nhánh, bỏ câu chỉ dẫn người trình bày khỏi draft.

## ER-003 — lịch sử bản ngày 2026-09-07

Yêu cầu đang xử lý: phần mở “Phân tích thuật toán xử lý dữ liệu lớn”, gồm đặc tả và đánh giá; có kết nối, tổng quan và trang riêng cho từng tiêu chí với khái niệm, ví dụ, hình. Bổ sung của người dùng: bỏ cách gọi “tổng byte” và ví dụ cộng dồn quá đơn giản khỏi phần phân tích.

Điều phối duyệt hai đề xuất độc lập của reader, đối chiếu trực tiếp sách MMDS3 tr.73–75, slide MMDS Ch3:15–17 và Stanford03-lsh:14–18. Giữ Ví dụ3.1 giao3/hợp8 và quy mô một triệu tài liệu; ưu tiên MMDS cho ngữ nghĩa và chuỗi biểu diễn/ứng viên, dùng Stanford đối chiếu quy mô. Bác chia bảy phần ngoài bên trong C và nội dung băm/shingle/LSH chi tiết của planner: C vẫn một phần ngoài, cơ chế chuyên biệt thuộc Bài05–07. Không lấy số ngày làm tròn trong slide làm số đo.

Phạm vi: C00–C16 thay C01–C08 cũ; A01 chỉ sửa lời hẹn ví dụ, B09 đổi câu nối, F03/F04 đổi cách thu hồi, E01 thay tự kiểm bảng tổng, E04 thêm cầu sang phân tán và bỏ cách gọi bị phản đối. Giữ bài tập nguồn. 60 trang, 7 phần; 120+60 phút. Dàn thời lượng và ánh xạ từng trang trong storyboard là bản hiện hành; các mục ER-001/ER-002 bên dưới là lịch sử.

| Chủ đề | Nhãn / quyết định | Vai trò, tiên quyết, sản phẩm và kết nối |
|---|---|---|
| Đặc tả cặp gần trùng | cốt lõi / thay cộng dồn | Tập hợp→Jaccard3/8→R; lấp khoảng trống định nghĩa gần trùng của A06; dùng MMDS3.1, không kết luận ngữ nghĩa |
| Xét mọi cặp | cốt lõi / giữ cơ chế trực tiếp của nguồn, hình thức hóa | Vòng lặp→giả mã→bất biến phần đã xét→O(N²L); không giảng cơ chế LSH |
| Mười khía cạnh đánh giá | cốt lõi / tách | Đúng, tính, RAM, I/O, mạng, trễ, xây, cập nhật, dung lượng, chất lượng; mỗi tiêu chí có trang riêng và hình |
| Ứng viên và bỏ sót | cầu nối / thêm vào cuối C | Kết quả đúng từng cặp chưa chắc đủ; A∩R và điều kiện R⊆A trong ghi chú; nối sang phương pháp D |
| Shingling/MinHash/LSH chi tiết | chuyển bài | Không cần để đạt mục tiêu Bài01; chỉ dùng tập đoạn và vai trò bộ lọc; cơ chế ở Bài05–06 |
| Ví dụ cộng dồn | bỏ khỏi phân tích C | A01 vẫn là một bài toán khảo sát; không dùng làm ví dụ xuyên suốt hoặc câu kiểm tra cuối |

Cập nhật nguồn độc lập đề nghị dùng tiêu chí ANN nhưng chưa có cập nhật chỉ mục trong phần đã đọc; dùng DSC14:4,10–11 cho ví dụ thay lương, không suy diễn cơ chế cập nhật ANN. Các tiêu chí khác dùng DSC15:17–28, MMDS2.2/2.5, Nelson–Gailly và nguồn Bài07 đã ánh xạ. Không thêm số đo, tỷ lệ nén hoặc dữ liệu nguồn mới.

Quill rà tuyến A/B→cặp gần trùng→đặc tả→đánh giá→D; ghi chú định nghĩa trước ví dụ, slide trực giác/ví dụ trước hình thức. No-ai-slop bỏ câu hỏi tu từ, diễn đạt khổng lồ/bất khả thi vô điều kiện và chỉ dẫn người soạn. Không tạo quill.json. Codex Slides dự án cũ vẫn draft/0slide; kiểm RevealJS cục bộ theo ngoại lệ đã báo, không tuyên bố đã đồng bộ trình soạn ấy.


## ER-002 — dòng dữ liệu, lưu trữ và truy vấn

Kế hoạch được điều phối duyệt ngày 2026-09-06: giữ 12 trang B và 26 phút; toàn bài 51 trang, bảy phần, 120+60 phút. B00 giới thiệu cả ba nhóm nhu cầu; B10 mở cụm nén; B11 mở cụm xử lý tệp trên đĩa. Ba nhóm không phải các bước bắt buộc của một hệ thống.

Giữ chín ví dụ, sửa cách trình bày theo phần A: nhiệm vụ và đầu ra trước hình; hình giải thích dữ liệu và trở ngại; thẻ khó khăn thay nhãn trừu tượng. B01 phân biệt lấy mẫu truy vấn theo người dùng với lọc thư theo danh sách cho phép. B02 dùng người dùng và lượt truy cập để giải thích thống kê; mômen ở ghi chú, không xuất hiện trước định nghĩa trên mặt trang. Phần D vẫn định vị các thuật toán chuyên biệt.

Nguồn: MMDS4.1–4.7 cho dòng; Nelson–Gailly và CMU cho nén; DSC14/15/24/31 cho lưu trữ và truy vấn. MMDS Streams1:3–9 và Stanford CS246 16-streams:4–9 tương đương về nhu cầu, ưu tiên MMDS; sách cung cấp ví dụ cụ thể. Sửa dẫn quy mô hai bảng sang DSC15 trang chiếu24. Giữ ngân sách20 khối từ ví dụ Bài15. Không thêm dữ liệu số hoặc kết quả thực nghiệm.

Vẽ lại hình để giảm khái niệm cần biết trước; giữ quan hệ Q giao cả A và B trong hình vùng. Quill nối từ yêu cầu tìm kiếm của A sang ba nhóm công việc, rồi thu các giới hạn về khung phân tích C. No-ai-slop bỏ tiêu đề kể tiến trình, chỉ dẫn người viết và các câu thiếu đối tượng cụ thể. Đồng bộ ghi chú; A và C–R không đổi.

## ER-001 — làm rõ bài toán trong phần giới thiệu

Yêu cầu ngày 2026-09-06 trong edit_request.md: sửa section đầu để người mới hiểu bài toán, khó khăn do quy mô hoặc triển khai và hình minh họa. Phạm vi P00/P01/A01–A07, bảy SVG tương ứng và phần đầu ghi chú; giữ B–R. Kế hoạch này thay bản nháp 52 trang chưa triển khai và các mô tả phần A trong lịch sử bên dưới.

Điều phối duyệt kế hoạch reader 41911: P00 chỉ nhận diện bài; P01 nêu mục tiêu khái quát; bỏ A08/A09 vì lặp đầu ra mà chưa đặt bài toán mới. Bảy ví dụ đi từ nhiệm vụ và đầu vào–đầu ra đến trở ngại; hình chỉ rõ đối tượng và cách trực tiếp gặp khó, không giới thiệu sớm chuỗi chữ ký/chỉ mục. Không giữ khung ba nhãn ngắn nếu chúng che mất ý nghĩa. Bác đề xuất ghi thời lượng trong notes; thời lượng chỉ ở storyboard. Phần A vẫn 25 phút, phân bổ 1/2/3/3/3/3/3/4/3; toàn bài 51 trang, bảy phần, 120+60 phút.

Quill dùng rà ngữ cảnh trước thuật ngữ, nối A02→A03 (từ thống kê nội dung sang sắp kết quả), A05→A06 (điểm hạng và bản sao), A07→B00 (kho và dòng yêu cầu). No-ai-slop dùng bỏ lời dẫn trên trang bìa, tiêu đề chỉ gọi lĩnh vực, nhãn mơ hồ và chỉ dẫn người soạn; giữ giả thiết và câu hỏi học tập. Không khởi tạo dự án sách. Rà mạch toàn bài và kiểm trực quan sau triển khai.

| Trang | Quyết định / sản phẩm nhìn thấy | Nguồn và giới hạn cần giữ |
|---|---|---|
| A01 | sửa: cộng kích thước trang web theo máy chủ; dùng lại bảng bốn bản ghi C02; hình kho lớn và bộ nhớ hữu hạn | Stanford intro62 cụ thể hơn MMDS về URL/size; MMDS1.3.4 tr13 cho chi phí; không nhầm với lưu lượng |
| A02 | sửa: đếm mọi lần xuất hiện của từng từ trên nhiều máy; hình cùng từ ở các phần kho và nút thắt truyền mạng | MMDS Ch2 slide8–13,20 và sách2.1–2.2.6; không đếm số tài liệu, không tự tạo số đếm |
| A03 | sửa: tính điểm quan trọng theo liên kết để hỗ trợ tìm kiếm; giữ đồ thị y,a,m và chỉ ra tính lặp | MMDS5.1–5.2/Link Analysis1:18–21,48,53; không tự gán điểm hay coi điểm liên kết là độ liên quan đầy đủ |
| A04 | sửa: ưu tiên kết quả theo chủ đề đã xác định; hình jaguar và lựa chọn ô tô | MMDS5.3.1 tr195–196; lưu điểm riêng toàn web cho từng người quá lớn; không bảo đảm đoán ý định |
| A05 | sửa: hạn chế tác động liên kết rác lên điểm; khoanh nhóm trang cùng bên kiểm soát | MMDS5.4/Hình5.16; giữ chiều cạnh và ba nhóm; TrustRank cần tập tin cậy, không loại hết spam |
| A06 | sửa: tìm cặp văn bản gần trùng; hình phần nội dung chung/phần sửa và tất cả cặp | MMDS3.1–3.4 ưu tiên nội dung; Stanford03-lsh14 cho quy mô một triệu; công thức bằng KaTeX |
| A07 | sửa: tìm đoạn tài liệu gần truy vấn bằng véc-tơ; hình một truy vấn đối chiếu nhiều đoạn đã mã hóa | BIODS271 L12:16 cho ứng dụng, 17–18 cho quy mô; Princeton08:2–5; không tự gán khoảng cách/kết quả |

Các chủ đề đều là cốt lõi khảo sát ứng dụng đã có; thay hình/diễn giải, không thêm thuật toán hay bài tập. Chu trình đầy đủ cộng dồn vẫn ở C02–C06. Rà nguồn độc lập, storyboard, năm góc nhìn, writer chỉnh sửa và rà mạch lại trước bàn giao.

## Lịch sử: sửa mở đầu và cầu nối trước ER-001

Yêu cầu mới thay quyết định mở thẳng vào A01: bổ sung trang tên bài, nội dung buổi học và các cầu nối trên màn hình; sau triển khai dùng no-ai-slop bỏ chỉ dẫn người soạn khỏi HTML, ghi chú diễn giả và ghi chú tự học. Quill dùng để kiểm quan hệ vào–ra; không tạo dự án sách.

Kế hoạch đã được điều phối viên duyệt sau hai đề xuất độc lập của reader (lập kế hoạch và nguồn). Thêm P00/P01 trước A01; A08 giữa A02/A03; A09 giữa A05/A06; B00 trước B01; B10 giữa B02/B03; B11 giữa B04/B05; D00 trước D01. Chuyển E04 sau F04; sửa C01, D01, E01, F01, R00 thành điểm vào phần có nội dung cụ thể. Giữ các mã cũ để truy nguyên; thứ tự là thứ tự trong storyboard, không phải thứ tự từ điển của mã.

Tám trang mới mang nhãn `cầu nối`, không thêm chủ đề học thuật, ví dụ, dữ liệu hay thuật toán. P00/P01 đặt bối cảnh và sản phẩm; các trang còn lại đối chiếu đầu ra/giới hạn của hai cụm lân cận. Nguồn và ví dụ theo bảng dưới. Không vẽ thêm hình trang trí; 19 SVG hiện có tiếp tục minh họa các ứng dụng. Bản trước sửa được lưu nguyên vẹn trong commit `0c81011`, ngoài bản sao lưu đã có.

Chấp nhận chẩn đoán thiếu mở đầu và chỉ có câu nối trong notes của planner. Bác đề xuất tăng tổng lên 123 phút và bù thời lượng không khớp số học; phân bổ lại đúng 120+60. Bác gợi ý dùng câu hỏi tu từ, mã A00 đặt cuối A, hoặc đưa “16 trang sau” lên slide. Với source reader, giữ các câu liên hệ Bài 02–15 và phân biệt liệt kê cặp với truy hồi vì đó là định hướng cho sinh viên, không phải chỉ dẫn tác giả. Giữ nhãn quy mô mô hình của 20 khối và cảnh báo toán. Bỏ lời giải trình việc vẽ/soạn, chuyển chúng về nhật ký. Sửa dẫn lưu trữ MMDS từ mục 1.3.3 thành 1.3.4, tr. 13 sau đối chiếu trực tiếp sách.

Tiêu chí: 53 trang, 7 phần ngoài, 120 phút giảng +60 phút bài tập; có mở bài, mọi ranh giới phần có câu nối, kết thúc phần giảng mới giao chuẩn bị MapReduce; không còn chỉ dẫn người viết trong học liệu. Rà lại toàn bộ bài và ghi chú, sáu reviewer độc lập gồm storyboard và năm góc nhìn, rồi writer chỉnh sửa và reviewer mạch rà lại; kiểm trực quan, công thức, bàn phím và bản in trước commit/push.

## Nền nội dung giữ từ lần triển khai trước

Đây là đặc tả cho bản triển khai ngày 2026-09-06, đã qua kiểm định nội dung và hiển thị. Yêu cầu: mở bằng ví dụ và ứng dụng từ Bài 02–15, từ đó rút ra nhiều mặt của nhu cầu giải thuật; sau đó giới thiệu học phần, nội dung sẽ học, thuộc tính cần đánh giá và sự chuẩn bị của sinh viên. Mỗi ví dụ có hình trong storyboard và bản công khai.

Người dùng đã yêu cầu triển khai cả HTML, ghi chú bài giảng, SVG và chỉ mục, sao lưu bản cũ, rồi commit/push khi kiểm định đạt. Bản sao lưu đầu tiên nằm tại `2627-1/backups/lec-01/2026-09-06-before-applications/`. Giữ số bài, tên bài và đường dẫn theo thứ tự đề xuất của nguồn cấp học phần. Bài 01 ánh xạ buổi gốc 1.

## Luận điểm và sản phẩm học tập

Một yêu cầu như tổng hợp nhật ký, tìm tài liệu gần trùng hoặc nối hai bảng chỉ trở thành lời giải khả thi khi xác định được đầu ra, cách biểu diễn, giới hạn tài nguyên và chất lượng cần bảo đảm. Quy mô còn nằm ở số cặp phải xét, số chiều, số liên kết, tốc độ dữ liệu đến và số truy vấn.

Sau Bài 01, sinh viên có thể:

1. Nêu đầu vào, đầu ra và giới hạn chính của các tình huống đã khảo sát.
2. Phân biệt đặc tả bài toán, biểu diễn, thuật toán, cài đặt và kết quả đo.
3. Đặc tả tìm cặp gần trùng; giải thích tính đúng của thuật toán xét mọi cặp và chi phí theo số tài liệu, kích thước tập.
4. So sánh các yêu cầu về tính toán, bộ nhớ, đọc/ghi, truyền thông, độ trễ và bảo đảm kết quả.
5. Đặt các thuật toán sẽ học vào năm mạch của học phần; nêu kiến thức cần ôn và sản phẩm học tập cần tạo.
6. Phân biệt kết quả tính đúng theo mô hình với kết luận có căn cứ về dữ liệu; nêu giới hạn của phép tìm mẫu trùng.

Mục tiêu 1–4 thực hiện sản phẩm Bài 01 trong nguồn cấp học phần. Mục tiêu 5 triển khai yêu cầu giới thiệu học phần của người dùng. Mục tiêu 6 giữ cầu nối từ MMDS Chương 1 sang bài tập và trách nhiệm xử lý dữ liệu. Bài 01 chưa yêu cầu sinh viên cài đặt những thuật toán chỉ mới được giới thiệu tên.

## Sáu mạch giảng và phần bài tập

| Mạch | Vai trò, đầu vào và đầu ra | Phút |
|---|---|---:|
| A. Mở đầu, tổng hợp và tìm kiếm dữ liệu web | Tên bài và nội dung buổi học → bảy bài toán có đầu vào, đầu ra, trở ngại và hình; câu nối nằm trong ngữ cảnh ứng dụng | 23 |
| B. Dòng dữ liệu, nén và truy vấn | Ba cầu nối: kho sang dòng, thống kê sang khôi phục, lưu gọn sang truy cập | 24 |
| C. Phân tích thuật toán xử lý dữ liệu lớn | Đặc tả cặp gần trùng; xét mọi cặp; tổng quan và mười tiêu chí đánh giá | 31 |
| D. Nội dung học phần | Từ giới hạn tới nhóm phương pháp, rồi giới thiệu mục tiêu học phần và năm mạch Bài 02–15 | 17 |
| E. Chuẩn bị và cách học | Nối mỗi mạch với kiến thức đầu vào, kỹ năng và trách nhiệm; dẫn thẳng sang kiểm chứng kết luận | 9 |
| F. Giả thiết và kết luận | Mẫu trùng → giới hạn suy luận → ứng dụng mở bài → chuẩn bị MapReduce ở cuối phần giảng | 16 |
| **Phần giảng** | **54 trang; sáu phần giảng, tổng bảy phần ngoài khi tính R** | **120** |
| R. Bài tập củng cố | MMDS 1.2.1–1.2.2; năm hoạt động có gợi ý và lời giải trong ghi chú diễn giả | 60 |

R là phần dọc thứ bảy sau phần giảng; có sáu trang kể cả trang chuyển phần không tính thời lượng. Tổng 60 trang, bảy phần ngoài. Hai mạch A–B giữ 16 tình huống ngắn, mỗi tình huống làm rõ dữ liệu → kết quả → giới hạn. Cơ chế chi tiết của các thuật toán chuyên biệt thuộc Bài 02–15.

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
| Xét mọi cặp gần trùng | cốt lõi | thay ví dụ cộng dồn theo người dùng; có đặc tả, vết thứ tự cặp, giả mã, bất biến, chi phí và biên |
| Đặc tả, biểu diễn, thuật toán, cài đặt và kết quả | cốt lõi | dùng cặp gần trùng; bảng phân biệt ở ghi chú, không nhồi lên slide |
| Khung chi phí và bảo đảm | cốt lõi | mở rộng theo các ứng dụng, tách I/O khỏi truyền thông và thêm độ trễ/cập nhật |
| Bản đồ chương trình và sự chuẩn bị | cốt lõi | thêm mạch D/E; tránh dồn 14 bài vào một trang cuối |
| Nhiều phép thử, V17–V18 | cầu nối | giữ ở F/R; lấp tiên quyết trực tiếp cho bài tập và cụ thể hóa trách nhiệm suy luận |
| Hai nghĩa của mô hình; ví dụ lọc thư | đọc thêm | lược khỏi tuyến giảng mới; không cần để hiểu khung đặc tả–chi phí |
| Thể tích gần biên, chứng minh cao chiều | đọc thêm | chuyển khỏi tuyến chính; V07 đủ định vị số chiều và chuẩn bị cho Bài 05–07 |
| Thuật toán chi tiết của Bài 02–15 | đọc thêm trong Bài 01 | chuyển về đúng bài; ở đây chỉ nêu vai trò, đầu ra và thuộc tính mong đợi |

Các chủ đề thêm đều lấy từ nguồn và bài đã có; không thêm mệnh đề học thuật chưa có nguồn. Nguồn phân tích độc lập và quyết định bác/giữ của điều phối viên được ghi trong review-log.

## Ký hiệu và điều kiện hiện hành

- $N$: số tài liệu; $C_i$: tập đoạn ký tự hữu hạn không rỗng của tài liệu i; $\tau\in[0,1]$: ngưỡng đã cho.
- $J(S,T)=|S\cap T|/|S\cup T|$; ví dụ giao3/hợp8. Hợp rỗng không thuộc miền đã chọn.
- $R=\{(i,j):1\le i<j\le N,J(C_i,C_j)\ge\tau\}$; $N<2$ trả rỗng.
- Duyệt mỗi cặp hợp lệ một lần, kiểm chính xác rồi xuất; bất biến kết quả đúng trên phần đã xét. Không phải lưu toàn bộ đầu ra trong RAM.
- $L$: số phần tử lớn nhất của một tập; danh sách sắp không lặp và so sánh đơn vị cho $O(N^2L)$, cận trên phần xét cặp, chưa tính tiền xử lý; có thêm chi phí xuất.
- $A$: tập ứng viên, $\widehat R=A\cap R$ sau hậu kiểm; đầy đủ khi $R\subseteq A$. Không tự đổi đặc tả chính xác sang gần đúng.
- $k$: số hàng xóm cần trả, chuẩn đúng phá hòa cố định; recall tại5 bằng3/5 trong ví dụ có sẵn Bài07.
- $F$: số khối tệp ở ví dụ I/O; đọc F và ghi F cho2F chuyển khối. Nối bảng giữ quy mô100/400khối và ngân sách20khối của Bài15.
- V01 vẫn dùng $D,M$ cho dung lượng tệp và bộ nhớ, không làm ví dụ phân tích xuyên suốt.
- V17 giữ $P,T,H,q$ và biến đếm cặp người–bộ ngày; bài tập không đổi.

## Hướng đồng bộ ghi chú khi triển khai

Ghi chú đã được viết lại theo tám chủ đề của storyboard: vai trò/đặc tả ứng dụng trước ví dụ, thuật toán xét mọi cặp gần trùng, khung đánh giá, chương trình, chuẩn bị, giới hạn suy luận và bài tập. Ký hiệu băng thông thống nhất thành $v$. Cao chiều và hai cách nhìn mô hình chỉ còn định tuyến đọc thêm; không giữ lại các mệnh đề cao chiều thiếu giả thiết trong bản cũ. Bản tự học có chứng minh đầy đủ, gợi ý và lời giải gập. Trạng thái kiểm định cuối được cập nhật trong nhật ký.

Nguồn quy trình: [bản đồ học phần](../../../sources/source.md), [slide tham khảo](../../../sources/reference-slides/README.md). Đặc tả từng trang và từng hình nằm trong [storyboard](storyboard.md); trạng thái rà soát nằm trong [nhật ký](review-log.md).

### Kết quả chỉnh sau rà ER-003

C01 phân biệt giống hệt/gầntrùng thay nhắc lại quy mô; C04 dùng N2,C1=S,C2=T cho kết quả{(1,2)} khiτ≤3/8 hoặc rỗng khiτ>3/8. Dữ kiện giữ từ Ví dụ3.1, chỉ suy ra hai trường hợp, không gán ngưỡng số mới. C16nhắc lại cặp tài liệu sau ví dụ véc-tơ. Tựkiểm E01 và cầu E04 đồng bộ. Chọn mốc2phút cho C15vàC16, giữ31phút cho C. Rà lại mạch toàn bài và độ chính xác sau writer chỉnh sửa.
