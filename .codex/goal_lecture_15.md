# Goal ghi chú Bài 15

## 1. Goal

Hoàn thiện ghi chú tự học **Bài 15 — Thuật toán kết nối dữ liệu** tại `2627-1/materials/lec-15/lecture-note.md`. Tài liệu phải giúp sinh viên chạy, chứng minh và so sánh sáu thuật toán nối theo mô hình I/O, rồi chọn phương án dựa trên điều kiện nối, bộ nhớ, thứ tự, chỉ mục và độ lệch phân hoạch.

## 2. Vấn đề trung tâm

Hai quan hệ `student` và `takes` đều nằm trên đĩa và không vừa bộ nhớ. Mọi thuật toán nối đều phải tạo đúng tích các nhóm khóa trùng, nhưng cách tổ chức lại phép đọc — theo tuple, nhóm khối, chỉ mục, thứ tự hay phân hoạch — quyết định số lần truyền khối và seek.

## 3. Bằng chứng hoàn thành

- Người học phân biệt số tuple, số khối, số khối bộ nhớ, lần truyền khối và seek; không cộng các đại lượng khác đơn vị.
- Người học chạy Nested-Loop, Block Nested-Loop và Indexed Nested-Loop, nêu đúng điều kiện áp dụng và chi phí.
- Người học chạy Sort-Merge trên nhóm khóa trùng, chứng minh không bỏ hoặc lặp cặp và xử lý trường hợp nhóm không vừa bộ nhớ.
- Người học chạy Hash Join trong bộ nhớ, lưu mọi bản sao và kiểm khóa thật sau băm.
- Người học chạy Grace Hash Join qua phân hoạch, xây–dò, skew và đường lui hữu hạn; kiểm riêng điều kiện bộ nhớ của hai pha.
- Người học tính lại ví dụ `student/takes` và các bài 15.3–15.5 mà không đổi dữ kiện nguồn.
- Viewer, Markdown, KaTeX, SVG, liên kết, bàn phím, màn hình rộng/hẹp, bản in và an toàn đường dẫn đều đạt trước khi cập nhật index.

## 4. Đầu ra

- `2627-1/materials/lec-15/lecture-note.md`.
- Cập nhật phần ghi chú trong `2627-1/planning/lec-15/{outline,storyboard,review-log}.md`.
- Dùng mười SVG hiện có trong `2627-1/img/lec-15/`.
- Thêm liên kết ghi chú Bài 15 vào `2627-1/index.html` sau khi viewer đạt.
- Không sửa deck trừ khi phát hiện lỗi nội dung dùng chung cần đồng bộ.

## 5. Nguồn và quyết định chọn nguồn

- *Database System Concepts* 7e, Chương 15, slide 7–9 và 24–40 làm trục cho mô hình chi phí, sáu thuật toán và ví dụ `student/takes`.
- Slide 28, 30, 35 và 40 bị ẩn nhưng chứa nội dung trực tiếp nên vẫn được dùng. Các lỗi slide 33, 37, 39 và 40 giữ bản sửa đã kiểm định trong planning/deck.
- Bài 15.3–15.5 dùng nguyên đề trong Practice Exercises và đối chiếu Practice Solutions trang 112–114. Bài 15.3 giữ kết quả Merge/Hash dạng biểu thức khi đề không cho $M$.
- External Merge Sort chỉ được dẫn lại từ Bài 12; B+-Tree và băm tĩnh dẫn lại từ Bài 13.
- Hybrid Hash Join và mọi nội dung ngoài phạm vi trong prompt bị bỏ, không chuyển sang mục đọc thêm vì nguồn hiện tại không đủ rõ cho bố trí bộ nhớ.

## 6. Bản đồ chủ đề dự kiến

| `note-topic-id` | Nhãn | Chủ đề và sản phẩm | Nguồn, kết nối |
|---|---|---|---|
| `L15-N01` | cầu nối | Tình huống `student/takes`, đặc tả equi-join và mô hình I/O | slide 7–9, 24; Bài 12–13 → các thuật toán |
| `L15-N02` | cốt lõi | Nested-Loop theo tuple | slide 25–26 → gộp khối |
| `L15-N03` | cốt lõi | Block Nested-Loop và hai bố trí $q$ | slide 27–28; Bài 15.3 → chỉ mục |
| `L15-N04` | cốt lõi | Indexed Nested-Loop và chỉ mục thứ cấp | slide 29–30; Bài 13 → thứ tự |
| `L15-N05` | cốt lõi | Sort-Merge, nhóm khóa trùng và chi phí vật chất hóa | slide 31–32; Bài 12 → băm |
| `L15-N06` | cốt lõi | Hash Join trong bộ nhớ | slide 35–36, 39 → Grace |
| `L15-N07` | cốt lõi | Grace: phân hoạch và vết xây–dò | slide 33–37 → điều kiện bộ nhớ |
| `L15-N08` | cốt lõi | Grace: skew, đường lui, tính đúng và chi phí | slide 38–40 → tổng hợp |
| `L15-N09` | cốt lõi | Chọn thuật toán theo điều kiện và đơn vị chi phí | tổng hợp N02–N08 |
| `L15-N10` | cốt lõi | Recitation 15.3–15.4 | Practice Ex/Sol 15.3–15.4 |
| `L15-N11` | cốt lõi | Recitation 15.5 và khép học phần | Practice Ex/Sol 15.5 |

Đồ thị tiên quyết: `N01→N02→N03→N04→N05→N06→N07→N08→N09→{N10,N11}`. Codex chính giữ 11 chủ đề sau khi hợp nhất ba reader; tách Grace thành cơ chế và bảo đảm để tránh dồn điều kiện bộ nhớ, đường lui và chi phí vào một mục quá tải.

## 7. Ký hiệu và hợp đồng phải giữ

- $r,s$ là hai quan hệ; mặc định $s$ là phía xây khi băm. $n_r,n_s$ là số tuple; $b_r,b_s$ là số khối; $M$ là số khối bộ nhớ.
- $q$ là số khối ngoài giữ trong Block Nested: $M-2$ khi giữ riêng bộ đệm đầu ra, $M-1$ khi đầu ra chuyển tiếp.
- $b_b$ là hệ số đọc/ghi liên tiếp của mô hình seek tổng, độc lập với $b_{in},b_{out}$ của pha xây–dò.
- $p_h$ là số phân hoạch; $\alpha\ge1$ là phụ trội bảng băm; $t_T,t_S$ là thời gian truyền khối và seek.
- Chi phí ghi thành cặp `(truyền khối, seek)` hoặc thời gian có ghi rõ đơn vị; không tính ghi kết quả cuối; giả sử không có khối sẵn trong bộ đệm.
- Xét equi-join theo khóa khác `NULL`, bảo toàn bản sao; ngữ nghĩa SQL ba trị nằm ngoài phạm vi.

## 8. Công thức và giá trị phải tính lại

- Nested với $r$ ngoài: $b_r+n_rb_s$ truyền và $b_r+n_r$ seek. `student` ngoài: 2.000.100 truyền; `takes` ngoài: 1.000.400.
- Block Nested: $b_r+\lceil b_r/q\rceil b_s$ truyền và xấp xỉ $2\lceil b_r/q\rceil$ seek.
- Sort-Merge vật chất hóa: $f=\lfloor M/b_b\rfloor-1>1$, $P(b)=\lceil\log_f\lceil b/M\rceil\rceil$, $T_{sort}^{mat}(b)=2b(P(b)+1)$; cộng lượt đọc lại hai dãy để nối.
- Hash trong bộ nhớ: $\alpha b_s+b_{in}+b_{out}\le M$; chi phí lý tưởng $b_r+b_s$ truyền.
- Grace: pha phân hoạch $(p_h+1)b_b\le M$; pha xây–dò $\alpha\max_i b_{s_i}+b_{in}+b_{out}\le M$. Chi phí lý tưởng $3(b_r+b_s)$; cận tính khối biên là thêm tối đa $4p_h$.
- Ví dụ Grace dùng $M=20,b_b=2,p_h=7,\alpha=1{,}2$, kích thước phía xây $15;15;14;14;14;14;14$: 1.500 truyền lý tưởng, 1.528 với khối biên, 500 seek theo công thức nguồn.
- Bài 15.3: $b_{r_1}=800,b_{r_2}=1500$; Nested lần lượt 30.000.800 và 36.001.500 truyền.
- Bài 15.5: đọc đúng một lần mỗi quan hệ, $b_r+b_s$ truyền; cần $\min(b_r,b_s)+2$ khối bộ nhớ.

## 9. Rủi ro

- Không dùng $q=M-2$ như hằng số toàn cục; không dùng kích thước trung bình phân hoạch để chứng minh phía xây vừa bộ nhớ.
- Không làm mất tích Descartes $G_r\times G_s$ khi khóa trùng; không ghi đè tuple trùng trong ngăn băm.
- Không xem cùng giá trị băm là cùng khóa; luôn so khóa thật sau khi băm.
- Không gán chi phí quét một lần cho Sort-Merge khi nhóm trùng phải đọc lại.
- Không gọi đệ quy phân hoạch mà thiếu tiêu chuẩn tiến triển; cặp không giảm phải chuyển sang Block Nested.
- Không so trực tiếp chi phí thời gian Indexed Nested với số lần truyền của thuật toán khác.
- Không đưa mã trang, thời lượng, worker, reviewer, prompt, goal, rubric hoặc quy trình sản xuất vào ghi chú công khai.

## 10. Kế hoạch tác tử

1. Ba reader `z-ai/glm-5.3-flash` qua OpenRouter lập kế hoạch, ánh xạ nguồn và đề xuất chủ đề độc lập.
2. Codex chính hợp nhất và duyệt goal trước writer.
3. Một writer `deepseek/deepseek-v4-flash-0731` soạn trong gốc tạm hẹp.
4. Năm reviewer `z-ai/glm-5.3-flash` kiểm nguồn, toán–thuật toán, mạch sư phạm, tính liên tục và viewer.
5. Codex chính áp dụng sửa có căn cứ; hai reviewer GLM tái kiểm toán–thuật toán và mạch.
6. Dùng `$no-ai-slop` và `$quill`, không tạo `quill.json`; kiểm viewer thật, rồi mới cập nhật index, commit, push và xác minh SHA.

## 11. Trạng thái

**Hoàn tất.** Reader kế hoạch phiên `34866`, reader nguồn phiên `81722` và reader bản đồ chủ đề phiên `52504` dùng `z-ai/glm-5.3-flash`; writer phiên `37140` dùng `deepseek/deepseek-v4-flash-0731`; năm reviewer được chấp nhận là `73898`, `75855`, `47740`, `43252`, `77991`; hai lượt tái kiểm PASS là `13459`, `44095`. Metadata đều xác nhận đúng model và provider OpenRouter. Codex chính đã kiểm PPTX/PDF nguồn, áp dụng sửa được duyệt, biên tập bằng `$no-ai-slop`, rà mạch bằng `$quill`, kiểm Chromium rộng/hẹp, bàn phím, bản in, đường dẫn an toàn và index. Không gửi `.env`, bí mật hoặc thông tin xác thực tới worker.
