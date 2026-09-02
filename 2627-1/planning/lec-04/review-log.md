# Nhật ký rà soát Bài 4

## Nguồn đã đọc

- `sources/source.md`: Bài 4 theo thứ tự đề xuất; mục tiêu, tiên quyết và ánh xạ từ buổi gốc 5.
- `sources/reference-slides/README.md`: dòng Bài 4 và yêu cầu so sánh MMDS với Stanford.
- `sources/textbooks/mmds-3e-ch05-link-analysis.pdf`: mục 5.3–5.5, Hình 5.15–5.20 và bài tập.
- `sources/reference-slides/mmds/ch05-linkanalysis1.pdf` và `ch05-linkanalysis2.pdf`.
- `sources/reference-slides/stanford-cs246/10-spam.pdf`.
- `2627-1/lecture-template.html`, `2627-1/lecture-style.css`, `2627-1/index.html` và bố cục Bài 3.

## So sánh MMDS và Stanford

| Cụm | MMDS | Stanford | Quyết định |
|---|---|---|---|
| PageRank theo chủ đề | Có công thức, ví dụ Hình 5.15 và bài tập trực tiếp | Công thức tương đương, sau đó đi sâu vào Pixie và số liệu hệ thống ngoài phạm vi | Dùng MMDS; không đưa Pixie vào Bài 4 |
| Liên kết rác | Có Hình 5.16, phân tích $x,y,n,m$ và xấp xỉ | Hình và diễn giải gần như tương đương | Ưu tiên MMDS; đổi ký hiệu sách thành $x,y,N,q$ để không lẫn $n,m_G$ của đồ thị |
| TrustRank, khối lượng rác | Có lựa chọn hạt giống, Hình 5.17 và bài tập | Có trực giác và hạt giống, nhưng không có bài tập cần dùng | Dùng MMDS; Stanford chỉ đối chiếu thuật ngữ |
| HITS | Có Hình 5.18–5.20, phép lặp và bài tập | Tệp Stanford được ánh xạ không trình bày đầy đủ HITS trong phần hiện có | Dùng MMDS toàn bộ |

## Sửa lỗi và làm chặt giả thiết

| Mức độ | Trang | Vấn đề hoặc bằng chứng | Quyết định |
|---|---|---|---|
| nghiêm trọng | S04–S05 | MMDS §5.4.2 bỏ phần dịch chuyển trực tiếp $(1-\beta)/N$ của trang đích rồi trình bày kết quả đơn giản hóa. | Nêu đẳng thức chính xác $y=x/(1-\beta^2)+(\beta q+1)/(N(1+\beta))$, sau đó mới nêu xấp xỉ và sai số $1/[N(1+\beta)]$. |
| nghiêm trọng | H08 | MMDS nói nút cụt và bẫy nhện không cản HITS hội tụ có ý nghĩa, nhưng không nêu điều kiện phổ. | Chỉ kết luận hướng duy nhất khi trị riêng lớn nhất phù hợp trội và khởi tạo có thành phần theo hướng đó. |
| trung bình | S05 | Công thức xấp xỉ có thể bị đọc thành tăng $q$ làm $y$ lớn tùy ý. | Nêu $q&lt;N$, tổng hạng bằng 1 và việc thêm trang có thể đổi $N$ cùng $x$. |
| trung bình | K03–K05 | Cụm từ “fraction” trong nguồn dễ làm tỷ số bị hiểu là xác suất trong $[0,1]$. Hình 5.17 có giá trị âm. | Ghi $r_p>0$, cho phép âm, không kẹp và không tạo ngưỡng bảo đảm. |
| trung bình | K01–K02 | Ví dụ miền tin cậy có thiên lệch địa lý và không bảo đảm trang sạch. | Giữ cảnh báo của sách, thêm giới hạn độ phủ và sai hạt giống. |
| trung bình | H05 | Nguồn dừng khi thay đổi “đủ nhỏ” nhưng không có giới hạn vòng, cờ hoặc xử lý vector 0. | Thêm $K_{\max}$, $\tau$, cờ hội tụ và hai nhánh vector 0 trực tiếp trong giả mã. |
| nhẹ | H02 | $L$ dùng hàng nguồn, còn $P$ ở Bài 3 dùng cột nguồn. | Đặt hai quy ước cạnh nhau trước khi nhân ma trận. |
| nhẹ | T07 | §5.3.4 chuyển sang Jaccard, phá mạch và đi trước tiên quyết Bài 5. | Không dạy §5.3.4; ghi rõ trong outline và storyboard. |

## Bài tập và đáp án đã kiểm tra

- Bài 5.3.1, trang in 199/PDF 25, 18 phút. Đáp án: $S=\{A\}$ cho $(3/7,4/21,4/21,4/21)$; $S=\{A,C\}$ cho $(27/70,6/35,19/70,6/35)$.
- Bài 5.4.2, trang in 204/PDF 30, 22 phút gồm trang dữ kiện và trang giải. Quy ước nguồn: PageRank cơ sở không có hệ số giảm $(1/3,2/9,2/9,2/9)$; TrustRank $\beta=0{,}8$, $T=\{B\}$; không kẹp khối lượng rác âm.
- Bài 5.5.1, trang in 208/PDF 34, 20 phút. Ma trận $L$ $4\times4$, hai vòng và hai vector giới hạn được tính lại; nhóm được dùng bảng tính và ngưỡng thay đổi $10^{-3}$.
- Tổng bài tập: 60 phút; không có trang logistics riêng.

## Tài sản trực quan

| Tệp | Nguồn và xử lý |
|---|---|
| `hinh-5-15.svg` | Vẽ lại MMDS Hình 5.15, giữ cạnh và tập $S=\{B,D\}$ |
| `hinh-5-1-trung-tinh.svg` | Cùng đồ thị Hình 5.1/5.15 nhưng không đánh dấu tập dịch chuyển; dùng riêng cho R01–R02 |
| `hinh-5-16-cum-thao-tung.svg` | Vẽ lại MMDS Hình 5.16, Việt hóa ba vùng |
| `luong-hang-trong-cum.svg` | Vẽ lại luồng đại lượng trong phân tích MMDS §5.4.2 |
| `hinh-5-18.svg` | Vẽ lại MMDS Hình 5.18, giữ nút cụt E |
| `cap-vai-tro-hits.svg` | Sơ đồ hóa trực giác MMDS §5.5.1; mỗi nút vẫn có cả hai điểm |

Hình 5.17 dùng bảng HTML; Hình 5.19 dùng KaTeX; Hình 5.20 dùng hai bảng HTML. Không có ảnh raster hoặc phụ thuộc mạng cốt lõi.

## Ngoại lệ chỉ dẫn

- Theo chỉ dẫn trực tiếp cho Bài 4, thời lượng chỉ xuất hiện trong storyboard, không đặt trên mặt trang chiếu hoặc trong ghi chú diễn giả. Quyết định này ưu tiên hơn quy ước chung yêu cầu thời lượng trong notes.
- Không cập nhật `index.html`, không sửa CSS/tài sản dùng chung, không commit hoặc đẩy ở giai đoạn bản nháp.

## Tự kiểm biên tập

- Dùng `no-ai-slop`: cắt câu dẫn rỗng, câu hỏi tu từ và nhận định quảng bá; giữ thuật ngữ nhất quán.
- Dùng Outline Workflow của `quill` mà không tạo `quill.json`: rà lại thứ tự tình huống → trực giác → ví dụ cạnh → ma trận → thuật toán → điều kiện → chi phí → kiểm tra.
- Tiêu đề và nhãn thuần Việt; chỉ giữ PageRank, TrustRank, HITS, Web và ký hiệu chuẩn.

## Kiểm định storyboard

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | T00–T07 | Cụm theo chủ đề chưa truyền quyết định truy vấn đến vector được dùng. | T00 chỉ nói chi phí lưu trữ; T07 chỉ kiểm tra $q_S$. | Mở bằng “jaguar”; kết thúc bằng xác định chủ đề → chọn hoặc phối hợp vector → xếp hạng. Đã xử lý. |
| nghiêm trọng | S03–S05 | Chu trình dừng ở đại số ký hiệu, chưa có ứng dụng số và kiểm tra. | Không có hệ số số của Ví dụ 5.11 hoặc câu hỏi phân biệt nguồn hạng. | Thêm $3{,}6036$, $0{,}4595$ và câu hỏi về $x$, dịch chuyển, tuần hoàn. Đã xử lý. |
| nghiêm trọng | H02–H07 | Ma trận và giả mã xuất hiện trước chạy tay. | H02, H04, H05 đứng trước H06–H07. | Đưa H03 và H06–H07 trước H05; nối tổng trên cạnh sang ma trận. Đã xử lý. |
| trung bình | Z01 | Một bảng gánh cơ chế, phạm vi, đầu ra và chi phí. | Năm cột ở cỡ chữ nhỏ. | Tách Z01 cơ chế và Z02 quyết định–chi phí. Đã xử lý. |

## Rà soát góc nhìn sinh viên

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| chặn bàn giao | R02 | Bài 5.4.2 không tự chứa đồ thị, ma trận và PageRank cơ sở. | Dữ kiện chỉ có trong nguồn hoặc notes. | Tách R02 thành trang dữ kiện có hình trung tính, $P,r$; R03 giữ yêu cầu. Đã xử lý. |
| nghiêm trọng | K00–K04 | Phương trình TrustRank không hiện trước bài tính. | K00 chỉ mô tả bằng lời. | Hiển thị $q_T$ và phép cập nhật trên K00, điều kiện phân phối trên K01. Đã xử lý. |
| nghiêm trọng | T03–T04 | Ví dụ một vòng chỉ cho đầu vào và kết quả. | Không thấy phần cạnh và phần dịch chuyển. | Thêm bảng ba hàng $\beta Pr^{(0)}$, $(1-\beta)q_S$, $r^{(1)}$. Đã xử lý. |
| nghiêm trọng | H05–H07, Z01 | Giả mã và bảng trọng tâm dưới `.75em`. | CSS cũ dùng `.67em` và `.66em`. | Nâng giả mã lên `.75em`, bảng compact `.75em`, bảng thường `.78em`; giảm mật độ H04 và tách Z. Đã xử lý. |
| nghiêm trọng | R01–R03 | Ba bài đều yêu cầu giải hệ đầy đủ trong một phiên. | Hai hệ ở 5.3.1, TrustRank cùng tỷ số, và giới hạn HITS. | Chia ý theo nhóm, thêm checkpoint, công cụ và ngưỡng; giữ nguyên yêu cầu toán học cùng tổng 60 phút. Đã xử lý. |

## Rà soát chuyên gia giải thuật và khoa học dữ liệu

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | T06, S02–S05, H09, Z01 | Ký hiệu kích thước đổi nghĩa giữa các mô hình. | $m$ vừa là số cạnh vừa là số trang hỗ trợ. | Giữ $n=|V|$, $m_G=|E|$; dùng $N,q$ cho trang trại. Đã xử lý. |
| nghiêm trọng | K04 | Bảng nguồn so PageRank và TrustRank ở hai quy ước khác nhau nhưng mặt trang không nói rõ. | Chỉ notes ghi PageRank không có hệ số giảm và TrustRank có $\beta=0{,}8$. | Gắn nhãn hai quy ước và khuyến nghị so cùng thiết lập trong ứng dụng. Đã xử lý. |
| trung bình | H00, H09 | HITS thiếu giới hạn quy mô ngay khi mở. | Chỉ nói tập kết quả truy vấn. | Nêu đồ thị con thưa, không dựng ma trận đặc toàn Web; chốt hai lượt cạnh và $\Theta(n+m_G)$. Đã xử lý. |

## Rà soát độ chính xác toán học và thuật toán của điều phối viên

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | T06, S02–S05, H09, Z01 | $m$ đổi nghĩa làm sai đặc tả chi phí. | Bài 3 dùng $m=|E|$, phần trang trại dùng $m$ cho trang hỗ trợ. | Dùng $m_G$ và $N,q$. Đã xử lý trong HTML, SVG và planning; đại số được thay lại. |
| nghiêm trọng | R01, R02 | SVG theo chủ đề gắn $S=\{B,D\}$ gây dữ kiện ngầm sai; R02 thiếu $P,r$. | Hai bài dùng $S=\{A\}$, $S=\{A,C\}$ hoặc $T=\{B\}$. | Tạo `hinh-5-1-trung-tinh.svg`; hiển thị $P,r$ ở R02. Đã xử lý. |
| nghiêm trọng | K00–K04 | Thiếu phương trình TrustRank và nhãn quy ước. | Công thức chỉ suy được từ phần T; Hình 5.17 trộn hai thiết lập nguồn. | Thêm công thức K00–K01 và nhãn K04. Đã xử lý. |
| nghiêm trọng | H05 | Chuẩn hóa vector 0 chỉ ở notes. | Giả mã cũ gọi hàm chuẩn hóa không toàn phần. | Đưa hai phép kiểm tra chuẩn 0 và đầu ra suy biến lên mặt trang. Đã xử lý. |
| trung bình | H08 | “Trị riêng phù hợp là trội” mơ hồ. | Không nêu so sánh trị tuyệt đối. | Định nghĩa trị riêng lớn nhất theo trị tuyệt đối lớn nghiêm ngặt hơn trị riêng kế tiếp. Đã xử lý. |

Tác tử điều phối đã tính độc lập các vector PageRank theo chủ đề, công thức chính xác và xấp xỉ trang trại, bảng K04, đáp án R02, hai vòng H06–H07 và đáp án HITS; các giá trị số hiện tại đạt.

## Rà soát phản biện học thuật và giảng dạy của điều phối viên

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | T00, T06–T07 | Thiếu trường hợp truy vấn và quyết định dùng vector. | Mở phần bằng chi phí; kết thúc bằng phép viết $q_S$. | Dùng “jaguar” và quy trình xác định chủ đề → chọn/phối hợp → xếp hạng. Đã xử lý. |
| nghiêm trọng | H02–H07 | Hình thức và giả mã đứng trước ví dụ. | Sinh viên chưa cộng điểm trên một cạnh trước khi thấy $L,L^T$. | Đổi thứ tự H00→H01→H03→H02→H04→H06→H07→H05→H08→H09. Đã xử lý và rà các trang lân cận. |
| nghiêm trọng | S03–S05 | Thiếu ứng dụng số và kiểm tra. | Không dùng Ví dụ 5.11. | Thêm hệ số nguồn và câu hỏi xác định ba nguồn hạng. Đã xử lý. |
| nghiêm trọng | H05–H07, Z01 | Cỡ chữ dưới chuẩn. | `.67em` và `.66em`. | Nâng lên ít nhất `.75em`, giảm nội dung và tách Z. Đã xử lý. |
| trung bình | K04, R03 | Quy ước nguồn và tiêu chuẩn hoàn thành chỉ ở notes. | Sinh viên không thấy thiết lập so sánh hoặc cách dừng. | Đưa quy ước lên K04; R04 cho phép bảng tính, ngưỡng $10^{-3}$ và ba chữ số. Đã xử lý. |

## Lượt chỉnh sửa tiếp theo (bản ghi kế hoạch)

- Phạm vi: chỉ sửa HTML Bài 4 và `planning/lec-04/{outline,storyboard,review-log}.md`; `index.html` đã đúng, không sửa; không sửa CSS chung, SVG hoặc tệp khác.
- Ba thay đổi đã có trong HTML từ lượt dở dang được giữ nguyên: cỡ `pre`/`.trace` nâng lên, cầu nối T00 trên mặt trang, giả thiết T05 về tính co.
- Việc còn lại: thêm Z03 (thu hồi P01, nối recitation), thêm R00 (mở section recitation), phân bổ storyboard 120+60, S03 tách hai nguồn hạng, S04 hiện phương trình mở rộng, K00 thêm $t^{(0)}=q_T$, H00 câu nối một điểm → hai vai trò, H03 định nghĩa $h/a$, H06 quy tắc chuẩn hóa, H05 $0&lt;\tau&lt;1$, Z01 thêm $a^{(0)}=0$, R02 ghi dùng cho R03/R04, R04 nối R02 và phân biệt L/P, T04 bỏ gần đúng, K04 cảnh báo hai thiết lập, T07 notes bỏ Jaccard khỏi mạch, R01 giải thích phần dư điểm cố định; giữ 7 outer sections và ID HITS phi tuần tự có chủ ý.
- Phân tích nguồn: đọc lại `sources/textbooks/mmds-3e-ch05-link-analysis.pdf` mục 5.3–5.5 và hai tệp slide MMDS phần 2 để xác nhận các bổ sung trên không thêm khẳng định ngoài nguồn; các bổ sung đặc tả ($K_{\max}$, $\tau$, cờ, khởi tạo) đã được ghi rõ là bổ sung trong notes.
- Kiểm định storyboard sau chỉnh sửa: 41 `data-slide-id` duy nhất (P00–P01, T00–T07, S00–S05, K00–K05, H00–H09, Z00–Z03, R00–R04); 7 outer sections; phần giảng 120 phút (Z03 2 phút gộp vào tổng), bài tập 60 phút (R00 0 phút mở section); hai trang lân cận của mỗi thay đổi đã rà lại câu nối và ký hiệu.
- Nội dung mới qua bộ lọc `no-ai-slop`: không câu dẫn rỗng, không câu hỏi tu từ, không nhận định quảng bá; rà `quill` về mạch tình huống → trực giác → hình thức → kiểm tra và tính nhất quán thuật ngữ, ký hiệu ($q_S$, $q_T$, $t^{(u)}$, $h,a$, $L$, $P$, $N,q$, $m_G$) mà không tạo `quill.json`.

## Báo cáo độc lập của các tác tử rà soát (lượt này)

| Báo cáo | Phát hiện chính | Mức độ | Quyết định |
|---|---|---|---|
| Rà thuật toán | S04 thiếu phương trình mở rộng trước kết quả; K00 thiếu khởi tạo $t^{(0)}=q_T$; H05 thiếu điều kiện $0&lt;\tau&lt;1$ | nghiêm trọng | Đã áp dụng trong HTML và storyboard |
| Rà giảng dạy | Thiếu Z03 thu hồi và R00 mở recitation; H00 thiếu câu nối một điểm → hai vai trò | nghiêm trọng | Đã áp dụng; giữ 7 outer sections |
| Rà toán | T04 nêu điểm cố định gần đúng trùng với bài tập R01; Z01 thiếu $a^{(0)}=0$ | trung bình | Đã áp dụng; T04 bỏ gần đúng, Z01 bổ sung khởi tạo |
| Rà nhất quán ký hiệu | R02 chưa ghi phạm vi dùng chung; R04 chưa nối R02 và chưa phân biệt $L$ với $P$ | trung bình | Đã áp dụng trong notes R02, R04 |
| Rà nguồn | K04 cảnh báo hai thiết lập chỉ ở notes; H06 quy tắc chuẩn hóa chỉ ngầm trong bảng | trung bình | Đã đưa lên mặt trang K04, H04/H06 |

Quyết định chung: mọi lỗi nghiêm trọng và trung bình của năm báo cáo đã được xử lý hoặc ghi rõ lý do không áp dụng (không có đề xuất nào bị bỏ qua trong lượt này); các đề xuất chỉ mang tính phong cách không chặn đã được ghi nhận nhưng không áp dụng để giữ mật độ trang.

## Phạm vi kiểm định của lượt này

- Đã kiểm định: tính nhất quán tĩnh giữa HTML, outline và storyboard (số ID, thứ tự, thời lượng, câu nối); tính đúng đắn toán học của các bổ sung (khởi tạo, điều kiện $\tau$, phương trình mở rộng khớp S03/S05).
- Chưa thực hiện trong lượt này: kiểm duyệt trình duyệt cuối cùng và kiểm định bằng Codex Slides; hai việc này thuộc lượt kiểm định cuối và chưa được phê duyệt.
- Lịch sử: lệnh `python3 -m reloadserver 8765` trong nhật ký cũ chỉ là ghi chép lịch sử của lượt trước, chưa được phê duyệt cho lượt này và không được chạy lại.

## Hậu kiểm nội dung sau chỉnh sửa

- Thay câu tổng kết sai “một cơ chế duy nhất” bằng hai lựa chọn thiết kế đúng ở Z03.
- S05 nay yêu cầu phân loại đủ bốn số hạng của đẳng thức chính xác, gồm dịch chuyển trực tiếp vào trang đích.
- Đưa các câu nối cần đọc trên mặt trang lên H00, H03, R02 và R04; thống nhất mô tả thay thế của R01 với Hình 5.1.
- Bỏ câu mâu thuẫn về trang mở phần bài tập trong ghi chú R00. Đây là hậu kiểm tĩnh, chưa phải kiểm định trình duyệt hoặc Codex Slides.

## Tái kiểm độc lập sau thay đổi cấu trúc

- Vai kết nối và mạch viết rà lại toàn bộ 7 mạch, 41 trang cùng các ranh giới phần. Kết quả: mở đầu T00, kết luận Z03, điểm vào bài tập R00 và chuỗi HITS đều có vai trò, kết nối vào–ra rõ; không còn lỗi mới. Kiểm đếm tĩnh của điều phối viên xác nhận 41 `data-slide-id` duy nhất và 41 khối ghi chú.
- Vai toán học và thuật toán tính lại S03–S05, K00, H03–H07, Z01–Z03 và R01–R04. Công thức chính xác, hai hệ số xấp xỉ, hai vòng HITS và mọi đáp án bài tập đều khớp; không có lỗi chặn bàn giao hoặc nghiêm trọng.
- Hai lượt tái kiểm dùng `requested_model = observed_model = z-ai/glm-5.3-flash`, `provider = OpenRouter`, chế độ chỉ đọc trên bản sao không chứa `.env`.
- Nội dung hiển thị và ghi chú đã được quét lại: không còn mã `data-slide-id` hoặc thời lượng; các thông tin này chỉ nằm trong HTML nội bộ và tệp planning.

## Kiểm định cuối của lượt hiện tại

- Lệnh bắt buộc `python3 -m reloadserver 8765` vẫn thất bại vì môi trường không có mô-đun `reloadserver`. Máy chủ tương thích `/tmp/reloadserver.py` chạy tại `127.0.0.1:8765` để phục vụ đúng thư mục gốc kho; đây là phương án thay thế, không được ghi là lệnh bắt buộc đã thành công.
- Chromium headless duyệt đủ 41 trang ở $1280\times720$ và $800\times600$: không lỗi console, lỗi trang, yêu cầu hỏng hoặc lỗi điều hướng bàn phím. Bộ dò hình học gắn cờ lề của các tiêu đề phần và hộp cuộn nội tại của giả mã; ảnh chụp và contact sheet xác nhận nội dung nằm trong khung, không bị cắt hoặc chồng lấn.
- Kiểm tra tĩnh: 7 `<section>` ngoài, 41 `data-slide-id` duy nhất, 41 khối ghi chú, mọi đường dẫn cục bộ tồn tại, 6 SVG phân tích được và có `role="img"`, `title`, `desc`; không có tham chiếu ảnh raster.
- Tự kiểm `no-ai-slop/eval.md`: nội dung mới không có câu dẫn rỗng, khẩu hiệu, câu hỏi tu từ hoặc kết luận lặp. Rà theo Quill xác nhận mạch, thuật ngữ và ký hiệu liên tục; không tạo `quill.json`.
- Codex Slides: dự án `20260827161616-b-i-4-pagerank-theo-ch-spam-li-n-k-t-v-h-urwd` đọc được nhưng vẫn ở trạng thái `draft`, 0 trang. Design Files hiện có brief, outline và nguồn; tải HTML cuối bằng `upload_design_file` trả HTTP 500. Bề mặt hiện tại không có Browser nội bộ để mở resource link, nên không tuyên bố đã kiểm tra trực quan bằng Codex Slides.

## Runtime

- requested=observed: `z-ai/glm-5.3-flash` qua provider OpenRouter.

## Quyết định sau chỉnh sửa (cập nhật)

- Mọi lỗi `chặn bàn giao` và `nghiêm trọng` trong năm báo cáo đã được xử lý.
- Giữ tổng phần giảng 120 phút và bài tập 60 phút; thời lượng chỉ nằm trong storyboard.
- Không áp dụng đề xuất cũ yêu cầu đưa thời lượng vào notes vì xung đột chỉ dẫn hiện hành.
- Không dạy Jaccard ở Bài 4; T07 chỉ nêu mô hình xác định chủ đề nằm ngoài PageRank và dẫn sang Bài 5.
- Không dựng $L^T$, $LL^T$ hoặc $L^TL$ thành ma trận đặc; H04 chỉ hiển thị $L$, H08 chỉ giữ quan hệ trị riêng.
- Không sửa `index.html`, CSS dùng chung, tài sản dùng chung; không commit hoặc push trong lượt chỉnh sửa này.

## Rà toán lại sau chỉnh sửa

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | T01, K00–K01 | $e_S,e_T$ và điều kiện tập khác rỗng chưa đứng trước phép chia. | Người học chưa đủ dữ kiện để dựng hai vector chỉ báo. | Định nghĩa từng thành phần của $e_S,e_T$ và đặt $S,T\ne\varnothing$ ngay trên mặt trang. Đã xử lý. |
| trung bình | T04, T07 | Thiếu khởi tạo chạy tay và điều kiện để tổ hợp vẫn là phân phối. | $r^{(0)}$ cùng các điều kiện của $\alpha_\ell$ chỉ có trong ghi chú. | Hiển thị $r^{(0)}=q_S$, $\alpha_\ell\ge0$ và $\sum\alpha_\ell=1$. Đã xử lý. |
| trung bình | R04 | Thiếu khởi tạo và chuẩn hóa trong dữ kiện thực hành. | Hai lựa chọn này quyết định toàn bộ dãy HITS. | Ghi $h^{(0)}=e$ và chuẩn hóa bằng thành phần lớn nhất trên mặt trang. Đã xử lý. |
| nhẹ | K00, H05 | $k$ vừa đếm chủ đề vừa đếm vòng; đầu ra suy biến chưa ghi kiểu vector. | Hai nghĩa xuất hiện trong cùng bài; `(0,0)` mơ hồ với số vô hướng. | Giữ $k$ cho số chủ đề, dùng $u$ cho vòng và viết $0_n$. Đã xử lý. |

Rà lại độc lập xác nhận các vector PageRank theo chủ đề, công thức trang trại, bảng khối lượng rác, chiều ma trận HITS, hai vòng lặp, đáp án bài tập và tổng thời lượng đều đúng; không còn lỗi chặn bàn giao.

## Chốt goal ghi chú tự học

- Ba worker OpenRouter độc lập dùng đúng `z-ai/glm-5.3-flash`: reader lập kế hoạch, reader ánh xạ nguồn và reviewer phản biện bản đồ chủ đề. Cả ba chỉ đọc hồ sơ đã lọc, không chứa `.env` hoặc thông tin xác thực.
- Reader nguồn đã đối chiếu trực tiếp MMDS §5.3–5.5, slide MMDS phần 2, Stanford CS246 `10-spam.pdf` và ba đề 5.3.1, 5.4.2, 5.5.1. Nguồn đủ để chuyển trạng thái goal sang `sẵn sàng soạn`.
- Quyết định `giữ`: năm cụm cốt lõi PageRank theo chủ đề, spam farm, TrustRank/khối lượng rác, HITS và so sánh; hai cầu nối ký hiệu Bài 03 và bài tập nguồn.
- Quyết định `thêm` ở mức ngắn: DMOZ trong Ví dụ 5.9 làm bối cảnh; một câu về sự thích nghi qua lại ở §5.4.3 nối spam farm với TrustRank.
- Quyết định `bỏ` hoặc `chuyển bài`: Jaccard sang Bài 05; Pixie, SimRank, API, nhận định lịch sử về Ask, suy đoán về PageRank hiện thời và lời giải đóng đầy đủ Ví dụ 5.15 ra khỏi phạm vi.
- Phần làm chặt của học phần phải được dán nhãn: tập dịch chuyển khác rỗng, $r_p>0$, nhánh vector 0, điều kiện dừng và điều kiện hội tụ HITS. Không gán các phát biểu này nguyên văn cho MMDS.
- Goal được ghi tại `.codex/goal_lecture_4.md` với đúng 13 mục; không tạo `quill.json`.

## Soạn và rà ghi chú Bài 04

### Runtime writer

- Writer được yêu cầu: `deepseek/deepseek-v4-flash-0731` qua OpenRouter.
- Lượt đầu trên dossier nguồn dài thất bại nguyên văn: `model returned an empty or incomplete answer after all retries`; hai phản hồi đều kết thúc bằng `finish_reason: length`, không tạo tệp.
- Lượt thử lại giữ nguyên model và nguồn nhưng dùng briefing hẹp. Writer tạo `lecture-note.md`, sau đó kết thúc với `model exceeded the tool-call limit (8)` trong lúc đọc lại. Tệp đã ghi đầy đủ được giữ làm bản thảo; điều phối viên kiểm và sửa trước khi review.
- Reader, năm reviewer và recheck đều dùng `requested_model = observed_model = z-ai/glm-5.3-flash`, provider OpenRouter. Hồ sơ gửi ra ngoài đã lọc, không chứa `.env` hoặc thông tin xác thực.

### Năm báo cáo độc lập

| Vai rà | Phát hiện chính | Quyết định |
|---|---|---|
| Nguồn và phạm vi | Hai lỗi HITS ở bài 5.5.1; thiếu nhãn Ví dụ 5.11–5.12 và Hình 5.19–5.20 | Sửa vector tỷ lệ $(3,5,5,5)$, đỉnh thẩm quyền $B,C$; bổ sung nhãn và truy nguyên |
| Toán và thuật toán | Xác nhận các ma trận, công thức spam farm, TrustRank, spam mass và phần lớn vector; yêu cầu làm rõ $h_{\text{thô}}=La_{\text{mới}}$ | Áp dụng đầy đủ; tính lại độc lập bằng phân số |
| Mạch tự học | Thiếu tự kiểm cục bộ, giới hạn spam farm bị lẫn trong đại số, hình HITS dùng nhầm sơ đồ luồng spam | Thêm mục giới hạn và tự kiểm; chuyển hình luồng về phần spam; giữ SVG HITS đúng vai trò |
| Ngôn ngữ và ký hiệu | Bản thảo còn toán văn bản thô, dấu trừ Unicode, dấu phẩy thập phân mơ hồ, câu quy trình và thuật ngữ không nhất quán | Viết lại ba cụm `exercise`/`hint`/`solution`; dùng KaTeX, dấu chấm phẩy cho vector thập phân; cắt nội dung quy trình; thống nhất thuật ngữ |
| Viewer và khả năng tiếp cận | Cặp directive đúng; cảnh báo bảng rộng và ma trận; phát hiện đúng toán chưa bọc và alt lệch. Cảnh báo thiếu HTML/SVG do dossier hẹp | Sửa toán và alt; bác cảnh báo thiếu tài sản sau khi kiểm trực tiếp kho chính; giữ bảng để kiểm thực tế ở khung hẹp/in |

### Biên tập cuối

- `$no-ai-slop`: cắt lời dẫn rỗng, câu nhấn kiểu “điều cốt lõi/điều quan trọng”, nội dung quy trình, đoạn tự kiểm dành cho writer và phần kết luận lặp; giữ các số, giả thiết và chi tiết nguồn. Tự kiểm theo `no-ai-slop/eval.md` đạt: không thêm mệnh đề, không còn từ cấm hoặc mẫu câu máy móc được liệt kê.
- `$quill`: dùng quy trình revise/outline để rà mạch Bài 03 → PageRank theo chủ đề → cụm thao túng → TrustRank/khối lượng rác → HITS → so sánh → bài tập; thuật ngữ và ký hiệu được truyền liên tục. Không khởi tạo `quill.json`.
- Tính lại độc lập bằng phân số xác nhận hai vòng HITS Hình 5.18, ba nghiệm bài tập, tổng các phân phối và bốn tỷ số khối lượng rác.
- Recheck GLM trên bản mới nhất trả `GO`: không còn lỗi chặn hoặc nghiêm trọng. Ba góp ý thẩm mỹ được xử lý hai mục về dấu câu và cách dùng “tách ... khỏi ...”; dấu chấm phẩy trong vector thập phân được giữ để phân biệt dấu phẩy thập phân tiếng Việt.
- Không thay đổi ký hiệu, giả thiết, ví dụ, kết luận hoặc thứ tự dùng chung so với deck; không cần sửa deck. Các làm chặt của học phần vẫn khớp deck và được ghi rõ trong ghi chú.

## Kiểm định viewer và phát hành index

- Máy chủ cục bộ tương thích chạy tại `127.0.0.1:8765`; Chromium headless dùng viewport thật $1280\times720$ và $390\times844$.
- Lượt đầu phát hiện bảng so sánh năm cột làm tài liệu tràn ngang 63 px ở khung hẹp. Bảng được tách thành hai bảng ba cột, giữ đủ bốn mô hình và năm tiêu chí.
- Lượt cuối đạt ở cả hai khung: 41 heading và 41 liên kết mục lục; 380 biểu thức KaTeX, 0 lỗi; 5 SVG, 0 ảnh hỏng; 6 khối `hint`/`solution` đóng mặc định; không lỗi console, lỗi trang hoặc request; không tràn ngang.
- Bàn phím: liên kết bỏ qua điều hướng nhận focus và hoạt động; phím Enter mở được khối gập đầu tiên.
- Bản in: mọi khối gập mở, mục lục và nhóm hành động bị ẩn. PDF A4 có 19 trang; kiểm tra văn bản xác nhận đủ Gợi ý/Lời giải của ba bài và kiểm ảnh hai trang đầu không có cắt/chồng.
- An toàn: viewer từ chối đường dẫn traversal và từ chối cặp `doc`/`deck` khác số bài.
- Sau khi các cổng trên đạt, mới thêm đúng một liên kết ghi chú Bài 04 vào `2627-1/index.html`. Chromium nhấp từ index, tải đúng tiêu đề, `doc` và `deck`, không có lỗi runtime.

## Kiểm định cuối (lượt trước — lịch sử, chưa được phê duyệt cho lượt này)

- Kiểm tra tĩnh: 39 `data-slide-id` duy nhất, 39 khối ghi chú, thứ tự ID khớp storyboard; phần giảng 120 phút và bài tập 60 phút.
- Kiểm tra tài nguyên: mọi đường dẫn cục bộ tồn tại; 6 SVG phân tích được bằng XML và có `role="img"`, `title`, `desc`; không có ảnh raster hoặc tài nguyên cốt lõi từ mạng.
- Kiểm tra trình duyệt: Chromium headless duyệt đủ 39 trang ở khung $1280\times720$ và $800\times600$; không có lỗi console, lỗi trang, yêu cầu hỏng hoặc phần tử tràn khung. Hai bảng liên hệ, giả mã HITS và bốn trang bài tập được kiểm tra lại trên ảnh chụp.
- Lệnh bắt buộc `python3 -m reloadserver 8765` không chạy vì môi trường không cài mô-đun `reloadserver`. Máy chủ HTTP cục bộ đã có ở `127.0.0.1:8765`; trang Bài 4 trả HTTP 200 và được dùng cho toàn bộ kiểm tra trình duyệt.
- Codex Slides: dự án bền vững `20260827161616-b-i-4-pagerank-theo-ch-spam-li-n-k-t-v-h-urwd` vẫn ở checkpoint `clarify`, có đủ nguồn MMDS, Stanford, giáo trình, mẫu và CSS. Outline cuối cùng cùng storyboard/nhật ký đã được ghi và đọc lại thành công trong Design Files. Công cụ tải Design File mới trả HTTP 500, nên HTML và SVG cuối không được sao chép vào dự án; Browser trong trình biên tập không khả dụng trên bề mặt hiện tại. Vì vậy không tuyên bố đã kiểm tra trực quan bằng Codex Slides; kiểm tra trực quan cuối dùng RevealJS cục bộ và ảnh chụp Chromium.
- Chỉ sau các kiểm tra trên mới thêm thẻ Bài 4 vào `2627-1/index.html`; chỉ mục không liên kết tới tệp quy trình.

## Chu kỳ đồng bộ bộ trang chiếu với ghi chú — 2026-09-02

### Điều phối và soạn

- Reader kế hoạch phiên `59340` và reader nguồn phiên `28513` dùng `z-ai/glm-5.3-flash` qua OpenRouter. Hai reader giữ nguyên MMDS mục 5.3–5.5, 41 trang, 7 mạch, ba bài tập và mọi công thức; chỉ đề xuất dọn văn phong, thống nhất ký hiệu và sửa nhãn index.
- Writer hợp lệ dùng `deepseek/deepseek-v4-flash-0731` qua OpenRouter trên hồ sơ tạm chỉ gồm sáu đoạn notes. Metadata runtime xác nhận requested model trùng observed model và provider OpenRouter. Lượt writer trên toàn HTML hết thời hạn 300 giây và bị loại; không có thay đổi nào từ lượt lỗi được nhập vào kho.
- Codex chính chỉ áp dụng các sửa đã được phê duyệt, không đổi nguồn hoặc phạm vi. Không gửi `.env`, khóa, token, mật khẩu, cookie, khóa riêng hoặc thông tin xác thực tới worker.

### Năm báo cáo độc lập

| Vai | Phiên hợp lệ | Kết quả và quyết định |
|---|---:|---|
| Trung thành nguồn và phạm vi | `6374` | PASS; đúng MMDS §5.3–5.5, nhãn hình/ví dụ và ba bài tập; các phần làm chặt được phân biệt với nguồn. |
| Toán và giải thuật | `70845` | PASS; PageRank theo chủ đề, spam farm, TrustRank, khối lượng rác, HITS, đáp án và độ phức tạp đều đúng. |
| Học thuật và sư phạm | `68572` | Phát hiện tổng hàng thời lượng là 122 phút và chỉ số vòng `t/u`; đã giảm T00, Z03 mỗi trang 1 phút và thống nhất chỉ số `u`. |
| Văn phong, no-ai-slop và Quill | `88073` | PASS có sửa nhẹ; bỏ nhịp nhấn máy móc, sửa chú thích Hình 5.18, tiêu đề T06/K04 và nguồn S04. |
| Kỹ thuật tĩnh | `81479` | PASS; 41 ID duy nhất, 41 notes, 7 mạch, thư viện cục bộ, viewer/index/planning và 6 SVG đạt. |

Các lượt reviewer hết thời hạn, chạm giới hạn công cụ hoặc hết ngân sách phản hồi không được dùng làm bằng chứng. Thứ tự ID HITS phi tuần tự được giữ vì ID là mã nội bộ đã ổn định, vẫn duy nhất và không làm thay đổi thứ tự hiển thị.

### Sửa đã chấp nhận và tái kiểm

- Bỏ tên `sources/source.md`, câu nối kiểu quy trình và siêu bình luận khỏi notes; giữ nguồn học thuật ở dạng tự nhiên. Đổi câu chuyển ý `La^{(2)}` trong ghi chú thành phát biểu trực tiếp.
- Thống nhất phép lặp PageRank theo chủ đề dùng chỉ số vòng `u` trong deck, note và outline. Storyboard hiện cộng đúng 120 phút giảng; recitation giữ 60 phút.
- Làm rõ nguồn MMDS §5.4.2 cho S04, sửa alt Hình 5.18 thành mô tả đồ thị, đổi “Bảng tính” thành “Bảng số liệu” và thu gọn hai hộp nhiệm vụ R01/R04 mà không đổi yêu cầu toán học.
- Đổi nhãn tài nguyên Bài 04 trên index thành “Ghi chú bài giảng”; URL `doc`/`deck` không đổi.
- Tái kiểm mạch/no-ai-slop/Quill phiên `20423`: PASS; 120+60, văn phong, ký hiệu và tính liên tục deck–note đều đạt; không tạo `quill.json`.
- Tái kiểm toán độc lập phiên `58341`: PASS; xác nhận bản exact disk về chỉ số, S04, các mô hình, ba đáp án, chi phí và caption đều đúng.
- Các lượt tái kiểm dùng requested model và observed model `z-ai/glm-5.3-flash`, provider OpenRouter.

### Kiểm định cuối

- Kiểm tĩnh: 41 `data-slide-id` duy nhất, 41 notes, 7 outer section cân bằng; 6 SVG đọc được, đều có `role="img"`, `title`, `desc`; không có ảnh raster; `git diff --check` đạt.
- Chromium duyệt đủ 41 trang ở $1280\times720$, $800\times600$ và $720\times900$: không tràn, không lỗi console/page/request. Bàn phím chuyển ngang/dọc đúng; 41 notes; 0 lỗi KaTeX. Hai hộp R01/R04 được xem trực quan sau sửa. PDF deck có 41 trang A4.
- Viewer ở $1280\times720$ và $390\times844$: 41 heading, 29 liên kết mục lục, 380 phần tử KaTeX và 0 lỗi; 5 ảnh tải đủ; 6 khối gập đóng mặc định, mở được bằng bàn phím và mở khi in; không tràn ngang hay lỗi runtime. PDF viewer có 19 trang A4. Hai phép thử vượt thư mục và lệch số bài đều bị từ chối.
- Index có đúng một URL ghi chú Bài 04 và mở đúng `doc`/`deck`, không lỗi console.
- Codex Slides project `20260827161616-b-i-4-pagerank-theo-ch-spam-li-n-k-t-v-h-urwd` đọc được bằng CLI, giữ đủ bảy nguồn/tài sản. Project vẫn ở trạng thái `draft`, workflow `clarify`, `pages=[]`, `outline=[]`; không có Browser callable nên không tuyên bố đã kiểm trực quan trong Codex Slides. Kiểm định trực quan dùng Chromium trên đúng HTML phát hành.

Kết luận: không còn lỗi chặn, nghiêm trọng hoặc trung bình; bộ trang chiếu, ghi chú, planning, viewer và index Bài 04 đồng bộ và đủ điều kiện commit/push.
