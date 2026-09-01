# Goal ghi chú Bài 11

## 1. Goal

Hoàn thiện ghi chú tự học **Bài 11 — Nén bằng từ điển và nén mất dữ liệu** tại `2627-1/materials/lec-11/lecture-note.md`. Tài liệu phải giúp sinh viên thực thi ba thuật toán LZ, giải thích điều kiện khôi phục đúng, theo dõi đường ống JPEG dựa trên DCT và chọn phương pháp theo đặc tả đầu ra cùng chi phí trạng thái.

## 2. Vấn đề trung tâm

Nén từ điển thay một cụm đã gặp bằng tham chiếu hoặc mã và phải khôi phục đúng từng ký hiệu. JPEG dựa trên DCT chấp nhận mất thông tin ở các bước đã công bố để đổi tốc độ bit lấy sai số tái tạo. Cùng là giảm kích thước dữ liệu, hai họ thuật toán có trạng thái, bất biến và hợp đồng đầu ra khác nhau.

## 3. Bằng chứng hoàn thành

- Người học tách được hai đặc tả khôi phục đúng và khôi phục gần đúng, rồi dùng đặc tả để loại phương án không phù hợp.
- Người học mã hóa và giải mã LZ77 bằng cửa sổ hữu hạn, giải thích sao chép chồng lấn, chứng minh bất biến lịch sử và nêu chi phí theo $n,W,L$.
- Người học mã hóa và giải mã LZ78, xử lý đúng token thường và token `EOS`, chứng minh hai phía cập nhật cùng từ điển.
- Người học chạy vết LZW, giải thích bất biến độ trễ một mục, phân loại $k<\texttt{next\_code}$, $k=\texttt{next\_code}$ và $k>\texttt{next\_code}$, đồng thời tách ngưỡng $T=2^b$ khỏi `MAX`.
- Người học theo dõi JPEG qua khối $8\times8$, dịch mức, DCT, lượng tử hóa, DC/AC, zigzag, mã độ dài loạt và IDCT; phân biệt bước khả nghịch với bước mất dữ liệu.
- Người học tính hai ô lượng tử có nguồn, liên hệ chúng với lượt zigzag và giải thích quan hệ có điều kiện giữa tốc độ bit với RMS.
- Năm bài recitation giữ nguyên dữ kiện và yêu cầu nguồn CMU đã được phê duyệt ngày 2026-08-28.
- Viewer, Markdown, KaTeX, SVG, liên kết, bàn phím, màn hình rộng/hẹp, bản in và an toàn đường dẫn đều đạt trước khi cập nhật index.

## 4. Đầu ra

- `2627-1/materials/lec-11/lecture-note.md`.
- Cập nhật phần ghi chú trong `2627-1/planning/lec-11/{outline,storyboard,review-log}.md`.
- Dùng 12 SVG hiện có trong `2627-1/img/lec-11/`.
- Thêm liên kết ghi chú Bài 11 vào `2627-1/index.html` sau khi viewer đạt.
- Không sửa deck trừ khi phát hiện lỗi nội dung dùng chung cần đồng bộ.

## 5. Nguồn và quyết định chọn nguồn

- Nelson–Gailly, *The Data Compression Book*, Chương 8, 9 và 11 là nguồn trục. Chương 8 chốt biến thể LZ77; Chương 9 chốt LZ78/LZW; Chương 11 chốt JPEG dựa trên DCT. Không dùng Chương 10 làm nguồn JPEG.
- CMU `compression3-lz.pdf` cung cấp các vết LZ và bốn bài luyện; `compression4-lossy.pdf` cung cấp bài về mục tiêu của biến đổi và chia khối. MIT 15.564 chỉ là nguồn đối chiếu tổng quan, không thay dữ kiện Nelson–Gailly hoặc CMU.
- Phần giảng LZ77 dùng khoảng lùi $(d,\ell,c)$; bài CMU giải mã dùng vị trí tuyệt đối $(p,\ell,c)$ đánh số từ 0. Hai quy ước phải được đặt cạnh nhau, không trộn.
- Ghi chú dùng dòng mã LZW nguyên đã đóng khung: $D[0..255]$ là byte, `next_code=256`, nên mã 256 là mục dữ liệu mới đầu tiên chứ không phải `EOS`. Biến thể 12 bit trong sách chỉ dùng để đối chiếu hợp đồng định dạng.
- Ngoài phạm vi: LZSS, MPEG, wavelet, Burrows–Wheeler, ACB, lựa chọn ma trận lượng tử chuẩn chi tiết và tỷ lệ nén cố định.

## 6. Bản đồ chủ đề

| `note-topic-id` | Nhãn | Chủ đề và sản phẩm | Nguồn, kết nối |
|---|---|---|---|
| `L11-N01` | cốt lõi | Hai đặc tả khôi phục và tiêu chí chọn thuật toán | `sources/source.md`; CMU LZ/lossy; mở hai nhánh LZ và JPEG |
| `L11-N02` | cốt lõi | LZ77: cửa sổ, token, vết chạy và sao chép chồng lấn | Nelson–Gailly Ch.8; CMU logic 3–6; nối đặc tả đúng sang thuật toán |
| `L11-N03` | cốt lõi | LZ77: giải mã, bất biến, dừng và chi phí | Nelson–Gailly Ch.8; CMU logic 6–10; trao giới hạn cửa sổ cho LZ78 |
| `L11-N04` | cốt lõi | LZ78: từ điển cụm, hai nhánh kết thúc và đồng bộ | Nelson–Gailly Ch.9; CMU logic 11–14, 18; dẫn sang việc bỏ ký tự ở LZW |
| `L11-N05` | cốt lõi | LZW: mã hóa và vết từ điển | Nelson–Gailly Ch.9; CMU logic 15–17; chuẩn bị bất biến độ trễ |
| `L11-N06` | cốt lõi | LZW: giải mã, `k=next_code`, hợp đồng độ rộng và chính sách đầy | Nelson–Gailly Ch.9; CMU logic 16, 19; đóng đặc tả khôi phục đúng |
| `L11-N07` | cốt lõi | JPEG: hợp đồng tốc độ bit–sai số và đường ống | Nelson–Gailly Ch.11; CMU lossy logic 2, 11, 13–16; mở nhánh gần đúng |
| `L11-N08` | cốt lõi | DCT khối và lượng tử hóa | Nelson–Gailly Ch.11; hai ô Hình 11.10–11.11; chỉ ra nơi mất dữ liệu |
| `L11-N09` | cốt lõi | DC/AC, zigzag, RLE, IDCT, chi phí và RMS | Nelson–Gailly Ch.11; nối hệ số lượng tử với dòng bit và ảnh tái tạo |
| `L11-N10` | cầu nối | So sánh LZ77, LZ78, LZW và JPEG | Tổng hợp N02–N09; thu hồi hợp đồng N01 |
| `L11-N11` | cốt lõi | Năm bài tập có dữ kiện và lời giải truy nguyên được | CMU LZ logic 5, 6, 13, 16; CMU lossy logic 11 |

Đồ thị tiên quyết: `N01→N02→N03→N04→N05→N06`; `N01→N07→N08→N09`; hai nhánh hội tụ ở `N10`, rồi dẫn sang `N11`. Không thêm chủ đề `bổ sung`. MIT được giữ ở mức đối chiếu/đọc thêm vì không cần để khép mạch.

## 7. Khuôn trình bày và ký hiệu

Mỗi thuật toán trọng tâm đi theo vai trò; đặc tả; ví dụ chạy tay; trực quan; thuật toán hoặc mệnh đề; chứng minh/lập luận; chi phí, giới hạn và tự kiểm. Công thức Markdown chỉ dùng `$...$` và `$$...$$`; khối tùy biến không lồng nhau.

- $W$ là kích thước từ điển LZ77, $L$ là độ dài vùng nhìn trước; $(d,\ell,c)$ dùng khoảng lùi và $(p,\ell,c)$ dùng vị trí tuyệt đối.
- $EOS$ nằm ngoài bảng chữ cái và chỉ hợp lệ ở token cuối. Token thường của LZ78 vẫn có thể là token cuối.
- $D[i]$ là cụm mang mã $i$; `next_code` là mã chưa cấp nhỏ nhất. Trong LZW, trước mã kế, mọi mã nhỏ hơn `next_code` của bộ giải mã trùng với bộ mã hóa; bộ mã hóa có thể đi trước đúng một mục.
- $C_{u,v}$ là hệ số DCT, $Q_{u,v}>0$ là bước lượng tử, $\hat C_{u,v}$ là số nguyên lượng tử và $\tilde C_{u,v}$ là hệ số tái tạo.
- DC là $C_{0,0}$; AC là 63 hệ số còn lại. RLE là mã độ dài loạt. RMS là căn sai số bình phương trung bình, không thay thế đánh giá cảm nhận.

## 8. Giá trị và lập luận phải tính lại

- LZ77 cho `aacaacabcabaaac`, $W=6$, $L=4$: năm token theo quy ước khoảng lùi là $(0,0,a)$, $(1,1,c)$, $(3,4,b)$, $(3,3,a)$, $(1,2,c)$. Token $(3,4,b)$ chép `aaca` rồi thêm `b`; ký tự chép thứ tư đọc lại dữ liệu vừa tạo.
- Bài CMU với từ điển hiện tại `abcd` và $(p,\ell,c)=(2,9,e)$, $p$ đánh số từ 0: chép `cdcdcdcdc`, thêm `e`; toàn đầu ra là `abcdcdcdcdcdce`.
- LZ78 cho `aabaacabcabcb`: các cặp là $(0,a),(1,b),(1,a),(0,c),(2,c),(5,b)$; từ điển cuối $D[1]=a,D[2]=ab,D[3]=aa,D[4]=c,D[5]=abc,D[6]=abcb$.
- LZW dùng $p\mapsto112,q\mapsto113,r\mapsto114$, `next_code=256`; chuỗi `ppqpprpqrpqrq` cho dòng mã `112,112,113,256,114,257,260,113,114,113`. Các mục mới 256–264 lần lượt là `pp`, `pq`, `qp`, `ppr`, `rp`, `pqr`, `rpq`, `qr`, `rq`.
- Với $w=\texttt{aba}$ và `next_code=271`: mã 270 tra bảng; mã 271 suy ra `abaa`; mã 272 là lỗi.
- DCT dùng $x,y,u,v\in\{0,\ldots,7\}$, $\alpha(0)=1/\sqrt8$ và $\alpha(t)=1/2$ với $t>0$. Lượng tử: $\hat C_{u,v}=\operatorname{round}(C_{u,v}/Q_{u,v})$, $\tilde C_{u,v}=Q_{u,v}\hat C_{u,v}$.
- Hai ô nguồn: tại $(0,2)$, $(-9,7)\to-1\to-7$, ở lượt zigzag 6 nếu đếm từ 1; tại $(0,4)$, $(3,11)\to0\to0$, ở lượt 15. Chỉ ô thứ nhất được dùng làm phép tính bắt buộc trong bài kiểm tra của deck.
- $E_{RMS}=\sqrt{\frac1N\sum_{i=1}^{N}(X_i-\hat X_i)^2}$. Với khối cố định $8\times8$, chi phí toàn ảnh là $\Theta(N)$ trong mô hình RAM; không suy ra tỷ lệ nén hay RMS cố định.

## 9. Rủi ro và điểm cần duyệt

- Không đồng nhất hai quy ước vị trí LZ77; không sao chép một lần bằng lát cắt khi nguồn và đích chồng lấn.
- Không phát `EOS` ra dữ liệu; chỉ chấp nhận nó ở token cuối. Với LZ78, không buộc mọi dòng phải kết thúc bằng `(i,EOS)`.
- Không viết bất biến “hai từ điển LZW luôn giống nhau”. Phải dùng độ trễ một mục và ba trường hợp của mã kế.
- Không dành mã 256 cho `EOS` trong vết của bài; không tự đặt mốc đổi độ rộng. Định dạng phải công bố early/late-change và freeze/reset có tín hiệu.
- Không nói DCT tự nó làm mất dữ liệu; trong mô hình bài, lấy mẫu thưa sai màu là tùy chọn và lượng tử hóa là bước không khả nghịch nói chung. Zigzag, RLE và mã entropy không làm mất thêm dữ liệu.
- Không dùng RMS như thước đo đầy đủ cho chất lượng cảm nhận; không tuyên bố lượng tử mạnh cho một tỷ lệ kích thước–sai số cố định.
- Không đưa mã trang, thời lượng, worker, reviewer, prompt, goal, rubric hoặc quy trình sản xuất vào ghi chú công khai.

## 10. Kế hoạch tác tử

1. Ba reader `z-ai/glm-5.3-flash` qua OpenRouter lập kế hoạch, ánh xạ nguồn và đề xuất chủ đề độc lập.
2. Codex chính hợp nhất và duyệt goal trước writer.
3. Một writer `deepseek/deepseek-v4-flash-0731` soạn trong gốc tạm hẹp.
4. Năm reviewer `z-ai/glm-5.3-flash` kiểm nguồn, toán–thuật toán, mạch sư phạm, tính liên tục và viewer.
5. Codex chính áp dụng sửa có căn cứ; hai reviewer GLM tái kiểm toán–thuật toán và mạch.
6. Dùng `$no-ai-slop` và `$quill`, không tạo `quill.json`; kiểm viewer thật, rồi mới cập nhật index, commit, push và xác minh SHA.

## 11. Trạng thái

**Hoàn tất.** Ghi chú, ba tệp planning và liên kết index đã được cập nhật. Ba reader, writer, năm reviewer và hai reviewer tái kiểm đều dùng đúng model/provider đã duyệt; lần tái kiểm toán cuối ở phiên `83111` và tái kiểm mạch ở phiên `91975` đều `PASS`. `$no-ai-slop` và `$quill` đã được áp dụng. Viewer thật đạt ở màn hình rộng, màn hình hẹp và bản in; KaTeX, SVG, liên kết, bàn phím và hai phép thử an toàn đường dẫn đều đạt.
