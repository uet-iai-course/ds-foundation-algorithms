# Nhật ký rà soát Bài 10

## Trạng thái bản nháp

- Tạo 48 trang: 44 trang phần giảng và 4 trang recitation.
- Phân bổ 120 phút giảng và 60 phút recitation; ngoại lệ nguồn cho ba bài đã được người dùng phê duyệt ngày 2026-08-28.
- Tạo 9 SVG cục bộ; không dùng ảnh raster hay tài nguyên mạng cốt lõi.
- Chưa cập nhật `2627-1/index.html`; tệp này nằm ngoài phạm vi lượt QA hiện tại.

## Quyết định nguồn

- Nelson–Gailly Chương 3–5 là nguồn trục về ví dụ, biến thể và thuật toán.
- Stanford EE398A và CS106B chỉ hỗ trợ cách trình bày trực quan; không thay dữ liệu A–E của sách bằng ví dụ chín ký hiệu.
- CMU hỗ trợ liên hệ mô hình–bộ mã hóa, Kraft và bài tập mã hóa số học.
- MMDS không bao phủ Huffman hoặc mã hóa số học, nên không dùng cho Bài 10.

## Sai khác có chủ ý và sửa lỗi nguồn

- Không dùng Hình 4.1 ở Nelson–Gailly PDF tr.69 vì hình và mô tả trọng số không khớp. Dùng Hình 4.2–4.3, PDF tr.70–71, để trình bày tăng và đổi nút.
- Bảng giải mã “BILL GATES” in A ở khoảng sai trong bản PDF. Deck dùng đúng bảng mô hình ở PDF tr.97: A thuộc $[0{,}1;0{,}2)$.
- Không gắn tên NYT, FGK hoặc Vitter cho biến thể thích nghi. Deck giữ `ESCAPE`, `EOS` và quy tắc cập nhật của Nelson–Gailly.
- Phần chuẩn hóa hữu hạn dùng ba trường hợp E1/E2/E3 theo slide Stanford để tránh sa vào mã C 16 bit của sách. Bản sửa dùng nhất quán khoảng nửa mở: E1 với $H\le1/2$, E2 với $L\ge1/2$, E3 với $1/4\le L&lt;H\le3/4$.
- Tình huống mã số học dùng trực tiếp phép thử trong Nelson–Gailly Ch.5: 100.000 số 0, $p(0)=16382/16383$, tệp mã số học dài 3 byte và cận tối thiểu Huffman là 12.501 byte.

## Bài tập và ngoại lệ nguồn đã phê duyệt

- X01, 20 phút: ví dụ Huffman A–E ở Nelson–Gailly Ch.3, PDF tr.35–37, được chuyển thành bài luyện.
- X02, 15 phút: ví dụ ở Hình 4.2–4.3, Nelson–Gailly Ch.4, PDF tr.70–71, được chuyển thành bài luyện.
- X03, 25 phút: CMU 15-499 Assignment 1a, Problem 3, tr.1; đáp án đối chiếu solution tr.2–3.
- Người dùng phê duyệt rõ ngoại lệ nguồn cho X01–X03 ngày 2026-08-28. Tổng thời lượng giữ nguyên $20+15+25=60$ phút. Lỗi chặn nguồn đã đóng; không còn lỗi chặn hoặc nghiêm trọng.

## Rà ngôn ngữ và mạch

- Áp dụng `no-ai-slop`: bỏ câu hỏi tu từ, lời dẫn rỗng, nhấn mạnh quảng bá và tổng kết lặp; giữ câu ngắn, động từ rõ.
- Áp dụng `quill` ở chế độ rà mạch, không tạo `quill.json`: thứ tự đi từ mô hình chung đến mã nguyên bit, cập nhật mô hình trực tuyến, rồi mã khoảng; ký hiệu $[L,H)$ được giữ xuyên suốt phần số học.

## Hợp nhất bốn báo cáo độc lập và kiểm định storyboard

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| chặn bàn giao | X01–X03 | Cần phê duyệt loại nguồn bài luyện | X01–X02 chuyển ví dụ Nelson–Gailly thành bài luyện; X03 thuộc CMU Assignment 1a | Xin người dùng phê duyệt ngoại lệ nguồn | Đã đóng ngày 2026-08-28: người dùng phê duyệt rõ ngoại lệ |
| nghiêm trọng | H07, H11, A05, R02 | Một số công thức ở phần tử `.math` thiếu dấu phân cách KaTeX | HTML chứa văn bản TeX thô | Bọc toàn bộ công thức bằng `$...$` | Đã sửa |
| nghiêm trọng | H03 | Cây Kraft vẽ nhánh con dưới lá mã `10` | SVG cũ nối nút `10` với hai nút sâu hơn | Vẽ lại cây dừng ở bốn lá và tách tám ô sức chứa | Đã sửa SVG |
| nghiêm trọng | R04, R11 | Hình khoảng không theo tỷ lệ; E1/E2/E3 trộn quy ước biên | Các hình cũ dùng hình chữ nhật tùy ý và điều kiện $H<1/2$, $H<3/4$ trong khi deck dùng $[L,H)$ | Vẽ từng mức phóng đại theo tỷ lệ; ghi rõ khoảng cuối dưới độ phân giải; dùng điều kiện và phép biến đổi nửa mở nhất quán | Đã sửa SVG và ghi chú |
| nghiêm trọng | A02, A07–A08 | Thiếu vết ký hiệu mới và giả mã có thể quét/đổi không an toàn ở gốc | Bản nháp chỉ nói phát `ESCAPE`; vòng lặp dùng “không vượt qua gốc” nhưng không dừng trước bước tìm khối | Thêm bốn bước `ESCAPE` + 8 bit + lá 0 + cập nhật; dừng ngay sau tăng gốc; loại tổ tiên khỏi ứng viên đổi; thêm bất biến nhánh mới | Đã sửa |
| nghiêm trọng | R08, X03 | Thiếu tự thông tin và cầu nối để giải thích chuỗi CMU dài hơn entropy trung bình | X03 hỏi về độ dài nhưng phần giảng chưa phân biệt $I(x)$ và $H(P)$ | Thay trang erratum bằng công thức tự thông tin/entropy; chuyển erratum vào ghi chú và nhật ký | Đã sửa |
| nghiêm trọng | P02, R12, S00–S01 | Trộn mô hình tĩnh/thích nghi với bộ mã Huffman/số học trên một trục | Bảng cũ liệt kê “Huffman tĩnh, Huffman thích nghi, số học” như ba bộ mã độc lập | Dùng ma trận hai trục và câu hỏi gán cặp | Đã sửa |
| nghiêm trọng | A00, A09, S00 | Hàm ý Huffman thích nghi tự xử lý drift | Trọng số cơ bản cộng dồn toàn lịch sử; không có forgetting | Đổi tình huống thành chưa biết bảng trước; nói rõ giảm trọng số/cửa sổ quên là cơ chế khác | Đã sửa |
| nghiêm trọng | H11 | Chứng minh tham lam thiếu phép đổi định lượng và cấu trúc con tối ưu | Ba gạch đầu dòng chưa chỉ ra vì sao chi phí không tăng | Nêu cặp lá anh em sâu nhất, $\Delta\le0$, phép co và phản chứng | Đã sửa |
| trung bình | R00 | Tình huống dữ liệu lớn chưa có quy mô | Bản nháp dùng bảy A, không phải dữ liệu lớn | Dùng phép thử 100.000 số 0 và kết quả từ Chương 5 | Đã sửa |
| trung bình | toàn deck | Chữ bảng, mã và chú thích nhỏ | `.trace=.78em`, `.code=.72em`, `.small=.72em` trên section `.8em` | Tăng section lên `.84em`; `.trace=.92em`, `.code=.9em`, `.small=.88em` | Đã sửa; cần kiểm tra tràn cuối |
| trung bình | S01 | Câu hỏi tổng hợp có nhiều đáp án “đều có thể” | Câu cũ hỏi thiếu mục nào gây lệch ngay | Cho ba tình huống và yêu cầu gán đúng cặp mô hình–bộ mã | Đã sửa |

Sau thay đổi mạch ở P02, A00–A09, R00–R12 và S00–S01, đã rà lại nội dung hai trang lân cận của từng cụm trong storyboard. Tổng thời lượng phần giảng không đổi: 120 phút. Số trang không đổi: 48, gồm 44 trang giảng và 4 trang recitation; ba bài tập giữ tổng 60 phút.

## Việc còn lại sau bản nháp

- Không còn lỗi chặn hoặc nghiêm trọng; tiếp tục kiểm định cuối theo quy trình chung.
- Chỉ sau kiểm định cuối mới cập nhật `index.html`, commit và push.

## Kiểm định sau chỉnh sửa

- Tác tử độ chính xác kiểm tra lại H11, A02, A07, A08, R11, chín SVG và các kết quả số: `PASS`; 41 biểu thức KaTeX phân tích được. Sau phê duyệt ngoại lệ nguồn ngày 2026-08-28, không còn lỗi chặn hoặc nghiêm trọng.
- Bộ phân tích HTML ghi nhận 48 `data-slide-id` duy nhất, 48 ghi chú diễn giả, không thiếu tệp hình hoặc văn bản thay thế; cả chín SVG là XML hợp lệ.
- QA ngày 2026-08-28 phát hiện chín SVG chưa có thuộc tính `aria-label` trực tiếp ở phần tử gốc. Đã thêm `role="img"` và nhãn tiếng Việt cụ thể cho từng hình, đồng thời giữ nguyên `title` và `desc`; lỗi metadata SVG đã đóng.
- Không có tham chiếu ảnh raster hoặc tài nguyên mạng cốt lõi.
- Lệnh bắt buộc `python3 -m reloadserver 8765` thất bại vì môi trường không có mô-đun `reloadserver`. Máy chủ HTTP cục bộ sẵn có trên cổng 8765 trả `200 OK` cho deck.
- Chromium không giao diện duyệt đủ 48 trang ở `1280 × 720` và `800 × 600`: không có lỗi console, lỗi tải tài nguyên hoặc trang tràn. Hai contact sheet đã được kiểm tra trực quan; không thấy chữ bị cắt, chồng lấn hoặc TeX thô.
- Dự án Codex Slides: `20260827223939-b-i-10-n-n-d-li-u-kh-ng-m-t-th-ng-tin-oh97`. Sáu PDF nguồn đã được gắn. Upload Design File trả HTTP 500; chế độ dự phòng đã ghi và đọc lại thành công `generated/outline.md` cùng `generated/brief.md`. Phiên này không có Browser tích hợp để đối chiếu trực tiếp canvas Codex Slides, nên không tuyên bố đã rà trực quan bằng Browser.
