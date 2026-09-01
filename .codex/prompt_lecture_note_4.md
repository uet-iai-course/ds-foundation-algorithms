# Prompt xác định goal ghi chú Bài 04

Hãy xác định goal cho ghi chú tự học của **Bài 04 — PageRank theo chủ đề, liên kết rác và HITS**, học phần **Giải thuật nền tảng của Khoa học dữ liệu**, học kỳ 1 năm học 2026–2027. Đây là bước chốt phạm vi; chưa soạn `lecture-note.md`, chưa sửa deck và chưa cập nhật index.

## Đầu vào đã xác định

- Bài theo thứ tự đề xuất: `04 — PageRank theo chủ đề, liên kết rác và HITS`, ánh xạ từ buổi gốc 5.
- Deck: `2627-1/lecture-04-pagerank-theo-chu-de-lien-ket-rac-va-hits.html`.
- Ghi chú đích: `2627-1/materials/lec-04/lecture-note.md`.
- Planning: `2627-1/planning/lec-04/{outline,storyboard,review-log}.md`.
- Đối tượng đã học Bài 03, đồ thị có hướng, ma trận–vector, phân phối xác suất và chuẩn $L_1$.
- Mức độ `đầy đủ`: mỗi chủ đề cốt lõi phải có đặc tả, ví dụ kiểm được, lập luận đúng, chi phí, giới hạn và tự kiểm tra; không tự mở rộng ngoài MMDS §5.3–5.5.

## Sản phẩm học tập phải phục vụ

1. Thay vector dịch chuyển đều bằng $q_S=e_S/|S|$, tính PageRank theo chủ đề và giải thích cách chọn hoặc phối hợp các vector đã tính.
2. Phân tích cụm thao túng liên kết ở Hình 5.16, tách công thức chính xác khỏi xấp xỉ và kiểm số của Ví dụ 5.11.
3. Đặc tả TrustRank như PageRank theo chủ đề với tập tin cậy $T$, tính khối lượng rác $s_p=(r_p-t_p)/r_p$ khi $r_p>0$, nêu đúng giới hạn diễn giải.
4. Đặc tả HITS với ma trận Boolean $L$ có hàng là nguồn, hai vector trang trung tâm $h$ và trang thẩm quyền $a$, chạy tay trước ma trận, chuẩn hóa, dừng, trường hợp vector 0, điều kiện hội tụ và chi phí $\Theta(n+m_G)$ mỗi vòng.
5. So sánh PageRank theo chủ đề, TrustRank, khối lượng rác và HITS theo phạm vi đồ thị, tín hiệu khởi tạo, đầu ra, bảo đảm và chi phí.

Không dạy phân loại chủ đề bằng Jaccard ở MMDS §5.3.4; nội dung này thuộc Bài 05. Không biến bài thành hướng dẫn API hay cài đặt cụm. Bài tập chỉ dùng trực tiếp MMDS 5.3.1, 5.4.2 và 5.5.1, giữ nguyên đồ thị, dữ kiện và yêu cầu.

## Nguồn bắt buộc

1. `AGENTS.md` và mục Bài 04 trong `sources/source.md`.
2. Dòng Bài 04 trong `sources/reference-slides/README.md`.
3. `sources/textbooks/mmds-3e-ch05-link-analysis.pdf`, trực tiếp §5.3–5.5, Ví dụ 5.10–5.14, Hình 5.15–5.20 và Bài 5.3.1, 5.4.2, 5.5.1.
4. `sources/reference-slides/mmds/ch05-linkanalysis1.pdf` cho ký hiệu nối từ Bài 03; `sources/reference-slides/mmds/ch05-linkanalysis2.pdf` cho nội dung chính.
5. `sources/reference-slides/stanford-cs246/10-spam.pdf` để so sánh từng cụm; ưu tiên MMDS khi tương đương, ghi lý do nếu Stanford rõ hơn.
6. Deck, planning và sáu SVG hiện có trong `2627-1/img/lec-04/`.
7. Viewer, mẫu Markdown và `2627-1/index.html` để chốt ràng buộc phát hành.

Phải phân biệt phát biểu của nguồn với phần làm chặt do học phần chứng minh. Không gán điều kiện co, bảo đảm HITS, điều kiện dừng hoặc giới hạn tỷ số cho MMDS nếu nguồn không phát biểu như vậy.

## Điều phối OpenRouter

Người dùng cho phép gửi các tệp cần thiết đã lọc tới OpenRouter, trừ `.env`, khóa, token, mật khẩu, cookie, khóa riêng và thông tin xác thực.

1. Reader/reviewer dùng `z-ai/glm-5.3-flash` qua OpenRouter.
2. Chạy một reader lập kế hoạch (`plan`), một reader ánh xạ nguồn (`source`) và một reviewer lập bản đồ chủ đề (`review`). Các vai chỉ đọc và đề xuất độc lập.
3. Codex chính đối chiếu nguồn, bác đề xuất thiếu căn cứ và hợp nhất goal trước khi writer chạy.
4. Writer dùng `deepseek/deepseek-v4-flash-0731`; năm reviewer và recheck giữ GLM. Codex chính được phép áp dụng trực tiếp các sửa được reviewer phê duyệt.
5. Worker lỗi thì ghi nguyên văn và thử lại cùng model trên dossier hẹp hơn; không đổi ngầm model, nguồn, phạm vi hoặc cổng.

## Điểm bắt buộc trong bản đồ chủ đề

- Mạch vào từ Bài 03: $P$ là ma trận chuyển cột đã sửa nút cụt, $0<\beta<1$, vector xác suất và phép lặp.
- PageRank theo chủ đề: $S\ne\varnothing$, $e_S$, $q_S$, một vòng chạy tay Hình 5.15, phép co giữ nguyên, chi phí lưu $k$ vector và bước chọn/phối hợp.
- Cụm thao túng: ba vùng trang, $N,q,x,y$, luồng hạng, đẳng thức chính xác, điều kiện xấp xỉ và Ví dụ 5.11; không đổi $m_G=|E|$ thành số trang hỗ trợ.
- TrustRank: $T\ne\varnothing$, $q_T$, khởi tạo, phép lặp, cách chọn tập tin cậy, bảng Hình 5.17 và giới hạn của khối lượng rác.
- HITS: đồ thị con truy vấn, $L$ hàng nguồn, tổng trên cạnh, $a=L^Th$, $h=La$, chuẩn hóa vô cùng, giả mã, vector 0, điều kiện dừng, dạng trị riêng và điều kiện hội tụ.
- So sánh: không xem bốn tên là cùng một thuật toán; chỉ ra đầu ra một điểm hay hai vai trò, đồ thị toàn cục hay đồ thị con và tín hiệu dịch chuyển.
- Bài tập MMDS: 5.3.1 dùng Hình 5.15 với tập dịch chuyển (a) $\{A\}$, (b) $\{A,C\}$; 5.4.2 dùng Hình 5.1 với chỉ $B$ tin cậy; 5.5.1 tính hubbiness và authority cho Hình 5.1.

Với mỗi chủ đề, đánh dấu thành phần trong chuỗi `vai trò và nhu cầu → định nghĩa/đặc tả → ví dụ chạy tay → trực quan → mệnh đề/thuật toán → chứng minh → ứng dụng, lỗi dễ mắc và kiểm tra`. Mục không áp dụng phải có lý do.

## Đầu ra goal

Tạo `.codex/goal_lecture_4.md` bằng tiếng Việt với đúng 13 mục:

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

Chỉ ghi `sẵn sàng soạn` khi đã kiểm trực tiếp các phần nguồn và ba đề bài, mọi bổ sung có căn cứ, và không còn khoảng trống làm thay đổi đáng kể kết quả. Không tạo `quill.json`.
