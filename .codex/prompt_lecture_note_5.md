# Prompt xác định goal ghi chú Bài 05

Hãy xác định goal cho ghi chú tự học của **Bài 05 — Biểu diễn tương đồng: Shingling và MinHash**, học phần **Giải thuật nền tảng của Khoa học dữ liệu**, học kỳ 1 năm học 2026–2027. Đây là bước chốt phạm vi; chưa soạn `lecture-note.md`, chưa sửa deck và chưa cập nhật index.

## Đầu vào đã xác định

- Bài theo thứ tự đề xuất: `05 — Biểu diễn tương đồng: Shingling và MinHash`, ánh xạ từ buổi gốc 4.
- Deck: `2627-1/lecture-05-bieu-dien-tuong-dong-shingling-va-minhash.html`.
- Ghi chú đích: `2627-1/materials/lec-05/lecture-note.md`.
- Planning: `2627-1/planning/lec-05/{outline,storyboard,review-log}.md`.
- Đối tượng đã học lập trình, tập hợp, xác suất cơ bản và hàm băm; có thể đọc ma trận thưa.
- Mức độ `đầy đủ`: mỗi chủ đề cốt lõi phải có đặc tả, ví dụ kiểm được, lập luận đúng, chi phí, giới hạn và tự kiểm tra; không tự mở rộng ngoài MMDS §§3.1–3.3.

## Sản phẩm học tập phải phục vụ

1. Chuẩn hóa tài liệu, tạo tập $k$-shingle, xử lý $k>n$ và phân biệt độ dài shingle với độ dài mã băm.
2. Tính, diễn giải và cài đặt độ tương đồng Jaccard trên hai tập hoặc hai danh sách đã sắp; xử lý hợp rỗng.
3. Đặc tả MinHash trên vũ trụ hữu hạn với hoán vị đều và chứng minh $\Pr[h_\pi(C_1)=h_\pi(C_2)]=J(C_1,C_2)$.
4. Ghép $p$ phép thử độc lập thành chữ ký, chứng minh tính không chệch của tỷ lệ hàng trùng và phân tích phương sai trong mô hình lý tưởng.
5. Lập chữ ký bằng một lượt quét ma trận thưa, nêu bất biến, điều kiện dừng, cột rỗng, chi phí thời gian–bộ nhớ và giới hạn do va chạm hoặc họ hàm không đều–độc lập.
6. Giải bốn bài tập trực tiếp MMDS 3.1.1, 3.2.3, 3.3.2 và 3.3.3 mà không đổi dữ kiện hay yêu cầu.

Không dạy LSH, banding, khoảng cách tổng quát, Jaccard đa tập, shingle theo từ hoặc tối ưu chia khối hàng ở §§3.3.6–3.3.7. Không biến bài thành hướng dẫn thư viện hay hệ phân tán.

## Nguồn bắt buộc

1. `AGENTS.md` và mục Bài 05 trong `sources/source.md`.
2. Dòng Bài 05 trong `sources/reference-slides/README.md`.
3. `sources/textbooks/mmds-3e-ch03-finding-similar-items.pdf`, trực tiếp §§3.1–3.3, Ví dụ 3.1, 3.3, 3.4, 3.7, 3.8, Hình 3.2–3.6 và Bài 3.1.1, 3.2.3, 3.3.2, 3.3.3.
4. `sources/reference-slides/mmds/ch03-lsh.pdf` và Stanford CS246 `03-lsh.pdf`, `04-lsh_theory.pdf` để so sánh từng cụm; ưu tiên MMDS khi tương đương và không lấy nội dung LSH.
5. Deck, planning và năm SVG hiện có trong `2627-1/img/lec-05/`.
6. Viewer, mẫu Markdown và `2627-1/index.html` để chốt ràng buộc phát hành.

Phải phân biệt định lý với hoán vị đều khỏi phép thay thế bằng hàm băm thực hành. Phải kiểm độc lập mọi vết chạy, đáp án, miền chỉ số và cận chi phí; không gán phần làm chặt của học phần cho MMDS.

## Điều phối OpenRouter

Người dùng cho phép gửi các tệp cần thiết đã lọc tới OpenRouter, trừ `.env`, khóa, token, mật khẩu, cookie, khóa riêng và thông tin xác thực.

1. Reader/reviewer dùng `z-ai/glm-5.3-flash` qua OpenRouter.
2. Chạy một reader lập kế hoạch (`plan`), một reader ánh xạ nguồn (`source`) và một reviewer lập bản đồ chủ đề (`review`). Các vai chỉ đọc và đề xuất độc lập.
3. Codex chính đối chiếu nguồn, bác đề xuất thiếu căn cứ và hợp nhất goal trước khi writer chạy.
4. Writer dùng `deepseek/deepseek-v4-flash-0731`; năm reviewer và recheck giữ GLM. Codex chính được phép áp dụng trực tiếp các sửa được reviewer phê duyệt.
5. Worker lỗi thì ghi nguyên văn và thử lại cùng model trên dossier hẹp hơn; không đổi ngầm model, nguồn, phạm vi hoặc cổng.

## Điểm bắt buộc trong bản đồ chủ đề

- Tình huống mở: kho tài liệu hoặc trang web gần trùng, $N$ tài liệu tạo $N(N-1)/2$ cặp; Bài 05 giảm kích thước biểu diễn nhưng chưa giảm số cặp.
- Shingling: quy tắc chuẩn hóa, $S_k(D)$ là tập không phải đa tập, Ví dụ 3.3, chọn $k$, băm shingle và va chạm.
- Jaccard: giao, hợp, ba loại hàng X/Y/Z, Ví dụ 3.1, hợp rỗng, thuật toán hai con trỏ và chi phí.
- MinHash lý tưởng: $U$ hữu hạn, tập không rỗng, hoán vị đều, Ví dụ 3.7, chứng minh bằng phần tử đầu tiên của hợp.
- Chữ ký: $p$ hoán vị độc lập, biến chỉ báo Bernoulli, kỳ vọng $pJ$ cho số hàng trùng và $J$ cho tỷ lệ; phương sai chỉ áp dụng dưới giả thiết độc lập.
- Quét thưa: Hình 3.4/Ví dụ 3.8, $SIG$, dữ liệu nhóm theo hàng, bất biến lấy min, cột toàn $\infty$, $O(pu+pz)$ và $\Theta(pN\log(u+1))$ bit dưới mô hình chi phí đã nêu.
- Giới hạn thực hành: mã băm có va chạm hoặc không tương ứng với các hoán vị độc lập–đều thì không được viện dẫn nguyên xi định lý lý tưởng.
- Bài tập: giữ đúng dữ kiện và yêu cầu của 3.1.1, 3.2.3, 3.3.2, 3.3.3; phân biệt Hình 3.4 với Hình 3.6.

Với mỗi chủ đề, đánh dấu thành phần trong chuỗi `vai trò và nhu cầu → định nghĩa/đặc tả → ví dụ chạy tay → trực quan → mệnh đề/thuật toán → chứng minh → ứng dụng, lỗi dễ mắc và kiểm tra`. Mục không áp dụng phải có lý do.

## Đầu ra goal

Tạo `.codex/goal_lecture_5.md` bằng tiếng Việt với đúng 13 mục:

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

Chỉ ghi `sẵn sàng soạn` khi đã kiểm trực tiếp các phần nguồn và bốn đề bài, mọi bổ sung có căn cứ, và không còn khoảng trống làm thay đổi đáng kể kết quả. Không tạo `quill.json`.
