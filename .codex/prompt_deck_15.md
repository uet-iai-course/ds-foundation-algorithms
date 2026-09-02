# Prompt hiệu chỉnh bộ trang chiếu Bài 15

Hiệu chỉnh hẹp **Bài 15 — Thuật toán kết nối dữ liệu** theo `AGENTS.md` và các kết luận reader đã được điều phối viên duyệt. Không mở rộng phạm vi, thêm nguồn hoặc thay đổi cấu trúc học tập.

## Cơ sở đã duyệt

- Reader lập kế hoạch: phiên `25176`, model `z-ai/glm-5.3-flash`, provider OpenRouter.
- Reader nguồn độc lập: phiên `84227`, cùng model và provider, kết luận `GO`.
- Kiểm kê cố định: 60 slide, 60 ghi chú diễn giả, 60 `data-slide-id` duy nhất, 7 phần ngoài, 50 slide giảng và 10 slide recitation, thời lượng 120+60 phút, 10 SVG.
- Định nghĩa, công thức, thuật toán Nested/Block/Indexed Nested, Sort-Merge, Hash trong bộ nhớ, Grace Hash, các ví dụ và Bài 15.3–15.5 đã được tính lại và đạt.

## Delta bắt buộc

Trong thẻ Bài 15 của `2627-1/index.html`, đổi nhãn `Ghi chú` thành `Ghi chú bài giảng`. Giữ nguyên nhãn `Bài giảng` và cả hai URL.

## Biên tập `$no-ai-slop` hẹp

Chỉ biên tập ghi chú diễn giả tại các slide sau; giữ nguyên dữ kiện, ký hiệu, công thức, thuật toán, kết luận và nguồn:

- `P00`: bỏ đường dẫn nội bộ `sources/source.md`; không thay bằng mô tả quy trình.
- `M00`: đổi cách nói “Deck dùng...” thành “Bài này dùng...”.
- `M01`: bỏ câu “Giảm tải ký hiệu ở đầu bài”; nêu trực tiếp nơi từng ký hiệu được định nghĩa.
- `N02`: bỏ câu nói vết này sẽ được dùng ở trang sau.
- `N08`: bỏ metadata “slide 28 bị ẩn”; vẫn dẫn slide 28 và slide 24.
- `S00`: bỏ “phần này tập trung”; nối tự nhiên từ External Merge Sort sang bước nối.
- `S08`: đổi “Deck chốt...” thành phát biểu trực tiếp về phương án bài dùng.
- `H02`: bỏ “yêu cầu hiệu chỉnh của bài”.
- `H07`: bỏ lời kể về deck và việc sửa tên; phát biểu trực tiếp quy ước $p_h$, $r_i$, $s_i$.
- `H08`: bỏ cụm “hiệu chỉnh điều kiện bộ nhớ”.
- `H09`: đổi “Deck dùng...” thành phát biểu trực tiếp về phía xây và phía dò.
- `H14`: bỏ lời kể “tham số ... đã hiệu chỉnh”; giữ nguồn và điều kiện áp dụng.
- `C04`: bỏ “Chuyển sang...”; giữ câu trả lời và nguồn bài tập.
- `X07`: bỏ “deck bổ sung...” và nói trực tiếp điều kiện cần để tránh suy kết luận chỉ từ kích thước.

Giữ nguyên slide `C03`: “Quy trình chọn thuật toán nối” là nội dung học thuật, không phải hướng dẫn sản xuất tài liệu.

Tự kiểm bản sửa theo `no-ai-slop/eval.md`. Dùng nguyên tắc `$quill` để giữ tuyến khái niệm, thuật ngữ và ký hiệu xuyên suốt; không tạo `quill.json`.

## Ràng buộc đầu ra

- Chỉ sửa các bản sao trong dossier tạm của:
  - `2627-1/lecture-15-thuat-toan-ket-noi-du-lieu.html`;
  - `2627-1/index.html`.
- Không sửa lecture note, SVG, outline, storyboard, review-log, CSS, viewer, template hoặc nguồn.
- Không đổi nội dung hiển thị của deck.
- Không đổi số slide, ID, phần ngoài, thứ tự, thời lượng, công thức, thuật toán, ví dụ, recitation hoặc đường dẫn tài sản.
- Không chèn mã quy trình, phiên worker, prompt, goal, rubric hoặc thời lượng lên mặt slide hay vào ghi chú diễn giả.
- Không commit hoặc push.

Writer phải trả danh sách tệp đã sửa và mô tả ngắn từng thay đổi. Codex chính sẽ kiểm diff trước khi quyết định áp dụng vào workspace.
