# Goal ghi chú Bài 09

## 1. Goal

Hoàn thiện ghi chú tự học **Bài 09 — Dòng dữ liệu: đếm, mômen và cửa sổ** tại `2627-1/materials/lec-09/lecture-note.md`. Tài liệu phải giúp sinh viên chọn phác thảo theo đại lượng cần ước lượng, chạy được từng thuật toán, giải thích bảo đảm và nhận ra điều kiện khiến bảo đảm không còn đúng.

## 2. Vấn đề trung tâm

Một dòng sự kiện có thể dài không giới hạn trong khi bộ nhớ chỉ giữ được trạng thái nhỏ. Cùng một dòng nhưng câu hỏi khác nhau — số khóa phân biệt, tần suất một khóa, độ lệch của phân phối, số bit 1 gần đây hoặc tổng giảm trọng số theo tuổi — đòi hỏi các trạng thái, mô hình sai số và cách cập nhật khác nhau.

## 3. Bằng chứng hoàn thành

- Người học phân biệt truy vấn toàn dòng với truy vấn gần đây và chọn đúng phác thảo theo đầu ra.
- Người học chạy Flajolet–Martin, giải thích vai trò của $\rho$, $R$, ước lượng $2^R$, đuôi nặng và thứ tự gộp trung bình trong nhóm rồi lấy trung vị giữa các nhóm.
- Người học cập nhật/truy vấn Count-Min Sketch trên dòng chỉ tăng và nối nhiễu kỳ vọng với bất đẳng thức Markov cùng khuếch đại qua các hàng độc lập.
- Người học định nghĩa $F_k$, chạy biến AMS cho $F_2$ và chứng minh $\mathbb E[X]=F_2$.
- Người học duy trì bucket DGIM, truy vấn hậu tố bằng mốc phải, chứng minh cận sai số 50% và phân tích bộ nhớ $O(\log^2N)$ bit.
- Người học suy ra truy hồi của tổng suy giảm mũ và phân biệt nó với cửa sổ cứng.
- Năm bài MMDS 4.4.1, 4.5.1, 4.5.3, 4.6.1 và 4.6.3 giữ nguyên dữ kiện, yêu cầu và nguồn.
- Viewer, Markdown, KaTeX, SVG, liên kết, bàn phím, màn hình rộng/hẹp, bản in và an toàn đường dẫn đều đạt trước khi cập nhật index.

## 4. Đầu ra

- `2627-1/materials/lec-09/lecture-note.md`.
- Cập nhật phần ghi chú trong `2627-1/planning/lec-09/{outline,storyboard,review-log}.md`.
- Dùng chín SVG hiện có trong `2627-1/img/lec-09/`.
- Thêm liên kết ghi chú Bài 09 vào `2627-1/index.html` sau khi viewer đạt.
- Không sửa deck trừ khi phát hiện lỗi nội dung dùng chung cần đồng bộ.

## 5. Nguồn và quyết định chọn nguồn

- MMDS Chương 4 mục 4.4–4.7 và hai bộ slide MMDS làm trục cho FM, mômen/AMS, DGIM và cửa sổ suy giảm.
- Stanford CS246 2017 dùng để kiểm tra thứ tự gộp FM và cách diễn đạt DGIM. Không theo các trang MMDS Streams 2 và Stanford 2026 đảo thứ tự gộp; thứ tự đúng theo sách là trung bình trong nhóm rồi lấy trung vị giữa các nhóm.
- Count-Min Sketch chỉ dùng UMass CS514 Lecture 10 với $m=\lceil2k/\varepsilon\rceil$, $t=\lceil\log_2(1/\delta)\rceil$ và sai số $\varepsilon n/k$ theo ký hiệu của nguồn đã chọn; không trộn dạng tham số khác.
- Bài tập trực tiếp: MMDS Ex.4.4.1 tr.145, Ex.4.5.1 và 4.5.3 tr.150, Ex.4.6.1 và 4.6.3 tr.157.
- Ngoài phạm vi: cơ chế HyperLogLog chuẩn, Count-Min có cập nhật âm, thuật toán sinh khóa nặng, biến thể DGIM sai số tùy ý và duy trì suy giảm cho nhiều khóa.

## 6. Bản đồ chủ đề

| `note-topic-id` | Nhãn | Chủ đề và sản phẩm | Nguồn, kết nối |
|---|---|---|---|
| `L09-N01` | cốt lõi | Bản đồ quyết định theo đại lượng và phạm vi thời gian | MMDS 4.4–4.7; nối từ mô hình dòng Bài 8 |
| `L09-N02` | cốt lõi | Flajolet–Martin cho $F_0$ | MMDS 4.4; đặc tả, vết băm, lập luận ngưỡng, gộp và chi phí |
| `L09-N03` | cốt lõi | Count-Min Sketch cho tần suất một khóa | UMass Lecture 10; dòng chỉ tăng, ví dụ va chạm, Markov và khuếch đại |
| `L09-N04` | cốt lõi | Mômen và đại lượng $F_2$ | MMDS 4.5.1; nối truy vấn tần suất riêng sang độ lệch toàn phân phối |
| `L09-N05` | cốt lõi | Biến AMS và tính không chệch | MMDS 4.5.2–4.5.5; vết hậu tố, giả mã, chứng minh và duy trì bằng hồ chứa |
| `L09-N06` | cốt lõi | Đặc tả và bất biến DGIM | MMDS 4.6.1–4.6.3; bucket, mốc phải và trạng thái cửa sổ |
| `L09-N07` | cốt lõi | Cập nhật, truy vấn, cận sai số và chi phí DGIM | MMDS 4.6.3–4.6.5; cascade, bucket biên và cận 50% |
| `L09-N08` | cầu nối | Tổng suy giảm mũ | MMDS 4.7.1–4.7.2; tổng hữu hạn và truy hồi $O(1)$ |
| `L09-N09` | cốt lõi | So sánh năm hợp đồng phác thảo | Tổng hợp nguồn; thu hồi bản đồ quyết định mở bài |
| `L09-N10` | cốt lõi | Năm bài tập MMDS | Giữ nguyên đề; lời giải và hướng dẫn chấm phải truy nguyên được |

Đồ thị tiên quyết: `N01→N02→N03`; `N01→N04→N05`; `N01→N06→N07→N08`; các nhánh hội tụ ở `N09`, rồi dẫn sang `N10`. `N05` dùng lại lấy mẫu hồ chứa của Bài 8.

## 7. Khuôn trình bày và ký hiệu

Mỗi chủ đề cốt lõi đi theo vai trò; đặc tả; ví dụ chạy tay; trực quan; thuật toán hoặc mệnh đề; chứng minh/lập luận; chi phí, giới hạn và tự kiểm. Công thức Markdown chỉ dùng `$...$` và `$$...$$`; khối tùy biến không lồng nhau.

- $f_x$ hoặc $f_i$ là tần suất; $F_k=\sum_i f_i^k$. Với $F_0$, nêu quy ước $0^0=0$ hoặc phát biểu tương đương là chỉ đếm khóa có tần suất dương.
- FM dùng $\rho(h(x))$ cho số bit 0 liên tiếp ở cuối và $R$ cho cực đại. Với băm hữu hạn $L$ bit, quy ước $\rho(0)=L$ và dòng rỗng trả 0 là quy ước biên của bài, không phải mệnh đề trích nguyên từ MMDS.
- Count-Min dùng $n=\lVert f\rVert_1$ cho tổng cập nhật, $k$ cho ngưỡng khóa nặng trong tham số nguồn, $m$ ô mỗi hàng và $t$ hàng. Các hàm băm độc lập đôi một trong một hàng và các hàng độc lập nhau.
- AMS dùng vị trí $I$ chọn đều, bộ đếm hậu tố $c_I$ và $X=n(2c_I-1)$. Không dùng lẫn $c_I$ với $X$.
- DGIM dùng $N$ cho độ dài cửa sổ, $k$ cho độ dài hậu tố truy vấn, $b^*$ cho bucket biên. Bucket không phải đoạn vị trí liên tục; truy vấn chỉ cần mốc phải.
- Cửa sổ suy giảm dùng $0<c<1$ và $S_t=\sum_{i=0}^{t-1}a_{t-i}(1-c)^i$, với truy hồi $S_{t+1}=(1-c)S_t+a_{t+1}$.

## 8. Giá trị và lập luận phải tính lại

- MMDS Ex.4.4.1: ba ước lượng FM là $1,16,16$.
- MMDS Ex.4.5.1: $F_2=21$, $F_3=51$ cho dòng chín phần tử.
- MMDS Ex.4.5.3: $c_i=[2,3,2,2,1,1,2,1,1]$; nếu dùng $X_i$ để tự kiểm thì trung bình bằng 21.
- MMDS Ex.4.6.1: $k=5$ cho 3 chính xác; $k=15$ ước lượng 10 so với 9, sai số tương đối $1/9$.
- Ví dụ AMS sách: $F_2=59$; ba biến cho $75,45,45$, trung bình 55.
- DGIM: chứng minh cận bằng tổng bucket mới hơn $A\ge|b^*|-1$; tách trường hợp số thật $c=0$ trước khi chia cho $c$.
- Tổng trọng số hữu hạn là $(1-(1-c)^t)/c$, chỉ tiến tới $1/c$ khi $t$ tăng.

## 9. Rủi ro và điểm cần duyệt

- Không gọi $2^R$ là ước lượng không chệch; nêu rõ đuôi nặng và lý do cần nhiều bản sao.
- Không đảo thứ tự gộp FM thành trung vị trước rồi trung bình.
- Không suy Count-Min tìm được khóa nặng nếu chưa có tập ứng viên; không áp dụng bảo đảm dòng chỉ tăng cho cập nhật âm.
- Không gọi AMS đúng trên từng lần chạy; bảo đảm là kỳ vọng không chệch dưới lựa chọn vị trí đều.
- Không ghi bộ nhớ DGIM là $O(\log N)$; cần $O(\log^2N)$ bit khi tính cả mốc thời gian.
- Với Ex.4.6.3, phần trái trạng thái không xác định nên lời giải phải nêu nhánh cascade có điều kiện ở bucket 8 và các mức cao hơn.
- Không đưa mã trang, thời lượng, worker, reviewer, prompt, goal hoặc quy trình sản xuất vào ghi chú công khai.

## 10. Kế hoạch tác tử

1. Ba reader `z-ai/glm-5.3-flash` qua OpenRouter lập kế hoạch, ánh xạ nguồn và đề xuất chủ đề độc lập.
2. Codex chính hợp nhất và duyệt goal trước writer.
3. Một writer `deepseek/deepseek-v4-flash-0731` soạn trong gốc tạm hẹp.
4. Năm reviewer `z-ai/glm-5.3-flash` kiểm nguồn, toán–thuật toán, mạch sư phạm, tính liên tục và viewer.
5. Codex chính áp dụng sửa có căn cứ; hai reviewer GLM tái kiểm toán–thuật toán và mạch.
6. Dùng `$no-ai-slop` và `$quill`, không tạo `quill.json`; kiểm viewer thật, rồi mới cập nhật index, commit, push và xác minh SHA.

## 11. Trạng thái

**Hoàn tất.** Ghi chú đã qua năm reviewer, hai lượt tái kiểm sau sửa, biên tập `$no-ai-slop`, rà mạch `$quill`, kiểm định viewer rộng/hẹp/in/bàn phím/an toàn đường dẫn và kiểm tra liên kết index. Writer dùng `deepseek/deepseek-v4-flash-0731`; reader và reviewer dùng `z-ai/glm-5.3-flash`, đúng provider OpenRouter.
