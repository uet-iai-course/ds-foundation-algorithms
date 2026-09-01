# Prompt xây dựng ghi chú Bài 13

Thực hiện đầy đủ quy trình trong `AGENTS.md` để xây dựng ghi chú tự học **Bài 13 — Chỉ mục truyền thống và băm tĩnh**. Đây là yêu cầu chỉ làm ghi chú: không viết lại deck, trừ khi thay đổi nội dung dùng chung buộc phải đồng bộ.

## Phạm vi bắt buộc

- Đọc `sources/source.md` và dòng Bài 13 trong `sources/reference-slides/README.md` trước khi chọn nội dung.
- Dùng *Database System Concepts* 7e, Chương 14 làm trục; Chương 24 chỉ bổ sung mặt nạ tồn tại và NULL cho Bitmap Index.
- Trọng tâm là B+-Tree; B-Tree chỉ dùng để đối chiếu. Phạm vi gồm tìm điểm và khoảng, chèn–tách, xóa–mượn–gộp, chiều sâu và chi phí I/O, băm tĩnh, chuỗi tràn, Bitmap Index, phép Boolean, vị trí đã xóa và NULL.
- Giữ $m,K,d,f,L,J,D,N,M,c,N_e,t,R,w,q,E,V_v,V_{\mathrm{NULL}}$ như planning; không dùng $B$ vì Bài 12 đã dùng ký hiệu này cho số khung.
- Recitation dùng trực tiếp Bài 14.1, 14.3(b), 14.4 trên cây 14.3(b) và 14.13. Không đổi dữ kiện; phải ghi rõ lời giải nguồn của Insert 8 in nhầm 9 ở lá phải và sửa thành 19 để bảo toàn đa tập khóa.
- Không khẳng định công thức hệ số tải hay $1+t+D$ là nguyên văn nguồn: đây là suy ra trong mô hình một ngăn bằng một khối, không bộ nhớ đệm.

## Tệp đầu ra

- `.codex/goal_lecture_13.md`;
- `2627-1/materials/lec-13/lecture-note.md`;
- cập nhật phần ghi chú trong `2627-1/planning/lec-13/{outline,storyboard,review-log}.md`;
- dùng mười SVG hiện có trong `2627-1/img/lec-13/`, chỉ thêm hình khi thật sự cần và có nguồn;
- cập nhật mục Bài 13 trong `2627-1/index.html` sau khi viewer đạt mọi cổng.

## Điều phối OpenRouter

1. Chạy ba reader độc lập bằng `z-ai/glm-5.3-flash` qua OpenRouter: lập kế hoạch, ánh xạ nguồn và đề xuất bản đồ chủ đề. Chúng chỉ đọc và không sửa tệp.
2. Codex chính hợp nhất, duyệt đề xuất rồi hoàn thiện goal trước khi writer bắt đầu.
3. Chạy một writer `deepseek/deepseek-v4-flash-0731` trong gốc tạm hẹp. Codex chính kiểm bản nháp trước khi đưa vào kho.
4. Chạy năm reviewer `z-ai/glm-5.3-flash` độc lập: nguồn, toán–thuật toán, mạch sư phạm, tính liên tục và viewer.
5. Codex chính áp dụng các sửa có căn cứ; chạy hai lượt `recheck` về toán–thuật toán và mạch viết.
6. Dùng `$no-ai-slop` và `$quill` cho bản cuối; không tạo `quill.json`.
7. Kiểm viewer thật ở màn hình rộng, hẹp, bàn phím, bản in, đường dẫn an toàn và liên kết từ index. Chỉ commit/push khi toàn bộ cổng đạt.

Mọi worker phải dùng `--json`; chỉ chấp nhận khi `requested_model`, `observed_model` và `provider` đúng. Người dùng cho phép gửi các tệp cần thiết tới OpenRouter, ngoại trừ `.env`, bí mật và thông tin xác thực. Nếu worker lỗi, thử lại cùng model trong phạm vi hẹp hơn; không đổi ngầm model, provider, nguồn hoặc cổng kiểm định.
