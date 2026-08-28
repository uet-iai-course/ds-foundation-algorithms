# Nhật ký rà soát Bài 15

## Trạng thái bản nháp

- Tạo deck RevealJS gồm 50 trang giảng và 10 trang recitation.
- Phân bổ phần giảng đúng 120 phút; recitation đúng 60 phút.
- Tạo SVG cục bộ cho use case, ba biến thể vòng lặp lồng, nhóm Sort-Merge, build–probe, phân hoạch Grace, chi phí, skew và bản đồ chọn thuật toán.
- Không sửa `2627-1/index.html`, `2627-1/lecture-style.css` hoặc bài khác. Chưa commit và chưa push.

## Quyết định nguồn và phạm vi

- Ch15 slide 24–41 là trục. Slide 7–9 cung cấp mô hình chi phí; slide 17–23 chỉ được nhắc để dùng lại External Merge Sort từ Bài 12.
- Slide 28, 30, 35 và 40 bị ẩn trong PPTX nhưng vẫn được đọc vì chứa công thức, ví dụ và lập luận đúng liên quan trực tiếp.
- Bỏ selection, aggregation, set operations, outer join, materialization, pipelining, stream và cache-conscious processing vì nằm ngoài sản phẩm Bài 15.
- Recitation dùng nguyên đề 15.3, 15.4 và 15.5 từ Practice Exercises; lời giải và hướng dẫn chấm bám Practice Solutions tương ứng.

## Sửa lỗi và sai khác có chủ ý

- Slide 33: sửa tên phân hoạch của $s$ và dùng $p_h$ phân hoạch đánh số $0..p_h-1$.
- Slide 37: sửa phía dò thành $r_i$; chỉ phía xây $s_i$ phải vừa vùng xây. Dùng $M-2$ thay cho cách ghi $M$ lỏng trong nguồn để giữ hai khối đầu vào/đầu ra.
- Slide 39: tách $3(b_r+b_s)$ lý tưởng và số hạng tối đa $4p_h$ do khối biên; không cộng hai cách đếm mà không giải thích.
- Slide 40: với $M=20$, thay năm phân hoạch xây kích thước 20 bằng sáu phân hoạch trung bình $100/6<18$. Kết quả 1.500 lần truyền lý tưởng; 1.524 nếu tính $4p_h$. Với $b_b=3$, số seek là $2(\lceil100/3\rceil+\lceil400/3\rceil)=336$.
- Slide 41: bỏ Hybrid Hash Join khỏi tuyến chính vì phân bổ bộ đệm của ví dụ nguồn không đủ rõ để kiểm chứng trong mô hình $M-2$. Dùng thời gian này cho vết Grace ở mức tuple và điều kiện dừng.
- Sort-Merge lấy tích Descartes của hai nhóm khóa trùng; không tiến một phía rồi làm mất bản sao.
- Hash Join lưu danh sách tuple trong mỗi khóa, kiểm tra khóa thật sau khi băm và không ghi đè bản sao.
- Khi skew làm phân hoạch xây tràn, deck nêu băm lại cả cặp phân hoạch và fallback Block Nested-Loop Join.
- Deck xét khóa nối không `NULL`; ngữ nghĩa SQL `NULL` nằm ngoài phạm vi và được nêu công khai.
- Lời giải 15.3 dùng $M-1$ ở Block Nested-Loop Join. Deck dùng $M-2$ nhất quán với mô hình một khối đọc phía trong và một khối đầu ra; trang bài tập ghi cả biểu thức nguồn và biểu thức dùng trong bài.

## Hợp nhất bốn báo cáo độc lập

- **Chặn bàn giao — H11:** giả mã cũ nói “phân hoạch lại” nhưng không gọi đệ quy hoặc đưa cặp tràn vào cấu trúc công việc. Đã thay bằng hàng đợi; chỉ xếp lại khi kích thước giảm, nếu không dùng Block Nested-Loop Join.
- **Nghiêm trọng — H08, H10–H14:** phép chia trung bình $100/6$ bị trình bày như bảo đảm bộ nhớ, còn skew và đường lui đứng sau chi phí. Đã ghi điều kiện $\max_i b_{s_i}\le M-2$, đặt thuật toán, chứng minh và đường lui trước H14; H14 chỉ tính trường hợp không tràn, không đệ quy.
- **Nghiêm trọng — H12:** chứng minh cũ mới cho thấy cùng khóa cùng số phân hoạch, chưa chứng minh các cặp con rời nhau và được xử lý đúng một lần. Đã thêm lập luận khởi tạo–duy trì–kết thúc trong notes và mệnh đề phân hoạch rời trên mặt trang.
- **Nghiêm trọng — X02–X04:** 25 phút của Bài 15.3 hiển thị sẵn kết quả. Đã đổi thành ba trang giao việc; toàn bộ đáp án, hai hướng Block Nested, seek sắp/trộn và Hash seek chuyển vào notes.
- **Nghiêm trọng — N09–N11:** Indexed Nested thiếu vết khóa vắng/bản sao, giả mã, dừng và công thức đúng đơn vị. Đã bổ sung cả bốn; chi phí dùng $b_r(t_T+t_S)+n_rc$.
- **Trung bình — N06, H07–H10:** Block Nested và Grace thiếu vết chạy tay. Đã dùng ví dụ tuple nhỏ; vết Grace truyền cùng dữ liệu qua $h_1$, $h_2$, va chạm, so khóa và cặp kết quả.
- **Trung bình — nhịp 120 phút:** không tăng số trang; loại Hybrid khỏi tuyến chính và dành đúng thời gian cũ cho vết Grace. Tổng giảng vẫn 120 phút.
- **Trung bình — P01 và thuật ngữ:** giữ P01 vì SVG đã hiển thị hai quan hệ, khóa ID và số khối; notes cung cấp giới hạn đĩa. Thuật ngữ chuẩn trong tên thuật toán được giữ, còn build/probe tiếp tục đi cùng “phía xây/phía dò”.
- **Trung bình — X07:** giữ câu nguồn dưới fragment và giữ cảnh báo trong notes rằng phải so tổng chi phí, không dùng kích thước phía ngoài như điều kiện đủ. Không đổi vì đây là nội dung trực tiếp của Bài 15.4.

## Rà sau chỉnh sửa

- Rà lại H06–H15 và hai trang lân cận: thứ tự hiện là vấn đề → phân hoạch/vết → điều kiện bộ nhớ → vết dò → thuật toán/dừng → tính đúng → skew/đường lui → chi phí → kiểm tra.
- Rà lại N04–S01: vết Block và Indexed đứng trước giả mã hoặc công thức tương ứng; câu nối sang Sort-Merge không đổi.
- `X01–X04` vẫn dùng nguyên dữ kiện Bài 15.3 và đúng 35 phút. Hai quy ước được tách bằng $q$: nguồn $q=M-1$, deck $q=M-2$.
- Biên tập no-ai-slop giữ câu ngắn, bỏ lời khẳng định “an toàn” thiếu giả thiết. Rà Quill xác nhận ký hiệu và dữ liệu truyền liên tục giữa ví dụ, thuật toán, chứng minh và chi phí; không tạo `quill.json`.

## Rà chính xác sau chỉnh sửa

- H11 đổi hai điều kiện độc lập thành `nếu / ngược lại nếu / ngược lại`; một cặp con chỉ được xây–dò, đưa vào hàng đợi hoặc chuyển sang Block Nested đúng một lần.
- H10 dùng $h_2(k)=\lfloor k/2\rfloor\bmod2$, khác $h_1(k)=k\bmod2$. Đã chạy lại: $h_2(4)=0$, $h_2(2)=h_2(6)=1$; chỉ $(r_2,s_2)$ được xuất.
- X03 dùng công thức seek slide 23: tạo run $2\lceil b/M\rceil$, phần trộn $\lceil b/b_b\rceil(2P(b)-1)$ với cơ số $\lfloor M/b_b\rfloor-1$, rồi cộng seek quét nối.
- X04 bỏ quy ước $M-1$ của Block Nested khỏi Grace. Pha phân hoạch và pha xây–dò được tách; điều kiện deck là $\max_i b_{s_i}\le M-2$.
- M01 và bảng ký hiệu ghi giả thiết $M\ge3$; H15 dùng câu hỏi số nhiều.

## Đóng vòng chính xác cuối

- X04 đã bổ sung fan-out $f=\lfloor M/b_b\rfloor-1$, điều kiện $f>1$ và số lượt theo quy ước nguồn: $L=\lceil\log_f(800/M)\rceil$ khi phía xây chưa vừa RAM, còn $L=0$ khi đã vừa. Pha phân hoạch và điều kiện xây–dò $\max_i b_{s_i}\le M-2$ vẫn được tách riêng.
- Mọi lỗi `chặn bàn giao` và `nghiêm trọng` của vòng accuracy đã đóng; lỗi trung bình X04 đã sửa.
- `python3 -m reloadserver 8765` thất bại với `/usr/bin/python3: No module named reloadserver`. Cổng 8765 hiện có máy chủ cục bộ do điều phối viên dùng cho QA.
- Browser và Codex Slides không khả dụng trong môi trường tác tử; không tuyên bố đã rà trực quan bằng Codex Slides.

## Tự chạy lại kết quả

- `student` ngoài trong tuple Nested: $5.000\cdot400+100=2.000.100$ lần truyền; `takes` ngoài: $10.000\cdot100+400=1.000.400$.
- Grace ví dụ nguồn: $3(100+400)=1.500$ lần truyền lý tưởng; với sáu phân hoạch, $1.500+4\cdot6=1.524$; với $b_b=3$, $2(34+134)=336$ seek.
- Bài 15.3: $b_{r_1}=20.000/25=800$ và $b_{r_2}=45.000/30=1.500$. Nested với $r_1$ ngoài: 30.000.800 lần truyền; với $r_2$ ngoài: 36.001.500.
- Bài 15.5: đọc mỗi quan hệ đúng một lần, cần $b_r+b_s$ lần truyền và $\min(b_r,b_s)+2$ khối bộ nhớ theo lời giải chính thức.

## Tự rà no-ai-slop

- Nội dung hiển thị dùng câu ngắn, số liệu và cơ chế cụ thể; không dùng lời dẫn rỗng, ca tụng, câu hỏi tu từ hoặc kết luận lặp.
- Mọi lời mời tương tác trên mặt trang dùng nhãn “Câu hỏi:”.
- Tiêu đề viết bằng tiếng Việt; chỉ giữ tên thuật toán chuẩn và ký hiệu.

## Tự rà Quill

- Mạch xuyên suốt giữ cùng một phép nối và thay đổi đơn vị tái sử dụng: tuple → nhóm khối → chỉ mục → thứ tự → phân hoạch.
- Ký hiệu $r,s,n_r,n_s,b_r,b_s,M,M-2,b_b,p_h$ không đổi nghĩa.
- Ví dụ `student/takes` đi từ use case đến công thức Nested, Grace và bảng so sánh.
- Không có và không tạo `quill.json` vì đây không phải dự án sách.

## Codex Slides và giới hạn kiểm định

- Browser và project id của Codex Slides không khả dụng trong môi trường tác tử này; không tuyên bố đã rà bằng Codex Slides.
- Bốn báo cáo độc lập và kiểm định storyboard đã được hợp nhất trong vòng chỉnh sửa này. Kiểm định trình duyệt cuối vẫn thuộc điều phối viên.

## Kiểm định tĩnh sau chỉnh sửa

- Parse HTML xác nhận 60 trang, gồm 50 trang giảng và 10 trang recitation; 60 `data-slide-id` duy nhất và 60 khối ghi chú.
- Tổng thời lượng lấy từ ghi chú là 120 phút giảng và 60 phút recitation.
- Cấu trúc `section`, `div`, `aside`, dấu phân cách công thức và mọi đường dẫn cục bộ hợp lệ.
- Parse đủ 10 SVG; mỗi tệp có `role="img"`, `aria-label`, `title` và `desc` tiếng Việt.
- Không có tham chiếu ảnh raster hoặc tài nguyên mạng cốt lõi. `git diff --check` không báo lỗi.
- Sau vòng sửa: vẫn có 60 trang, gồm 50 trang giảng và 10 trang recitation; 60 mã duy nhất, 60 notes và 60 dòng storyboard. Tổng thời lượng notes của `P00–C04` là 120 phút; `X01–X09` là 60 phút (`X00` chỉ công bố tổng, không cộng thêm).
