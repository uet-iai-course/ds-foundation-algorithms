# Nhật ký rà soát Bài 12

## Quyết định nguồn và biên tập

- Dùng Chương 12/13 cho khối và bộ quản lý đệm; Chương 15 cho sắp xếp ngoài, chi phí và truyền dòng.
- Dùng Wisconsin CS 764 cho chọn thay thế vì vết hoạt động/đóng băng và nhận định độ dài kỳ vọng rõ hơn slide sách.
- Không dùng MMDS hoặc Stanford CS246 vì hai nguồn này không bao phủ mô hình khối/khung và sắp xếp ngoài ở phạm vi Bài 12 trong bản đồ nguồn.
- Không dùng số liệu tốc độ thiết bị trong Chương 12 để tránh biến số liệu phần cứng cũ thành mệnh đề hiện thời.
- Vẽ lại tám SVG; không nhập ảnh raster, CSS, phông hoặc tệp nhị phân bên thứ ba.
- Dùng tiếng Việt cho tiêu đề và nhãn. Giữ “Replacement Selection” một lần sau tên Việt để đối chiếu nguồn.

## Báo cáo kiểm định storyboard

- `chặn bàn giao`, `X03`: quy ước ba khung của lời giải 15.1 tưởng như mâu thuẫn với $k=B-1$. Rà lại cho thấy đề có đúng một bản ghi mỗi khối: khung chứa đầu nhỏ nhất vừa rỗng có thể ghi ngay một khối đầu ra đầy rồi nạp tiếp chính dãy đó. Deck giữ lịch I/O đặc biệt này và không khái quát thành $k=B$.
- `nghiêm trọng`, `S02–S03`: thuật toán đứng trước ví dụ. Đã đưa 12 bản ghi nguồn và bốn dãy lên trước giả mã.
- `nghiêm trọng`, `S10–S11/Q00–Q02`: công thức dùng truyền dòng trước khi giải thích điều kiện. Đã chuyển `Q00–Q02` lên trước `S12–S13`.
- `nghiêm trọng`, `R02–R08`: $B$ đổi nghĩa từ khung sang khóa. Đã dùng $H$ cho sức chứa heap theo bản ghi và đổi kết luận thành khoảng $2H$.
- `trung bình`, `S03/S06/S08`: các ví dụ đổi $B,k$ không báo trước. Đã dùng một vết $N=12,B=3,k=2$, $4\rightarrow2\rightarrow1$.
- `trung bình`, `P02`: công thức xuất hiện trước trực giác. Đã bỏ công thức khỏi trang mạch và giữ định nghĩa ở `I04/S05`.
- `trung bình`, `X04`: đáp án hiện sẵn. Đã chuyển thành fragment và giữ hướng dẫn chấm trong ghi chú.
- `trung bình`, nguồn bài tập: trang lời giải sai. Đã sửa 15.1 thành PDF trang 1/trang in 111 và 13.5 thành PDF trang 5/trang in 95.

## Phản biện góc nhìn sinh viên

- `nghiêm trọng`, toàn deck: chữ phụ và giả mã nhỏ hơn ngưỡng đọc. Đã nâng thân trang lên `.82em`; `.tiny`, `.trace` và `pre` đều `.82em` tương đối, không còn cỡ khai báo dưới `.65em` sau khi nhân cấp.
- `trung bình`, `I09/S17/R09/X04`: câu hỏi lộ đáp án. Đã ẩn bằng fragment; đáp án chi tiết vẫn có trong ghi chú.
- `trung bình`, `X01–X04`: bước đọc dữ kiện và tạo dãy chồng nhau, làm 35 phút thiếu hoạt động thật. Đã tách thành 5 phút đọc đặc tả, 10 phút tạo dãy, 10 phút lượt đầu và 10 phút lượt cuối kèm chứng minh.
- `trung bình`, chuyển ý: dữ liệu đổi giữa tạo dãy, trộn và chi phí. Đã truyền cùng 12 bản ghi từ `S02` đến `S14` và `X01–X04`.

## Phản biện chuyên gia giải thuật và khoa học dữ liệu

- `nghiêm trọng`, `S00–S09`: thiếu giả mã External Merge Sort đầy đủ. Đã thêm `S08–S09` với nhóm cuối nhỏ hơn $k$, refill, flush, cập nhật $r\leftarrow\lceil r/k\rceil$ và điều kiện dừng.
- `nghiêm trọng`, `S06–S16/R06`: chỉ có chi phí I/O. Đã thêm heap $k$ đầu dãy, $O(n\log k)$, $O(B)$ khung; chọn thay thế có $O(n\log H)$ và $O(H)$ bản ghi ngoài đệm I/O.
- `nghiêm trọng`, `I06–I07/S16/X05`: trộn lần truyền khối với seek. Đã tách hai đại lượng, nêu mô hình $n_Tt_T+n_St_S$ trong ghi chú và chốt hai quy ước cấp $b_b$ khung.
- `trung bình`, `I00`: use case trừu tượng và tiêu đề nhân hóa. Đã dùng bảng sự kiện vượt RAM cần `ORDER BY` và cấp dòng đã sắp; tiêu đề chuyển sang phát biểu về nút thắt I/O.
- `trung bình`, `S12`: đẳng thức chi phí thiếu chính sách nhóm một dãy. Đã nêu đẳng thức giả sử sao chép mọi dãy ở mỗi lượt; nếu không sao chép thì là cận trên.
- Đánh giá nguồn: không dùng MMDS/Stanford là hợp lý; Database System Concepts và Wisconsin khớp mục tiêu hơn.

## Phản biện độ chính xác toán học và thuật toán

- `chặn bàn giao`, `X03`: phản biện ban đầu cho rằng phải có khung đầu ra riêng. Rà lại theo dữ kiện một bản ghi mỗi khối xác nhận có thể luân phiên dùng khung vừa rỗng để ghi đầu ra; nhận định phản biện ban đầu không được áp dụng.
- `nghiêm trọng`, `S07`: bất biến chỉ nói các bản ghi đang nạp. Đã phát biểu trên toàn bộ phần chưa xuất và bổ sung khởi tạo–duy trì–kết thúc.
- `nghiêm trọng`, `R08`: $2B$ sai đơn vị. Đã đổi thành $2H$ bản ghi dưới giả thiết thứ tự đến độc lập và đủ ngẫu nhiên.
- `trung bình`, `S01–S09`: thiếu rỗng, mẻ cuối, nhóm cuối, khóa trùng và ổn định. Đã ghi đủ trường hợp; thuật toán không ổn định nếu không có khóa phụ vị trí gốc.
- `trung bình`, `S16`: công thức fan-in phụ thuộc quy ước đệm đầu ra. Đã tách một khung đầu ra và $b_b$ khung đầu ra thành hai công thức.
- Các phép tính đã chạy lại: $r_0=4$, $p=2$, $C_{\mathrm{mat}}=72$, $C_{\mathrm{pipe}}=60$ cho $N=12,B=3,k=2$; vết chọn thay thế cho ba dãy dài 7, 3 và 2.

## Phản biện học thuật và giảng dạy

- `nghiêm trọng`, `S02→S03`: đã sửa thành ví dụ trước giả mã.
- `nghiêm trọng`, `S12–S13/Q00–Q02`: đã dạy vật chất hóa/truyền dòng trước khi dẫn xuất công thức.
- `nghiêm trọng`, `S00–S09`: đã thêm giả mã toàn cục và chứng minh ba bước.
- `nghiêm trọng`, chi phí: đã bổ sung CPU và bộ nhớ nhưng giữ block I/O là mô hình chính.
- `trung bình`, `Q01`: đã diễn đạt chính xác rằng phải tiêu thụ đủ đầu vào để tạo run trước; lượt trộn cuối vẫn có thể truyền dòng.
- `trung bình`, câu kiểm tra: đã ẩn đáp án ban đầu và giữ lời giải trong notes/fragment.

## Sai khác có chủ ý so với nguồn

- Chuẩn hóa $B$ thành tổng số khung, $k=B-1$ khi dành một khung đầu ra; nguồn có chỗ dùng $M$ cho bộ nhớ.
- Dùng $H$ cho sức chứa heap theo bản ghi để không đổi đơn vị của $B$.
- Dùng chuỗi 12 bản ghi của bài 15.1 thêm trong phần giảng. Không đổi dữ kiện hay thứ tự đầu vào.
- Lời giải 15.1 được giữ nguyên ở recitation nhưng gắn đúng mô hình rút gọn của nguồn; phần giảng vẫn dùng $B=3,k=2$.
- Đưa vật chất hóa/truyền dòng lên trước công thức chi phí và đưa ví dụ lên trước giả mã để khôi phục thứ tự học tập.
- Không đưa bài 13.8 theo yêu cầu.

## Tự rà biên tập

- no-ai-slop: nội dung hiển thị dùng câu trực tiếp, không dùng câu hỏi tu từ, khẩu hiệu, nhận định phô trương hoặc thuật ngữ luân phiên.
- Quill: mạch $N,B,k,r_0,p$ được giữ từ ví dụ đến công thức; $H$ chỉ xuất hiện ở chọn thay thế; hai quy ước đầu ra đứng trước chi phí.
- Tiêu đề viết thuần Việt; tiếng Anh chỉ còn tên thuật toán, mã SQL, ký hiệu chuẩn và thuật ngữ cần đối chiếu.

## Trạng thái sau chỉnh sửa

- HTML có 53 trang: 46 trang giảng và 7 trang recitation.
- Thời lượng giữ 120 + 60 phút.
- Tài sản giữ tám SVG; `kway-merge.svg` và `merge-tree.svg` đã vẽ lại theo vết $B=3,k=2$.
- Chưa sửa `index.html` theo phân công.

## Kiểm định cuối

- Rà lại độ chính xác sau chỉnh sửa: đạt. Ngoại lệ ba khung của bài 15.1 đã được kiểm lại theo lịch một bản ghi mỗi khối; các công thức, vết chạy, $H$, nguồn và ký hiệu chi phí đều đạt.
- Kiểm tra tĩnh: 53 mã trang duy nhất, 53 ghi chú, 61 cặp `section`, storyboard ánh xạ đủ 53 mã, tám đường dẫn ảnh hợp lệ và không có tài nguyên mạng cốt lõi.
- Tám SVG phân tích được bằng bộ phân tích XML chuẩn; mỗi tệp có `role="img"` và `title` hoặc `desc`. HTML không tham chiếu ảnh raster.
- Lệnh bắt buộc `python3 -m reloadserver 8765` không chạy vì môi trường thiếu mô-đun `reloadserver`. Máy chủ HTTP cục bộ an toàn đang có tại cổng 8765 trả HTTP 200 cho URL của bài.
- Chromium/Playwright đã duyệt đủ 53 trang ở 1280×720 và 800×600: không lỗi console, không lỗi KaTeX, không tràn hoặc chồng lấn theo kiểm tra hình học. Hai contact sheet và các trang chữ dày đã được xem trực quan.
- Dự án Codex Slides bền vững: `20260828001844-b-i-12-m-h-nh-i-o-v-s-p-x-p-ngo-i-b-nh-9zjs`. Bốn nguồn nhị phân đã gắn từ đầu; `generated/outline.md` và `generated/brief.md` đã đồng bộ và đọc lại sau bản sửa cuối.
- Browser tích hợp của Codex Slides không khả dụng trong phiên này. Vì vậy không tuyên bố đã render hoặc rà trực quan deck trong Codex Slides; kiểm định trực quan cuối dùng RevealJS cục bộ và Chromium.
