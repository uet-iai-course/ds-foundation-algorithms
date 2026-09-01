# Goal ghi chú Bài 06

## 1. Goal

Hoàn thiện ghi chú tự học **Bài 06 — Tìm cặp tương đồng bằng băm nhạy cảm cục bộ** tại `2627-1/materials/lec-06/lecture-note.md`. Tài liệu phải giúp sinh viên đi từ chữ ký MinHash đến tập ứng viên, chứng minh công thức xác suất của phép phân dải, đặc tả thuật toán và chi phí, rồi phân biệt đúng các họ LSH cho Hamming, cosin và Euclid. Ghi chú dùng cùng ký hiệu và thứ tự khái niệm với deck nhưng không chép lại trang chiếu.

## 2. Vấn đề trung tâm

Chữ ký MinHash làm mỗi tài liệu ngắn hơn nhưng vẫn để lại $\binom N2$ cặp. Bài 06 xây một tầng lọc xác suất: chỉ những cặp trùng ít nhất một khóa dải mới trở thành ứng viên, sau đó mới được đối chiếu chính xác. Thiết kế phải đồng thời kiểm soát xác suất bỏ sót, số ứng viên giả, khối lượng truyền và bộ nhớ.

## 3. Bằng chứng hoàn thành

- Người học dùng Ví dụ 3.10 để tính quy mô quét mọi cặp và chỉ ra vì sao nén chữ ký chưa giải quyết số cặp.
- Người học tạo đúng khóa `(chỉ-số-dải, vector-r-hàng)`, suy ra $q(s)=1-(1-s^r)^b$, tính Ví dụ 3.12 và ngưỡng nửa chính xác.
- Người học đặc tả thuật toán tạo tập ứng viên không thứ tự, chứng minh bất biến loại trùng, nêu hậu kiểm và phân biệt chi phí bản ghi với khối lượng từ truyền.
- Người học phát biểu họ LSH bằng hai ngưỡng gần–xa, hai cận xác suất và không gán bảo đảm cho vùng giữa.
- Người học suy ra phép khuếch đại AND/OR dưới giả thiết độc lập và giữ đúng thứ tự ghép trong Bài 3.6.1.
- Người học phân biệt miền, nguồn ngẫu nhiên, xác suất va chạm và trường hợp biên của Hamming, cosin và Euclid.
- Người học tính đúng xác suất mô hình vân tay và phân biệt mô hình sách với bằng chứng thực nghiệm.
- Ba bài MMDS 3.4.4, 3.6.1 và 3.8.2 giữ nguyên dữ kiện, yêu cầu và có lời giải kiểm được.
- Markdown, công thức, SVG, liên kết, bàn phím, màn hình rộng, màn hình hẹp, bản in và ràng buộc an toàn của viewer đều qua kiểm định trước khi cập nhật index.

## 4. Đầu ra

- `2627-1/materials/lec-06/lecture-note.md`.
- Các cập nhật liên quan đến ghi chú trong `2627-1/planning/lec-06/outline.md`, `storyboard.md` và `review-log.md`.
- Chỉ tạo thêm SVG nếu mười SVG hiện có chưa đủ cho một lập luận bắt buộc.
- Một liên kết ghi chú đúng mẫu trong `2627-1/index.html`, chỉ thêm sau khi viewer đạt mọi cổng.
- Không sửa deck trừ khi phát hiện thay đổi dùng chung về ký hiệu, giả thiết, ví dụ, kết luận hoặc thứ tự khái niệm; nếu có, ghi tác động trước khi sửa.

## 5. Đối tượng và tiên quyết

Sinh viên đại học đã học lập trình, toán rời rạc, đại số tuyến tính và xác suất cơ bản; đã hoàn thành Bài 05 về shingle, Jaccard, MinHash và chữ ký. Có thể dùng xác suất độc lập, tích vô hướng, góc, ba khoảng cách và mô hình MapReduce của Bài 02, nhưng phải nhắc ngắn ý nghĩa trước lần dùng quyết định.

## 6. Phạm vi nguồn

- Bản đồ học phần: `sources/source.md`, mục Bài 06; ánh xạ slide: `sources/reference-slides/README.md`, dòng Bài 06.
- Nguồn trục: *Mining of Massive Datasets*, ấn bản 3, Chương 3, §§3.4, 3.6–3.8; §3.5 chỉ dùng cho định nghĩa khoảng cách; Ví dụ 3.10–3.12, 3.18 và các ví dụ vân tay; Bài 3.4.4, 3.6.1, 3.8.2.
- Slide MMDS `ch03-lsh.pdf`; Stanford CS246 `03-lsh.pdf`, `04-lsh_theory.pdf` dùng để đối chiếu từng cụm. Ưu tiên MMDS khi tương đương; dùng Stanford cho cấu trúc khuếch đại nếu rõ hơn và kiểm lại bằng sách.
- Datar, Immorlica, Indyk và Mirrokni, “Locality-Sensitive Hashing Scheme Based on p-Stable Distributions”, SoCG 2004, DOI `10.1145/997817.997857`; bản tác giả tại `https://immorlica.com/pubs/pstable.pdf`. Codex chính đã kiểm trực tiếp §3.2 để xác minh $h_{a,u}(v)=\lfloor(a\cdot v+u)/w\rfloor$, $u$ đều trên $[0,w]$ và các tọa độ của $a$ lấy độc lập từ phân phối $p$-ổn định. Chỉ dùng phần này để lấp khoảng trống nguồn của công thức Euclid đang có trong deck.
- Deck, planning và mười SVG Bài 06 hiện có là nguồn đồng bộ sản phẩm, không thay giáo trình làm căn cứ học thuật.
- Các phân tích $A=\sum_B\binom{|B|}{2}$, `bN+A` bản ghi và $\Theta(pN+A)$ từ là phần làm chặt của học phần, phải ghi rõ mô hình chi phí.

## 7. Bản đồ chủ đề

| `note-topic-id` | Nhãn | Chủ đề, nguồn và sản phẩm | Chuỗi trình bày và kết nối |
|---|---|---|---|
| `L06-N01` | cầu nối | Từ chữ ký đến nút thắt số cặp; MMDS Ví dụ 3.10. Sản phẩm: tính $\binom N2$ và phân biệt giảm chiều với giảm số cặp. | Vai trò → đặc tả $N,p$ → ví dụ quy mô → chi phí → kiểm tra. Định lý và thuật toán không áp dụng vì đây là mục định hướng. Dẫn sang `L06-N02`. |
| `L06-N02` | cốt lõi | Phân dải và khóa đầy đủ; MMDS §§3.4.1–3.4.2. Sản phẩm: chia $p=br$, tạo ngăn và định nghĩa cặp ứng viên. | Vai trò → đặc tả → ví dụ khóa → trực quan dải → thủ tục tạo ngăn → lỗi va chạm mã băm → kiểm tra. Dẫn sang xác suất ở `L06-N03`. |
| `L06-N03` | cốt lõi | Đường cong ứng viên; MMDS §3.4.2, Ví dụ 3.11–3.12. Sản phẩm: suy ra $q(s)$, biên, $s_{1/2}$ và hướng đổi $b,r$. | Vai trò → giả thiết độc lập → ví dụ → trực quan đường cong S → mệnh đề → chứng minh bù → tham số, lỗi và kiểm tra. Dẫn sang thuật toán ở `L06-N04`. |
| `L06-N04` | cốt lõi | Thuật toán tạo và hậu kiểm ứng viên; MMDS §§3.4.1, 3.4.3 và Bài 3.4.4. Sản phẩm: giả mã, bất biến, dừng và chi phí $A,|C|$. | Vai trò → đầu vào/đầu ra → vết ngăn nhỏ → luồng hai công việc → thuật toán → chứng minh bất biến → I/O, bộ nhớ, lỗi và kiểm tra. Dẫn sang ngôn ngữ chung ở `L06-N05`. |
| `L06-N05` | cốt lõi | Định nghĩa họ LSH; MMDS §§3.6.1–3.6.2, Ví dụ 3.18. Sản phẩm: phát biểu $(d_1,d_2,\alpha_1,\alpha_2)$ đúng miền và vùng bảo đảm. | Vai trò → đặc tả $h\sim F$ → ví dụ Jaccard → trực quan hai miền → mệnh đề → kiểm giả thiết → vùng giữa và kiểm tra. Dẫn sang khuếch đại. |
| `L06-N06` | cốt lõi | Khuếch đại AND/OR; MMDS §3.6.3. Sản phẩm: suy ra $\rho^r$ và $1-(1-\rho)^b$, rồi ghép đúng thứ tự. | Vai trò → định nghĩa phép ghép → ví dụ → trực quan → công thức → chứng minh bằng độc lập → đánh đổi và kiểm tra. Cấp công cụ cho ba họ và vân tay. |
| `L06-N07` | cốt lõi | LSH Hamming; MMDS §3.7.1. Sản phẩm: chứng minh xác suất $1-H(x,y)/m$. | Vai trò → miền và đặc tả → ví dụ bit → trực quan tọa độ → mệnh đề → đếm tọa độ trùng → giới hạn họ chỉ có $m$ hàm, kiểm tra. |
| `L06-N08` | cốt lõi | LSH cosin; MMDS §3.7.2. Sản phẩm: giải thích siêu phẳng ngẫu nhiên và chứng minh xác suất $1-\theta/\pi$. | Vai trò → vector khác 0 và pháp tuyến đẳng hướng → ví dụ góc → trực quan nêm góc → mệnh đề → lập luận hình học → radian, vector 0, Rademacher và kiểm tra. |
| `L06-N09` | cốt lõi | LSH Euclid; MMDS §§3.7.4–3.7.5 và Datar et al. §3.2. Sản phẩm: phân biệt xây dựng hình học 2D của MMDS với họ chiếu dịch $p$-ổn định. | Vai trò → đặc tả ngẫu nhiên → ví dụ hai hình chiếu → trực quan ngăn dịch → mệnh đề có điều kiện → lập luận xác suất → giới hạn, tham số và kiểm tra. Không suy diễn công thức đóng ngoài nguồn. |
| `L06-N10` | cốt lõi | Mô hình khớp vân tay; MMDS §§3.8.4–3.8.5. Sản phẩm: tính xác suất bộ ba, OR 1024 và AND hai tầng. | Vai trò → mô hình ô lưới → ví dụ → trực quan hai ngăn → mệnh đề xác suất → tính theo độc lập → giới hạn mô hình và kiểm tra. |
| `L06-N11` | cầu nối | Ba bài tập nguồn và tổng hợp; MMDS 3.4.4, 3.6.1, 3.8.2. Sản phẩm: lời giải truy nguyên được và bảng tự kiểm. | Đặc tả đề → vết tính/luồng → kết quả → lỗi dễ mắc. Các thành phần được gộp theo từng bài vì chúng đo trực tiếp `L06-N04`, `L06-N06`, `L06-N10`. Kết thúc ở ranh giới sang Bài 07. |

## 8. Chủ đề bổ sung đề xuất

- `L06-S01` — **bổ sung, giữ**: khóa dải gồm chỉ số dải và vector đầy đủ; kiểm tra bằng nhau sau khi mã băm trùng. Khoảng trống là cách triển khai có thể tạo ứng viên sai nếu coi mã băm là khóa học thuật.
- `L06-S02` — **bổ sung, giữ**: phân biệt số bản ghi trung gian `bN+A` với khối lượng từ $\Theta(pN+A)$ và tập $C$ sau loại trùng. Khoảng trống là định nghĩa thuật toán chưa đủ để đánh giá I/O.
- `L06-S03` — **bổ sung, giữ có nguồn**: công thức chiếu–dịch Euclid từ Datar et al. §3.2. Chỉ dùng để giải thích công thức đã có trong deck; không mở rộng sang thuật toán lân cận gần đúng hoặc cận truy vấn của bài báo.
- Không thêm tối ưu tham số thực nghiệm, multiprobe LSH, HNSW, PQ, IVF-PQ hoặc triển khai thư viện. Chúng không cần cho mục tiêu và thuộc bài sau hoặc ngoài học phần.

## 9. Khuôn trình bày

Mỗi chủ đề cốt lõi theo thứ tự: vai trò và nhu cầu; định nghĩa hoặc đặc tả; ví dụ chạy tay; ý nghĩa trực quan; mệnh đề hoặc thuật toán; chứng minh hay lập luận đúng; ứng dụng, lỗi dễ mắc và kiểm tra. Dùng cùng ký hiệu từ ví dụ sang công thức, giả mã và chi phí. Tách rõ xác suất cơ sở, phép khuếch đại và hậu kiểm chính xác. Công thức Markdown chỉ dùng `$...$` và `$$...$$`; khối `hint` và `solution` không lồng nhau. Văn phong thuần Việt, trực tiếp, không chứa hướng dẫn quy trình sản xuất tài liệu.

## 10. Ngoài phạm vi

- HNSW, Product Quantization, IVF-PQ, Z-order curve, API và triển khai cụm.
- Tối ưu truy vấn lân cận gần đúng và các cận không được dạy trong MMDS Chương 3.
- Entity resolution ngoài ví dụ cần thiết; bằng chứng hiệu năng hiện thời cho nhận dạng vân tay.
- Khoảng cách hoặc họ băm khác Hamming, cosin và Euclid.
- Số liệu tự tạo, giả thiết độc lập ngầm hoặc tuyên bố bảo đảm trong vùng giữa hai ngưỡng LSH.

## 11. Rủi ro và điểm cần duyệt

- MMDS dùng điều kiện gần $d\le d_1$ và xa $d\ge d_2$; ghi chú theo quy ước này. Không trộn với bất đẳng thức nghiêm của một số slide Stanford.
- Công thức $q(s)$ và AND/OR chỉ đúng theo dạng lũy thừa khi các phép băm liên quan độc lập.
- Ngưỡng nửa là $(1-2^{-1/b})^{1/r}$; $(1/b)^{1/r}$ chỉ là xấp xỉ thường dùng.
- Với cosin, $\theta$ đo bằng radian, hai vector phải khác 0 và pháp tuyến phải đẳng hướng. Vector Rademacher không cho công thức chính xác nói chung.
- Với Euclid, MMDS §3.7.4 cho xây dựng đường/ngăn 2D và một họ $(a/2,2a,1/2,1/3)$; câu điều kiện in trong sách có dấu hiệu đảo chiều. Không lặp mệnh đề sai `d1 < 4d2`; chỉ phát biểu hệ quả đã kiểm hoặc dùng dạng tổng quát §3.7.5. Công thức chiếu–dịch phải dẫn Datar et al.
- Bài 3.8.2: OR 2048 cho tỷ lệ âm tính giả khoảng $0.000224$, không phải $0.9998$; số sau là xác suất dương tính thật. AND của hai OR 1024 cho âm tính giả khoảng $0.02968$ và dương tính giả khoảng $0.00402$.
- Chỉ dùng `img/lec-06/...` trong Markdown và `lecture-06-tim-cap-tuong-dong-bang-lsh.html` cho liên kết deck.
- Nếu năm reviewer phát hiện thay đổi ảnh hưởng ký hiệu, giả thiết, ví dụ, kết luận hoặc thứ tự dùng chung, phải rà deck và ghi quyết định trong `review-log.md`.

## 12. Kế hoạch tác tử

1. Đã chạy độc lập reader lập kế hoạch, reader ánh xạ nguồn và reviewer bản đồ chủ đề bằng `z-ai/glm-5.3-flash`; Codex chính đã đối chiếu và hợp nhất goal.
2. Writer `deepseek/deepseek-v4-flash-0731` soạn một tệp ghi chú trên hồ sơ đã lọc, không nhận bí mật hoặc thông tin xác thực.
3. Năm reviewer GLM độc lập kiểm: nguồn/phạm vi; toán và thuật toán; mạch sư phạm; thuật ngữ–ký hiệu–liên tục; viewer và khả năng tiếp cận.
4. Codex chính chỉ áp dụng các sửa có căn cứ đã được phê duyệt, rồi chạy GLM tái kiểm cho thay đổi toán hoặc mạch.
5. Dùng `$no-ai-slop` biên tập bản cuối và tự kiểm theo `eval.md`; dùng `$quill` rà dàn ý, mạch, thuật ngữ và ký hiệu, không tạo `quill.json`.
6. Kiểm định viewer ở màn hình rộng/hẹp, bàn phím, bản in, công thức, SVG, liên kết và từ chối đường dẫn không hợp lệ. Chỉ sau đó cập nhật index, commit, push và kiểm SHA trên `origin/main`.

## 13. Trạng thái

**Hoàn tất.** Ba vai GLM đã kiểm hồ sơ; writer DeepSeek soạn bản nháp; năm reviewer GLM và hai lượt tái kiểm đã hoàn tất. Codex chính áp dụng các sửa đã duyệt, dùng `$no-ai-slop` và `$quill`, rồi kiểm viewer ở màn hình rộng, hẹp, bàn phím, bản in và các ràng buộc an toàn. Index chỉ được cập nhật sau khi mọi cổng đạt.
