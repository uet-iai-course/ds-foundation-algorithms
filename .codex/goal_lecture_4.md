# Goal ghi chú Bài 04

## 1. Goal

Hoàn thiện ghi chú tự học **Bài 04 — PageRank theo chủ đề, liên kết rác và HITS** tại `2627-1/materials/lec-04/lecture-note.md`. Tài liệu phải giúp sinh viên tự đặc tả, tính, giải thích và so sánh các mô hình trong MMDS §5.3–5.5; dùng cùng ký hiệu và thứ tự khái niệm với deck hiện có nhưng không chép lại trang chiếu.

## 2. Vấn đề trung tâm

PageRank cơ sở cho một điểm toàn cục, nhưng truy vấn cần ưu tiên theo chủ đề, cấu trúc liên kết có thể bị thao túng và một đồ thị con truy vấn có thể cần tách vai trò trang trung tâm khỏi trang thẩm quyền. Ghi chú phải chỉ ra ba thay đổi mô hình tương ứng: thay phân phối dịch chuyển, thay tập hạt giống bằng trang tin cậy và thay một vector điểm bằng cặp vector HITS.

## 3. Bằng chứng hoàn thành

- Người học tính được ít nhất một vòng PageRank theo chủ đề trên Hình 5.15 và giải thích cách chọn hoặc phối hợp các vector đã tính.
- Người học suy ra công thức hạng của trang đích trong Hình 5.16, phân biệt đẳng thức chính xác với xấp xỉ và kiểm được Ví dụ 5.11.
- Người học đặc tả TrustRank, tính một dòng khối lượng rác trong Hình 5.17 và nêu vì sao tỷ số này không phải xác suất.
- Người học chạy hai vòng HITS trên Hình 5.18–5.20, nêu bất biến chuẩn hóa, nhánh vector 0, điều kiện dừng, giới hạn hội tụ và chi phí mỗi vòng.
- Người học chọn đúng mô hình từ phạm vi đồ thị, tín hiệu dịch chuyển, đầu ra và chi phí.
- Ba bài MMDS 5.3.1, 5.4.2 và 5.5.1 giữ nguyên dữ kiện, yêu cầu và có hướng dẫn hoặc lời giải kiểm được.
- Markdown, công thức, SVG, liên kết, bàn phím, màn hình rộng, màn hình hẹp, bản in và các ràng buộc an toàn của viewer đều qua kiểm định trước khi cập nhật index.

## 4. Đầu ra

- `2627-1/materials/lec-04/lecture-note.md`.
- Các cập nhật liên quan đến ghi chú trong `2627-1/planning/lec-04/outline.md`, `storyboard.md` và `review-log.md`.
- Chỉ tạo thêm SVG trong `2627-1/img/lec-04/` nếu ghi chú thực sự cần; ưu tiên sáu SVG đã có.
- Một liên kết ghi chú đúng mẫu trong `2627-1/index.html`, chỉ thêm sau khi viewer đạt mọi cổng.
- Không sửa nội dung deck trừ khi phát hiện thay đổi dùng chung về ký hiệu, giả thiết, ví dụ, kết luận hoặc thứ tự khái niệm; nếu có, ghi tác động trước khi sửa.

## 5. Đối tượng và tiên quyết

Sinh viên đại học đã học lập trình, toán rời rạc, đại số tuyến tính và xác suất cơ bản; đã hoàn thành Bài 03. Ghi chú được phép dùng lại $G=(V,E)$, $n=|V|$, $m_G=|E|$, ma trận chuyển cột $P$ đã xử lý nút cụt, $0<\beta<1$, vector xác suất, phép nhân ma trận–vector thưa và chuẩn $L_1$, nhưng phải nhắc ngắn ý nghĩa trước lần dùng quyết định.

## 6. Phạm vi nguồn

- Bản đồ học phần: `sources/source.md`, mục Bài 04.
- Ánh xạ slide: `sources/reference-slides/README.md`, dòng Bài 04.
- Nguồn trục: *Mining of Massive Datasets*, ấn bản 3, Chương 5, §5.3–5.5; Ví dụ 5.9–5.15; Hình 5.15–5.20; Bài 5.3.1, 5.4.2 và 5.5.1.
- Slide chính thức MMDS `ch05-linkanalysis1.pdf` để nối ký hiệu Bài 03 và `ch05-linkanalysis2.pdf` cho nội dung chính.
- Stanford CS246 `10-spam.pdf` chỉ để đối chiếu từng cụm; ưu tiên MMDS khi tương đương. Stanford được dùng cho sơ đồ spam rõ hơn và cách hiện số hạng nhỏ trước khi xấp xỉ; không dùng để mở rộng sang Pixie hay biến thể ngoài phạm vi.
- Deck, planning và sáu SVG Bài 04 hiện có là nguồn đồng bộ sản phẩm, không thay giáo trình làm căn cứ học thuật.
- Phải ghi rõ phần làm chặt của học phần: $S,T\ne\varnothing$, điều kiện $r_p>0$, đặc tả dừng và nhánh suy biến HITS, cùng điều kiện hội tụ theo hướng riêng trội.

## 7. Bản đồ chủ đề

| `note-topic-id` | Nhãn | Chủ đề, nguồn và sản phẩm | Chuỗi trình bày và kết nối |
|---|---|---|---|
| `L04-N01` | cầu nối | Từ PageRank cơ sở đến ba giới hạn mới; Bài 03, MMDS §5.3 và §5.5. Sản phẩm: bảng ký hiệu phân biệt $P$ cột nguồn với $L$ hàng nguồn, $m_G$ với $N,q$. | Vai trò → đặc tả ký hiệu → lỗi dễ mắc. Ví dụ, định lý, thuật toán và chứng minh không áp dụng vì đây là mục khôi phục tiên quyết. Đầu ra cấp ký hiệu cho `L04-N02`–`L04-N06`. |
| `L04-N02` | cốt lõi | PageRank theo chủ đề; MMDS §5.3.1–5.3.3, Hình 5.15, Ví dụ 5.10. Sản phẩm: dựng $q_S$, chạy tay một vòng, giải thích chọn/phối hợp $k$ vector và chi phí lưu trữ. | Vai trò → $S,e_S,q_S$ → ví dụ Hình 5.15 → ý nghĩa dịch chuyển → phép lặp và lập luận co $L_1$ kế thừa Bài 03 → ứng dụng, chi phí, kiểm tra. Dẫn sang khả năng thao túng cấu trúc ở `L04-N03`. |
| `L04-N03` | cốt lõi | Cụm thao túng liên kết; MMDS §5.4.1–5.4.2, Hình 5.16, Ví dụ 5.11. Sản phẩm: theo luồng hạng, lập phương trình, giải dạng chính xác rồi chỉ ra điều kiện xấp xỉ. | Nhu cầu → ba vùng trang và $N,q,x,y$ → ví dụ luồng qua một trang hỗ trợ → trực quan vòng phản hồi → suy dẫn đại số → kiểm số và sai số. Không gọi suy dẫn đại số là định lý. Dẫn sang `L04-N04`. |
| `L04-N04` | cốt lõi | TrustRank và khối lượng rác; MMDS §5.4.3–5.4.5, Hình 5.17, Ví dụ 5.12. Sản phẩm: đặc tả $q_T$, phép lặp, cách chọn hạt giống, tính $s_p$ và giới hạn diễn giải. | Vai trò → $T,q_T,t,r_p,s_p$ → kiểm một dòng bảng → trực quan “thiếu phần tin cậy” → thuật toán kế thừa PageRank theo chủ đề → ứng dụng, giá trị âm, chia cho 0 và kiểm tra. Không có chứng minh mới; lý do ghi rõ. Dẫn từ một điểm sang hai vai trò ở `L04-N05`. |
| `L04-N05` | cốt lõi | HITS; MMDS §5.5.1–5.5.2, Hình 5.18–5.20, Ví dụ 5.13–5.15. Sản phẩm: chạy tổng trên cạnh rồi hai vòng ma trận, đặc tả giả mã, dừng, suy biến, dạng trị riêng, điều kiện hội tụ và chi phí. | Vai trò → đồ thị con và $L,h,a$ → ví dụ chạy tay → trực quan khuếch đại hai phía → mệnh đề cập nhật và dạng trị riêng → thuật toán thưa → lập luận đúng/điều kiện hội tụ được dán nhãn làm chặt → ứng dụng, lỗi chiều ma trận, kiểm tra. Dẫn sang so sánh `L04-N06`. |
| `L04-N06` | cốt lõi | So sánh PageRank theo chủ đề, TrustRank, khối lượng rác và HITS; tổng hợp MMDS §5.3–5.5. Sản phẩm: bảng chọn mô hình theo đồ thị, tín hiệu, đầu ra, bảo đảm và chi phí. | Vai trò → tiêu chí → ví dụ chọn mô hình → trực quan một điểm/hai vai trò → kết luận so sánh → lỗi đánh đồng và tự kiểm. Định lý, thuật toán và chứng minh không áp dụng vì đây là mục tổng hợp. |
| `L04-N07` | cầu nối | Bài tập nguồn 5.3.1, 5.4.2, 5.5.1. Sản phẩm: lời giải hoặc hướng dẫn chấm truy nguyên được, dùng đúng Hình 5.15 và Hình 5.1 trung tính. | Đặc tả đề → vết tính → kết quả → lỗi dễ mắc. Phần vai trò, trực quan và lập luận được gộp vào từng lời giải vì bài tập trực tiếp đo `L04-N02`, `L04-N04`, `L04-N05`. Đầu ra chốt bài và nối sang Bài 05. |

## 8. Chủ đề bổ sung đề xuất

- `L04-S01` — **bổ sung, giữ rất ngắn**: DMOZ và 16 chủ đề từ MMDS Ví dụ 5.9, chỉ làm ví dụ về tập dịch chuyển được chuẩn bị trước. Không dùng như dữ kiện hiện thời và không phát triển thành lịch sử công cụ tìm kiếm.
- `L04-S02` — **bổ sung, giữ một đoạn nối**: sự thích nghi qua lại giữa người thao túng và bộ máy tìm kiếm trong MMDS §5.4.3. Chỉ giải thích vì sao chống spam không dừng ở nhận diện một mẫu Hình 5.16; không dạy thêm biến thể spam farm.
- Không nhận đề xuất về Ask, nhận định “PageRank hiện nay thực chất là TrustRank”, bài gốc HITS/TrustRank hoặc lời giải đóng đầy đủ của Ví dụ 5.15: chúng không cần để đạt sản phẩm học tập hoặc thiếu vị trí trong phạm vi đã khóa. Có thể ghi liên kết đọc thêm chỉ khi nguồn học phần đã cung cấp trực tiếp.

## 9. Khuôn trình bày

Mỗi chủ đề cốt lõi theo thứ tự: vai trò và nhu cầu; định nghĩa hoặc đặc tả; ví dụ chạy tay; ý nghĩa trực quan; mệnh đề hoặc thuật toán; chứng minh hay lập luận đúng; ứng dụng, lỗi dễ mắc và kiểm tra. Dùng cùng dữ kiện từ ví dụ sang công thức, giả mã và chi phí. Tách rõ “nguồn phát biểu”, “suy ra từ công thức nguồn” và “điều kiện làm chặt của học phần”. Công thức Markdown chỉ dùng `$...$` và `$$...$$`; khối `hint` và `solution` không lồng nhau. Văn phong thuần Việt, trực tiếp, không chứa hướng dẫn quy trình sản xuất tài liệu.

## 10. Ngoài phạm vi

- Phân loại chủ đề bằng Jaccard trong MMDS §5.3.4; nội dung này thuộc Bài 05.
- Pixie, SimRank, Random Walk with Restarts, API, cài đặt phân tán và hướng dẫn cụm.
- Dựng $LL^T$ hoặc $L^TL$ thành ma trận đặc để cài đặt.
- Các bài MMDS 5.4.1, 5.4.3, 5.5.2 và dữ kiện tự tạo thay cho ba bài đã chọn.
- Số liệu tỷ lệ spam không có dẫn nguồn trực tiếp; nhận định lịch sử hay hiện trạng công cụ tìm kiếm không cần cho mục tiêu.

## 11. Rủi ro và điểm cần duyệt

- Công thức spam farm: phải hiện số hạng dịch chuyển trực tiếp trước khi nêu xấp xỉ; không trình bày xấp xỉ như đẳng thức. Dùng $N,q$ để không đè $n,m_G$.
- Hình 5.17 dùng hai thiết lập nguồn khác nhau; phải ghi rõ trước khi so số. Khối lượng rác có thể âm và không phải xác suất.
- HITS có khác biệt nguồn về khởi tạo và chuẩn hóa; ghi chú theo deck: $h^{(0)}=e$, chuẩn vô cùng. Điều kiện dừng và hội tụ là phần làm chặt, không gán cho MMDS.
- $P$ và $L$ dùng quy ước chiều khác nhau; mọi bảng vết phải kiểm lại bằng phép tính độc lập.
- Chỉ dùng `img/lec-04/...` trong Markdown và `lecture-04-pagerank-theo-chu-de-lien-ket-rac-va-hits.html` cho liên kết deck.
- Nếu năm reviewer phát hiện thay đổi ảnh hưởng ký hiệu, giả thiết, ví dụ, kết luận hoặc thứ tự dùng chung, phải rà deck và ghi quyết định trong `review-log.md`.

## 12. Kế hoạch tác tử

1. Đã chạy độc lập reader lập kế hoạch, reader ánh xạ nguồn và reviewer bản đồ chủ đề bằng `z-ai/glm-5.3-flash`; Codex chính đã đối chiếu và hợp nhất goal.
2. Writer `deepseek/deepseek-v4-flash-0731` soạn một tệp ghi chú trên hồ sơ đã lọc, không nhận bí mật hoặc thông tin xác thực.
3. Năm reviewer GLM độc lập kiểm: nguồn/phạm vi; toán và thuật toán; mạch sư phạm; thuật ngữ–ký hiệu–liên tục; viewer và khả năng tiếp cận.
4. Codex chính chỉ áp dụng các sửa có căn cứ đã được phê duyệt, rồi chạy GLM tái kiểm.
5. Dùng `$no-ai-slop` biên tập bản cuối và tự kiểm theo `eval.md`; dùng `$quill` rà dàn ý, mạch, thuật ngữ và ký hiệu, không tạo `quill.json`.
6. Kiểm định viewer ở màn hình rộng/hẹp, bàn phím, bản in, công thức, SVG, liên kết và từ chối đường dẫn không hợp lệ. Chỉ sau đó cập nhật index, commit, push và kiểm SHA trên `origin/main`.

## 13. Trạng thái

**Sẵn sàng soạn.** Ba vai GLM đã đọc trực tiếp trích đoạn MMDS §5.3–5.5, slide MMDS/Stanford, planning hiện có và ba đề bài 5.3.1, 5.4.2, 5.5.1. Không còn thiếu nguồn làm thay đổi đáng kể kết quả; mọi bổ sung được giữ ở mức có căn cứ và đã tách khỏi phát biểu của MMDS.
