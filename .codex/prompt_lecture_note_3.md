# Prompt xác định goal ghi chú Bài 03

Hãy xác định goal cho việc xây dựng ghi chú bài giảng của **Bài 03 — PageRank: mô hình và tính toán**, học phần **Giải thuật nền tảng của Khoa học dữ liệu**, học kỳ 1 năm học 2026–2027. Đây là bước chốt phạm vi; chưa soạn `lecture-note.md`, chưa sửa bộ trang chiếu và chưa cập nhật `index.html`.

## Đầu vào đã xác định

- Bài: `03 — PageRank: mô hình và tính toán` theo thứ tự đề xuất, lấy phần PageRank của buổi gốc 4 và dùng lại MapReduce từ Bài 02.
- Tệp trang chiếu hiện có: `2627-1/lecture-03-pagerank-mo-hinh-va-tinh-toan.html`.
- Ghi chú đích: `2627-1/materials/lec-03/lecture-note.md`.
- Mức độ: `đầy đủ`.
- Đối tượng: sinh viên đại học đã học Bài 02, đồ thị có hướng, phép nhân ma trận–vector và phân phối xác suất cơ bản.
- Yêu cầu riêng: ghi chú phải đọc độc lập với trang chiếu; dùng cùng đồ thị $y,a,m$, quy ước ma trận cột, ký hiệu $P_0,\bar P,A_\beta,r^{(t)}$ và thứ tự khái niệm; mở rộng vết chạy, tính đúng, hội tụ, cận dừng, biểu diễn thưa và một vòng PageRank bằng MapReduce khi nguồn hỗ trợ.
- Giới hạn: chỉ xác định goal và kế hoạch; không tạo nội dung ghi chú, không sửa HTML, SVG, planning hoặc index ở bước này.

`Đầy đủ` yêu cầu mọi chủ đề cốt lõi có đủ thành phần áp dụng trong khuôn trình bày, mọi mệnh đề kỹ thuật có nguồn, ví dụ quan trọng được tính lại, thuật toán có đặc tả–tính đúng–chi phí và mỗi cụm có câu hỏi tự kiểm tra. Mức này không cho phép tự thêm chủ đề hoặc mở rộng sang Bài 04.

## Phạm vi sơ bộ phải kiểm chứng

Goal phải phục vụ các sản phẩm học tập sau:

1. đặc tả đồ thị Web có hướng, mô hình người lướt ngẫu nhiên, ma trận chuyển cột và phương trình PageRank;
2. chạy tay phép cập nhật trên đồ thị nhỏ $y,a,m$, bảo toàn phân phối xác suất và phân biệt nghiệm cố định với một vòng lặp;
3. nhận diện nút cụt và bẫy nhện, giải thích mất hoặc kẹt khối lượng, sửa cột nút cụt và thêm hệ số giảm/dịch chuyển ngẫu nhiên;
4. nêu đủ giả thiết cho hội tụ khi không có hệ số giảm; với $0<\beta<1$, dùng ánh xạ co theo chuẩn $L_1$ để lập luận duy nhất, hội tụ và cận dừng hậu nghiệm;
5. đặc tả thuật toán lặp gồm đầu vào, đầu ra, điều kiện trước/sau, $\tau$, $K_{\max}$, trường hợp đạt và chưa đạt ngưỡng;
6. biểu diễn ma trận thưa bằng cạnh, mô tả một vòng PageRank phân tán với bản ghi cấu trúc, đóng góp, tổng nút cụt $\delta$, thay đổi $\Delta$ và chi phí $\Theta(n+m)$ theo mô hình nguồn.

Không đưa Topic-Sensitive PageRank, link spam, TrustRank, Spam Mass hoặc HITS vào tuyến chính; các chủ đề này thuộc Bài 04. Không biến ghi chú thành hướng dẫn API hoặc cài đặt Hadoop. Bài tập chỉ dùng trực tiếp MMDS Bài 5.1.1, 5.1.2, 5.2.1 và 5.2.2; giữ nguyên dữ kiện, hình và yêu cầu toán học.

## Nguồn bắt buộc phải đọc

1. `AGENTS.md`.
2. Mục Bài 03 và các phần liên quan trong `sources/source.md`: tình huống đồ thị Web lớn, mục tiêu–tiên quyết–học liệu, thứ tự đề xuất, ánh xạ từ phần PageRank của buổi gốc 4 và mạch Bài 02 → 03 → 04.
3. Dòng `Buổi đề xuất 3` trong `sources/reference-slides/README.md`.
4. `sources/textbooks/mmds-3e-ch05-link-analysis.pdf`: kiểm tra trực tiếp mục 5.1.2–5.1.5, 5.2.1–5.2.2; Bài 5.1.1–5.1.2 ở trang in 187–188 và Bài 5.2.1–5.2.2 ở trang in 195. Mục 5.1.1 chỉ dùng làm bối cảnh nếu cần; từ mục 5.3 trở đi thuộc Bài 04.
5. `sources/reference-slides/mmds/ch05-linkanalysis1.pdf`, đọc toàn bộ; ưu tiên các cụm về mô hình, đồ thị $y,a,m$, nút cụt, bẫy nhện, hệ số giảm, biểu diễn thưa và PageRank phân tán.
6. `sources/reference-slides/stanford-cs246/09-pagerank.pdf`, đọc toàn bộ; dùng để so sánh trực giác người lướt, ví dụ/hình tính toán và diễn giải PageRank quy mô lớn. Không lấy phần Topic-Specific PageRank làm nội dung Bài 03.
7. `2627-1/planning/lec-03/outline.md`, `storyboard.md`, `review-log.md`, năm SVG trong `2627-1/img/lec-03/` và bộ trang chiếu hiện có của Bài 03.
8. `2627-1/material-viewer.html`, `material-viewer.css`, `material-viewer.js`, `material-index.css`, các mẫu trong `materials/_templates/` và `2627-1/index.html`.
9. `.codex/lecture-note-goal-prompt.md`, `.codex/prompt_lecture_note_1.md`, `.codex/goal_lecture_1.md` và `openrouter-mcp/README.md` để kế thừa cấu trúc và quy trình, không kế thừa nội dung Bài 01.

Với từng cụm, so sánh slide chính thức MMDS và Stanford theo mức khớp mục tiêu, độ chính xác, ví dụ/hình và khả năng Việt hóa. Dùng sách MMDS để kiểm chứng. Nếu hai nguồn tương đương, ưu tiên MMDS; nếu chọn Stanford, ghi lý do cụ thể. Không sao chép CSS, phông chữ hoặc tài sản nhị phân của nguồn.

## Cách điều phối

Người dùng cho phép gửi tới OpenRouter nội dung các tệp cần thiết trong workspace để thực hiện nhiệm vụ, ngoại trừ `.env`, `.env.*`, khóa, token, mật khẩu, cookie, khóa riêng, thông tin xác thực và mọi giá trị bí mật. Không đọc, đưa vào prompt hoặc log các nội dung bị loại trừ.

1. Reader và reviewer dùng `z-ai/glm-5.3-flash` qua OpenRouter. Từ `openrouter-mcp/`, chạy song song khi đầu vào ổn định:
   - `uv run openrouter-mcp-reader --repo-root .. --json --task-profile plan "Lập kế hoạch hẹp cho goal ghi chú Bài 03; không sửa tệp."`;
   - `uv run openrouter-mcp-reader --repo-root .. --json --task-profile source "Kiểm kê và ánh xạ nguồn hẹp cho ghi chú Bài 03; không sửa tệp."`.
2. Reader lập kế hoạch xác định mục tiêu, đối tượng, phạm vi, đầu ra, tiêu chí hoàn thành, rủi ro và quan hệ tuần tự–song song.
3. Reader nguồn kiểm kê định nghĩa, ví dụ, hình, mệnh đề, thuật toán, chứng minh, bài tập, nguồn và khoảng trống. Phân biệt mệnh đề nguồn với quyết định biên tập, nhất là phần ánh xạ co và cận dừng.
4. Giao một reviewer GLM độc lập lập bản đồ chủ đề. Mỗi chủ đề nhận nhãn `cốt lõi`, `cầu nối`, `bổ sung` hoặc `đọc thêm`, kèm nguồn, vai trò, kiến thức đầu vào, sản phẩm học tập, kết nối vào–ra và tác động phạm vi.
5. Codex chính kiểm tra metadata runtime, đối chiếu báo cáo với nguồn, bác đề xuất thiếu căn cứ rồi hợp nhất thành `.codex/goal_lecture_3.md`. Không giao writer trước khi goal được chấp nhận.
6. Khi goal được duyệt, writer dùng `deepseek/deepseek-v4-flash-0731`; năm reviewer và các lượt `recheck` vẫn dùng GLM. Codex chính được phép trực tiếp áp dụng các sửa đã được năm reviewer phê duyệt mà không đổi nguồn, phạm vi hoặc cổng kiểm định.

Nếu worker OpenRouter lỗi, dừng giai đoạn phụ thuộc và báo nguyên văn lỗi; không đổi ngầm model, nhà cung cấp hoặc tác tử khác.

## Điểm cần phân tích trong bản đồ chủ đề

- Đồ thị Web thưa: miền đỉnh/cạnh, đa liên kết được gộp, vòng tự nối, bậc ra và giới hạn không dựng ma trận đặc.
- Người lướt ngẫu nhiên và PageRank lý tưởng: đóng góp theo cạnh, ma trận chuyển cột, vector xác suất, phương trình cố định và vết chạy $y,a,m$.
- Nút cụt và bẫy nhện: hai biến thể riêng của cùng đồ thị; không trộn ma trận hoặc nghiệm giữa đồ thị cơ sở và đồ thị bẫy.
- Sửa nút cụt bằng $\bar P=P_0+ed^T/n$ và hệ số giảm $A_\beta=\beta\bar P+(1-\beta)ee^T/n$; phân biệt biểu diễn toán học với triển khai thưa dùng $\delta=d^Tr$.
- Điều kiện hội tụ: phân biệt bất khả quy, không chu kỳ, tính dương do dịch chuyển ngẫu nhiên, bảo toàn chuẩn $L_1$, ánh xạ co và kết luận duy nhất/hội tụ.
- Cận dừng: phân biệt phần dư $\Delta_t$ với sai số đích $\varepsilon$; kiểm tra hệ số $\beta$ trong cận hậu nghiệm và điều kiện $K_{\max}\in\mathbb N$.
- PageRank quy mô lớn: bản ghi cấu trúc cho mọi nút, kể cả danh sách rỗng; cặp đóng góp; hai tổng toàn cục $\delta,\Delta$; số pha đồng bộ; thời gian, bộ nhớ và I/O theo phạm vi nguồn.
- Bài tập MMDS 5.1.1, 5.1.2, 5.2.1, 5.2.2: đề, hình, gợi ý, lời giải và giả thiết biên; giữ nguyên dữ kiện.

Với mỗi chủ đề, đánh dấu các thành phần áp dụng trong chuỗi `vai trò và nhu cầu → định nghĩa hoặc đặc tả → ví dụ chạy tay → trực quan hoặc hình học → định lý hoặc mệnh đề → thuật toán → chứng minh → ứng dụng, lỗi dễ mắc và kiểm tra`. Ghi `không áp dụng` kèm lý do; không tạo đề mục rỗng.

## Đầu ra bắt buộc

Tạo `.codex/goal_lecture_3.md` bằng tiếng Việt với đúng 13 mục:

1. `Goal`.
2. `Vấn đề trung tâm`.
3. `Bằng chứng hoàn thành`.
4. `Đầu ra`.
5. `Đối tượng và tiên quyết`.
6. `Phạm vi nguồn`.
7. `Bản đồ chủ đề` có `note-topic-id` duy nhất.
8. `Chủ đề bổ sung đề xuất`.
9. `Khuôn trình bày`.
10. `Ngoài phạm vi`.
11. `Rủi ro và điểm cần duyệt`.
12. `Kế hoạch tác tử`.
13. `Trạng thái`.

Goal phải đo được độ bao phủ, tính đúng, khả năng truy nguyên nguồn, tính liên tục và khả năng đọc độc lập với trang chiếu. Chỉ ghi `sẵn sàng soạn` khi nguồn và phạm vi đủ, mọi trang hoặc slide được dùng đã được kiểm tra trực tiếp và mọi chủ đề bổ sung được đưa vào có nguồn đã xác minh. Nếu không, ghi `bị chặn` cùng một yêu cầu cụ thể. Không tạo `quill.json`.
