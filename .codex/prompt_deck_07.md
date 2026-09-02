# Prompt đồng bộ deck Bài 07

Thực hiện theo `AGENTS.md` để đồng bộ `2627-1/lecture-07-chi-muc-hang-xom-gan-dung.html` với `2627-1/materials/lec-07/lecture-note.md` và nguồn Bài 07. Đây là sửa hẹp deck hiện có.

## Quyết định đầu vào

- Bài theo thứ tự đề xuất: **07 — Chỉ mục hàng xóm gần đúng**.
- Giữ 47 slide, 47 `data-slide-id`, 47 speaker notes, 7 section ngoài, 38 slide giảng + 9 slide thực hành, 120+60 phút và 9 SVG.
- Giữ các cụm LSH cầu nối, ANN/recall, HNSW, VQ/PQ/ADC, IVF-PQ, kết luận và ba nhiệm vụ notebook. Không thêm bài tập HNSW vì nguồn thực hành không có nhiệm vụ trực tiếp.
- Dùng `$no-ai-slop` để bỏ câu quy trình và siêu bình luận; dùng `$quill` để rà mạch, thuật ngữ và ký hiệu; không tạo `quill.json`.

## Sửa có bằng chứng từ hai reader

- Sửa lecture note để `SEARCH-LAYER` dùng `ep` là tập điểm vào đúng bài báo gốc và deck: `V ← ep; C ← ep; W ← ep`, với `1≤|ep|≤ef`; bỏ câu sai rằng nguồn chỉ dùng một điểm vào đơn.
- Đồng bộ truy vấn dư trên deck I02/I04 thành `\widetilde q_i=q-\mu_i` như lecture note.
- Đồng bộ ví dụ VQ trong lecture note sang quy ước chỉ số tâm 0-based: tâm `c_0,…,c_{k^*-1}`, `0≤i<k^*`, điểm `y=3` nhận mã 1.
- Tách đúng R00: “PQ thủ công: ô 82–97” và “so sánh mã 6 byte: ô 98–99”.
- Đổi nhãn index Bài 07 thành “Ghi chú bài giảng”.
- Biên tập nhẹ P02, H04, H10 và các câu speaker notes mang giọng checklist; không đổi mệnh đề hoặc cấu trúc.

## Hệ thống tác tử

- Reader/reviewer: `z-ai/glm-5.3-flash` qua OpenRouter.
- Writer: `deepseek/deepseek-v4-flash-0731` qua OpenRouter trên hồ sơ tạm hẹp.
- Codex chính kiểm diff và áp dụng các sửa được reader/reviewer chấp thuận.
- Sau sửa: năm reviewer độc lập, hai recheck, kiểm tĩnh, Chromium rộng/hẹp/bàn phím/notes/in, viewer, index và Codex Slides.

Không đọc hoặc gửi `.env`, bí mật hay thông tin xác thực cho worker.
