# Dàn ý Bài 02: MapReduce và ngăn xếp xử lý dữ liệu lớn

## Mục tiêu và quyết định phạm vi

Viết mới bộ trang chiếu và ghi chú tự học Bài 02 cho sinh viên năm 2: theo dõi luồng khóa–giá trị, thiết kế thuật toán cơ bản, chứng minh bằng các đóng góp được gom đúng, và tính chi phí từ đầu vào từng tác vụ. Người dùng yêu cầu lấy `sources/textbooks/ch2n.pdf` làm nguồn chính, mỗi section ngoài ứng với một mục PDF; section đầu gồm tiêu đề, nội dung và mục tiêu.

Bài số 02 theo thứ tự đề xuất trong `sources/source.md`, ánh xạ buổi gốc 4. Phạm vi học phần là MapReduce và ngăn xếp xử lý dữ liệu lớn. Kiến thức đầu vào: lập trình, toán rời rạc, đại số tuyến tính và xác suất cơ bản; khôi phục hàng/cột/quan hệ, nhóm và khóa ngay trước nơi dùng. Thiết kế 120 phút giảng và 60 phút bài tập. Không tạo mã trình diễn ngoài nguồn.

## Bản đồ chủ đề và đồ thị tiên quyết

| Chủ đề | Nhãn | Đầu vào → sản phẩm → phần sau | Nguồn | Quyết định |
|---|---|---|---|---|
| Hệ tệp phân tán | cốt lõi | Giới hạn một máy → khối, bản sao → chia tác vụ | 2.1, tr.22–24 | giữ |
| Đếm từ, nhóm và bộ kết hợp | cốt lõi | Vòng lặp, tổng → map/reduce và bất biến → chọn khóa khác | 2.2, tr.25–30 | giữ, tách vết chạy/giả mã |
| Hàng/cột, quan hệ tập hợp | cầu nối | Bảng dữ liệu → hiểu chọn/chiếu/nối | 2.3.3, tr.32–35 | thêm trước phép toán để không giả định đã học CSDL |
| Nhân ma trận–vector và chia dải | cốt lõi | Tổng theo hàng → phát tích, gom đúng hàng → đọc lặp vector | 2.3.1–2.3.2 | giữ |
| Chọn, chiếu, nối và tổng hợp | cốt lõi | Khóa, quan hệ → giả mã và vết Links → chi phí nối | 2.3.4–2.3.8 | giữ; phép tập hợp 2.3.6 đọc thêm |
| Nhân ma trận–ma trận | đọc thêm | Nối + tổng → liên hệ hai công việc | 2.3.9–2.3.10 | một trang định vị; chi tiết đọc thêm |
| Luồng công việc, Spark | cốt lõi | Một công việc → chuỗi biến đổi, lưu đệm, tính lại → tổng qua nhiều tác vụ | 2.4.1–2.4.3 | giữ, giảm chi tiết hệ thống |
| Các mở rộng khác | đọc thêm | Định vị các mô hình | 2.4.4–2.4.6 | không kiểm tra chi tiết |
| Mô hình đầu vào tác vụ | cốt lõi | Thuật toán cụ thể → bảng Map/Reduce → so sánh có điều kiện | 2.5.1–2.5.3 | giữ, nêu đơn vị trước công thức |
| Bộ nhớ và sao chép | cốt lõi | Lưới reducer → q, rho và mọi cặp ảnh → tính khả thi | 2.6.1–2.6.2 | giữ ví dụ, đổi r thành rho tránh trùng |
| Lược đồ ánh xạ, cận dưới | đọc thêm | Mô hình q/rho → phân tích tổ hợp | 2.6.3–2.6.7 | không giảng chứng minh dài |
| Tổng kết và nguồn | cốt lõi | Thu hồi sản phẩm học tập, hướng đọc | 2.7–2.8 | giữ thành hai section theo yêu cầu |

Không thêm mệnh đề học thuật từ nguồn ngoài. Sáu hình SVG minh họa khối/bản sao, chia dải, luồng công việc, chuỗi Spark, mô hình chi phí và lưới reducer. Các sơ đồ khái niệm được phân biệt với dữ kiện cấu hình thực tế. Không sao chép tài sản hoặc CSS môn tham khảo.

## Quy tắc thể hiện

Với slide: nhu cầu → trực giác → vết chạy → đặc tả/giả mã → lập luận đúng → chi phí → kiểm tra. Vết ký hiệu của ma trận thay ma trận số tự đặt; bốn hàng Links dùng xuyên phép toán và tính chi phí. Với ghi chú: đặc tả trước ví dụ, sau đó giải thích, chứng minh và ứng dụng. Các chủ đề hệ thống không gán định lý hay giả mã khi không áp dụng; dùng cơ chế, điều kiện và tình huống lỗi. Các phần đọc thêm chỉ định vị, không giả vờ hoàn thành chu trình thuật toán.

Bằng chứng hoàn thành: 61 mã trang khớp storyboard, 9 section ngoài, đủ 120+60 phút trong kế hoạch, các ví dụ và công thức tính lại được, năm báo cáo độc lập, xem được slide/ghi chú ngoại tuyến với tài nguyên cục bộ, liên kết chỉ mục đúng. Chi tiết kiểm định và giới hạn công cụ nằm trong review-log.md.

## Thuật ngữ và ký hiệu

| Ký hiệu/thuật ngữ | Quy ước |
|---|---|
| khóa–giá trị | Đơn vị Map phát; mọi cặp trùng vẫn được giữ khi chúng biểu diễn đóng góp |
| reducer / tác vụ Reduce / máy | Một khóa / đơn vị lập lịch nhiều khóa / nơi thực thi |
| RDD | Tập dữ liệu phân tán có khả năng khôi phục; không loại lặp tự động |
| $M,v,x$ | Ma trận, vector đầu vào, vector kết quả |
| $i,j$ | Chỉ số hàng/cột; chỉ số băm 0..b-1 hoặc 0..c-1 được nêu riêng |
| $r,s,t$ | Số bộ của quan hệ R,S,T |
| $I,M$ trong phần chi phí | Tổng kích thước đầu vào Map và Reduce; M ở đây không là ma trận |
| $b,c,k$ | Số nhóm băm B,C và số reducer k=bc |
| $q,\rho$ | Đầu vào tối đa/reducer và số cặp trung gian trung bình/đầu vào |

## Nguồn và tham khảo cách dạy

Nguồn nội dung quyết định: `sources/textbooks/ch2n.pdf`, 60 trang PDF, trang in 20–79. Bản đồ học phần và slide tham khảo đã được kiểm kê trong giai đoạn đầu; MMDS/Stanford chỉ đối chiếu, không quyết định cấu trúc thay chương sách. Tham khảo `../math-4-AI/2627-1/` lecture 01–03 ở mức một ý trung tâm, ví dụ trước ký hiệu, nhịp hình–giải thích–kiểm tra; không chuyển nội dung toán của môn đó sang bài này. Mẫu kỹ thuật: `2627-1/lecture-template.html` và `lecture-style.css`. Đường dẫn kho machine-learning được quy định trong AGENTS không có tại môi trường này; áp dụng các nguyên tắc đã nêu trong AGENTS.

## Đầu ra

HTML, ghi chú, SVG mới, outline, storyboard, review-log và mô tả bài 2 trong index. Không dùng nội dung HTML cũ làm khung; chỉ giữ tên tệp để liên kết học phần ổn định. Các tệp của bài khác và hạ tầng người dùng đang sửa nằm ngoài phạm vi.

## Sửa theo slide_authoring_standard.md — 2026-09-14

Mục tiêu không đổi. Bản hiện hành có52 trang giảng và9 trang recitation, giữ9 section và 120+60phút. Storyboard mới ghi mục đích quan sát được, tiên quyết, cách thể hiện, kết nối, nguồn và thời lượng cho từng trang. Đây là tiêu chí duyệt, không xem tiêu đề như thay thế mục đích học tập.

Quyết định hợp nhất plan/source: giữ các nguồn, thêm các trang cầu nối làm rõ giả thiết và tính đúng; tách giả mã nhân ma trận–vector khỏi vết ký hiệu; chuyển vết nối trước khái quát; thêm quy tắc Map/Reduce nối ba bảng trước tính chi phí; sửa đặc tả cặp ảnh vượt ngưỡng. Không bổ sung tối ưu Lagrange vào phần bắt buộc. Các chủ đề đọc thêm vẫn không thành tiên quyết ngầm.

Thứ tự nối: ví dụ hai cạnh → bảng nhóm → đặc tả/giả mã → hai chiều đúng/biên/chi phí. Thứ tự đánh giá: đơn vị/phạm vi → hình nơi nhận → đếm từng tầng → cộng/thay số → kết luận với điều kiện. Phần ảnh phải giải thích cặp cùng nhóm được giao đúng một nơi. Ghi chú dùng tau cho ngưỡng; s là hàm tương tự trong2.6, khác số bộ quan hệ S trong2.5.
