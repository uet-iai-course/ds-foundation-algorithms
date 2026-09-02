# Prompt đồng bộ deck Bài 12

Thực hiện theo `AGENTS.md` để đồng bộ `2627-1/lecture-12-mo-hinh-io-va-sap-xep-ngoai-bo-nho.html` với ghi chú đã phát hành, planning và nguồn Bài 12. Đây là sửa hẹp deck hiện có; không đổi phạm vi, ví dụ, công thức, recitation hoặc cấu trúc bài.

## Quyết định đầu vào

- Bài theo thứ tự đề xuất: **12 — Mô hình I/O và sắp xếp ngoài bộ nhớ**.
- Giữ 53 slide, 53 `data-slide-id`, 53 speaker notes, 7 section ngoài, 46 slide giảng + 7 slide recitation, 120+60 phút và 8 SVG.
- Giữ mạch khối–khung và mô hình I/O → External Merge Sort → vật chất hóa/truyền dòng → Replacement Selection → tổng hợp và ba bài nguồn.
- Giữ đúng ký hiệu: $n$ là số bản ghi, $N$ là số khối, $B$ là tổng số khung, $k=B-1$, $r_0$ là số dãy ban đầu, $p$ là số lượt trộn, $H$ là sức chứa heap và $b_b$ là số khung cho một dãy.
- Giữ các trường hợp biên $N=0$, $0<N\le B$, điều kiện $B\ge3$ khi $N>B$ và phân biệt lần truyền khối với lần định vị.
- Giữ mốc Bài 13.5: đề PDF trang 2/trang in 42; lời giải PDF trang 5/trang in 95. Nhận xét đổi trang 5 thành trang 3 là false positive đã bị bác sau kiểm tra trực tiếp PDF.

## Sửa đã có bằng chứng

- Trong mục Bài 12 của `2627-1/index.html`, đổi nhãn `Trang chiếu` thành `Bài giảng` và `Ghi chú` thành `Ghi chú bài giảng`. Không đổi URL.
- Biên tập speaker notes của P00, P01, P02, I06, I07, S06, S11, S15, S16, R00, T01 và X01 bằng `$no-ai-slop`: bỏ giọng quy trình, nhãn nội bộ, câu mô tả việc biên tập và lời dẫn kiểu checklist; giữ nguồn, giả thiết, lập luận, đáp án, chuyển ý sư phạm và dữ kiện.
- Dùng `$quill` để rà thứ tự khái niệm, thuật ngữ, ký hiệu và câu nối. Không tạo `quill.json`.
- Không sửa nội dung hiển thị, công thức, thuật toán, chứng minh, note công khai, planning hoặc SVG nếu không phát hiện lỗi cụ thể trong diff writer.

## Nguồn và kiểm định phải giữ

- *Database System Concepts* 7e, Chương 12–13 và trang chiếu 17–23, 51–59 của Chương 15 là trục.
- Wisconsin CS764, bài 2, trang 16–20 chỉ bổ sung Replacement Selection; nhận định độ dài trung bình khoảng $2H$ không phải bảo đảm.
- Recitation giữ nguyên Bài 15.1, 15.9 và 13.5. Biến thể ba khung của lời giải 15.1 không được khái quát thành $k=B$.
- Sau writer: Codex chính kiểm diff rồi mới áp dụng; tiếp theo phải có năm reviewer độc lập, hai recheck, kiểm tĩnh, Chromium, viewer, index và Codex Slides trước commit/push.

## Hệ thống tác tử

- Reader/reviewer: `z-ai/glm-5.3-flash` qua OpenRouter.
- Writer: `deepseek/deepseek-v4-flash-0731` qua OpenRouter trong dossier tạm hẹp.
- Chỉ chấp nhận kết quả `--json` khi `requested_model`, `observed_model` và `provider` khớp.
- Không đọc hoặc gửi `.env`, khóa, token, mật khẩu, cookie, khóa riêng hay thông tin xác thực cho worker.
