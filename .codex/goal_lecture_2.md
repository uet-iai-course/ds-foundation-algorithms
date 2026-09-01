# Goal brief — Ghi chú Bài 02

## 1. Goal

Xây dựng ghi chú tự học độc lập cho Bài 02, giúp sinh viên đặc tả một phép tính MapReduce, chứng minh kết quả, giải thích cách hệ thống phân phối và chạy lại tác vụ, rồi phân tích chi phí theo đúng đại lượng được đo. Ghi chú nối mô hình MapReduce với hệ tệp phân tán, DAG và Spark mà không biến thành hướng dẫn phần mềm.

## 2. Vấn đề trung tâm

Một kho metadata Web chứa URL, kích thước và thuộc tính trang; toàn bộ kho không vừa bộ nhớ một máy. Cần tính tổng kích thước theo máy chủ. Ví dụ này cho thấy vai trò của giải thuật trong Khoa học dữ liệu: phép cộng chỉ trở thành lời giải dùng được khi ta chọn mô hình truy cập, phân chia công việc, chứng minh tính đúng và tính đúng loại chi phí.

Từ tình huống trên, ghi chú xây dựng luồng map–nhóm theo khóa–reduce, dùng Word Count làm ví dụ chạy tay, rồi mở rộng sang bộ kết hợp, lệch tải, chịu lỗi và ngăn xếp xử lý theo lô.

## 3. Bằng chứng hoàn thành

- Phân biệt đúng Map/Reduce function, mapper/reducer, Map/Reduce task và phần hệ thống thực hiện.
- Có đặc tả Word Count, quy ước tách từ, vết chạy, giả mã, trường hợp biên và chứng minh tính đúng.
- Nêu đủ điều kiện để bộ kết hợp bảo toàn ngữ nghĩa; tách mệnh đề nguồn khỏi điều kiện suy ra.
- Phân tích hàm phân vùng, số task, lệch tải và giới hạn của các quy tắc kinh nghiệm.
- Giải thích đúng lỗi Master, Map worker và Reduce worker; nêu điều kiện thiết kế để chạy lại an toàn.
- Định nghĩa riêng $I+M$ và $I+2M+O$, chỉ ra chúng đo hai phạm vi I/O khác nhau và áp dụng nhất quán.
- Định vị DFS, Hadoop MapReduce, DAG và Spark; nêu khi nào xử lý theo lô phù hợp.
- Bài MMDS 2.2.1(a–c) và 2.3.1(a–d) giữ nguyên dữ kiện, có gợi ý và lời giải đã kiểm tra.
- Mọi mệnh đề kỹ thuật truy nguyên được đến sách hoặc trang chiếu; ghi chú đọc được độc lập.

## 4. Đầu ra

- `2627-1/materials/lec-02/lecture-note.md`;
- SVG cần thiết trong `2627-1/img/lec-02/`;
- cập nhật phần ghi chú trong `2627-1/planning/lec-02/outline.md`, `storyboard.md`, `review-log.md`;
- mục tài nguyên Bài 02 trong `2627-1/index.html`, chỉ công bố sau kiểm định viewer;
- rà deck Bài 02 nếu thay đổi ký hiệu, giả thiết, ví dụ, kết luận hoặc thứ tự dùng chung; ghi tác động trong `review-log.md`.

## 5. Đối tượng và tiên quyết

Sinh viên đã học Bài 01 và biết cặp khóa–giá trị, bảng băm, phép nhóm, vòng lặp, bất biến, độ phức tạp, tệp, bộ nhớ chính và lưu trữ thứ cấp. Khôi phục ngắn phân biệt function với task, tính kết hợp–giao hoán và tổng trên một phân hoạch. Bất biến là công cụ nền cho chứng minh Word Count, không tạo chủ đề riêng.

## 6. Phạm vi nguồn

| Nguồn | Phần dùng | Vai trò |
|---|---|---|
| `sources/source.md` | Bài 02, mục tiêu, tiên quyết, ánh xạ | Chốt phạm vi cấp học phần |
| MMDS 3e, Chương 2 | §2.1; §2.2.1–2.2.6; §2.4; §2.5.1; Bài 2.2.1, 2.3.1 | Nội dung và bài tập chính |
| Slide MMDS Chương 2 | Trang chiếu 2–35, 38–40 | Luồng, điều phối, hình, tổng I/O |
| Stanford CS246 `01-intro.pdf` | Trang chiếu 49–60, 62, 66–69 | DAG/Spark, giới hạn batch, metadata Web, chi phí |
| Planning và deck Bài 02 | Toàn bộ | Giữ thuật ngữ, ký hiệu và mạch đã kiểm định |

Ưu tiên MMDS cho hạ tầng, MapReduce, Word Count, lệch tải và chịu lỗi. Chọn Stanford cho DAG/Spark vì diễn giải nhiều tầng tác vụ, cache, RDD và giới hạn batch rõ hơn; sách MMDS vẫn kiểm chứng khái niệm.

## 7. Bản đồ chủ đề

| `note-topic-id` | Chủ đề | Nhãn | Kết nối vào → ra | Quyết định |
|---|---|---|---|---|
| `note-topic-02-motivation` | Metadata Web và giới hạn bộ nhớ/I/O | cốt lõi | Bài 01 → DFS | giữ |
| `note-topic-02-dfs-locality` | DFS, chunk, bản sao, data locality | cầu nối | động lực → task | giữ ngắn |
| `note-topic-02-map-group-reduce` | Map–nhóm theo khóa–reduce | cốt lõi | khóa–giá trị → Word Count | giữ |
| `note-topic-02-word-count` | Word Count từ đặc tả đến chứng minh | cốt lõi | luồng MapReduce → combiner | giữ |
| `note-topic-02-combiner` | Bộ kết hợp và bảo toàn ngữ nghĩa | cốt lõi | Word Count → tải trung gian | giữ |
| `note-topic-02-partition-skew` | Phân vùng, số task và lệch tải | cốt lõi | nhóm theo khóa → điều phối | giữ |
| `note-topic-02-fault-tolerance` | Điều phối và chạy lại tác vụ | cốt lõi | DFS/task → an toàn chạy lại | giữ |
| `note-topic-02-rerun-safety` | Điều kiện an toàn khi chạy lại | bổ sung | chịu lỗi → DAG | giữ có điều kiện |
| `note-topic-02-cost-models` | Hai quy ước chi phí | cốt lõi | dữ liệu trung gian → chọn ngăn xếp | gộp hai quy ước trong một mục |
| `note-topic-02-dag-spark` | DAG, Spark và ranh giới batch | cốt lõi ở mức định vị | chịu lỗi/chi phí → quyết định mô hình | giữ, không dạy API |
| `note-topic-02-exercises` | Bài tập MMDS 2.2.1 và 2.3.1 | cốt lõi luyện tập | các chủ đề trên → tự kiểm tra | giữ nguyên dữ kiện |

Đồ thị tiên quyết: `motivation → dfs-locality → map-group-reduce → word-count → {combiner, partition-skew} → fault-tolerance → rerun-safety → cost-models → dag-spark`. Bài tập nhận đầu vào từ Word Count, combiner, lệch tải và mô hình chi phí.

## 8. Chủ đề bổ sung đề xuất

- **Thêm** `rerun-safety` như chủ đề ngắn. MMDS mô tả chạy lại nhưng không phát biểu tổng quát về tính quyết định hoặc hiệu ứng ngoài; đây là điều kiện thiết kế suy ra từ đặc tả, không phải trích dẫn nguyên văn.
- **Gộp** điều kiện đóng/cùng kiểu và bảo toàn dưới mọi cây gộp vào `combiner`. Nguồn trực tiếp nêu kết hợp và giao hoán; phần mở rộng phải ghi là điều kiện suy ra để combiner có cùng kiểu và ngữ nghĩa với reducer.
- Không thêm chủ đề khác. PageRank, join, nhân ma trận, đại số quan hệ và API nằm ngoài phạm vi.

## 9. Khuôn trình bày

| Cụm | Thành phần áp dụng | Không áp dụng |
|---|---|---|
| Động lực, DFS | nhu cầu, định nghĩa, ví dụ, trực quan, ứng dụng, kiểm tra | không có định lý hay thuật toán cần chứng minh |
| Map–nhóm–reduce | vai trò, đặc tả, ví dụ, trực quan, quy trình, lỗi dễ mắc | không phát biểu định lý riêng |
| Word Count | đủ chuỗi: đặc tả, vết chạy, trực quan, mệnh đề, giả mã, chứng minh, chi phí, kiểm tra | không |
| Combiner | đặc tả, cây gộp, mệnh đề điều kiện, chứng minh bảo toàn, phản ví dụ | không cần thuật toán độc lập |
| Phân vùng, lệch tải | định nghĩa, ví dụ tải, trực quan, ứng dụng, kiểm tra | quy tắc số task không phải định lý |
| Chịu lỗi, chạy lại | trạng thái, quy trình, ví dụ lỗi, điều kiện thiết kế, phản ví dụ | không có chứng minh hệ thống đầy đủ trong nguồn |
| Chi phí | định nghĩa, phép tính, phạm vi đo, ứng dụng, lỗi dễ mắc | không có hình học hoặc thuật toán mới |
| DAG/Spark | nhu cầu, định nghĩa định vị, hình luồng, so sánh có điều kiện | không dạy API, không chứng minh hiệu năng |
| Bài tập | đề gốc, gợi ý, lời giải, kiểm tra giả thiết | không tạo dữ kiện hoặc bài mới |

Mỗi cụm lớn có câu nối vào, đầu ra cho cụm sau và câu tự kiểm tra. Không tạo đề mục rỗng.

## 10. Ngoài phạm vi

- PageRank, phép nối, đại số quan hệ, nhân ma trận–vector và nhân ma trận.
- Hướng dẫn API Hadoop, Spark, RDD, DataFrame hoặc cài đặt cụm.
- Lịch sử phần mềm ở slide MMDS 43–48.
- Khẳng định Spark luôn nhanh hơn hoặc quy tắc cố định về số task.
- Gọi cả $I+M$ và $I+2M+O$ là byte mạng.
- Mã minh họa, dữ liệu mới và `quill.json`.

Ngoại lệ duy nhất liên quan nhân ma trận là không có: MMDS Bài 2.3.1 ở PDF trang 21 thực tế yêu cầu xử lý một tệp số nguyên rất lớn, không phải bài nhân ma trận.

## 11. Rủi ro và điểm cần duyệt

- Bài 2.3.1 đã được kiểm tra trực tiếp ở PDF trang 21: tìm số lớn nhất, tính trung bình, loại trùng và đếm số giá trị phân biệt; khóa đầu ra được bỏ qua. Writer phải giữ nguyên yêu cầu.
- Quy tắc tách từ, chữ hoa/thường và dấu câu là quy ước ví dụ do ghi chú đặt ra; không gán cho MMDS.
- Điều kiện mở rộng về combiner và an toàn chạy lại là suy luận biên tập; reviewer phải kiểm tra truy nguyên riêng.
- $I+M$ đếm tổng đầu vào task và bao gồm I/O cục bộ; $I+2M+O$ đếm tổng I/O tiến trình. Không so sánh trước khi định nghĩa cùng phạm vi.
- Nhận xét hiệu năng Spark chỉ được trình bày có điều kiện.
- Nếu nội dung dùng chung lệch deck hiện có, phải rà deck và ghi tác động; không mặc định sửa HTML.

## 12. Kế hoạch tác tử

| Giai đoạn | Vai trò/hồ sơ | Quan hệ | Trạng thái |
|---|---|---|---|
| Lập kế hoạch goal | OpenRouter reader `plan` | trước soạn | hoàn tất |
| Ánh xạ nguồn | OpenRouter reader `source` | độc lập với plan | hoàn tất sau khi thu hẹp hồ sơ |
| Bản đồ chủ đề | OpenRouter reviewer `review` | trước writer | hoàn tất |
| Hợp nhất goal | Codex chính | chặn writer | hoàn tất |
| Soạn trong thư mục tạm | OpenRouter writer `write` | sau goal | hoàn tất với `deepseek/deepseek-v4-flash-0731` theo xác nhận của người dùng |
| Năm lượt rà độc lập | OpenRouter reviewers `review` | sau bản nháp | hoàn tất với `z-ai/glm-5.3-flash` |
| Sửa tuần tự | Codex chính theo ủy quyền của người dùng | sau hợp nhất lỗi | hoàn tất; chỉ áp dụng phát hiện đã duyệt |
| Biên tập bản cuối | Codex chính với `$no-ai-slop` và `$quill` | trước tái kiểm | hoàn tất |
| Rà lại thay đổi | OpenRouter reviewer `recheck` | sau sửa | hoàn tất; không còn lỗi trung bình/nghiêm trọng |
| Kiểm định viewer, công bố | Codex chính | sau mọi tái kiểm | hoàn tất ở màn hình rộng, hẹp, bàn phím, bản in và cổng an toàn |

Worker dùng `z-ai/glm-5.3-flash` qua OpenRouter. Chỉ gửi tệp đã lọc; loại `.env`, khóa, token, mật khẩu, cookie, khóa riêng và thông tin xác thực. Nếu worker lỗi, dừng giai đoạn phụ thuộc và báo nguyên văn lỗi; không đổi ngầm mô hình hoặc nhà cung cấp.

## 13. Trạng thái

`hoàn tất`

Các cụm nguồn bắt buộc và PDF trang 21 của Bài 2.3.1 đã được kiểm tra trực tiếp. Bản đồ 11 chủ đề đã được duyệt; hai bổ sung có điều kiện có nhãn và ranh giới rõ. Năm lượt rà độc lập, sửa theo phát hiện đã duyệt, `$no-ai-slop`, `$quill`, các lượt GLM tái kiểm, kiểm định viewer và cập nhật index đều đã hoàn tất. Goal chỉ được đóng sau khi commit của Bài 02 được push và xác minh trên `origin/main`.
