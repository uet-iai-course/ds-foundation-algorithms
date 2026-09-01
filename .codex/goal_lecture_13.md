# Goal ghi chú Bài 13

## 1. Goal

Hoàn thiện ghi chú tự học **Bài 13 — Chỉ mục truyền thống và băm tĩnh** tại `2627-1/materials/lec-13/lecture-note.md`. Tài liệu phải giúp sinh viên chọn cấu trúc theo loại truy vấn, chạy đúng B+-Tree và băm tĩnh, dùng Bitmap Index với mặt nạ hợp lệ, rồi phân tích I/O, cập nhật và dung lượng.

## 2. Vấn đề trung tâm

Một quan hệ lớn không vừa bộ nhớ phải phục vụ truy vấn điểm, khoảng và tổ hợp bộ lọc mà không quét toàn bộ $N$ khối. Chỉ mục giảm khối phải đọc nhưng tiêu tốn dung lượng và chi phí cập nhật; không có một cấu trúc tốt nhất cho mọi dạng truy vấn.

## 3. Bằng chứng hoàn thành

- Người học phân biệt khóa tìm kiếm, mục lá, RID và dữ liệu; chọn B+-Tree, B-Tree, băm tĩnh hoặc bitmap theo loại truy vấn.
- Người học tìm điểm, quét khoảng và tính chi phí $d+1+J+D$ hoặc $d+1+L+J+D$ với đúng giả thiết.
- Người học chạy chèn, tách lá/nút trong, xóa, mượn, gộp và co gốc; nêu bất biến thứ tự, sức chứa và đồng độ sâu lá.
- Người học chạy băm tĩnh qua ngăn nhà và chuỗi tràn, phân biệt truy vấn bằng với khoảng, giải thích hệ số tải và trường hợp xấu.
- Người học dựng bitmap, thực hiện phép Boolean, chặn vị trí đã xóa và NULL trong phép NOT, rồi lọc điều kiện dư trên bản ghi thật.
- Bốn bài recitation 14.1, 14.3(b), 14.4 và 14.13 giữ nguyên dữ kiện và yêu cầu nguồn.
- Viewer, Markdown, KaTeX, SVG, liên kết, bàn phím, màn hình rộng/hẹp, bản in và an toàn đường dẫn đều đạt trước khi cập nhật index.

## 4. Đầu ra

- `2627-1/materials/lec-13/lecture-note.md`.
- Cập nhật phần ghi chú trong `2627-1/planning/lec-13/{outline,storyboard,review-log}.md`.
- Dùng mười SVG hiện có trong `2627-1/img/lec-13/`.
- Thêm liên kết ghi chú Bài 13 vào `2627-1/index.html` sau khi viewer đạt.
- Không sửa deck trừ khi phát hiện lỗi nội dung dùng chung cần đồng bộ.

## 5. Nguồn và quyết định chọn nguồn

- *Database System Concepts* 7e, Chương 14 là nguồn trục cho khái niệm chỉ mục, B+-Tree, B-Tree, băm tĩnh và Bitmap Index.
- Chương 24, trang chiếu 11–15 chỉ bổ sung mặt nạ tồn tại và NULL cho phép NOT trên bitmap.
- Recitation dùng Bài 14.1, 14.3(b), 14.4 trên cây của 14.3(b), 14.13 cùng lời giải chính thức đã ánh xạ trong planning.
- Sửa lỗi in trong lời giải 14.4 sau Insert 8: lá phải phải bắt đầu bằng 19, không phải 9; ghi rõ lý do bảo toàn đa tập khóa.
- MMDS, Stanford CS246, chỉ mục văn bản, chỉ mục không gian và băm động nằm ngoài phạm vi.

## 6. Bản đồ chủ đề dự kiến

| `note-topic-id` | Nhãn | Chủ đề và sản phẩm | Nguồn, kết nối |
|---|---|---|---|
| `L13-N01` | cốt lõi | Bài toán chỉ mục, giá truy vấn–cập nhật và tiêu chí chọn | Ch.14.3–16; mở các nhánh |
| `L13-N02` | cốt lõi | B+-Tree: cấu trúc, bất biến và biểu diễn khóa trùng | Ch.14.17–24; chuẩn bị tìm kiếm |
| `L13-N03` | cốt lõi | Tìm điểm, khoảng, tính đúng và I/O | Ch.14.25–28, 40; trao bất biến cho cập nhật |
| `L13-N04` | cốt lõi | Chèn và tách lá/nút trong | Ch.14.29–33; vết Bài 14.4 |
| `L13-N05` | cốt lõi | Xóa, phân phối lại, gộp và co gốc | Ch.14.34–39; đóng B+-Tree |
| `L13-N06` | cầu nối | B-Tree đối chiếu với B+-Tree | Ch.14.46–48; bỏ thứ tự để sang băm |
| `L13-N07` | cốt lõi | Băm tĩnh, chuỗi tràn, cập nhật và chi phí | Ch.14.51–59; sang bộ lọc tập |
| `L13-N08` | cốt lõi | Bitmap cơ sở, phép Boolean và chi phí | Ch.14.71–75; Bài 14.13 |
| `L13-N09` | cốt lõi | Bitmap với vị trí xóa, NULL và NOT | Ch.24.11–15; đóng điều kiện biên |
| `L13-N10` | cầu nối | Ma trận chọn cấu trúc theo truy vấn, I/O, cập nhật, dung lượng | Tổng hợp N01–N09 |
| `L13-N11` | cốt lõi | Bốn bài nguồn có lời giải | Bài 14.1, 14.3(b), 14.4, 14.13 |

Đồ thị tiên quyết: `N01→N02→N03→N04→N05→N06→N07→N08→N09→N10→N11`. Codex chính giữ 11 chủ đề sau khi hợp nhất ba reader. Nhắc tiên quyết được gộp vào N01; không thêm bảng lỗi riêng vì các lỗi phải nằm cạnh thuật toán tương ứng; không thêm mục đọc thêm về các bài ngoài phạm vi.

## 7. Ký hiệu và hợp đồng phải giữ

- $m$ là số con tối đa của nút trong; lá có tối đa $m-1$ khóa. $f=\lceil m/2\rceil$ là cận dưới số con của nút trong không phải gốc.
- $K$ là số mục khóa trong lá; $d$ là số cạnh từ gốc đến lá; cây chỉ có gốc là lá có $d=0$.
- $L,J,D$ lần lượt là số khối lá bổ sung, khối RID-list ngoài lá và khối dữ liệu kết quả. Điểm đọc $d+1+J+D$; khoảng đọc $d+1+L+J+D$.
- $M,c,N_e,t$ dùng cho băm tĩnh; mô hình một ngăn bằng một khối, không bộ nhớ đệm.
- $R,w,q,E,V_v,V_{\mathrm{NULL}}$ dùng cho bitmap; dung lượng chưa nén tối đa $(q+2)R$ bit khi cần cả tồn tại và NULL.
- Không dùng $B$ làm biến trong bài này.

## 8. Giá trị và lập luận phải tính lại

- Bài 14.3(b), $m=6$, chèn $2,3,5,7,11,17,19,23,29,31$ cho gốc $[7,19]$ và ba lá $[2,3,5]$, $[7,11,17]$, $[19,23,29,31]$.
- Chèn 9, 10 chưa tràn; chèn 8 tách lá giữa thành $[7,8,9]$ và $[10,11,17]$, sao chép 10 lên gốc $[7,10,19]$. Lá phải vẫn là $[19,23,29,31]$.
- Xóa 23 để lại $[19,29,31]$; xóa 19 gây thiếu, gộp với $[10,11,17]$, gốc còn $[7,10]$.
- Vết bitmap 12 hàng: $S_1=001000000000$, $S_2=000000000000$, $S_3=100010010000$, $S_4=010101101111$; `Finance` $=010000001000$; phép AND cho hai ứng viên Wu và Singh, rồi phải lọc lại lương từ 80.000.
- Hệ số tải $\alpha=N_e/(Mc)$ và chi phí $1+t+D$ là dẫn xuất của bài giảng trong mô hình đã nêu, không phải công thức trích nguyên văn tại các trang nguồn.

## 9. Rủi ro và điểm cần duyệt

- Không áp cận sức chứa nút thường cho gốc.
- Không trộn sao chép khóa phân cách khi tách lá với đẩy khóa khi tách nút trong.
- Không xóa mục khóa có RID-list nếu danh sách vẫn còn RID.
- Không bỏ $J$ khi RID-list nằm ngoài lá; không bỏ $D$ khi phải đọc bản ghi thật.
- Không tuyên bố băm tĩnh hỗ trợ truy vấn khoảng hiệu quả hoặc bảo đảm hằng số trong trường hợp xấu.
- Không dùng phép NOT bitmap mà thiếu $E$ và $V_{\mathrm{NULL}}$ khi chúng có ý nghĩa.
- Không đưa mã trang, thời lượng, worker, reviewer, prompt, goal, rubric hoặc quy trình sản xuất vào ghi chú công khai.

## 10. Kế hoạch tác tử

1. Ba reader `z-ai/glm-5.3-flash` qua OpenRouter lập kế hoạch, ánh xạ nguồn và đề xuất chủ đề độc lập.
2. Codex chính hợp nhất và duyệt goal trước writer.
3. Một writer `deepseek/deepseek-v4-flash-0731` soạn trong gốc tạm hẹp.
4. Năm reviewer `z-ai/glm-5.3-flash` kiểm nguồn, toán–thuật toán, mạch sư phạm, tính liên tục và viewer.
5. Codex chính áp dụng sửa có căn cứ; hai reviewer GLM tái kiểm toán–thuật toán và mạch.
6. Dùng `$no-ai-slop` và `$quill`, không tạo `quill.json`; kiểm viewer thật, rồi mới cập nhật index, commit, push và xác minh SHA.

## 11. Trạng thái

**Hoàn tất.** Reader kế hoạch phiên `11965`, reader nguồn phiên `31332` và reader bản đồ chủ đề phiên `78833` dùng `z-ai/glm-5.3-flash` qua OpenRouter. Writer `deepseek/deepseek-v4-flash-0731` phiên `94655` tạo bản nháp rồi chạm giới hạn công cụ sau khi đã ghi tệp; Codex chính kiểm và sửa các lỗi có căn cứ. Năm reviewer GLM gồm nguồn `60597`, toán–thuật toán `29726`, sư phạm `81489`, mạch `64599`, viewer `42582`; tái kiểm toán `8408` và mạch `73590` đều `PASS`. Bản cuối đã qua `$no-ai-slop`, `$quill`, kiểm tĩnh, Chromium rộng/hẹp, bàn phím, bản in, an toàn đường dẫn và liên kết index. Không tạo `quill.json`; không gửi `.env`, bí mật hoặc thông tin xác thực tới worker.
