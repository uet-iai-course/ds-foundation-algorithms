# Storyboard Bài 02: MapReduce và ngăn xếp xử lý dữ liệu lớn

## Bản viết mới theo `ch2n.pdf` — 2026-09-14

Phương án này thay đề xuất ngày 2026-09-13. Nguồn nội dung và thứ tự chính là [Chương 2 do người dùng chỉ định](../../../sources/textbooks/ch2n.pdf), *MapReduce and the New Software Stack*, 60 trang PDF, trang in 20–79. Bài vẫn mang số 02 theo `sources/source.md`. Đối tượng được chốt là sinh viên năm 2.

Người dùng đã yêu cầu viết lại toàn bộ lecture 02. HTML và ghi chú được soạn mới từ chương 2; chỉ kế thừa nền kỹ thuật của mẫu học phần. Outline và review-log được cập nhật cho bản này. Không tiếp tục dùng cấu trúc bảy mạch hoặc quy định loại nhân ma trận và phép nối trong plan cũ.

## Cấu trúc và mức độ

Mỗi section ngoài sau phần mở đầu tương ứng đúng một mục cấp 2.x của PDF. Không chia một mục PDF thành nhiều section ngoài, không ghép hai mục PDF vào một section. Chín section là ngoại lệ có chủ ý so với quy ước 5–7, để thực hiện yêu cầu mới của người dùng.

| Section ngoài | Căn cứ PDF | Trang in / trang PDF | Số trang giảng | Phút giảng |
|---|---|---|---:|---:|
| 1. Mở đầu | Phần dẫn chương và mục tiêu học phần | 21–22 / 2–3 | 3 | 5 |
| 2. Hệ tệp phân tán | 2.1 | 22–24 / 3–5 | 3 | 10 |
| 3. Mô hình MapReduce | 2.2 | 25–30 / 6–11 | 7 | 18 |
| 4. Các thuật toán dùng MapReduce | 2.3 | 30–40 / 11–21 | 10 | 30 |
| 5. Mở rộng MapReduce | 2.4 | 41–53 / 22–34 | 5 | 12 |
| 6. Mô hình chi phí truyền thông | 2.5 | 53–60 / 34–41 | 9 | 27 |
| 7. Đánh đổi bộ nhớ và sao chép dữ liệu | 2.6 | 61–74 / 42–55 | 4 | 12 |
| 8. Tổng kết chương | 2.7 | 74–77 / 55–58 | 2 | 5 |
| 9. Tài liệu tham khảo | 2.8 | 77–79 / 58–60 | 1 | 1 |
| **Tổng phần giảng** | | | **44** | **120** |

Bám cấu trúc chương không có nghĩa giảng mọi tiểu mục với cùng độ sâu. Trong 120 phút, cần dành thời gian cho chạy tay và giải thích; các chứng minh cận dưới dài, chi tiết nhân ma trận–ma trận và hệ thống mở rộng được chỉ rõ là đọc thêm. Bài tập có 60 phút riêng, mô tả ở cuối storyboard.

### Cách thể hiện phù hợp với sinh viên năm 2

Giả định sinh viên đã biết vòng lặp, hàm, bảng băm, tổng hữu hạn và phép nhân ma trận–vector cơ bản. Không mặc định đã học hệ phân tán, đại số quan hệ, Spark hoặc phương pháp nhân tử Lagrange. Khôi phục kiến thức cần dùng ngay trước nơi dùng: hàng/cột/khóa của bảng, chỉ số ma trận, phép nhóm và phép cộng tổng cục bộ.

| Nội dung | Trình tự thể hiện | Mức sinh viên cần đạt |
|---|---|---|
| Khái niệm hệ thống | Một nhu cầu cụ thể → hình có nhãn → tên khái niệm → trách nhiệm và giới hạn | Đọc được sơ đồ và giải thích cơ chế |
| Thuật toán trọng tâm | Bài toán dữ liệu lớn → đầu vào/đầu ra → trực giác → ví dụ chạy tay → khóa và giả mã → lập luận đúng → chi phí/giới hạn → kiểm tra | Tự viết map/reduce và giải thích vì sao gom đúng dữ liệu |
| Công thức chi phí | Chỉ nơi dữ liệu được đọc → lập bảng từng tác vụ/giai đoạn → cộng → thay số nguồn → so sánh phương án | Tự lập phép tính, biết đại lượng nào đang được đếm |
| Mệnh đề hoặc bảo đảm | Phát biểu với giả thiết → chỉ bước dùng giả thiết → kết luận → trường hợp không áp dụng | Không suy kết luận từ một ví dụ riêng |
| Lý thuyết 2.6 | Cùng dữ liệu, đổi cách phân phối → đếm bộ nhớ và số bản sao → giải thích đánh đổi | Hiểu hai đại lượng; không yêu cầu chứng minh cận dưới tổng quát |

Giữ cách dạy đã tham khảo ở ba bài `math-4-AI`: dữ liệu cụ thể trước ký hiệu chung; giữ cùng ví dụ qua các bước; hình và bảng chuẩn bị cho công thức; quay lại kiểm chứng đầu ra. Không sao chép nội dung hoặc giao diện của môn toán. Quy tắc trình bày:

- Mỗi trang có một việc người học cần theo dõi. Một bước biến đổi khó được tách thành trang riêng thay vì thu nhỏ chữ.
- Ví dụ chạy tay dùng bảng **đầu vào → cặp map phát → nhóm nhận → kết quả reduce**; không hiện toàn bộ lời giải ngay từ đầu. Các trạng thái xuất hiện bằng bàn phím và giữ nhãn để đọc được khi in.
- Giả mã ngắn đặt cạnh đúng trạng thái vừa chạy; tránh đưa thêm API hoặc cú pháp cài đặt khi đang học ý tưởng.
- Công thức có định nghĩa ký hiệu ngay cạnh. Hình có nhãn và đường nét ngoài màu. Đích chữ thân bài khoảng 28–32 px ở khung 1280×720; đo cỡ chữ sau khi co giãn hình.
- Câu kiểm tra dùng nhãn **Câu hỏi:**, yêu cầu một thao tác cụ thể. Đáp án, giải thích và nguồn nằm trong ghi chú diễn giả.

## Section 1. Mở đầu

Ba trang theo đúng thứ tự người dùng yêu cầu:

| Mã trang | Nội dung | Phút |
|---|---|---:|
| `lec02-s00-01` | Tiêu đề bài giảng, học phần, học kỳ; nối giới hạn dữ liệu lớn ở bài 1 | 1 |
| `lec02-s00-02` | Mục lục tám phần nội dung, giữ thứ tự 2.1–2.8; nhấn phần thuật toán và phần chi phí là hai trọng tâm | 2 |
| `lec02-s00-03` | Mục tiêu: mô tả MapReduce; thiết kế map/reduce cho bài toán đại diện; tính chi phí theo mô hình đã nêu; giải thích đánh đổi bộ nhớ–truyền dữ liệu | 2 |

Đầu ra của phần mở đầu là bốn việc có thể kiểm tra. Câu nối: “Dữ liệu được lưu trên nhiều máy; trước hết cần xác định cách lưu và đọc các phần của một tệp.”

## Section 2. Hệ tệp phân tán — PDF 2.1

**Mạch viết:** dữ liệu vượt một máy → cụm máy và mạng → lỗi máy hoặc giá máy → chia khối và lưu bản sao → đặt tính toán gần bản sao đầu vào. Nguồn: 2.1.1–2.1.2, Hình 2.1. Không dùng thông số phần cứng lịch sử làm chuẩn hiện tại.

| Mã trang | Luận điểm và cách thể hiện | Phút |
|---|---|---:|
| `lec02-s01-01` | Sơ đồ máy–giá máy–mạng; theo một đường dữ liệu phải di chuyển | 3 |
| `lec02-s01-02` | Một tệp được chia khối và có bản sao ở các vị trí khác nhau; đánh dấu một máy hỏng để thấy dữ liệu nào còn đọc được | 3 |
| `lec02-s01-03` | Đặt tác vụ gần dữ liệu; phân biệt lưu bền vững với thực thi tính toán; kiểm tra chọn vị trí đọc | 4 |

Chỉ yêu cầu giải thích cơ chế, không chứng minh hệ tệp hoặc cấu hình HDFS. Đầu ra cho 2.2: dữ liệu đã được chia; hệ thống cần tổ chức các phép tính trên những phần đó.

## Section 3. Mô hình MapReduce — PDF 2.2

**Mạch viết:** nhu cầu đếm từ trong kho tài liệu → đóng góp một lần xuất hiện → map → nhóm theo khóa → reduce → tính đúng → gộp cục bộ → tác vụ, điều phối và khôi phục. Theo 2.2.1–2.2.6, Ví dụ 2.1–2.2, Hình 2.2–2.3 và khung giải thích reducer ở trang in 28.

| Mã trang | Nội dung, ví dụ và cách thể hiện | Phút |
|---|---|---:|
| `lec02-s02-01` | Đặc tả bằng lời: tài liệu vào, số lần xuất hiện theo từ ra; sơ đồ ba bước | 2 |
| `lec02-s02-02` | Ví dụ 2.1: một lần xuất hiện phát một cặp $(w,1)$; vết từ tài liệu đến cặp | 3 |
| `lec02-s02-03` | Ví dụ 2.2: gom mọi giá trị cùng từ rồi cộng; bảng nhóm cạnh kết quả | 3 |
| `lec02-s02-04` | Giả mã map/reduce, giả thiết tách từ và không tràn bộ đếm; mỗi lần xuất hiện tạo đúng một đóng góp, bất biến tổng, dừng và đầu vào rỗng | 3 |
| `lec02-s02-05` | Bộ kết hợp: cộng cục bộ trước khi chuyển, vẫn cần tổng hợp toàn cục; nêu điều kiện kết hợp, giao hoán và giữ đúng ý nghĩa trạng thái | 2 |
| `lec02-s02-06` | Hình lồng: lời gọi reduce cho một khóa → Reduce task → máy; danh sách dài gây lệch tải | 2 |
| `lec02-s02-07` | Cùng sơ đồ lưu trữ, lần lượt đánh dấu lỗi máy map và máy reduce; giải thích phần phải chạy lại | 3 |

Hai chuỗi tiếng Việt là bản cụ thể hóa Ví dụ 2.1–2.2: tách theo khoảng trắng cho `dữ`, `liệu`, `lớn`; tuyệt đối không vừa quy định tách khoảng trắng vừa coi `dữ liệu` là một đơn vị. Không đưa bài minh họa này vào danh sách bài tập nguyên văn từ sách.

Đầu ra: sinh viên đọc được luồng khóa–giá trị và hiểu phần nào do hệ thống bảo đảm. Câu nối: “Ở bài đếm từ, khóa là từ cần tổng hợp. Các bài toán tiếp theo thay cách chọn khóa và phép xử lý trong reduce.”

## Section 4. Các thuật toán dùng MapReduce — PDF 2.3

**Mạch viết:** từ đóng góp theo từ sang đóng góp theo hàng ma trận → điều kiện bộ nhớ → bảng dữ liệu và phép biến đổi → ghép dữ liệu theo khóa chung → tổng hợp → nhận ra phép nhân ma trận là nối rồi cộng. Mỗi thuật toán trọng tâm phải có vết chạy trước giả mã tổng quát; không chỉ trình bày danh sách tên thuật toán.

| Mã trang | Nội dung và cách thể hiện | Nguồn | Phút |
|---|---|---|---:|
| `lec02-s03-01` | Bài toán $x=Mv$: một thành phần kết quả cần các tích trong cùng hàng; nêu kích thước và cách lưu $(i,j,m_{ij})$ | 2.3.1, in 31/PDF 12 | 3 |
| `lec02-s03-02` | Theo hàng $i$: $m_{i1}v_1,m_{i2}v_2,\ldots$ → cùng khóa $i$ → tổng; sau vết ký hiệu mới ghi giả mã và lập luận đúng | 2.3.1, in 31–32/PDF 12–13 | 3 |
| `lec02-s03-03` | Vector không vừa bộ nhớ: hình năm dải của sách, theo một dải ma trận và dải vector tương ứng; gom các tổng về cùng hàng | 2.3.2, Hình 2.4, in 32/PDF 13 | 3 |
| `lec02-s03-04` | Quan hệ là bảng có tên cột; dựng bốn hàng Links, chỉ rõ hàng, cột và thuộc tính dùng để nối | 2.3.3, Hình 2.5, Ví dụ 2.3, in 33–34/PDF 14–15 | 2 |
| `lec02-s03-05` | Phép chọn giữ hàng thỏa điều kiện: chạy hai trong bốn hàng Links qua điều kiện From=url1: một hàng giữ, một hàng bỏ; áp dụng cả bảng giữ hai hàng; rồi khái quát map/reduce | 2.3.4, in 35/PDF 16 | 2 |
| `lec02-s03-06` | Phép chiếu giữ cột và loại bản sao; chiếu cột From của phần trích Links để thấy bốn giá trị thành hai giá trị phân biệt | 2.3.5; Ví dụ 2.4, in 35–36/PDF 16–17 | 2 |
| `lec02-s03-07` | Vấn đề tìm đường đi dài hai; trực giác hai cạnh gặp nhau tại đỉnh giữa; chạy một cặp cạnh trước khi đặt nhãn nguồn và viết map/reduce | 2.3.7; Ví dụ 2.4, in 35,37/PDF 16,18 | 5 |
| `lec02-s03-08` | Vết đầy đủ trên phần trích Links: cặp phát, nhóm, hai kết quả; dùng vết giải thích đủ và chỉ các đường đi dài hai được phát | Cùng nguồn trên | 4 |
| `lec02-s03-09` | Nhóm và tổng hợp: khóa là thuộc tính nhóm; Ví dụ 2.5 đếm bạn của Sally, đầu ra $(\text{Sally},300)$; không giả vờ đã có danh sách 300 bạn để liệt kê | 2.3.8; Ví dụ 2.5, in 35,38/PDF 16,19 | 3 |
| `lec02-s03-10` | Sơ đồ liên hệ nhân ma trận: nối theo $j$ để tạo tích, rồi cộng theo $(i,k)$; chi tiết hai công việc và biến thể một công việc chuyển sang đọc thêm | 2.3.9–2.3.10, in 38–40/PDF 19–21 | 3 |
| **Tổng** | | | **30** |

### Đặc tả thuật toán và ví dụ cần có

**Nhân ma trận–vector.** Đầu vào $M\in\mathbb R^{n\times n}$ và $v\in\mathbb R^n$; kết quả $x_i=\sum_{j=1}^n m_{ij}v_j$. Khi vector vừa bộ nhớ, map phát $(i,m_{ij}v_j)$; reduce cộng các giá trị của khóa $i$. Mỗi tích cần thiết được phát một lần và được gom đúng hàng, nên tổng là $x_i$. Dừng sau hữu hạn phần tử và danh sách giá trị. Nếu lưu thưa, các phần tử không lưu được hiểu bằng 0; cần quy định cách hiểu hàng không phát cặp là thành phần kết quả 0. Khi chia dải, không được bỏ việc đọc dải vector ở từng Map task. Ví dụ dùng biểu thức và Hình 2.4 của nguồn, không tự thêm ma trận số.

**Chọn và chiếu.** Chọn: map phát $(t,t)$ nếu $C(t)$ đúng; reduce giữ nguyên. Chiếu: map tạo bộ $t'$ gồm các thuộc tính được chọn và phát $(t',t')$; reduce phát đúng một bản $t'$ cho mỗi khóa. Giả thiết quan hệ theo ngữ nghĩa tập hợp; việc bỏ cột có thể tạo bản sao nên phép chiếu cần bước loại trùng. Kiểm tra ngắn yêu cầu sinh viên chỉ ra dòng mã giữ hàng hoặc bỏ cột, không yêu cầu nhớ tên ký hiệu trước khi hiểu thao tác.

**Nối tự nhiên.** Với $R(A,B)$ và $S(B,C)$, map phát $(b,(R,a))$ từ $(a,b)\in R$, và $(b,(S,c))$ từ $(b,c)\in S$. Reduce chia danh sách theo nhãn nguồn, rồi phát mọi $(a,b,c)$ tạo bởi một giá trị mỗi phía. Nhãn $R,S$ là nhãn nguồn, không phải gửi nguyên bảng trong mỗi cặp.

Vết chạy lấy đúng phần trích Links của Hình 2.5: $(url1,url2)$, $(url1,url3)$, $(url2,url3)$, $(url2,url4)$. Hai bản sao có lược đồ $L_1(U_1,U_2)$ và $L_2(U_2,U_3)$. Để tránh đổi tên giữa ví dụ và giả mã, dùng nhãn $L_1,L_2$ thay $R,S$ khi chạy:

| Khóa đỉnh giữa | Giá trị từ $L_1$ | Giá trị từ $L_2$ | Kết quả reduce |
|---|---|---|---|
| `url1` | Không có | `url2`, `url3` | Không phát |
| `url2` | `url1` | `url3`, `url4` | `(url1,url2,url3)`, `(url1,url2,url4)` |
| `url3` | `url1`, `url2` | Không có | Không phát |
| `url4` | `url2` | Không có | Không phát |

Trước bảng nhóm, phải cho thấy một cạnh được phát hai cách: cạnh `(url1,url2)` ở $L_1$ phát `(url2,(L1,url1))`; ở $L_2$ phát `(url1,(L2,url2))`. Sinh viên dự đoán nhóm của cạnh tiếp theo rồi mới hiện kết quả. Đây là kết quả trên bốn hàng được trích, không khẳng định chỉ có hai đường đi trong quan hệ Web đầy đủ.

Lập luận đúng gồm hai chiều: bộ được phát chứa hai cạnh có chung đỉnh giữa; mọi cặp cạnh cần nối gặp nhau ở đúng khóa đó. Chi phí tính toán cục bộ phụ thuộc số cặp ghép và đầu ra; phần 2.5 sẽ phân biệt với chi phí truyền thông.

**Nhóm và tổng hợp.** Với $R(A,B,C)$, map phát $(a,b)$; reduce áp dụng phép tổng hợp đã chọn lên danh sách của $a$. COUNT đếm số phần tử, SUM cộng giá trị, AVG cần tổng và số lượng nếu gộp cục bộ. Ví dụ Sally chỉ cung cấp đầu ra 300 của nguồn; dùng danh sách ký hiệu để giải thích phép đếm, không bịa tên bạn.

Các phép hợp/giao/hiệu ở 2.3.6 và chi tiết 2.3.9–2.3.10 là đọc thêm trong section này, không tính là thuật toán sinh viên đã tự thiết kế được sau 30 phút. Không giao bài tập bắt buộc dựa trên các chi tiết đó. Đầu ra cho 2.4 là các công việc có thể nối tiếp nhau; đầu ra cho 2.5 là thuật toán nối và tổng hợp để tính chi phí.


## Section 5. Mở rộng MapReduce — PDF 2.4

**Mạch viết:** một công việc có hai tầng → nhiều phép biến đổi phụ thuộc nhau → đồ thị luồng công việc → dữ liệu phân tán trong Spark → dùng lại và tái tạo dữ liệu. Dùng Word Count đã biết để sinh viên tập trung vào cách tổ chức thực thi mới.

| Mã trang | Nội dung và ví dụ nguồn | Phút |
|---|---|---:|
| `lec02-s04-01` | Khái niệm đồ thị có hướng không chu trình theo 2.4.1; không sao chép Hình 2.6; phân biệt sơ đồ hàm với tập tác vụ chạy trên máy | 2 |
| `lec02-s04-02` | Tập dữ liệu phân tán có khả năng khôi phục (RDD); Ví dụ 2.7: Map cho một đối tượng kết quả mỗi đầu vào, Flatmap phát nhiều phần tử | 3 |
| `lec02-s04-03` | Ví dụ 2.8: nối Flatmap với Filter để loại từ dừng; bảng trước/sau một phép biến đổi | 2 |
| `lec02-s04-04` | Ví dụ 2.9–2.10: đánh giá lười, lưu kết quả dùng lại và tái tạo từ chuỗi phép biến đổi; sơ đồ còn/mất giống phần chịu lỗi | 3 |
| `lec02-s04-05` | So sánh trách nhiệm lưu trữ và thực thi; chỉ ra giới hạn mô hình hai tầng; chỉ dẫn đọc thêm 2.4.4–2.4.6 | 2 |

TensorFlow, hệ đệ quy và hệ đồng bộ theo từng bước được định vị trong bản đồ đọc thêm; không giảng triển khai, API hoặc thuật toán đường đi ở mức bắt buộc. Không đồng nhất Reduce toàn cục của Spark với reduce theo khóa của MapReduce. Đầu ra cho 2.5: một phép tính có thể là mạng nhiều tác vụ; cần một quy tắc đếm chi phí cho cả mạng.

## Section 6. Mô hình chi phí truyền thông — PDF 2.5

**Mạch viết:** định nghĩa đối tượng đếm và đơn vị → dùng lại đếm từ → tính nối hai bảng → lưới nối ba bảng và số bản sao → bảng chi phí → so sánh nối tuần tự dưới giả thiết nguồn → kiểm tra tải lớn nhất. Phần này dùng lại thuật toán 2.3 để mỗi công thức gắn với đường đi của dữ liệu.

| Mã trang | Nội dung thực tế | Nguồn | Phút |
|---|---|---|---:|
| `lec02-s05-01` | Sơ đồ đầu vào Map/Reduce, định nghĩa $I,M$ và $C=I+M$ | 2.5.1, tr.53–55 | 4 |
| `lec02-s05-02` | Chốt đơn vị, đọc lặp, tổng chi phí và thời gian hoàn thành | 2.5.1–2.5.2 | 2 |
| `lec02-s05-03` | Đếm từ: $I+5B$ và $I+4B$, với $I,B$ tính bằng byte | Ví dụ2.1, 2.2.4, 2.5.1 | 3 |
| `lec02-s05-04` | Nối hai bảng: Map đọc $r+s$, Reduce nhận $r+s$; đầu ra có thể lớn | Ví dụ2.14, tr.55 | 2 |
| `lec02-s05-05` | Lưới4×4, R/S/T có4/1/4 nơi nhận, kiểm tra giá trị khóa thật | Hình2.8, Ví dụ2.15, tr.57 | 3 |
| `lec02-s05-06` | Bảng chi phí theo quan hệ và tổng $r+2s+t+cr+bt$ | 2.5.3, tr.58 | 3 |
| `lec02-s05-07` | Nối tuần tự: trung gian $30r$, tổng $66r$ | Ví dụ2.16, tr.59 | 3 |
| `lec02-s05-08` | So sánh $4r+2r\sqrt{k}$ với $66r$; biên961 và điều kiện lưới vuông | Ví dụ2.15–2.16 | 4 |
| `lec02-s05-09` | Phân biệt tổng với tải lớn nhất, câu hỏi về thời gian hoàn thành | 2.5.2, nối2.6 | 3 |
| **Tổng** | | | **27** |

### 1. Nêu mô hình trước phép tính

Theo 2.5.1, với tác vụ $\tau$:

$$
C(\tau)=|\operatorname{input}(\tau)|,\qquad C_{\mathrm{toàn\ bộ}}=\sum_{\tau}C(\tau).
$$

Kích thước có thể đo bằng byte; với ví dụ quan hệ, dùng số bộ và công bố quy ước biểu diễn. Đẳng thức đếm bộ không tự trở thành đẳng thức byte khi bộ đầu vào và cặp trung gian khác kích thước. Với một công việc MapReduce, nếu $I$ là tổng đầu vào map và $M$ là tổng đầu vào reduce thì $C=I+M$. Không dùng hai công thức chi phí khác nhau làm hai kiến thức bắt buộc trong bài nhập môn này.

Đầu ra một tác vụ sẽ được tính khi tác vụ kế tiếp đọc nó. Đầu ra cuối không nằm trong phép cộng trên; sách thường dựa vào việc kết quả cuối nhỏ hoặc được tổng hợp tiếp. Nếu đầu ra nối rất lớn, phải nêu chi phí sinh/ghi đầu ra hoặc tính thêm tác vụ đọc nó. Không dùng $O(r+s)$ để kết luận thời gian chạy luôn tuyến tính bất kể kích thước kết quả. Các con số tốc độ mạng và quy mô mạng xã hội trong sách là dữ kiện lịch sử của ví dụ, không phải mô tả hiện trạng.

### 2. Ví dụ nối hai bảng — Ví dụ 2.14

Đặt $r=|R|$, $s=|S|$. Dùng đơn vị bộ/cặp chuẩn hóa, một đầu vào phát một cặp:

| Giai đoạn | Dữ liệu đi vào | Chi phí đếm bộ/cặp |
|---|---|---:|
| Map | Đọc toàn bộ $R,S$ | $r+s$ |
| Reduce | Nhận các cặp đã đổi khóa | $r+s$ |
| Tổng | Cộng hai hàng, không cộng lại đầu ra map như một khoản riêng | $2(r+s)$ |

Từ bảng mới rút ra $O(r+s)$ như sách. Hỏi sinh viên chỉ nơi quan hệ có một khóa phổ biến làm tăng số kết quả ghép, dù số cặp đi vào reduce vẫn như cũ.

### 3. Ví dụ nối ba bảng — Ví dụ 2.15

Với $R(A,B)\bowtie S(B,C)\bowtie T(C,D)$, đặt $r,s,t$ là số bộ. Dùng $b$ nhóm băm cho $B$, $c$ nhóm băm cho $C$, $bc=k$. Một bộ $S$ biết cả hai thành phần khóa nên đến một reducer; một bộ $R$ thiếu $C$ nên đến $c$ reducer; một bộ $T$ thiếu $B$ nên đến $b$ reducer.

Giữ đúng $b=c=4$, $k=16$ của nguồn. Chuẩn hóa cả hình và văn bản về chỉ số $0,1,2,3$: $S(v,w)$ đến $(2,1)$; $R(u,v)$ đến $(2,y)$ với $y\in\{0,1,2,3\}$; $T(w,x)$ đến $(z,1)$ với $z\in\{0,1,2,3\}$. Ba bộ gặp nhau ở đúng $(2,1)$. PDF vẽ 0–3 nhưng đoạn văn ghi 1–4; đây là hiệu chỉnh chỉ số cần ghi trong review-log.

$$
C_{\mathrm{Map}}=r+s+t,\qquad C_{\mathrm{Reduce}}=cr+s+bt,
$$
$$
C_3=(r+s+t)+(cr+s+bt)=r+2s+t+cr+bt.
$$

Mặt trang hiện lưới và số bản sao trước công thức. Không đưa đạo hàm Lagrange vào mạch năm 2. Tối ưu liên tục $b=\sqrt{kr/t}$, $c=\sqrt{kt/r}$ và chọn cặp số nguyên thỏa $bc=k$ để đọc thêm; không ngầm dùng nghiệm liên tục như một cấu hình nguyên luôn hợp lệ.

### 4. Ví dụ tính số và chọn phương án — Ví dụ 2.16

Nguồn cho ba quan hệ cùng là quan hệ bạn bè, mỗi quan hệ có $r=3\times10^{11}$ bộ; giả định kích thước nối trung gian là $30r=9\times10^{12}$ bộ. $30r$ là ước lượng của ví dụ, không phải đẳng thức đúng cho mọi mạng xã hội.

| Phương án | Các khoản cần cộng | Kết quả |
|---|---|---|
| Hai công việc nối hai bảng | Công việc đầu: $2r+2r=4r$. Công việc sau: $(30r+r)+(30r+r)=62r$ | $66r=1.98\times10^{13}$ |
| Một công việc, chia cân bằng $b=c=\sqrt{k}$ | Map: $3r$. Reduce: $r\sqrt{k}+r+r\sqrt{k}$ | $4r+2r\sqrt{k}=1.2\times10^{12}+6\times10^{11}\sqrt{k}$ |

$$
4r+2r\sqrt{k}<66r
\iff \sqrt{k}<31
\iff k<961.
$$

Tại $k=961$, hai chi phí bằng nhau. Sách kết luận bằng lời “không quá 961” là rẻ hơn; cần sửa dấu biên này. Công thức chia cân bằng trên là cấu hình nguyên khi $k$ là số chính phương; với $k$ khác phải chọn $b,c$ nguyên rồi tính lại. So sánh này còn giả định dữ liệu mỗi reducer xử lý được; ít truyền dữ liệu hơn chưa đủ để chọn phương án nếu vượt bộ nhớ. Đây là câu nối trực tiếp sang 2.6.


## Section 7. Đánh đổi bộ nhớ và sao chép dữ liệu — PDF 2.6

**Mạch viết cho năm 2:** một reducer nhận bao nhiêu dữ liệu → mỗi đầu vào được gửi bao nhiêu lần → một ví dụ rất ít bộ nhớ nhưng truyền nhiều → gom đầu vào để đổi hai đại lượng. Giảng 2.6.1–2.6.2 và Ví dụ 2.18; các mục 2.6.3–2.6.7 để đọc thêm có hướng dẫn.

| Mã trang | Nội dung và phép tính cần nhìn thấy | Phút |
|---|---|---:|
| `lec02-s06-01` | Định nghĩa $q$ là cận số giá trị của một reducer, không phải số máy. Dùng $\rho$ cho hệ số sao chép trung bình; sách dùng $r$, đổi ký hiệu để tránh nhầm với kích thước quan hệ ở 2.5 | 3 |
| `lec02-s06-02` | Bài so sánh ảnh của 2.6.2: $10^6$ ảnh, mỗi ảnh $10^6$ byte; gửi mỗi ảnh cho mọi cặp. $q=2$, $\rho=999999$; khoảng $10^{18}$ byte trung gian | 3 |
| `lec02-s06-03` | Ví dụ 2.18: chia $g=1000$ nhóm; mỗi ảnh gửi tới $g-1=999$ reducer theo cặp nhóm. Mỗi reducer nhận $2\times10^6/g=2000$ ảnh, khoảng $2\times10^9$ byte | 3 |
| `lec02-s06-04` | Bảng so sánh: giao tiếp còn $10^6\times999\times10^6=9.99\times10^{14}$ byte; giảm sao chép nhưng tăng dữ liệu mỗi reducer. Chỉ ra cách xử lý cặp trong cùng nhóm đúng một lần theo nguồn | 3 |

Giữ giả thiết chia nhóm đều và số byte theo quy ước thập phân của ví dụ. Không suy thời gian hoàn thành thực tế từ một đường truyền đơn lẻ. Không tuyên bố thuật toán tối ưu nếu chưa trình bày cận dưới. Bản đồ đồ thị phụ thuộc, lược đồ ánh xạ, dữ liệu đầu vào thiếu và chứng minh cận dưới được dẫn đúng 2.6.3–2.6.7 trong ghi chú đọc thêm.

Đầu ra: sinh viên giải thích được giảm dữ liệu mỗi reducer có thể làm tăng số bản sao. Câu nối: “Thiết kế thuật toán cần giữ đúng đầu ra và chọn mức truyền dữ liệu, bộ nhớ, song song phù hợp.”

## Section 8. Tổng kết chương — PDF 2.7

| Mã trang | Nội dung | Phút |
|---|---|---:|
| `lec02-s07-01` | Bảng tổng hợp theo 2.7: lưu dữ liệu → chọn khóa → thực thi → đếm chi phí → kiểm tra bộ nhớ; mỗi hàng trỏ về một ví dụ đã học | 3 |
| `lec02-s07-02` | Kiểm tra cuối: trên ví dụ nối bảng đã có, chỉ ra khóa, một bước bảo đảm tính đúng và phần chi phí tăng khi sao chép; nối bài 3 bằng nhân ma trận–vector, không dạy PageRank tại đây | 2 |

Không lặp nguyên văn mục lục. Kết luận phải thu hồi hai sản phẩm chính: thiết kế được map/reduce và tự lập phép tính chi phí.

## Section 9. Tài liệu tham khảo — PDF 2.8

`lec02-s08-01`, 1 phút. Dẫn `ch2n.pdf` là nguồn chính; dùng danh mục 2.8 để chỉ hướng đọc bài gốc về MapReduce, hệ tệp và mô hình lý thuyết. Không tuyên bố đã đọc bài gốc nếu mới đọc danh mục tài liệu của sách. Giữ ghi công MMDS. Các slide MMDS/Stanford trong ánh xạ học phần chỉ hỗ trợ cách vẽ khi triển khai; không thay thứ tự, ví dụ hay quy ước chi phí của PDF được chỉ định.

## Bài tập 60 phút và đường trình bày

Để giữ ánh xạ một section ngoài với một mục PDF, các trang bài tập đặt cuối section tương ứng: 2.2.7, 2.3.11 và 2.5.4. Phần giảng 120 phút đi theo các trang nội dung; sau đó quay lại các trang bài tập cho 60 phút luyện tập. Đây là điều chỉnh có chủ ý so với quy ước một section bài tập riêng ở cuối deck; không tạo section ngoài trộn nhiều mục PDF. Khi dựng cần liên kết điều hướng nội bộ rõ trong tài liệu tổ chức, không hiển thị mã quy trình hoặc thời lượng trên mặt trang.

| Mã trang | Bài nguồn và phạm vi giữ | Trang in / PDF | Phút | Sản phẩm và hướng dẫn trong ghi chú |
|---|---|---|---:|---|
| `lec02-ex221a` | 2.2.1(a), không có bộ kết hợp | 30 / 11 | 5 | Giải thích lệch độ dài danh sách theo khóa |
| `lec02-ex221b` | 2.2.1(b), giữ 10 và 10.000 Reduce task | 30 / 11 | 5 | So sánh gộp reducer và số đơn vị lập lịch |
| `lec02-ex221c` | 2.2.1(c), giữ 100 Map task | 30 / 11 | 5 | Giải thích ảnh hưởng gộp cục bộ |
| `lec02-ex231a` | 2.3.1(a), tìm số lớn nhất | 40 / 21 | 4 | Khóa, map/reduce, điều kiện đầu vào có phần tử |
| `lec02-ex231b` | 2.3.1(b), trung bình | 40 / 21 | 6 | Giữ tổng và số lượng nếu gộp; xử lý miền xác định |
| `lec02-ex231c` | 2.3.1(c), loại bản sao | 40 / 21 | 4 | Mỗi giá trị làm khóa, phát một lần |
| `lec02-ex231d` | 2.3.1(d), đếm giá trị phân biệt | 40 / 21 | 6 | Trình bày phương án hai công việc loại trùng rồi đếm; không tuyên bố mọi thuật toán đều bắt buộc hai công việc |
| `lec02-ex251a` | 2.5.1(a), chi phí nhân ma trận–vector chia dải | 59 / 40 | 13 | Đếm phần ma trận và số lượt các tác vụ đọc dải vector; ghi rõ giả thiết về chia tác vụ, không ngầm coi vector chỉ đọc một lần toàn cụm |
| `lec02-ex251c` | 2.5.1(c), chi phí nhóm và tổng hợp | 59 / 40 | 12 | Lập bảng đầu vào map/reduce, thống nhất đơn vị và nêu cận theo kích thước quan hệ |
| **Tổng** | | | **60** | |

Đề bài được dịch từ PDF, giữ dữ kiện và yêu cầu toán học. Phần dẫn 2.2.1 phải giữ 100 Map task cho cả ba ý. Bài 2.3.1 cho phép bỏ/không dùng khóa đầu ra. Chỉ chọn 2.5.1(a,c); không giao (b,d) khi các thuật toán tương ứng chưa được học đủ sâu. Đáp án và hướng dẫn chấm nằm trong ghi chú; thời lượng mới là dự kiến cần kiểm lại khi diễn tập.

## Tiêu chí duyệt và triển khai

- Chốt **9 section ngoài**, **44 trang giảng + 9 trang bài tập**, **120 + 60 phút**; mã nêu trong storyboard là mã thực tế của bản mới.
- Chấp nhận mức chọn lọc cho năm 2: giảng kỹ ví dụ và cơ chế; không phủ toàn chương bằng các định nghĩa liệt kê hoặc chứng minh lướt.
- Mỗi thuật toán trọng tâm có ví dụ nguồn, khóa/giá trị, giả mã, lập luận đúng và điều kiện áp dụng. Ví dụ biểu thức của sách được chạy bằng ký hiệu; không tự thêm ma trận số hoặc quan hệ không có nguồn.
- Phần đánh giá nêu đơn vị, phạm vi đếm, giả thiết, từng phép cộng chi phí và kết luận so sánh. Hiệu chỉnh lỗi biên hoặc chỉ số của sách phải ghi rõ trong review-log.
- Đã triển khai: cập nhật outline, storyboard và review-log; dựng HTML/SVG theo mẫu học phần; đồng bộ phần ghi chú dùng chung. Hình trọng tâm là khối/bản sao, chia dải ma trận, chuỗi Spark, mô hình chi phí và lưới reducer; vết nối trên Links là bảng HTML, không dùng SVG.
- Rà độc lập về sinh viên, thuật toán, toán học, giảng dạy và mạch kết nối; kiểm tra công thức, đường dẫn, chữ, tràn trang, bàn phím và bản in. Thời lượng là dự kiến sư phạm, chưa có dữ liệu diễn tập hoặc đánh giá với lớp học thật.

Các báo cáo và quyết định cuối được ghi tại review-log.md.

## Bản đồ triển khai từng trang

Bảng dưới là danh mục thực tế của bản viết mới. Mỗi hàng ghi luận điểm qua tiêu đề; đặc tả nội dung, vết chạy, lập luận đúng, giới hạn và nguồn nằm trong HTML cùng ghi chú diễn giả. Bài tập ở cuối section tương ứng, truy cập sau phần giảng bằng liên kết ở tổng kết và tài liệu tham khảo. Khi giảng liên tục dùng phím phải để sang section kế tiếp trước cụm bài tập. Đây là ngoại lệ vị trí recitation để giữ đúng ánh xạ một section ngoài với một mục PDF.

| Mã trang | Luận điểm / sản phẩm | Mục nguồn | Phút | Loại |
|---|---|---|---:|---|
| `lec02-s00-01` | MapReduce và ngăn xếp xử lý dữ liệu lớn | Phần dẫn chương, trang in 21–22; sources/source.md, Bài 2. | 1 | Giảng |
| `lec02-s00-02` | Nội dung bài giảng | Chương 2, các mục 2.1–2.8. | 2 | Giảng |
| `lec02-s00-03` | Mục tiêu học tập | sources/source.md, Bài 2; Chương 2. | 2 | Giảng |
| `lec02-s01-01` | Cụm máy và mạng kết nối | 2.1, trang in 22–24. | 3 | Giảng |
| `lec02-s01-02` | Lỗi máy và lỗi kết nối | 2.1, trang in 22–24. | 3 | Giảng |
| `lec02-s01-03` | Hệ tệp phân tán: chia khối và đặt tính toán gần dữ liệu | 2.1, trang in 22–24. | 4 | Giảng |
| `lec02-s02-01` | 2.2 · Mô hình MapReduce | 2.2.1–2.2.3, Ví dụ 2.1–2.2, trang in 25–27. | 2 | Giảng |
| `lec02-s02-02` | Mỗi lần xuất hiện tạo một đóng góp | Ví dụ 2.1, trang in 26; dữ liệu minh họa tiếng Việt được ghi trong storyboard. | 3 | Giảng |
| `lec02-s02-03` | Nhóm theo khóa rồi cộng | 2.2.2–2.2.3, Ví dụ 2.2, trang in 26–27. | 3 | Giảng |
| `lec02-s02-04` | Thuật toán đếm từ và tính đúng | 2.2.1–2.2.3, trang in 25–27; lập luận đúng từ Ví dụ 2.1–2.2. | 3 | Giảng |
| `lec02-s02-05` | Gộp cục bộ trước khi truyền | 2.2.4, trang in 27–28. | 2 | Giảng |
| `lec02-s02-06` | Khóa, tác vụ và máy | Khung reducer/tác vụ/máy, trang in 28; 2.2.5. | 2 | Giảng |
| `lec02-s02-07` | Lưu trữ quyết định phần cần chạy lại | 2.2.5–2.2.6, trang in 28–30. | 3 | Giảng |
| `lec02-ex221a` | Bài tập 2.2.1(a) · Lệch tải khi chưa gộp | Bài tập 2.2.1(a), trang in 30 / PDF 11. | 5 | Bài tập |
| `lec02-ex221b` | Bài tập 2.2.1(b) · Gom reducer vào tác vụ | Bài tập 2.2.1(b), trang in 30 / PDF 11. | 5 | Bài tập |
| `lec02-ex221c` | Bài tập 2.2.1(c) · Tác động của bộ kết hợp | Bài tập 2.2.1(c), trang in 30 / PDF 11. | 5 | Bài tập |
| `lec02-s03-01` | 2.3 · Nhân ma trận–vector | 2.3.1, trang in 31–32. | 3 | Giảng |
| `lec02-s03-02` | Khóa hàng gom đúng các tích | 2.3.1, trang in 31–32. | 3 | Giảng |
| `lec02-s03-03` | Chia dải khi vector không vừa bộ nhớ | 2.3.2, Hình 2.4, trang in 32. | 3 | Giảng |
| `lec02-s03-04` | Một quan hệ là một bảng dữ liệu | 2.3.3, Hình 2.5, Ví dụ 2.3, trang in 33–34. | 2 | Giảng |
| `lec02-s03-05` | Phép chọn giữ các hàng thỏa điều kiện | 2.3.4, trang in 35. | 2 | Giảng |
| `lec02-s03-06` | Phép chiếu giữ cột và loại bản sao | 2.3.5 và Ví dụ 2.4, trang in 35–36. | 2 | Giảng |
| `lec02-s03-07` | Hai cạnh nối qua cùng đỉnh giữa | 2.3.7 và Ví dụ 2.4, trang in 35,37. | 5 | Giảng |
| `lec02-s03-08` | Vết nối trên bốn hàng Links | Hình 2.5, Ví dụ 2.4 và 2.3.7, trang in 33,35,37. | 4 | Giảng |
| `lec02-s03-09` | Nhóm theo người dùng rồi tổng hợp | 2.3.8 và Ví dụ 2.5, trang in 35,38. | 3 | Giảng |
| `lec02-s03-10` | Nhân ma trận là nối rồi cộng | 2.3.9–2.3.10, trang in 38–40. | 3 | Giảng |
| `lec02-ex231a` | Bài tập 2.3.1(a) · Số nguyên lớn nhất | Bài tập 2.3.1(a), trang in 40 / PDF 21. | 4 | Bài tập |
| `lec02-ex231b` | Bài tập 2.3.1(b) · Trung bình các số nguyên | Bài tập 2.3.1(b), trang in 40 / PDF 21. | 6 | Bài tập |
| `lec02-ex231c` | Bài tập 2.3.1(c) · Mỗi số chỉ xuất hiện một lần | Bài tập 2.3.1(c), trang in 40 / PDF 21. | 4 | Bài tập |
| `lec02-ex231d` | Bài tập 2.3.1(d) · Số lượng giá trị khác nhau | Bài tập 2.3.1(d), trang in 40 / PDF 21. | 6 | Bài tập |
| `lec02-s04-01` | Mở rộng: luồng công việc nhiều hàm | 2.4.1–2.4.3, trang in 41–48. | 2 | Giảng |
| `lec02-s04-02` | Spark và RDD; Map khác Flatmap | 2.4.1–2.4.3, trang in 41–48. | 3 | Giảng |
| `lec02-s04-03` | Nối Flatmap với Filter | 2.4.1–2.4.3, trang in 41–48. | 2 | Giảng |
| `lec02-s04-04` | Đánh giá lười và dòng dõi | 2.4.1–2.4.3, trang in 41–48. | 3 | Giảng |
| `lec02-s04-05` | Vai trò lưu trữ và thực thi | 2.4.1–2.4.3, trang in 41–48. | 2 | Giảng |
| `lec02-s05-01` | 2.5 · Đếm đầu vào của từng tác vụ | 2.5.1, trang in 53–55. | 4 | Giảng |
| `lec02-s05-02` | Đơn vị và phạm vi của phép đếm | 2.5.1–2.5.2, trang in 53–56. | 2 | Giảng |
| `lec02-s05-03` | Đếm từ: theo dữ liệu qua hai tầng | Ví dụ 2.1, 2.2.4 và mô hình 2.5.1; phần trích minh họa được ghi trong storyboard. | 3 | Giảng |
| `lec02-s05-04` | Nối hai bảng: một lần phát cho mỗi bộ | Ví dụ 2.14, trang in 55; phần Links Hình 2.5. | 2 | Giảng |
| `lec02-s05-05` | Nối ba bảng: gửi tới một lưới | 2.5.3 và Ví dụ 2.15, trang in 56–58. | 3 | Giảng |
| `lec02-s05-06` | Chi phí của phép nối ba bảng | 2.5.3, trang in 56–58. | 3 | Giảng |
| `lec02-s05-07` | Nối tuần tự có thể tạo bảng trung gian lớn | Ví dụ 2.16, trang in 58–59. | 3 | Giảng |
| `lec02-s05-08` | So sánh hai cách dưới cùng giả thiết | Ví dụ 2.15–2.16, trang in 57–59; hiệu chỉnh biên đẳng thức. | 4 | Giảng |
| `lec02-s05-09` | Tổng chi phí và tải lớn nhất | 2.5.2 và chuyển sang 2.6, trang in 55–56,61. | 3 | Giảng |
| `lec02-ex251a` | Bài tập 2.5.1(a) · Nhân ma trận–vector | Bài tập 2.5.1(a), trang in 59 / PDF 40; 2.3.2. | 13 | Bài tập |
| `lec02-ex251c` | Bài tập 2.5.1(c) · Nhóm và tổng hợp | Bài tập 2.5.1(c), trang in 59 / PDF 40; 2.3.8. | 12 | Bài tập |
| `lec02-s06-01` | 2.6 · Bộ nhớ và số lần sao chép | 2.6.1, trang in 61. | 3 | Giảng |
| `lec02-s06-02` | So sánh mọi cặp ảnh | 2.6.2, trang in 61–63. | 3 | Giảng |
| `lec02-s06-03` | Gom nhóm để dùng lại mỗi ảnh | 2.6.2, trang in 62–63. | 3 | Giảng |
| `lec02-s06-04` | Đánh đổi cần kiểm tra trước khi triển khai | 2.6.2–2.6.7, trang in 61–74. | 3 | Giảng |
| `lec02-s07-01` | 2.7 · Từ lưu trữ đến đánh giá thuật toán | 2.7, trang in 74–77. | 3 | Giảng |
| `lec02-s07-02` | Kiểm tra bằng sản phẩm học tập | 2.7 và bài tập 2.2.1,2.3.1,2.5.1. | 2 | Giảng |
| `lec02-s08-01` | 2.8 · Tài liệu tham khảo | 2.8, trang in 77–79. | 1 | Giảng |

## Ánh xạ ghi chú độc lập

| note-topic-id | Chủ đề | Trang tương ứng | Kết nối vào → ra |
|---|---|---|---|
| `lec02-note-01` | Hệ tệp phân tán | `lec02-s01-*` | Theo mục 2.1; kế thừa ký hiệu và ví dụ của mục trước |
| `lec02-note-02` | MapReduce và đếm từ | `lec02-s02-*` | Theo mục 2.2; kế thừa ký hiệu và ví dụ của mục trước |
| `lec02-note-03` | Thuật toán theo khóa | `lec02-s03-*` | Theo mục 2.3; kế thừa ký hiệu và ví dụ của mục trước |
| `lec02-note-04` | Mở rộng thực thi | `lec02-s04-*` | Theo mục 2.4; kế thừa ký hiệu và ví dụ của mục trước |
| `lec02-note-05` | Mô hình chi phí | `lec02-s05-*` | Theo mục 2.5; kế thừa ký hiệu và ví dụ của mục trước |
| `lec02-note-06` | Bộ nhớ và sao chép | `lec02-s06-*` | Theo mục 2.6; kế thừa ký hiệu và ví dụ của mục trước |
| `lec02-note-07` | Tổng kết, bài tập | `lec02-s07-*` | Theo mục 2.7; kế thừa ký hiệu và ví dụ của mục trước |
| `lec02-note-08` | Nguồn và hướng đọc | `lec02-s08-*` | Theo mục 2.8; kế thừa ký hiệu và ví dụ của mục trước |

## Áp dụng cách thể hiện từ math-4-AI

| Nguồn cách dạy đã đối chiếu | Nguyên tắc | Áp dụng ở bản mới |
|---|---|---|
| Lecture 01, D01–D04, L01–L03, F01–F02 | Dữ kiện và quyết định trước mô hình; hình chuẩn bị định nghĩa | S02 vết đếm từ trước giả mã; S03 bảng Links trước phép toán |
| Lecture 02, S02-01b–S02-09, S04-01–S04-09 | Giữ cùng dữ liệu và đơn vị qua nhiều bước | Bốn hàng Links qua chiếu, nối, chi phí; bảng từng tầng trước tổng |
| Lecture 03, S02-02–S02-07, S03-03a/b/c | Cận cụ thể trước khái niệm, chỉ rõ chỗ dùng giả thiết | S05 lưới4×4 trước công thức tổng; biên961; S06 mỗi cặp ảnh trước q/rho |

Chỉ kế thừa cách giải thích, không sao chép nội dung toán hoặc CSS. Các chứng minh cần sinh viên năm2 theo dõi được dựa vào bất biến tổng, đủ/chỉ các đóng góp và kiểm tra điều kiện; không dùng Lagrange để tối ưu b,c trong phần bắt buộc.

Hiệu chỉnh sau review sinh viên: bảng chi phí đếm từ dùng byte, $I+5B$ và $I+4B$, với $B$ là độ dài một cặp; ghi rõ $M$ ở phần chi phí không phải ma trận. Trang phép chọn có hai hàng lấy ra từ bảng Links minh họa trước ký hiệu.
