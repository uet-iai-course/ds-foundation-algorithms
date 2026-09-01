# Goal ghi chú Bài 12

## 1. Goal

Hoàn thiện ghi chú tự học **Bài 12 — Mô hình I/O và sắp xếp ngoài bộ nhớ** tại `2627-1/materials/lec-12/lecture-note.md`. Tài liệu phải giúp sinh viên chuyển từ tệp không vừa RAM sang mô hình khối–khung, chạy và chứng minh sắp xếp trộn ngoài, tính chi phí theo điều kiện đầu ra, rồi đánh giá hai cách giảm số lượt: đổi hệ số trộn và tạo dãy dài hơn.

## 2. Vấn đề trung tâm

Khi dữ liệu không vừa bộ nhớ chính, thời gian CPU không còn đủ để mô tả chi phí. Thuật toán phải tổ chức truy cập theo khối, giới hạn trạng thái bằng số khung, tạo các dãy đã sắp và trộn chúng qua nhiều lượt. Điều kiện sau—ghi thành tệp hay truyền trực tiếp—quyết định lần ghi cuối có được tính hay không.

## 3. Bằng chứng hoàn thành

- Người học phân biệt bản ghi, khối, khung; giải thích trúng/trượt đệm, khối bẩn và sự khác nhau giữa lần truyền khối với lần định vị.
- Người học đặc tả External Merge Sort, xử lý đúng $N=0$, $0<N\le B$ và $N>B$, rồi tạo dãy ban đầu với $r_0=\lceil N/B\rceil$.
- Người học trộn $k=B-1$ dãy bằng đầu dãy nhỏ nhất, nêu bất biến, điều kiện dừng và chứng minh đầu ra đúng đa tập, có khóa không giảm.
- Người học tính $p=\lceil\log_k r_0\rceil$, $C_{\mathrm{mat}}$, $C_{\mathrm{pipe}}$ và giải thích giả thiết của từng công thức.
- Người học tách chi phí truyền khối, seek, CPU và bộ nhớ; phân tích đánh đổi khi cấp nhiều khung cho mỗi dãy.
- Người học chạy Replacement Selection bằng trạng thái hoạt động/đóng băng, tách $H$ khỏi $B$ và không biến nhận định trung bình khoảng $2H$ thành bảo đảm.
- Ba bài recitation 15.1, 15.9 và 13.5 giữ nguyên dữ kiện, yêu cầu và đáp án nguồn.
- Viewer, Markdown, KaTeX, SVG, liên kết, bàn phím, màn hình rộng/hẹp, bản in và an toàn đường dẫn đều đạt trước khi cập nhật index.

## 4. Đầu ra

- `2627-1/materials/lec-12/lecture-note.md`.
- Cập nhật phần ghi chú trong `2627-1/planning/lec-12/{outline,storyboard,review-log}.md`.
- Dùng tám SVG hiện có trong `2627-1/img/lec-12/`.
- Thêm liên kết ghi chú Bài 12 vào `2627-1/index.html` sau khi viewer đạt.
- Không sửa deck trừ khi phát hiện lỗi nội dung dùng chung cần đồng bộ.

## 5. Nguồn và quyết định chọn nguồn

- *Database System Concepts* 7e, Chương 12–13 và phần sắp xếp ngoài bộ nhớ của Chương 15 là nguồn trục.
- Chương 12, trang chiếu 10–11 và 32–33 cung cấp hệ phân cấp và truy cập khối; Chương 13, trang chiếu 2–3 và 19–20 cung cấp bản ghi–khối cùng bộ quản lý đệm. Lược số liệu phần cứng có thể lỗi thời.
- Chương 15, trang chiếu 17–23 chốt hai pha External Merge Sort; trang chiếu 51–59 chốt trường hợp truyền dòng không ghi kết quả cuối.
- Wisconsin CS764, bài 2, trang 16–20 chỉ bổ sung Replacement Selection và nhận định độ dài trung bình khoảng hai lần sức chứa; không gán cho nguồn một mô hình xác suất mà nguồn không nêu.
- Recitation dùng trực tiếp Bài 15.1 (đề trang in 47; lời giải PDF 1/trang in 111), Bài 15.9 (đề PDF 2/trang in 48; lời giải PDF 5/trang in 115) và Bài 13.5 (đề PDF 2/trang in 42; lời giải PDF 5/trang in 95).
- MMDS, Stanford CS246, B+-Tree và các thuật toán Join chi tiết nằm ngoài phạm vi.

## 6. Bản đồ chủ đề

| `note-topic-id` | Nhãn | Chủ đề và sản phẩm | Nguồn, kết nối |
|---|---|---|---|
| `L12-N01` | cốt lõi | Tình huống `ORDER BY`, đầu vào–đầu ra và giới hạn RAM | `source.md`; Ch.15.17; mở mô hình I/O |
| `L12-N02` | cầu nối | Hệ phân cấp, bản ghi, khối và khung | Ch.12.10–11; Ch.13.2–3; trao đơn vị cho N03 |
| `L12-N03` | cốt lõi | Bộ quản lý đệm và hai thước đo I/O | Ch.12.32–33; Ch.13.19–20; trao chi phí cho N04 |
| `L12-N04` | cốt lõi | Đặc tả External Merge Sort và tạo dãy ban đầu | Ch.15.17–19; Bài 15.1; tạo $r_0$ cho N05 |
| `L12-N05` | cốt lõi | Trộn nhiều đường, bất biến, dừng và tính đúng | Ch.15.20–21; dùng bốn dãy của N04 |
| `L12-N06` | cốt lõi | Số lượt và cây trộn | Ch.15.21–22; tạo $p$ cho N07 |
| `L12-N07` | cốt lõi | Vật chất hóa, truyền dòng và chi phí | Ch.15.22, 51–59; tạo động cơ tối ưu N08–N09 |
| `L12-N08` | cốt lõi | Truyền khối, seek, CPU, bộ nhớ và đệm dài | Ch.15.22–23; Bài 15.9; đổi fan-in lấy seek |
| `L12-N09` | cốt lõi | Replacement Selection: trạng thái và vết chạy | Wisconsin 16–20; giảm $r_0$ từ phía tạo dãy |
| `L12-N10` | cốt lõi | Replacement Selection: đúng, dừng, chi phí và giới hạn $2H$ | Wisconsin 16–20; đóng nhánh tạo dãy dài |
| `L12-N11` | cầu nối | Tổng hợp $B\to(r_0,k)\to p\to C$ và chọn đầu ra | Tổng hợp N01–N10; thu hồi `ORDER BY` |
| `L12-N12` | cốt lõi | Ba bài nguồn 15.1, 15.9, 13.5 có lời giải | Các Practice Exercises/Solutions đã ánh xạ |

Đồ thị tiên quyết: `N01→N02→N03→N04→N05→N06→N07`; từ N07 tách thành `N08` (đổi $k$) và `N09→N10` (giảm $r_0$), hội tụ ở `N11→N12`. Không có chủ đề ngoài nguồn. Đệm dài và biến thể ba khung là cốt lõi vì prompt yêu cầu trực tiếp, không gắn nhãn bổ sung. Nhận định $2H$ chỉ là giới hạn thực hành trong N10, không phải chủ đề đọc thêm độc lập.

## 7. Ký hiệu và hợp đồng phải giữ

- $n$ là số bản ghi, $b$ là số bản ghi mỗi khối và $N=\lceil n/b\rceil$ là số khối.
- $B$ là tổng số khung đệm; mô hình chung dành một khung đầu ra nên $k=B-1$.
- $r_0=\lceil N/B\rceil$ cho tạo dãy theo mẻ; $p=\lceil\log_k r_0\rceil$ chỉ dùng khi $N>B$ và $k\ge2$.
- $H$ là số bản ghi vừa vùng heap của Replacement Selection. Chỉ trong vết một bản ghi/khối mới có cùng giá trị số $H=B=3$.
- $b_b\in\mathbb{Z}$, $b_b\ge1$ là số khung cho mỗi dãy đầu vào trong biến thể đệm dài.
- Dãy đã sắp là đoạn có khóa không giảm. Khóa trùng vẫn đúng; muốn ổn định phải dùng vị trí gốc làm khóa phụ.
- Vật chất hóa ghi tệp cuối; truyền dòng cấp kết quả cho toán tử nhận và không tính chi phí của toán tử đó.

## 8. Giá trị và lập luận phải tính lại

- Bài 15.1 có 12 bản ghi, một bản ghi/khối và bộ nhớ ba khối. Phần giảng dùng $N=12,B=3,k=2$, tạo bốn dãy: `[emu,kangaroo,wallaby]`, `[lion,platypus,wombat]`, `[meerkat,warthog,zebra]`, `[baboon,hornbill,hyena]`.
- Cây trộn chung là $4\to2\to1$, nên $p=2$. Theo quy ước vật chất hóa mọi lượt, $C_{\mathrm{mat}}=2N(1+p)=72$; nếu truyền dòng ở lượt cuối, $C_{\mathrm{pipe}}=N(2p+1)=60$.
- $C_{\mathrm{pipe}}=0$ khi $N=0$; bằng $N$ khi $0<N\le B$; bằng $N(2p+1)$ khi $p\ge1$. $C_{\mathrm{mat}}=2N(1+p)$ là cận trên nếu không sao chép nhóm chỉ có một dãy.
- Với $N=80,B=5$: $k=4,r_0=16,p=2,C_{\mathrm{mat}}=480$.
- Với một khung đầu ra, $k=\lfloor(B-1)/b_b\rfloor$; nếu đầu ra cũng dùng $b_b$ khung, $k=\lfloor B/b_b\rfloor-1$. Đây là suy ra từ phân bổ khung; nguồn Bài 15.9 chỉ nêu đánh đổi định tính. Với $B=11,b_b=2$, hai giá trị là 5 và 4.
- Replacement Selection với $H=3$ trên 12 tên tạo ba dãy: `[emu,kangaroo,platypus,wallaby,warthog,wombat,zebra]`, `[hyena,lion,meerkat]`, `[baboon,hornbill]`.
- Biến thể nguồn của lời giải 15.1 trộn ba dãy bằng ba khung vì một bản ghi lấp đầy một khối: xuất đầu nhỏ nhất làm rỗng khung, ghi ngay khối đầu ra đầy rồi nạp đầu kế của chính dãy. Không khái quát thành $k=B$.
- Bài 13.5 chọn bảng băm từ mã khối đến vị trí khung; băm đến xô rồi tìm tuyến tính trong xô hoặc dùng cách xử lý va chạm tương đương.

## 9. Rủi ro và điểm cần duyệt

- Không trộn $B$ theo khung với $H$ theo bản ghi.
- Không dùng $p=\lceil\log_k r_0\rceil$ khi $k<2$ hoặc $N\le B$.
- Không gộp lần truyền khối với seek; cùng số lần truyền có thể có số lần định vị khác nhau.
- Không trình bày $C_{\mathrm{mat}}$ như chi phí chính xác nếu triển khai bỏ sao chép nhóm một dãy.
- Không biến hai công thức đệm dài thành phát biểu nguyên văn của Bài 15.9.
- Không trình bày độ dài trung bình khoảng $2H$ như định lý hay bảo đảm trường hợp xấu.
- Không biến lịch ba khung của lời giải 15.1 thành thuật toán trộn chung.
- Không đưa mã trang, thời lượng, worker, reviewer, prompt, goal, rubric hoặc quy trình sản xuất vào ghi chú công khai.

## 10. Kế hoạch tác tử

1. Ba reader `z-ai/glm-5.3-flash` qua OpenRouter lập kế hoạch, ánh xạ nguồn và đề xuất chủ đề độc lập.
2. Codex chính hợp nhất và duyệt goal trước writer.
3. Một writer `deepseek/deepseek-v4-flash-0731` soạn trong gốc tạm hẹp.
4. Năm reviewer `z-ai/glm-5.3-flash` kiểm nguồn, toán–thuật toán, mạch sư phạm, tính liên tục và viewer.
5. Codex chính áp dụng sửa có căn cứ; hai reviewer GLM tái kiểm toán–thuật toán và mạch.
6. Dùng `$no-ai-slop` và `$quill`, không tạo `quill.json`; kiểm viewer thật, rồi mới cập nhật index, commit, push và xác minh SHA.

## 11. Trạng thái

**Hoàn tất.** Reader kế hoạch phiên `27292`, reader nguồn phiên `53056` và reader bản đồ chủ đề phiên `87725` đều dùng `z-ai/glm-5.3-flash` qua OpenRouter. Writer `deepseek/deepseek-v4-flash-0731` tạo bản nháp qua các phiên `44749`, `42398`, `30279`, `88884`, `35136`; Codex chính hợp nhất các phần hợp lệ và sửa theo năm báo cáo độc lập. Năm reviewer GLM phiên `64754`, `75649`, `52013`, `68655`, `72287` đều đạt sau xử lý các góp ý có căn cứ; tái kiểm toán–thuật toán phiên `55540` và mạch viết phiên `61765` đều `PASS`. Bản cuối đã qua `$no-ai-slop`, rà liên tục bằng `$quill`, kiểm tĩnh, Chromium rộng/hẹp, bàn phím, bản in, an toàn đường dẫn và liên kết index. Không tạo `quill.json`; không gửi `.env`, bí mật hoặc thông tin xác thực tới worker.
