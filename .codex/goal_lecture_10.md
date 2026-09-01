# Goal ghi chú Bài 10

## 1. Goal

Hoàn thiện ghi chú tự học **Bài 10 — Nén dữ liệu không mất thông tin** tại `2627-1/materials/lec-10/lecture-note.md`. Tài liệu phải giúp sinh viên tách mô hình xác suất khỏi bộ mã, thực thi ba cơ chế trong phạm vi bài, giải thích vì sao giải mã khôi phục đúng và nêu đủ thông tin giao thức mà hai phía phải chia sẻ.

## 2. Vấn đề trung tâm

Một kho dữ liệu có phân phối ký hiệu lệch có thể được biểu diễn bằng ít bit hơn, nhưng bộ giải nén chỉ khôi phục chính xác khi biết cùng bảng chữ cái, mô hình, quy tắc tạo mã và điều kiện kết thúc. Huffman tĩnh trả chi phí đếm trước và đầu mục; Huffman thích nghi cập nhật cây đồng bộ khi chưa biết thống kê; mã số học tránh làm tròn riêng độ dài của từng ký hiệu bằng cách mã cả chuỗi thành một khoảng.

## 3. Bằng chứng hoàn thành

- Người học phân biệt trục mô hình tĩnh/cập nhật với trục bộ mã Huffman/số học và liệt kê thông tin cần cho giải mã đúng.
- Người học kiểm tra mã tiền tố, dùng bất đẳng thức Kraft như điều kiện khả thi, dựng cây Huffman cho A–E và giải thích lập luận trao đổi–co cặp cho tính tối ưu.
- Người học mô phỏng ký hiệu mới bằng `ESCAPE`, tám bit thô, lá mới trọng số 0, rồi cập nhật cây theo đúng biến thể Nelson–Gailly; phân biệt trọng số cố định của lá `ESCAPE` với trọng số ban đầu của lá ký hiệu mới.
- Người học chạy phép tăng, phát hiện vi phạm tính chất anh em, đổi nút an toàn, tiếp tục từ cha mới và giải thích điều kiện dựng lại khi chống tràn.
- Người học mã hóa và giải mã bằng khoảng nửa mở, nêu cách dừng, và giải thích ba nhánh chuẩn hóa hữu hạn cùng trạng thái bit chờ.
- Người học phân biệt tự thông tin $I(x)=-\log_2P(x)$ của một chuỗi với entropy trung bình $H(P)$; không giả định xác suất chuỗi tách thành tích nếu nguồn không nhớ chưa được nêu.
- Ba bài recitation X01–X03 giữ nguyên dữ kiện, yêu cầu và nguồn theo ngoại lệ đã được phê duyệt ngày 2026-08-28.
- Viewer, Markdown, KaTeX, SVG, liên kết, bàn phím, màn hình rộng/hẹp, bản in và an toàn đường dẫn đều đạt trước khi cập nhật index.

## 4. Đầu ra

- `2627-1/materials/lec-10/lecture-note.md`.
- Cập nhật phần ghi chú trong `2627-1/planning/lec-10/{outline,storyboard,review-log}.md`.
- Dùng chín SVG hiện có trong `2627-1/img/lec-10/`.
- Thêm liên kết ghi chú Bài 10 vào `2627-1/index.html` sau khi viewer đạt.
- Không sửa deck trừ khi phát hiện lỗi nội dung dùng chung cần đồng bộ.

## 5. Nguồn và quyết định chọn nguồn

- Nelson–Gailly, *The Data Compression Book*, Chương 3–5 là nguồn trục. Chương 3 cung cấp dữ liệu A–E và Huffman tĩnh; Chương 4 cung cấp đúng biến thể Huffman thích nghi; Chương 5 cung cấp ví dụ “BILL GATES”, kết thúc dòng, số học hữu hạn, underflow và ví dụ 100.000 số 0.
- CMU 15-499 Assignment 1a là nguồn cho bất đẳng thức Kraft và bài giải mã số học Problem 3. Stanford EE398A được dùng để đối chiếu Huffman, số học hữu hạn và phép dịch; Stanford CS106B chỉ hỗ trợ cách kể bằng cây và hàng đợi ưu tiên. Không thay dữ kiện sách bằng ví dụ Stanford.
- Chứng minh tối ưu Huffman trong ghi chú là bản triển khai phép đổi, co cặp và quy nạp từ mệnh đề tối ưu của sách cùng nguồn đối chiếu; không mô tả như chứng minh chép nguyên từ Nelson–Gailly vì sách chỉ phát biểu kết quả.
- Recitation: X01 và X02 chuyển hai ví dụ Nelson–Gailly thành bài luyện; X03 dùng nguyên CMU Assignment 1a Problem 3. Không thay X02 bằng ví dụ “AAAAAAA”.
- Ngoài phạm vi: Shannon–Fano chi tiết, mã I/O bằng C, FGK, Vitter, nút NYT, Lempel–Ziv và nén mất dữ liệu.

## 6. Bản đồ chủ đề

| `note-topic-id` | Nhãn | Chủ đề và sản phẩm | Nguồn, kết nối |
|---|---|---|---|
| `L10-N01` | cốt lõi | Bài toán khôi phục chính xác, hai trục lựa chọn và bốn nhóm thông tin giao thức | `sources/source.md`; Nelson–Gailly Ch.2–5; mở ba nhánh thuật toán |
| `L10-N02` | cốt lõi | Mã tiền tố và Kraft như miền độ dài khả thi | CMU Assignment 1a P4; nối điều kiện giải mã duy nhất sang tối ưu chi phí |
| `L10-N03` | cốt lõi | Huffman tĩnh: dựng cây, mã/giải mã, tính đúng, tối ưu và chi phí | Nelson–Gailly Ch.3, PDF tr.31–37; Stanford EE398A/CS106B đối chiếu |
| `L10-N04` | cốt lõi | Huffman thích nghi: đồng bộ, `ESCAPE`, `EOS`, ký hiệu mới và tính chất anh em | Nelson–Gailly Ch.4, PDF tr.67–74; nối nhược điểm đầu mục của N03 |
| `L10-N05` | cốt lõi | Huffman thích nghi: tăng, đổi nút, bất biến, chống tràn và dựng lại | Nelson–Gailly Ch.4, PDF tr.70–85; dùng nguyên trạng thái Hình 4.2–4.3 |
| `L10-N06` | cốt lõi | Mã số học lý tưởng bằng khoảng nửa mở, giải mã và cách dừng | Nelson–Gailly Ch.5, PDF tr.96–99; ví dụ “BILL GATES” |
| `L10-N07` | cốt lõi | Chuẩn hóa hữu hạn, tiền tố chung, underflow và bit chờ | Nelson–Gailly Ch.5, PDF tr.100–103; Stanford EE398A đối chiếu |
| `L10-N08` | cầu nối | Độ rộng khoảng, tự thông tin, entropy và chi phí | Nelson–Gailly Ch.2/5; CMU P3; nối cơ chế N07 sang so sánh |
| `L10-N09` | cốt lõi | So sánh ba cặp mô hình–bộ mã và điều kiện giao thức | Tổng hợp N03–N08; thu hồi bản đồ N01 |
| `L10-N10` | cốt lõi | Ba bài tập X01–X03 với sản phẩm và lời giải truy nguyên được | Nelson–Gailly Ch.3–4; CMU Assignment 1a P3 |

Đồ thị tiên quyết: `N01→N02→N03→N04→N05`; `N01→N06→N07→N08`; hai nhánh hội tụ ở `N09`, rồi dẫn sang `N10`. N08 được giữ làm cầu nối vì thiếu nó thì cơ chế khoảng không giải thích được số bit của một chuỗi cụ thể hoặc bài CMU.

## 7. Khuôn trình bày và ký hiệu

Mỗi thuật toán trọng tâm đi theo vai trò; đặc tả; ví dụ chạy tay; trực quan; thuật toán hoặc mệnh đề; chứng minh/lập luận; chi phí, giới hạn và tự kiểm. Công thức Markdown chỉ dùng `$...$` và `$$...$$`; khối tùy biến không lồng nhau.

- $\Sigma$ là bảng chữ cái; $f_s,p_s,\ell_s$ là tần suất, xác suất và độ dài từ mã của ký hiệu $s$.
- Mã tiền tố nghĩa là không từ mã nào là tiền tố của từ mã khác. Không đồng nhất “giải mã duy nhất” với “mã tiền tố”: mã tiền tố là điều kiện đủ thuận tiện, không phải toàn bộ lớp mã giải mã duy nhất.
- Mã số học dùng khoảng nửa mở $[L,H)$ và cận tích lũy $0\le C_s<D_s\le1$. Công thức lý tưởng là $L'=L+(H-L)C_s$, $H'=L+(H-L)D_s$.
- `ESCAPE` và `EOS` là hai lá đặc biệt có trọng số khởi tạo 1 trong cây Nelson–Gailly. Khi gặp ký hiệu mới, lá ký hiệu mới được chèn với trọng số 0 rồi cập nhật ngay. Không gọi `ESCAPE` là NYT.
- Trạng thái chuẩn hóa số học dùng `pending` khởi tạo một lần trước thông điệp và giữ xuyên các ký hiệu. Nhánh tiền tố chung phát bit cùng các bit bù đang chờ; nhánh underflow chỉ tăng `pending`.
- $I(x)=-\log_2P(x)$ là tự thông tin của chuỗi cụ thể; $H(P)=\sum_s p(s)(-\log_2p(s))$ là trung bình theo phân phối.

## 8. Giá trị và lập luận phải tính lại

- Huffman A–E: tần suất $15,7,6,6,5$; bốn lượt ghép $5+6=11$, $6+7=13$, $11+13=24$, $15+24=39$; một bảng mã của sách là A=0, B=100, C=101, D=110, E=111; tổng $87$ bit.
- Chứng minh tối ưu Huffman phải đặt $x,y$ là hai ký hiệu nhẹ nhất, $a,b$ là cặp lá anh em sâu nhất; hai phép đổi không tăng chi phí, rồi co cặp và quy nạp. Nêu quy tắc phá hòa chỉ có thể đổi mã cụ thể, không đổi chi phí tối ưu.
- Vết Huffman thích nghi X02 bắt đầu sau mũi tên: A=B=C=D=2, nút 5=nút 6=4, nút 7=8, gốc 9=18. Tăng A lên 3, đổi A với D, rồi xử lý cha mới là nút 6.
- Ví dụ “BILL GATES”: sau B là $[0.2,0.3)$, sau I là $[0.25,0.26)$, sau L là $[0.256,0.258)$; khoảng cuối theo sách là $[0.2572167752,0.2572167756)$.
- Ví dụ 100.000 số 0: $p(0)=16382/16383$, $p(\mathrm{EOS})=1/16383$; mã số học cho tệp 3 byte, so với ít nhất 12.501 byte theo ví dụ nguồn. Ghi đây là ví dụ có chủ ý, không suy rộng thành bảo đảm chung.
- CMU P3: $0.01001110110_2=0.3076171875$; giải mã bốn ký hiệu thành `caba`; các khoảng toàn cục lần lượt là $[0.3,1)$, $[0.3,0.37)$, $[0.307,0.321)$, $[0.307,0.3084)$; $P(\text{caba})=0.0014$ và tự thông tin xấp xỉ $9.48$ bit. Dòng 11 bit do nguồn cung cấp, không tuyên bố ngắn nhất.
- Bảng giải mã “BILL GATES” ở PDF tr.99 in nhầm khoảng A thành khoảng B. Ghi chú dùng bảng mô hình đúng ở tr.97 và ghi erratum trong planning, không lặp lỗi.

## 9. Rủi ro và điểm cần duyệt

- Không trộn trọng số lá `ESCAPE` với trọng số 0 của lá ký hiệu mới; không dùng NYT/FGK/Vitter.
- Không dùng Hình 4.1 của Chương 4 vì hình và lời mô tả trọng số lệch nhau; dùng Hình 4.2–4.3 đã vẽ lại.
- Không nói dựng lại bảo đảm bám phân phối trôi. Mục đích bắt buộc là chống tràn; chiết giảm lịch sử chỉ là tác dụng kèm theo được nguồn quan sát.
- Không dùng bất đẳng thức Kraft như chứng minh tối ưu Huffman; Kraft chỉ mô tả miền độ dài khả thi.
- Không mô tả số thực lý tưởng như cài đặt. Phải tách khoảng lý tưởng khỏi số nguyên hữu hạn, phép dịch, underflow, kết thúc và đệm.
- Không gọi 11 bit của X03 là tối thiểu; không dùng entropy trung bình thay cho tự thông tin của `caba`.
- Không đưa mã trang, thời lượng, worker, reviewer, prompt, goal, rubric hoặc quy trình sản xuất vào ghi chú công khai.

## 10. Kế hoạch tác tử

1. Ba reader `z-ai/glm-5.3-flash` qua OpenRouter lập kế hoạch, ánh xạ nguồn và đề xuất chủ đề độc lập.
2. Codex chính hợp nhất và duyệt goal trước writer.
3. Một writer `deepseek/deepseek-v4-flash-0731` soạn trong gốc tạm hẹp.
4. Năm reviewer `z-ai/glm-5.3-flash` kiểm nguồn, toán–thuật toán, mạch sư phạm, tính liên tục và viewer.
5. Codex chính áp dụng sửa có căn cứ; hai reviewer GLM tái kiểm toán–thuật toán và mạch.
6. Dùng `$no-ai-slop` và `$quill`, không tạo `quill.json`; kiểm viewer thật, rồi mới cập nhật index, commit, push và xác minh SHA.

## 11. Trạng thái

**Hoàn tất.** Ba reader, writer DeepSeek và năm reviewer đã chạy đúng model qua OpenRouter; các lượt lỗi hoặc vượt giới hạn công cụ đều bị loại và chạy lại trong phạm vi hẹp. Codex chính đã áp dụng các sửa được reviewer chấp thuận; hai lượt tái kiểm toán–thuật toán và mạch tự học đều `PASS`. Bản cuối đã qua `$no-ai-slop`, rà liên tục bằng `$quill` mà không tạo `quill.json`, kiểm viewer rộng/hẹp, bàn phím, bản in, KaTeX, SVG, đường dẫn an toàn và liên kết từ index. Deck không cần sửa vì ghi chú không thay đổi nội dung dùng chung.
