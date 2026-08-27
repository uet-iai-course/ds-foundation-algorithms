# Nhật ký rà soát Bài 6

## Quyết định nguồn và biên tập

- MMDS là nguồn chính cho §3.4, các độ đo, vân tay và ba bài tập. Stanford CS246 bài 04 chỉ cung cấp cách trình bày từ họ cơ sở đến khuếch đại ở §§3.6–3.7; mọi công thức đã đối chiếu sách.
- Sửa lỗi trên slide MMDS: giá trị dùng trong phép tính là $s=0.3=30\%$, không phải $0.3\%$.
- Không dùng xấp xỉ $(1/b)^{1/r}$ như đẳng thức. Deck suy ra $s_{1/2}=(1-2^{-1/b})^{1/r}$ và xấp xỉ lớn-$b$ là $(\ln2/b)^{1/r}$.
- Định nghĩa họ LSH dùng xác suất theo $h\sim F$, $\alpha_1>\alpha_2$; không phát biểu gì cho $d_1<d<d_2$.
- Khóa dải là $(\ell,\text{toàn bộ vector dải})$. Nếu hiện thực bằng mã băm, phải kiểm tra hai khóa có bằng nhau hay không; không dùng giả thiết “đủ nhiều ngăn” thay cho tính đúng.
- Cosin dùng pháp tuyến đẳng hướng, có thể lấy Gaussian; vector $\{\pm1\}^d$ chỉ là xấp xỉ. Trường hợp tích vô hướng bằng 0 có quy tắc gán cố định; với Gaussian liên tục, biến cố này có xác suất 0 cho vector khác 0 cố định.
- Euclid dùng độ dịch độc lập $u\sim U[0,a)$ để không trùng với ngưỡng hậu kỳ $\tau$. Công thức $\max(0,1-|\delta|/a)$ chỉ là xác suất theo $u$ khi hướng chiếu đã cố định; xác suất đầy đủ còn lấy trung bình theo hướng Gaussian. Nguồn: MMDS §§3.7.4–3.7.5 và Datar et al., 2004, DOI `10.1145/997817.997857`.
- Ví dụ vân tay được gọi là phép tính trong mô hình MMDS, dựa trên giả thiết độc lập; không mô tả là kết quả thực nghiệm hiện thời. Kết quả “không” đi vào ngăn đơn riêng, không vào một ngăn “không” chung.
- Không tuyên bố diện tích dưới đường cong chữ S là tỷ lệ lỗi của kho dữ liệu; đó chỉ là xác suất có điều kiện theo một cặp có độ tương đồng $s$.
- Không tuyên bố thời gian $O(1)$ hay $O(N)$ nếu thiếu mô hình ngăn. Chi phí ghi theo $A=\sum_B\binom{|B|}{2}$ và trường hợp xấu $\Theta(bN^2)$.

## Sai khác có chủ ý

- Tách thuật toán tạo ứng viên khỏi phân tích xác suất. Thứ tự đã sửa thành luồng trực giác → vết chạy → kiểu và giả mã → bất biến giai đoạn sinh cặp → chi phí, bộ nhớ và đối chiếu hậu kỳ.
- Bài tập được dịch và chia thành nhiều trang để đủ thời lượng; dữ kiện và yêu cầu toán học giữ nguyên. Mọi đáp án và hướng dẫn chấm chỉ ở notes.
- Chỉ đưa ba họ Hamming, cosin và Euclid có trong phạm vi; không thêm HNSW, PQ hoặc nội dung Bài 7.

## Xử lý phản biện sau bản nháp

- **Chặn bàn giao — B02:** đổi vector dải 3 của $D_3$ từ $(6,3)$ thành $(6,9)$. Sau sửa, chỉ $D_1,D_2$ trùng trọn dải 2; hai cặp còn lại không trùng trọn dải nào. Ghi chú không còn mâu thuẫn với bảng.
- **Nghiêm trọng — A01–A04:** A01 chuyển từ kiểu dữ liệu sang luồng trực giác; A02 giữ vết chạy; A03 gom điều kiện trước, kiểu khóa và giả mã; A04 chỉ phát biểu bất biến trên $t$ ngăn đã được gom xong. Ghi chú A04 tách rõ giai đoạn một xây ngăn và giai đoạn hai sinh cặp.
- **Nghiêm trọng — A05:** bỏ lời giải hai công việc MapReduce khỏi phần giảng. Trang tách chi phí tạo ứng viên kỳ vọng $\Theta(pN+A)$ dưới mô hình bảng băm, bộ nhớ khóa tham chiếu $O(bN+|C|)$, khả năng $O(pN)$ khi vật hóa khóa và chi phí đối chiếu chữ ký $O(p|C|)$. Thiết kế hai công việc vẫn là nhiệm vụ của Bài tập 3.4.4.
- **Nghiêm trọng — Q04:** chỉ gọi $q(s)$ là đường cong chữ S khi $b>1$ và $r>1$; mô tả thay thế là đường xác suất.
- **Nghiêm trọng — F01–F05:** thêm MMDS Ví dụ 3.18 trước định nghĩa; dùng $\rho$ cho xác suất va chạm để không trùng $p=br$; F05 chỉ kiểm tra nghĩa AND/OR và không đưa chuỗi số hoặc đáp án của Bài tập 3.6.1.
- **Nghiêm trọng — D01–D04:** dùng $m$ cho số chiều; thêm điều kiện $x,y\ne0$ và pháp tuyến bất biến quay cho công thức cosin; thay độ dịch $\tau$ bằng $u$ ở Euclid; hạ tuyên bố Euclid về xác suất có điều kiện theo hướng chiếu và bổ sung nguồn Datar et al.
- **Trung bình — hậu kiểm:** phân biệt rõ đối chiếu chữ ký chỉ cho ước lượng MinHash, còn đối chiếu tập shingle hoặc dữ liệu gốc mới cho Jaccard chính xác; đồng bộ M00, M02, A05 và C00.
- **Trung bình — F02, D03–D04, R07–R08:** bổ sung miền $0\le\alpha_2<\alpha_1\le1$; đưa $v\sim\mathcal N(0,I_m)$ và tính độc lập với $u$ lên mặt trang; nêu rõ độc lập giữa ô, giữa hai dấu khác ngón và giữa các hàm OR theo mô hình bài tập.
- **Nghiêm trọng — V01:** bỏ các xác suất cơ sở, kết quả OR 1024 và AND của hai nhóm. Trang chỉ nêu chiều đánh đổi; toàn bộ phép tính vẫn thuộc Bài tập 3.8.2.
- **Trung bình — bài tập:** R02 không chấm yêu cầu xử lý va chạm mã băm như một mục ngoài đề; R06 bỏ yêu cầu chứng minh không giao hoán và chỉ chấm hai công thức (c), (d) của nguồn. Các khung chia bước không đổi dữ kiện hoặc yêu cầu toán học.
- **Trung bình — thuật ngữ và mạch học phần:** Việt hóa `band` thành “dải”, `bucket` thành “ngăn”, `exact` thành “đầy đủ”; P00 viết đầy đủ băm nhạy cảm cục bộ trước LSH; thêm P02 nêu hành trình; C00 nối sang Bài 7 nhưng không dạy trước HNSW hoặc PQ.
- **Khả năng đọc:** tăng cỡ chữ và Việt hóa nhãn ở các SVG phân dải, khóa dải, đường xác suất, AND/OR, luồng ứng viên và Euclid. Không đổi dữ liệu hoặc quan hệ hình học.
- **Không đồng nhất hai cách hậu kiểm:** chữ ký MinHash đầy đủ chỉ cho ước lượng Jaccard; tập shingle hoặc dữ liệu gốc mới cho Jaccard chính xác. LSH chỉ sinh ứng viên.

## Tài sản và công cụ

- Mười hình được vẽ lại thành SVG cục bộ trong `img/lec-06/`; không dùng raster hoặc tài nguyên mạng.
- Dự án Codex Slides: `20260827182308-b-i-6-t-m-c-p-t-ng-ng-b-ng-lsh-bmts`.
- Codex Slides trong trình duyệt biên tập chưa khả dụng trong môi trường tác tử này; không tuyên bố đã rà trực quan bằng Codex Slides. Kiểm định RevealJS cục bộ được ghi sau khi chạy.

## Kiểm định đã chạy

- Bộ kiểm tra tĩnh ban đầu xác nhận 39 trang giảng, 10 trang recitation, 49 `data-slide-id` duy nhất và 49 notes. Sau phản biện thêm P02; kết quả kiểm định lại được ghi bên dưới.
- Storyboard khớp thứ tự HTML; tổng thời lượng tính lại là 120 + 60 phút.
- Mười SVG đọc được bằng trình phân tích XML, có `role`, `title`, `desc`; mọi đường dẫn tài sản tồn tại.
- Không tìm thấy ảnh raster, URL tài nguyên từ xa hoặc phụ thuộc mạng cốt lõi.
- `python3 -m reloadserver 8765` không chạy vì môi trường thiếu mô-đun `reloadserver`. Điều phối viên dùng máy chủ dự phòng `python3 -m http.server 8765` trên đúng cổng sau khi xác nhận cổng đã có tiến trình phục vụ.
- `git diff --check` không báo lỗi ở bản nháp; không sửa `index.html`, CSS hoặc tệp ngoài phạm vi Bài 6.

## Kiểm định lại sau chỉnh sửa

- Kiểm tra tĩnh xác nhận 40 trang giảng và 10 trang recitation; 50 `data-slide-id` duy nhất; mỗi trang có đúng một khối ghi chú; thứ tự HTML khớp storyboard.
- Tổng thời lượng tính từ storyboard là 120 phút giảng và 60 phút recitation.
- Mười tham chiếu SVG đều tồn tại. Mỗi SVG đọc được bằng trình phân tích XML và có `role="img"`, `title`, `desc`; không có tham chiếu raster hoặc tài nguyên mạng cốt lõi.
- Tính lại B02 cho đúng một cặp ứng viên; đối chiếu các công thức $q(s)$, ngưỡng một nửa, AND/OR, Hamming, cosin, Euclid có độ dịch và các đáp án recitation.
- Tự kiểm theo `no-ai-slop/eval.md`: không có từ cấm, lời dẫn rỗng, câu hỏi tu từ hoặc kết luận lặp; thuật ngữ và ký hiệu được dùng nhất quán theo rà mạch Quill.
- `git diff --check` không báo lỗi. Không sửa `index.html`, CSS chung hoặc tệp ngoài Bài 6.
- Hai tái kiểm độc lập xác nhận không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng`; các mục trung bình về mô hình chi phí, hậu kiểm, miền xác suất, nguồn ngẫu nhiên Euclid và giả thiết độc lập đã được vá.
- Playwright duyệt đủ 50 trang ở `1280 × 720` và `800 × 600`: không có lỗi tải, lỗi JavaScript hoặc trang tràn khung. Điều phối viên đã kiểm hai contact sheet và kiểm riêng A05, D03, R07 sau bản vá cuối.
- Dự án Codex Slides đã lưu và đọc lại `generated/outline.md` cùng `generated/brief.md`. Tải HTML cuối vào Design Files trả lỗi HTTP 500; bề mặt Browser của Codex Slides không khả dụng, nên không tuyên bố đã rà trực quan bằng Codex Slides. Rà trực quan RevealJS cục bộ là kiểm định hiển thị cuối.
