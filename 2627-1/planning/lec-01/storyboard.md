# Storyboard Bài 1

**Bản hiện hành (2026-11-13).** Deck có 100 trang: 80 trang giảng (120 phút), 8 trang Đọc thêm (mạch 5, không tính giờ) và 12 trang bài tập (60 phút); bảy mạch 15/19/25/16/8/5/12 trang. Thứ tự, quyết định, âm tiết, số dòng và thời lượng hiện hành nằm ở mục "Sửa deck theo bảng phát hiện 2026-11-13" cuối tệp; các mục bên dưới, kể cả "Sửa toàn diện theo chuẩn 2026-10-14", là lịch sử.


## Trạng thái hiện hành

ER-004 hoàn tất: D/E/F/R đã kiểm định và commit/push riêng lên origin/main. 77 trang, 7 phần (thêm sáu trang tiêu đề mạch ngày 2026-10-14); A23/B24/C31/D17/E9/F16 = 120 phút và R60 phút; thời lượng trang tiêu đề mạch lấy từ trang đầu mạch. Bảng từng trang là bản hiện hành; các thống kê trong mục triển khai từng phần ghi nhận thời điểm tương ứng.


## Bổ sung trang tiêu đề mạch 2026-10-14

Căn cứ: `AGENTS.md` mục "Trang tiêu đề mạch" và yêu cầu người dùng 2026-10-14. Mã `<tiền tố mạch>00` (L01-B00, …, L01-R00) đã thuộc các trang mở phần có nội dung, nên trang tiêu đề mạch dùng mã `<tiền tố mạch>T`, theo cách viết liền chữ cái và số của bài này. Các trang mở phần cũ giữ nguyên nội dung và đứng thứ hai trong mạch. Mỗi trang tiêu đề mạch ngoài chu trình khái niệm; thời lượng 0,5 phút lấy từ trang đầu mạch, tổng 120 + 60 phút không đổi.

| Mã trang | Tiêu đề (tên mạch) | Mục đích | Vị trí | Kiến thức đầu vào | Đầu ra | Ghi chú | Phút | Quyết định |
|---|---|---|---|---|---|---|---:|---|
| L01-BT | Dòng dữ liệu, nén và truy vấn trên đĩa | Nêu nhu cầu của mạch và từ khóa; notes nối kết quả kế thừa với kết quả giao cho mạch sau | điểm vào mạch 2, `id="mach-2"`, trước L01-B00 | Bảy nhiệm vụ trên kho web của mạch 1 | Ba loại giới hạn: bộ nhớ trước dòng dữ liệu, dung lượng, khối đọc ghi | ngoài chu trình khái niệm; tên khác tiêu đề L01-B00 | 0,5 (từ L01-B00) | thêm |
| L01-CT | Đặc tả và đánh giá thuật toán | Nêu nhu cầu của mạch và từ khóa; notes nối kết quả kế thừa với kết quả giao cho mạch sau | điểm vào mạch 3, `id="mach-3"`, trước L01-C00 | Giới hạn tài nguyên của mạch 1–2 | Bài toán mẫu tìm cặp gần trùng và khung đặc tả, tính đúng, chi phí | ngoài chu trình khái niệm; tên khác tiêu đề L01-C00 | 0,5 (từ L01-C00) | thêm |
| L01-DT | Năm nhóm thuật toán của học phần | Nêu nhu cầu của mạch và từ khóa; notes nối kết quả kế thừa với kết quả giao cho mạch sau | điểm vào mạch 4, `id="mach-4"`, trước L01-D00 | Khung đánh giá của mạch 3 | Năm nhóm Bài 02–15 với nhu cầu và phương pháp đại diện | ngoài chu trình khái niệm; tên khác tiêu đề L01-D00 | 0,5 (từ L01-D00) | thêm |
| L01-ET | Chuẩn bị và cách học | Nêu nhu cầu của mạch và từ khóa; notes nối kết quả kế thừa với kết quả giao cho mạch sau | điểm vào mạch 5, `id="mach-5"`, trước L01-E00 | Bản đồ năm nhóm của mạch 4 | Kiến thức nền cần ôn, sản phẩm học tập, trách nhiệm dữ liệu | ngoài chu trình khái niệm; tên khác tiêu đề L01-E00 | 0,5 (từ L01-E00) | thêm |
| L01-FT | Mẫu trùng ngẫu nhiên và suy luận | Nêu nhu cầu của mạch và từ khóa; notes nối kết quả kế thừa với kết quả giao cho mạch sau | điểm vào mạch 6, `id="mach-6"`, trước L01-F00 | Trách nhiệm báo cáo có giả thiết của mạch 5 | Mô hình lưu trú $P,T,H,q$, kỳ vọng nền và giới hạn kết luận | ngoài chu trình khái niệm; tên khác tiêu đề L01-F00 | 0,5 (từ L01-F00) | thêm |
| L01-RT | Bài tập vận dụng | Nêu nhu cầu của mạch và từ khóa; notes nối kết quả kế thừa với kết quả giao cho mạch sau | điểm vào mạch 7, `id="mach-7"`, trước L01-R00 | Mô hình lưu trú và kỳ vọng của mạch 6 | Hai bài MMDS 1.2.1–1.2.2 với bốn thành phần lời giải | ngoài chu trình khái niệm; tên khác tiêu đề L01-R00 | 0,5 (từ L01-R00) | thêm |

L01-P01 "Nội dung buổi học": ba thẻ nhóm được thay bằng danh sách đánh số 1–7 trùng từng chữ với tên mạch (mạch 1 "Tổng hợp và tìm kiếm dữ liệu web" mở bằng trang bìa L01-P00); giữ ba mục tiêu "Sau buổi học"; notes viết lại thành một câu cho mỗi mạch. Quyết định: sửa. Ngoại lệ tạm thời về mật độ: mặt trang L01-P01 khoảng 89–95 âm tiết, vượt trần 80 vì trang gộp danh sách bảy mạch với ba mục tiêu; đợt này chỉ đánh số theo phạm vi đã giao, đợt sau tách mục tiêu sang trang riêng.

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

### Triển khai D của ER-004

D có11trang, thêm D08/D09/D10 để tách xếp hạng, truy vấn véc-tơ và thống kê dòng. Toàn bài hiện63trang (57giảng,6bài tập),7phần; A23/B24/C31/D17/E9/F16=120, R60. Bảng từng trang dưới đây là hiện hành; thống kê ER-003 là lịch sử. Chu trình D rút gọn: bài toán A/B → ý tưởng bằng sơ đồ/ví dụ → thuộc tính cần xét → bài sẽ học. Giả mã/chứng minh chuyên biệt không áp dụng vì thuộc Bài02–15. N05 trong ghi chú mở rộng ý nghĩa các tên trong danh mục và nối N04→N06.

Bốn SVG thêm: chuong-trinh-cap-ung-vien (MMDS3.3–3.4), chuong-trinh-vec-to (Bài07/Princeton8–9), chuong-trinh-mau-loc (MMDS4.2–4.3), chuong-trinh-thong-ke (MMDS4.1,4.4–4.7). Sơ đồ định tính, không có xác suất/số đo mới; D03/D08/D06 dùng lại hình đếm từ/đồ thị/chuỗi gốc; D07 dùng bảng ánh xạ bài toán–cách tổ chức. Giữ dữ kiện, không đổi nguồn bài tập.

### E — triển khai ER-004

Phần E có6trang/9phút: E00mở phần → E01nền theo nhóm → E05vận dụngtậphợp → E02sản phẩm → E06báocáo → E03trách nhiệm. Toàn bài66trang,7phần,120+60phút. N06cốt lõi theo CLO1–CLO4, nối N05→N07; định nghĩa kỹ năng trước ví dụ trong ghi chú; slide lấy lại giao3/hợp8 và recall3/5 đã giải thích. Thêm hoc-tap-san-pham.svg; tái dùng hai hình nguồn, không có số đo mới. Không áp chu trình giải thuật đầy đủ cho thông tin cách học, nhưng có vận dụng và sản phẩm kiểm tra được. Writer8112 soạn mở phần; điều phối giữ ba nhánh, bỏ câu chỉ dẫn người trình bày khỏi draft.

### F — triển khai ER-004

F9trang/16phút: F00mở → F01bàitoán → F02môhình → F05xácsuất → F06đếm → F03kỳvọng → F07diễngiải → F04thu hồi → E04MapReduce. Toàn bài70trang/7phần/120+60phút. N07cốt lõi: định nghĩa mô hình và biến đếm trước kỳ vọng, ví dụ nguồn dùng xuyên suốt; N08thu hồi chuẩn bịBài02. Hai SVGmới suy-luan-mau-luu-tru và suy-luan-hai-ngay, nguồnMMDS1.2.3tr.7; không có dữ liệu quan sát mới. Gộp bước thuật toán/chi phí triển khai là không áp dụng vì đây là phép đếm mô hình, không thuật toán phát hiện người. F03/F07mỗi3phút cho khái niệm kỳ vọng/giới hạn suy luận. Writer50859soạn mở phần; điều phối giữ3bước, bỏ cách gọi số trùng bình thường vì chỉ tính kỳ vọng.

### R — triển khai ER-004

R7trang/60phút: R00mở3, R01dựngmôhình7, R02a/b15, R03c10, R04giỏhàng8, R06đơnvịđếm5, R05lờigiải12. Toàn bài71trang:64giảng+7bàitập,7outer,120+60phút. N09cốt lõi: bài1.2.1và1.2.2, MMDS1.2.4tr.8; các khối đề/gợi ý/lời giải Markdown giữ nguyên. Thêm phần giải thích ngoài các khối, bảng đổi đơn vị và2SVG bai-tap-quy-mo/bai-tap-ba-ngay. Chỉ chia bước/đổi bố cục, không đổi dữ kiện hoặc đặt bài. R00lấy3phút từR01; R06lấy2phút từR04và3phút từR05. Writer95599lỗi đầu ra không hoàn chỉnh; lượt79767cùng mô hình hoàn tất, giữ hai bài/bốn sản phẩm và bỏ lời chào/nhãn nhấn rỗng bằng no-ai-slop.

## ER-003 — lịch sử bản ngày 2026-09-07

Phần C được thay trọn theo yêu cầu và bổ sung bỏ ví dụ cộng dồn. Mở bằng “Phân tích thuật toán xử lý dữ liệu lớn”; dùng cặp gần trùng để thiết lập đặc tả và thuật toán, rồi tổng quan và tách mười tiêu chí. 60 trang: 54 trang giảng, 6 trang bài tập; 7 phần ngoài. Thời lượng A23, B24, C31, D17, E9, F16 =120 phút; R60 phút. E04 nằm trong phần ngoài F nên thời lượng tính vào F, không cộng theo tiền tố mã. Các phần lịch sử bên dưới mô tả bản trước, không thay bảng từng trang hiện hành.

Tăng C thêm6phút để đủ nhịp giải thích; giảm mỗi A06,A07,B03,B09,D07,F04 một phút do các bài toán được dùng lại sâu hơn trong C. Không đổi dữ kiện/bài tập nguồn hoặc thêm bài lập trình. Hai trang lân cận B08–B09 và D00–D01 được rà lại; câu thu hồi F03/F04 đồng bộ nên rà mạch toàn bài.

Bản đồ ghi chú: N03 (cốt lõi, đặc tả/biểu diễn/ví dụ/thuật toán/chứng minh) ↔ C01–C07; N04 (cốt lõi, tiêu chí và ví dụ ứng dụng) ↔ C05–C16. Tiên quyết N03: tập hợp/vòng lặp; sản phẩm là R và luận điểm đúng. N04 dùng N03 và các bài toán A/B; sản phẩm là phân biệt mười phép đo và điều kiện không bỏ sót. Ghi chú đặt định nghĩa trước ví dụ; slide đặt trực giác/ví dụ trước đặc tả. Cơ chế chỉ mục/LSH không áp dụng chu trình đầy đủ tại đây vì thuộc Bài05–15.

### Hình thêm cho ER-003

| Mã hình | Tệp | Dữ kiện và điều phải nhìn thấy | Nguồn / trang dùng |
|---|---|---|---|
| H20 | danh-gia-jaccard.svg | Hai tập:2chỉS,3chung,3chỉT; giữ giao3/hợp8 | MMDS Ví dụ3.1/Hình3.1; C02 |
| H21 | danh-gia-tinh-dung.svg | Sáu cặp của4tài liệu; ba đã xét, ba chưa xét; không gán cặp đạt ngưỡng | Minh họa bất biến giả mã C04; C06 |
| H22 | danh-gia-bo-nho.svg | Bảng100/400khối, bộ nhớ20ô; hình kho không tỷ lệ diện tích | DSC15:24,28; Bài15; C08 |
| H23 | danh-gia-doc-ghi.svg | Đọc→bộ đệm→ghi→lượt tiếp; không gán số lượt | DSC15:17–23; C09 |
| H24 | danh-gia-truyen-mang.svg | Hai máy đếm cùng từ w cục bộ rồi gửi số đếm; không gán số đếm | MMDS2.2.4–2.2.6; C10 |
| H25 | danh-gia-do-tre.svg | Nhận→chờ→truy cập→tính→trả; độ rộng không phải số đo | Bài07; C11 |
| H26 | danh-gia-xay-dung.svg | Kho→xây→chỉ mục dùng lại cho nhiều truy vấn; không có benchmark | Bài07/Princeton8–9; C12 |
| H27 | danh-gia-cap-nhat.svg | Thay lương tác động bản ghi và chỉ mục; không quy định giao thức giao dịch | DSC14:4,10–11; C13 |
| H28 | danh-gia-luu-tru.svg | Mã+thông tin giải mã cần lưu→khôi phục; không tỷ lệ nén | Nelson–Gailly3,8–9,11; C14 |
| H29 | danh-gia-do-thu-hoi.svg | Tập thật a–e, tập trả c–g; giao3/5; công thức bằng KaTeX | Bài07 ann-recall.svg; C15 |
| H30 | danh-gia-ung-vien.svg | Bộ lọc chọn cặp; nhánh không chọn không được hậu kiểm; không số đo | MMDS3.4; C16 |

Mọi hình mới là SVG ngữ nghĩa có mô tả, không dùng ảnh sinh hay ảnh raster. C01/C07 dùng lại V06. Không tạo hình giả cho đặc tả và giả mã: chúng được dựng bằng HTML/KaTeX.


## Bản triển khai theo kế hoạch ngày 2026-09-06

Tuyến mới: ứng dụng cụ thể → giới hạn cần xử lý → đặc tả và thuộc tính giải thuật → nội dung học phần → sự chuẩn bị của sinh viên → giới hạn suy luận và bài tập. HTML và ghi chú đã theo tuyến này và đạt kiểm định; nhật ký ghi bằng chứng cùng giới hạn công cụ.

Bản ER-001: 45 trang giảng, 120 phút; sáu trang bài tập kể cả trang chuyển phần, 60 phút. Bảy phần ngoài A, B, C, D, E, F, R. P00/P01 mở bài, không đặt ví dụ chưa có ngữ cảnh. Bỏ A08/A09; A01–A07 tự nêu nhiệm vụ, đầu vào–đầu ra và trở ngại bằng hình. E04 vẫn cuối phần giảng. Bản này thay phần A của bản 53 trang; B–R không đổi ở ER-001; ER-002 dưới đây thay phần B.

## Vai trò và kết nối giữa các mạch

*Lịch sử, giữ để đối chiếu: bảng và các câu nối dưới đây ghi cấu trúc trước lượt sửa toàn diện 2026-10-14 (còn mạch E, L01-ET). Cấu trúc bảy mạch hiện hành nằm ở mục "Sửa toàn diện theo chuẩn 2026-10-14".*

| Mạch | Kiến thức đầu vào | Vai trò và sản phẩm | Kết nối vào → ra |
|---|---|---|---|
| A | Tệp, bản ghi, liên kết web; véc-tơ được giải thích là dãy số | P00 là trang tiêu đề mạch 1; P01 liệt kê đánh số bảy mạch và mục tiêu; bảy nhiệm vụ phân biệt đầu vào, đầu ra và khó khăn | Mục tiêu học → thống kê kho web → sắp kết quả và tìm tương đồng → dòng yêu cầu |
| B (mở bằng L01-BT) | Tệp, bản ghi, truy vấn cơ bản | Nhận diện trạng thái dòng, khôi phục và truy cập chọn lọc | Từ tìm kiếm kho tĩnh → danh mục giới hạn cần phân tích trong C |
| C (mở bằng L01-CT) | Tập hợp, vòng lặp, độ phức tạp | Đặc tả cặp gần trùng; xét mọi cặp và đánh giá mười khía cạnh | Từ giới hạn của A/B → ngôn ngữ để đọc bản đồ học phần |
| D (mở bằng L01-DT) | Khung đánh giá của C | Xác định năm mạch, tên phương pháp và lý do học | Từ nhu cầu → nội dung sẽ học → kiến thức phải chuẩn bị |
| E (mở bằng L01-ET) | Bản đồ chương trình, nền tảng cá nhân | Tự nhận diện phần cần ôn; nêu sản phẩm và trách nhiệm học tập | Từ danh mục thuật toán → cách học và kiểm chứng kết luận |
| F (mở bằng L01-FT) | Tổ hợp, xác suất độc lập, tuyến tính kỳ vọng | Phân biệt đúng theo mô hình với suy luận có căn cứ; áp lại khung chọn giải thuật | Từ trách nhiệm dữ liệu → bài tập kiểm tra mô hình |
| R (mở bằng L01-RT) | F02–F03, gợi ý công thức và dữ kiện nguồn | Giải các biến thể và giải thích giới hạn của phép tìm mẫu trùng | Dùng mô hình đã có → sản phẩm có thể chấm |

Câu nối giữa các mạch được thể hiện cả trên trang mở phần và trong lời giảng:

- A→B: “Kho web còn sinh dòng truy vấn, cần lưu trữ và phục vụ nhiều loại tra cứu. Mỗi công việc đặt thêm một giới hạn.”
- B→C: “Các ví dụ vừa gặp yêu cầu khác nhau về bộ nhớ, thời gian truy cập và kết quả. Ta dùng tìm cặp tài liệu gần trùng để phân tích đặc tả, tính đúng và chi phí, rồi đối chiếu các tiêu chí trên nhiều ứng dụng.”
- C→D: “Khung đặc tả và chi phí giúp xác định vai trò của từng phương pháp trong học phần.”
- D→E: “Mỗi mạch dùng một phần kiến thức nền khác nhau. Sinh viên cần biết phần nào đã có và phần nào phải ôn trước khi học.”
- E→F: “Một chương trình chạy đúng vẫn có thể dẫn đến kết luận sai nếu giả thiết về dữ liệu không phù hợp.”
- F→R: “Các bài tập tiếp theo thay đổi quy mô và tiêu chuẩn trùng để kiểm tra chính mô hình vừa dùng.”

## Bản đồ từng trang

Mã V trỏ tới danh mục hình bên dưới, đồng thời cung cấp nguồn và dữ kiện. Thời lượng gồm câu kiểm tra, chuyển ý và thời gian quan sát hình; không hiển thị trên trang chiếu. Tên thuật toán chuyên biệt chỉ được giới thiệu có hệ thống từ mạch D.

| Mã trang | Tiêu đề trang chiếu | Luận điểm, hoạt động và sản phẩm | Nguồn/hình | Phút | Nối sang trang sau |
|---|---|---|---|---:|---|
| L01-P00 | Bài toán dữ liệu lớn và mô hình thuật toán | Nhận diện bài, học phần và học kỳ | source.md | 1 | Nội dung buổi học |
| L01-P01 | Nội dung buổi học | Danh sách đánh số bảy mạch, trùng tên trang tiêu đề mạch; ba mục tiêu quan sát được (ngoại lệ tạm thời: vượt trần 80 âm tiết, tách ở đợt sau) | source.md | 2 | Nhiệm vụ thống kê kho web |
| L01-A01 | Tính tổng kích thước trang web theo máy chủ | Bốn bản ghi → tổng 55/25/0; hình tệp vượt bộ nhớ; phân biệt kích thước trang và lưu lượng | V01; bảng HTML minh họa đầu ra | 3 | Kho có thể chia trên nhiều máy |
| L01-A02 | Đếm số lần xuất hiện của từng từ | Cùng từ ở nhiều phần kho → tổng toàn kho; gom dữ liệu qua mạng gây nút thắt, lỗi máy cần tránh đếm trùng | V02 | 3 | Kho tìm kiếm còn cần sắp kết quả |
| L01-A03 | Tính điểm quan trọng của trang web | Trang và liên kết → điểm hỗ trợ sắp kết quả; phụ thuộc điểm buộc đọc/cập nhật nhiều vòng | V03 | 3 | Điểm chung chưa phân biệt chủ đề |
| L01-A04 | Ưu tiên kết quả tìm kiếm theo chủ đề | Jaguar + chủ đề ô tô → ưu tiên trang về xe; điểm riêng cho mỗi người tốn lưu trữ | V04 | 3 | Điểm liên kết có thể bị thao túng |
| L01-A05 | Hạn chế liên kết rác trong xếp hạng | Cụm cùng bên kiểm soát đẩy điểm t; cần hạn chế ảnh hưởng lên kết quả | V05 | 3 | Kết quả tìm kiếm còn có bản sao |
| L01-A06 | Tìm các cặp tài liệu gần trùng | Nội dung chung và phần sửa; một triệu tài liệu sinh $499\,999\,500\,000$ cặp cần xét nếu so tất cả | V06 | 3 | Đổi từ mọi cặp sang một truy vấn |
| L01-A07 | Tìm đoạn tài liệu bằng véc-tơ truy vấn | Truy vấn và đoạn tài liệu mã hóa cùng cách → k đoạn gần theo khoảng cách; mỗi truy vấn quét lại kho lớn | V07 | 2 | Truy vấn đến nối tiếp tạo dòng |
| L01-BT | Dòng dữ liệu, nén và truy vấn trên đĩa | Trang tiêu đề mạch 2: tên mạch, dòng dẫn nêu nhu cầu, từ khóa; notes nêu kết quả kế thừa, nhiệm vụ và kết quả giao | AGENTS.md "Trang tiêu đề mạch" | 0,5 | Xử lý dòng dữ liệu, lưu trữ và truy vấn |
| L01-B00 | Xử lý dòng dữ liệu, lưu trữ và truy vấn | Giới thiệu ba nhóm: dòng, nén, xử lý và truy vấn trên đĩa; mỗi nhóm gắn đầu ra và giới hạn | V07–V09; MMDS4.1 | 0,5 | Dòng truy vấn và dòng thư có nhiệm vụ khác nhau |
| L01-B01 | Giữ mẫu truy vấn và lọc thư đến | Lưu hết lịch sử tốn bộ nhớ. Tra danh sách lớn trên đĩa cho từng thư làm tăng thời gian xử lý. | V08 | 3 | Đếm người dùng và lượt truy cập |
| L01-B02 | Đếm người dùng và lượt truy cập gần đây | Đếm người dùng cần nhận ra lần quay lại. Thống kê gần đây phải bỏ ảnh hưởng của bản ghi hết hạn mà vẫn cập nhật kịp. | V09 | 3 | Dữ liệu cần giữ lại còn chiếm dung lượng |
| L01-B10 | Nén dữ liệu để lưu và khôi phục | Một số đếm không khôi phục dữ liệu; nén văn bản và ảnh có yêu cầu khác nhau | V09–V11; MMDS4; Nelson–Gailly3,11 | 1 | Nén văn bản khôi phục nguyên vẹn |
| L01-B03 | Lưu văn bản với ít dung lượng hơn | Lược bỏ tùy ý làm mất văn bản gốc. Mã và thông tin phụ trợ phải đủ để giải mã, nhưng cũng chiếm dung lượng. | V10 | 2 | Dữ liệu ảnh có thể có đặc tả khác |
| L01-B04 | Giảm dung lượng ảnh với sai số cho phép | Gộp các giá trị điểm ảnh làm mất chi tiết. Cần kiểm cả dung lượng mã và sai khác của ảnh khôi phục. | V11 | 2 | Dữ liệu đã lưu vẫn cần tổ chức để xử lý |
| L01-B11 | Xử lý và truy vấn dữ liệu trên đĩa | Định nghĩa khối đọc ghi và phần tệp vừa bộ nhớ; phân biệt sắp, tra, nối | V11–V16; DSC15 | 1 | Tệp đầu vào và đầu ra của phép sắp |
| L01-B05 | Sắp xếp tệp lớn theo khóa | Không thể nạp trọn tệp để sắp như một mảng trong bộ nhớ. Đọc và ghi lại nhiều lần làm tăng chi phí dù số so sánh ít. | V12 | 3 | Tệp có thứ tự hỗ trợ truy cập chọn lọc |
| L01-B06 | Tìm hồ sơ giảng viên theo mã hoặc lương | Quét cả bảng cho mỗi yêu cầu đọc nhiều dữ liệu thừa. Nếu dùng chỉ mục, phải cập nhật nó khi mã hoặc lương thay đổi. | V13 | 2 | Từ khóa cần một cách ánh xạ khác |
| L01-B07 | Tìm tài liệu chứa đồng thời hai từ khóa | Đọc từng tài liệu cho mỗi truy vấn lặp lại công việc trên cả kho. Cần tìm được nơi xuất hiện của từng từ mà không quét lại hết. | V14 | 2 | Vùng không gian không phải danh sách từ |
| L01-B08 | Tìm đối tượng giao vùng trên bản đồ | Kiểm mọi hình trên bản đồ tốn công. Lọc theo hộp bao giảm ứng viên, nhưng hộp bao giao vùng chưa đủ kết luận về hình thật. | V15 | 2 | Truy vấn cũng có thể kết hợp hai bảng |
| L01-B09 | Ghép sinh viên với các môn đã đăng ký | Hai bảng chiếm 100 và 400 khối; bộ nhớ chỉ có 20 khối. Quét bảng đăng ký lại cho từng sinh viên sẽ đọc cùng dữ liệu nhiều lần. | V16 | 2 | Gom các giới hạn thành khung phân tích |
| L01-CT | Đặc tả và đánh giá thuật toán | Trang tiêu đề mạch 3: tên mạch, dòng dẫn nêu nhu cầu, từ khóa; notes nêu kết quả kế thừa, nhiệm vụ và kết quả giao | AGENTS.md "Trang tiêu đề mạch" | 0,5 | Phân tích thuật toán xử lý dữ liệu lớn |
| L01-C00 | Phân tích thuật toán xử lý dữ liệu lớn | Phân biệt đặc tả và đánh giá; gọi đúng bài toán dùng xuyên suốt | MMDS3 tr.73–75; BHK1 | 0,5 | Tìm cặp gần trùng trên kho web |
| L01-C01 | Bài toán tìm cặp tài liệu gần trùng | Phân biệt bản sao khác tên máy chủ/liên kết với giống hệt từng ký tự; độ đo/ngưỡng chốt đầu ra | V06; MMDS3.1.2; Stanford03-lsh14 | 2 | Biểu diễn để tính tương đồng |
| L01-C02 | Độ tương đồng của hai tài liệu | Tập đoạn ký tự; giao3/hợp8; kết luận đạt ngưỡng khi τ≤3/8 | MMDS Ví dụ3.1/Hình3.1; H20 | 2 | Đặc tả toàn bộ tập kết quả |
| L01-C03 | Đặc tả tìm cặp gần trùng | Miền hữu hạn, tập không rỗng, ngưỡng; đúng/đủ/mỗi cặp một lần, biên N<2 | MMDS3.1–3.4 | 3 | Thuật toán thực hiện đặc tả |
| L01-C04 | Thuật toán xét mọi cặp | Hai vòng i<j; chạy N2 trên S,T cho một cặp với hai nhánh theo τ≤3/8; kiểm lỗi bắt đầu j=1 | MMDS3 tr.73; Bài05 | 3 | Khung đánh giá lời giải |
| L01-C05 | Các tiêu chí đánh giá | Tổng quan10tiêu chí thành3nhóm kết quả/tài nguyên/vận hành | MMDS1.3.4,2.5,3.4; DSC14–15; Bài07 | 1 | Tính đúng theo đặc tả |
| L01-C06 | Tính đúng của thuật toán | Bất biến trên phần cặp đã xét, khởi tạo/duy trì/kết thúc; đúng và đủ | C03–C04; H21 | 2 | Tính đúng chưa xác định chi phí |
| L01-C07 | Khối lượng tính toán | Số cặp×chi phí một cặp; N=1triệu; danh sách≤L cho O(N²L); tách chi phí chuẩn bị/đầu ra | V06; Bài05 | 2 | Dữ liệu phải giữ đồng thời |
| L01-C08 | Bộ nhớ làm việc | Bộ nhớ làm việc khác đầu vào; nối bảng100/400khối trong20khối, tính cả bộ đệm | DSC15:24,28; Bài15; H22 | 2 | Chia phần có thể đọc lại |
| L01-C09 | Đọc ghi và số lượt quét | Khối chuyển đĩa–RAM và lượt quét; sắp ngoài phải đọc/ghi lại | DSC15:17–23; H23 | 2 | Chuyển dữ liệu giữa máy |
| L01-C10 | Dữ liệu truyền qua mạng | Đếm từ tại chỗ, gửi đóng góp, tránh tính trùng; lượng mạng khác thời gian chờ | MMDS2.2.4–2.2.6,2.5; H24 | 2 | Độ trễ một yêu cầu |
| L01-C11 | Độ trễ truy vấn | Nhận truy vấn véc-tơ→chờ/truy cập/tính/trả; khác thông lượng; không số đo giả | Bài07; H25 | 2 | Chỉ mục cần được tạo trước |
| L01-C12 | Chi phí xây dựng chỉ mục | Kho→xây→chỉ mục→nhiều truy vấn; thời gian và bộ nhớ đỉnh | Bài07/Princeton8–9; H26 | 1 | Dữ liệu đổi sau khi xây |
| L01-C13 | Chi phí cập nhật dữ liệu | Sửa lương phải sửa bản ghi/chỉ mục; giữ tính nhất quán sau cập nhật | DSC14:4,10–11; H27 | 1 | Cấu trúc phụ còn chiếm chỗ |
| L01-C14 | Dung lượng lưu trữ | Mã văn bản và thông tin giải mã cần lưu; khôi phục đúng, khác RAM | Nelson–Gailly3,8–9,11; H28 | 1 | Khi cho phép gần đúng cần đo chất lượng |
| L01-C15 | Chất lượng kết quả gần đúng | Hai tập5phần tử giao3; recall@5=3/5; chuẩn đúng, phá hòa và điều kiện đo | Bài07 mục1; H29 | 2 | Bỏ sót cặp tài liệu cũng không sửa bằng hậu kiểm |
| L01-C16 | Giảm ứng viên và nguy cơ bỏ sót | Ứng viên→kiểm chính xác; trả đúng từng cặp chưa bảo đảm đủ; câu kiểm tra | MMDS3.4; H30 | 2 | Yêu cầu xác định nhóm phương pháp D |
| L01-DT | Năm nhóm thuật toán của học phần | Trang tiêu đề mạch 4: tên mạch, dòng dẫn nêu nhu cầu, từ khóa; notes nêu kết quả kế thừa, nhiệm vụ và kết quả giao | AGENTS.md "Trang tiêu đề mạch" | 0,5 | Nội dung học phần và các nhóm thuật toán |
| L01-D00 | Nội dung học phần và các nhóm thuật toán | Nhu cầu đã phân tích → chương trình và năng lực; ý tưởng và ví dụ đã gặp, không giảng trước cơ chế đầy đủ | Đề cương; nguồn cụ thể trong notes; SVG cùng bài | 0,5 | chương trình và năng lực |
| L01-D01 | Học phần và năng lực cần đạt | Bốn năng lực → năm nhóm bài; ý tưởng và ví dụ đã gặp, không giảng trước cơ chế đầy đủ | Đề cương; nguồn cụ thể trong notes; SVG cùng bài | 1 | năm nhóm bài |
| L01-D02 | Năm nhóm bài của học phần | Bản đồ → đếm từ phân tán; ý tưởng và ví dụ đã gặp, không giảng trước cơ chế đầy đủ | Đề cương; nguồn cụ thể trong notes; SVG cùng bài | 1 | đếm từ phân tán |
| L01-D03 | MapReduce: gom kết quả theo khóa | Gom một lượt → tính lặp trên đồ thị; ý tưởng và ví dụ đã gặp, không giảng trước cơ chế đầy đủ | Đề cương; nguồn cụ thể trong notes; SVG cùng bài | 2 | tính lặp trên đồ thị |
| L01-D08 | PageRank: tính điểm theo liên kết | Điểm theo liên kết → tương đồng nội dung; ý tưởng và ví dụ đã gặp, không giảng trước cơ chế đầy đủ | Đề cương; nguồn cụ thể trong notes; SVG cùng bài | 2 | tương đồng nội dung |
| L01-D04 | MinHash và LSH: chọn cặp cần đối chiếu | Cặp tập hợp → một truy vấn véc-tơ; ý tưởng và ví dụ đã gặp, không giảng trước cơ chế đầy đủ | Đề cương; nguồn cụ thể trong notes; SVG cùng bài | 2 | một truy vấn véc-tơ |
| L01-D09 | Chỉ mục cho truy vấn véc-tơ | Kho lập chỉ mục → cập nhật dòng; ý tưởng và ví dụ đã gặp, không giảng trước cơ chế đầy đủ | Đề cương; nguồn cụ thể trong notes; SVG cùng bài | 1 | cập nhật dòng |
| L01-D05 | Lấy mẫu và lọc trên dòng dữ liệu | Mẫu/phép thuộc → thống kê; ý tưởng và ví dụ đã gặp, không giảng trước cơ chế đầy đủ | Đề cương; nguồn cụ thể trong notes; SVG cùng bài | 1 | thống kê |
| L01-D10 | Cấu trúc gọn cho thống kê dòng | Tóm tắt truy vấn → khôi phục dữ liệu; ý tưởng và ví dụ đã gặp, không giảng trước cơ chế đầy đủ | Đề cương; nguồn cụ thể trong notes; SVG cùng bài | 2 | khôi phục dữ liệu |
| L01-D06 | Nén theo ký hiệu, mẫu lặp và ảnh | Dung lượng mã → truy cập dữ liệu đã lưu; ý tưởng và ví dụ đã gặp, không giảng trước cơ chế đầy đủ | Đề cương; nguồn cụ thể trong notes; SVG cùng bài | 2 | truy cập dữ liệu đã lưu |
| L01-D07 | Tổ chức dữ liệu để giảm đọc ghi | Các phương pháp → kiến thức và cách học; ý tưởng và ví dụ đã gặp, không giảng trước cơ chế đầy đủ | Đề cương; nguồn cụ thể trong notes; SVG cùng bài | 2 | kiến thức và cách học |
| L01-ET | Chuẩn bị và cách học | Trang tiêu đề mạch 5: tên mạch, dòng dẫn nêu nhu cầu, từ khóa; notes nêu kết quả kế thừa, nhiệm vụ và kết quả giao | AGENTS.md "Trang tiêu đề mạch" | 0,5 | Kiến thức, kỹ năng và cách học |
| L01-E00 | Kiến thức, kỹ năng và cách học | Xác định ba nội dung chuẩn bị: kiến thức, kỹ năng và cách học | CLO1–CLO4; MMDS Ví dụ3.1; Bài07 | 0,5 | nền cần ôn |
| L01-E01 | Kiến thức nền dùng ở từng nhóm bài | Gắn mỗi phần kiến thức nền với một công việc trong nhóm bài | CLO1–CLO4; MMDS Ví dụ3.1; Bài07 | 2 | vận dụng tập hợp |
| L01-E05 | Tập hợp, Jaccard và điều kiện chọn | Tính giao/hợp và giải điều kiện ngưỡng của cặp Jaccard3/8 | CLO1–CLO4; MMDS Ví dụ3.1; Bài07 | 1 | sản phẩm thuật toán |
| L01-E02 | Sản phẩm khi phân tích thuật toán | Phân biệt đặc tả, vết chạy, chứng minh và kiểm thử | CLO1–CLO4; MMDS Ví dụ3.1; Bài07 | 2 | đo kết quả |
| L01-E06 | Báo cáo chất lượng và hiệu năng | Đọc độ thu hồi3/5 và nêu điều kiện so hiệu năng | CLO1–CLO4; MMDS Ví dụ3.1; Bài07 | 1 | báo cáo có trách nhiệm |
| L01-E03 | Tự học, hợp tác và trách nhiệm dữ liệu | Nêu hành vi tự học/hợp tác và giới hạn suy luận từ độ tương đồng | CLO1–CLO4; MMDS Ví dụ3.1; Bài07 | 2 | mô hình ngẫu nhiên và suy luận |
| L01-FT | Mẫu trùng ngẫu nhiên và suy luận | Trang tiêu đề mạch 6: tên mạch, dòng dẫn nêu nhu cầu, từ khóa; notes nêu kết quả kế thừa, nhiệm vụ và kết quả giao | AGENTS.md "Trang tiêu đề mạch" | 0,5 | Mô hình ngẫu nhiên và giới hạn suy luận |
| L01-F00 | Mô hình ngẫu nhiên và giới hạn suy luận | Trách nhiệm dữ liệu → bài toán lưu trú; giải thích và tính theo mô hình nguồn | MMDS1.2.1–1.2.3 tr.6–8; hình lưu trú | 0,5 | bài toán lưu trú |
| L01-F01 | Tìm mẫu trùng trong hồ sơ lưu trú | Mẫu trùng → cách dữ liệu phát sinh; giải thích và tính theo mô hình nguồn | MMDS1.2.1–1.2.3 tr.6–8; hình lưu trú | 1 | cách dữ liệu phát sinh |
| L01-F02 | Mô hình lưu trú không phối hợp | Giả thiết → xác suất một và hai ngày; giải thích và tính theo mô hình nguồn | MMDS1.2.1–1.2.3 tr.6–8; hình lưu trú | 2 | xác suất một và hai ngày |
| L01-F05 | Xác suất trùng một ngày và hai ngày | Xác suất một phép thử → số phép thử; giải thích và tính theo mô hình nguồn | MMDS1.2.1–1.2.3 tr.6–8; hình lưu trú | 2 | số phép thử |
| L01-F06 | Đơn vị đếm và số phép thử | Đơn vị cặp người–cặp ngày → biến đếm X; giải thích và tính theo mô hình nguồn | MMDS1.2.1–1.2.3 tr.6–8; hình lưu trú | 2 | biến đếm X |
| L01-F03 | Kỳ vọng số biến cố trùng | Kỳ vọng nền → giới hạn diễn giải; giải thích và tính theo mô hình nguồn | MMDS1.2.1–1.2.3 tr.6–8; hình lưu trú | 3 | giới hạn diễn giải |
| L01-F07 | Mẫu trùng và căn cứ suy luận | Giới hạn suy luận → thu hồi bài toán gần trùng; giải thích và tính theo mô hình nguồn | MMDS1.2.1–1.2.3 tr.6–8; hình lưu trú | 3 | thu hồi bài toán gần trùng |
| L01-F04 | Đặc tả, chi phí và giới hạn kết luận | Khung toàn bài → chuẩn bị MapReduce; giải thích và tính theo mô hình nguồn | MMDS1.2.1–1.2.3 tr.6–8; hình lưu trú | 1 | chuẩn bị MapReduce |
| L01-E04 | Chuẩn bị cho Bài 02: MapReduce | Chuẩn bị bài sau → bài tập mô hình lưu trú; giải thích và tính theo mô hình nguồn | MMDS2.2; hình đếm từ | 1 | bài tập mô hình lưu trú |
| L01-RT | Bài tập vận dụng | Trang tiêu đề mạch 7: tên mạch, dòng dẫn nêu nhu cầu, từ khóa; notes nêu kết quả kế thừa, nhiệm vụ và kết quả giao | AGENTS.md "Trang tiêu đề mạch" | 0,5 | Bài tập về phép đếm và suy luận |
| L01-R00 | Bài tập về phép đếm và suy luận | Nhận diện hai bài tập và bốn thành phần của lời giải | MMDS1.2.4 tr.8 | 2,5 | hai bài tập nguồn |
| L01-R01 | Ba biến thể của bài toán lưu trú | Lập bảng tham số thay đổi riêng cho từng biến thể | MMDS Bài1.2.1(a–c) tr.8 | 7 | thay riêng từng điều kiện |
| L01-R02 | Ảnh hưởng của số ngày và số người | Tính kỳ vọng và tỷ lệ thay đổi ở hai biến thể quy mô | MMDS Bài 1.2.1(a,b), tr. 8 | 15 | thay tiêu chuẩn trùng |
| L01-R03 | Mẫu lưu trú trùng trong ba ngày | Đổi đơn vị đếm sang bộ ba ngày và tính kỳ vọng | MMDS Bài 1.2.1(c), tr. 8; mô hình 1.2.3, tr. 7 | 10 | cặp lượt mua |
| L01-R04 | Tìm cặp người mua cùng tập mặt hàng | Xác định dữ kiện, giả thuyết nguồn và đầu ra cần tìm | MMDS Bài1.2.2 và chú thích3 tr.8 | 8 | đơn vị người/lượt/tập |
| L01-R06 | Đơn vị đếm trong bài toán giỏ hàng | Phân biệt người, lượt mua, tập mặt hàng và mô hình nền | MMDS Bài1.2.2 và chú thích3 tr.8 | 5 | lời giải và diễn giải |
| L01-R05 | Lời giải và giới hạn kết luận | Hoàn thiện phép đếm, xác suất, kỳ vọng và kết luận có điều kiện | MMDS Bài1.2.2 và chú thích3 tr.8 | 12 | trả lời có điều kiện |

## Chu trình học tập và phạm vi rút gọn

| Cụm | Tình huống → vấn đề → trực giác | Ví dụ → hình thức → cơ chế/lập luận | Chi phí, kiểm tra và lý do gộp |
|---|---|---|---|
| Cặp gần trùng, cốt lõi | A06/C01 đặt bài toán; C02 tập đoạn và trực giác giao–hợp | C02 chạy Ví dụ3.1; C03 đặc tả; C04 giả mã; C06 chứng minh | C05 tổng quan để định vị chứng minh; C07 chi phí; C16 kiểm tra hậu kiểm. Bài01 không giảng cơ chế LSH; đủ chu trình cho thuật toán xét mọi cặp |
| V02–V16, khảo sát ứng dụng | A02–B09 mỗi trang có đầu vào, đầu ra, cách trực tiếp và giới hạn; hình gợi một hướng xử lý | Không chạy giả mã hay chứng minh chuyên biệt trong Bài 01; D03–D07 định vị nơi sẽ học | C05–C16 nêu phép đo và bảo đảm; F04 kiểm tra lựa chọn. Chu trình rút gọn vì mục tiêu là nhận diện nhu cầu, không làm chủ thuật toán bài sau |
| V17, mô hình xác suất | F00 mở phần; F01 đặt bài toán và mẫu lưu trú; F02 nêu mô hình nền | F05 tính một/hai ngày; F06 xác định đơn vị và số phép thử; F03 định nghĩa X, kỳ vọng và thay số | F07 giới hạn suy luận; R01–R03 thay quy mô. Thuật toán/chi phí triển khai không áp dụng vì đây là phép đếm mô hình, không thuật toán phát hiện người |
| V18, bài tập nguồn | R04 giữ đề và giả thuyết; R06 đối chiếu cặp ngày với cặp lượt mua | Người học dựng mô hình; R05 hoàn tất phép đếm, xác suất, kỳ vọng và kết luận; N09 có lời giải gập | Giữ câu hỏi MMDS1.2.2/chú thích3, không biến thành bài mới hoặc thuật toán nhận diện người; R00–R05/R06 tổng60phút |
| D/E, giới thiệu khóa học | D00 và E00 mở rõ nội dung; dùng lại bài toán A/B và khung C | D03/D08/D04/D09/D05/D10/D06/D07 giải thích ý tưởng đại diện; E05/E02/E06 vận dụng tập hợp, vết chạy và độ thu hồi | Nhận diện vai trò phương pháp và sản phẩm học; không dạy trước giả mã/chứng minh bài sau. E03 nối trách nhiệm sang F |

Câu kiểm tra trên mặt trang dùng nhãn “Câu hỏi:”. Mã trang, V/H và nhãn quy trình chỉ ở tệp kế hoạch. Chi tiết thời lượng nằm ở storyboard và hướng dẫn tổ chức; lời giảng không đọc các mã nội bộ.

## Đặc tả hình cho mọi ví dụ

Toàn bộ 19 tệp dưới đây đã được dựng trong 2627-1/img/lec-01/. V01/V17/H19 thay hình cùng tên; 16 tệp còn lại được thêm mới. Các tài sản bài khác chỉ làm nguồn tham khảo, không sửa. Hai SVG cũ về giao thoa lĩnh vực và thể tích gần biên được giữ nhưng không còn dùng trong tuyến mới. Bản đồ H19 dùng chung với index nên phải kiểm định cả hai nơi.

Bố cục ER-001 phần A: câu nêu bài toán, hình đối tượng/đầu ra/trở ngại, thẻ khó khăn; A01 ghép bảng HTML với hình bộ nhớ. ER-002 áp dụng cùng nguyên tắc cho B; C–R giữ nguyên. Hình định tính là sơ đồ, không phải kết quả đo. SVG có role, title/desc, nhãn tiếng Việt và nét/hình hỗ trợ màu; bảng, công thức, giả mã bằng HTML/KaTeX.

| Ví dụ / hình | Tệp dự kiến | Dữ liệu, bố cục và quan hệ phải giữ | Kết luận hình và văn bản thay thế dự kiến | Nguồn / tài sản tham khảo | Chỗ dùng lại |
|---|---|---|---|---|---|
| V01 / H01 | kho-nhat-ky-bo-nho.svg | Tệp trên đĩa không vừa bộ nhớ; mũi tên nạp toàn bộ bị chặn. SVG 600×360 để đọc trong cột. Bảng HTML gồm bốn bản ghi minh họa đầu ra, tổng 55/25/0; không vẽ bảng trong SVG | Tệp lớn buộc đổi cách đọc và trạng thái giữ lại | Stanford intro62; MMDS1.3.4 tr13 | A01, E02 |
| V02 / H02 | ung-dung-tong-hop-phan-tan.svg | Từ w ở hai phần kho; gom toàn bộ tài liệu qua mạng về một máy để đếm. Không gán số đếm | Mạng và một máy nhận trở thành nút thắt; phần chữ nêu lỗi chạy lại | MMDS Ch2 slide8–13,20; sách2.1–2.2.6 | A02, C10, D03 |
| V03 / H03 | ung-dung-xep-hang-web.svg | Giữ y→y,a; a→y,m; m→a. Hộp là trang, đầu ra điểm từng trang hỗ trợ sắp kết quả; dải đọc/cập nhật/lặp | Điểm phụ thuộc nhau, chi phí phát sinh nhiều vòng; không gán điểm/thứ hạng | MMDS5.1–5.2; Link Analysis1:18–21,48,53 | A03, D03 |
| V04 / H04 | ung-dung-truy-van-theo-chu-de.svg | Jaguar có bốn nghĩa; chủ đề ô tô đã biết dẫn tới mục tiêu ưu tiên trang về xe | Một từ chưa chốt đầu ra; thẻ khó khăn nêu chi phí bộ điểm riêng theo người | MMDS5.3.1 tr195–196 | A04, D03 |
| V05 / H05 | ung-dung-lien-ket-thao-tung.svg | Giữ ba nhóm Hình5.16; khoanh nét đứt t và trang hỗ trợ cùng bên kiểm soát; nhóm có thể tác động→t; t↔mỗi hỗ trợ | Nhiều liên kết cùng bên tạo có thể đẩy điểm; cần hạn chế ảnh hưởng | MMDS5.4.1–5.4.4/Hình5.16 | A05, D03, F01 |
| V06 / H06 | ung-dung-tai-lieu-gan-trung.svg | Hai tài liệu có phần chung/phần sửa; bốn biểu tượng nối đủ sáu cặp không hướng; công thức bằng KaTeX. Bỏ chuỗi chữ ký chưa định nghĩa | Đầu ra là cặp; xét tất cả tăng theo số cặp. Nét minh họa định tính, không đo tương đồng | MMDS3.1–3.4; Stanford03-lsh14 | A06, C01/C07/C16, D04, F04 |
| V07 / H07 | ung-dung-truy-hoi-vec-to.svg | Truy vấn dạng véc-tơ được so với các đoạn tài liệu đã mã hóa; đầu ra k đoạn gần. Bỏ chỉ mục/độ thu hồi khỏi hình | Mỗi truy vấn quét lại kho, tính nhiều khoảng cách; không gán tọa độ hay kết quả giả | BIODS271 PDF16–18; Princeton08:2–5 | A07, C11/C12/C15, D04 |
| V08 / H08 | ung-dung-dong-truy-van.svg | Hai nhiệm vụ tách biệt: nhật ký truy vấn tạo mẫu theo người dùng; thư đến được kiểm địa chỉ theo danh sách cho phép. | Minh họa định tính yêu cầu bài toán; không gán kết quả hoặc số đo mới | MMDS 4.1–4.3; Streams 1 slide 6; lec-08/stream-model.svg, bloom-pipeline.svg | B01, D05 |
| V09 / H09 | ung-dung-thong-ke-cua-so.svg | Trục thời gian tách các lượt truy cập quá cũ khỏi cửa sổ gần đây; đếm người dùng khác nhau phân biệt với đếm lượt. | Minh họa định tính yêu cầu bài toán; không gán kết quả hoặc số đo mới | MMDS 4.4–4.7, Hình 4.2–4.4; UMass Count-Min; lec-09/decision-map.svg | B02, D05 |
| V10 / H10 | ung-dung-nen-van-ban.svg | Văn bản gốc được lưu thành dữ liệu mã và thông tin giải mã; đầu ra phải khôi phục nguyên vẹn chuỗi. | Minh họa định tính yêu cầu bài toán; không gán kết quả hoặc số đo mới | Nelson–Gailly Ch3/9; CMU LZ logic11–14; Bài11 Z00; lec-11/two-contracts.svg | B03, C14, D06 |
| V11 / H11 | ung-dung-nen-anh.svg | Các mức sáng gần nhau được gộp về mức đại diện; chi tiết mức sáng bị mất nên ảnh khôi phục có thể khác ảnh gốc. | Minh họa định tính yêu cầu bài toán; không gán kết quả hoặc số đo mới | Nelson–Gailly Ch11; CMU lossy logic2–16; lec-11/two-contracts.svg; Bài11 J00–J06 | B04, C14, D06 |
| V12 / H12 | ung-dung-sap-xep-ngoai.svg | Các bản ghi được đổi từ thứ tự bất kỳ sang khóa tăng dần; tệp đầu vào lớn không thể nạp trọn vào bộ nhớ. | Minh họa định tính yêu cầu bài toán; không gán kết quả hoặc số đo mới | DSC Ch15 slide 17–23; lec-12/external-sort.svg, kway-merge.svg | B05, C09, D07 |
| V13 / H13 | ung-dung-tra-cuu-khoa.svg | Hai yêu cầu: tìm theo một mã và tìm lương trong đoạn kín; đầu ra là hồ sơ thỏa điều kiện, không phải toàn bảng. | Minh họa định tính yêu cầu bài toán; không gán kết quả hoặc số đo mới | DSC Ch14 slide 3–16; Bài13 mở bài; sơ đồ hóa đặc tả truy vấn | B06, C13, D07 |
| V14 / H14 | ung-dung-tim-tu-khoa.svg | Hai từ khóa phải cùng có mặt trong mỗi tài liệu kết quả; tài liệu chỉ chứa một từ không thỏa điều kiện. | Minh họa định tính yêu cầu bài toán; không gán kết quả hoặc số đo mới | DSC Ch31 tr.13–16, slide 14–16; lec-14/text-index.svg, inverted-disk.svg | B07, D07 |
| V15 / H15 | ung-dung-truy-van-khong-gian.svg | Vùng cần tìm Q giao hộp bao A và B của hai nhóm đối tượng; phải kiểm đối tượng trong cả hai nhóm trước khi trả kết quả. | Minh họa định tính yêu cầu bài toán; không gán kết quả hoặc số đo mới | DSC Ch24 slide 17, 21–24; Auburn PDF 10–13; lec-14/rtree.svg, filter-refine.svg | B08, D07 |
| V16 / H16 | ung-dung-noi-bang.svg | Hồ sơ sinh viên và lượt đăng ký được ghép bằng mã sinh viên; một sinh viên có thể tạo nhiều kết quả ứng với nhiều lượt đăng ký. | Minh họa định tính yêu cầu bài toán; không gán kết quả hoặc số đo mới | DSC Ch15 slide 24, 28, 40; lec-15/join-usecase.svg | B09, C08, D07 |
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

Phần F gồm 3 phút về giả thiết và trách nhiệm, 9 phút dựng mô hình xác suất và kỳ vọng, 2 phút kết luận và 2 phút chuẩn bị MapReduce. Recitation giữ nguyên yêu cầu toán học, chỉ dịch và chia bước như bản trước. Vì phần lý thuyết xác suất giảm, R01 dành phần đầu để dựng lại mô hình; gợi ý phân tầng gồm bảng ký hiệu, số phép thử, xác suất một phép thử. R04 có sơ đồ đơn vị người/lượt/tập để tránh nhầm. Hai bài này đo mô hình hóa và diễn giải; các mục tiêu về tài nguyên và bản đồ khóa học được kiểm tra ở C06, C08, E01 và F04, không tuyên bố recitation đánh giá đủ mọi mục tiêu.

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
| L01-N03 | cốt lõi: biểu diễn, Jaccard, đặc tả R, chạy hai tập, giả mã và chứng minh xét mọi cặp | C01–C07 | Cặp gần trùng → lời giải đúng/đủ → chi phí |
| L01-N04 | cốt lõi: mười khía cạnh đánh giá, ví dụ ứng dụng và điều kiện hậu kiểm | C05–C16 | Lời giải → phép đo/bảo đảm → nhóm phương pháp |
| L01-N05 | cốt lõi: bản đồ học phần và thuật ngữ theo vai trò | D00–D07 | Tiêu chí → nhóm phương pháp |
| L01-N06 | cốt lõi: tiên quyết, kỹ năng và hành vi học tập | E01–E03; E04 ở cuối F | Nhóm phương pháp → kiến thức/kỹ năng/trách nhiệm → chuẩn bị bài tiếp theo |
| L01-N07 | cầu nối: giả thiết, kỳ vọng và giới hạn suy luận | F01–F03 | Trách nhiệm → mô hình kiểm chứng |
| L01-N08 | cốt lõi: tự kiểm và hai bài tập có gợi ý/lời giải | F04, R01–R05 | Mô hình → sản phẩm có thể kiểm tra |

Ánh xạ này đã được áp dụng cho ghi chú. Những chủ đề đọc thêm chỉ được định tuyến ở cuối, không tạo mã mới trong tuyến chính.

## Điều kiện kiểm định khi triển khai

Kế hoạch được chốt khi đủ 14 bài, 18 ví dụ có đặc tả hình, mỗi trang có vai trò/nguồn/câu nối, thời lượng $23+24+31+17+9+16=120$ và $10+15+10+10+15=60$. Kiểm tra số trang 54+6=60, bảy phần ngoài, các mã duy nhất. R00 được tính trong 60 trang nhưng chỉ chuyển phần, không tính vào 60 phút làm bài của R01–R05.

Rà lại toàn bộ bài vì mở bài và luận điểm đã đổi. Kiểm thử RevealJS/ghi chú/SVG ở 1280×720, màn hình hẹp, bàn phím và bản in; nguồn, hình, KaTeX và tài nguyên cục bộ; rà năm góc nhìn độc lập và xử lý lỗi bắt buộc. H19 dùng chung với index phải được kiểm tra tại trang chỉ mục. Kết quả thực thi nằm trong review-log, không suy đạt chỉ từ đặc tả này.

## Khuôn ghi chú và quyết định triển khai

| note-topic-id | Đầu vào → sản phẩm → nối ra | Thành phần áp dụng và phần không áp dụng |
|---|---|---|
| L01-N01 | Tệp, tập hợp, đồ thị/véc-tơ → phân biệt bảy đầu ra → thêm nhu cầu dòng/lưu trữ | Vai trò, đặc tả, ví dụ/hình, giới hạn, kiểm tra. Không có giả mã/chứng minh chuyên biệt vì chỉ khảo sát ứng dụng Bài 02–07 |
| L01-N02 | Các đầu ra đã gặp → phân biệt khôi phục, truy cập, cửa sổ → khung tài nguyên | Định nghĩa trước minh họa, hình và điều kiện. Không có định lý hoặc giả mã mới của Bài 08–15 |
| L01-N03 | V06, tập hợp/vòng lặp → đặc tả R, vết hai tập, bất biến và chi phí → so sánh | Đầy đủ vai trò, đặc tả, ví dụ3/8, giao–hợp, giả mã, chứng minh, biên, chi phí, kiểm tra; LSH chi tiết chuyển Bài06 |
| L01-N04 | Lời giải cụ thể → mười tiêu chí và điều kiện đầy đủ → đọc chương trình | Tổng quan, từng khái niệm/ví dụ/hình, phép suy ra hậu kiểm A∩R; không triển khai chỉ mục hoặc LSH |
| L01-N05 | Khung đánh giá → tên/vai trò/thuộc tính của 14 bài → chuẩn bị | Bản đồ và bảng 14 bài. Không áp dụng chứng minh/giả mã cho thông tin chương trình |
| L01-N06 | Bản đồ và nền cá nhân → kế hoạch ôn, sản phẩm, hành vi → trách nhiệm suy luận | Tiên quyết, kỹ năng, tự chẩn đoán, chuẩn bị Bài 02. Không áp dụng định lý/thuật toán |
| L01-N07 | Tổ hợp, độc lập, kỳ vọng → biến đếm/giá trị đúng → bài tập | Vai trò, mô hình, hình, suy diễn và giới hạn. Không có thuật toán/cận triển khai vì chỉ đếm theo mô hình |
| L01-N08 | Mô hình nền → lời giải hai bài nguồn → giới hạn khi diễn giải | Đề, hình, gợi ý, lời giải và kiểm tra. Lập luận chỉ báo cho xác suất có trùng giữ từ bản cũ, được chứng minh một bước; không thêm thuật toán phát hiện người |

Bố cục ứng dụng được điều chỉnh từ hình hai phần ba chiều rộng sang hình toàn chiều ngang phía trên, ba thẻ dữ liệu/kết quả/giới hạn ở dưới để giữ chữ trong SVG dễ đọc. Mỗi trang vẫn có một luận điểm. H15 giữ vị trí tương đối A/B/Q, chỉ dịch cả nhóm hình khi vẽ lại; không tự thêm hình học thật. H10 giữ đúng chuỗi, không thêm mã hoặc tỷ lệ nén. H19 giữ năm nhóm và tên bài; danh mục phương pháp ở D03–D07 và bảng ghi chú.

Ghi chú diễn giả không đọc mã nội bộ hoặc phút. Thời lượng tổ chức giữ ở bảng từng trang: R01 dựng mô hình10, R02 giải(a,b)15, R03 giải(c)10, R04 dựng giỏ hàng10, R05 hoàn tất/chữa15 phút; R00 chuyển phần không tính. Các lời giải và hướng chấm ở đúng trang bài tập. Không phát sinh mã trình diễn.

## Tiêu chí riêng cho trang mở đầu và cầu nối

Các trang P00/P01/B00/B10/B11/C00/D00 mở bài hoặc kết nối các cụm. Chúng không có thuật toán hay định lý mới, nên không áp dụng chu trình giả mã–chứng minh riêng. P00 nhận diện bài; P01 nêu sản phẩm học tập; các trang còn lại xác định sự thay đổi đầu ra hoặc tài nguyên. Không thêm SVG trang trí. A08/A09 đã bỏ theo ER-001; phần giới thiệu dùng ngữ cảnh và câu nối ngay trong các ví dụ.

C00 mở phần C bằng đặc tả/đánh giá; C01 phân biệt gần trùng và giống hệt; C05 mở khung đánh giá; E01 nối chương trình với nền kiến thức; F01 nối trách nhiệm với suy luận; R00 nối mô hình lưu trú với bài tập. E04 nằm sau F04 để chỉ giao chuẩn bị bài kế tiếp khi kết thúc lập luận. Quill rà toàn bộ đường vào–ra và hai trang lân cận mỗi phía. No-ai-slop áp dụng lên mặt trang, alt, notes và Markdown; giữ nguồn, giả thiết, cảnh báo kỹ thuật và lời giải/chấm bài, bỏ lời dặn vẽ/soạn và giải trình lịch sử biên tập khỏi học liệu.

## ER-002 — bố cục và quyết định triển khai

B00 giới thiệu toàn phần; B01–B02 xét dữ liệu đang đến; B10 mở nhu cầu nén trước B03–B04; B11 định nghĩa truy cập theo khối trước B05–B09. Giữ 12 trang và thứ tự để bảo toàn ánh xạ với Bài08–15. Phần B 26 phút; tổng giảng120 và recitation60 không đổi. A và C–R giữ nguyên nội dung.

Điều phối giữ đề xuất planner về ba cụm và các trang mở cụm; sửa đề xuất giữ hình cũ vì hình cũ giới thiệu cơ chế trước bài toán. B01 dùng hai hàng cho hai đầu vào khác nhau, không coi thư và truy vấn là một dòng. B02 chuyển mômen sang ghi chú sau các đại lượng dễ hiểu. B03–B09 giữ đặc tả và nguồn; hình tập trung đầu vào, điều kiện đầu ra và trở ngại.

Các ví dụ này là khảo sát nhu cầu, không phải các thuật toán trọng tâm phải chứng minh trong Bài01. Đặc tả và khó khăn được nêu trên mặt; cơ chế và bảo đảm chi tiết chuyển tới bài tương ứng. C01 thu hồi chi phí, C07–C08 thu hồi cập nhật và điều kiện đúng. Kiểm tra ứng dụng ở F04 dùng lại khung ấy.

Nguồn bổ sung được chọn trong nguồn đã có: MMDS4.2 tr136–138 lấy mẫu theo người dùng và4.3 tr139 lọc thư; DSC14:6,10 hồ sơ giảng viên theo mã/lương; CMU lossy trang logic3 gộp mức sáng. Không thêm bộ dữ liệu. Vạch ở V12 chỉ mã hóa thứ tự tương đối, giữ đa tập trước/sau; dải sáng V11 là sơ đồ định tính, không mô phỏng chất lượng hoặc tỷ lệ nén. V15 giữ hình hộp bao nên chưa có đối tượng thật hoặc kết quả cuối; ghi rõ giới hạn trên hình và notes. Sửa quy mô student/takes về DSC15 slide24.

Writer tạo bản nháp B00/B01 và hình hai hàng trong thư mục tạm. Điều phối giữ ý ba nhóm và hai bài toán, không nhập nguyên văn: bản nháp thiếu B02, bỏ nhầm data-slide-id/notes và còn nhãn hình chật; bản tích hợp khôi phục cấu trúc mẫu và biên tập đầy đủ. Không thay đổi CSS chung.

### Chỉnh sau rà ER-003

Writer72050 soạn bốn đoạn sau đủ năm báo cáo; điều phối giữ ý chạy hai tập và gom đủ đóng góp, sửa cách gọi sai “cặp tài liệu là cặp ứng viên”, dùng định nghĩa chiều đúng. C01 bỏ số quy mô lặp để làm rõ chuẩn gần trùng. C04 chạy N2 cùngS,T theo hai nhánh ngưỡng, không đặt ngưỡng số mới. C15còn2phút,C16tăng2phút, tổng31giữ nguyên. E01tự kiểm dùng giao3/hợp8; E04thêm cầu tính đủ/không tính trùng khi phân tán. H26đảo mũi tên truy vấn→chỉ mục. Các thay đổi được rà lại toán và mạch toàn bài.

## Sửa toàn diện theo chuẩn 2026-10-14

Căn cứ: `AGENTS.md` ("Mẫu RevealJS bắt buộc", "Trang tiêu đề mạch", "Phân loại phần lớn", "Văn phong và mật độ mặt trang chiếu", "Tiêu chuẩn trang chiếu và ghi chú diễn giả"), `slide_authoring_standard.md`, deck mẫu Bài 06; kế hoạch `plan-lec01.md` (tác tử lập kế hoạch) và quyết định của điều phối viên (mục "Bài 01" và "Chung cho mọi bài" trong `decisions-decks.md`). Một tác tử soạn ghi tệp; không commit.

**Cấu trúc.** Bảy section ngoài: gộp mạch D và E cũ thành mạch 4 "Năm nhóm thuật toán và cách học"; F thành mạch 5; thêm mạch 6 "Tổng kết và tự kiểm tra" (section riêng, trước bài tập); mạch 7 bài tập giữ. Bỏ D00, ET, E00, E05, F00 và gộp E04 (nội dung chuyển như ghi trong bảng dưới). Thêm P02, P03 (tách từ P01), P04, A10, B12, C17 và C18 (tách từ C04, C06), D11, GT, G01, G02, G03; F04 chuyển sang mạch 6 và đổi vai trò. Deck 83 trang: 75 trang giảng, 8 trang bài tập.

| Mạch | Tên (khớp trang Nội dung) | Số trang | Phút | Vai trò chu trình của trang mở mạch |
|---|---|---:|---:|---|
| 1 | Tổng hợp và tìm kiếm dữ liệu web | 13 | 23 | bìa là trang tiêu đề mạch mở đầu |
| 2 | Dòng dữ liệu, nén và truy vấn trên đĩa | 14 | 24 | BT ngoài chu trình khái niệm |
| 3 | Đặc tả và đánh giá thuật toán | 20 | 30 | CT ngoài chu trình khái niệm |
| 4 | Năm nhóm thuật toán và cách học | 16 | 21 | DT ngoài chu trình khái niệm |
| 5 | Mẫu trùng ngẫu nhiên và suy luận | 7 | 14 | FT ngoài chu trình; nhận nội dung F00 |
| 6 | Tổng kết và tự kiểm tra | 5 | 8 | GT ngoài chu trình khái niệm |
| 7 | Bài tập vận dụng | 8 | 60 | RT ngoài chu trình; 0,5 phút lấy từ R00 |

**Phân bổ thời gian khi phần giảng vượt 60 trang.** 75 trang giảng trong 120 phút, trung bình khoảng 1,6 phút mỗi trang: 23 + 24 + 30 + 21 + 14 + 8 = 120; bài tập 0,5 + 2,5 + 7 + 15 + 10 + 8 + 5 + 12 = 60. So với bản trước (A23/B24/C31/D17/E9/F16): mạch 3 bớt 1 phút, mạch D+E bớt 5 phút nhờ bỏ bốn trang tổng quan hoặc lặp, mạch F bớt 2 phút khi F00, F04, E04 rời mạch; mạch 6 mới nhận 8 phút. Năm trang tiêu đề mạch của phần giảng (BT, CT, DT, FT, GT) và trang Nội dung mỗi trang 0,5 phút; 16 trang tình huống theo một khuôn cố định 2–2,5 phút. Không phần nào chuyển sang đọc thêm và không rút ví dụ, chứng minh cốt lõi.

**Khuôn trang tình huống** (A01–A07, B01–B09): dòng Đầu vào, dòng Đầu ra, hình giữ nguyên, một câu nêu giới hạn của cách làm trực tiếp; câu thứ hai của khung cũ chuyển vào ghi chú. A01 theo cùng khuôn, thêm bảng dữ kiện cạnh hình.

**Chu trình các cụm.** Cặp gần trùng: A06, C01 (nhu cầu) → C02 (ví dụ rồi định nghĩa Jaccard) → C03 (đặc tả) → C17 (ví dụ chạy tay) → C04 (thuật toán, câu hỏi) → C05 (khung tiêu chí) → C06, C18 (tính đúng, dừng, biên) → C07 (chi phí) → C08–C15 (tiêu chí khác) → C16 (kiểm tra). Đủ tám bước; bước "giới hạn của cách làm trước" không áp dụng vì đây là thuật toán đầu tiên của học phần. Mô hình xác suất: F01 → F02 → F05 → F06 → F03 → F07. Giới thiệu học phần: DT → D01 … E03 → D11 (chu trình rút gọn: phần định hướng, không giả mã hay chứng minh của Bài 02–15). Bảng thuật toán, đầu vào, bảo đảm, chi phí ở mạch 6 không lập riêng vì bài chỉ đặc tả một thuật toán; G01 có hàng cho thuật toán xét mọi cặp.

**Loại kiểm tra theo mạch.** Mạch 1: A10. Mạch 2: B12. Mạch 3: câu hỏi C04, C16. Mạch 4: D11. Mạch 5: F07. Mạch 6: G02. Mạch 7: hai bài MMDS 1.2.1, 1.2.2. Lời giải ở ghi chú diễn giả.

**Ngoại lệ.** A01: bảng dữ kiện 4 hàng; sau lượt sửa theo đúng khuôn tình huống (Đầu vào, Đầu ra, bảng cạnh hình, một câu giới hạn), 8 dòng kể cả hàng bảng (quyết định 5). P01 (Nội dung): 7 mạch và dòng Đọc trước, 8 dòng. G03 (Nguồn và tài liệu đọc): 7 dòng. D02 chỉ có hình. Các trang bảng (B00, C05, C18, D01, D06, D07, D10, E01, E02, E03, F02, F07, G01, R00, R06) tối đa 8 dòng kể cả hàng bảng. Cột "Dòng" dưới đây đếm thô phần tử `p`, `li`, hàng bảng, kể cả nhãn trong khối hình HTML.

Âm tiết đếm bằng `scratchpad/w01/cap01.py` (bỏ tiêu đề, công thức, khối mã, SVG); cột "trước" lấy từ bảng §0.1 của `plan-lec01.md`.

| # | Mạch | Mã | Tiêu đề hiện hành | Quyết định | Âm tiết trước → sau | Trần | Dòng | Phút | Lý do |
|---:|---:|---|---|---|---|---:|---:|---:|---|
| 1 | 1 | `L01-P00` | Bài toán dữ liệu lớn và mô hình thuật toán | `sửa` | 12 → 49 | — | 4 | 0,5 | khuôn `title-slide`; câu luận đề 24 âm tiết (bốn thành phần); thêm ghi chú (trước không có); lượt sửa: luận đề "Yêu cầu dữ liệu lớn chỉ thành… khi đã chốt…" (25) |
| 2 | 1 | `L01-P02` | Tiên quyết và quy ước | `thêm` | — → 58 | 60 | 5 | 1,5 | Tiên quyết và quy ước: UET.CS1058, số cặp, giao–hợp, độc lập và kỳ vọng tổng, ký hiệu $N$, $C_i$, $i<j$, $\tau$; lượt sửa: Ký hiệu thêm $R$; tên học phần tiên quyết vào ghi chú |
| 3 | 1 | `L01-P03` | Mục tiêu học tập | `thêm` | — → 80 | 80 | 5 | 1 | tách từ P01: năm mục tiêu, mỗi mục một sản phẩm kiểm được; trần 80 |
| 4 | 1 | `L01-P01` | Nội dung | `sửa` | 91 → 68 | 80 | 8 | 0,5 | `agenda-slide`, tiêu đề "Nội dung"; bảy mạch mới (cột 1–3, 4–7); Đọc trước; hết ngoại lệ tạm; lượt sửa: Đọc trước ghi tên sách Foundations of Data Science; ngoại lệ 8 dòng của trang Nội dung |
| 5 | 1 | `L01-P04` | Vấn đề trung tâm | `thêm` | — → 59 | 60 | 5 | 1,5 | Vấn đề trung tâm: Nhu cầu $10^6$ tài liệu và bốn câu trả lời có điều kiện theo mạch 2–5; lượt sửa: danh sách không đánh số; dòng cuối "Lưu trú độc lập: kỳ vọng…biến cố trùng" |
| 6 | 1 | `L01-A01` | Tính tổng kích thước trang web theo máy chủ | `sửa` | 45 → 50 | 60 | 8 | 2,5 | Đầu vào, bảng 4 hàng, hình, Kết luận có số; bỏ mũi tên; ngoại lệ 7 dòng (quyết định 5); lượt sửa: theo khuôn tình huống: thêm Đầu ra (kèm số), câu kết nêu giới hạn tệp vượt bộ nhớ; 8 dòng kể cả bảng |
| 7 | 1 | `L01-A02` | Đếm số lần xuất hiện của từng từ | `sửa` | 46 → 36 | 60 | 3 | 2,5 | khuôn tình huống Đầu vào, Đầu ra, hình, một câu giới hạn; câu thứ hai vào ghi chú; lượt sửa: bỏ câu lặp ghi chú |
| 8 | 1 | `L01-A03` | Tính điểm quan trọng của trang web | `sửa` | 56 → 43 | 60 | 3 | 2,5 | khuôn tình huống; ghi chú ≤ 150 |
| 9 | 1 | `L01-A04` | Ưu tiên kết quả tìm kiếm theo chủ đề | `sửa` | 52 → 41 | 60 | 3 | 2 | khuôn tình huống |
| 10 | 1 | `L01-A05` | Hạn chế liên kết rác trong xếp hạng | `sửa` | 55 → 46 | 60 | 3 | 2 | khuôn tình huống |
| 11 | 1 | `L01-A06` | Tìm các cặp tài liệu gần trùng | `sửa` | 37 → 36 | 60 | 3 | 2,5 | khuôn tình huống; ví dụ xuyên suốt; ghi chú sửa lộ trình Bài 05 (chữ ký MinHash), Bài 06 (phân dải LSH) |
| 12 | 1 | `L01-A07` | Tìm đoạn tài liệu bằng véc-tơ truy vấn | `sửa` | 49 → 44 | 60 | 3 | 2 | khuôn tình huống; ghi chú 183 → ≤ 150 |
| 13 | 1 | `L01-A10` | Câu hỏi về bảy bài toán trên kho web | `thêm` | — → 44 | 60 | 4 | 2 | Câu hỏi về bảy bài toán; dữ kiện từ A01, A06, A07; lời giải trong ghi chú |
| 14 | 2 | `L01-BT` | 2. Dòng dữ liệu, nén và truy vấn trên đĩa | `giữ` | — → 38 | — | 2 | 0,5 | trang tiêu đề mạch 2; ghi chú bọc `p` |
| 15 | 2 | `L01-B00` | Bộ nhớ, dung lượng và số khối đọc ghi | `sửa` | 79 → 61 | 80 | 4 | 0,5 | tiêu đề "Bộ nhớ, dung lượng và số khối đọc ghi" (khác tên mạch); bảng ba hàng; trần 80 |
| 16 | 2 | `L01-B01` | Giữ mẫu truy vấn và lọc thư đến | `sửa` | 49 → 50 | 60 | 3 | 2,5 | khuôn tình huống |
| 17 | 2 | `L01-B02` | Đếm người dùng và lượt truy cập gần đây | `sửa` | 49 → 39 | 60 | 3 | 2,5 | khuôn tình huống; dòng 22 âm tiết tách |
| 18 | 2 | `L01-B10` | Nén dữ liệu để lưu và khôi phục | `sửa` | 65 → 42 | 60 | 3 | 1 | Nhu cầu + hai `ex-card` |
| 19 | 2 | `L01-B03` | Lưu văn bản với ít dung lượng hơn | `sửa` | 48 → 34 | 60 | 3 | 2 | khuôn tình huống; `code` → `span.inline-code` |
| 20 | 2 | `L01-B04` | Giảm dung lượng ảnh với sai số cho phép | `sửa` | 45 → 39 | 60 | 3 | 2 | khuôn tình huống |
| 21 | 2 | `L01-B11` | Xử lý và truy vấn dữ liệu trên đĩa | `sửa` | 83 → 58 | 60 | 6 | 1 | định nghĩa khối lên mặt trang; `ul` ba thao tác; bỏ `.grid3` |
| 22 | 2 | `L01-B05` | Sắp xếp tệp lớn theo khóa | `sửa` | 58 → 47 | 60 | 3 | 2 | khuôn tình huống |
| 23 | 2 | `L01-B06` | Tìm hồ sơ giảng viên theo mã hoặc lương | `sửa` | 52 → 39 | 60 | 3 | 2 | khuôn tình huống |
| 24 | 2 | `L01-B07` | Tìm tài liệu chứa đồng thời hai từ khóa | `sửa` | 55 → 33 | 60 | 3 | 2 | khuôn tình huống |
| 25 | 2 | `L01-B08` | Tìm đối tượng giao vùng trên bản đồ | `sửa` | 52 → 38 | 60 | 3 | 2 | khuôn tình huống |
| 26 | 2 | `L01-B09` | Ghép sinh viên với các môn đã đăng ký | `sửa` | 54 → 44 | 60 | 3 | 2 | khuôn tình huống; ghi chú bỏ "Phần tiếp theo…" |
| 27 | 2 | `L01-B12` | Câu hỏi về dòng, nén và truy vấn trên đĩa | `thêm` | — → 51 | 60 | 4 | 2 | Câu hỏi về dòng, nén và truy vấn trên đĩa; dữ kiện từ B10, B09, B04; lượt sửa: câu 2 hỏi vì sao quét lại tốn khối; lời giải có phép đếm 2 000 100 (DSC) |
| 28 | 3 | `L01-CT` | 3. Đặc tả và đánh giá thuật toán | `giữ` | — → 38 | — | 2 | 0,5 | trang tiêu đề mạch 3 |
| 29 | 3 | `L01-C00` | Phân tích thuật toán xử lý dữ liệu lớn | `sửa` | 69 → 43 | 60 | 3 | 0,5 | hai `ex-card` Đặc tả, Đánh giá |
| 30 | 3 | `L01-C01` | Bài toán tìm cặp tài liệu gần trùng | `sửa` | 53 → 49 | 60 | 3 | 1,5 | Nhu cầu, hình, Đầu ra |
| 31 | 3 | `L01-C02` | Độ tương đồng Jaccard | `sửa` | 38 → 46 | 60 | 4 | 2 | tiêu đề "Độ tương đồng Jaccard"; ví dụ trước định nghĩa; Kết luận $\tau\le3/8$; lượt sửa: "đoạn ký tự (shingle)"; Kết luận $J\ge\tau\iff\tau\le3/8$ |
| 32 | 3 | `L01-C03` | Đặc tả tìm cặp gần trùng | `sửa` | 41 → 30 | 60 | 5 | 2,5 | thẻ thành dòng Đầu vào, Đầu ra; Trường hợp biên |
| 33 | 3 | `L01-C17` | Ví dụ: thứ tự xét cặp | `thêm` | — → 22 | 60 | 4 | 1,5 | tách từ C04: thứ tự xét cặp $N=4$ và ví dụ $N=2$ |
| 34 | 3 | `L01-C04` | Thuật toán: xét mọi cặp | `sửa` | 24 → 29 | 60 | 2 | 2,5 | "Thuật toán: xét mọi cặp"; Đầu vào/Đầu ra; `pre.ex-code`; câu hỏi dạng nhiệm vụ; ghi chú bỏ hứa "Bài 05 phân tích hai con trỏ" |
| 35 | 3 | `L01-C05` | Các tiêu chí đánh giá | `sửa` | 75 → 68 | 80 | 6 | 1 | bảng bốn hàng thay ba thẻ; trần 80 |
| 36 | 3 | `L01-C06` | Tính đúng: bất biến của xét mọi cặp | `sửa` | 45 → 39 | 60 | 2 | 1,5 | "Tính đúng: xét mọi cặp"; Mệnh đề, hình, Bất biến; lượt sửa: tiêu đề "Tính đúng: bất biến của xét mọi cặp" |
| 37 | 3 | `L01-C18` | Tính đúng: khởi tạo, duy trì, kết thúc | `thêm` | — → 60 | 60 | 6 | 1,5 | tách: bảng Khởi tạo, Duy trì, Kết thúc; Điều kiện dừng; Trường hợp biên; lượt sửa: tiêu đề "Tính đúng: khởi tạo, duy trì, kết thúc"; Duy trì "cặp mới chưa từng xét" |
| 38 | 3 | `L01-C07` | Chi phí: khối lượng tính toán | `sửa` | 38 → 59 | 60 | 5 | 2 | `cost-slide`; Mô hình; bảng Bước, Số lần, Chi phí mỗi lần, Đóng góp; bỏ hình lặp; lượt sửa: chi phí mỗi lần $\le2L$ phép so sánh (trộn hai danh sách), đóng góp $\le N(N-1)L$ |
| 39 | 3 | `L01-C08` | Bộ nhớ làm việc | `sửa` | 38 → 30 | 60 | 2 | 1,5 | câu kết một câu |
| 40 | 3 | `L01-C09` | Đọc ghi và số lượt quét | `sửa` | 47 → 37 | 60 | 3 | 1,5 | định nghĩa bằng "là" |
| 41 | 3 | `L01-C10` | Dữ liệu truyền qua mạng | `sửa` | 45 → 37 | 60 | 2 | 1,5 | câu kết một câu |
| 42 | 3 | `L01-C11` | Độ trễ truy vấn | `sửa` | 42 → 28 | 60 | 2 | 1,5 | câu kết một câu |
| 43 | 3 | `L01-C12` | Chi phí xây dựng chỉ mục | `sửa` | 45 → 29 | 60 | 2 | 1 | định nghĩa bằng "là" |
| 44 | 3 | `L01-C13` | Chi phí cập nhật dữ liệu | `sửa` | 45 → 36 | 60 | 2 | 1 | câu kết một câu |
| 45 | 3 | `L01-C14` | Dung lượng lưu trữ | `sửa` | 40 → 36 | 60 | 2 | 1 | câu kết một câu |
| 46 | 3 | `L01-C15` | Chất lượng kết quả gần đúng | `sửa` | 31 → 33 | 60 | 3 | 2 | công thức không còn chữ Việt trong `\text{}`; Kết luận |
| 47 | 3 | `L01-C16` | Giảm ứng viên và nguy cơ bỏ sót | `sửa` | 35 → 31 | 60 | 2 | 2 | câu hỏi dạng nhiệm vụ; thuật ngữ LSH theo Bài 06 |
| 48 | 4 | `L01-DT` | 4. Năm nhóm thuật toán và cách học | `sửa` | — → 41 | — | 2 | 0,5 | mạch 4 "Năm nhóm thuật toán và cách học" (gộp D+E); dòng dẫn, từ khóa, ghi chú mới |
| 49 | 4 | `L01-D01` | Học phần và năng lực cần đạt | `sửa` | 73 → 36 | 80 | 4 | 0,5 | bỏ dòng tên học phần lặp bìa; ba mặt năng lực vào ghi chú; trần 80; lượt sửa: rút thành trang dẫn hai năng lực CLO1–CLO2 (hai năng lực còn lại ở E02, E03); 1 → 0,5 phút |
| 50 | 4 | `L01-D02` | Năm nhóm bài của học phần | `giữ` | 0 → 0 | 60 | 0 | 1 | chỉ hình (`l01-map`) |
| 51 | 4 | `L01-D03` | MapReduce: gom kết quả theo khóa | `sửa` | 52 → 44 | 60 | 3 | 1,5 | khung → câu kết |
| 52 | 4 | `L01-D08` | PageRank: tính điểm theo liên kết | `sửa` | 68 → 50 | 60 | 3 | 1,5 | định nghĩa phân phối dịch chuyển vào ghi chú; lượt sửa: "bước nhảy ngẫu nhiên" thay "điểm nền" |
| 53 | 4 | `L01-D04` | MinHash và LSH: chọn cặp cần đối chiếu | `sửa` | 57 → 59 | 60 | 4 | 1,5 | dòng dẫn "Bài 05: chữ ký MinHash; Bài 06: phân dải LSH"; LSH theo Bài 06 |
| 54 | 4 | `L01-D09` | Chỉ mục cho truy vấn véc-tơ | `sửa` | 70 → 47 | 60 | 3 | 1 | HNSW giải nghĩa; câu đo lường vào ghi chú |
| 55 | 4 | `L01-D05` | Lấy mẫu và lọc trên dòng dữ liệu | `sửa` | 53 → 46 | 60 | 3 | 1 | thẻ rút ≤ 15 âm tiết |
| 56 | 4 | `L01-D10` | Cấu trúc gọn cho thống kê dòng | `sửa` | 90 → 62 | 80 | 5 | 1,5 | bảng rút ô; trần 80 |
| 57 | 4 | `L01-D06` | Nén theo ký hiệu, mẫu lặp và ảnh | `sửa` | 68 → 64 | 80 | 5 | 1,5 | bảng rút ô; trần 80 |
| 58 | 4 | `L01-D07` | Tổ chức dữ liệu để giảm đọc ghi | `sửa` | 114 → 77 | 80 | 6 | 1,5 | bảng rút ô; khung vào ghi chú; trần 80 |
| 59 | 4 | `L01-E01` | Kiến thức nền dùng ở từng nhóm bài | `sửa` | 124 → 79 | 80 | 6 | 1,5 | bảng rút ô; dòng tiên quyết sang P02; vượt 1,5 lần trần → đạt; lượt sửa: tên nhóm theo bản đồ năm nhóm |
| 60 | 4 | `L01-E02` | Sản phẩm khi phân tích thuật toán | `sửa` | 85 → 77 | 80 | 6 | 2 | bảng rút ô; trần 80; lượt sửa: nhận 0,5 phút từ D01 |
| 61 | 4 | `L01-E06` | Báo cáo chất lượng và hiệu năng | `sửa` | 70 → 41 | 60 | 3 | 1 | một câu kết; lượt sửa: bỏ hình lặp C15, thay bằng dòng Nhắc lại |
| 62 | 4 | `L01-E03` | Tự học, hợp tác và trách nhiệm dữ liệu | `sửa` | 112 → 79 | 80 | 6 | 1,5 | bảng rút ô; Kết luận; trần 80 |
| 63 | 4 | `L01-D11` | Câu hỏi về nhóm bài và kiến thức nền | `thêm` | — → 34 | 60 | 3 | 2 | Câu hỏi về nhóm bài và kiến thức nền; lời giải trong ghi chú |
| 64 | 5 | `L01-FT` | 5. Mẫu trùng ngẫu nhiên và suy luận | `sửa` | — → 37 | — | 2 | 0,5 | mạch 5 (`id="mach-5"`); ghi chú nhận nội dung F00 |
| 65 | 5 | `L01-F01` | Tìm mẫu trùng trong hồ sơ lưu trú | `sửa` | 51 → 47 | 60 | 4 | 1,5 | Nhu cầu (từ F00), Đầu vào; bỏ nhãn "Khó khăn:" |
| 66 | 5 | `L01-F02` | Mô hình lưu trú không phối hợp | `sửa` | 62 → 41 | 60 | 6 | 2 | Giả thiết một dòng; 6 dòng kể cả bảng |
| 67 | 5 | `L01-F05` | Xác suất trùng một ngày và hai ngày | `sửa` | 46 → 37 | 60 | 4 | 2 | Kết luận $p^2=10^{-18}$ |
| 68 | 5 | `L01-F06` | Đơn vị đếm và số phép thử | `sửa` | 42 → 37 | 60 | 3 | 2 | định nghĩa phép thử bằng "là"; công thức không còn chữ Việt trong KaTeX |
| 69 | 5 | `L01-F03` | Kỳ vọng số biến cố trùng | `sửa` | 48 → 44 | 60 | 4 | 3 | bỏ `.big`; Kết luận; lượt sửa: "$X$ là tổng các chỉ báo trùng" |
| 70 | 5 | `L01-F07` | Mẫu trùng và căn cứ suy luận | `sửa` | 111 → 71 | 80 | 5 | 3 | bảng rút ô; câu hỏi; trần 80 |
| 71 | 6 | `L01-GT` | 6. Tổng kết và tự kiểm tra | `thêm` | — → 40 | — | 2 | 0,5 | trang tiêu đề mạch 6 "Tổng kết và tự kiểm tra" |
| 72 | 6 | `L01-G01` | Kết quả và giả thiết không được bỏ | `thêm` | — → 78 | 80 | 7 | 2 | Kết quả và giả thiết không được bỏ (5 hàng); trần 80; lượt sửa: thêm hàng chi phí đọc ghi ($F$, $2F$); rút ô để giữ 80 |
| 73 | 6 | `L01-F04` | Câu trả lời cho vấn đề trung tâm | `sửa` | 102 → 78 | 80 | 5 | 2 | chuyển sang mạch 6, đổi vai trò "Câu trả lời cho vấn đề trung tâm" theo thứ tự P04; dòng 4 nêu chữ ký MinHash, phân dải LSH; lượt sửa: danh sách không đánh số; dòng khối đọc ghi nêu sắp hoặc băm theo khóa (Bài 12, 15); dòng cuối "kỳ vọng…biến cố trùng" |
| 74 | 6 | `L01-G02` | Câu hỏi tự kiểm tra | `thêm` | — → 50 | 60 | 4 | 2,5 | Câu hỏi tự kiểm tra (gom câu E05, E04 và dòng tự kiểm của ghi chú bài giảng); lượt sửa: câu 2 dựa trên hàng chi phí đọc ghi của G01 ($6F$); lời giải câu 3 nêu độc lập giữa hai người cho $1/H$ |
| 75 | 6 | `L01-G03` | Nguồn và tài liệu đọc | `thêm` | — → 70 | 80 | 6 | 1 | Nguồn và tài liệu đọc; ghi công mmds.org; dòng Bài 02 (gộp E04); lượt sửa: phạm vi chương, mục, trang; tên sách Foundations of Data Science; "tính kết hợp và giao hoán"; 7 dòng (ngoại lệ trang nguồn) |
| 76 | 7 | `L01-RT` | 7. Bài tập vận dụng | `giữ` | — → 34 | — | 2 | 0,5 | trang tiêu đề mạch 7 (0,5 phút lấy từ R00) |
| 77 | 7 | `L01-R00` | Bài tập: phép đếm và suy luận | `sửa` | 73 → 65 | 80 | 5 | 2,5 | "Bài tập: …"; bỏ dòng nguồn, mũi tên, nhãn "Sản phẩm:" |
| 78 | 7 | `L01-R01` | Bài tập: hồ sơ lưu trú, ba biến thể | `sửa` | 49 → 56 | 80 | 6 | 7 | ba dòng (a), (b), (c); dòng Nguồn `ex-note`; lượt sửa: "kỳ vọng số biến cố trùng (sách: số cặp nghi vấn)" |
| 79 | 7 | `L01-R02` | Bài tập: hồ sơ lưu trú (a), (b) | `sửa` | 62 → 52 | 80 | 4 | 15 | "Gợi ý:" vào ghi chú; dòng Nguồn `ex-note`; lượt sửa: "từng phần" |
| 80 | 7 | `L01-R03` | Bài tập: hồ sơ lưu trú (c) | `sửa` | 45 → 51 | 80 | 5 | 10 | "Sản phẩm:" → "Lời giải gồm…"; dòng Nguồn |
| 81 | 7 | `L01-R04` | Bài tập: cặp người mua cùng tập mặt hàng | `sửa` | 48 → 46 | 80 | 4 | 8 | câu hỏi rút ≤ 20 âm tiết, giữ nghĩa đề; dòng Nguồn; lượt sửa: câu hỏi không dùng "kỳ vọng" theo nghĩa thường |
| 82 | 7 | `L01-R06` | Bài tập: tập mặt hàng, đơn vị đếm | `sửa` | 96 → 74 | 80 | 7 | 5 | bảng giữ; Giả thiết; dòng Nguồn |
| 83 | 7 | `L01-R05` | Bài tập: tập mặt hàng, bốn phần lời giải | `sửa` | 52 → 56 | 80 | 6 | 12 | dòng Nguồn `ex-note` |

Trang bỏ hoặc gộp: `L01-D00` (`bỏ`: bảng mô tả chính phần, trùng dòng dẫn; ví dụ "tìm gần trùng cần giảm số cặp; nối bảng cần giảm khối đọc lại" vào ghi chú DT); `L01-ET` (`bỏ`: mạch 5 cũ gộp vào mạch 4; ghi chú vào DT); `L01-E00` (`bỏ`: trùng D01 và E01–E03; ba mặt kiến thức, kỹ năng, cách học vào ghi chú D01); `L01-E05` (`bỏ`: trùng C02; câu hỏi sang G02 câu 1); `L01-F00` (`gộp`: câu nhu cầu thành dòng Nhu cầu của F01, ba thẻ vào ghi chú FT); `L01-E04` (`gộp`: dòng chuẩn bị Bài 02 sang G03, câu hỏi chạy lại tác vụ sang G02 câu 2).

**Phiếu trang mới (lượt sửa sau rà ba vai: mỗi trang một phiếu, đủ chín trường).** Thứ tự trường: mạch; mục đích; hành động của sinh viên; đối tượng trung tâm; dữ kiện kế thừa; kiến thức đầu vào; sản phẩm; bằng chứng; quyết định.

- `L01-P02` Tiên quyết và quy ước — 1; nêu kiến thức tiên quyết thật sự dùng (bài đầu học phần); đối chiếu bốn dòng nhắc lại với kiến thức đã học; số cặp, giao–hợp, độc lập và kỳ vọng tổng; UET.CS1058; toán rời rạc, xác suất cơ bản; ký hiệu $N$, $C_i$, $i<j$, $\tau$, $R$; A06, C02, C03, F05, F03 dùng lại; `thêm`.
- `L01-P03` Mục tiêu học tập — 1; năm mục tiêu kiểm được (1↔MT1; 2↔MT2, MT3; 3↔MT3, MT4; 4↔MT5; 5↔MT6); ghi sản phẩm cần nộp; năm năng lực của bài; không; P02; danh sách mục tiêu; A10, B12, C04, C18, C07, C16, D11, F07, G02, bài tập; `thêm` (tách từ P01).
- `L01-P04` Vấn đề trung tâm — 1; nêu nhu cầu kho $10^6$ tài liệu và bốn câu trả lời có điều kiện; ghi bốn điều kiện để kiểm ở cuối bài; $R$, $N(N-1)/2$, khối đọc ghi, kỳ vọng $249\,750$ biến cố trùng; ký hiệu P02; P02, P03; bốn điều kiện; F04 trả lời cùng thứ tự (dòng 1 ↔ khối đọc ghi và sắp, băm theo khóa; dòng 2 ↔ $499\,999\,500\,000$ lần kiểm, $O(N^2L)$; dòng 3 ↔ điều kiện đủ khi chọn ứng viên bằng chữ ký MinHash, phân dải LSH; dòng 4 ↔ kỳ vọng nền và giới hạn kết luận); `thêm`. Ghi chú: ba câu hỏi, phần mẫu trùng là đọc thêm thu gọn (quyết định tác giả 2026-11-11). Deck: bốn câu ở P04/F04, mạch 5 trong phần giảng, G01–G02 hỏi về $\mathbb E[X]$. Quyết định: không sửa deck trong đợt này.
- `L01-A10` Câu hỏi về bảy bài toán trên kho web — 1; kiểm khả năng nêu đầu vào, đầu ra, trở ngại; trả lời ba câu; ba bài toán A01, A06, A07; số liệu A01, A06, A07; A01–A07; lời giải trong ghi chú; câu trả lời của sinh viên; `thêm`.
- `L01-B12` Câu hỏi về dòng, nén và truy vấn trên đĩa — 2; kiểm phân biệt trạng thái đếm, bản nén và khối đọc ghi; trả lời ba câu; số đếm người dùng, hai bảng 100/400 khối, ảnh nén mất thông tin; B10, B09, B04; B01–B09; lời giải (có phép đếm $2\,000\,100$ lần chuyển khối theo DSC); câu trả lời; `thêm`.
- `L01-C17` Ví dụ: thứ tự xét cặp — 3; chạy tay vòng lặp $i<j$; liệt kê sáu cặp với $N=4$ và xét $N=2$; thứ tự cặp; $S$, $T$, $J=3/8$ của C02; đặc tả C03; vết chạy; C04 câu hỏi; `thêm` (tách từ C04).
- `L01-C18` Tính đúng: khởi tạo, duy trì, kết thúc — 3; chứng minh thuật toán xét mọi cặp trả đúng $R$; theo ba bước của bất biến; bất biến của C06; giả mã C04; bất biến (học phần tiên quyết); lập luận ba bước, điều kiện dừng, trường hợp biên; G01 hàng tính đúng, mục tiêu 2; `thêm` (tách từ C06).
- `L01-D11` Câu hỏi về nhóm bài và kiến thức nền — 4; kiểm việc ghép giới hạn với nhóm bài; ghép ba giới hạn và nêu kiến thức cần ôn; bản đồ năm nhóm; số cặp, bảng 400 khối, bản ghi đến liên tục; D02–E01; lời giải trong ghi chú; câu trả lời; `thêm`.
- `L01-GT` Tổng kết và tự kiểm tra — 6; trang tiêu đề mạch kết luận; đọc dòng dẫn và từ khóa; năm kết quả của bài; mọi mạch trước; không; định hướng mạch; G01–G03; `thêm`.
- `L01-G01` Kết quả và giả thiết không được bỏ — 6; đặt sáu kết quả cạnh giả thiết; nêu hệ quả khi bỏ từng giả thiết; bảng kết quả–giả thiết–công thức; $R$, bất biến, $F$/$2F$, $O(N^2L)$, điều kiện đủ, kỳ vọng nền; C03, C18, C09, C07, C16, F03; bảng tóm tắt; G02 câu 2; `thêm`.
- `L01-G02` Câu hỏi tự kiểm tra — 6; kiểm ba kết quả của G01 (Jaccard và ngưỡng; chi phí đọc ghi; mô hình lưu trú); trả lời và nêu kết quả đã dùng; ba câu; $J=3/8$, $F$, $\mathbb E[X]$; C02, C09, G01, F03, F05; lời giải trong ghi chú; câu trả lời; `thêm`.
- `L01-G03` Nguồn và tài liệu đọc — 6; liệt kê nguồn có chương, mục, trang, ghi công mmds.org, nối Bài 02; chọn tài liệu đọc; danh mục nguồn; dòng "Nguồn:" của mọi ghi chú; không; danh mục và dòng chuẩn bị Bài 02; không có câu hỏi; `thêm` (gộp E04).
- `L01-F04` Câu trả lời cho vấn đề trung tâm — 6 (chuyển từ mạch F, đổi vai trò); trả lời P04 theo thứ tự bằng số của bài; đối chiếu từng dòng với P04; bốn kết luận có điều kiện; G01; mọi mạch; bốn câu trả lời; G02; `sửa`. Ghi chú: ba câu hỏi, phần mẫu trùng là đọc thêm thu gọn (quyết định tác giả 2026-11-11). Deck: bốn câu ở P04/F04, mạch 5 trong phần giảng, G01–G02 hỏi về $\mathbb E[X]$. Quyết định: không sửa deck trong đợt này.

## Ánh xạ chủ đề của ghi chú (đợt B1, 2026-11-11)

Ghi chú viết lại theo chuẩn giáo trình; mã chủ đề cũ `L01-N0k` đổi thành `lec-01-topic-0k`. Các chú thích `<!-- note-topic-id: … -->` đặt trước tiêu đề mục tương ứng trong `materials/lec-01/lecture-note.md`.

| Mã cũ | note-topic-id | Mục ghi chú | Trang chiếu (`data-slide-id`) | Khối số hiệu | Vào → ra |
|---|---|---|---|---|---|
| L01-N01 | `lec-01-topic-01` | Mục 1 (1.1–1.2) | L01-P00, P02, P03, P01, P04, A01–A07, A10 | Định nghĩa 01.1, 01.2; Nhận xét 01.3; Ví dụ 01.1–01.2; Bài tập 01.1–01.2 | mô hình RAM của học phần tiên quyết → bài toán dữ liệu có ngân sách → cần đơn vị đo |
| L01-N02 | `lec-01-topic-02` | Mục 2 | L01-BT, B00, B01, B02, B10, B03, B04, B11, B05–B09, B12; C09 cho Mệnh đề 01.5 | Định nghĩa 01.4, 01.7, 01.8; Mệnh đề 01.5; Nhận xét 01.6; Ví dụ 01.3–01.5; Bài tập 01.3–01.4 | ngân sách bằng lời → số lần chuyển khối $F$, $2F$, $2mF$ → cần đặc tả chặt |
| L01-N03 | `lec-01-topic-03` | Mục 3.1–3.3 | L01-CT, C00, C01, C02, C03, C17, C04, C06, C18 | Định nghĩa 01.9, 01.10; Thuật toán 01.11; Mệnh đề 01.12; Ví dụ 01.6–01.7 | cặp gần trùng → $R$ và tính đúng → cần chi phí |
| L01-N04 | `lec-01-topic-04` | Mục 3.4–3.5 | L01-C05, C07, C08, C10–C16 | Định nghĩa 01.13, 01.17; Bổ đề 01.14; Mệnh đề 01.15, 01.16; Ví dụ 01.8 (chi phí), 01.9 (xác minh ứng viên), 01.10 (độ thu hồi); Bài tập 01.5–01.7 | $N(N-1)L$ phép so sánh → điều kiện $R\subseteq A$ → nhóm phương pháp |
| L01-N05 | `lec-01-topic-05` | Mục 4.1 | L01-DT, D02, D03, D08, D04, D09, D05, D10, D06, D07, D11 | Ví dụ 01.11 | ba giới hạn → năm nhóm Bài 02–15 → kiến thức nền |
| L01-N06 | `lec-01-topic-06` | Mục 4.2 | L01-D01, E01, E02, E06, E03 | Bài tập 01.8 | nhóm bài → CLO, kiến thức nền, sản phẩm, trách nhiệm → câu hỏi về mẫu ngẫu nhiên |
| L01-N07 | `lec-01-topic-07` | Đọc thêm (trước là Mục 5; loại `đọc thêm`, quyết định tác giả 2026-11-11) | L01-FT, F01, F02, F05, F06, F03, F07 | Định nghĩa 01.18, 01.19; Mệnh đề 01.20; Bổ đề 01.21; Hệ quả 01.22; Nhận xét 01.23; Ví dụ 01.12–01.14; Bài tập 01.9 | phần đọc thêm, không nối vào mạch chính: mô hình nền → $\mathbb E[X]\approx249\,750$, Markov → giới hạn kết luận |
| L01-N08 | `lec-01-topic-08` | Bài tập củng cố; `materials/lec-01/exercises.md` | L01-RT, R00–R06 | Bài tập 01.10 (MMDS 1.2.1), 01.11 (MMDS 1.2.2) | mô hình nền → hai bài recitation có gợi ý và lời giải |

Các trang tổng kết L01-GT, G01, F04, G02, G03 ứng với "Tóm tắt chương" và "Hướng dẫn đọc thêm" của ghi chú, không mang `note-topic-id` riêng. Ba tình huống áp dụng của ghi chú (Tình huống 01.1–01.3) không có trang chiếu tương ứng: Tình huống 01.1 dùng MMDS Ví dụ 3.10, Tình huống 01.2 dùng DSC Ch.15 trang chiếu 24–28, 40, Tình huống 01.3 dùng MMDS Ví dụ 1.5.

## Sửa deck theo bảng phát hiện 2026-11-13

Căn cứ: bảng phát hiện "Rà soát deck theo nguyên tắc deck mới và đối chiếu ghi chú bài giảng (2026-11-13)" và "Quyết định của người dùng (2026-11-13)" trong `review-log.md`; quyết định điều phối `edit-decisions.md` (G1–G18, D01); ghi chú `materials/lec-01/lecture-note.md`, `exercises.md` là chuẩn nội dung. Một tác tử sửa ghi tệp; không commit. Mục này thay mục "Sửa toàn diện theo chuẩn 2026-10-14" làm bản hiện hành; các quyết định "không sửa deck trong đợt này" ở phiếu `L01-P04`, `L01-F04` phía trên hết hiệu lực.

**Cấu trúc.** 83 → 100 trang, vẫn bảy section ngoài. Phần giảng 80 trang trong 120 phút (1,5 phút mỗi trang); mạch 5 thành **Đọc thêm** (8 trang, không tính giờ, nhãn `self-study-badge` trên trang Nội dung, dòng dẫn trang tiêu đề mạch và mọi trang nội dung); mạch 7 có 12 trang trong 60 phút. Thêm 17 trang: `A11`, `A12`, `B14`, `B15`, `B16`, `B17`, `B18`, `C19` (tách từ `C17`), `C20`, `C21`, `C23`, `C24`, `F08`, `R07`, `R02B`, `R03B`, `R05B`. Không bỏ trang nào. Đổi thứ tự: mạch 3 theo note:603–776 là `C20` → `C05` → `C08`…`C14` → `C21` → `C07` → `C16` → `C23` → `C24` → `C15` (trang tổng `C05` liền các trang tiêu chí theo ER-003); `D02` lên đầu mạch 4, `D01` về trước `E01`. Bỏ thuộc tính `id="L01-…"` của mọi trang nội dung (giữ `data-slide-id`, giữ `id="mach-N"`).

| Mạch | Tên (khớp trang Nội dung) | Loại | Trang | Phút | Trang mở mạch | Vào → ra |
|---|---|---|---:|---:|---|---|
| 1 | Tổng hợp và tìm kiếm dữ liệu web | giới thiệu | 15 | 25 | bìa `P00` | mô hình RAM → bài toán dữ liệu có ngân sách (Định nghĩa 01.1, 01.2) → cần đơn vị đo |
| 2 | Dòng dữ liệu, nén và truy vấn trên đĩa | khái niệm/mô hình | 19 | 29 | `BT`, trang bài toán có hình `B00` | ngân sách bằng lời → $F$, $2F$, $2mF$ (Mệnh đề 01.5), Định nghĩa 01.7, 01.8 → cần đặc tả chặt |
| 3 | Đặc tả và đánh giá thuật toán | thuật toán, chi phí | 25 | 37,5 | `CT`, trang bài toán có hình `C00` | $R$, Mệnh đề 01.12, 01.15, 01.16 → điều kiện $R\subseteq A$ |
| 4 | Năm nhóm thuật toán và cách học | giới thiệu | 16 | 18 | `DT`, trang bài toán có hình `D02` | ba giới hạn → năm nhóm Bài 02–15, CLO, sản phẩm |
| 5 | Mẫu trùng ngẫu nhiên và suy luận (Đọc thêm) | khái niệm/mô hình | 8 | — | `FT` | mô hình nền → $\mathbb E[X]\approx249\,750$, Hệ quả 01.22 → công cụ của bài tập |
| 6 | Tổng kết và tự kiểm tra | tổng kết | 5 | 10,5 | `GT` | các kết quả → bảng giả thiết, câu trả lời có số |
| 7 | Bài tập vận dụng | thực hành | 12 | 60 | `RT`, trang "Nhắc lại:" có hình `R07` | Bài tập 01.10, 01.11 với trang "Lời giải:" |

Tổng phần giảng: 25 + 29 + 37,5 + 18 + 10,5 = 120 phút. Bài tập: 0,5 + 4 + 1,5 + 5 + 10 + 5 + 7 + 4 + 6 + 4 + 8 + 5 = 60 phút. Thời gian của mạch 5 cũ (14 phút) chuyển cho Định nghĩa 01.1, 01.2, Mục 2.1, Ví dụ 01.4, Định nghĩa 01.8, Bổ đề 01.14, Mệnh đề 01.16; mạch 4 bớt 3 phút (các trang phương pháp còn 1 phút, theo bảng Mục 4.1 của ghi chú).

**Chu trình các cụm.** Khối và lượt quét: `B00` (nhu cầu có số, hình) → `B14` (định nghĩa) → `B15` (ví dụ có số) → `B16` (mệnh đề; chứng minh trong ghi chú diễn giả) → `C09`, `G02` câu 2 (kiểm tra). Xét mọi cặp: `C00`, `C01` (nhu cầu) → `C02` (ví dụ rồi Định nghĩa 01.9) → `C03` (đặc tả) → `C17`, `C19` (chạy tay) → `C04` (Đầu vào/Đầu ra, giả mã, dòng đọc giả mã, câu hỏi) → `C06`, `C18` (tính đúng) → `C20` (giới hạn có số) → `C05`, `C08`–`C14` (mô hình chi phí và các tiêu chí, ER-003) → `C21` (thủ tục trộn) → `C07` (câu chi phí rồi bảng đếm); bước "giới hạn của cách làm trước" không áp dụng vì đây là thuật toán đầu tiên của học phần. Xác minh ứng viên: `C16` (nhu cầu, câu hỏi) → `C23` (mệnh đề, chứng minh) → `C24` (ví dụ) → `C15` (độ thu hồi tại $k$) → `G02` câu 3. Mạch 4 rút gọn: phần định hướng, không giả mã hay chứng minh của Bài 02–15.

**Loại kiểm tra theo mạch.** Mạch 1: `A10` (Bài tập 01.1). Mạch 2: `B12` (Bài tập 01.4). Mạch 3: câu hỏi `C04` (Bài tập 01.5), `C16`. Mạch 4: `D11` (Ví dụ 01.11). Mạch 5: câu hỏi `F07`. Mạch 6: `G02` (Bài tập 01.6, 01.3, 01.7). Mạch 7: Bài tập 01.10, 01.11, mỗi bài có trang đề và trang "Lời giải:" kế tiếp cùng tiêu đề.

**Ngoại lệ mật độ** (đếm bằng `check_deck.py`: token có chữ cái, bỏ tiêu đề, KaTeX, `pre`, hình, ô bảng chỉ có số; số dòng đếm `p`, `li`, hàng bảng kể cả hàng đầu). Trang trần 80: `P03` 78 (đếm tay `wc -w` 78), `P01` 70 và 8 dòng (trang Nội dung), `C05` 73, `C07` 67 và 8 dòng (bảng chi phí), `D07` 79, `D01` 78, `E01` 77, `E02` 63, `E03` 69 và 7 dòng, `F07` 78, `G01` 65, `F04` 70 (trang trả lời vấn đề trung tâm), `G03` 67 (trang nguồn), `R00` 67, `R01` 63, `R03` 62, `R05` 65, `R06` 75 và 7 dòng (đề bài tập). Số dòng: `A01` 8 (bảng dữ kiện bốn hàng, như trước), `C18` 7 (bảng), `C19` 7 (bảng vết). Mọi trang khác ≤ 60 âm tiết và ≤ 6 dòng; mọi dòng ≤ 20 âm tiết trừ câu luận đề bìa (23) và dòng dẫn trang tiêu đề mạch (≤ 23, trần 25). Ghi chú diễn giả trên 150 âm tiết là chứng minh hoặc lời giải: `A10` 192, `B16`, `C18`, `C21`, `C07`, `C23`, `D11` 200, `R05B` (≤ 250).

**Quyết định của điều phối viên (lượt sửa sau kiểm lại, 2026-11-13).**

- *Ngoại lệ ER-004, trang `D05`–`D10`:* người dùng yêu cầu "nhu cầu → cơ chế đại diện → bài sẽ học → bảo đảm" cho mạch 4 (`edit_request.md`, ER-004 mục D), nên mỗi trang giữ **một dòng cơ chế** viết bằng thuật ngữ của ghi chú bài sau và dẫn số khối của bài đó khi có: `D08` Định nghĩa 03.8, `D09` Định nghĩa 07.27, `D05` Định nghĩa 08.22, `D10` Định nghĩa 09.5, `D06` Thuật toán 10.14, `D07` câu chung của nhóm Bài 12–15 (note:893; ghi chú Bài 12–15 chưa có khối đánh số). Từ đợt sửa ghi chú 2026-11-13, ghi chú Bài 01 Mục 4.1 có một câu cơ chế cho mỗi phương pháp (note:876–893) nhưng không dẫn số khối của bài sau; các trang deck giữ số khối đó, mỗi trang một số.
- *Mạch 6 không có trang mở có hình:* `F04` nhắc lại $N=10^6$ bằng số; hình cấu trúc chương của ghi chú (680×640, nhãn 18–25 px) chỉ còn khoảng 13 px khi chiếu.

**Bảng từng trang** (cột "trước" lấy từ `scan/01/density.json` của lượt rà; "—" là trang mới; "phát hiện k" là dòng thứ k, từ 1 đến 30, của bảng phát hiện 2026-11-13 trong `review-log.md`).

| # | Mạch | Mã | Tiêu đề | Quyết định | Âm tiết trước → sau | Trần | Phút | Mục đích, sản phẩm | Lý do |
|---:|---:|---|---|---|---|---:|---:|---|---|
| 1 | 1 | `L01-P00` | Bài toán dữ liệu lớn và mô hình thuật toán | `sửa` | 49 → 47 | — | 0,5 | bìa; luận đề theo ba thành phần của Định nghĩa 01.1 | phát hiện 4: luận đề bốn thành phần lệch note:3 |
| 2 | 1 | `L01-P02` | Tiên quyết và quy ước | `sửa` | 58 → 56 | 60 | 1,5 | nhắc lại tiên quyết đúng note:20–28 (danh sách đã sắp tăng ngặt); ký hiệu $F,M,L$ | phát hiện 17: dòng "Nhắc lại: tiên quyết" không phải kết quả; thiếu bất biến, trộn, $F,M,L$ |
| 3 | 1 | `L01-P03` | Mục tiêu học tập | `sửa` | 80 → 78 | 80 | 1 | bốn mục tiêu theo note:11–14 và dòng Đọc thêm | phát hiện 1, 6; đếm tay 78 âm tiết |
| 4 | 1 | `L01-P01` | Nội dung | `sửa` | 68 → 70 | 80 | 0,5 | nội dung bảy mạch; mạch 5 mang nhãn Đọc thêm | D01; ngoại lệ 8 dòng của trang Nội dung giữ |
| 5 | 1 | `L01-P04` | Vấn đề trung tâm | `sửa` | 59 → 45 | 60 | 2 | ba câu hỏi của note:85–89 | phát hiện 1, 7 |
| 6 | 1 | `L01-A01` | Tính tổng kích thước trang web theo máy chủ | `sửa` | 50 → 51 | 60 | 2 | Ví dụ 01.1, Đầu vào theo tệp siêu dữ liệu | phát hiện 15, 27 (bỏ $D$, $M$ khỏi ghi chú diễn giả); 8 dòng kể cả bảng như trước |
| 7 | 1 | `L01-A11` | Bài toán dữ liệu | `thêm` | — → 60 | 60 | 3 | Định nghĩa 01.1 đọc trên Ví dụ 01.1; phản ví dụ trong ghi chú diễn giả | phát hiện 4 (nghiêm trọng) |
| 8 | 1 | `L01-A02` | Đếm số lần xuất hiện của từng từ | `sửa` | 36 → 36 | 60 | 1,5 | đếm từ; Nhận xét 01.3 vào ghi chú diễn giả | phát hiện 15 |
| 9 | 1 | `L01-A03` | Tính điểm quan trọng của trang web | `sửa` | 43 → 47; 47 → 47 | 60 | 1,5 | PageRank: trở ngại theo bảng note:146 | phát hiện 14, 15; sửa theo ghi chú 2026-11-13: nguồn đồ thị y, a, m là trang chiếu MMDS, *Link Analysis* 1, tr.19 (note:152), mặt trang không đổi |
| 10 | 1 | `L01-A04` | Ưu tiên kết quả tìm kiếm theo chủ đề | `sửa` | 41 → 50 | 60 | 1,5 | xếp hạng theo chủ đề: trở ngại theo note:147 | phát hiện 15 |
| 11 | 1 | `L01-A05` | Hạn chế liên kết rác trong xếp hạng | `sửa` | 46 → 44 | 60 | 1,5 | liên kết rác: trở ngại theo note:148 | phát hiện 15 |
| 12 | 1 | `L01-A06` | Tìm các cặp tài liệu gần trùng | `sửa` | 36 → 30 | 60 | 2 | cặp gần trùng, $N=10^6$ | phát hiện 15, 23 |
| 13 | 1 | `L01-A07` | Tìm đoạn tài liệu bằng véc-tơ truy vấn | `sửa` | 44 → 40 | 60 | 1,5 | $k$ hàng xóm; Ví dụ 01.2 ($122{,}88$ TB) trong ghi chú diễn giả | phát hiện 15 (câu BIODS "không phải số đo") |
| 14 | 1 | `L01-A12` | Tập $k$ hàng xóm gần nhất chính xác | `thêm` | — → 38 | 60 | 2 | Định nghĩa 01.2 với ví dụ phá hòa $n=3,k=1$ | phát hiện 4 (nghiêm trọng) |
| 15 | 1 | `L01-A10` | Câu hỏi về bảy bài toán trên kho web | `sửa` | 44 → 48 | 60 | 3 | Bài tập 01.1; lời giải và hướng dẫn chấm | câu hỏi dẫn Định nghĩa 01.1 |
| 16 | 2 | `L01-BT` | 2. Dòng dữ liệu, nén và truy vấn trên đĩa | `sửa` | 38 → 40 | — | 0,5 | trang tiêu đề mạch 2; từ khóa mới | khối và lượt quét đứng đầu mạch |
| 17 | 2 | `L01-B00` | Tệp 1 TB và bộ nhớ 1 GB | `sửa` | 61 → 58 | 60 | 1 | trang bài toán có hình: tệp 1 TB, bộ nhớ 1 GB; ba nhóm | phát hiện 9; giữ chức năng ER-002 |
| 18 | 2 | `L01-B14` | Khối, lần truyền khối và lượt quét | `thêm` | — → 54 | 60 | 2 | Định nghĩa 01.4 | phát hiện 3 (nghiêm trọng), 10(a) |
| 19 | 2 | `L01-B15` | Ví dụ: tệp 1 TB | `thêm` | — → 53 | 60 | 2,5 | Ví dụ 01.3: $F=15\,258\,790$, $2{,}78$ giờ, $1{,}77$ ngày | phát hiện 3 |
| 20 | 2 | `L01-B16` | Chi phí của lượt quét | `thêm` | — → 56 | 60 | 3 | Mệnh đề 01.5 ($F$, $2F$, $2mF$); chứng minh và phản ví dụ trong ghi chú diễn giả | phát hiện 3 |
| 21 | 2 | `L01-B01` | Giữ mẫu truy vấn và lọc thư đến | `sửa` | 50 → 49 | 60 | 1,5 | số liệu $10^9$ địa chỉ, 20 GB, $1/10$ bản ghi | phát hiện 12, 14 (bỏ tính chất Bloom) |
| 22 | 2 | `L01-B17` | Ví dụ: mẫu theo từng truy vấn | `thêm` | — → 59 | 60 | 2,5 | Ví dụ 01.4: $\mu_2/(10\mu_1+19\mu_2)$, $1/29$ so với $1/2$ | phát hiện 12 |
| 23 | 2 | `L01-B02` | Đếm người dùng và lần truy cập gần đây | `sửa` | 39 → 54 | 60 | 1,5 | "lần truy cập", cửa sổ (window) | phát hiện 8(6), 15 |
| 24 | 2 | `L01-B10` | Nén dữ liệu để lưu và khôi phục | `sửa` | 39 → 58 | 60 | 1,5 | Định nghĩa 01.7 thay hai thẻ | phát hiện 12 |
| 25 | 2 | `L01-B03` | Lưu văn bản với ít dung lượng hơn | `sửa` | 34 → 37 | 60 | 1 | chuỗi 13 ký tự; bỏ câu ngoài ghi chú | phát hiện 14, 15 |
| 26 | 2 | `L01-B04` | Giảm dung lượng ảnh với sai số cho phép | `sửa` | 39 → 39 | 60 | 1 | lượng tử hóa; hai đại lượng phải báo | phát hiện 15 |
| 27 | 2 | `L01-B11` | Xử lý và truy vấn dữ liệu trên đĩa | `sửa` | 58 → 59 | 60 | 0,5 | "Nhắc lại:" Định nghĩa 01.4; ba nhóm truy vấn | phát hiện 3, 10(a): khối không còn định nghĩa ở đây |
| 28 | 2 | `L01-B05` | Sắp xếp tệp lớn theo khóa | `sửa` | 47 → 47 | 60 | 1 | DSC $2F$ mỗi lượt, lượt cuối $F$ trong ghi chú diễn giả | phát hiện 15 |
| 29 | 2 | `L01-B06` | Tìm hồ sơ giảng viên theo mã hoặc lương | `sửa` | 39 → 39 | 60 | 1 | truy vấn theo mã, theo khoảng | phát hiện 15 |
| 30 | 2 | `L01-B18` | Hàm băm và chỉ mục băm | `thêm` | — → 56 | 60 | 2 | Định nghĩa 01.8 và Ví dụ 01.5; Tình huống 01.3 trong ghi chú diễn giả | phát hiện 12 |
| 31 | 2 | `L01-B07` | Tìm tài liệu chứa đồng thời hai từ khóa | `sửa` | 33 → 33 | 60 | 1 | chỉ mục đảo; bỏ đính chính PPTX | phát hiện 16 |
| 32 | 2 | `L01-B08` | Tìm đối tượng giao vùng trên bản đồ | `sửa` | 38 → 38 | 60 | 1 | hộp bao; bỏ lời chú người soạn | phát hiện 15, 16 |
| 33 | 2 | `L01-B09` | Ghép sinh viên với các môn đã đăng ký | `sửa` | 44 → 43 | 60 | 1,5 | $M=20$ khối (DSC trang chiếu 40); Tình huống 01.2 trong ghi chú diễn giả | phát hiện 8(6), 16 |
| 34 | 2 | `L01-B12` | Câu hỏi về dòng, nén và truy vấn trên đĩa | `sửa` | 51 → 53 | 60 | 3 | Bài tập 01.4(a, b) và câu nối bảng; "lần truyền khối" | phát hiện 8(3), 15 |
| 35 | 3 | `L01-CT` | 3. Đặc tả và đánh giá thuật toán | `sửa` | 38 → 43 | — | 0,5 | trang tiêu đề mạch 3; ghi chú 97 âm tiết | phát hiện 21 |
| 36 | 3 | `L01-C00` | Phân tích thuật toán xử lý dữ liệu lớn | `sửa` | 39 → 34 | 60 | 1 | trang bài toán có hình (ER-003 giữ): $N=10^6$, $499\,999\,500\,000$ cặp | phát hiện 9 |
| 37 | 3 | `L01-C01` | Bài toán tìm cặp tài liệu gần trùng | `sửa` | 49 → 59 | 60 | 1 | nhu cầu và đoạn ký tự; bỏ hình (đã lên C00) | tránh hai hình giống nhau liền nhau |
| 38 | 3 | `L01-C02` | Độ tương đồng Jaccard | `sửa` | 46 → 34 | 60 | 2,5 | Ví dụ 01.6, Định nghĩa 01.9 với $\mathrm{SIM}$, $C_1,C_2$; hình danh-gia-jaccard-c.svg | phát hiện 8(1), (2), 30 |
| 39 | 3 | `L01-C03` | Đặc tả tìm cặp gần trùng | `sửa` | 30 → 30 | 60 | 2,5 | Định nghĩa 01.10 với $\mathrm{SIM}$ | phát hiện 8, 30 |
| 40 | 3 | `L01-C17` | Ví dụ: thứ tự xét cặp | `sửa` | 22 → 22 | 60 | 1 | Ví dụ 01.7(a), dòng "Tính …" | phát hiện 11, 25 |
| 41 | 3 | `L01-C19` | Ví dụ: thứ tự xét cặp, vết chạy với $N=3$ | `tách` | — → 42 | 60 | 2,5 | Ví dụ 01.7(b): bảng vết $N=3$, $\tau=1/2$; tách từ C17 | phát hiện 11; bảng vết 7 dòng |
| 42 | 3 | `L01-C04` | Thuật toán: xét mọi cặp | `sửa` | 29 → 42 | 60 | 2 | Thuật toán 01.11 với $\mathrm{SIM}$, đánh số dòng, dòng đọc giả mã | phát hiện 8, 30; cụm thuật toán |
| 43 | 3 | `L01-C06` | Tính đúng: bất biến của xét mọi cặp | `sửa` | 39 → 34 | 60 | 2 | Mệnh đề 01.12; bất biến $\mathcal O_\ell=R\cap\mathcal S_\ell$ | phát hiện 30 |
| 44 | 3 | `L01-C18` | Tính đúng: khởi tạo, duy trì, kết thúc | `sửa` | 60 → 43 | 80 | 2 | Tính đúng: bảng bốn hàng (thêm "mỗi cặp một vòng") | bảng 7 dòng kể cả hàng đầu |
| 45 | 3 | `L01-C20` | Một triệu chữ ký trong bộ nhớ | `thêm` | — → 49 | 60 | 1,5 | MMDS Ví dụ 3.10: $15\,259$ khối, $5{,}79$ ngày | phát hiện 5, 10(b) |
| 46 | 3 | `L01-C05` | Các tiêu chí đánh giá | `sửa` | 68 → 73 | 80 | 1 | Định nghĩa 01.13 + bảng bốn nhóm; chuyển sau C20 | phát hiện 10(b), 21 |
| 47 | 3 | `L01-C08` | Bộ nhớ làm việc | `sửa` | 30 → 35 | 60 | 1 | định nghĩa theo Định nghĩa 01.13 | phát hiện 15 |
| 48 | 3 | `L01-C09` | Đọc ghi và số lượt quét | `sửa` | 37 → 26 | 60 | 1 | "Nhắc lại:" Mệnh đề 01.5; Bài tập 01.3 trong ghi chú diễn giả | phát hiện 3, 10(a) |
| 49 | 3 | `L01-C10` | Dữ liệu truyền qua mạng | `sửa` | 37 → 55 | 60 | 1 | chi phí truyền thông CS246 (note:708) thay "MMDS 2.5" | phát hiện 14, 23 |
| 50 | 3 | `L01-C11` | Độ trễ truy vấn | `sửa` | 28 → 33 | 60 | 0,5 | độ trễ và thông lượng theo note:630 | phát hiện 14 |
| 51 | 3 | `L01-C12` | Chi phí xây dựng chỉ mục | `sửa` | 29 → 30 | 60 | 0,5 | định nghĩa theo note:625; bỏ câu kết châm ngôn | phát hiện 20, 23 |
| 52 | 3 | `L01-C13` | Chi phí cập nhật dữ liệu | `sửa` | 36 → 37 | 60 | 0,5 | định nghĩa theo note:626 | phát hiện 14, 15, 16 |
| 53 | 3 | `L01-C14` | Dung lượng lưu trữ | `sửa` | 36 → 38 | 60 | 0,5 | định nghĩa theo note:623 | phát hiện 15 |
| 54 | 3 | `L01-C21` | Thủ tục trộn đếm giao và hợp | `thêm` | — → 50 | 60 | 2,5 | Bổ đề 01.14 (thủ tục trộn, điều kiện lặp); chứng minh trong ghi chú diễn giả; đặt sau C14 | phát hiện 5 |
| 55 | 3 | `L01-C07` | Chi phí: xét mọi cặp | `sửa` | 59 → 67 | 80 | 2,5 | Mệnh đề 01.15, bảng bốn hàng note:681–686, Ví dụ 01.8 | phát hiện 5, 8(5), 18; bảng chi phí 8 dòng |
| 56 | 3 | `L01-C16` | Cặp ứng viên và bước xác minh | `sửa` | 31 → 42 | 60 | 1,5 | cặp ứng viên, xác minh; câu hỏi | phát hiện 2, 8(4), 10(c), 15 |
| 57 | 3 | `L01-C23` | Xác minh ứng viên | `thêm` | — → 44 | 60 | 2,5 | Mệnh đề 01.16 với chứng minh một dòng | phát hiện 2 (nghiêm trọng) |
| 58 | 3 | `L01-C24` | Ví dụ: một cặp sai bị loại, một cặp đúng bị bỏ sót | `thêm` | — → 57 | 60 | 2,5 | Ví dụ 01.9; FP, FN; độ thu hồi $1/2$ | phát hiện 2 |
| 59 | 3 | `L01-C15` | Chất lượng kết quả gần đúng | `sửa` | 33 → 30 | 60 | 1,5 | Định nghĩa 01.17, Ví dụ 01.10; chuyển cuối mạch | phát hiện 8(7), 10(c), 19 |
| 60 | 4 | `L01-DT` | 4. Năm nhóm thuật toán và cách học | `sửa` | 41 → 40 | — | 0,5 | trang tiêu đề mạch 4; ghi chú 74 âm tiết | phát hiện 21 |
| 61 | 4 | `L01-D02` | Ba giới hạn và năm nhóm bài | `sửa` | 0 → 32 | 60 | 1,5 | trang bài toán có hình: ba giới hạn có số + bản đồ; chuỗi tiên quyết trong ghi chú diễn giả | phát hiện 9, 10(d), 28 |
| 62 | 4 | `L01-D03` | MapReduce: gom kết quả theo khóa | `sửa` | 44 → 46 | 60 | 1 | Bài 02 theo bảng note:851; "khóa" in nghiêng | phát hiện 14, 23, 24 |
| 63 | 4 | `L01-D08` | PageRank: tính điểm theo liên kết | `sửa` | 50 → 48; 48 → 48 | 60 | 1 | Bài 03–04 theo bảng note:852–853; một dòng cơ chế (Định nghĩa 03.8), ngoại lệ ER-004 | phát hiện 14 (bỏ bước nhảy ngẫu nhiên, cơ chế HITS); sửa theo ghi chú 2026-11-13: thêm nguồn đồ thị y, a, m vào ghi chú diễn giả, mặt trang không đổi |
| 64 | 4 | `L01-D04` | MinHash và LSH: chọn cặp cần đối chiếu | `sửa` | 50 → 53 | 60 | 1 | Bài 05–06 theo note:854–855, 869 | phát hiện 8(4), 14 (bỏ hoán vị) |
| 65 | 4 | `L01-D09` | Chỉ mục cho truy vấn véc-tơ | `sửa` | 47 → 60; 60 → 60; 60 → 60; 60 → 60 | 60 | 1 | Bài 07 theo note:856; HNSW, PQ in nghiêng, một dòng cơ chế mỗi phương pháp (Định nghĩa 07.27), ngoại lệ ER-004 | phát hiện 14, 24; sửa theo ghi chú 2026-11-13: HNSW tìm tham lam ở các tầng trên, tầng 0 tìm kiếm chùm ghi trong ghi chú diễn giả (note:882, Thuật toán 07.17); PQ: "thay đoạn tọa độ bằng chỉ số véc-tơ đại diện gần nhất" (note:883), Định nghĩa 07.27 chuyển vào ghi chú diễn giả; dòng HNSW giữ "ở các tầng trên"; dòng Bài 07 "không quét kho" để giữ trần 60; ghi chú diễn giả 149 âm tiết |
| 66 | 4 | `L01-D05` | Lấy mẫu và lọc trên dòng dữ liệu | `sửa` | 41 → 59; 59 → 60 | 60 | 1 | Bài 08 theo note:857; một dòng cơ chế Bloom (Định nghĩa 08.22), ngoại lệ ER-004 | phát hiện 14; sửa theo ghi chú 2026-11-13: bỏ $k$ (trong Bài 01, $k$ là số hàng xóm), bit 0 ở vị trí băm; câu cơ chế đầy đủ trong ghi chú diễn giả (note:886) |
| 67 | 4 | `L01-D10` | Cấu trúc gọn cho thống kê dòng | `sửa` | 62 → 58; 58 → 59 | 60 | 1 | Bài 09 theo note:858; một dòng cơ chế Flajolet–Martin (Định nghĩa 09.5), ngoại lệ ER-004 | phát hiện 14, 22; sửa theo ghi chú 2026-11-13: bỏ $R$, $2^R$ (trong Bài 01, $R$ là tập cặp đạt ngưỡng); "2 mũ độ dài đuôi lớn nhất"; định nghĩa đuôi trong ghi chú diễn giả (note:887) |
| 68 | 4 | `L01-D06` | Nén theo ký hiệu, mẫu lặp và ảnh | `sửa` | 64 → 50; 50 → 70 | 80 | 1 | Bài 10–11 theo note:859–860; hai dòng cơ chế Huffman (Thuật toán 10.14), ngoại lệ ER-004 | phát hiện 14 (bỏ DCT); sửa theo ghi chú 2026-11-13: lá là ký hiệu, trọng số là số lần xuất hiện, nút cha mang tổng (note:890); hai dòng ≤ 20 âm tiết, trang bảng so sánh trần 80, 5 dòng; từ mã trong ghi chú diễn giả |
| 69 | 4 | `L01-D07` | Tổ chức dữ liệu để giảm đọc ghi | `sửa` | 77 → 79 | 80 | 1 | Bài 12–15 theo note:861–864; dòng cơ chế theo note:872, ngoại lệ ER-004 | bảng 6 dòng |
| 70 | 4 | `L01-D01` | Học phần và năng lực cần đạt | `sửa` | 36 → 78 | 80 | 1 | CLO1–CLO4 (note:899–904); chuyển sau D07 | phát hiện 10(d), 22, 28 |
| 71 | 4 | `L01-E01` | Kiến thức nền dùng ở từng nhóm bài | `sửa` | 79 → 77 | 80 | 1 | bảng kiến thức nền theo note:908–914 | phát hiện 15 |
| 72 | 4 | `L01-E02` | Sản phẩm khi phân tích thuật toán | `sửa` | 77 → 63 | 80 | 1,5 | bốn sản phẩm theo note:920–923; vết $N=3$ | phát hiện 8(2), 11, 14, 22 |
| 73 | 4 | `L01-E06` | Báo cáo chất lượng và hiệu năng | `sửa` | 41 → 43 | 60 | 1 | báo cáo thực nghiệm theo note:924 | phát hiện 15 |
| 74 | 4 | `L01-E03` | Tự học, hợp tác và trách nhiệm dữ liệu | `sửa` | 79 → 69 | 80 | 1 | trách nhiệm CLO4 theo note:928 | phát hiện 15; bảng 7 dòng |
| 75 | 4 | `L01-D11` | Câu hỏi về nhóm bài và kiến thức nền | `sửa` | 34 → 41 | 60 | 2,5 | Ví dụ 01.11, Bài tập 01.8 | lời giải theo ghi chú |
| 76 | 5 | `L01-FT` | 5. Mẫu trùng ngẫu nhiên và suy luận | `sửa` | 37 → 40 | — | Đọc thêm | trang tiêu đề mạch 5, nhãn Đọc thêm | D01, phát hiện 1, 21 |
| 77 | 5 | `L01-F01` | Tìm mẫu trùng trong hồ sơ lưu trú | `sửa` | 47 → 50 | 60 | Đọc thêm | Đọc thêm; câu kết theo note:958 | D01, phát hiện 15, 23 |
| 78 | 5 | `L01-F02` | Mô hình lưu trú không phối hợp | `sửa` | 41 → 44 | 80 | Đọc thêm | Đọc thêm; Định nghĩa 01.18 | D01, phát hiện 15 |
| 79 | 5 | `L01-F05` | Xác suất trùng một ngày và hai ngày | `sửa` | 26 → 30 | 60 | Đọc thêm | Đọc thêm; Ví dụ 01.12 | D01 |
| 80 | 5 | `L01-F06` | Đơn vị đếm và số phép thử | `sửa` | 37 → 48 | 60 | Đọc thêm | Đọc thêm; Định nghĩa 01.19, Ví dụ 01.14 | D01, phát hiện 15 |
| 81 | 5 | `L01-F03` | Kỳ vọng số biến cố trùng | `sửa` | 44 → 27 | 60 | Đọc thêm | Đọc thêm; Mệnh đề 01.20, Ví dụ 01.13 | D01, phát hiện 23 |
| 82 | 5 | `L01-F08` | Bất đẳng thức Markov | `thêm` | — → 30 | 60 | Đọc thêm | Đọc thêm; Bổ đề 01.21, Hệ quả 01.22; trường hợp ba ngày ($X_c$) trong ghi chú diễn giả | D01: Hệ quả 01.22 cần cho bài tập |
| 83 | 5 | `L01-F07` | Mẫu trùng và căn cứ suy luận | `sửa` | 71 → 78 | 80 | Đọc thêm | Đọc thêm; bảng Nhận xét 01.23 | D01 |
| 84 | 6 | `L01-GT` | 6. Tổng kết và tự kiểm tra | `sửa` | 40 → 42 | — | 0,5 | trang tiêu đề mạch 6 | phát hiện 22 |
| 85 | 6 | `L01-G01` | Kết quả và giả thiết không được bỏ | `sửa` | 79 → 65 | 80 | 2,5 | năm kết quả cốt lõi; bỏ hàng kỳ vọng (Đọc thêm) | phát hiện 1, 18 |
| 86 | 6 | `L01-F04` | Câu trả lời cho vấn đề trung tâm | `sửa` | 78 → 70 | 80 | 3 | ba câu trả lời có số theo P04 | phát hiện 1, 7 |
| 87 | 6 | `L01-G02` | Câu hỏi tự kiểm tra | `sửa` | 50 → 55 | 60 | 3,5 | Bài tập 01.6, 01.3, 01.7 | phát hiện 1 (câu 3), 8 |
| 88 | 6 | `L01-G03` | Nguồn và tài liệu đọc | `sửa` | 70 → 67 | 80 | 1 | BHK 04/01/2018, CLRS 4e, liên kết bài tập, Bài 02 | phát hiện 22, 29 |
| 89 | 7 | `L01-RT` | 7. Bài tập vận dụng | `sửa` | 34 → 36 | — | 0,5 | trang tiêu đề mạch 7 | phát hiện 13 |
| 90 | 7 | `L01-R07` | Mô hình lưu trú và cận xác suất | `thêm` | — → 52 | 60 | 4 | một nhãn "Nhắc lại:" cho danh sách bốn ý: mô hình, $p$, $\mathbb E[X]$, Hệ quả 01.22; có hình | D01 |
| 91 | 7 | `L01-R00` | Bài tập: phép đếm và suy luận | `sửa` | 65 → 67 | 80 | 1,5 | Bài tập 01.10, 01.11 | phát hiện 30 |
| 92 | 7 | `L01-R01` | Bài tập: hồ sơ lưu trú, ba biến thể | `sửa` | 56 → 63 | 80 | 5 | đề Bài tập 01.10 (MMDS 1.2.1) với yêu cầu Hệ quả 01.22 | phát hiện 13, 30 |
| 93 | 7 | `L01-R02` | Bài tập: hồ sơ lưu trú (a), (b) | `sửa` | 52 → 53 | 80 | 10 | đề (a), (b); hướng dẫn chấm | phát hiện 13 |
| 94 | 7 | `L01-R02B` | Bài tập: hồ sơ lưu trú (a), (b) | `thêm` | — → 34 | 60 | 5 | Lời giải (a), (b) theo ex:32–57 | phát hiện 13 |
| 95 | 7 | `L01-R03` | Bài tập: hồ sơ lưu trú (c) | `sửa` | 51 → 62 | 80 | 7 | đề (c); hướng dẫn chấm | phát hiện 13 |
| 96 | 7 | `L01-R03B` | Bài tập: hồ sơ lưu trú (c) | `thêm` | — → 39 | 60 | 4 | Lời giải (c), cận $0{,}0831$ | phát hiện 13 |
| 97 | 7 | `L01-R04` | Bài tập: cặp người mua cùng tập mặt hàng | `sửa` | 46 → 60 | 80 | 6 | đề Bài tập 01.11; "lần mua", giả thuyết làm việc | phát hiện 8(6), 16, 30 |
| 98 | 7 | `L01-R06` | Bài tập: tập mặt hàng, đơn vị đếm | `sửa` | 74 → 75 | 80 | 4 | đơn vị đếm; "lần mua" | phát hiện 8(6), 16; bảng 7 dòng |
| 99 | 7 | `L01-R05` | Bài tập: tập mặt hàng, bốn phần lời giải | `sửa` | 56 → 65 | 80 | 8 | đề bốn phần; hướng dẫn chấm | phát hiện 13 |
| 100 | 7 | `L01-R05B` | Bài tập: tập mặt hàng, bốn phần lời giải | `thêm` | — → 48 | 60 | 5 | Lời giải Bài tập 01.11 theo ex:81–100 | phát hiện 13 |

**Phiếu trang mới** (mạch; mục đích; hành động của sinh viên; đối tượng trung tâm; dữ kiện kế thừa; kiến thức đầu vào; sản phẩm; bằng chứng; quyết định).

- `L01-A11` Bài toán dữ liệu — 1; nêu Định nghĩa 01.1; đọc ba thành phần trên bốn dòng của Ví dụ 01.1; $\mathcal I$, $\mathrm{Out}(I)$, ngân sách; bảng `A01`; khái niệm bài toán tính toán (CLRS §1.1); $\mathrm{Out}(I)$ của ví dụ; `A10`, ba phản ví dụ trong ghi chú diễn giả; `thêm`.
- `L01-A12` Tập $k$ hàng xóm gần nhất chính xác — 1; nêu Định nghĩa 01.2 với quy tắc phá hòa; áp quy tắc cho $n=3$, $k=1$; $\mathcal N_k(\mathbf y)$; kho véc-tơ của `A07`; khoảng cách, thứ tự từ điển; $\mathcal N_1(\mathbf y)=\{1\}$; `C15` dùng lại $\mathcal N_k$; `thêm`.
- `L01-B14` Khối, lần truyền khối và lượt quét — 2; nêu Định nghĩa 01.4; phân biệt khối, lần truyền khối, lượt quét; mô hình chi phí đọc ghi; tệp 1 TB của `B00`; mô hình RAM; định nghĩa bằng lời; `B15`, `B16`; `thêm`.
- `L01-B15` Ví dụ: tệp 1 TB — 2; Ví dụ 01.3; tính $F$ và hai thời gian đọc; $F=15\,258\,790$; số liệu đĩa MMDS §1.3.4; phép làm tròn lên; $2{,}78$ giờ, $1{,}77$ ngày; dòng kiểm trong ghi chú diễn giả; `thêm`.
- `L01-B16` Chi phí của lượt quét — 2; Mệnh đề 01.5; áp (a)–(c) cho một số lượt; $F$, $2F$, $2mF$; Định nghĩa 01.4; đếm; công thức; `C09`, `G01`, `G02` câu 2; `thêm`.
- `L01-B17` Ví dụ: mẫu theo từng truy vấn — 2; Ví dụ 01.4; tính tỷ số trên mẫu; $\mu_2/(10\mu_1+19\mu_2)$; nhu cầu của `B01`; xác suất độc lập, kỳ vọng; $1/29\ne1/2$; `D05` dùng lại; `thêm`.
- `L01-B18` Hàm băm và chỉ mục băm — 2; Định nghĩa 01.8, Ví dụ 01.5; tra một khóa qua thùng; $h$, $B$; nhu cầu tra theo mã của `B06`; bảng băm (tiên quyết); thùng 17; Tình huống 01.3 trong ghi chú diễn giả; `thêm`.
- `L01-C19` Ví dụ: thứ tự xét cặp, vết chạy với $N=3$ — 3; Ví dụ 01.7(b); điền bảng vết; $R\cap\mathcal S_\ell$; $C_1,C_2$ của `C02`, $C_3=C_1$; đặc tả `C03`; $R=\{(1,3)\}$; `C06` (bất biến), `E02`; `tách` từ `C17`.
- `L01-C20` Một triệu chữ ký trong bộ nhớ — 3; MMDS Ví dụ 3.10, giới hạn có số trước mô hình chi phí; xác định đại lượng giới hạn; bộ nhớ, đọc ghi, tính toán; $N=10^6$, Mệnh đề 01.5(a); $\binom N2$; $5{,}79$ ngày; `C05`, `F04`; `thêm`.
- `L01-C21` Thủ tục trộn đếm giao và hợp — 3 (sau `C14`); Bổ đề 01.14 với điều kiện lặp; chạy thủ tục trên hai danh sách; $\gamma$; danh sách tăng ngặt (`P02`); trộn hai danh sách đã sắp; cận $|C|+|C'|$; `C07`; `thêm`.
- `L01-C23` Xác minh ứng viên — 3; Mệnh đề 01.16; chứng minh (a)–(c); $\widehat R=A\cap R$; câu hỏi `C16`; $R$ của `C03`; điều kiện $R\subseteq A$; `C24`, `G02` câu 3; `thêm`.
- `L01-C24` Ví dụ: một cặp sai bị loại, một cặp đúng bị bỏ sót — 3; Ví dụ 01.9; tính $\widehat R$ và độ thu hồi; FP, FN; `C23`; Mệnh đề 01.16; $1/2$; `C15`, `D04`; `thêm`.
- `L01-F08` Bất đẳng thức Markov — 5 (Đọc thêm); Bổ đề 01.21, Hệ quả 01.22; chặn $\Pr(X\ge1)$; $\mathbb E[X]$ của `F03`; kỳ vọng; $0{,}0831$; `R07`, `R03B`; `thêm`.
- `L01-R07` Mô hình lưu trú và cận xác suất — 7; trang "Nhắc lại:" đầu mạch bài tập (D01), một nhãn cho danh sách bốn ý; đối chiếu mô hình với đề; $P,T,H,q$, $\mathbb E[X]$, Hệ quả 01.22; phần đọc thêm; xác suất rời rạc; bảng công cụ; `R01`–`R05B`; `thêm`.
- `L01-R02B`, `L01-R03B`, `L01-R05B` (trang "Lời giải:" cùng tiêu đề với `R02`, `R03`, `R05`) — 7; lời giải khớp `exercises.md` (Bài tập 01.10, 01.11); so lời giải của nhóm; số phép thử, xác suất, kỳ vọng, cận Hệ quả 01.22; đề ở trang trước; `R07`; lời giải có số; hướng dẫn chấm theo bước trong ghi chú diễn giả; `thêm`.

**Ánh xạ chủ đề của ghi chú sau đợt sửa** (thay bảng "Ánh xạ chủ đề của ghi chú (đợt B1, 2026-11-11)" ở cột trang chiếu).

| note-topic-id | Mục ghi chú | Trang chiếu (`data-slide-id`) |
|---|---|---|
| `lec-01-topic-01` | Mục 1 | L01-P00, P02, P03, P01, P04, A01, A11, A02–A07, A12, A10 |
| `lec-01-topic-02` | Mục 2 | L01-BT, B00, B14, B15, B16, B01, B17, B02, B10, B03, B04, B11, B05, B06, B18, B07, B08, B09, B12 |
| `lec-01-topic-03` | Mục 3.1–3.3 | L01-CT, C00, C01, C02, C03, C17, C19, C04, C06, C18 |
| `lec-01-topic-04` | Mục 3.4–3.5 | L01-C20, C05, C08–C14, C21, C07, C16, C23, C24, C15 |
| `lec-01-topic-05` | Mục 4.1 | L01-DT, D02, D03, D08, D04, D09, D05, D10, D06, D07 |
| `lec-01-topic-06` | Mục 4.2 | L01-D01, E01, E02, E06, E03, D11 |
| `lec-01-topic-07` | Đọc thêm | L01-FT, F01, F02, F05, F06, F03, F08, F07 |
| `lec-01-topic-08` | Bài tập củng cố; `exercises.md` | L01-RT, R07, R00, R01, R02, R02B, R03, R03B, R04, R06, R05, R05B |

Tóm tắt chương ứng với L01-GT, G01, F04, G02, G03. Tình huống 01.1 có trang `C20`; Tình huống 01.2 nằm trong ghi chú diễn giả `B09`, `B12`; Tình huống 01.3 trong ghi chú diễn giả `B18`.
