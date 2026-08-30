# Nhật ký rà soát Bài 15

## Trạng thái bản nháp

- Tạo deck RevealJS gồm 50 trang giảng và 10 trang recitation.
- Phân bổ phần giảng đúng 120 phút; recitation đúng 60 phút.
- Tạo SVG cục bộ cho use case, ba biến thể vòng lặp lồng, nhóm Sort-Merge, build–probe, phân hoạch Grace, chi phí, skew và bản đồ chọn thuật toán.
- Không sửa `2627-1/index.html`, `2627-1/lecture-style.css` hoặc bài khác. Chưa commit và chưa push.

## Quyết định nguồn và phạm vi

- Ch15 slide 24–41 là trục. Slide 7–9 cung cấp mô hình chi phí; slide 17–23 chỉ được nhắc để dùng lại External Merge Sort từ Bài 12.
- Slide 28, 30, 35 và 40 bị ẩn trong PPTX nhưng vẫn được đọc vì chứa công thức, ví dụ và lập luận đúng liên quan trực tiếp.
- Bỏ selection, aggregation, set operations, outer join, stream và cache-conscious processing vì nằm ngoài sản phẩm Bài 15. Chỉ dùng khái niệm vật chất hóa để chốt mô hình chi phí Sort-Merge của Bài 15.3.
- Recitation dùng nguyên đề 15.3, 15.4 và 15.5 từ Practice Exercises; lời giải và hướng dẫn chấm bám Practice Solutions tương ứng.

## Sửa lỗi và sai khác có chủ ý

- Slide 33: sửa tên phân hoạch của $s$ và dùng $p_h$ phân hoạch đánh số $0..p_h-1$.
- Slide 37: sửa phía dò thành $r_i$; pha xây–dò yêu cầu $\alpha b_{s_i}+b_{in}+b_{out}\le M$, với $b_{in}=b_{out}=1$.
- Slide 39: tách $3(b_r+b_s)$ lý tưởng và số hạng tối đa $4p_h$ do khối biên; không cộng hai cách đếm mà không giải thích.
- Slide 40: thay bố trí năm phân hoạch không khả thi bằng $M=20$, $b_b=2$, $p_h=7$, $\alpha=1{,}2$ và kích thước $15;15;14;14;14;14;14$. Pha phân hoạch dùng 16 khối; pha xây–dò tái dùng bộ nhớ và đạt $1{,}2\cdot15+1+1=20$.
- Slide 41: bỏ Hybrid Hash Join khỏi tuyến chính vì phân bổ bộ đệm của ví dụ nguồn không đủ rõ để kiểm chứng. Dùng chỗ này cho vết Grace ở mức tuple và điều kiện dừng.
- Sort-Merge lấy tích Descartes của hai nhóm khóa trùng; không tiến một phía rồi làm mất bản sao.
- Hash Join lưu danh sách tuple trong mỗi khóa, kiểm tra khóa thật sau khi băm và không ghi đè bản sao.
- Khi skew làm phân hoạch xây tràn, deck nêu băm lại cả cặp phân hoạch và fallback Block Nested-Loop Join.
- Deck xét khóa nối không `NULL`; ngữ nghĩa SQL `NULL` nằm ngoài phạm vi và được nêu công khai.
- Lời giải 15.3 dùng $q=M-1$ ở Block Nested khi đầu ra không giữ bộ đệm riêng; slide 28 dùng $q=M-2$ khi vật chất hóa đầu ra. Deck dùng $q$ và khai báo bố trí thay vì áp một giá trị toàn cục.

## Hợp nhất các báo cáo độc lập

- **Chặn bàn giao — H11:** giả mã cũ nói “phân hoạch lại” nhưng không gọi đệ quy hoặc đưa cặp tràn vào cấu trúc công việc. Đã thay bằng hàng đợi; chỉ xếp lại khi kích thước giảm, nếu không dùng Block Nested-Loop Join.
- **Nghiêm trọng — H08, H10–H14:** phép chia trung bình từng bị trình bày như bảo đảm bộ nhớ. Đã thay bằng bố trí khả thi và điều kiện cực đại có phụ trội $\alpha$; thuật toán, chứng minh và đường lui đứng trước chi phí trường hợp không tràn.
- **Nghiêm trọng — H12:** chứng minh cũ mới cho thấy cùng khóa cùng số phân hoạch, chưa chứng minh các cặp con rời nhau và được xử lý đúng một lần. Đã thêm lập luận khởi tạo–duy trì–kết thúc trong notes và mệnh đề phân hoạch rời trên mặt trang.
- **Nghiêm trọng — X02–X04:** 25 phút của Bài 15.3 hiển thị sẵn kết quả. Đã đổi thành ba trang giao việc; toàn bộ đáp án, hai hướng Block Nested, seek sắp/trộn và Hash seek chuyển vào notes.
- **Nghiêm trọng — N09–N11:** Indexed Nested thiếu vết khóa vắng/bản sao, giả mã, dừng và công thức đúng đơn vị. Đã bổ sung cả bốn; chi phí dùng $b_r(t_T+t_S)+n_rc$.
- **Trung bình — N06, H07–H10:** Block Nested và Grace thiếu vết chạy tay. Đã dùng ví dụ tuple nhỏ; vết Grace truyền cùng dữ liệu qua $h_1$, $h_2$, va chạm, so khóa và cặp kết quả.
- **Trung bình — nhịp 120 phút:** không tăng số trang; loại Hybrid khỏi tuyến chính và dành đúng thời gian cũ cho vết Grace. Tổng giảng vẫn 120 phút.
- **Trung bình — P01 và thuật ngữ:** giữ P01 vì SVG đã hiển thị hai quan hệ, khóa ID và số khối; notes cung cấp giới hạn đĩa. Thuật ngữ chuẩn trong tên thuật toán được giữ, còn build/probe tiếp tục đi cùng “phía xây/phía dò”.
- **Trung bình — X07:** không giữ câu nguồn như kết luận. Đã thay bằng bất đẳng thức tổng I/O và ghi rõ kích thước phía ngoài không phải điều kiện đủ.

## Rà sau chỉnh sửa

- Rà lại H06–H15 và hai trang lân cận: thứ tự hiện là vấn đề → phân hoạch/vết → điều kiện bộ nhớ → vết dò → thuật toán/dừng → tính đúng → skew/đường lui → chi phí → kiểm tra.
- Rà lại N04–S01: vết Block và Indexed đứng trước giả mã hoặc công thức tương ứng; câu nối sang Sort-Merge không đổi.
- `X01–X04` vẫn dùng nguyên dữ kiện Bài 15.3 và đúng 35 phút trong storyboard. Hai bố trí được tách bằng $q$: $q=M-1$ khi đầu ra được chuyển tiếp, $q=M-2$ khi vật chất hóa.
- Biên tập no-ai-slop giữ câu ngắn, bỏ lời khẳng định “an toàn” thiếu giả thiết. Rà Quill xác nhận ký hiệu và dữ liệu truyền liên tục giữa ví dụ, thuật toán, chứng minh và chi phí; không tạo `quill.json`.

## Rà chính xác sau chỉnh sửa

- H11 đổi hai điều kiện độc lập thành `nếu / ngược lại nếu / ngược lại`; một cặp con chỉ được xây–dò, đưa vào hàng đợi hoặc chuyển sang Block Nested đúng một lần.
- H10 dùng $h_2(k)=\lfloor k/2\rfloor\bmod2$, khác $h_1(k)=k\bmod2$. Đã chạy lại: $h_2(4)=0$, $h_2(2)=h_2(6)=1$; chỉ $(r_2,s_2)$ được xuất.
- X03 chốt kết quả sắp được vật chất hóa: seek sắp là $2\lceil b/M\rceil+2P(b)\lceil b/b_b\rceil$, rồi cộng seek quét nối. Biên $P=0$ không sinh số hạng âm.
- X04 tách pha phân hoạch $(p_h+1)b_b\le M$ khỏi pha xây–dò $\alpha\max_i b_{s_i}+b_{in}+b_{out}\le M$.
- M01 bỏ vùng $M-2$ toàn cục và bổ sung $q,\alpha$; H15 dùng câu hỏi số nhiều.

## Đóng vòng chính xác cuối

- X04 bỏ cận số lượt dựa trên kích thước trung bình vì không bảo đảm phân hoạch lớn nhất vừa. Trang yêu cầu kiểm trực tiếp hai bố trí bộ đệm và cộng chi phí từng lượt phát sinh nếu phải phân hoạch lại.
- Mọi lỗi `chặn bàn giao` và `nghiêm trọng` của vòng accuracy đã đóng; lỗi trung bình X04 đã sửa.
- `python3 -m reloadserver 8765` thất bại với `/usr/bin/python3: No module named reloadserver`. Cổng 8765 hiện có máy chủ cục bộ do điều phối viên dùng cho QA.
- Browser và Codex Slides không khả dụng trong môi trường tác tử; không tuyên bố đã rà trực quan bằng Codex Slides.

## Tự chạy lại kết quả

- `student` ngoài trong tuple Nested: $5.000\cdot400+100=2.000.100$ lần truyền; `takes` ngoài: $10.000\cdot100+400=1.000.400$.
- Grace ví dụ đã sửa: $3(100+400)=1.500$ lần truyền lý tưởng; với bảy phân hoạch, $1.500+4\cdot7=1.528$; với $b_b=2$, $2(50+200)=500$ seek.
- Bài 15.3: $b_{r_1}=20.000/25=800$ và $b_{r_2}=45.000/30=1.500$. Nested với $r_1$ ngoài: 30.000.800 lần truyền; với $r_2$ ngoài: 36.001.500.
- Bài 15.5: đọc mỗi quan hệ đúng một lần, cần $b_r+b_s$ lần truyền và $\min(b_r,b_s)+2$ khối bộ nhớ theo lời giải chính thức.

## Tự rà no-ai-slop

- Nội dung hiển thị dùng câu ngắn, số liệu và cơ chế cụ thể; không dùng lời dẫn rỗng, ca tụng, câu hỏi tu từ hoặc kết luận lặp.
- Mọi lời mời tương tác trên mặt trang dùng nhãn “Câu hỏi:”.
- Tiêu đề viết bằng tiếng Việt; chỉ giữ tên thuật toán chuẩn và ký hiệu.

## Tự rà Quill

- Mạch xuyên suốt giữ cùng một phép nối và thay đổi đơn vị tái sử dụng: tuple → nhóm khối → chỉ mục → thứ tự → phân hoạch.
- Ký hiệu $r,s,n_r,n_s,b_r,b_s,M,q,b_b,p_h,\alpha$ không đổi nghĩa; bố trí bộ đệm được khai báo tại thuật toán dùng nó.
- Ví dụ `student/takes` đi từ use case đến công thức Nested, Grace và bảng so sánh.
- Không có và không tạo `quill.json` vì đây không phải dự án sách.

## Codex Slides và giới hạn kiểm định

- Browser và project id của Codex Slides không khả dụng trong môi trường tác tử này; không tuyên bố đã rà bằng Codex Slides.
- Các báo cáo độc lập và kiểm định storyboard đã được hợp nhất trong vòng chỉnh sửa này. Kiểm định trình duyệt cuối vẫn thuộc điều phối viên.

## Kiểm định tĩnh sau chỉnh sửa

- Parse HTML xác nhận 60 trang, gồm 50 trang giảng và 10 trang recitation; 60 `data-slide-id` duy nhất và 60 khối ghi chú.
- Thời lượng chỉ nằm trong storyboard: 120 phút giảng và 60 phút recitation; HTML và notes không chứa thời lượng.
- Cấu trúc `section`, `div`, `aside`, dấu phân cách công thức và mọi đường dẫn cục bộ hợp lệ.
- Parse đủ 10 SVG; mỗi tệp có `role="img"`, `aria-label`, `title` và `desc` tiếng Việt.
- Cả 10 SVG đều được HTML tham chiếu; không còn tài sản mồ côi.
- Không có tham chiếu ảnh raster hoặc tài nguyên mạng cốt lõi. `git diff --check` không báo lỗi.
- Sau vòng sửa: vẫn có 60 trang, gồm 50 trang giảng và 10 trang recitation; 60 mã duy nhất, 60 notes và 60 dòng storyboard. Tổng trong storyboard là 120+60 phút.

## Vòng triển khai theo đặc tả phân tích cuối

- **Nghiêm trọng — M01, N05–N08, H06–H15:** vùng $M-2$ từng bị dùng như quy ước chung. Quyết định: dùng $q$ cho Block Nested; tách bộ đệm phân hoạch và bảng băm Grace; thêm $\alpha$.
- **Nghiêm trọng — S08, X03:** công thức seek từng mô tả lượt trộn cuối không vật chất hóa, trong khi lời giải 15.3 cộng dãy sắp đã ghi. Quyết định: chốt phương án vật chất hóa và sửa cả biên $P=0$.
- **Nghiêm trọng — H08–H14:** bộ tham số cũ không chứng minh được khả thi. Quyết định: dùng $p_h=7$, $b_b=2$, $M=20$, $\alpha=1{,}2$ và vết kích thước cụ thể; cập nhật transfer, khối biên và seek.
- **Trung bình — X07:** câu theo kích thước có thể bị đọc như điều kiện đủ. Quyết định: so tổng I/O bằng bất đẳng thức và giữ câu nguồn chỉ như ngữ cảnh có điều kiện trong notes.
- Ba SVG trước đó không được tham chiếu nay được dùng tại `N05`, `N09`, `H08` và sửa theo đúng dữ kiện. `skew-fallback.svg` bỏ số lượng phân hoạch cố định để không mâu thuẫn với ví dụ bảy phân hoạch.
- Đã tự rà theo `no-ai-slop/eval.md`: không thêm mở bài rỗng, câu quảng bá, câu hỏi tu từ hay kết luận lặp. Quill được dùng để rà thứ tự ví dụ → đặc tả → thuật toán → chi phí và sự liên tục của $q,b_b,p_h,\alpha$; không tạo `quill.json`.

## Quyết định sau năm báo cáo độc lập

| Báo cáo | Mức độ và trang | Quyết định |
|---|---|---|
| Góc nhìn sinh viên | Nghiêm trọng X05; trung bình M01, N09, H02, S07–S08, H08, H11, H14 | Áp dụng: làm X05 tự chứa; giảm ký hiệu mở đầu; hiện đầu ra Indexed, hai loại va chạm, hai nhánh nhóm trùng, ví dụ số và phép tính. Đổi `Block NLJ` thành `Block Nested`. Không chuẩn hóa mọi đáp án fragment vì tăng chữ mà không sửa lỗi học thuật. |
| Chuyên gia giải thuật và khoa học dữ liệu | Nghiêm trọng H00–H15; trung bình P01–P02, C02, X07 | Áp dụng: tách mô hình bộ nhớ theo pha, chốt $M=20$, ghi các trạng thái C02 là giả định thay thế và giữ bất đẳng thức tổng I/O ở X07. |
| Độ chính xác toán học và thuật toán | Nghiêm trọng S05–S08, H03–H15; trung bình N11, C01 | Áp dụng: thêm miền $b\ge1$, biên $P(0)$, điều kiện nhóm trùng, phụ trội bảng băm và hai bộ đệm; cấm so trực tiếp thời gian chỉ mục với số lần truyền. |
| Phản biện học thuật và giảng dạy | Nghiêm trọng thứ tự Grace; trung bình H08, H11–H14 | Áp dụng thứ tự `H06→H07→H10→H08→H09→H13→H11→H12→H14→H15`; vết đúng đắn đi trước bố trí quy mô, rồi skew, thuật toán, chứng minh và chi phí. |
| Kết nối và mạch viết | Nghiêm trọng cụm Grace; trung bình C00–X05 | Áp dụng câu nối mới trong storyboard; giới hạn C00–C01 ở các biến thể trong bài; C04 nối điều kiện lựa chọn sang ba bài nguồn. |

## Trạng thái sau lượt chỉnh sửa

- Giữ 60 trang, 7 mạch ngoài và tổng thời lượng 120+60 phút trong storyboard.
- Static mới: 60 mã duy nhất, 60 notes, 7 section ngoài; thứ tự Grace là `H06→H07→H10→H08→H09→H13→H11→H12→H14→H15`; mọi ảnh tham chiếu tồn tại; 10 SVG parse được và đủ `role`, `aria-label`, `title`, `desc`; `git diff --check` đạt.
- Rà lại toán đạt sau khi xác định $b_b$ là hệ số đọc/ghi liên tiếp trong mô hình seek tổng, độc lập với $b_{in},b_{out}$; 500 là số seek tổng theo công thức nguồn, không gán riêng cho pha phân hoạch.
- Rà lại mạch đạt: thứ tự Grace nối từ vết đúng đắn sang bố trí hai pha, skew, ba nhánh hữu hạn, chứng minh, chi phí và kiểm tra. Chưa tuyên bố QA trình duyệt hoặc kiểm định cuối.

## Kiểm định cuối của điều phối viên

- `python3 -m reloadserver 8765` không chạy vì môi trường thiếu mô-đun `reloadserver`; bản thay thế trên 8765 gặp cổng đã được dùng. Dùng máy chủ dự phòng cục bộ ở cổng 8767, không dừng tiến trình ngoài phạm vi.
- Chromium duyệt đủ 60 trang ở 1280 × 720 và 800 × 600: không có lỗi console, lỗi KaTeX, tài nguyên hỏng hoặc phần tử vượt khung theo kiểm tra tự động.
- Rà ảnh các trang rủi ro S08, H08, H11, H14 và X05 phát hiện công thức dưới ba thẻ H14 sát chân trang; giảm chiều cao hình H14 từ 335 xuống 250 px rồi chạy lại kiểm định trang này.
- Kiểm tra bàn phím xác nhận điều hướng ngang/dọc hoạt động; DOM có 60 mã duy nhất, 60 notes, `lang="vi"` và không có phụ thuộc mạng cốt lõi.
- Codex Slides đã tạo dự án bền vững `20260830180051-b-i-15-thu-t-to-n-k-t-n-i-d-li-u-ssuw` và nhận snapshot HTML cuối sau sửa H14 dưới mã học liệu `20260830183800757-8jy2.html`. Phiên Codex hiện tại không có bề mặt Browser nội bộ để giữ dự án mở và đối chiếu trực quan, nên không tuyên bố đã rà hình bằng Browser của Codex Slides; kiểm tra trực quan dùng RevealJS cục bộ.
