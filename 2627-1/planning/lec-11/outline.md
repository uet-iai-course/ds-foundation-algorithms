# Bài 11: Nén bằng từ điển và nén mất dữ liệu — dàn ý ghi chú (dựng lại 2026-11)

> **Đồng bộ với ghi chú sau biên tập 2026-11-19, bản cuối** (`materials/lec-11/lecture-note.md`, md5 `4b9cd9af3fdda50c45031f8d6e181f1d`, 30 407 âm tiết; bản sao `scratchpad/lec11-note-final.md` của phiên điều phối). Từ mục 4 trở đi, số hiệu, tiêu đề, ký hiệu, ví dụ, tình huống và bài tập là của ghi chú thực tế; số dòng dẫn trong tệp này lấy theo bản v2 và có thể lệch vài dòng so với bản cuối. Chỗ ghi chú lệch kế hoạch ban đầu nêu ở mục 13. Căn cứ đồng bộ: R4 (`lec11-recheck-I6-mach.md`), M-N16 (`lec11-review-I5-mach.md`), bảng quyết định I.6 (`lec11-I6-quyet-dinh.md`), mục "Duyệt danh sách bài tập (II.1)" của `review-log.md`.

> Tệp planning, không công khai. Thay toàn bộ dàn ý cũ (bản cũ còn trong git, commit trước 2026-11-19). Căn cứ: `planning/lec-11/prompt-xay-dung-bai-11.md` (Q1–Q10 theo cột "Đề xuất", người dùng chốt 2026-11-19), `NGUYEN-TAC-HOC-PHAN.md` (GC-DSFA-1…15, BT-DSFA-1…11, NT-DSFA-10/11, VP-DSFA-1…8), `NGUYEN-TAC-GHI-CHU.md` (GC1–GC26), `NGUYEN-TAC-VAN-PHONG.md` (VP1–VP24), `NGUYEN-TAC-BAI-TAP.md` (BT1–BT13). Mẫu tham chiếu: ghi chú Bài 10 và `planning/lec-10/outline.md`. Người lập: tác tử lập kế hoạch (giai đoạn I.1), chờ điều phối viên duyệt. Đã đối chiếu với báo cáo phân tích nguồn I.2 (`scratchpad/lec11-source-analysis.md` của phiên điều phối, đã được điều phối viên kiểm); chỗ dẫn "PTN §k" là mục của báo cáo đó.
>
> Viết tắt nguồn trong tệp này: **NG** = Nelson và Gailly, *The Data Compression Book*, ấn bản 2 (`sources/textbooks/the-data-compression-book-2e.pdf`), số trang là **trang PDF**; **CMU-LZ** = Blelloch, CMU 15-499 `compression3-lz.pdf`; **CMU-L** = CMU 15-499 `compression4-lossy.pdf`; "tc. N" = trang chiếu logic N (số "Page N" in dưới mỗi trang chiếu; mỗi trang PDF có bốn trang chiếu); **MIT** = MIT 15.564 `lec3-compression.pdf` (chỉ đối chiếu). Mọi vết chạy và phép tính ghi trong tệp này đã được người lập kế hoạch chạy lại bằng Python (script trong scratchpad của phiên, không đưa vào repo); tác tử soạn và vai rà thuật toán vẫn phải tự tính lại (GC26).

## 0. Tóm tắt quyết định của dàn ý

- Sáu mục nội dung, sáu mạch nội dung của deck (kể cả "Mở đầu" và "Tổng kết"), recitation là `<section>` ngoài thứ bảy, không tính (NT-DSFA-10, Q3).
- Hai ví dụ xuyên suốt, đều lấy từ nguồn:
  - **hai chuỗi của CMU**: chuỗi mười lăm ký tự `aacaacabcabaaac` (LZ77, CMU-LZ tc. 5) và chuỗi mười ba ký tự `aabaacabcabcb` (LZ78 và LZW, CMU-LZ tc. 13, 17; CMU dùng **cùng** chuỗi cho hai thuật toán nên so sánh được trực tiếp);
  - **ảnh xám CHEETAH.GS** 320 × 200 điểm, 64 000 byte (NG tr. 265, Hình 11.14 tr. 287): khối 8 × 8 của Hình 11.9 (tr. 258) đi trọn đường ống JPEG, bảng Hình 11.14 cho đánh đổi tốc độ bit–sai số.
- Bỏ chuỗi `ppqpprpqrpqrq` của ghi chú cũ: chuỗi này không có trong nguồn nào, là chuỗi CMU-LZ tc. 17 đổi chữ a → p, b → q, c → r để 112–114 thành mã ASCII đúng (PTN §3). Dùng thẳng `aabaacabcabcb` của CMU. CMU in mã 112, 113, 114 cho a, b, c, không phải mã ASCII; đề xuất dùng **mã byte thật** a ↦ 97, b ↦ 98, c ↦ 99, khớp Định nghĩa 11.18 (mã $0..255$ là chính giá trị byte, như NG tr. 220: "code 65 will always represent the character A"); cấu trúc dòng mã và các mục 256–264 giữ nguyên như CMU (điểm D3, mục 13).
- (Đã quyết khi soạn: Ví dụ 11.8 gồm (a) IWOMBAT của NG tr. 217 và (b) vết đầy đủ `abababa` viết "Giả sử".) Bỏ ví dụ tự dựng của ghi chú cũ cho mã LZW chưa có ($w=\texttt{aba}$, `next_code` = 271). Vết CMU `aabaacabcabcb` **không** chạm nhánh $k=\texttt{next\_code}$ (PTN §3). Nguồn chỉ có hai dạng của nhánh này: dạng trừu tượng `…SSc…`, `S[0]=c` (CMU-LZ tc. 16, là bài recitation) và đoạn vết IWOMBAT với mã 300, 400 (NG tr. 217). Đề xuất dùng IWOMBAT làm Ví dụ 11.8; có cần thêm một vết đầy đủ tối thiểu như `abababa` (mã 97, 98, 256, 258; dạng $cScSc$ với $c=\mathrm a$, $S=\mathrm b$, không có trong nguồn) hay không là điểm D7 cho điều phối viên.
- Bỏ phần đổi độ rộng mã LZW ($T=2^b$, `MAX`, early/late change) khỏi ghi chú: NG chỉ trình bày bản mã cố định 12 bit (LZW12.C, tr. 218–226); nguồn đã giao không có quy tắc đổi độ rộng (điểm D6). Vì vậy không cần mục "Đọc thêm" theo GC-DSFA-15 ở ước lượng độ dài hiện tại.
- Lượng tử hóa làm tròn tới số nguyên gần nhất (công thức NG tr. 259, khớp ngưỡng 16 của ô (7,7) ở tr. 260); không chép ma trận "sau giải lượng tử" của Hình 11.11 vì hình đó theo phép chia nguyên cắt cụt của mã DCT.C (điểm D4).
- Quy ước LZ77 duy nhất trong ghi chú: bộ ba $(d,\ell,c)$ với $d$ là **khoảng lùi** tính từ con trỏ. Đây chính là quy ước của CMU-LZ tc. 4 ("position … relative to the cursor"); ghi chú cũ và review-log cũ ghi nhầm rằng CMU dùng vị trí tuyệt đối. NG dùng vị trí trong cửa sổ văn bản (tr. 175–176). Điểm D2.

## 1. Câu hỏi trung tâm (bài toán dữ liệu lớn, NT-DSFA-5)

Nguồn của tình huống: `sources/source.md` dòng 403 ("Nén kho văn bản lặp mẫu và kho ảnh lớn có yêu cầu chất lượng khác nhau"; khó khăn: "một mô hình nén duy nhất không phù hợp đồng thời với dữ liệu ký hiệu và dữ liệu cảm nhận").

**Dữ liệu.**

- Kho văn bản và nhật ký: dòng byte dài $n$, đọc một lượt, có cụm lặp lại (NG tr. 208: tên "Jacob Ziv" lặp bốn, năm lần rải rác trong sách; danh bạ điện thoại lặp họ "Jones"). Phải khôi phục đúng từng byte (đặc tả của Bài 10, Định nghĩa 10.1). $n$ để dạng ký hiệu; không đặt số cỡ kho (không có nguồn). Nếu tác tử soạn cần một cỡ cụ thể, viết "Giả sử …" và ghi lý do vào `review-log.md`.
- Kho ảnh: danh mục bán hàng 1 000 ảnh, mỗi ảnh 320 × 200 điểm, 1 byte mỗi điểm, tức 64 000 byte mỗi ảnh và khoảng 64 MB cả kho (NG tr. 246; NG ghi "64K" và "64MB"; cỡ 64 000 byte theo cột "Starting Size" của Hình 11.14, tr. 287). Ảnh chụp cho phép sai khác nhỏ mà mắt không nhận ra (NG tr. 247).

**Đầu ra.** Với mỗi kho: một dòng bit nén và bộ giải nén tương ứng. Kho văn bản: bản giải nén trùng từng byte. Kho ảnh: ảnh tái tạo có sai số căn bình phương trung bình (RMS) dưới một ngưỡng chọn trước.

**Giới hạn.**

- Bộ nhớ của bộ nén: cửa sổ hữu hạn (NG tr. 179: cửa sổ 4 096 byte, vùng nhìn trước 16 byte) hoặc từ điển hữu hạn (NG tr. 220: mã 12 bit, tối đa 4 096 mục).
- Một lượt đọc, thời gian mỗi byte gần hằng số (NG tr. 178: tìm vét cạn tốn tỷ lệ với tích cỡ cửa sổ và cỡ vùng nhìn trước).
- Kho ảnh: ngưỡng RMS. Số đo nguồn để neo: CHEETAH.GS ở hệ số chất lượng 2 còn 18 367 byte với RMS 6,9; ở hệ số 25 còn 5 094 byte với RMS 17,4 (NG Hình 11.14, tr. 287).

**Câu hỏi trung tâm (dự kiến cho hộp "Câu hỏi:" của deck và đoạn mở Mục 1, văn bản sinh viên, đã qua `no-ai-slop` Edit):**

> Với kho văn bản phải khôi phục đúng từng byte và kho ảnh chỉ cần khôi phục gần đúng, thuật toán nào đạt từng đặc tả trong một lượt đọc với bộ nhớ hữu hạn, và đổi lại được bao nhiêu byte?

Câu trả lời có điều kiện của chương (đoạn kết Mục 6 của ghi chú, dòng 1714–1716; ghi chú diễn giả "Tổng kết"): kho văn bản → LZ77 (lặp gần, cửa sổ $W$; mã hóa $O(nWL)$ khi so vét cạn, giải mã $O(n)$), LZ78/LZW (lặp xa, từ điển $M$ mục; kỳ vọng $O(n)$ với bảng băm), khôi phục đúng theo Định lý 11.8, 11.15, 11.23; rút ngắn khi một đơn vị mã mô tả nhiều hơn số ký tự hòa vốn (1,75 / 3 / 3,125 / 1,125 / 1,5 ký tự); trên `aabaacabcabcb` 70, 72, 90 bit so với 104 bit (Ví dụ 11.14); gzip 2,59 bit mỗi ký tự trên bộ Calgary (Tình huống 11.4). Kho ảnh → đường ống DCT–lượng tử hóa, sai số mỗi khối $\le\beta(q)$ (Định lý 11.31), $\beta(2)+\tfrac12\approx9{,}60$ cho bộ làm tròn; chương trình NG đưa CHEETAH.GS từ 64 000 xuống 18 367 byte, sai số đo 6,9 (Tình huống 11.1). Nén từ điển cho ảnh vẫn khôi phục đúng nhưng phình (Tình huống 11.2); nén mất dữ liệu cho văn bản vi phạm Định nghĩa 11.1.

## 2. Cấu trúc chương, mạch và `note-topic-id`

Mẫu chương GC-DSFA-2. Tên mục là cụm danh từ (VP7). Mỗi mạch nội dung của deck gồm một hoặc nhiều mục liên tiếp (GC-DSFA-4); mạch "Mở đầu" của deck gồm các trang khung (bìa, tiên quyết, mục tiêu, nội dung, vấn đề trung tâm) và Mục 1, như Bài 10.

| Phần của ghi chú | Tiêu đề dự kiến | `note-topic-id` | Mạch deck |
|---|---|---|---|
| Giới thiệu + liên kết deck | (không tiêu đề) | — | 1 Mở đầu |
| Mục tiêu học tập | `## Mục tiêu học tập` | — | 1 |
| Kiến thức tiên quyết | `## Kiến thức tiên quyết` | `lec-11-topic-01` | 1 |
| Bảng ký hiệu | `## Bảng ký hiệu` | — | 1 |
| Mục 1 | `## 1. Khôi phục đúng và khôi phục gần đúng` | — | 1 |
| 1.1 | `### 1.1 Hai đặc tả khôi phục` | `lec-11-topic-02` | 1 |
| 1.2 | `### 1.2 Giới hạn của nén khôi phục đúng` | `lec-11-topic-03` | 1 |
| Mục 2 | `## 2. Nén bằng cửa sổ trượt LZ77` | — | 2 |
| 2.1 | `### 2.1 Cửa sổ, vùng nhìn trước và bộ ba` | `lec-11-topic-04` | 2 |
| 2.2 | `### 2.2 Giải mã và sao chép chồng lấn` | `lec-11-topic-05` | 2 |
| 2.3 | `### 2.3 Chi phí và giá của một bộ ba` | `lec-11-topic-06` | 2 |
| Mục 3 | `## 3. Nén bằng từ điển cụm LZ78` | — | 3 |
| 3.1 | `### 3.1 Từ điển cụm và cây từ điển` | `lec-11-topic-07` | 3 |
| 3.2 | `### 3.2 Đồng bộ hai từ điển` | `lec-11-topic-08` | 3 |
| 3.3 | `### 3.3 Chi phí và từ điển đầy` | `lec-11-topic-09` | 3 |
| Mục 4 | `## 4. Thuật toán LZW` | — | 4 |
| 4.1 | `### 4.1 Từ điển nạp sẵn và mã hóa` | `lec-11-topic-10` | 4 |
| 4.2 | `### 4.2 Giải mã với độ trễ một mục` | `lec-11-topic-11` | 4 |
| 4.3 | `### 4.3 Chi phí và độ rộng mã cố định` | `lec-11-topic-12` | 4 |
| Mục 5 | `## 5. Nén ảnh JPEG dựa trên DCT` | — | 5 |
| 5.1 | `### 5.1 Khối 8 × 8, dịch mức và DCT` | `lec-11-topic-13` | 5 |
| 5.2 | `### 5.2 Lượng tử hóa và sai số tái tạo` | `lec-11-topic-14` | 5 |
| 5.3 | `### 5.3 Sai phân DC, thứ tự zigzag và mã độ dài loạt` | `lec-11-topic-15` | 5 |
| 5.4 | `### 5.4 Đường ống mã hóa, giải mã và chi phí` | `lec-11-topic-16` | 5 |
| Mục 6 | `## 6. Chọn phương pháp nén` | `lec-11-topic-17` | 6 Tổng kết |
| Tình huống | `## Tình huống áp dụng và ứng dụng` | `lec-11-topic-18` | 6 |
| Tóm tắt | `## Tóm tắt chương` | `lec-11-topic-19` | 6 |
| Bài tập củng cố | `## Bài tập củng cố` | `lec-11-topic-20` | (recitation, mạch 7) |
| Tham khảo | `## Hướng dẫn đọc thêm và tài liệu tham khảo` | `lec-11-topic-21` | 6 (trang "Tài liệu tham khảo") |

Trong tiêu đề Markdown, "8 × 8" viết `$8\times8$` theo VP10 (tiêu đề có công thức như Bài 10). Chú thích `note-topic-id` đặt ngay trước tiêu đề `###` (hoặc `##` khi mục không chia tiểu mục), như ghi chú Bài 10.

**Bảng mạch (để storyboard dùng lại; không tính recitation, NT-DSFA-10):**

| Mạch | Tên mạch dự kiến | Mục | Loại (AGENTS.md) | Đầu vào | Đầu ra | Phút |
|---:|---|---|---|---|---|---:|
| 1 | Mở đầu | khung + Mục 1 | giới thiệu và động lực; khái niệm | Mệnh đề 10.2, Hệ quả 10.19 | Định nghĩa 11.1, Mệnh đề 11.2: hai đặc tả, khi nào bắt buộc mất dữ liệu | 12 |
| 2 | Nén LZ77 với cửa sổ trượt | 2 | thuật toán và ví dụ vận dụng | đặc tả khôi phục đúng | bộ ba, Định lý 11.8, chi phí $O(nWL)$; giới hạn: quên cụm xa hơn $W$ | 26 |
| 3 | Từ điển cụm LZ78 | 3 | thuật toán và ví dụ vận dụng | giới hạn cửa sổ | Định lý 11.15 đồng bộ; giới hạn: mỗi cặp mang một ký tự 8 bit | 18 |
| 4 | Thuật toán LZW | 4 | thuật toán và ví dụ vận dụng | cặp LZ78 | Định lý 11.23, mã chưa có; giới hạn: chuỗi phải khớp đúng từng byte | 22 |
| 5 | Nén ảnh mất dữ liệu bằng JPEG | 5 | khái niệm; thuật toán; chi phí | đặc tả khôi phục gần đúng | Định lý 11.31 (sai số ≤ bước/2), Thuật toán 11.34, chi phí mỗi khối | 34 |
| 6 | Tổng kết | 6 + Tình huống + Tóm tắt | tổng kết | mọi kết quả | bảng chọn phương pháp, trả lời câu hỏi trung tâm | 8 |
| — | **Giảng** | | | | | **120** |
| 7 | Bài tập trên lớp (recitation) | `exercises.md` | bài tập | mạch 2–5 | năm bài recitation CMU, Bài tập 11.12, 11.13, 11.15–11.17 (mục 14) | 60 |

Thời lượng chỉ ghi ở đây (GC17, NT27). Phương án dự phòng: nếu storyboard thấy mạch 5 quá tải (DCT, chứng minh trực chuẩn, lượng tử, mã hệ số), tách thành hai mạch ("Biến đổi DCT và lượng tử hóa" = 5.1–5.2; "Mã hệ số và đường ống JPEG" = 5.3–5.4), tổng 7 mạch nội dung, vẫn trong 5–7.

## 3. Mục tiêu học tập (đúng như ghi chú, dòng 9–16; Q6)

Sau chương này, người học có thể:

1. Phân biệt đặc tả khôi phục đúng với đặc tả khôi phục gần đúng, tính tốc độ bit (bit rate) và sai số căn bình phương trung bình (root mean squared error, RMS), và chứng minh rằng một bộ nén rút ngắn mọi đầu vào phải làm mất dữ liệu (Mục 1).
2. Mã hóa và giải mã LZ77 bằng bộ ba khoảng lùi–độ dài–ký tự, kể cả khi vùng nguồn chồng lên vùng đích, chứng minh bộ giải mã khôi phục đúng và đếm chi phí theo cỡ cửa sổ và cỡ vùng nhìn trước (Mục 2).
3. Mã hóa và giải mã LZ78, dựng cây từ điển và chứng minh bằng quy nạp rằng hai phía giữ cùng từ điển (Mục 3).
4. Mã hóa và giải mã LZW, xử lý mã chưa có trong từ điển của bộ giải mã và chứng minh mã đó chỉ có thể bằng mã kế tiếp (Mục 4).
5. Tính DCT, lượng tử hóa, thứ tự zigzag và mã độ dài loạt trên một khối $8\times8$, chỉ ra bước làm mất dữ liệu và chặn sai số tái tạo theo bước lượng tử (Mục 5).
6. Chọn phương pháp nén cho một kho dữ liệu theo đặc tả khôi phục, dạng dư thừa của dữ liệu và chi phí bộ nhớ (Mục 6).

Ghi chú cho tác tử soạn: mục tiêu không có số hiệu khối, không ký hiệu mới ngoài $8\times8$ (GC16, VP21). Ánh xạ mục tiêu ↔ bài tập ở mục 14.

## 4. Kiến thức tiên quyết (đúng như ghi chú, dòng 19–35)

Câu quy ước số hiệu: `10.k`, `08.k`, `05.k`. Câu thứ hai liệt kê biến tạm của các kết quả nhắc lại: $u$, $r$, $j$, $P$, $H$, $X$, $Y$, $\alpha$, $\theta$, $\omega$ (không mang nghĩa của bảng ký hiệu Bài 11). Mười một gạch đầu dòng:

1. Mã giải mã duy nhất (Định nghĩa 10.1).
2. Không mã nào rút ngắn mọi thông điệp (Mệnh đề 10.2).
3. Mô hình, bộ mã và cách dừng (Định nghĩa 10.3, Nhận xét 10.4), kể cả mô hình bậc $j$.
4. Mã tiền tố (Định nghĩa 10.5).
5. Entropy và mã Huffman (Định nghĩa 10.11, Thuật toán 10.14, Định lý 10.18, Hệ quả 10.19).
6. Mã số học (Định lý 10.34).
7. Số bit của một bộ đếm (Bài 08, Mục 1.4, sau Định nghĩa 08.3).
8. Quy nạp và bất biến vòng lặp (chứng minh Mệnh đề 05.19; CLRS, Chương 2).
9. Bảng băm và cây (CLRS, Chương 11): giả thiết băm đều, hệ số tải $\alpha$ hằng, kỳ vọng $O(1)$; địa chỉ mở với $\alpha<1$: tìm không thành công kỳ vọng $\le1/(1-\alpha)$ lần dò.
10. Ma trận trực chuẩn (Đại số tuyến tính), kể cả vết $\operatorname{tr}(XY)=\operatorname{tr}(YX)$.
11. Biến tích thành tổng (toán phổ thông).

CLRS dẫn theo chương, không theo mục, vì `sources/` không có bản CLRS để kiểm số mục (quyết định I.6 số 25). Còn mở (R1 của `lec11-recheck-I6-mach.md`): $\alpha$ ở dòng 23 được gọi là biến tạm nhưng Mệnh đề 11.24 và Nhận xét 11.25 dùng $\alpha$ làm hệ số tải; chữ $c$ dùng cho "mã ký hiệu" ở dòng 25, 139 trùng $c$ của bảng.

## 5. Bảng ký hiệu (đúng như ghi chú, dòng 37–80; 27 dòng)

Câu dẫn của ghi chú: mỗi chữ trong bảng giữ một nghĩa trong cả chương; $i$, $j$, $t$ còn làm chỉ số chạy; chữ chỉ dùng trong một khối được giới thiệu tại chỗ và không trùng chữ trong bảng; ma trận DCT viết $T$ (NG gọi là $C$).

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $\Sigma$; $\lvert\Sigma\rvert$ | bảng chữ cái; số ký hiệu | tập hữu hạn; 256 với byte |
| $x=x_1\cdots x_n$; $n$ | chuỗi đầu vào; độ dài | $x_i\in\Sigma$ |
| $x[i..j]$ | đoạn $x_i\cdots x_j$; rỗng khi $i>j$ | chuỗi con |
| $\{0,1\}^*$; $\lvert\cdot\rvert$ | tập các chuỗi bit hữu hạn; độ dài | |
| $m$; $m_{\mathrm h}$, $m_{\mathrm w}$ | số mẫu; số hàng, số cột của ảnh, $m=m_{\mathrm h}m_{\mathrm w}$ | số nguyên dương |
| $\varphi$; $\psi$ | bộ nén; bộ giải nén | ánh xạ |
| $y$ | đầu ra của bộ giải nén | chuỗi hoặc ảnh |
| $p$ | số ký tự đã mã hóa (vị trí con trỏ) | $0\le p\le n$ |
| $W$; $L$ | cỡ cửa sổ; độ dài khớp tối đa (cỡ vùng nhìn trước) | số nguyên dương |
| $(d,\ell,c)$ | bộ ba LZ77 | $0\le d\le W$, $0\le\ell\le L$, $c\in\Sigma$ |
| $\tau$ | số đơn vị mã (bộ ba, cặp hoặc mã) bộ mã hóa phát | số nguyên không âm |
| $D$; $D[i]$ | từ điển; cụm mang mã $i$ | |
| $(i,c)$ | cặp LZ78 | $i$ có trong $D$ |
| $w$ | cụm hiện tại (mã hóa) hoặc cụm vừa xuất (giải mã) | chuỗi khác rỗng |
| $k$; $\texttt{next\_code}$ | mã LZW đọc vào; mã chưa cấp nhỏ nhất | số nguyên không âm |
| $\operatorname{first}(w)$ | ký tự đầu của $w$ | $\Sigma$ |
| $M$; $b$ | số mục tối đa của từ điển; số bit mỗi mã | $M=2^b$ |
| `EOS` | ký hiệu kết thúc dòng | ngoài $\Sigma$ |
| $P=(P_{\xi\eta})$; $A=(A_{\xi\eta})$ | khối điểm ảnh $8\times8$; khối sau dịch mức | hàng $\xi$, cột $\eta\in\{0,\ldots,7\}$ |
| $T=(T_{u\xi})$ | ma trận DCT | thực, $8\times8$, trực chuẩn |
| $F=(F_{uv})$ | hệ số DCT $F=TAT^{\top}$; $F_{00}$ là hệ số DC | thực |
| $Q=(Q_{uv})$; $q$ | ma trận lượng tử; hệ số chất lượng | $Q_{uv}=1+(1+u+v)q$ |
| $\hat F_{uv}$; $\tilde F_{uv}$ | số nguyên lượng tử; hệ số giải lượng tử | $\mathbb Z$; $\mathbb Z$ |
| $\tilde A$; $\tilde P$ | khối tái tạo trước và sau khi cộng 128, làm tròn, cắt | thực; $\{0,\ldots,255\}$ |
| $\beta(q)$ | cận sai số RMS của một khối, $\tfrac12\sqrt{\tfrac1{64}\sum_{u,v}Q_{uv}^2}$ | mức xám |
| $K$; $\kappa$; $\delta_\kappa$ | số khối; số thứ tự khối; sai phân DC của khối $\kappa$ | $K=m/64$ |
| $(r,s,a)$ | bộ ba mã độ dài loạt: số các số 0 đứng trước, số bit, biên độ | $r,s\ge0$; $a\in\mathbb Z$ |
| $E_{\mathrm{RMS}}$; $R$ | sai số căn bình phương trung bình; tốc độ bit | mức xám; bit mỗi mẫu |

**Đổi chữ so với bảng dự kiến của dàn ý** (quyết định I.6 số 1): chỉ số điểm ảnh $x,y\to\xi,\eta$ (vì $x$, $y$ là chuỗi đầu vào và đầu ra); số mẫu $m$ (mới) với $m_{\mathrm h}$, $m_{\mathrm w}$ thay cho cạnh ảnh $H$, $V$; số đơn vị mã $\tau$ (mới); $N=8$ bỏ khỏi bảng (viết thẳng 8); hệ số chuẩn hóa DCT $\alpha(u)\to\gamma(u)$ (cục bộ, Định nghĩa 11.26); tham số của Bổ đề 11.27 là $\mu$ với $\theta=\mu\pi/16$; sai số lượng tử một hệ số không còn chữ riêng; thêm $\beta(q)$, $K$, $\kappa$, $\delta_\kappa$, $(r,s,a)$, $\tilde A$; $\hat F$, $\tilde F$ thuộc $\mathbb Z$.

**Ký hiệu cục bộ** (giới thiệu tại chỗ, không trùng bảng): $\varepsilon$ ngưỡng sai số (Định nghĩa 11.1); $\lambda$ độ dài hòa vốn (Bài tập 11.2); $w_1,\ldots,w_\tau$, $k_1,\ldots,k_\tau$ cụm và mã LZW (Bổ đề 11.21); $\chi$, $S$ ký tự và chuỗi của dạng $\chi S\chi S\chi$ (Mệnh đề 11.22); $\nu$ (Bài tập 11.6); $\gamma(u)$ (Định nghĩa 11.26); $\mu$, $\theta$ (Bổ đề 11.27); $\sigma$, $n_\sigma$ đường chéo (lời giải Bài tập 11.9); $\beta_\kappa$ (Bài tập 11.9). Quy ước đọc (dòng 69–78): dấu phẩy thập phân, chuỗi trong khối mã, ký tự đứng riêng chữ đứng, dấu cách `␣`, chỉ số từ 0, mã byte $\mathrm a\mapsto97$, $\mathrm b\mapsto98$, $\mathrm c\mapsto99$, dấu cách $\mapsto32$; quy tắc "bộ nén/bộ giải nén" ($\varphi$, $\psi$) với "bộ mã hóa/bộ giải mã" (thuật toán cụ thể); viết tắt NG, CMU-I, CMU-LZ, CMU-L, CLRS.


## 6. Thuật ngữ Việt–Anh (VP-DSFA-5, thống nhất với Bài 10)

| Tiếng Việt | Tiếng Anh | Ghi chú |
|---|---|---|
| nén không mất thông tin; nén khôi phục đúng | lossless compression | Bài 10 dùng "nén không mất thông tin"; Bài 11 gọi đặc tả là "khôi phục đúng" |
| nén mất dữ liệu (còn gọi là nén mất thông tin) | lossy compression | Bài 10 viết "nén mất thông tin (lossy compression, còn gọi là nén mất dữ liệu)"; tên Bài 11 cố định "nén mất dữ liệu" (`source.md`) — điểm D9 |
| đặc tả khôi phục gần đúng; độ méo | approximate reconstruction; distortion | |
| nén bằng từ điển | dictionary-based compression | NG tr. 247: "statistical programs in disguise" |
| cửa sổ trượt; cửa sổ văn bản; vùng nhìn trước; con trỏ | sliding window; text window; look-ahead buffer; cursor | CMU-LZ tc. 4; NG tr. 174 |
| cụm; cụm khớp dài nhất; độ dài khớp | phrase; longest match; match length | |
| khoảng lùi | offset (CMU: position relative to the cursor) | NG dùng vị trí trong cửa sổ |
| bộ ba (LZ77); cặp (LZ78); mã (LZW) | token | "token" chỉ trong ngoặc ở lần đầu — điểm D8 |
| sao chép chồng lấn | overlapping copy | |
| LZSS; bit cờ | Lempel–Ziv–Storer–Szymanski; flag bit | chỉ ở "Trong thực hành" |
| từ điển cụm; cây từ điển (cây tiền tố) | phrase dictionary; dictionary tree, trie, multiway tree | CMU-LZ tc. 11 "trie"; NG tr. 212 "multiway tree" |
| mã kế tiếp | next code (`next_code`) | |
| độ trễ một mục | (không có thuật ngữ nguồn) | tên do học phần đặt; CMU-LZ tc. 16: "one step behind" |
| mã chưa có trong từ điển | the catch; KwKwK case | NG tr. 216 "The Catch" |
| từ điển đầy; đóng băng; xóa và khởi tạo lại | full dictionary; stop adding; flush, reset | NG tr. 213; CMU-LZ tc. 18 |
| độ rộng mã | code width, code size | |
| mã hóa biến đổi | transform coding | CMU-L tc. 7 |
| biến đổi cosine rời rạc; biến đổi ngược | discrete cosine transform (DCT); inverse DCT (IDCT) | |
| dịch mức | level shift | NG tr. 268 |
| hệ số DC; hệ số AC | DC coefficient; AC coefficients | |
| ma trận trực chuẩn; bảo toàn năng lượng | orthonormal matrix; energy conservation | CMU-L tc. 12 |
| lượng tử hóa; bước lượng tử; ma trận lượng tử; giải lượng tử | quantization; quantum, step size; quantization matrix (table); dequantization | NG tr. 259 |
| hệ số chất lượng | quality factor | NG tr. 260 |
| thứ tự zigzag | zig-zag sequence | NG tr. 262 |
| mã sai phân | difference coding | CMU-L tc. 13 |
| mã độ dài loạt | run-length encoding (RLE), run-length coding | Bài 10 dùng "mã độ dài loạt (run-length)" |
| mã hóa entropy | entropy coding | NG tr. 261 |
| sai số căn bình phương trung bình | root mean squared error (RMS) | NG tr. 266 |
| tốc độ bit; bit mỗi điểm ảnh | bit rate; bits per pixel (bpp) | CMU-L tc. 17 |
| đánh đổi tốc độ bit–sai số | rate–distortion trade-off | |
| mã hóa theo khối; hiện tượng khối | block coding; blocking (artifacts) | NG tr. 255, 287 |

## 7. Khối có số hiệu theo mục (theo ghi chú thực tế)

Bộ đếm chung 11.1–11.36 (Định nghĩa, Định lý, Mệnh đề, Bổ đề, Nhận xét, Thuật toán) liên tục; Ví dụ 11.1–11.14; Bài tập 11.1–11.11 trong ghi chú; Tình huống 11.1–11.4. Số dòng là của `lecture-note.md` bản v2. Mọi chứng minh ở mức đầy đủ; ngoài phạm vi chỉ có tính tối ưu tiệm cận của LZ77 (Wyner–Ziv, CMU-LZ trang chiếu 10), nêu ở Nhận xét 11.10 và mục tham khảo.

| Mục / tiểu mục (`note-topic-id`) | Khối, theo thứ tự đọc | Ghi chú đồng bộ |
|---|---|---|
| Mục 1, mở mục (dòng 81–94) | hình `note-cau-truc-chuong-11.svg` | bài toán hai kho có số, câu hỏi trung tâm, đọc hình |
| 1.1 Hai đặc tả khôi phục (`-02`) | Ví dụ 11.1 (Ảnh CHEETAH.GS ở ba hệ số chất lượng); Định nghĩa 11.1 (Bộ nén, hai đặc tả khôi phục, tốc độ bit, sai số RMS); Mệnh đề 11.2 (Bộ nén rút ngắn mọi đầu vào phải làm mất dữ liệu); Nhận xét 11.3 (Trong thực hành); Bài tập 11.1 (Đọc bảng kết quả nén và tính sai số; câu (a)–(e)) | 11.1(c) viết lại theo quyết định I.6 số 2; (d) tính RMS, (e) dùng Mệnh đề 11.2 |
| 1.2 Giới hạn của nén khôi phục đúng (`-03`) | đoạn văn | Mệnh đề 10.2 chỉ cho "có đầu vào không rút ngắn được" (quyết định I.6 số 3) |
| 2.1 Cửa sổ, vùng nhìn trước và bộ ba (`-04`) | Ví dụ 11.2 (Ba bộ ba đầu của chuỗi `aacaacabcabaaac`); Định nghĩa 11.4 (Cửa sổ, vùng nhìn trước và bộ ba LZ77); Thuật toán 11.5 (Mã hóa LZ77 tham lam) | vùng nhìn trước không chứa ký tự kế: $L$ là độ dài khớp tối đa; cấu hình NG 4 096 / 16 byte ứng với $L=15$ (quyết định I.6 số 19); bộ ba cuối buộc $p+\ell+1\le n$, không `EOS`; phá hòa bằng $d$ nhỏ nhất |
| 2.2 Giải mã và sao chép chồng lấn (`-05`) | Ví dụ 11.3 (Giải mã bộ ba $(3,4,\mathrm b)$ sau `aac`); Thuật toán 11.6 (Giải mã LZ77); Bổ đề 11.7 (Sao chép tuần tự); Định lý 11.8 (LZ77 khôi phục đúng) | Phạm vi của Định lý 11.8 gồm mọi dãy bộ ba hợp lệ, kể cả không tham lam |
| 2.3 Chi phí và giá của một bộ ba (`-06`) | Mệnh đề 11.9 (Chi phí của LZ77; (a) $\le\tau W(L+1)$ phép so, (b) $n$ phép ghi, (c) $W+L+1$ ký tự, (d) bit mỗi bộ ba); Nhận xét 11.10 (Trong thực hành: LZSS, gzip, 75/68 bit, Wyner–Ziv); Bài tập 11.2 (Số bit của một cặp và điểm hòa vốn; $\lambda$); Bài tập 11.3 (Một trăm chữ A) | |
| 3.1 Từ điển cụm và cây từ điển (`-07`) | Ví dụ 11.4 (Bốn cặp đầu của chuỗi `aabaacabcabcb`); Định nghĩa 11.11 (Từ điển cụm, cặp LZ78 và cây từ điển); Bổ đề 11.12 (Từ điển đóng với tiền tố); Thuật toán 11.13 (Mã hóa LZ78) | tiêu đề đổi từ "cây tiền tố" thành "cây từ điển"; Mục 3 mở bằng tên riêng 9 ký tự lặp cách hơn $W$ ("Giả sử", quyết định I.6 số 10) |
| 3.2 Đồng bộ hai từ điển (`-08`) | Ví dụ 11.5 (Giải mã bốn cặp đầu và dựng cây); Thuật toán 11.14 (Giải mã LZ78); Định lý 11.15 (Đồng bộ từ điển và khôi phục đúng của LZ78) | cặp cuối $(i,\texttt{EOS})$ là quy ước của chương |
| 3.3 Chi phí và từ điển đầy (`-09`) | Mệnh đề 11.16 (Chi phí của LZ78; (d) $\lceil\log_2M\rceil+9$ bit mỗi cặp với byte, trường ký tự chứa thêm `EOS`); Nhận xét 11.17 (Trong thực hành); Bài tập 11.4 (LZ78 cho chuỗi `DAD␣DADA␣DADDY␣DADO`; (d) quy nạp: các cụm đôi một khác nhau) | R3 còn mở: (d) không chứng minh "hai phía giữ cùng từ điển" như mục tiêu 3 |
| 4.1 Từ điển nạp sẵn và mã hóa (`-10`) | Ví dụ 11.6 (Mã hóa LZW chuỗi `aabaacabcabcb`, mã 97–99); Định nghĩa 11.18 (Từ điển LZW và mã kế tiếp); Thuật toán 11.19 (Mã hóa LZW) | mã cụm đầu 256, dòng đóng khung bằng số mã |
| 4.2 Giải mã với độ trễ một mục (`-11`) | Ví dụ 11.7 (Giải mã LZW dòng mã của Ví dụ 11.6, cả 10 mã); Ví dụ 11.8 (Mã chưa có trong từ điển của bộ giải mã: (a) IWOMBAT, NG tr. 217; (b) vết đầy đủ "Giả sử" `abababa` → 97, 98, 256, 258); Thuật toán 11.20 (Giải mã LZW; nhánh 3.2 là $k=\texttt{next\_code}$); Bổ đề 11.21 (Độ trễ một mục; (a)–(c)); Mệnh đề 11.22 (Mã chưa có trong từ điển của bộ giải mã; dạng $\chi S\chi S\chi$); Định lý 11.23 (LZW khôi phục đúng) | D7 đã quyết: có cả vết `abababa`; hình `note-lzw-ma-chua-co.svg` vẽ vết này |
| 4.3 Chi phí và độ rộng mã cố định (`-12`) | Mệnh đề 11.24 (Chi phí của LZW; (d) $b$ bit mỗi mã); Nhận xét 11.25 (Trong thực hành: LZW12, bảng băm 5 021, hệ số tải $\alpha$); Bài tập 11.5 (LZW cho chuỗi `␣WED␣WE␣WEE␣WEB␣WET`); Bài tập 11.6 (Chuỗi toàn chữ a; $n=6$ và $n=\nu(\nu+1)/2$) | Bài tập 11.6 mới, thay bài "ba bộ nén trên một chuỗi" của dàn ý; phần so sánh chuyển vào Ví dụ 11.14 (M-N16) |
| Mục 5, mở mục (dòng 1055–1062) | hình `note-jpeg-duong-ong.svg` | |
| 5.1 Khối $8\times8$, dịch mức và DCT (`-13`) | Ví dụ 11.9 (Khối $8\times8$ của CHEETAH.GS và hệ số DC); Định nghĩa 11.26 (Dịch mức, DCT và IDCT của khối $8\times8$; dạng ma trận và dạng tổng kép với $\gamma(u)$); Bổ đề 11.27 (Tổng cosine; $\mu$, $\theta$); Mệnh đề 11.28 (DCT trực chuẩn); Ví dụ 11.10 (Năng lượng của khối CHEETAH.GS) | khối Hình 11.9 gọi là "khối Hình 11.9 của NG"; "khối đầu tiên" chỉ dành cho khối Hình 11.11 (quyết định I.6 số 18); ô (0,7) dùng giá trị tính $-19$ (chính xác $-18{,}94$; Hình 11.9 in 19) |
| 5.2 Lượng tử hóa và sai số tái tạo (`-14`) | đoạn chạy tay ngắn trước định nghĩa (quyết định I.6 số 16); Định nghĩa 11.29 (Ma trận lượng tử, lượng tử hóa và giải lượng tử); Ví dụ 11.11 (Lượng tử hóa khối CHEETAH.GS ở hệ số chất lượng 2, cả khối, 30 hệ số khác 0); Mệnh đề 11.30 (Lượng tử hóa không khả nghịch và sai số mỗi hệ số); Định lý 11.31 (Sai số tái tạo của một khối bị chặn bởi bước lượng tử; $\beta(q)$, $\beta(2)\approx9{,}10$); Ví dụ 11.12 (IDCT và sai số của khối CHEETAH.GS; 4,12 trên hệ số, 4,21 trên điểm ảnh) | D4 đã quyết: lượng tử cả khối Hình 11.9 bằng làm tròn; Hình 11.11 chỉ dùng ô an toàn (Bài tập 11.8) |
| 5.3 Sai phân DC, thứ tự zigzag và mã độ dài loạt (`-15`) | đoạn chạy tay ngắn trước định nghĩa; Định nghĩa 11.32 (Hệ số AC, sai phân DC, thứ tự zigzag và mã độ dài loạt); Mệnh đề 11.33 (Các bước sau lượng tử hóa khôi phục đúng); Ví dụ 11.13 (Dãy zigzag và loạt số 0 của khối đã lượng tử); hình `note-zigzag-khoi-luong-tu.svg` | **mã độ dài loạt theo từng khối** như NG tr. 263–264 (quyết định I.6 số 7): mỗi số khác 0 cho bộ ba $(r,s,a)$; khối kết thúc bằng loạt $r$ số 0 thì đóng bằng bộ $(r,0)$ — **quy ước của chương**, dựa cách DCT.C ghi số bit 0 (NG tr. 271), không phải mã kết thúc khối của JPEG chuẩn. Ví dụ 11.13: giả sử DC khối trước là 60, $\delta=2$; 31 bộ = 30 bộ ba + $(9,0)$; số khác 0 cuối ở vị trí 55. "Hệ số AC" định nghĩa trong Định nghĩa 11.32 (D12 đã xử lý bằng định nghĩa) |
| 5.4 Đường ống mã hóa, giải mã và chi phí (`-16`) | Thuật toán 11.34 (Nén và giải nén một ảnh xám theo khối $8\times8$); Nhận xét 11.35 (Trong thực hành; cận khoảng 18,2 của chương trình cắt thương); Bài tập 11.7 (Ngưỡng của ô $(7,7)$); Bài tập 11.8 (Ba ô của khối hệ số đầu tiên: $F_{02}=-9$, $F_{04}=3$, $F_{20}=-84$); Bài tập 11.9 (Cận sai số và số đo trên CHEETAH.GS; (b) từ khối sang ảnh); Bài tập 11.10 (Một hệ số DCT và một đoạn mã độ dài loạt; mới) | Bài tập 11.10 mới theo quyết định I.6 số 15 (mục tiêu 5: tính một hệ số DCT, lập bộ ba RLE) |
| Mục 6 Chọn phương pháp nén (`-17`) | Ví dụ 11.14 (Ba bộ nén từ điển trên chuỗi `aabaacabcabcb`); danh sách điểm hòa vốn; bảng `Phương pháp \| Đặc tả \| Dư thừa khai thác \| Trạng thái \| Bảo đảm \| Chi phí`; Nhận xét 11.36 (Dấu hiệu chọn phương pháp); Bài tập 11.11 (Chọn phương pháp cho ba kho) | Ví dụ 11.14 ghi **đủ sáu cặp LZ78** (thêm $(2,\mathrm c)$, $(5,\mathrm b)$; quyết định I.6 số 11): LZ77 5 bộ ba × 14 bit = 70 bit; LZ78 6 cặp × 12 bit = 72 bit (giả sử mã cụm 3 bit); LZW 10 mã × 9 bit = 90 bit; so với 104 bit. Điểm hòa vốn: 1,75 / 3 (LZ77), 3,125 (LZ78, $M=2^{16}$), 1,125 / 1,5 (LZW). Bài tập 11.11 là bài chọn phương pháp (trước là 11.10) |

Kết mục và câu nối một phía ở mọi ranh giới đã được vai mạch kiểm (R-bảng mục 2 của `lec11-recheck-I6-mach.md`: đạt). Không có cầu nối sang Bài 12 (D13).


## 8. Ví dụ xuyên suốt (VP-DSFA-6, GC10)

| Tên gọi trong ghi chú | Dữ liệu | Nguồn | Dùng ở |
|---|---|---|---|
| chuỗi `aacaacabcabaaac` | 15 ký tự, $W=6$, $L=4$; ba bộ ba đầu | CMU-LZ trang chiếu 5 | Ví dụ 11.2, 11.3; Bài tập 11.12 (`exercises.md`, recitation) |
| chuỗi `aabaacabcabcb` | 13 ký tự; mã byte 97–99 (CMU in 112–114) | CMU-LZ trang chiếu 11, 13, 14, 17, 19 | Ví dụ 11.4, 11.5, 11.6, 11.7, 11.14; Bài tập 11.15 (`exercises.md`, tự kiểm) |
| ảnh CHEETAH.GS | $320\times200$, 64 000 byte; khối Hình 11.9 (điểm ảnh, DCT); khối đầu tiên Hình 11.11 (ô an toàn); bảng Hình 11.14 | NG tr. 258, 261, 265, 287 | Ví dụ 11.1, 11.9–11.13; Bài tập 11.1, 11.8, 11.9, 11.10; Tình huống 11.1, 11.2 |

Dữ liệu phụ: 100 chữ A (NG tr. 176, Bài tập 11.3); `DAD␣DADA␣DADDY␣DADO` (NG tr. 210–212, Bài tập 11.4); `␣WED␣WE␣WEE␣WEB␣WET` (NG tr. 214–215, Bài tập 11.5, Tình huống 11.3); IWOMBAT (NG tr. 217, Ví dụ 11.8(a)); `abababa` và chuỗi toàn chữ a (giả sử, Ví dụ 11.8(b), Bài tập 11.6); tên riêng 9 ký tự lặp cách hơn $W$ (giả sử, mở Mục 3); bộ Calgary (CMU-I trang chiếu 9–10, Tình huống 11.4); `abcd`, `(2,9,e)` (CMU-LZ trang chiếu 6, Bài tập 11.13).

## 9. Tình huống áp dụng (đúng như ghi chú, dòng 1719–1791)

Mở phần bằng danh sách bốn tình huống (mẫu Bài 10). Hai tình huống thỏa giả thiết, hai vi phạm giả thiết (GC-DSFA-12).

- **Tình huống 11.1 (Danh mục $1\,000$ ảnh)** — thỏa giả thiết. NG tr. 246 (ảnh VGA 256 màu theo bảng màu, $320\times200$, 1 byte mỗi điểm, 64 MB); "Giả sử ảnh xám 8 bit". Ngưỡng $E_{\mathrm{RMS}}\le10$. Cận cho bộ làm tròn $\beta(q)+\tfrac12$: $q=2$ cho $9{,}60\le10$; tách khỏi chương trình cắt thương của NG (cận khoảng 18,2) mà số đo Hình 11.14 thuộc về: $q=2$ cho 18 367 byte, sai số 6,9; kho khoảng 18,4 MB (giả sử như CHEETAH.GS). Chi phí $1\,024\,000$ phép nhân mỗi ảnh, khoảng $1{,}02\cdot10^9$ cả kho; bộ nhớ một dải $2\,560$ điểm.
- **Tình huống 11.2 (Nén từ điển cho ảnh chụp)** — vi phạm giả thiết cụm khớp dài. LZ77 với $W=4\,096$, $L=15$, bộ ba 24 bit. **Kịch bản "Giả sử mỗi bộ ba chỉ khớp $\ell=1$"** (thay kịch bản "không cụm nào khớp" của dàn ý, vốn không thể xảy ra khi $p\ge256$; quyết định I.6 số 6): $32\,000$ bộ ba, $768\,000$ bit $=96\,000$ byte, gấp 1,5 ảnh gốc; LZSS 9 bit mỗi điểm, $72\,000$ byte, hơn gốc 12,5%; cận trên $\le32\,000\cdot4\,096\cdot16\approx2{,}1\cdot10^9$ phép so (Mệnh đề 11.9(a)). Định lý 11.8 vẫn đúng; cái hỏng là tỷ lệ nén.
- **Tình huống 11.3 (LZW cho tệp ngắn)** — vi phạm giả thiết từ điển đã có cụm dài. LZW12: 12 mã + `END_OF_STREAM` = 13 mã × 12 bit = 156 bit = 19,5 byte > 19 byte; mã 9 bit không mã kết thúc: 13,5 byte; 18 phép tra, 11 phép thêm.
- **Tình huống 11.4 (Kho văn bản)** — mới so với dàn ý (quyết định I.6 số 13). Bộ Calgary (CMU-I trang chiếu 9), giả sử $n=10^9$ byte; gzip 2,59 bit mỗi ký tự (khoảng $3{,}2\cdot10^8$ byte, tiết kiệm 68%), LZ77 gốc 3,94 bit mỗi ký tự (khoảng $4{,}9\cdot10^8$ byte, 51%) (CMU-I trang chiếu 10); cận vét cạn $\approx6{,}6\cdot10^{13}$ phép so, giải mã $10^9$ phép ghi. Còn mở R2: câu "bộ mã hóa là LZ77 (Thuật toán 11.5) trong cài đặt kiểu gzip" nên nói gzip là biến thể không tham lam, Định lý 11.8 áp dụng nhờ phần Phạm vi.
- Ứng dụng (dòng 1785–1790): gzip (CMU-LZ trang chiếu 3, 8); `compress` dùng LZW (NG tr. 214), GIF (NG tr. 170); QIC-122, V.42bis (NG tr. 170–171); JPEG với Huffman hoặc mã số học của Bài 10 (NG tr. 261).

## 10. Phân loại chủ đề bốn nhóm (chỉ ở outline, GC17)

| `note-topic-id` | Chủ đề | Nhóm | Khối chính |
|---|---|---|---|
| `lec-11-topic-01` | Kiến thức tiên quyết | cầu nối | danh sách phát biểu lại |
| `lec-11-topic-02` | Hai đặc tả khôi phục | cốt lõi | Ví dụ 11.1; Định nghĩa 11.1; Mệnh đề 11.2; Nhận xét 11.3; Bài tập 11.1 |
| `lec-11-topic-03` | Giới hạn của nén khôi phục đúng | cầu nối, chu trình rút gọn | đoạn văn |
| `lec-11-topic-04` | Cửa sổ, bộ ba, mã hóa LZ77 | cốt lõi | Ví dụ 11.2; Định nghĩa 11.4; Thuật toán 11.5 |
| `lec-11-topic-05` | Giải mã, chép chồng lấn, tính đúng | cốt lõi; Bổ đề 11.7 bổ sung | Ví dụ 11.3; Thuật toán 11.6; Bổ đề 11.7; Định lý 11.8 |
| `lec-11-topic-06` | Chi phí, giá bộ ba, LZSS | cốt lõi; LZSS/gzip bổ sung; Wyner–Ziv đọc thêm | Mệnh đề 11.9; Nhận xét 11.10; Bài tập 11.2, 11.3 |
| `lec-11-topic-07` | Từ điển cụm, cây từ điển, mã hóa LZ78 | cốt lõi; Bổ đề 11.12 bổ sung | Ví dụ 11.4; Định nghĩa 11.11; Bổ đề 11.12; Thuật toán 11.13 |
| `lec-11-topic-08` | Giải mã và đồng bộ LZ78 | cốt lõi | Ví dụ 11.5; Thuật toán 11.14; Định lý 11.15 |
| `lec-11-topic-09` | Chi phí, từ điển đầy | cốt lõi, chu trình rút gọn | Mệnh đề 11.16; Nhận xét 11.17; Bài tập 11.4 |
| `lec-11-topic-10` | Từ điển nạp sẵn, mã hóa LZW | cốt lõi | Ví dụ 11.6; Định nghĩa 11.18; Thuật toán 11.19 |
| `lec-11-topic-11` | Giải mã LZW, độ trễ một mục, mã chưa có | cốt lõi; Bổ đề 11.21 bổ sung | Ví dụ 11.7, 11.8; Thuật toán 11.20; Bổ đề 11.21; Mệnh đề 11.22; Định lý 11.23 |
| `lec-11-topic-12` | Chi phí LZW, LZW12 | cốt lõi, chu trình rút gọn | Mệnh đề 11.24; Nhận xét 11.25; Bài tập 11.5, 11.6 |
| `lec-11-topic-13` | Khối $8\times8$, dịch mức, DCT, trực chuẩn | cốt lõi; Bổ đề 11.27, chứng minh Mệnh đề 11.28 bổ sung | Ví dụ 11.9, 11.10; Định nghĩa 11.26; Bổ đề 11.27; Mệnh đề 11.28 |
| `lec-11-topic-14` | Lượng tử hóa, sai số tái tạo | cốt lõi; Định lý 11.31 bổ sung (chứng minh của chương) | Định nghĩa 11.29; Ví dụ 11.11, 11.12; Mệnh đề 11.30; Định lý 11.31 |
| `lec-11-topic-15` | Sai phân DC, zigzag, mã độ dài loạt | cốt lõi; bộ $(r,0)$ là quy ước của chương | Định nghĩa 11.32; Mệnh đề 11.33; Ví dụ 11.13 |
| `lec-11-topic-16` | Đường ống JPEG cơ sở, chi phí | cốt lõi, chu trình gộp | Thuật toán 11.34; Nhận xét 11.35; Bài tập 11.7–11.10 |
| `lec-11-topic-17` | Chọn phương pháp nén | cốt lõi, chu trình rút gọn (tổng hợp) | Ví dụ 11.14; bảng; Nhận xét 11.36; Bài tập 11.11 |
| `lec-11-topic-18` | Tình huống áp dụng và ứng dụng | cốt lõi | Tình huống 11.1–11.4 |
| `lec-11-topic-19` | Tóm tắt chương | cốt lõi | đoạn kể dẫn Thuật toán 11.5, 11.6, 11.13, 11.14, 11.19, 11.20, 11.34 và chi phí từng thuật toán; kết quả theo mục; công thức; giả thiết hay quên |
| `lec-11-topic-20` | Bài tập củng cố | cốt lõi | một câu: "Bài tập 11.12–11.17 nằm trong tệp bài tập Bài 11" (dòng 1849) |
| `lec-11-topic-21` | Hướng dẫn đọc thêm và tài liệu tham khảo | đọc thêm | NG theo chương, tên mục và trang bản điện tử; CMU-I, CMU-LZ, CMU-L; CLRS Chương 2, 11; ba bài báo gốc theo NG; Wyner–Ziv ngoài phạm vi; mục "đọc thêm" một dòng (LZSS, LZW12.C, DCT.C) |

Đồ thị tiên quyết như dàn ý: 01 → mọi chủ đề; 02 → 03 → 04 → … → 12; 02 → 13 → 14 → 15 → 16; 12, 16 → 17 → 18 → 19; mọi chủ đề nội dung → 20. Giáo trình tham khảo cho từng mục: xem mục tham khảo của ghi chú (dòng 1852–1869); MIT 15.564 không được dẫn trong ghi chú (chỉ đối chiếu).

## 11. Độ dài thực tế (GC-DSFA-6)

`wc -w lecture-note.md` = 30 407 âm tiết (bản cuối, md5 `4b9cd9af…`), trong khoảng 12 000–32 000; không có mục `## Đọc thêm: …`. Bản v2 có 29 990; ước lượng của dàn ý là 30 450.

## 12. Hình của ghi chú (thực tế)

Mười SVG mới `note-*.svg` trong `2627-1/img/lec-11/`, sinh bởi `tools/courses/ds-foundation-algorithms/2627-1/img/lec-11/generate_note_svg.py`; mỗi hình dùng đúng một lần trong ghi chú:

| Tệp | Vị trí trong ghi chú |
|---|---|
| `note-cau-truc-chuong-11.svg` | mở Mục 1 |
| `note-hai-dac-ta.svg` | 1.1 |
| `note-lz77-cua-so.svg` | 2.1 |
| `note-lz77-chep-chong-lan.svg` | 2.2 |
| `note-lz78-cay.svg` | 3.2 (sau Ví dụ 11.5) |
| `note-lzw-ma-chua-co.svg` | 4.2 (vết `abababa`) |
| `note-jpeg-duong-ong.svg` | mở Mục 5 |
| `note-dct-ham-co-so.svg` | 5.1 |
| `note-zigzag-khoi-luong-tu.svg` | 5.3 (Ví dụ 11.13) |
| `note-cheetah-byte-rms.svg` | 5.4 (Nhận xét 11.35) |

Mười hai SVG cũ (`dct-basis`, `jpeg-pipeline`, `lz77-*`, `lz78-*`, `lzw-*`, `quantization`, `two-contracts`, `zigzag`) không còn được ghi chú dùng; deck cũ còn dẫn chúng. Giữ hay xóa quyết ở giai đoạn III (dựng lại deck). Không raster.


## 13. Điểm đã quyết, việc còn mở và ánh xạ số hiệu

### Các điểm D1–D13 của dàn ý sau khi soạn và biên tập

| Mã | Điểm | Trạng thái trong ghi chú |
|---|---|---|
| D1 | Sáu hay bảy mạch | ghi chú giữ sáu mục; chia mạch quyết ở storyboard (giai đoạn III) |
| D2 | Quy ước LZ77 | một quy ước $(d,\ell,c)$ khoảng lùi; CMU là khoảng lùi, NG là offset trong bộ đệm (dòng 259) |
| D3 | Mã byte LZW | 97–99 (quy ước đọc, dòng 74) |
| D4 | Số liệu JPEG | làm tròn; cả khối Hình 11.9 được lượng tử; Hình 11.11 chỉ ô an toàn (Bài tập 11.8); đính chính chỉ ở `review-log.md` |
| D5 | Kết thúc dòng | LZ77 không `EOS` ($p+\ell+1\le n$); LZ78 cặp $(i,\texttt{EOS})$, trường ký tự 9 bit; LZW mã đầu 256, đóng khung bằng số mã; LZW12 (256 = `END_OF_STREAM`, đầu 257) chỉ ở Nhận xét 11.25 và Tình huống 11.3 |
| D6 | Độ rộng mã LZW thay đổi | không có trong ghi chú |
| D7 | Vết đầy đủ cho mã chưa có | có: Ví dụ 11.8(b) `abababa`, viết "Giả sử" |
| D8 | "token" | bộ ba, cặp, mã; "đơn vị mã" là tên chung, ký hiệu số lượng $\tau$ |
| D9 | "nén mất dữ liệu" | theo tên bài |
| D10 | CMU-LZ trang chiếu 7 (LZSS) | **đã giải quyết (II.1):** Bài tập 11.14 vào `exercises.md`, không recitation, đề nêu $W=6$, $L=4$ của trang chiếu 5 (BT-DSFA-6); dùng cho trang bài tập tổng hợp của "Tổng kết" |
| D11 | Chứng minh của chương cho Bổ đề 11.27, Mệnh đề 11.28, Định lý 11.31 | giữ, nhóm `bổ sung` |
| D12 | "hệ số AC" | định nghĩa trong Định nghĩa 11.32 |
| D13 | Cầu nối sang Bài 12 | không viết |

Quyết định thêm khi biên tập (I.6, `lec11-I6-quyet-dinh.md`): mã độ dài loạt theo từng khối với bộ $(r,0)$ là quy ước của chương (số 7); Tình huống 11.2 kịch bản $\ell=1$ (số 6); Tình huống 11.4 Calgary (số 13); sáu cặp LZ78 trong Ví dụ 11.14 (số 11); thêm Bài tập 11.10 và câu con (số 15); $L$ không tính ký tự kế, NG ứng với $L=15$ (số 19); đổi chữ ký hiệu (số 1); CLRS theo chương (số 25).

### Việc đã giải quyết sau đồng bộ v2

- R1, R2, R3 của `lec11-recheck-I6-mach.md` đã sửa trong ghi chú bản cuối (xem mục "Kiểm lại lần 2" của `lec11-recheck-I6-*.md`): ký hiệu $\alpha$, $c$, $\sin\mu\pi$, $\sum_\xi$; cách gọi gzip ở Tình huống 11.4; độ phủ mục tiêu 2, 3, 6. Các ghi chú "R1/R2/R3 còn mở" ở mục 4, 7, 9, 14 của tệp này là lịch sử, không còn hiệu lực.
- D10: xem bảng trên.
- Danh sách `exercises.md` (II.1, `review-log.md` mục "Duyệt danh sách bài tập (II.1)"): chấp nhận 11.12–11.17; tiêu đề khối dạng `(Tên ngắn; CMU 15-499, <tệp>, trang chiếu N)`; 11.17 rút "Cosine or Fourier" thành "biến đổi cosine" (BT-DSFA-6, ghi chỗ chỉnh); 11.15 theo phương án A: giữ ghi chú, đề đòi quá trình (nút hiện tại, tra con, cây đủ sáu nút, kiểm Định lý 11.15(a) sau từng cặp).

### Rủi ro còn lại

- Lộ lời giải recitation: sáu cặp LZ78 ở Ví dụ 11.14 làm Bài tập 11.15 (CMU-LZ trang chiếu 13) thành bài tự kiểm (quyết định I.6 số 11); Mệnh đề 11.22 trả lời CMU-LZ trang chiếu 16; Mục 5.1 trả lời một phần CMU-L trang chiếu 11. Đề trong `exercises.md` yêu cầu dẫn số hiệu (BT10).
- Sai sót in của NG (Hình 11.9 ô (0,7), Hình 11.11 phép cắt và ô (1,3), mất dấu cách ở tr. 211, 215–216, IWOMBATI ở tr. 217, bảng số bit tr. 264): ghi chú dùng giá trị đúng; đính chính chỉ trong `review-log.md`.

### Ánh xạ số hiệu cũ → mới

| Cũ (ghi chú `a0bded9`; dàn ý trước biên tập) | Mới (ghi chú v2) |
|---|---|
| "Bài 1" (hoàn tất vết LZ77, CMU-LZ trang chiếu 5) | Bài tập 11.12 (`exercises.md`, recitation) |
| "Bài 2" (giải mã `(2,9,e)`, trang chiếu 6; đề cũ ghi sai "vị trí tuyệt đối") | Bài tập 11.13 (`exercises.md`, recitation; quy ước khoảng lùi) |
| — (CMU-LZ trang chiếu 7, LZSS) | Bài tập 11.14 (`exercises.md`, đề xuất D10) |
| "Bài 3" (hoàn tất vết LZ78, trang chiếu 13) | Bài tập 11.15 (`exercises.md`, recitation, thành bài tự kiểm) |
| "Bài 4" (độ trễ một mục LZW, trang chiếu 16) | Bài tập 11.16 (`exercises.md`, recitation) |
| "Bài 5" (chọn biến đổi, CMU-L trang chiếu 11) | Bài tập 11.17 (`exercises.md`, recitation) |
| bài không số §2.6 cũ (`(3,4,b)` sau `aac`) | Ví dụ 11.3 |
| bài không số §3.5 cũ (phần còn lại `abcabcb`) | bỏ; sáu cặp đầy đủ nằm ở Ví dụ 11.14 |
| bài không số §4.6 cũ ($w=\texttt{aba}$, 271) | bỏ; thay bằng Ví dụ 11.8 |
| bài không số §5.5 cũ (ô (0,2)) | Bài tập 11.8 |
| bài không số §6 cũ (kho ảnh xem trước) | bỏ; thay bằng Bài tập 11.11 |
| dàn ý: Bài tập 11.6 "Ba bộ nén từ điển trên một chuỗi" | Ví dụ 11.14; Bài tập 11.6 là "Chuỗi toàn chữ a" |
| dàn ý: Bài tập 11.10 "Chọn phương pháp cho ba kho" | Bài tập 11.11; Bài tập 11.10 mới là "Một hệ số DCT và một đoạn mã độ dài loạt" |
| dàn ý: `exercises.md` 11.11–11.16 | 11.12–11.17 |
| dàn ý: Tình huống 11.1–11.3 | Tình huống 11.1–11.3 giữ số; thêm Tình huống 11.4 (Kho văn bản, Calgary) |
| §1 cũ (bảng hai đặc tả) | Định nghĩa 11.1 |
| §2.4, §2.6, §2.7 cũ (LZ77) | Thuật toán 11.5, 11.6; Bổ đề 11.7; Định lý 11.8; Mệnh đề 11.9 |
| §3.4–3.6 cũ (LZ78) | Thuật toán 11.13, 11.14; Định lý 11.15; Mệnh đề 11.16 |
| §4.2–4.6 cũ (LZW) | Thuật toán 11.19, 11.20; Bổ đề 11.21; Mệnh đề 11.22; Định lý 11.23 |
| §4.7 cũ (độ rộng bit, $T=2^b$) | bỏ; còn Nhận xét 11.25 (LZW12) |
| §5.4–5.8 cũ (JPEG) | Định nghĩa 11.26, Mệnh đề 11.28; Định nghĩa 11.29, Mệnh đề 11.30, Định lý 11.31; Định nghĩa 11.32, Mệnh đề 11.33; Thuật toán 11.34 |
| `L11-N01` … `L11-N11` | `lec-11-topic-02/03`; `-04`; `-05/06`; `-07/08/09`; `-10`; `-11/12`; `-13/16`; `-13/14`; `-15/16`; `-17`; `-20` |

Mã trang deck cũ ánh xạ ở storyboard của giai đoạn III.

## 14. Bài tập cho `exercises.md` (BT-DSFA-1/2) và độ phủ mục tiêu

Nguồn duy nhất được phép: CMU 15-499 (BT-DSFA-2); NG không có bài tập. Số hiệu tiếp nối sau Bài tập 11.11 của ghi chú (BT4), khớp câu "Bài tập 11.12–11.17" của ghi chú; chốt ở giai đoạn II.1.

| Số | Nguồn | Nhiệm vụ | Lời giải đã chạy lại | Mức dự kiến | Recitation | Mục tiêu |
|---|---|---|---|---|---|---|
| 11.12 | CMU-LZ trang chiếu 5 | hoàn tất vết LZ77 `aacaacabcabaaac`, $W=6$, $L=4$ | $(3,3,\mathrm a)$, $(1,2,\mathrm c)$ | tính toán | có | 2 |
| 11.13 | CMU-LZ trang chiếu 6 | `abcd`, `(2,9,e)`; trường hợp $\ell>d$ | `abcdcdcdcdcdce` | nhận biết | có | 2 |
| 11.14 | CMU-LZ trang chiếu 7 | vết LZSS `(0,vị trí,độ dài)` hoặc `(1,ký tự)`, điền "?" | `(0,3,4)` với $W=6$, $L=4$ (đã chốt D10) | tính toán | không | 2 |
| 11.15 | CMU-LZ trang chiếu 13 | hoàn tất vết LZ78 `aabaacabcabcb`; phương án A: đề đòi quá trình (nút hiện tại, tra con, cây đủ sáu nút, kiểm Định lý 11.15(a) sau từng cặp) | $(2,\mathrm c)$, $(5,\mathrm b)$ (cũng có ở Ví dụ 11.14) | tính toán | có (tự kiểm) | 3 |
| 11.16 | CMU-LZ trang chiếu 16 | `…SSc…`, `S[0]=c`: bộ giải mã làm gì với mã chưa có; chứng minh | $D[id_2]=S\,S[0]$ (Mệnh đề 11.22) | chứng minh | có | 4 |
| 11.17 | CMU-L trang chiếu 11 | ba mục tiêu chọn biến đổi; vì sao biến đổi cosine trên toàn ảnh kém (rút "Cosine or Fourier", BT-DSFA-6); khắc phục | dựa NG tr. 255 | vận dụng | có | 5, 6 |

Độ phủ mục tiêu ↔ bài tập (BT9, BT-DSFA-7), theo ghi chú v2 và mục 4 của `lec11-recheck-I6-mach.md`:

| Mục tiêu | Kết quả hoặc ví dụ | Bài tập trong ghi chú | Bài tập trong `exercises.md` | Ghi chú |
|---|---|---|---|---|
| 1 Hai đặc tả, tốc độ bit, RMS, Mệnh đề 11.2 | Ví dụ 11.1; Định nghĩa 11.1; Mệnh đề 11.2 | 11.1 (a)–(c) tốc độ bit; (d) tính RMS; (e) Mệnh đề 11.2 | — | không có bài nguồn; dựa Bài tập 11.1 |
| 2 LZ77 | Ví dụ 11.2, 11.3; Định lý 11.8; Mệnh đề 11.9 | 11.2, 11.3 | 11.12, 11.13, 11.14 | chưa có bài chứng minh tính đúng (R3); có thể đặt yêu cầu giải thích tính đúng vào 11.13 |
| 3 LZ78 | Ví dụ 11.4, 11.5, 11.14; Định lý 11.15 | 11.4 (a)–(d) | 11.15 | 11.4(d) chứng minh quy nạp tính đôi một khác nhau, chưa phải đồng bộ (R3) |
| 4 LZW | Ví dụ 11.6–11.8; Mệnh đề 11.22; Định lý 11.23 | 11.5; 11.6 (c) chứng minh | 11.16 | mã hóa LZW không có bài nguồn; dựa 11.5, 11.6 |
| 5 DCT, lượng tử, zigzag, RLE, sai số | Ví dụ 11.9–11.13; Định lý 11.31 | 11.7, 11.8, 11.9; 11.10 (a) một hệ số DCT, (b) bộ RLE | 11.17 (định tính) | phép tính số JPEG không có bài nguồn; dựa 11.7–11.10 |
| 6 Chọn phương pháp | Ví dụ 11.14; bảng Mục 6; Nhận xét 11.36 | 11.11 (đặc tả, dư thừa, dung lượng) | 11.17 (một phần) | 11.11 chưa hỏi chi phí bộ nhớ (R3) |

Ba mức đều có bài: nhận biết 11.13; tính toán hoặc chứng minh 11.12, 11.14, 11.15, 11.16; vận dụng 11.17. Không có `## Thực hành` (BT-DSFA-9). Tiêu đề khối: `::: exercise Bài tập 11.k (Tên ngắn; CMU 15-499, <tệp>, trang chiếu N)`. Trang bài tập tổng hợp của "Tổng kết" (NT15, NT-DSFA-10) dùng 11.14 (đã chốt II.1). Lý do "không có bài nguồn" ghi vào `review-log.md` ở giai đoạn II.
