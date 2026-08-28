# Nhật ký rà soát Bài 13

## Trạng thái bản kiểm định

- Tạo mới deck RevealJS, ba tệp planning và mười SVG cục bộ.
- Phần giảng có 49 trang, thiết kế cho 120 phút.
- Recitation có 10 trang kể cả trang giao nhiệm vụ, thiết kế cho 60 phút.
- CSS/RevealJS dùng chung và Bài 10–12 không bị sửa.
- `2627-1/index.html` chỉ được cập nhật sau khi bản cuối qua kiểm định.

## Quyết định nguồn

- Dùng *Database System Concepts* 7e, Chương 14 làm trục cho chỉ mục, B+-Tree, B-Tree và băm tĩnh.
- Dùng Chương 14 trang chiếu 71–75 cho bitmap cơ sở; dùng Chương 24 trang chiếu 11–15 để bổ sung bitmap tồn tại và bitmap NULL cho phép NOT.
- Dùng trực tiếp Practice Exercises/Solutions 14.1, 14.3(b), 14.4 và 14.13.
- Không dùng MMDS hoặc Stanford CS246 vì không thuộc cụm nguồn của bài và không bao phủ chỉ mục đĩa ở mức cần thiết.
- Không dùng số liệu thời gian truy cập thiết bị đã cũ trong Chương 14. Giữ ví dụ một triệu khóa và hệ số phân nhánh khoảng 100 vì đây là ví dụ cấu trúc, không phải số đo phần cứng hiện thời.

## Sai khác có chủ ý

- Chuẩn hóa $m$ là hệ số phân nhánh tối đa, $d$ là số cạnh gốc–lá, $K$ là số khóa và $M$ là số ngăn băm. Dành $h$ cho hàm băm; không dùng $B$ vì Bài 12 dùng cho tổng khung đệm.
- B+-Tree là trọng tâm; B-Tree chỉ đối chiếu hai trang. Lược chỉ mục dày/thưa chi tiết, LSM, buffer tree, chỉ mục không gian và thời gian vì ngoài phạm vi Bài 13 đề xuất.
- Dùng vết số của bài 14.3(b) trong phần giảng để truyền cùng dữ liệu sang recitation.
- Chỉ làm trường hợp $m=6$ của bài 14.3; không đưa $m=4$ và $m=8$.
- Tách rõ hai quy tắc: tách lá sao chép khóa nhỏ nhất của lá phải lên cha; tách nút trong đẩy khóa phân cách giữa lên cha và bỏ nó khỏi hai nút mới. Vết nút trong theo trang 33: đẩy 15, giữ [5,10] và [20,25,30].
- Sửa lỗi trong hình lời giải 14.4(b) sau Insert 8: lá phải phải là $[19,23,29,31]$, không phải $[9,23,29,31]$. Insert 8 không thể xóa khóa 19; cây sửa bảo toàn đúng đa tập khóa.
- Với bài 14.13(b), `Finance AND S4` chỉ tạo ứng viên. Deck bắt buộc đọc bản ghi ứng viên và lọc lại lương từ 80.000 vì $S_4$ bắt đầu từ 70.000.
- Thêm `X07D` với đủ 12 ID, tên, khoa và lương từ lời giải 14.13; phân bổ 3+5+7 phút, không đổi tổng 15 phút.
- Đổi thứ tự cục bộ thành ví dụ trước hình thức hóa: `B00→B01→B03→B02→B04`, `H00→H02→H01→H03`, `M00→M00A→M01`. Đã rà lại hai trang lân cận mỗi phía; ID được giữ để vết nguồn ổn định.
- Bổ sung mô hình chi phí: $f=\lceil m/2\rceil$ cho nút trong không phải gốc, $d=O(\log_f K)$; B+-Tree điểm $d+1+D$, khoảng $d+1+L+D$, cập nhật đọc/ghi $O(d+1)$; băm $1+t+D$; bitmap giá trị $qR$ bit, tối đa $(q+2)R$ với $E$/NULL, $\lceil R/w\rceil$ phép toán từ và I/O dữ liệu ứng viên. $N$ là số khối tệp dữ liệu.
- Không khẳng định B+-Tree luôn ít I/O hơn B-Tree. Hai trang tổng hợp tách ma trận truy vấn/I/O và cập nhật/dung lượng.
- Vòng sửa 2: hình `bplus-delete.svg` ghi đúng “sau xóa 19, trước gộp”, thêm đủ cạnh gốc–lá và chuỗi lá ở cả hai trạng thái. Hình băm bỏ phép `mod 10` không có trong nguồn.
- Vòng sửa 2: giả mã hiển thị được giới hạn cho khóa duy nhất/khóa ghép; ghi chú nêu rõ thêm RID không tăng số khóa và chỉ xóa mục khóa khi danh sách RID rỗng.

## Tự chạy lại ví dụ

- Bài 14.3(b): gốc $[7,19]$; ba lá $[2,3,5]$, $[7,11,17]$, $[19,23,29,31]$.
- Insert 9, 10: lá giữa lần lượt có 4 và 5 khóa, chưa tràn.
- Insert 8: sáu khóa chia 3–3; gốc thành $[7,10,19]$; bốn lá đều trong cận 3–5 khóa.
- Delete 23: lá $[19,29,31]$ còn đúng ba khóa.
- Delete 19: lá $[29,31]$ thiếu; gộp với $[10,11,17]$ thành năm khóa; gốc thành $[7,10]$.
- Bitmap lương: $S_1=001000000000$, $S_2=000000000000$, $S_3=100010010000$, $S_4=010101101111$.
- `Finance AND S4 = 010000001000`; vị trí ứng viên là Wu và Singh; cả hai qua bộ lọc lương từ 80.000.

## Hợp nhất báo cáo rà soát

- Đã xử lý các lỗi nghiêm trọng về dữ kiện bài 14.13, hình cây không đủ con/lá, giả thiết khóa trùng, định nghĩa chiều sâu và chi phí khối dữ liệu.
- Đã xử lý các lỗi trung bình về thứ tự ví dụ–hình thức hóa, vết tách nút trong, kiểm tra giữa cụm, vết băm, bảng chân trị bitmap, chỉ số từ 0, ma trận so sánh và thuật ngữ thuần Việt.
- Giữ B-Tree ở mức đối chiếu vì dạy thuật toán cập nhật riêng sẽ vượt phạm vi 120 phút. Không tạo bài recitation băm vì nguồn bài tập được chọn không cung cấp bài tương ứng.
- Hình lời giải in sai khóa 19 chỉ được nêu trong ghi chú và planning; mặt trang `X05` yêu cầu kiểm bảo toàn khóa, không hiển thị nhãn quy trình sửa nguồn.

## Trường hợp biên đã xử lý

- Cây rỗng, gốc là lá, gốc trong có hai con, khóa bằng khóa phân cách và khóa trùng.
- Lá/nút trong tràn, tách gốc, lá thiếu, mượn, gộp, lan lên cha và gốc một con.
- Ngăn băm va chạm, khóa trùng, chuỗi tràn dài và M cố định; không suy diễn tràn khi chưa biết sức chứa.
- Vị trí bản ghi đã xóa, NULL và điều kiện truy vấn hẹp hơn dải bitmap.

## Tự rà no-ai-slop

- Nội dung hiển thị dùng câu ngắn và động từ trực tiếp.
- Không dùng câu hỏi tu từ, khẩu hiệu, nhận định quảng bá, lời dẫn rỗng hoặc kết luận lặp.
- Tiêu đề thuần Việt; tiếng Anh chỉ còn tên cấu trúc chuẩn, SQL, NULL, AND/OR/NOT và ký hiệu.
- Các câu hỏi tương tác đều dùng nhãn “Câu hỏi:”.

## Tự rà Quill

- Mạch khái niệm giữ thứ tự tình huống → trực giác/vết → hình thức → thuật toán/tính đúng → chi phí → kiểm tra.
- Ký hiệu $m,d,f,K,M,c,N_e,t,L,D,R,q,w,E,V_v,V_{\mathrm{NULL}}$ không đổi nghĩa giữa các phần.
- Vết $m=6$ và dữ liệu bitmap được truyền từ phần giảng sang recitation.
- Không có `quill.json`; không khởi tạo vì đây không phải dự án sách.

## Ngoại lệ và giới hạn

- Không có ảnh raster hoặc phụ thuộc mạng cốt lõi.
- Codex Slides Browser hiện không khả dụng; không tuyên bố đã rà trực quan bằng Browser. Design Files `generated/outline.md` và `generated/brief.md` của dự án `20260828012219-b-i-13-ch-m-c-truy-n-th-ng-v-b-m-t-nh-3hv7` đã được đồng bộ và đọc lại khớp với bản trong kho.
- Lệnh bắt buộc `python3 -m reloadserver 8765` không chạy vì môi trường thiếu mô-đun `reloadserver`. Kiểm định tiếp tục trên máy chủ HTTP cục bộ đã có ở cổng 8765; URL bài giảng trả HTTP 200.

## Kiểm định cuối

- Rà lại độ chính xác sau hai vòng sửa: PASS; không còn lỗi chặn bàn giao hoặc nghiêm trọng. Các vết 14.3(b), 14.4, 14.13, phép phủ định bitmap, công thức chi phí và trường hợp biên đã được tính lại.
- HTML có 59 `data-slide-id` duy nhất, 59 ghi chú diễn giả và 9 phần dọc; mọi trang nằm đúng hai tầng `section`.
- Mười SVG đều là XML hợp lệ, có vai trò và mô tả tiếp cận; mọi đường dẫn tồn tại; không có ảnh raster hoặc tài nguyên mạng cốt lõi.
- Chromium duyệt đủ 59 trang ở 1280 × 720 và 800 × 600: 0 lỗi JavaScript, 0 lỗi KaTeX, 0 tràn hoặc chồng lấn theo kiểm tra hình học.
- Đã rà contact sheet toàn bộ hai kích thước và các trang trọng yếu `C09`, `D00`, `H02`, `M05`, `T00`, `T01`, `X07D`. Cỡ chữ nhỏ nhất đo được ở khung chuẩn là 25,83 px trên `X07D`.
- `git diff --check` đạt; không có tệp nhị phân nguồn bên thứ ba được Git theo dõi.
