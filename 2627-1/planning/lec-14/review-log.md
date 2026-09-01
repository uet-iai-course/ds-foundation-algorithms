# Nhật ký rà soát Bài 14

## Trạng thái

- Bản sửa sau kiểm định storyboard và năm báo cáo độc lập giữ 58 `data-slide-id`, 58 khối ghi chú, 120 phút giảng và 60 phút recitation.
- Bảy wrapper là `P`; `I`; `S+R`; `K`; `B`; `Z+C`; `X`.
- Chỉ đổi cục bộ thứ tự `I06→I08→I07` để hoàn tất NOT trước khi chuyển sang bố trí đĩa.
- HTML và ghi chú không hiển thị thời lượng. Không sửa CSS chung, index, bài khác hay cấu hình người dùng.
- Chưa commit. Tái kiểm toán, mạch và kiểm định RevealJS cục bộ đã hoàn tất; kết quả nằm ở cuối nhật ký.

## Đặc tả nguồn đã xác nhận

| Cụm | Nguồn | Quyết định |
|---|---|---|
| Chỉ mục đảo | *Database System Concepts* 7e, Ch31 trang 13–16, slide 14–16 | OR là hợp; giữ vị trí, tần suất, precision/recall; ví dụ số do deck dựng từ docID đã có |
| R-tree | Ch24 slide 17, 21–24; Auburn trang 10–13 | Lọc MBR tạo ứng viên, sau đó kiểm hình thật; chỉ nêu hệ quả cập nhật, không dạy chèn/tách |
| kd-tree và ball tree | Cornell CS5780 trang 1–5 | Giữ cơ chế; vết kd/ball và cận dựng là phần deck dựng, được ghi rõ |
| Z-order | Auburn trang 12–13, slide 23–26 | Giữ hiệu chỉnh Morton 6/7; Z04 dẫn slide 26; so sánh đoạn chính xác/gộp từ cùng tập mã |
| Bài 31.2 | Ch31 7e, trang in 25 | Lời giải đống do deck triển khai từ đề; không lộ trước X03 |
| Bài 25.2–25.3 | Ch25 6e, Practice Exercises/Solutions trang 1–2 | Giữ lời giải nguồn; phân biệt tên B-tree của nguồn với B+-Tree triển khai |

## Kiểm định storyboard mới

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| chặn bàn giao | toàn bài | Wrapper chưa khớp bảy mạch chức năng | kd và ball tranh một mạch; Z và tổng hợp bị tách dù C thu hồi Z | Dùng `P|I|S+R|K|B|Z+C|X`; ghi chức năng và kết nối vào–ra |
| nghiêm trọng | B04–B06 | Chu trình dựng ball thiếu ví dụ chạy tay | Chưa có trạng thái $x_0,x_1,x_2,z,S_L,S_R,c,r$; lá chưa tạo ball | Đổi B04 thành vết số; B05 tạo $(c,r)$ trước trường hợp lá; B06 dùng lại cùng trạng thái |
| nghiêm trọng | X03 | Lời giải đống chưa phải giả mã thực thi được | Thiếu điều kiện vòng lặp, mã danh sách, tiến và tái chèn | Viết đủ hai vòng `while`, hậu điều kiện, bất biến và chi phí |
| nghiêm trọng | I06–I08 | NOT chưa có vết hoàn chỉnh trước bố trí đĩa | Chỉ có ký hiệu $S\setminus P_t$; I07 ngắt thuật toán | Dùng docID I02, đổi thứ tự I06→I08→I07 và ghi pipeline B12–B14 |
| trung bình | I09–I12, C00–C02 | Precision/recall đứng ngoài tuyến chính | Không có một cặp $R,G$ nhất quán để tính cả hai | Dùng $G,R_h,R_l$ xuyên bốn trang; thu hồi ở C00–C02 |
| trung bình | Z03–Z04 | “Nhiều đoạn” chưa cho thấy đánh đổi và tinh lọc | Không có dương tính giả cụ thể | So sánh bốn đoạn đơn với $[4,13]$, chỉ ra mã 5 bị loại |
| trung bình | K06, B02 | Ví dụ đi thẳng vào số LB | Thiếu cầu trực giác trước công thức | Nêu khoảng cách tới miền và “tới tâm trừ bán kính” trước hình thức hóa |

Quyết định: áp dụng toàn bộ. B04, B05 và X03 giữ cỡ chữ chuẩn bằng cách chuyển chứng minh dài và nguồn vào ghi chú, không thêm trang.

## Báo cáo độc lập: góc nhìn sinh viên

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | B04–B06 | Khó tự chạy phép dựng ball tree | Chưa có tập điểm nhỏ hay trạng thái trung gian | Thêm vết bốn điểm và bảng ball cha/hai lá |
| trung bình | I06–I08 | Mạch NOT bị ngắt bởi trang bố trí đĩa | Người học chưa thấy đáp án và điều kiện dừng | Đặt I08 ngay sau I06; I07 sau thuật toán |
| trung bình | I09–I12 | Công thức chất lượng thiếu dữ liệu để tính | $R$ và $G$ chỉ được định nghĩa trừu tượng | Dùng một ví dụ ngưỡng chặt/nới xuyên cụm |
| nhẹ | K01, B07 | Trang có nguy cơ dày chữ | Chi tiết phá hòa và giả thiết cận cùng nằm trên mặt slide | Chuyển phá hòa K01 vào notes; giữ giả thiết B07 ở cỡ thân bài |

Quyết định: áp dụng toàn bộ; không hạ cỡ chữ dưới chuẩn.

## Báo cáo độc lập: chuyên gia giải thuật và khoa học dữ liệu

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | B04–B07 | Phạm vi Euclid và metric chưa đủ rạch ròi | Dựng dùng trung bình/phép chiếu nhưng truy vấn nói metric tổng quát | Giới hạn dựng ở $S\subseteq\mathbb R^p$; yêu cầu ball chứa cây con theo cùng metric truy vấn |
| nghiêm trọng | X03 | Trạng thái đống thiếu mã danh sách | Không thể biết con trỏ nào phải tiến | Lưu `(docID,mã danh sách)` và tái chèn đầu mới |
| trung bình | C00 | So sánh lẫn đơn vị RAM và I/O | kd/ball dùng phép đo; R/Z/inverted dùng trang | Chốt mô hình chi phí; không so trực tiếp |
| trung bình | R03, C01 | Tải cập nhật bị bỏ khỏi quyết định chọn chỉ mục | MBR có thể nở và tăng chồng lấn | Nêu hệ quả cập nhật, không mở rộng sang thuật toán tách |

Quyết định: áp dụng toàn bộ; không thêm cận I/O ngoài nguồn.

## Báo cáo độc lập: độ chính xác toán học và thuật toán

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | B05–B06 | Lá không có tâm và bán kính | Giả mã cũ trả `lá(S)` trước khi tính $(c,r)$ | Tính $(c,r)$ trước nhánh cơ sở; vết xác nhận hai lá chứa điểm |
| nghiêm trọng | X03 | Chưa đủ điều kiện dừng và hậu điều kiện | Lệnh “lặp” không có điều kiện; không chỉ ra mỗi docID xuất một lần | Dùng `while H không rỗng`, gom hết đầu bằng $x$, nêu hậu điều kiện |
| trung bình | K05 | Điểm hỏi trên biên chưa có quy ước near | “near chứa q” có thể không duy nhất | Dùng thứ tự con cố định; far vẫn xét khi $LB\le\tau$ |
| trung bình | B07 | Cận dựng có thể bị hiểu là vô điều kiện | Cần cây cân bằng, sắp lại mỗi nút và chi phí $O(p)$ | Đưa đủ giả thiết ra mặt slide; ghi đây là suy ra của deck |
| trung bình | X08 | Thiếu đơn vị chi phí sau chứng minh | Chỉ có tính đúng | Thêm $j+1$ truy vấn vùng và $O(p|A|)$ số học khi tinh lọc Euclid |

Quyết định: áp dụng toàn bộ và chuyển B04–B07, K05, X03, X08 sang tái kiểm toán; kết quả cuối đạt sau khi làm rõ bộ nhớ X03.

## Báo cáo độc lập: phản biện học thuật và giảng dạy

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | B04–B06 | Hình thức hóa dựng xuất hiện trước ví dụ số kiểm được | Hình minh họa không truyền dữ kiện sang giả mã | Dùng B04 làm vết, B05 tổng quát hóa, B06 kiểm ball ở lá |
| trung bình | K06→K04, B02→B01 | Chu trình trực giác–hình thức chưa được phát tín hiệu | Bảng số dùng LB trước khi người học có cách đọc hình học | Thêm câu trực giác, giữ công thức ở trang sau |
| trung bình | I09–I12 | Precision dễ bị lẫn với “1-NN chính xác” | Cùng từ “độ chính xác” nhưng hai vai trò khác | Notes phân biệt precision với tính đúng exact 1-NN |
| trung bình | Z03–Z04 | Tinh lọc được nêu nhưng chưa được thực hiện | Không có ứng viên sai cụ thể | Cho mã 5 trong đoạn gộp và loại bằng tọa độ |

Quyết định: áp dụng toàn bộ.

## Báo cáo độc lập: kết nối và mạch viết

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| chặn bàn giao | ranh giới wrapper | Bảy wrapper chưa khớp bảy mạch | Vai trò: K và B cần hai chu trình; Z+C cùng thu hồi truy vấn vùng. Kết nối vào/ra bị mờ | Tách K/B, gộp Z/C; cập nhật outline và storyboard |
| nghiêm trọng | K09→B00 | Chuyển cấu trúc nhưng chưa nói rõ đặc tả được giữ | Vai trò K09 khép hòa; kết nối ra B00 thiếu “cùng 1-NN” | Nêu ball tree giữ đặc tả 1-NN và thay hộp bằng ball |
| nghiêm trọng | B07→Z00 | Nhảy từ 1-NN sang Z-order | Vai trò B07 khép cây metric; kết nối ra cần trở lại truy vấn vùng và B+-Tree Bài 13 | Thêm câu nối rõ trong notes và storyboard |
| trung bình | C00–C02 | Kết luận chưa thu hồi hai tình huống và chất lượng truy hồi | Vai trò tổng hợp; kết nối vào từ Z, kết nối ra bài tập | Gọi lại kho web, ảnh vệ tinh/trạm xăng, precision/recall và mô hình chi phí |

Quyết định: áp dụng toàn bộ. Do đổi wrapper và thứ tự I06–I08–I07, các trang lân cận và mọi ranh giới phần đã được tái kiểm; kết quả mạch viết đạt.

## Quyết định chỉnh sửa hợp nhất

- Áp dụng mọi lỗi `chặn bàn giao`, `nghiêm trọng` và lỗi `trung bình` ảnh hưởng tính đúng hoặc mạch.
- Không thêm slide riêng cho từng phép tính precision/recall hoặc chi phí X08: 58 ID là ràng buộc; chi tiết vừa trong notes.
- Không xóa `ball-build.svg` hoặc `kofn-heap.svg` dù HTML không dùng: đây là tài sản có trước; lượt sửa không thực hiện thao tác hủy.
- Không sửa CSS chung, index, bài khác hoặc cấu hình người dùng.

## Tự kiểm biên tập và tính liên tục

- `no-ai-slop/eval.md`: đạt. Câu hiển thị đi thẳng vào dữ kiện hoặc thao tác; không thêm khẩu hiệu, câu hỏi tu từ, số liệu hay nhận định ngoài nguồn. Các lời mời tương tác giữ nhãn **“Câu hỏi:”**.
- Quill continuity: đạt ở mức rà dàn ý. Tuyến là tình huống → ví dụ → hình thức → thuật toán/tính đúng → chi phí → kiểm tra; thuật ngữ `danh sách đảo`, `metric`, `Euclid`, $LB$, $\tau$, $R$, $G$ nhất quán. Không tạo `quill.json`.

## Tái kiểm sau chỉnh sửa

| vai rà soát | kết quả | phạm vi | bằng chứng và quyết định |
|---|---|---|---|
| Kết nối và mạch viết | đạt | Bảy wrapper, các ranh giới phần và hai trang lân cận | Tuyến `P|I|S+R|K|B|Z+C|X` liên tục; K09→B00 giữ đặc tả 1-NN, B07→Z00 khép 1-NN rồi trở lại truy vấn vùng; không cần đổi cấu trúc hoặc thứ tự |
| Toán học và thuật toán | sửa một lỗi trung bình tại X03 | Phân tích bộ nhớ của thuật toán đống | Ký hiệu $A$ lưu toàn bộ đầu ra nên câu “bộ nhớ $O(n)$” mơ hồ; sửa thành $O(n)$ bộ nhớ phụ không tính đầu ra, tương đương tổng $O(n+|A|)$ |

## QA trực quan sau tái kiểm

| mức độ | trang chiếu | vấn đề | bằng chứng | quyết định |
|---|---|---|---|---|
| chặn bàn giao | Z03 | Phần dưới của hai thẻ bị cắt ở khung $1280\times720$ | Rà ảnh chụp trực quan phát hiện lỗi dù kiểm tra hình học tự động không báo tràn | Rút tiêu đề thành “Đoạn chính xác và đoạn gộp”; thêm lớp cục bộ `.z-interval-figure` với `max-height: 300px`; giữ nguyên nội dung, ID, cỡ chữ thân bài và mạch |

Hai lần sửa bằng selector `.z-interval-figure` ở 300 px rồi 240 px đều chưa áp dụng vào kích thước tính toán: selector của Reveal giữ `max-height: 95%` do có độ đặc hiệu cao hơn. Đổi selector cục bộ thành `.reveal img.z-interval-figure{display:block;margin:.12em auto;max-height:240px}` để mức 240 px có hiệu lực và hình vẫn căn giữa khi Reveal ghi đè lề. Tái kiểm cuối đạt: `max-height` tính toán là 240 px; đáy thẻ ở 596 px, trước chân trang ở 690 px tại $1280\times720$; nội dung, ID và mạch không đổi.

## Kiểm định cuối

- Lệnh bắt buộc `python3 -m reloadserver 8765` thất bại vì môi trường không có mô-đun `reloadserver`. Máy chủ dự phòng `/tmp/reloadserver.py 8765` gặp `address already in use`; tiến trình ngoài phạm vi đang giữ cổng 8765 được giữ nguyên. QA dùng máy chủ dự phòng ở cổng 8766.
- Chromium QA sau khi sửa độ đặc hiệu selector: cả $1280\times720$ và $800\times600$ đều có 58 trang, `errors=[]`, `problems=[]`, không có lỗi KaTeX hoặc tràn. Contact sheet toàn bộ và các trang B04, B05, C00, X03, Z03, Z04 đã được rà trực quan; Z03 đạt ở lần cuối.
- DOM có đúng bảy stack: `P`; `I`; `S+R`; `K`; `B`; `Z+C`; `X`. Điều hướng bàn phím `P00→I00→I01` đạt.
- HTML dùng 11 SVG, tất cả được kiểm tra; hai tài sản mồ côi `ball-build.svg` và `kofn-heap.svg` được giữ và đã ghi nhận, không tham chiếu trong HTML.
- Dự án Codex Slides `20260830170505-b-i-14-ch-m-c-v-n-b-n-v-ch-m-c-kh-ng-gia-qpmz` vẫn ở trạng thái `draft` với 0 slide. Bản HTML mới nhất đã tải lên dưới mã vật liệu `20260830175122234-2rgp.html`. Browser nội bộ không khả dụng, nên không tuyên bố đã rà trực quan bằng Codex Slides.
- Điều phối viên chạy kiểm tra tĩnh và diff cuối ngay trước khi commit; cấu trúc không thay đổi sau khi mạch viết đạt.

## Quy trình ghi chú tự học

- Ba reader OpenRouter `z-ai/glm-5.3-flash`: kế hoạch phiên `79940`, nguồn `81734`, bản đồ chủ đề `12041`. Codex chính mở trực tiếp các PDF/PPTX mà reader văn bản không đọc được, hợp nhất 12 chủ đề và tách truy vấn ball metric khỏi phép dựng Euclid.
- Writer `deepseek/deepseek-v4-flash-0731` phiên `23162` tạo bản nháp trong gốc tạm hẹp rồi chạm giới hạn công cụ sau khi ghi xong. Codex chính kiểm toàn vẹn, đưa bản nháp vào kho và sửa một đoạn lỗi mã hóa trước khi rà soát.
- Năm vai reviewer GLM: nguồn phiên đầu `56788` hết vòng, chạy lại hẹp `87247`; toán–thuật toán `63063`; sư phạm phiên đầu `3373` hết vòng, chạy lại hẹp `54155`; mạch `10660`; viewer phiên đầu `7354` hết vòng, chạy lại hẹp `4796`. Mọi kết quả được chấp nhận đều có metadata đúng model và provider.

### Quyết định sau rà soát ghi chú

- Sửa mã Morton 5 từ tọa độ sai $(2,1)$ thành $(1,3)$; sửa bài tự kiểm vùng góc để hỏi có dương tính giả hay không.
- Sửa điều kiện dừng của vết NOT: sau $6=6$, cả hai con trỏ cùng cạn.
- Đổi tập điểm dựng ball từ $S$ sang $\mathcal X$ để không trùng tập nền của NOT; phát biểu $LB$ là điều kiện hợp lệ thay vì một định nghĩa duy nhất.
- Ghi rõ vết và giả mã kd-tree/ball tree do bài giảng triển khai từ Cornell; ghi rõ $O(p|A|)$ của Bài 25.3 là suy ra của bài giảng.
- Thay bài tự kiểm 25.3 thoái hóa bằng yêu cầu giải thích dãy bán kính, vùng đóng và tinh lọc, giữ đúng dữ kiện tổng quát của bài nguồn.
- Điều kiện hóa ảnh hưởng của vị trí–tần suất lên số trang; chuẩn hóa `kd-tree / ball tree`, ký hiệu $q$, câu dẫn và kết luận.
- Không áp dụng nhận xét viewer về việc đổi đường dẫn hình: viewer giải URL hình theo trang `material-viewer.html`, nên `img/lec-14/...` là dạng đúng. Giữ liên kết deck tương đối theo cùng cơ chế và kiểm bằng Chromium.

### Tái kiểm

- Toán–thuật toán phiên `58293`: `PASS`; mọi vết số, giả mã, dấu cắt, Morton, chi phí và điều kiện dừng đúng.
- Mạch viết phiên `83256`: `PASS`; không còn lỗi chặn, nghiêm trọng hoặc trung bình. Sửa thêm lỗi từ “chèn” trong mô tả dương tính giả bằng phát biểu chính xác về MBR và hình thật.
- `$no-ai-slop`: cắt câu kết dạng câu hỏi, bỏ lời dẫn rỗng, sửa câu gãy và nhịp liệt kê; giữ giọng học thuật trực tiếp.
- `$quill`: rà tuyến `N01→N12`, thuật ngữ, ký hiệu, câu nối và các điểm thu hồi; không tạo `quill.json`.

### Kiểm định viewer và index của ghi chú

- Chromium ở $1280\times720$ và $390\times844$: 28 heading khớp 28 mục TOC; 464 công thức KaTeX, 0 lỗi; 10 SVG, 0 hình hỏng; 24 khối gập đều đóng mặc định; 7 khối mã; không tràn ngang, lỗi console, lỗi trang hay request thất bại.
- Bàn phím: liên kết bỏ qua nội dung nhận focus; `Enter` mở khối gập. Bản in mở toàn bộ `hint/solution`, ẩn TOC và thanh hành động, không có hình vượt khổ; PDF A4 dài 29 trang.
- Đường dẫn `../AGENTS.md` và cặp doc/deck lệch số bài đều bị từ chối, phần nội dung bị ẩn.
- Liên kết Bài 14 trên index xuất hiện đúng một lần, nhận focus bằng bàn phím và mở đúng note/deck ở cả hai kích thước; không tràn ngang.
- Ghi chú dùng 10 SVG phục vụ trực tiếp lập luận. Ba SVG có trước nhưng không cần trong ghi chú (`ball-build.svg`, `kofn-heap.svg`, `posting-merge.svg`) được giữ nguyên; không thêm hoặc xóa tài sản.
- Kiểm tĩnh cuối: đúng một H1; 12 bộ `exercise/hint/solution`; 14 hàng rào mã; không có delimiter toán bị cấm, nhãn quy trình công khai, lỗi XML SVG hay `quill.json`.
