# Goal ghi chú Bài 14

## 1. Goal

Hoàn thiện ghi chú tự học **Bài 14 — Chỉ mục văn bản và chỉ mục không gian** tại `2627-1/materials/lec-14/lecture-note.md`. Tài liệu phải giúp sinh viên đặc tả và trộn chỉ mục đảo, đánh giá tập kết quả, chạy tìm kiếm 1-NN chính xác bằng cận dưới, rồi chọn cấu trúc không gian theo truy vấn và mô hình chi phí.

## 2. Vấn đề trung tâm

Một kho văn bản và đối tượng không gian lớn phải trả lời truy vấn từ khóa, vùng và lân cận mà không quét toàn bộ dữ liệu. Chỉ mục chỉ hiệu quả khi biểu diễn tạo được tập ứng viên không bỏ nghiệm, bước tinh lọc kiểm đúng đối tượng thật và chi phí được đo theo đúng mô hình RAM hoặc I/O trang.

## 3. Bằng chứng hoàn thành

- Người học đặc tả danh sách đảo, chạy AND, OR và NOT bằng hai con trỏ, nêu bất biến và chi phí tuyến tính.
- Người học phân biệt dữ liệu vị trí–tần suất với docID, giải thích tuyến lưu trữ trên đĩa và tính precision/recall trên cùng một ví dụ.
- Người học giải thích R-tree theo mô hình lọc–tinh lọc và chứng minh bước gom bằng MBR không bỏ nghiệm.
- Người học chạy 1-NN chính xác trên kd-tree và ball tree, giữ mọi nghiệm đồng hạng, chứng minh điều kiện chỉ cắt khi $LB>\tau$.
- Người học phân biệt truy vấn ball tree trong metric tổng quát với phép dựng Euclid và các cận chi phí có điều kiện.
- Người học mã hóa lưới bằng Z-order, so sánh đoạn chính xác với đoạn gộp và tinh lọc dương tính giả.
- Ba bài recitation 31.2, 25.2 và 25.3 giữ nguyên dữ kiện nguồn, có giả mã hoặc lập luận đúng, điều kiện dừng và chi phí.
- Viewer, Markdown, KaTeX, SVG, liên kết, bàn phím, màn hình rộng/hẹp, bản in và an toàn đường dẫn đều đạt trước khi cập nhật index.

## 4. Đầu ra

- `2627-1/materials/lec-14/lecture-note.md`.
- Cập nhật phần ghi chú trong `2627-1/planning/lec-14/{outline,storyboard,review-log}.md`.
- Dùng các SVG hiện có trong `2627-1/img/lec-14/`; không tạo tài sản ngoài nguồn.
- Thêm liên kết ghi chú Bài 14 vào `2627-1/index.html` sau khi viewer đạt.
- Không sửa deck trừ khi phát hiện lỗi nội dung dùng chung cần đồng bộ.

## 5. Nguồn và quyết định chọn nguồn

- *Database System Concepts* 7e, Chương 31 trang in 13–16 làm trục cho chỉ mục đảo, phép Boolean, vị trí–tần suất và precision/recall; Bài 31.2 ở trang in 25 cung cấp đề recitation.
- Chương 24, slide 17 và 21–24 cùng Auburn COMP7120 trang 10–13 cung cấp truy vấn không gian, R-tree và lọc–tinh lọc.
- Cornell CS5780 trang 1–5 cung cấp cơ chế kd-tree và ball tree; các vết số, giả mã đầy đủ và cận dựng có điều kiện là phần bài giảng triển khai, phải ghi đúng xuất xứ.
- Auburn COMP7120 trang 12–13, slide nguồn 23–26 cung cấp row-order/Z-order; sửa hoán vị mã 6/7 để nhất quán với công thức Morton và đủ 16 ô.
- Bài 25.2–25.3 dùng đề và lời giải chính thức của *Database System Concepts* 6e. Lời giải đống cho Bài 31.2 do bài giảng triển khai từ đề vì ấn bản 7 không công bố lời giải.
- MMDS, Stanford CS246, ANN/HNSW/PQ, xếp hạng học máy, chèn–tách R-tree, Hilbert curve và Decision Trees của Cornell nằm ngoài phạm vi.

## 6. Bản đồ chủ đề dự kiến

| `note-topic-id` | Nhãn | Chủ đề và sản phẩm | Nguồn, kết nối |
|---|---|---|---|
| `L14-N01` | cầu nối | Hai miền dữ liệu và tuyến ứng viên–tinh lọc | `source.md`; Bài 13 → các nhánh |
| `L14-N02` | cốt lõi | Danh sách đảo, AND, OR, NOT, bất biến và chi phí | Ch.31 tr.13–14; mở tuyến văn bản |
| `L14-N03` | cầu nối | Vị trí–tần suất và bố trí danh sách trên đĩa | Ch.31; Bài 12–13 → đánh giá |
| `L14-N04` | cốt lõi | Precision/recall trên $G,R_h,R_l$ | Ch.31 tr.15–16; thu hồi ở N10 |
| `L14-N05` | cốt lõi | Truy vấn không gian và R-tree lọc–tinh lọc | Ch.24; Auburn; sang cận khoảng cách |
| `L14-N06` | cốt lõi | kd-tree và 1-NN chính xác, đồng hạng, tính đúng và chi phí | Cornell tr.1–4; sang ball tree |
| `L14-N07` | cốt lõi | Ball tree: cận metric, truy vấn và vết chạy | Cornell tr.3–5; chuẩn bị dựng |
| `L14-N08` | cốt lõi | Dựng ball tree Euclid, tiến triển và cận có điều kiện | Cornell tr.5 + suy ra của deck |
| `L14-N09` | cốt lõi | Z-order, đoạn Morton, B+-Tree và tinh lọc | Auburn tr.12–13; thu hồi Bài 13 |
| `L14-N10` | bổ sung | Chọn chỉ mục theo đầu ra, giả thiết và đơn vị chi phí | Tổng hợp N01–N09 |
| `L14-N11` | cốt lõi | Recitation 31.2: hợp ít nhất $k$ danh sách bằng đống | Ch.31 Bài 31.2 |
| `L14-N12` | cốt lõi | Recitation 25.2–25.3: truy vấn điểm và 1-NN qua vùng | Ch.25 Bài 25.2–25.3 |

Đồ thị tiên quyết: `N01→N02→N03→N04→N05→N06→N07→N08→N09→N10→{N11,N12}`. Codex chính giữ 12 chủ đề sau khi hợp nhất ba reader; tách truy vấn ball metric khỏi phép dựng Euclid để không trộn giả thiết. Không thêm mục đọc thêm về đường phủ không gian khác vì chưa có nguồn chi tiết phù hợp.

## 7. Ký hiệu và hợp đồng phải giữ

- $D$ là tập tài liệu, $S\subseteq D$ là tập nền của NOT, $P_t=\langle d_1<\cdots<d_m\rangle$ là danh sách đảo của thuật ngữ $t$.
- $G$ là tập phù hợp chuẩn; $R_h,R_l$ là hai tập hệ thống trả về ở ngưỡng chặt và nới. Nêu quy ước riêng nếu $R=\varnothing$ hoặc $G=\varnothing$; không lẫn precision với tính đúng của 1-NN.
- $q$ là điểm hỏi; $U$ là nút hoặc miền cây con; $p$ là số chiều; $best,\tau$ là tập nghiệm tốt nhất và khoảng cách hiện có; $LB(q,U)$ là cận dưới hợp lệ.
- Trả mọi 1-NN đồng hạng; vì vậy chỉ cắt khi $LB>\tau$, không cắt khi bằng.
- $B(c,r)$ là ball tâm $c$, bán kính $r$. Truy vấn chỉ cần metric $\delta$ và ball chứa cây con theo cùng metric; phép dựng trong bài dùng tập hữu hạn khác rỗng trong $\mathbb R^p$, chuẩn Euclid và sức chứa lá $\ell\ge1$.
- Với Z-order, $u=x-1,v=y-1$ là tọa độ 0-based và $z$ là mã 1-based.
- Trong Bài 31.2, $n$ là số danh sách theo phạm vi cục bộ, $T=\sum_i|P_i|$; phần tử đống là `(docID, mã danh sách)`.

## 8. Giá trị và lập luận phải tính lại

- NOT: $S=[1,2,3,4,6,8]$, $P_t=[2,3,6,8]$, kết quả $[1,4]$.
- Đánh giá: $G=\{1,3,8\}$, $R_h=\{3,8\}$ cho $(1,2/3)$; $R_l=\{1,2,3,6,8\}$ cho $(3/5,1)$.
- kd-tree: $q=(3,2)$, gặp $p=(2,2)$ cho $\tau=1$; miền $x\ge4$ có $LB=1$ nên phải thăm và giữ $s=(4,2)$ đồng hạng; miền $x\ge5$ có $LB=2$ nên cắt.
- Ball tree với $\tau=2{,}5$: các cặp $(\delta(q,c),r)$ là $(3,1)$, $(5,2)$, $(4,1{,}5)$ cho $LB$ lần lượt $2,3,2{,}5$; ball thứ ba vẫn phải thăm.
- Dựng Euclid: $a=(0,0),b=(1,0),c=(3,0),d=(4,0)$; $x_0=a,x_1=d,x_2=a$; khóa chiếu $(0,4,12,16)$; hai lá có tâm $(0{,}5,0)$ và $(3{,}5,0)$, bán kính $0{,}5$.
- Cận dựng $O(n\log^2n+pn\log n)$ chỉ là suy ra của deck khi cây cân bằng, mỗi nút sắp lại và phép đo/chiếu xử lý $p$ tọa độ; không gán cho Cornell.
- Morton: $z=1+\sum_{j\ge0}(2u_j+v_j)4^j$; ma trận từ trên xuống là `6,8,14,16`; `5,7,13,15`; `2,4,10,12`; `1,3,9,11`. Vùng giữa có mã $\{4,7,10,13\}$; đoạn gộp $[4,13]$ chứa mã 5 là dương tính giả.
- Bài 31.2 có thời gian $O(n+T\log(n+1))$, bộ nhớ phụ $O(n)$ không tính đầu ra, tổng bộ nhớ $O(n+|A|)$.

## 9. Rủi ro và điểm cần duyệt

- Không coi danh sách đảo là tập chưa sắp; không lặp docID để biểu diễn tần suất.
- Không dùng NOT khi chưa chốt tập nền $S$; OR phải là hợp dù slide nguồn in nhầm thành giao.
- Không tuyên bố R-tree chỉ đi một nhánh hoặc tự trả hình học chính xác từ MBR; luôn tách gom ứng viên và tinh lọc.
- Không biến hiệu quả thực hành của kd-tree/ball tree thành bảo đảm $O(\log n)$; nêu trường hợp xấu tuyến tính.
- Không trộn metric tổng quát với tâm trung bình, phép chiếu và cận dựng Euclid.
- Không so trực tiếp số phép đo RAM với số trang I/O; không thêm cận I/O ngoài nguồn.
- Không bỏ điều kiện hữu hạn, không rỗng, $r_i\to\infty$ và vùng đóng trong chứng minh Bài 25.3; ghi rõ chúng là bổ sung hoàn thiện đặc tả.
- Không đưa mã trang, thời lượng, worker, reviewer, prompt, goal, rubric hoặc quy trình sản xuất vào ghi chú công khai.

## 10. Kế hoạch tác tử

1. Ba reader `z-ai/glm-5.3-flash` qua OpenRouter lập kế hoạch, ánh xạ nguồn và đề xuất chủ đề độc lập.
2. Codex chính hợp nhất và duyệt goal trước writer.
3. Một writer `deepseek/deepseek-v4-flash-0731` soạn trong gốc tạm hẹp.
4. Năm reviewer `z-ai/glm-5.3-flash` kiểm nguồn, toán–thuật toán, mạch sư phạm, tính liên tục và viewer.
5. Codex chính áp dụng sửa có căn cứ; hai reviewer GLM tái kiểm toán–thuật toán và mạch.
6. Dùng `$no-ai-slop` và `$quill`, không tạo `quill.json`; kiểm viewer thật, rồi mới cập nhật index, commit, push và xác minh SHA.

## 11. Trạng thái

**Hoàn tất.** Reader kế hoạch phiên `79940`, reader nguồn phiên `81734` và reader bản đồ chủ đề phiên `12041` dùng `z-ai/glm-5.3-flash` qua OpenRouter. Writer `deepseek/deepseek-v4-flash-0731` phiên `23162` tạo bản nháp rồi chạm giới hạn công cụ sau khi đã ghi xong; Codex chính kiểm và sửa bản nháp. Năm vai reviewer GLM gồm nguồn `87247`, toán–thuật toán `63063`, sư phạm `54155`, mạch `10660` và viewer `4796`; tái kiểm toán `58293` và mạch `83256` đều `PASS`. Bản cuối đã qua `$no-ai-slop`, `$quill`, kiểm tĩnh, Chromium rộng/hẹp, bàn phím, bản in, an toàn đường dẫn và liên kết index. Không tạo `quill.json`; không gửi `.env`, bí mật hoặc thông tin xác thực tới worker.
