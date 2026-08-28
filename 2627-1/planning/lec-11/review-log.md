# Nhật ký rà soát Bài 11

## Trạng thái sau chỉnh sửa

- HTML: `2627-1/lecture-11-nen-bang-tu-dien-va-nen-mat-du-lieu.html`.
- 42 trang giảng, 120 phút; 6 trang bài tập, 60 phút.
- 12 SVG; không có ảnh raster hoặc tài nguyên mạng trong nội dung bài.
- Chưa cập nhật `2627-1/index.html`; tệp này nằm ngoài phạm vi lượt cập nhật hồ sơ hiện tại.

## Lựa chọn nguồn

- Nelson–Gailly Chương 8–11 là nguồn trục cho biến thể và cơ chế.
- CMU cung cấp vết LZ, câu hỏi recitation và mạch JPEG. MIT chỉ dùng để đối chiếu trực giác.
- MMDS và Stanford CS246 không có mô-đun tương ứng nên không áp dụng quy tắc ưu tiên MMDS.
- Không mang tệp nhị phân nguồn vào đầu ra Git.

## Hợp nhất báo cáo rà soát

| Mức độ ban đầu | Trang | Vấn đề | Quyết định và kết quả |
|---|---|---|---|
| chặn bàn giao | W02 | Vết LZW sai với chuỗi `ppqpprpqrpqrq` | Vẽ lại đầy đủ: mã phát `112,112,113,256,114,257,260,113,114,113`; mục mới 256=`pp`, 257=`pq`, 258=`qp`, 259=`ppr`, 260=`rp`, 261=`pqr`, 262=`rpq`, 263=`qr`, 264=`rq`. |
| nghiêm trọng | L02–L06 | Literal `(0,0,c)` mâu thuẫn với cận $d\ge1$; thiếu quy ước kết thúc | Tách literal và tham chiếu; đưa cận vào L03; chọn $EOS$ dành riêng; cập nhật giải mã và chứng minh. |
| nghiêm trọng | L03–L04 | Giả mã đứng trước vết | Đưa L04 trước L03; L02 chỉ cung cấp từ vựng. |
| nghiêm trọng | X02 | `position=2` không rõ gốc chỉ số và bị lẫn với khoảng lùi | Ghi rõ position tính từ 0, ký tự nguồn là `c`; ghi đây không phải khoảng lùi của phần giảng. |
| nghiêm trọng | Z01–Z04 | Thiếu vết chạy trước giả mã và chứng minh | Z02 chạy bốn cặp; Z03 mới hình thức hóa hai phía; Z06 dùng hai cặp còn lại. |
| nghiêm trọng | W00–W05 | Thiếu cầu nối LZ78→LZW; thuật toán đứng trước ví dụ; nhánh đặc biệt xuất hiện quá sớm | W00 giải thích bỏ ký tự khỏi cặp LZ78; W02 đứng trước W01; W03 chỉ đường thường, W04 tạo trực giác, W05 hợp nhất và chứng minh. |
| nghiêm trọng | X04 | Ký hiệu $S_c,c$ tự mâu thuẫn và không nối với bài giảng | Đổi thành cụm trước $w$, mã $k=\texttt{next\_code}$; giữ nguyên yêu cầu toán học của CMU. |
| nghiêm trọng | X01, X03 | Ghi chú thiếu đáp án cụ thể | Thêm token, mục từ và chuỗi khôi phục đầy đủ. |
| nghiêm trọng | J01, J04, J06 | Biểu thức không có dấu phân cách KaTeX; DCT thiếu miền và $\alpha$ | Bọc `$...$`; nêu miền chỉ số, $\alpha(0)=1/\sqrt8$, $\alpha(t)=1/2$; thêm công thức IDCT ở J09. |
| nghiêm trọng | J04–J05 | Công thức DCT đứng trước trực giác | Đưa J05 trước J04; ghi hình chỉ minh họa định tính. |
| nghiêm trọng | J02–J11 | Tuyên bố lượng tử là bước mất dữ liệu duy nhất dù có lấy mẫu sắc | SVG và nội dung phân biệt lấy mẫu sắc mất dữ liệu tùy chọn với lượng tử bắt buộc mất trong lõi hệ số. |
| nghiêm trọng | J08–J09 | Thiếu tách dòng DC/AC | Thêm DC sai phân; AC zigzag, RLE và mã entropy; nối lại mã entropy của Bài 10. |
| nghiêm trọng | L08, Z05, W06 | Thiếu mô hình chi phí nén | Nêu chi phí bit token/cặp/mã theo giả thiết định dạng; không tuyên bố tỷ lệ nén cố định. |
| nghiêm trọng | Z00, W00 | Tình huống dữ liệu lớn thiếu đầu ra và giới hạn | Bổ sung luồng một lượt, đầu ra, trạng thái tăng và giới hạn bộ nhớ/độ rộng; không bịa quy mô số. |
| nghiêm trọng | W00, W06 | Khởi tạo và thời điểm tăng độ rộng chưa rõ | Chọn bản minh họa $D[0..255]$, `next_code=256`; sau mã $2^b-1$, chuyển sang $b+1$ bit trước mã kế; ghi định dạng khác có thể dùng chính sách khác. |
| trung bình | S01 | Không buộc phân biệt LZ78 và LZW | Dùng bốn tình huống riêng, gồm cặp `(i,c)` và luồng byte chỉ phát mã. |
| trung bình | J01, J06–J10 | MSE được nêu rồi bỏ | Nối sai số lượng tử về MSE trong ghi chú J06 và tốc độ bit ở J10. |
| trung bình | storyboard | Thiếu câu nối, bản đồ không khớp thứ tự thật | Viết lại hành trình, trạng thái truyền, câu nối và thứ tự 48 trang. |

## Rà lại độ chính xác sau chỉnh sửa

| Mức độ | Trang | Vấn đề còn lại | Cách xử lý |
|---|---|---|---|
| nghiêm trọng | L07, Z04 | Chứng minh chưa tách token thường và token EOS | Tách hai nhánh; nêu EOS không được phát, không được thêm vào từ điển LZ78 và làm thuật toán dừng. |
| nghiêm trọng | L08, Z05, W06 | Cận thời gian–bộ nhớ thiếu giả thiết | Thêm $O(nWL)$ cho LZ77 vét cạn, $O(n)$ giải mã, $O(W+L)$ bộ nhớ; với LZ78/LZW chỉ nêu gần tuyến tính hoặc kỳ vọng khi có trie/băm phù hợp, $O(M)$ mục dạng (cha, ký tự), và cảnh báo nối chuỗi có thể gây bậc hai. |
| trung bình | L06 | Kiểm tra token tham chiếu thiếu cận $W,L$ | Thêm $1\le d\le\min(W,|output|)$ và $1\le\ell\le L$; literal được kiểm riêng. |

## Quyết định kỹ thuật sau sửa

| Mục | Quyết định |
|---|---|
| LZ77 chồng lấn | Sao chép từng ký tự từ trái sang phải; ký tự vừa sinh có thể làm nguồn. |
| LZ77 kết thúc | Dùng $EOS$ ngoài bảng chữ cái; không phát $EOS$ khi giải mã. |
| LZ77 tham lam | Chỉ mô tả biến thể cụm dài nhất của nguồn; không tuyên bố tối ưu dòng bit. |
| LZ78 | Hai phía thêm đúng $D[i]+c$ ở cùng mã; quy ước EOS và chính sách đầy là phần của định dạng. |
| LZW | Chấp nhận mã chưa có chỉ khi `k = next_code`; mã lớn hơn là lỗi. |
| LZW độ rộng | Bản minh họa chuyển độ rộng sau khi cấp $2^b-1$, trước mã kế; định dạng phải công bố quy tắc. |
| JPEG | Lấy mẫu sắc có thể mất dữ liệu; lượng tử hóa là ánh xạ nhiều-một trong lõi hệ số. DCT/IDCT và mã DC/AC khả nghịch đối với đầu vào của chúng. |
| Độ phức tạp | Với khối $8\times8$ cố định, đường ống có chi phí $\Theta(N)$ theo số mẫu trong mô hình RAM; không suy ra tỷ lệ nén. |
| Chi phí họ LZ | LZ77 vét cạn $O(nWL)$, giải mã $O(n)$, bộ nhớ $O(W+L)$. LZ78/LZW chỉ gần tuyến tính dưới giả thiết trie/băm và biểu diễn mục từ gọn; bộ nhớ $O(M)$. |

## Đề xuất không áp dụng

- Không thêm trang mới cho mô hình chi phí. Nội dung được gộp vào L08, Z05 và W06 để giữ 42 trang và 120 phút.
- Không thêm ví dụ số DCT mới vì nguồn được chọn không cung cấp dữ kiện phù hợp cho một vết ngắn. J05 cung cấp trực giác định tính; J04 là định nghĩa; J06 chạy tay lượng tử hóa bằng dữ kiện đã có.
- Không đưa bảng lượng tử JPEG chuẩn lên mặt trang vì có nhiều bảng và quy tắc chất lượng; deck chỉ nêu vai trò của $Q_{u,v}$.
- Không dùng tên “KwKwK” trên mặt trang. Điều kiện `k=next_code` diễn đạt trực tiếp cơ chế cần học.
- Không thêm tỷ lệ nén, kích thước kho ảnh hoặc tốc độ I/O vì nguồn không cung cấp số liệu phù hợp.

## Ngoại lệ nguồn đã phê duyệt

### Recitation

X01–X05 giữ trực tiếp câu hỏi hoặc vết khuyết ở CMU 15-499 logic 5, 6, 13, 16 và lossy 11, với thời lượng lần lượt 12, 8, 12, 15 và 13 phút. Người dùng đã phê duyệt ngày 2026-08-28 việc dùng ví dụ giáo trình và bài tập CMU làm ngoại lệ cho recitation. Tổng thời lượng giữ nguyên 60 phút; lỗi chặn nguồn đã đóng và không còn lỗi chặn hoặc nghiêm trọng.

### Không có ngoại lệ raster

Không dùng ảnh raster. Mười hai SVG đều có `role="img"`, `aria-label` tiếng Việt, `title`, `desc`; thẻ `img` trong HTML có mô tả thay thế.

## Tự kiểm biên tập

- Rà theo `no-ai-slop/eval.md`: không thêm khẩu hiệu, câu hỏi tu từ, lời dẫn rỗng, nhận định phô trương hoặc số liệu không có nguồn.
- Rà Quill ở mức dàn ý: vết chạy đứng trước giả mã; ký hiệu được truyền từ ví dụ sang thuật toán và chứng minh; LZ78 nối trực tiếp sang LZW; DCT có trực giác trước công thức.
- Không tạo `quill.json` vì đây không phải dự án sách.

## Kiểm định cuối

- Tác tử độ chính xác rà lại lần cuối và kết luận `PASS`: vết LZW khôi phục đúng `ppqpprpqrpqrq`; các nhánh EOS, cận LZ77, LZ78, DCT/IDCT, JPEG và độ rộng mã không còn lỗi nghiêm trọng.
- HTML có 48 mã trang duy nhất và 48 ghi chú diễn giả; storyboard có đủ 48 mã.
- QA ngày 2026-08-28 xác nhận mười hai SVG phân tích XML hợp lệ và có đủ `role="img"`, `aria-label` tiếng Việt, `title`, `desc`; 11 tham chiếu hình trong HTML đều tồn tại. Thiếu metadata tiếp cận đã được đóng mà không đổi nội dung hình.
- Không có tham chiếu ảnh raster hoặc tài nguyên mạng trong nội dung bài.
- Chromium không giao diện tải đủ 48 trang ở $1280\times720$ và $800\times600$: không có lỗi bảng điều khiển, lỗi KaTeX hoặc phần tử vượt khung. Hai bảng ảnh liên hệ đã được xem trực quan.
- `python3 -m reloadserver 8765` không chạy vì môi trường thiếu mô-đun `reloadserver`. Cổng 8765 đã có máy chủ cục bộ; truy cập trang bài giảng trả HTTP 200.
- Dự án Codex Slides bền vững: `20260827233040-b-i-11-n-n-b-ng-t-i-n-v-n-n-m-t-d-li-u-j6kj`. Bốn PDF nguồn, outline và bản tóm tắt kiểm định đã được ghi và đọc lại trong Design Files. Browser Codex Slides không khả dụng trong phiên này, nên không tuyên bố đã rà trực quan bằng Codex Slides; rà trực quan được thực hiện trên RevealJS cục bộ.
- Ngoại lệ recitation đã được phê duyệt ngày 2026-08-28; việc cập nhật `index.html` thuộc vòng điều phối riêng.
