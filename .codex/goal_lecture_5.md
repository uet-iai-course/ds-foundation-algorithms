# Goal ghi chú Bài 05

## 1. Goal

Hoàn thiện ghi chú tự học **Bài 05 — Biểu diễn tương đồng: Shingling và MinHash** tại `2627-1/materials/lec-05/lecture-note.md`. Tài liệu phải giúp sinh viên tự chuyển tài liệu thành tập shingle, đo Jaccard, chứng minh định lý MinHash, lập chữ ký và phân tích cách quét dữ liệu thưa; dùng cùng ký hiệu và thứ tự khái niệm với deck nhưng không chép lại trang chiếu.

## 2. Vấn đề trung tâm

Một kho lớn có $N$ tài liệu tạo $N(N-1)/2$ cặp cần so sánh. Bài 05 xây một chuỗi biểu diễn kiểm được từ tài liệu đến tập shingle rồi đến chữ ký MinHash để giảm dữ liệu phải đọc cho mỗi cặp. Chuỗi này chưa giảm số cặp; việc tạo tập ứng viên bằng Locality-Sensitive Hashing (LSH) thuộc Bài 06.

## 3. Bằng chứng hoàn thành

- Người học tạo đúng $S_k(D)$ từ một tài liệu đã chuẩn hóa, xử lý $k>n$ và giải thích vì sao băm shingle không đồng nghĩa giảm $k$.
- Người học tính Jaccard bằng giao–hợp và bằng hai con trỏ trên danh sách sắp, nêu quy ước khi hợp rỗng và phân tích chi phí.
- Người học đặc tả MinHash trên vũ trụ hữu hạn, chạy Ví dụ 3.7 và chứng minh $\Pr[h_\pi(C_1)=h_\pi(C_2)]=J(C_1,C_2)$ với hoán vị đều.
- Người học dùng biến chỉ báo để suy ra số hàng trùng có kỳ vọng $pJ$, tỷ lệ hàng trùng không chệch và phương sai $J(1-J)/p$ khi các phép thử độc lập.
- Người học chạy Ví dụ 3.8, nêu bất biến của phép cập nhật `min`, xử lý cột rỗng và suy ra chi phí $O(pu+pz)$ cùng bộ nhớ $\Theta(pN\log(u+1))$ bit dưới mô hình đã nêu.
- Người học phân biệt bảo đảm của hoán vị lý tưởng với hàm băm thực hành có va chạm hoặc không được lấy độc lập–đều.
- Bốn bài MMDS 3.1.1, 3.2.3, 3.3.2 và 3.3.3 giữ nguyên dữ kiện, yêu cầu và có lời giải kiểm được.
- Markdown, công thức, SVG, liên kết, bàn phím, màn hình rộng, màn hình hẹp, bản in và ràng buộc an toàn của viewer đều qua kiểm định trước khi cập nhật index.

## 4. Đầu ra

- `2627-1/materials/lec-05/lecture-note.md`.
- Các cập nhật liên quan đến ghi chú trong `2627-1/planning/lec-05/outline.md`, `storyboard.md` và `review-log.md`.
- Chỉ tạo thêm SVG trong `2627-1/img/lec-05/` nếu ghi chú thực sự cần; ưu tiên năm SVG hiện có.
- Một liên kết ghi chú đúng mẫu trong `2627-1/index.html`, chỉ thêm sau khi viewer đạt mọi cổng.
- Không sửa deck trừ khi phát hiện thay đổi dùng chung về ký hiệu, giả thiết, ví dụ, kết luận hoặc thứ tự khái niệm; nếu có, ghi tác động trước khi sửa.

## 5. Đối tượng và tiên quyết

Sinh viên đại học đã học lập trình, toán rời rạc, đại số tuyến tính và xác suất cơ bản. Ghi chú được phép dùng tập hợp, giao–hợp, hàm băm, biến chỉ báo Bernoulli, kỳ vọng, phương sai, vector 0/1 và ma trận thưa, nhưng phải nhắc ngắn ý nghĩa trước lần dùng quyết định.

## 6. Phạm vi nguồn

- Bản đồ học phần: `sources/source.md`, mục Bài 05.
- Ánh xạ slide: `sources/reference-slides/README.md`, dòng Bài 05.
- Nguồn trục: *Mining of Massive Datasets*, ấn bản 3, Chương 3, §§3.1–3.3; Ví dụ 3.1, 3.3, 3.4, 3.7, 3.8; Hình 3.2–3.4, 3.6; Bài 3.1.1, 3.2.3, 3.3.2 và 3.3.3.
- Slide chính thức MMDS `ch03-lsh.pdf`; Stanford CS246 `03-lsh.pdf` và `04-lsh_theory.pdf` chỉ dùng để đối chiếu từng cụm. Ưu tiên MMDS khi tương đương; không mang banding hoặc đường cong S từ Stanford vào bài.
- Deck, planning và năm SVG Bài 05 hiện có là nguồn đồng bộ sản phẩm, không thay giáo trình làm căn cứ học thuật.
- Hình 3.5 thuộc §3.3.6 nên bị loại cùng phần tăng tốc MinHash; danh sách “Hình 3.2–3.6” trong prompt được hiểu là kiểm tra ranh giới, không phải yêu cầu đưa mọi hình vào ghi chú.
- Phải ghi rõ phần làm chặt của học phần: trường hợp $k>n$, hợp rỗng, tập rỗng, cột chữ ký rỗng, thuật toán hai con trỏ, bất biến quét thưa và phân tích chi phí.

## 7. Bản đồ chủ đề

| `note-topic-id` | Nhãn | Chủ đề, nguồn và sản phẩm | Chuỗi trình bày và kết nối |
|---|---|---|---|
| `L05-N01` | cầu nối | Từ kho tài liệu đến bài toán biểu diễn; MMDS §§3.1–3.3. Sản phẩm: tính số cặp, phân biệt giảm kích thước mỗi tài liệu với giảm số cặp. | Vai trò → đặc tả $N$ và đầu ra → ví dụ $N=10^6$ → chi phí → kiểm tra. Định lý và chứng minh không áp dụng vì đây là mục định hướng. Cấp bài toán cho `L05-N02`. |
| `L05-N02` | cốt lõi | Shingling; MMDS §§3.2.1–3.2.3, Ví dụ 3.3–3.4. Sản phẩm: đặc tả $S_k(D)$, chạy cửa sổ, chọn $k$ và phân biệt băm mã với rút ngắn shingle. | Vai trò → chuẩn hóa và đặc tả → Ví dụ 3.3 → trực quan cửa sổ → thuật toán quét và bất biến → chi phí, va chạm, biên, kiểm tra. Không có định lý riêng; lập luận đúng của phép quét thay cho chứng minh định lý. Dẫn sang `L05-N03`. |
| `L05-N03` | cốt lõi | Độ tương đồng Jaccard; MMDS §3.1.1, Ví dụ 3.1. Sản phẩm: tính giao–hợp, diễn giải X/Y/Z, đặc tả hai con trỏ và xử lý hợp rỗng. | Vai trò → định nghĩa → Ví dụ 3.1 → trực quan ba vùng → thuật toán hai con trỏ → bất biến và dừng → chi phí, lỗi biên, kiểm tra. Dẫn từ phép so sánh chính xác sang nén ở `L05-N04`. |
| `L05-N04` | cốt lõi | MinHash lý tưởng; MMDS §§3.3.1–3.3.3, Hình 3.2–3.3, Ví dụ 3.7. Sản phẩm: đặc tả $h_\pi$, chạy tay và chứng minh định lý xác suất. | Vai trò → $U,A,\pi,h_\pi$ → Ví dụ 3.7 → trực quan phần tử đầu trong hợp → mệnh đề → chứng minh X/Y/Z → biên, kiểm tra. Dẫn sang nhiều phép thử ở `L05-N05`. |
| `L05-N05` | cốt lõi | Chữ ký MinHash; MMDS §3.3.4. Sản phẩm: dựng chữ ký $p$ hàng, chứng minh tính không chệch, phương sai và đánh đổi theo $p$. | Vai trò → đặc tả các phép thử độc lập → ví dụ so hai cột → trực quan tỷ lệ trùng → mệnh đề kỳ vọng/phương sai → chứng minh bằng biến Bernoulli → chi phí, giới hạn, kiểm tra. Dẫn sang cách tính thực hành ở `L05-N06`. |
| `L05-N06` | cốt lõi | Quét ma trận thưa; MMDS §3.3.5, Hình 3.4, Ví dụ 3.8. Sản phẩm: chạy vết cập nhật, đặc tả luồng nhóm theo hàng, giả mã, bất biến, dừng và chi phí. | Vai trò → $SIG,u,z$ và miền ô → Ví dụ 3.8 → trực quan chỉ số 1 có thể hạ min → thuật toán → chứng minh bất biến → thời gian, bộ nhớ, cột rỗng, kiểm tra. Dẫn sang giới hạn ở `L05-N07`. |
| `L05-N07` | cốt lõi | Mô hình lý tưởng và hàm băm thực hành; MMDS §3.3.5 và Bài 3.3.3. Sản phẩm: chỉ ra đúng điều kiện bị mất bởi va chạm hoặc họ hàm cố định. | Vai trò → hai mô hình → phản ví dụ Hình 3.6 → trực quan trùng giả → kết luận có điều kiện → lỗi viện dẫn định lý và kiểm tra. Không có thuật toán hoặc chứng minh mới; mục này kiểm phạm vi áp dụng của `L05-N04`–`L05-N06`. |
| `L05-N08` | cầu nối | Bốn bài tập nguồn và tổng hợp; MMDS 3.1.1, 3.2.3, 3.3.2, 3.3.3. Sản phẩm: lời giải truy nguyên được và bảng tự kiểm cuối bài. | Đặc tả đề → vết tính → kết quả → lỗi dễ mắc. Vai trò, trực quan và lập luận được gộp vào từng lời giải vì bài tập đo trực tiếp `L05-N02`–`L05-N07`. Kết thúc bằng ranh giới sang LSH ở Bài 06. |

## 8. Chủ đề bổ sung đề xuất

- `L05-S01` — **bổ sung, giữ**: quy ước $J(\varnothing,\varnothing)$ là “không xác định” trong học phần và cách loại hai cột toàn $\infty$ khỏi ước lượng. Khoảng trống cụ thể là công thức có mẫu số 0 và dấu canh có thể tạo trùng giả; nội dung hoàn chỉnh đặc tả, không đổi định nghĩa nguồn.
- `L05-S02` — **bổ sung, giữ**: thuật toán hai con trỏ cho hai danh sách shingle đã sắp. Khoảng trống cụ thể là định nghĩa Jaccard chưa cho mô hình truy cập hoặc chi phí; mục này suy trực tiếp từ giao–hợp.
- `L05-S03` — **bổ sung, giữ**: biến chỉ báo Bernoulli cho tỷ lệ hàng chữ ký trùng. Khoảng trống cụ thể là cần phân biệt kỳ vọng $pJ$ của số lần trùng với kỳ vọng $J$ và phương sai của tỷ lệ.
- Không thêm Jaccard distance, Jaccard đa tập, shingle theo từ, Bài 3.3.1 hoặc lịch sử hệ thống phát hiện trùng. Chúng không cần để đạt sản phẩm của bài hoặc đẩy mạch sang nội dung đã chuyển bài.

## 9. Khuôn trình bày

Mỗi chủ đề cốt lõi theo thứ tự: vai trò và nhu cầu; định nghĩa hoặc đặc tả; ví dụ chạy tay; ý nghĩa trực quan; mệnh đề hoặc thuật toán; chứng minh hay lập luận đúng; ứng dụng, lỗi dễ mắc và kiểm tra. Dùng cùng dữ kiện từ ví dụ sang công thức, giả mã và chi phí. Tách rõ “định lý cho hoán vị đều”, “phép thay thế thực hành” và “phần làm chặt của học phần”. Công thức Markdown chỉ dùng `$...$` và `$$...$$`; khối `hint` và `solution` không lồng nhau. Văn phong thuần Việt, trực tiếp, không chứa hướng dẫn quy trình sản xuất tài liệu.

## 10. Ngoài phạm vi

- LSH, banding, đường cong S và nội dung MMDS từ §3.4; chỉ được nhắc một câu để nối sang Bài 06.
- Jaccard distance và các độ đo khoảng cách tổng quát.
- Jaccard đa tập, shingle dựa trên từ, lọc stop-word và §§3.3.6–3.3.7.
- Thư viện MinHash, API, triển khai phân tán và tối ưu hệ thống không có trong nguồn.
- Dữ kiện tự tạo thay bốn bài nguồn hoặc mệnh đề xác suất cho họ hàm băm chưa được chứng minh.

## 11. Rủi ro và điểm cần duyệt

- Hình 3.6 phải đọc đúng: $S_1=\{2,5\}$, $S_2=\{0,1\}$, $S_3=\{3,4\}$, $S_4=\{0,2,4\}$. Tính lại cho thấy ma trận chữ ký trong deck $(5,1,1,1)$, $(2,2,2,2)$, $(0,1,4,0)$ và sáu ước lượng hiện có là đúng. Phát hiện của reader cho rằng đáp án sai bị bác vì reader đã thêm hàng 0 vào $S_1$ và bỏ hàng 0 khỏi $S_2$.
- Hình 3.4 và Hình 3.6 có ma trận cùng bốn cột nhưng khác số hàng và dữ kiện; không tái dùng vết tính.
- Định lý MinHash cần $U$ hữu hạn, tập không rỗng và hoán vị đều. Phương sai cần các phép thử độc lập; một họ hàm băm có va chạm không tự động thỏa các giả thiết này.
- Cận $O(pu+pz)$ giả sử luồng nhóm theo hàng và thao tác băm, lấy min, truy cập ô tốn $O(1)$; nếu không nhóm theo hàng, phải nêu mô hình chi phí tương ứng.
- Bài 3.2.3 phải giữ giả thiết bảng chữ đủ lớn để số chuỗi độ dài $k$ ít nhất là $n$; không trình bày cận đạt được nếu thiếu giả thiết.
- Chỉ dùng `img/lec-05/...` trong Markdown và `lecture-05-bieu-dien-tuong-dong-shingling-va-minhash.html` cho liên kết deck.
- Nếu năm reviewer phát hiện thay đổi ảnh hưởng ký hiệu, giả thiết, ví dụ, kết luận hoặc thứ tự dùng chung, phải rà deck và ghi quyết định trong `review-log.md`.

## 12. Kế hoạch tác tử

1. Đã chạy độc lập reader lập kế hoạch, reader ánh xạ nguồn và reviewer bản đồ chủ đề bằng `z-ai/glm-5.3-flash`; hai vai hết lượt công cụ đã được thử lại cùng model trên dossier hẹp. Codex chính đã đối chiếu và hợp nhất goal.
2. Writer `deepseek/deepseek-v4-flash-0731` soạn một tệp ghi chú trên hồ sơ đã lọc, không nhận bí mật hoặc thông tin xác thực.
3. Năm reviewer GLM độc lập kiểm: nguồn/phạm vi; toán và thuật toán; mạch sư phạm; thuật ngữ–ký hiệu–liên tục; viewer và khả năng tiếp cận.
4. Codex chính chỉ áp dụng các sửa có căn cứ đã được phê duyệt, rồi chạy GLM tái kiểm.
5. Dùng `$no-ai-slop` biên tập bản cuối và tự kiểm theo `eval.md`; dùng `$quill` rà dàn ý, mạch, thuật ngữ và ký hiệu, không tạo `quill.json`.
6. Kiểm định viewer ở màn hình rộng/hẹp, bàn phím, bản in, công thức, SVG, liên kết và từ chối đường dẫn không hợp lệ. Chỉ sau đó cập nhật index, commit, push và kiểm SHA trên `origin/main`.

## 13. Trạng thái

**Sẵn sàng soạn.** Ba vai GLM đã kiểm hồ sơ Bài 05; Codex chính đã đọc trực tiếp MMDS §§3.1–3.3, slide trích xuất, bốn đề bài và tính lại các ví dụ có tranh chấp. Hình 3.5 được loại có lý do vì thuộc §3.3.6. Không còn thiếu nguồn làm thay đổi đáng kể kết quả; mọi bổ sung được giữ ở mức có căn cứ và tách khỏi phát biểu của MMDS.
