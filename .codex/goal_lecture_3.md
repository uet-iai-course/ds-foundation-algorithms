# Goal brief — Ghi chú Bài 03

## 1. Goal

Xây dựng ghi chú tự học độc lập cho Bài 03, giúp sinh viên mô hình hóa PageRank trên đồ thị Web thưa, xử lý nút cụt và bẫy nhện, chứng minh phép lặp có hệ số giảm hội tụ, đặt điều kiện dừng có bảo đảm và chuyển một vòng tính sang biểu diễn thưa bằng MapReduce.

## 2. Vấn đề trung tâm

Đầu vào là đồ thị Web có hướng $G=(V,E)$ với $n=|V|$ trang và $m=|E|$ cạnh sau khi gộp liên kết lặp. Cần tạo một phân phối hạng $r$ phản ánh dòng truy cập của người lướt ngẫu nhiên. Ma trận chuyển là thưa nhưng quá lớn để vật chất hóa như ma trận đặc; đồ thị còn có thể chứa nút cụt và bẫy nhện làm mất hoặc giữ toàn bộ khối lượng.

Ghi chú phải xây tới một phép lặp PageRank đã sửa nút cụt và có hệ số giảm, chứng minh tính đúng trên miền các phân phối xác suất, nêu cận sai số từ phần dư, rồi hiện thực cùng phép cập nhật bằng các bản ghi thưa và các pha MapReduce có chi phí mỗi vòng tuyến tính theo kích thước đồ thị.

## 3. Bằng chứng hoàn thành

- Đặc tả rõ đồ thị, quy ước cạnh, ma trận chuyển cột, vector xác suất, phương trình cố định và miền của mọi ký hiệu.
- Có vết chạy kiểm tra được trên đồ thị $y,a,m$; tách đúng đồ thị cơ sở, biến thể nút cụt và biến thể bẫy nhện.
- Giải thích và tính được lượng khối lượng mất ở nút cụt; chứng minh phép sửa cột bảo toàn tổng xác suất.
- Phát biểu chính xác phép cập nhật có hệ số giảm trên simplex xác suất; chứng minh ánh xạ co theo chuẩn $L_1$, nghiệm duy nhất, hội tụ và cận hậu nghiệm.
- Thuật toán lặp có đầu vào, đầu ra, điều kiện trước/sau, $\tau$, $\varepsilon$, $K_{\max}$, điều kiện dừng và hai trạng thái trả về.
- Một vòng phân tán giữ cấu trúc cho mọi nút, không cộng hai lần khối lượng nút cụt, phân biệt $\delta$ với $\Delta$ và nêu chi phí theo cả biểu thức nguồn lẫn $\Theta(n+m)$.
- Bốn bài tập MMDS 5.1.1, 5.1.2, 5.2.1 và 5.2.2 giữ nguyên dữ kiện, hình và yêu cầu; có gợi ý và lời giải kiểm tra được.
- Mọi mệnh đề phân biệt được giữa phát biểu của MMDS/Stanford, hệ quả chứng minh trực tiếp từ đặc tả và quyết định ký hiệu của học phần. Các tiêu chí này không thay thế tiêu chí bàn giao cuối trong `AGENTS.md`.

## 4. Đầu ra

- `2627-1/materials/lec-03/lecture-note.md`;
- chỉ sửa hoặc thêm SVG trong `2627-1/img/lec-03/` nếu ghi chú thực sự cần; mặc định tái sử dụng năm SVG hiện có;
- cập nhật phần ghi chú trong:
  - `2627-1/planning/lec-03/outline.md`;
  - `2627-1/planning/lec-03/storyboard.md`;
  - `2627-1/planning/lec-03/review-log.md`;
- thêm tài nguyên Ghi chú Bài 03 trong `2627-1/index.html` sau khi viewer đạt kiểm định.

Không viết lại `2627-1/lecture-03-pagerank-mo-hinh-va-tinh-toan.html`. Chỉ sửa deck nếu ghi chú làm thay đổi ký hiệu, giả thiết, ví dụ hoặc kết luận dùng chung và việc rà đồng bộ chứng minh sửa là cần thiết.

## 5. Đối tượng và tiên quyết

Có thể giả định:

- Bài 02: Map function, Reduce function, nhóm theo khóa, bản ghi cấu trúc, task và chi phí dữ liệu trung gian;
- đồ thị có hướng, bậc ra, đường đi và liên thông mạnh ở mức cơ bản;
- vector cột, nhân ma trận–vector, chuẩn $L_1$;
- phân phối xác suất, xác suất có điều kiện và tổng xác suất bằng 1.

Cần khôi phục ngắn trước khi dùng:

- ma trận cột ngẫu nhiên và simplex xác suất;
- trị riêng/vector riêng chỉ ở mức đọc phương trình cố định;
- bất khả quy và không chu kỳ như hai điều kiện đủ cho hội tụ của chuỗi hữu hạn khi không có dịch chuyển ngẫu nhiên;
- tổng của chuỗi hình học để suy ra cận hậu nghiệm.

## 6. Phạm vi nguồn

| Nguồn | Phần dùng | Vai trò | Quyết định |
|---|---|---|---|
| `sources/source.md` | Bài 03, tình huống mở bài, thứ tự và mạch Bài 02→03→04 | Chốt phạm vi cấp học phần | Cao nhất |
| MMDS 3e Chương 5 | §5.1.2–5.1.5; §5.2.1–5.2.2; Bài 5.1.1–5.1.2, 5.2.1–5.2.2 | Định nghĩa, mô hình, lỗi cấu trúc, biểu diễn thưa, MapReduce và bài tập | Nguồn nội dung chính |
| Slide chính thức MMDS Chương 5 phần 1 | Slide 16–46, 48, 52–55; slide 35–37 làm phản ví dụ hội tụ | Đồ thị $y,a,m$, vết chạy, trực quan, giả mã và ví dụ số | Ưu tiên khi tương đương; ghi công `http://www.mmds.org` |
| Stanford CS246 `09-pagerank.pdf` | Cụm người lướt ngẫu nhiên, phân phối dừng và trực quan tính toán tương ứng | Cầu nối hành vi–phương trình | Chỉ dùng nơi trực quan rõ hơn; MMDS kiểm chứng nội dung |
| Deck và planning Bài 03 | Toàn bộ | Giữ ký hiệu, ba biến thể đồ thị và các số đã rà | Nguồn biên tập thứ cấp |

MMDS trình bày cả xóa đệ quy nút cụt và bù/dịch chuyển. Ghi chú chọn quy ước cột nút cụt bằng $e/n$ vì nối trực tiếp với phép lặp và triển khai thưa; cách xóa đệ quy chỉ được nêu như một lựa chọn của sách. Stanford không thay MMDS làm nguồn cho định nghĩa hoặc bài tập.

## 7. Bản đồ chủ đề

| `note-topic-id` | Thứ tự | Chủ đề | Nhãn | Kết nối vào | Kết nối ra | Nguồn và quyết định |
|---|---:|---|---|---|---|---|
| `note-topic-03-web-graph` | 1 | Đồ thị Web có hướng và tính thưa | cốt lõi | Bài 02 | người lướt và đóng góp | MMDS §5.1.2, §5.2.1; giữ ngắn nhưng phải đặc tả miền |
| `note-topic-03-random-surfer` | 2 | Người lướt ngẫu nhiên và phân phối hạng | cầu nối | đồ thị | phương trình luồng | MMDS §5.1.2; Stanford bổ trợ trực giác |
| `note-topic-03-flow-matrix` | 3 | Đóng góp theo cạnh, ma trận cột và vết chạy $y,a,m$ | cốt lõi | người lướt | lỗi cấu trúc | MMDS slide 16–27 và §5.1.2; giữ |
| `note-topic-03-dead-end` | 4 | Nút cụt và sửa cột | cốt lõi | ma trận chuyển | bẫy nhện, triển khai thưa | MMDS §5.1.4, slide 38, 41–43; giữ và tách biến thể |
| `note-topic-03-spider-trap` | 5 | Bẫy nhện, hệ số giảm và dịch chuyển ngẫu nhiên | cốt lõi | nút cụt | hội tụ | MMDS §5.1.5, slide 39, 44–46; giữ và tách nghiệm |
| `note-topic-03-convergence` | 6 | Điều kiện hội tụ và ánh xạ co trên simplex | bổ sung | $A_\beta$ | cận dừng | Phản ví dụ từ MMDS slide 35–37; chứng minh co suy trực tiếp từ đặc tả; giữ có điều kiện |
| `note-topic-03-stopping` | 7 | Thuật toán lặp và cận dừng hậu nghiệm | bổ sung | ánh xạ co | tính toán thưa | Tiêu chí phần dư từ slide 25, 52; cận là hệ quả chứng minh; giữ có điều kiện |
| `note-topic-03-sparse-mapreduce` | 8 | Biểu diễn thưa và một vòng PageRank bằng MapReduce | cốt lõi | Bài 02, nút cụt, điều kiện dừng | kết luận | MMDS §5.2.1–5.2.2, slide 48, 52–55; giữ, không dạy API |
| `note-topic-03-exercises` | 9 | Bài tập MMDS 5.1.1–5.2.2 | cốt lõi luyện tập | các chủ đề trên | tự đánh giá | giữ nguyên dữ kiện và dùng hai SVG Hình 5.4, 5.7 |
| `note-topic-03-boundary` | 10 | Ranh giới sang Bài 04 | đọc thêm | kết luận PageRank cơ sở | Bài 04 | chỉ liên kết ra; không soạn mệnh đề Topic-Sensitive/Spam/HITS |

Đồ thị tiên quyết: `web-graph → random-surfer → flow-matrix → {dead-end, spider-trap} → convergence → stopping → sparse-mapreduce → exercises`. Tình huống đồ thị Web lớn phải trở lại ở biểu diễn thưa, chi phí mỗi vòng và kết luận.

## 8. Chủ đề bổ sung đề xuất

### Ánh xạ co trên simplex xác suất

- Khoảng trống: tiêu chí “vector thay đổi ít” của slide chưa cho biết khoảng cách đến nghiệm, còn phát biểu hội tụ lý tưởng của sách thiếu điều kiện không chu kỳ.
- Nguồn và căn cứ: MMDS định nghĩa $A_\beta$ và cung cấp phản ví dụ chu kỳ; phần co được chứng minh trực tiếp từ ma trận cột ngẫu nhiên trên simplex, không gán nguyên văn cho MMDS.
- Quyết định: `đưa vào` như một bổ sung có chứng minh đầy đủ. Phải nêu miền $\mathcal S=\{r\ge0:e^Tr=1\}$; với $x,y\in\mathcal S$, $U(x-y)=0$, nên $\|A_\beta x-A_\beta y\|_1\le\beta\|x-y\|_1$.

### Cận dừng hậu nghiệm

- Khoảng trống: phần dư giữa hai vòng không tự đồng nhất với sai số tới nghiệm.
- Nguồn và căn cứ: suy ra bằng tổng chuỗi hình học từ bất đẳng thức co vừa chứng minh.
- Quyết định: `đưa vào` trong cùng tuyến, không tạo “định lý của MMDS”. Cần kiểm tra chỉ số để dùng đúng $\beta\Delta_t/(1-\beta)$ theo định nghĩa $\Delta_t=\|r^{(t)}-r^{(t-1)}\|_1$.

### Điều kiện không chu kỳ khi $\beta=1$

- Khoảng trống: MMDS slide 35–37 cho phản ví dụ chu kỳ nhưng không gọi tên điều kiện; phát biểu trong sách không đủ để bảo đảm hội tụ từ mọi phân phối đầu.
- Quyết định: `đưa vào` như cầu nối ngắn. Chỉ nêu bất khả quy và không chu kỳ là điều kiện đủ; không triển khai lý thuyết chuỗi Markov tổng quát. Trọng tâm bảo đảm của bài vẫn là trường hợp $0<\beta<1$ được chứng minh trực tiếp.

### Block-striping, combiner và các tối ưu §5.2.3–5.2.5

- Nguồn có nhưng vượt sản phẩm “một vòng PageRank bằng MapReduce”.
- Quyết định: `đọc thêm`; không đưa vào tuyến chính và không phân tích các công thức theo $k$ ngoài một ghi chú nguồn nếu cần đối chiếu.

## 9. Khuôn trình bày

| Chủ đề | Thành phần bắt buộc | Không áp dụng |
|---|---|---|
| Web graph, random surfer | vai trò, định nghĩa, trực quan, ví dụ, lỗi dễ mắc, kiểm tra | thuật toán và chứng minh mới |
| Flow–matrix | vai trò, đặc tả, vết chạy, trực quan, phương trình cố định, power iteration, lập luận đúng, chi phí, kiểm tra | không |
| Dead end | định nghĩa, biến thể chạy tay, mất khối lượng, sửa cột, chứng minh bảo toàn, biên và kiểm tra | không |
| Spider trap | định nghĩa, biến thể chạy tay, $A_\beta$, nghiệm có nguồn, trực quan và kiểm tra | thuật toán riêng ngoài phép lặp chung |
| Convergence | miền simplex, mệnh đề, giả thiết, phản ví dụ $\beta=1$, chứng minh co cho $0<\beta<1$, kết luận duy nhất/hội tụ, kiểm tra | triển khai Markov tổng quát |
| Stopping | đặc tả, giả mã, điều kiện dừng, cận hậu nghiệm, chứng minh, $K_{\max}$, hai hậu điều kiện, lỗi chỉ số | hình học riêng |
| Sparse MapReduce | đặc tả bản ghi, ví dụ một nút, giả mã hoặc luồng, bất biến giữ cấu trúc, $\delta$, $\Delta$, chi phí và kiểm tra | API Hadoop |
| Exercises | đề nguồn, hình, gợi ý, lời giải, kiểm tra giả thiết và kết quả | định lý hoặc thuật toán mới |

## 10. Ngoài phạm vi

- Topic-Sensitive/Personalized PageRank, link spam, TrustRank, Spam Mass và HITS.
- Mục MMDS 5.3–5.5 và phần tương ứng cuối hai bộ slide.
- Hướng dẫn Hadoop, Spark hoặc API cụ thể; mã trình diễn và bộ dữ liệu mới.
- Block-striping, block-stripe thưa và tối ưu combiner của §5.2.3–5.2.5 trong tuyến chính.
- Bài tập khác ngoài 5.1.1, 5.1.2, 5.2.1 và 5.2.2.
- Sửa dữ kiện, cạnh hoặc yêu cầu của Hình 5.4 và Hình 5.7.
- Viết lại deck khi chưa có sai khác dùng chung cần đồng bộ; tạo `quill.json`.

## 11. Rủi ro và điểm cần duyệt

- Đồ thị cơ sở có $m\to a$, biến thể bẫy có $m\to m$, còn biến thể nút cụt bỏ cạnh ra của $m$; không dùng chung ma trận hoặc nghiệm.
- $A_{0,8}$ và $(7/33,5/33,21/33)^T$ thuộc biến thể bẫy; $(35/93,37/93,21/93)^T$ thuộc đồ thị cơ sở có hệ số giảm.
- Phép co chỉ đúng với hệ số $\beta$ trên hiệu của hai phân phối có cùng tổng; phải nêu miền simplex để số hạng $U(x-y)$ triệt tiêu.
- Cần cố định định nghĩa $\Delta_t$ trước khi dùng cận, tránh lệch một chỉ số hoặc thiếu hệ số $\beta$.
- Ký hiệu $P_0$ và $\bar P$ là quyết định biên tập; triển khai thưa dùng $\delta=d^Tr$ phải được trình bày là tương đương với cột nút cụt $e/n$, không cộng thêm lần hai.
- Biến $S$ trong giả mã slide là tổng khối lượng sau bước nhân thưa, không đồng nhất về tên với $\delta$; writer phải diễn giải quan hệ thay vì đổi ngầm.
- $\Theta(n+m)$ là cách viết tiệm cận cho một vòng; cần đặt cạnh biểu thức hoặc phép đếm bản ghi nguồn và không tính số vòng hội tụ vào cùng cận.
- Các con số quy mô Web trong slide là ví dụ lịch sử của nguồn, không phải số đo hiện tại.
- Bài 5.2.1 cần giả thiết $n\ge2$ để $\lceil\log_2n\rceil$ không bằng 0; Hình 5.4 và 5.7 phải dùng đúng năm SVG hiện có.

## 12. Kế hoạch tác tử

| Giai đoạn | Vai trò/model | Hồ sơ | Trạng thái và cổng |
|---|---|---|---|
| Lập kế hoạch | OpenRouter reader, GLM | `plan` | hoàn tất; metadata khớp OpenRouter |
| Ánh xạ nguồn | OpenRouter reader, GLM | `source` | hoàn tất sau một lượt lỗi tool-call limit và thử lại trên hồ sơ thu hẹp |
| Bản đồ chủ đề | OpenRouter reviewer, GLM | `review` | hoàn tất; Codex chính hợp nhất |
| Soạn trong thư mục tạm | OpenRouter writer `deepseek/deepseek-v4-flash-0731` | `write` | chờ goal được duyệt |
| Năm lượt rà độc lập | OpenRouter reviewers `z-ai/glm-5.3-flash` | `review` | chờ bản nháp |
| Hợp nhất và sửa | Codex chính | phát hiện đã duyệt | chờ năm báo cáo; được phép sửa trực tiếp |
| Biên tập bản cuối | Codex chính với `$no-ai-slop` và `$quill` | tự kiểm | chờ sửa kỹ thuật |
| Rà lại | OpenRouter reviewers GLM | `recheck` | chờ thay đổi kỹ thuật/mạch |
| Viewer, index, commit/push | Codex chính | kiểm định cục bộ | chờ mọi cổng trước |

Chỉ gửi tệp cần thiết đã lọc tới OpenRouter; loại `.env`, khóa, token, mật khẩu, cookie, khóa riêng và thông tin xác thực. Không đổi model hoặc nhà cung cấp khi worker lỗi. Mỗi commit chỉ chứa đầu ra Bài 03 và tệp dùng chung thực sự đã sửa.

## 13. Trạng thái

`sẵn sàng soạn`

MMDS Chương 5, slide chính thức MMDS và Stanford đã được kiểm tra trực tiếp; bốn đề bài cùng hai hình bắt buộc đã được đối chiếu. Nguồn đủ cho phạm vi cốt lõi. Ba bổ sung về điều kiện hội tụ, ánh xạ co và cận dừng được giới hạn ở hệ quả chứng minh trực tiếp từ đặc tả PageRank, không gán cho MMDS và không mở sang lý thuyết Markov tổng quát.
