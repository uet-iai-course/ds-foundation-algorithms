# Điều chỉnh cách viết và minh họa Lecture 03

## Yêu cầu và bằng chứng đối chiếu

Mục tiêu: giúp sinh viên năm 2 nhìn thấy dữ liệu, thao tác và kết quả trước khi phải tự nối các ký hiệu. Đối chiếu trực tiếp bản trình chiếu 1280 × 720 của Lecture 02 và Lecture 03, sau khi hai bài đã dùng CSS chung. Đây là thay đổi cách giải thích, không phải một lần thay giao diện.

| Khía cạnh | Bằng chứng từ Lecture 02 | Điểm cần sửa ở Lecture 03 | Quyết định |
|---|---|---|---|
| Bài toán và đối tượng | Slide đếm từ đặt văn bản, từ và số đếm cạnh đặc tả | Đặc tả đồ thị và véc tơ điểm chủ yếu là hai khối chữ | Thể hiện đầu vào → phép tính → đầu ra; giữ đầy đủ miền và điều kiện |
| Vết chạy | Slide chạy MapReduce đặt dữ liệu Map, nhóm và Reduce theo ba cột | Giả mã Map/Combine đứng riêng, chưa thấy bản ghi cụ thể qua từng bước | Đặt vết chạy của một khối cạnh giả mã, dùng lại đồ thị A–D |
| Ký hiệu và hình | Ví dụ nhân ma trận–véc tơ cho thấy các ô, khối và cặp đầu ra tương ứng | Slide ma trận liên kết có đồ thị nhưng cột A chỉ nằm trong caption | Nối trực tiếp từng cạnh ra của A với hàng tương ứng trong cột A |
| Công thức | Kết quả tính được đặt gần thao tác sinh ra nó | Quy tắc cập nhật lặp lại công thức bằng ba bullet; người học tự nối nguồn điểm | Bố trí ba nguồn đóng góp cùng đi vào một điểm mới |
| Chi phí | Dữ liệu và số phép toán gắn với máy/tác vụ đang xét | Slide đầu vào I có hai card diễn giải dài; 88 và 64 byte chưa gắn với luồng đọc | Minh họa bốn khối và số lần đọc hai dải véc tơ, rồi cộng byte |
| Chú thích | Nhiều caption chốt trực tiếp kết quả của ví dụ | Một số caption chứa cả định nghĩa, ngoại lệ và chuyển ý | Chuyển giải thích phụ vào notes; trên slide giữ giả thiết quyết định và một câu chốt |

Không coi mọi hình của Lecture 03 là chưa đạt. Giữ các đồ thị A–D, hình chia điểm/nhận điểm, bảng kết quả một vòng, timeline song song, hình bộ nhớ và đề bài MMDS đã rõ. Không thêm hình để lấp khoảng trắng.

## Phạm vi và quyết định duyệt kế hoạch

Giữ bảy phần, 63 slide, thời lượng 120 phút giảng và 60 phút bài tập. Giữ mô hình có bước nhảy và bù nút cụt, quy ước cột là nguồn, cùng dữ kiện xuyên suốt, mã Python và bài tập theo sách. Không mở rộng sang Lecture 04.

Hai reader độc lập qua OpenRouter đã kiểm kê đủ 63 slide. Runtime: requested_model = observed_model = `z-ai/glm-5.3-flash`, provider = `OpenRouter`. Điều phối viên đã đối chiếu lại HTML và ảnh trình chiếu; không áp dụng máy móc đề xuất chỉ dựa trên inventory.

Các đề xuất bị bác hoặc hiệu chỉnh:

- Không thêm con số dung lượng biểu diễn thưa “vài trăm MB” cho một tỷ trang: chưa có số cạnh và định dạng để suy ra.
- Không dùng animation/fragment cho bẫy liên kết.
- Không coi sinh viên chưa học MapReduce: Lecture 02 là tiên quyết, cần khôi phục liên hệ với bài đã học.
- Không bỏ chứng minh hội tụ trong notes; phải giữ các giả thiết và luận điểm của mô hình đầy đủ.
- Không dùng sơ đồ S → B → W → T như bốn bước xử lý: đó là các đại lượng đo khác nhau. Đặc biệt T không phải số byte mạng.
- Không khẳng định Q ≤ C cho cả công việc: C trong ví dụ chỉ đếm lõi phép nhân, còn Q phụ thuộc phạm vi đo, điều phối và chạy lại.
- Không vẽ bước nhảy thành mạng đầy đủ các cạnh để tránh nhầm với liên kết thật.

## Các cụm chỉnh sửa đã duyệt

| Cụm | Slide dự kiến | Cách thể hiện và sản phẩm học tập |
|---|---|---|
| Từ bài toán đến phép tính | s01-06, s02-02 | Luồng đồ thị → quy tắc → điểm; đọc được đặc tả đầu vào/đầu ra |
| Từ cạnh sang ma trận | s03-02, s03-03 | Cạnh A → cột A; bảng điểm cũ/mới; hiểu cập nhật đồng thời |
| Hoàn thiện mô hình | s03-04, s03-08, s03-13 | Phần điểm không chuyển được; ba nguồn điểm; bảo toàn tổng |
| Dừng và hội tụ | s03-12, s03-14 | Bảng chênh lệch từng trang; sơ đồ khoảng cách trước/sau F; phân biệt Δ và sai số nghiệm |
| Từ phép tính tới tác vụ | s03-15, s04-03–06, s04-08 | Cạnh → bản ghi → Map → nhóm khóa → Reduce; chỉ rõ điểm cũ và bậc toàn cục |
| Đo tài nguyên | s05-04, s05-07–08 | Số lần đọc dải, byte qua mạng và timeline pha; áp dụng công thức với phạm vi rõ |
| Từ đặc tả tới mã | s06-02–04 | Liên hệ out/r/new/delta với dữ liệu cụ thể; giữ mã chạy được |
| Thu hồi mạch bài | s07-01–02 | Đồ thị → mô hình → tính phân tán → kiểm chứng; không chỉ liệt kê thuật ngữ |

Các slide còn lại được kiểm tra trong toàn deck; chỉ sửa khi có bằng chứng khó theo hoặc mất liên hệ. Mỗi thay đổi phải có câu chốt và đầu vào từ slide trước. Bản ghi này bổ sung storyboard hiện có; không thay các mục nguồn và thời lượng.

## Tiêu chí kiểm định

- Người học chỉ được trên hình/bảng nguồn của từng số trong phép tính đang xét.
- Công thức tổng quát giữ nguyên; ví dụ minh họa không thay chứng minh.
- Giả mã có ít nhất một vết chạy cụ thể trong cùng cụm, với khóa/giá trị và trạng thái cũ/mới rõ.
- Mỗi chi phí nêu đối tượng đo, đơn vị, giả định và phạm vi; không đồng nhất byte đầu vào với byte qua mạng.
- Không giảm thang chữ chung; lớp bố cục mới nằm trong CSS chung và giới hạn cho Lecture 03.
- Kiểm tra tất cả 63 slide, SVG, KaTeX, tràn khung, bàn phím, bản in; kiểm hồi quy Lecture 02 khi đổi CSS chung.
- Các reviewer độc lập và editor xử lý bản nháp; kiểm lại toán và mạch phần thay đổi trước khi commit/push.


## Kết quả triển khai

Đã thay cách thể hiện 21 slide chính và làm rõ định nghĩa C trên s05-05 (22 slide có diff). Giữ s06-03 ở dạng mã đầy đủ một cột để đọc được toàn hàm; liên hệ dữ liệu/trạng thái nằm ở s06-02 và s06-04. Giữ s07-01 vì các kết quả học tập đã rõ, dùng s07-02 để thu hồi vòng tính bằng pipeline. Không giảm cỡ chữ hoặc tăng số slide. Ba SVG mới được sinh từ script; các phép tính và vết chạy bổ sung đã được kiểm bằng phân số và danh sách cạnh.

Các báo cáo độc lập, cách xử lý lỗi công cụ và kiểm định cuối nằm trong [review-log.md](review-log.md). Phần phân tích Lecture 02 được thực hiện cục bộ; hồ sơ gửi OpenRouter chỉ chứa Lecture 03.
