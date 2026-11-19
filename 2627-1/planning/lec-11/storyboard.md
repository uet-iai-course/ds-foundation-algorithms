# Storyboard Bài 11 — Nén bằng từ điển và nén mất dữ liệu (dựng lại theo NT, 2026-11-19)

> Tệp planning, không công khai. Thay toàn bộ storyboard cũ (bản cũ còn trong git; mã trang cũ `P00`…`X05`, `LT`…`XT` ánh xạ ở mục 11). Người lập: tác tử lập storyboard, giai đoạn III.1 của `planning/lec-11/prompt-xay-dung-bai-11.md`; chờ cổng storyboard (III.2) và điều phối viên duyệt.
>
> **Căn cứ.** Quyết định Q1–Q10 (người dùng 2026-11-19, theo cột "Đề xuất"): Q1 dựng lại deck, giữ tên tệp `lecture-11-nen-bang-tu-dien-va-nen-mat-du-lieu.html`; Q2 = NT-DSFA-11 (giảng 42–50 trang, trần 55; recitation 6–10); Q3 = NT-DSFA-10 (recitation là `<section>` ngoài riêng sau "Tổng kết"); Q7 = NT-DSFA-12; Q8 "phân phối"; Q9 phạm vi JPEG cơ sở. Quy định: `NGUYEN-TAC-TRANG-CHIEU.md` (NT1–NT28), `NGUYEN-TAC-HOC-PHAN.md` (mục 3: P1–P11, NT-DSFA-6…12; mục 5; mục 6), `AGENTS.md` ("Tham số trang chiếu của học phần" P1–P11, NT-DSFA-1…5; "Mẫu RevealJS bắt buộc"; "Trang tiêu đề mạch"; "Mở một khái niệm hoặc một thuật toán"; "Quy trình đa tác tử cho bộ trang chiếu"), `CLAUDE.md` của học phần ("Deck structure and content", "Writing"), `NGUYEN-TAC-VAN-PHONG.md` (VP1–VP24), GC-DSFA-1 (sinh viên năm 2), GC-DSFA-4, GC-DSFA-9, GC-DSFA-10, BT-DSFA-6, BT-DSFA-11.
>
> **Nguồn nội dung (P1 = `deck nguồn + ghi chú`).** Ghi chú `materials/lec-11/lecture-note.md` bản cuối (md5 `4b9cd9af…`, 30 407 âm tiết; số dòng dẫn trong tệp này là của bản đó) là chuẩn cho ký hiệu, phát biểu, số liệu (NT1, NT2); `materials/lec-11/exercises.md` bản hiện hành (md5 `d51a0647c0527bb16a06f9de53898315`, commit `91b781f`; Bài tập 11.12–11.17; đề, câu hỏi, gợi ý, lời giải của phần recitation và Bài tập 11.14 lấy đúng câu chữ bản này); `planning/lec-11/outline.md` (mạch–mục, `note-topic-id`, thuật ngữ). Deck nguồn: CMU 15-499 `compression3-lz.pdf` (viết tắt **LZ tc. N**) và `compression4-lossy.pdf` (**L tc. N**), "tc. N" là số "Page N" in dưới trang chiếu (bốn trang chiếu mỗi trang PDF; đã đọc cả 8 + 5 trang PDF liên quan). Viết tắt sách: **NG** = Nelson và Gailly, ấn bản 2, số trang PDF.
>
> **Đã chạy lại** (GC26, script trong scratchpad của phiên, không vào repo): LZ77 trên `aacaacabcabaaac` ($W=6$, $L=4$) cho $(0,0,\mathrm a)$, $(1,1,\mathrm c)$, $(3,4,\mathrm b)$, $(3,3,\mathrm a)$, $(1,2,\mathrm c)$; trên `aabaacabcabcb` cho 5 bộ ba, 70 bit; 100 chữ A cho 8 bộ ba; LZSS kiểu gzip (Bài tập 11.14) cho 10 mục, $(0,3,4)$ ở mục thứ tư; LZ78 trên `aabaacabcabcb` cho 6 cặp, trên `DAD␣DADA␣DADDY␣DADO` cho 9 cặp; LZW cho 97, 97, 98, 256, 99, 257, 260, 98, 99, 98, cho `abababa` là 97, 98, 256, 258; $\sum Q_{uv}^2=5\,856$, $21\,184$, $124\,384$ và $\beta(q)\approx4{,}78$; $9{,}10$; $22{,}04$ với $q=1,2,5$; cận của chương trình NG $9{,}60$; $18{,}23$; $44{,}12$; RMS của hàng tám điểm (Bài tập 11.1(d)) $\sqrt{17}\approx4{,}12$. Tất cả khớp ghi chú và `exercises.md`. Người viết deck và vai rà độ chính xác vẫn phải tự chạy lại.

## 0. Tóm tắt quyết định

- **Sáu mạch nội dung** (NT10): 1 Mở đầu, 2 LZ77, 3 LZ78, 4 LZW, 5 JPEG, 6 Tổng kết; recitation là `<section>` ngoài thứ bảy, không tính vào 5–7 (NT-DSFA-10). Mạch JPEG không tách (D-SB3).
- **Số trang:** giảng **55** (trần NT-DSFA-11, có lý do ở mục 12), recitation **11** (vượt khoảng 6–10, có lý do ở mục 12), tổng 66.
- **Bài tập có "Lời giải:" trên trang kế tiếp (NT24), mỗi cụm khái niệm lớn một bài:** hai đặc tả: Bài tập 11.1(b) (`s01-09`, `s01-10`); LZ77: Bài tập 11.14 (`s06-04`, `s06-05`); LZ78: 11.15; LZW: 11.16; JPEG: 11.17 (recitation). Lời giải 11.12 và 11.13 chỉ ở ghi chú diễn giả.
- **Ví dụ xuyên suốt** (VP-DSFA-6): chuỗi `aacaacabcabaaac` (LZ77), chuỗi `aabaacabcabcb` (LZ78, LZW, so sánh), ảnh CHEETAH.GS và khối Hình 11.9 của NG (JPEG). Bỏ chuỗi `ppqpprpqrpqrq`, mã 112–114, đổi độ rộng mã LZW, ô $(0,2)$/$(0,4)$ làm ví dụ chính của deck cũ (outline D3, D6, D4).
- **Mã trang** `lec11-sKK-mm` (P7): mạch $K=01$…$07$; trang tiêu đề mạch `lec11-sKK-00`, `id="mach-K"` với $K=2$…$7$; mạch 1 không có trang tiêu đề mạch (bìa là trang tiêu đề). Mạch $K$ mở tại `#/K` (`hashOneBasedIndex: true`).
- **Hình:** tám bản `-trang-chieu.svg` vẽ lại từ cùng dữ liệu của hình ghi chú (mục 9); không raster; SVG của deck cũ bị xóa trong commit deck (D-SB5).
- **Lớp gốc:** `<div class="reveal course-deck lecture-compression-dict">`; dùng lại các lớp sẵn có (`.example-slide`, `.ex-grid2`, `.ex-table`, `.cost-table`, `.stream-figure`, `.agenda-slide`, `.strand-title`); luật CSS riêng do điều phối viên thêm vào `lecture-course.css` khi người viết deck cần (D-SB10).

### Quyết định của điều phối viên (2026-11-19) cho các điểm D-SB của bản storyboard đầu

| Mã | Quyết định | Thay đổi trong storyboard |
|---|---|---|
| D-SB1 | Cụm "hai đặc tả" phải có bài với "Lời giải:" (NT24): Bài tập 11.1, câu chọn hệ số chất lượng theo ngưỡng RMS trên bảng Hình 11.14; bù hai trang để giảng vẫn ≤ 55, không vượt mật độ | thêm `s01-09`, `s01-10` (Bài tập 11.1(b)); câu nối sang mạch 2 chuyển từ `s01-08` sang `s01-10`; mạch 5 từ 13 xuống 11 trang: Mệnh đề 11.28 và 11.30 phát biểu tại bước dùng của ý tưởng chứng minh Định lý 11.31 (`s05-06`), Ví dụ 11.10 thành một dòng ở `s05-03`, Ví dụ 11.11 gộp vào trang "Lượng tử hóa" (`s05-04`) |
| D-SB2 | Chấp nhận giảng tới 55 trang với lý do đã ghi | mục 12 |
| D-SB3 | Không tách mạch JPEG | giữ 6 mạch nội dung |
| D-SB4 | Hậu tố hình `-trang-chieu.svg` như Bài 10 | mục 9 |
| D-SB5 | SVG cũ (`lz77-*.svg`, `lz78-*.svg`, `lzw-*.svg`, `dct-basis.svg`, `jpeg-pipeline.svg`, `quantization.svg`, `two-contracts.svg`, `zigzag.svg`) xóa trong commit deck nếu deck mới và ghi chú không tham chiếu | mục 9 |
| D-SB6 | Không có dòng nối sang Bài 12 (outline D13); điều phối viên giữ quyết định khi cổng III.2 đề nghị thêm: `sources/source.md` mục "Quan hệ tiên quyết sau điều chỉnh" không có quan hệ buổi 11 → buổi 12 | bỏ dòng "Bài sau" ở `s06-08` |
| D-SB7 | Lời giải 11.13 chỉ ở ghi chú diễn giả; đề 11.14 và 11.16 giữ nguyên dữ liệu, nhiệm vụ, câu hỏi như `exercises.md`, chỉ rút câu dẫn; trang đề vượt 80 âm tiết thì dồn dữ kiện vào bảng hoặc công thức, còn vượt thì ghi ngoại lệ có số trước/sau | `s06-04` khôi phục mọi điều kiện, dồn câu chọn dạng mục vào công thức; đề 11.16, 11.17 của bản hiện hành tách hai trang mỗi đề; lời giải 11.12 chuyển vào ghi chú diễn giả (cụm LZ77 có lời giải trên mặt trang ở Bài tập 11.14); ngoại lệ ghi số trước/sau ở mục 8 |
| D-SB8 | Bác: bảo đảm cho cả ảnh đứng đúng vị trí như ghi chú (sau Thuật toán 11.34) | dòng "Bảo đảm:" chuyển từ trang Định lý 11.31 sang câu kết của `s05-10`, trang ngay sau Thuật toán 11.34 |
| D-SB9 | Chấp nhận bảng "Bài tập về nhà" gồm 11.1–11.11 theo mục và 11.12–11.17 nếu ≤ 80 âm tiết | `s06-07` khoảng 50 âm tiết, giữ một trang |
| D-SB10 | Lớp gốc `lecture-compression-dict` | mục 0 |
| hai đề xuất nhẹ | ghi vào mục 7, không sửa | mục 7 |

### Phát hiện của cổng storyboard III.2 (2026-11-19) và cách xử lý

Báo cáo cổng: `lec11-III2-cong-storyboard.md` (scratchpad của phiên điều phối): 1 chặn bàn giao, 7 nghiêm trọng, 9 trung bình, 19 nhẹ. Nguyên nhân chính: phần recitation lập từ một bản `exercises.md` cũ; nay mọi đề, câu hỏi, gợi ý, lời giải của 11.12–11.17 lấy từ bản md5 `d51a0647…` (commit `91b781f`). Đã áp dụng 35 phát hiện; 1 phát hiện bị điều phối viên bác. Kiểm lại (cùng ngày): 1 trung bình (hàng đề xuất 11.16 còn sót ở mục 7, đã xóa) và 7 nhẹ (đồng bộ mục 0, mục 4.3; dấu cách ở `s05-07`; miền chỉ số ở `s05-03`; lý do mục tiêu 3 ở `s07-10`; dòng dẫn `s07-00`) đã sửa; phát hiện nhẹ về con số kho văn bản trên `s06-03` không áp dụng vì vượt giới hạn mật độ 90 (lý do ở mục Âm tiết của trang).

| Mức | Trang | Xử lý |
|---|---|---|
| chặn bàn giao | `s07-05`–`s07-07`, `s04-06`, mục 7 | dựng lại đề và lời giải 11.16 từ bản hiện hành (hai câu (a)(b), dữ kiện $\chi S\chi S\chi$), đề tách hai trang; ghi chú diễn giả `s04-06`, `s07-07` sửa: bài tập áp dụng Mệnh đề 11.22(b), không chứng minh nó; bỏ đề xuất về câu dẫn 11.16 ở mục 7; md5 `exercises.md` ghi ở đầu tệp |
| nghiêm trọng | `s07-08`–`s07-10` | đề 11.17 nguyên văn ("và chi phí tính toán", nghĩa tại chỗ của "khử tương quan", "hàm cơ sở"), tách hai trang; lời giải theo câu chữ bản hiện hành ("không khử thêm được tương quan đáng kể", "ít lợi thêm") |
| nghiêm trọng | `s07-03` | đề và gợi ý 11.15 nguyên văn bản hiện hành |
| nghiêm trọng | `s02-01` | câu so sánh sửa theo ghi chú: mã từng ký hiệu thay mỗi ký hiệu bằng một từ mã, LZ77 thay cả cụm độ dài thay đổi bằng bộ ba cỡ cố định |
| nghiêm trọng | `s03-07` | "bỏ mục ít được dùng gần đây nhất (BTLZ)" như ghi chú |
| nghiêm trọng | `s06-03` | 70/72/90 bit chuyển vào ghi chú diễn giả kèm giả thiết; nêu ngưỡng 10; tách cận của bộ nén làm tròn khỏi số đo của chương trình cắt thương |
| nghiêm trọng | `s05-08` | Mệnh đề 11.33 có "Giả thiết:" trên mặt trang; "Chứng minh." và "vị trí 55" chuyển vào ghi chú diễn giả |
| nghiêm trọng | `s01-10` | câu nối giữ giả thiết mô hình bậc 0 ("mã Huffman theo tần suất từng ký hiệu") |
| trung bình | `s01-07` | câu đầu nêu vấn đề của mạch, vế sau là trực quan; bỏ nhãn "Trực quan." dùng sai chỗ |
| trung bình | `s01-09`, `s06-03`, mục 2 | "Nelson và Gailly" thay "NG", không "DCT" ở mạch 1; quy ước dòng nguồn trong ghi chú diễn giả |
| trung bình | `s05-06`, `s02-08` | "Nhắc lại:" ma trận trực chuẩn trên mặt trang `s05-06`; số bit của bộ đếm (Bài 08) nhắc ở `s01-02` |
| trung bình | `s05-06`, mục 4.2 | nhãn "Kỹ thuật." lên mặt trang ở bước 2 |
| trung bình | `s02-07` | bỏ số hiệu Bổ đề 11.7 khỏi mặt trang, nêu nội dung (chép theo $j$ tăng dần) |
| trung bình | `s05-05` | tiêu đề "Sai số tái tạo của một khối"; lý do rút gọn bước 7 của cụm Thuật toán 11.34 ghi ở mục Quyết định |
| trung bình | `s02-05`, `s03-04` | dòng đọc giả mã chuyển vào ghi chú diễn giả, trang còn 6 dòng; số dòng ghi ở mục Âm tiết |
| trung bình | ghi chú diễn giả nhiều trang | mã nội bộ, mã quyết định, số dòng, so sánh với deck cũ, quyết định nguồn chuyển sang Nguồn/Quyết định; quy ước mới ở mục 2 |
| trung bình | `s06-08` | **không áp dụng** (điều phối viên bác): không thêm dòng nối sang Bài 12 vì `sources/source.md` mục "Quan hệ tiên quyết sau điều chỉnh" không có quan hệ buổi 11 → buổi 12 (chỉ 10 → 11 và 12 → 13 → 14) |
| nhẹ | `s01-03` | mục tiêu 2 giữ "và cỡ vùng nhìn trước" |
| nhẹ | `s03-07`, recitation | bỏ "(CLRS, Chương 11)" khỏi mặt trang; dòng nguồn recitation không tên tệp |
| nhẹ | `s01-07`, `s02-03`, `s03-02`, `s05-01` | thêm "root mean squared error", "sliding window", "distance", "match length", "dictionary tree", "multiway tree", "Joint Photographic Experts Group" |
| nhẹ | `s02-02`, `s03-01`, `s04-01`, `s05-02`, `s05-08`, `s04-03` | thêm dòng "Xác định …"/"Tính …"; "Diễn giải:" ở `s02-02`, `s04-03` (thay nhãn "Kiểm tra:"); các trang khác kết bằng dòng kết quả vì đã sát trần; tiêu đề `s04-01` "Ví dụ: chuỗi `aabaacabcabcb`, mã LZW" |
| nhẹ | `s04-04`, `s01-07`, `s07-00`, `s02-05`/`s03-04` | sửa câu dẫn thiếu chữ, câu "bộ nén được phép gán", dòng dẫn `s07-00` thành câu trần thuật, bỏ cặp câu phủ định–khẳng định lặp khuôn |
| nhẹ | `s04-06` | bước 1: $k_{t+1}\le255+t$ suy từ phía bộ mã hóa |
| nhẹ | `s05-05` | so cận với $4{,}18$ ($E_{\mathrm{RMS}}(A,\tilde A)$), $4{,}21$ chỉ ở ghi chú diễn giả |
| nhẹ | `s05-06` | bất đẳng thức then chốt là công thức hiển thị |
| nhẹ | `s05-07` | thêm "vị trí zigzag của ô đếm từ 1"; $\delta_1$ ở ghi chú diễn giả |
| nhẹ | `s05-09` | câu dẫn "Chỉ bước lượng tử hóa phụ thuộc $q$." |
| nhẹ | `s01-07` | "với ngưỡng $\varepsilon\ge0$", $x\in\mathcal X$ |
| nhẹ | `s02-08` | "phép tìm vét cạn" |
| nhẹ | `s04-01` | câu hỏi giữ "và chuỗi"; con số 16 bit thay 25 bit ở ghi chú diễn giả (trang đã sát trần) |
| nhẹ | `s06-04`, mục 6 | lý do đặt bài có lời giải của cụm LZ77 ở "Tổng kết" ghi ở mục 6; ghi chú diễn giả nối với Định lý 11.8 |
| nhẹ | `s07-02` | đề và gợi ý 11.13 nguyên văn; mục Quyết định sửa |
| nhẹ | mục 5 | LZ tc. 22 (dàn bài), 23–31 (Burrows–Wheeler, ACB) |
| nhẹ | mục 12 | chuyển 3 phút từ mạch 5 sang mạch 6, 1 phút sang mạch 1 |
| nhẹ | mạch 6 | thứ tự theo NT15: bài tập tổng hợp (`s06-04`, `s06-05`) trước "Câu hỏi tự kiểm tra" (`s06-06`) |

## 1. Bảng mạch (NT10, NT13, GC-DSFA-4)

Thời lượng chỉ ghi ở đây (NT27). "Câu hỏi của mạch" xuất hiện trên trang nội dung đầu tiên của mạch (NT13).

| Mạch | Tên (trùng trang "Nội dung" và trang tiêu đề mạch) | Loại (`AGENTS.md`) | Câu hỏi của mạch | Đầu vào | Đầu ra | Mục ghi chú | `note-topic-id` | Trang tiêu đề | Số trang | Phút |
|---:|---|---|---|---|---|---|---|---|---:|---:|
| 1 | Mở đầu | giới thiệu và động lực; khái niệm | Bộ giải nén phải trả lại cái gì, và đo cái được, cái mất bằng gì? | Mệnh đề 10.2, Hệ quả 10.19, Định lý 10.34, Nhận xét 10.4 | Định nghĩa 11.1 (hai đặc tả, tốc độ bit, RMS), Mệnh đề 11.2, Bài tập 11.1(b); giới hạn: mã từng ký hiệu trả đủ bit cho mỗi lần lặp của cụm | khung + Mục 1 (1.1, 1.2) | `lec-11-topic-01`, `-02`, `-03` | bìa `lec11-s01-01` | 10 | 15 |
| 2 | Nén bằng cửa sổ trượt LZ77 | thuật toán và ví dụ vận dụng | Mã mỗi lần lặp của một cụm bằng số bit cố định thế nào, chỉ dùng đoạn vừa đọc còn giữ, để bộ giải mã dựng lại đúng chuỗi? | đặc tả khôi phục đúng; cụm lặp `aac` | Định nghĩa 11.4, Thuật toán 11.5, 11.6, Định lý 11.8, Mệnh đề 11.9; giới hạn: cụm cách hơn $W$ ký tự phải mã lại | Mục 2 (2.1–2.3) | `-04`, `-05`, `-06` | `lec11-s02-00` | 9 | 23 |
| 3 | Nén bằng từ điển cụm LZ78 | thuật toán và ví dụ vận dụng | Giữ những cụm nào, và bộ giải mã biết các cụm đó bằng cách nào khi không có cửa sổ văn bản? | giới hạn cửa sổ $W$ | Định nghĩa 11.11, Thuật toán 11.13, 11.14, Định lý 11.15, Mệnh đề 11.16; giới hạn: mỗi cặp mang một ký tự thô 9 bit | Mục 3 (3.1–3.3) | `-07`, `-08`, `-09` | `lec11-s03-00` | 8 | 17 |
| 4 | Nén LZW với từ điển nạp sẵn | thuật toán và ví dụ vận dụng | Bỏ ký tự thô khỏi mỗi đơn vị mã thế nào mà bộ giải mã vẫn dựng lại được từ điển và chuỗi? | cặp LZ78; Định lý 11.15 | Thuật toán 11.19, 11.20, Bổ đề 11.21, Mệnh đề 11.22, Định lý 11.23, Mệnh đề 11.24; giới hạn: chỉ khai thác cụm khớp đúng từng ký tự | Mục 4 (4.1–4.3) | `-10`, `-11`, `-12` | `lec11-s04-00` | 8 | 20 |
| 5 | Nén ảnh JPEG dựa trên biến đổi cosine rời rạc | khái niệm; thuật toán; chi phí | Với ảnh chỉ cần khôi phục gần đúng, bỏ phần nào để giảm byte mà sai số mỗi khối vẫn bị chặn? | đặc tả khôi phục gần đúng (Định nghĩa 11.1); ma trận trực chuẩn | Định nghĩa 11.26, 11.29, 11.32, Mệnh đề 11.28, 11.30, 11.33, Định lý 11.31, Thuật toán 11.34, chi phí $\Theta(m)$ | Mục 5 (5.1–5.4) | `-13`…`-16` | `lec11-s05-00` | 11 | 29 |
| 6 | Tổng kết | tổng kết | Chọn bộ nén nào cho một kho, với bảo đảm và chi phí nào? | mọi kết quả của mạch 1–5 | hai bảng tổng kết, câu trả lời có điều kiện cho câu hỏi trung tâm, bài tổng hợp 11.14 | Mục 6, Tình huống, Tóm tắt, tham khảo | `-17`, `-18`, `-19`, `-21` (bài tổng hợp từ `-20`) | `lec11-s06-00` | 9 | 16 |
| — | **Phần giảng** | | | | | | | | **55** | **120** |
| 7 | Bài tập trên lớp | bài tập (recitation, NT-DSFA-4) | Chạy tay và chứng minh trên năm bài CMU 15-499 | mạch 2–5 | đề 11.12, 11.13 (lời giải ở ghi chú diễn giả); đề và lời giải 11.15, 11.16, 11.17, khớp `exercises.md` | `exercises.md` | `-20` | `lec11-s07-00` | 11 | 60 |

Mỗi mạch nội dung gồm các mục liên tiếp của ghi chú; ranh giới mạch trùng ranh giới `##` (GC-DSFA-4). Câu nối giữa hai mạch (NT13) đặt ở câu kết của trang cuối mạch trước (trang chi phí hoặc trang mệnh đề cuối), đúng chỗ kết mục của ghi chú (GC15, GC-DSFA-3), và đồng thời là bước 1 "giới hạn của cách làm trước, có số" của cụm thuật toán kế tiếp (NT-DSFA-2).

## 2. Quy ước chung cho mọi trang

- Khung: `2627-1/lecture-template.html` (P7), bỏ chữ mẫu cũ đã bị thay: "Nhu cầu:", dòng dẫn "Muốn …", tên "Tổng kết và tự kiểm tra", "Bài tập vận dụng" (`NGUYEN-TAC-HOC-PHAN.md` mục 6); `<html lang="vi" data-lecture="11">`, viewport `width=device-width,initial-scale=1` (NT26); không `fragment`, không `<style>`; chân trang "Giải thuật nền tảng của Khoa học dữ liệu · Học kỳ 1, 2026–2027 · Bài 11".
- Ghi chú diễn giả (NT22, VP-DSFA-1): không "chúng ta", không mã trang, không thời lượng, không câu quy trình; 40–150 âm tiết (tới ~250 cho ý tưởng chứng minh, bài tập, lời giải); kết bằng `<p class="note-source"><strong>Nguồn:</strong> ghi chú bài giảng Bài 11, §k (khối 11.x); <Nelson và Gailly, tr. … hoặc Blelloch, CMU 15-499, phần …, trang chiếu …>.</p>`. Trang "Tính đúng:" được tới ~250 âm tiết (`NGUYEN-TAC-HOC-PHAN.md` mục 5). Dòng nguồn trên mặt trang chỉ ở trang đề recitation (NT-DSFA-8).
- Thuật ngữ (P2, NT21, outline mục 6): tiếng Anh trong ngoặc ở lần đầu trên trang nội dung (cửa sổ trượt (sliding window), vùng nhìn trước (look-ahead buffer), bộ ba (token), sao chép chồng lấn (overlapping copy), cây từ điển (trie), mã kế tiếp (`next_code`), biến đổi cosine rời rạc (discrete cosine transform, DCT), lượng tử hóa (quantization), thứ tự zigzag (zig-zag sequence), mã độ dài loạt (run-length encoding, RLE), sai số căn bình phương trung bình (root mean squared error, RMS), tốc độ bit (bit rate)). "Ký hiệu:" (không "Kí hiệu:"), dấu thập phân `0{,}8`, "véc-tơ", "phân phối", "Lời giải".
- **Phần "Ghi chú diễn giả" của mỗi trang** chỉ chứa câu dành cho giảng viên và người học, viết như sẽ đưa vào `<aside class="notes">`: không mã trang, không mã quyết định (D-SB…, D…), không mã quy định (NT…, BT-DSFA…), không số dòng của ghi chú, không so sánh với deck cũ hay quyết định nguồn; các thông tin đó nằm ở **Nguồn** và **Quyết định** (VP8, NT22, NT-DSFA-12). Trên mặt trang và trong ghi chú diễn giả, "NG" viết "Nelson và Gailly", "CMU LZ tc. N"/"L tc. N" viết "Blelloch, CMU 15-499, phần nén bằng từ điển (phần nén mất dữ liệu), trang chiếu N"; viết tắt NG, LZ tc., L tc. chỉ dùng trong storyboard.
- Ký tự đứng riêng viết chữ đứng $\mathrm a$; chuỗi trong `code`; dấu cách `␣`; mã byte $\mathrm a\mapsto97$ (ghi chú dòng 76–78). Không `\text{}` chứa tiếng Việt trong KaTeX; công thức dài dùng `aligned`, không `\tag` (NT26).
- Giả mã là các bước đánh số bằng câu tiếng Việt và công thức như khối `algorithm` của ghi chú (GC-DSFA-9), dùng `<ol>` lồng, đúng ký hiệu của ví dụ chạy tay đứng trước.
- Số âm tiết ghi ở mỗi trang là **ước lượng** của người lập (đếm token chữ, không tính tiêu đề, KaTeX, số trong ô bảng, nhãn hình); số chính thức lấy từ `deck_lint.py` (NT17).

## 3. Từng trang

Mỗi mục: mã trang — tiêu đề; **Chức năng** (bước của hành trình NT8 hoặc của tám bước NT-DSFA-2); **Mặt trang** (văn bản dự kiến, đã qua `no-ai-slop` Edit; người viết deck được rút chữ nhưng không bỏ giả thiết, lượng từ, số); **Nguồn** (ghi chú: mục, khối, dòng; CMU); **Ghi chú diễn giả** (ý); **Quyết định** so với deck cũ; **Âm tiết** (ước lượng mặt trang).

### Mạch 1 — Mở đầu (`<section>` ngoài đầu tiên, không có trang tiêu đề mạch)

#### `lec11-s01-01` — Nén bằng từ điển và nén mất dữ liệu (bìa)
- **Chức năng:** bìa NT11; trang tiêu đề của mạch 1.
- **Mặt trang:** `h1` "Nén bằng từ điển và nén mất dữ liệu"; phụ đề "Bài 11 · LZ77, LZ78, LZW và JPEG"; luận đề (một câu, có điều kiện): "Khi dữ liệu phải khôi phục đúng, nén bằng từ điển thay mỗi cụm lặp bằng một đơn vị mã mà bộ giải mã tự dựng lại được; khi chỉ cần khôi phục gần đúng, lượng tử hóa các hệ số cosine đổi số byte lấy một sai số bị chặn theo bước lượng tử."; dòng học phần, học kỳ ("Học kỳ 1 · Năm học 2026–2027"), đơn vị. Không ghi công MMDS (bài không neo MMDS).
- **Nguồn:** ghi chú dòng 3 (đoạn giới thiệu), Tóm tắt chương dòng 1802.
- **Ghi chú diễn giả:** Bài 10 mã từng ký hiệu theo một mô hình đếm; bài này thêm hai họ bộ nén cho hai đặc tả khôi phục. Nguồn: Nelson và Gailly, *The Data Compression Book*, Chương 8, 9, 11; Blelloch, CMU 15-499, phần nén bằng từ điển và phần nén mất dữ liệu.
- **Quyết định:** sửa (`P00`): thêm luận đề có điều kiện; bỏ chữ viết tắt DCT khỏi luận đề (NT9).
- **Âm tiết:** ~60 (luận đề ~50).
- **Âm tiết (`deck_lint`, bản III.5):** 76 (bản v1: 88).
- **Sửa III.5:** luận đề rút còn một câu ngắn hơn ("Dữ liệu phải khôi phục đúng được nén bằng từ điển cụm …; ảnh chỉ cần khôi phục gần đúng được nén bằng lượng tử hóa hệ số cosine, với sai số bị chặn theo bước lượng tử."); ghi chú diễn giả đổi chủ ngữ.

#### `lec11-s01-02` — Tiên quyết và quy ước
- **Chức năng:** NT11, NT9 (nhắc lại kết quả Bài 10 có số hiệu).
- **Mặt trang:**
  - "**Nhắc lại:**" danh sách bốn ý: "không bộ mã khôi phục đúng nào rút ngắn mọi thông điệp (Mệnh đề 10.2)"; "mã Huffman dùng dưới $H(P)+1$ bit mỗi ký hiệu (Hệ quả 10.19), mã số học dưới $I(x)+2$ bit cho thông điệp $x$ (Định lý 10.34)"; "hai phía dùng chung bảng chữ cái, quy tắc mã và cách dừng (Nhận xét 10.4)"; "một đại lượng nhận $r+1$ giá trị cần $\lceil\log_2(r+1)\rceil$ bit (Bài 08, Mục 1.4)".
  - "**Ký hiệu:** chuỗi $x=x_1\cdots x_n$ trên $\Sigma$, $\lvert\Sigma\rvert=256$, đoạn $x[i..j]$; $m$ số mẫu; $\varphi$, $\psi$ là bộ nén, bộ giải nén."
  - Không nhắc ở đây: bảng băm (dòng "Mô hình:" của `lec11-s03-07`), ma trận trực chuẩn (dòng "Nhắc lại:" ở `lec11-s05-06`), bất biến vòng lặp (dòng "Nhắc lại:" ở `lec11-s02-07`, NT7). Số bit của một bộ đếm (Bài 08) được nhắc ở đây vì `lec11-s02-08` dùng nó (cổng III.2); quy ước chỉ số từ 0 nằm trong Định nghĩa 11.26 (`lec11-s05-03`).
- **Nguồn:** ghi chú "Kiến thức tiên quyết" dòng 25–30, "Bảng ký hiệu" dòng 43–50, quy ước đọc dòng 75–78.
- **Ghi chú diễn giả:** vì sao cần từng ý: Mệnh đề 10.2 dùng ở Mệnh đề 11.2; Hệ quả 10.19 giải thích vì sao ảnh chụp gần như không nén được bằng Huffman; Nhận xét 10.4 là gốc của các giả thiết "cùng quy tắc" ở Định lý 11.15, 11.23; mã byte $\mathrm a\mapsto97$; dấu cách viết `␣`.
- **Quyết định:** thêm (deck cũ không có).
- **Âm tiết:** ~62 (sát trần; nếu `deck_lint` > 60 thì bỏ cụm "cho thông điệp $x$" và "đoạn $x[i..j]$", không thêm ngoại lệ).
- **Âm tiết (`deck_lint`, bản III.5):** 60 (bản v1: 58).
- **Sửa III.5:** "$H(P)+1$" thành "entropy cộng 1" (tránh trùng chữ $P$ với khối điểm ảnh); bộ đếm không ghi số mục ở mặt trang (Bài 08, Mục 1.4 trong ghi chú diễn giả); "Ký hiệu:" bỏ $\varphi$, $\psi$ (định nghĩa ở `s01-07`).

#### `lec11-s01-03` — Mục tiêu học tập (mục tiêu 1–3)
- **Chức năng:** NT11; giữ đủ sáu mục tiêu của ghi chú, đúng nghĩa, đủ động từ; tách hai trang vì sáu mục tiêu ~160 âm tiết, vượt 1,5 lần trần 80 (NT17).
- **Mặt trang:** "Sau bài, người học có thể:" rồi `ol`:
  1. Phân biệt đặc tả khôi phục đúng với đặc tả khôi phục gần đúng, tính tốc độ bit và sai số căn bình phương trung bình, chứng minh rằng bộ nén rút ngắn mọi đầu vào phải làm mất dữ liệu.
  2. Mã hóa và giải mã LZ77 bằng bộ ba khoảng lùi–độ dài–ký tự, kể cả khi chép chồng lấn, chứng minh bộ giải mã khôi phục đúng và đếm chi phí theo cỡ cửa sổ và cỡ vùng nhìn trước.
  3. Mã hóa và giải mã LZ78, dựng cây từ điển và chứng minh bằng quy nạp rằng hai phía giữ cùng từ điển.
- **Nguồn:** ghi chú dòng 11–13 (Q6: deck bỏ "(Mục k)" vì mục ghi chú không phải mạch deck).
- **Ghi chú diễn giả:** mỗi mục tiêu ứng với sản phẩm kiểm được: tính $R$, $E_{\mathrm{RMS}}$ (Bài tập 11.1); vết LZ77 (Bài tập 11.12, 11.13); vết và cây LZ78 (Bài tập 11.15).
- **Quyết định:** sửa (`P01`): theo mục tiêu ghi chú mới; tách hai trang; mục tiêu 2 giữ đủ "cỡ cửa sổ và cỡ vùng nhìn trước" (cổng III.2).
- **Âm tiết:** ~84. **Ngoại lệ mật độ** (mục 8): trang mục tiêu giữ đúng nghĩa ghi chú (NT17); trần 80, giới hạn 120.
- **Âm tiết (`deck_lint`, bản III.5):** 113.

#### `lec11-s01-04` — Mục tiêu học tập (mục tiêu 4–6)
- **Chức năng:** như trên; `ol start="4"`.
- **Mặt trang:**
  4. Mã hóa và giải mã LZW, xử lý mã chưa có trong từ điển của bộ giải mã và chứng minh mã đó chỉ có thể là mã kế tiếp.
  5. Tính biến đổi cosine, lượng tử hóa, thứ tự zigzag và mã độ dài loạt trên một khối $8\times8$, chỉ ra bước làm mất dữ liệu và chặn sai số tái tạo theo bước lượng tử.
  6. Chọn phương pháp nén cho một kho theo đặc tả khôi phục, dạng dư thừa của dữ liệu và chi phí bộ nhớ.
- **Nguồn:** ghi chú dòng 14–16.
- **Ghi chú diễn giả:** sản phẩm kiểm: Bài tập 11.16 (mã chưa có), 11.7–11.10, 11.17 (JPEG), 11.11 (chọn phương pháp).
- **Quyết định:** thêm (trang thứ hai của mục tiêu).
- **Âm tiết:** ~75.
- **Âm tiết (`deck_lint`, bản III.5):** 90.

#### `lec11-s01-05` — Nội dung
- **Chức năng:** NT11; danh sách đánh số mọi mạch, liên kết `#/N`, tên trùng trang tiêu đề mạch; recitation có mục (NT-DSFA-10).
- **Mặt trang:** `ol` có liên kết: 1. Mở đầu (`#/1`); 2. Nén bằng cửa sổ trượt LZ77 (`#/2`); 3. Nén bằng từ điển cụm LZ78 (`#/3`); 4. Nén LZW với từ điển nạp sẵn (`#/4`); 5. Nén ảnh JPEG dựa trên biến đổi cosine rời rạc (`#/5`); 6. Tổng kết (`#/6`); 7. Bài tập trên lớp (`#/7`). "**Đọc trước:** Nelson và Gailly, *The Data Compression Book*, Chương 8, 9, 11."
- **Nguồn:** outline mục 2; ghi chú "Hướng dẫn đọc thêm" dòng 1863–1867.
- **Ghi chú diễn giả:** một câu cho mỗi mạch, nêu quan hệ: mạch 2–4 cùng giữ $y=x$, mỗi mạch sửa một giới hạn của mạch trước; mạch 5 đổi đặc tả; mạch 6 đặt các bảo đảm cạnh nhau.
- **Quyết định:** sửa (`P03`): tên mạch mới, thêm mục 7, liên kết `#/N`.
- **Âm tiết:** ~55.
- **Âm tiết (`deck_lint`, bản III.5):** 45; 8 dòng (bản v1: 46).
- **Sửa III.5:** "Đọc trước:" Chương 7–9, 11, khớp "Tài liệu tham khảo".

#### `lec11-s01-06` — Vấn đề trung tâm
- **Chức năng:** NT11, NT-DSFA-5: một hộp "Câu hỏi:" duy nhất, đúng câu hỏi trung tâm của ghi chú (dòng 90), có dữ liệu, đầu ra, giới hạn.
- **Mặt trang:** hộp `.question-box`: "**Câu hỏi:** Một kho văn bản phải khôi phục đúng từng byte; một danh mục $1\,000$ ảnh, 64 MB, chỉ cần khôi phục gần đúng. Thuật toán nào đạt từng đặc tả trong một lượt đọc với bộ nhớ hữu hạn, và đổi lại được bao nhiêu byte?"
- **Nguồn:** ghi chú dòng 86–90 (NG tr. 208, 246); outline mục 1; `sources/source.md` dòng 403.
- **Ghi chú diễn giả:** câu trả lời theo từng mạch, mỗi mạch một câu: mạch 2 cửa sổ $W$ cho cụm lặp gần; mạch 3–4 từ điển $M$ mục cho cụm lặp xa; mạch 5 lượng tử hóa đổi byte lấy sai số $\le\beta(q)$; mạch 6 thu hồi con số 64 MB. Giới hạn: một lượt, cửa sổ 4 096 byte hoặc từ điển 4 096 mục (Nelson và Gailly, tr. 179, 220).
- **Quyết định:** thêm.
- **Âm tiết:** ~45.
- **Âm tiết (`deck_lint`, bản III.5):** 47.

#### `lec11-s01-07` — Hai đặc tả khôi phục
- **Chức năng:** hành trình khái niệm "hai đặc tả" (NT8): vấn đề và ví dụ (Ví dụ 11.1, cột trái) → phát biểu (Định nghĩa 11.1, cột phải); trang nội dung đầu của mạch 1 mang câu hỏi của mạch (NT13) dưới dạng câu khẳng định đầu trang.
- **Mặt trang:** câu đầu (vấn đề của mạch, NT13; vế sau là trực quan, NT8): "Bộ giải nén phải trả lại ảnh gốc, hoặc chỉ một ảnh gần nó; khi chỉ cần gần, bộ nén được phép gán cùng một dòng bit cho nhiều ảnh." Bố cục `.ex-grid2`.
  - Trái, "**Ví dụ 11.1.** Ảnh CHEETAH.GS, $64\,000$ điểm, 8 bit mỗi điểm, nén ở hệ số chất lượng (quality factor) $q$:" bảng `$q$ | byte | bit mỗi điểm | RMS`: 1 | $27\,809$ | $3{,}48$ | $4{,}3$; 2 | $18\,367$ | $2{,}30$ | $6{,}9$; 25 | $5\,094$ | $0{,}64$ | $17{,}4$.
  - Phải, "**Định nghĩa 11.1.**" với $\varphi:\mathcal X\to\{0,1\}^*$, $\psi:\{0,1\}^*\to\mathcal X$: tốc độ bit (bit rate) $R(x)=\lvert\varphi(x)\rvert/m$; sai số căn bình phương trung bình (root mean squared error, RMS) $E_{\mathrm{RMS}}(x,y)=\sqrt{\tfrac1m\sum_{i}(x_i-y_i)^2}$; khôi phục đúng: $\psi(\varphi(x))=x$ với mọi $x$; khôi phục gần đúng, với ngưỡng $\varepsilon\ge0$: $E_{\mathrm{RMS}}(x,\psi(\varphi(x)))\le\varepsilon$ với mọi $x\in\mathcal X$.
- **Nguồn:** ghi chú 1.1, Ví dụ 11.1 (dòng 103–119; NG Hình 11.14, tr. 287), Định nghĩa 11.1 (dòng 123–132). CMU: LZ tc. 2 và L tc. 1–2 (lossy/lossless) chỉ đối chiếu.
- **Ghi chú diễn giả:** $R=8\cdot\text{byte}/64\,000$; từ $q=1$ tới $q=25$ số byte giảm khoảng 5,5 lần, sai số tăng khoảng 4 lần; khôi phục đúng là trường hợp $\varepsilon=0$; nhầm lẫn: hai ảnh cùng RMS chưa chắc giống nhau về mắt (60 điểm đúng, 4 điểm lệch 8 mức cũng cho RMS 2).
- **Quyết định:** sửa (`P02` "Hai đặc tả khôi phục" và `J01` "Tốc độ bit và sai số"): gộp về Mục 1 như ghi chú; thay hình `two-contracts.svg` bằng bảng số đo có nguồn.
- **Âm tiết:** ~76 (số trong bảng không tính; bản đầu ~65, tăng vì câu nêu vấn đề và tên tiếng Anh theo cổng III.2). **Ngoại lệ** (mục 8): 8 dòng (câu vấn đề + bảng 3 hàng + 4 ý định nghĩa) > 6 và ~76 âm tiết > 60, dưới giới hạn 90; lý do: trực quan, ví dụ và phát biểu của cùng một khái niệm đứng trên một trang để giữ 55 trang (NT8); cột trái là bảng số liệu.
- **Âm tiết (`deck_lint`, bản III.5):** 84; 8 dòng (bản v1: 85).
- **Sửa III.5:** câu vấn đề "khi chỉ cần khôi phục gần đúng"; định nghĩa gọi tên "bộ nén", "bộ giải nén"; tên lossless/lossy compression ở ghi chú diễn giả.

#### `lec11-s01-08` — Bộ nén rút ngắn mọi ảnh
- **Chức năng:** phát biểu và chứng minh một dòng (Mệnh đề 11.2 là kết quả phụ, NT6); trực quan bằng hình.
- **Mặt trang:**
  - "**Mệnh đề 11.2.** **Giả thiết:** $\mathcal X=\{0,\ldots,255\}^m$; $\lvert\varphi(x)\rvert<8m$ với mọi $x\in\mathcal X$. **Kết luận:** với mọi $\psi$, có ảnh $x$ để $\psi(\varphi(x))\ne x$."
  - "**Chứng minh.** Có $2^{8m}$ ảnh nhưng chỉ $2^{8m}-1$ chuỗi bit ngắn hơn $8m$, nên $\varphi$ gán cùng dòng bit cho hai ảnh (Mệnh đề 10.2)."
  - Hình `hai-dac-ta-trang-chieu.svg`: hàng trên $y=x$, mỗi $x$ một dòng bit riêng; hàng dưới nhiều khối chung một dòng bit, $E_{\mathrm{RMS}}\le\varepsilon$.
- **Nguồn:** ghi chú Mệnh đề 11.2 (dòng 150–166), hình `note-hai-dac-ta.svg` (dòng 142–144).
- **Ghi chú diễn giả:** giả thiết "mọi ảnh" chỉ dùng ở Bước 2 của chứng minh; Huffman vẫn rút ngắn ảnh có biểu đồ tần suất lệch nhưng không rút ngắn mọi ảnh; đặc tả gần đúng chấp nhận đúng hệ quả "nhiều ảnh chung một dòng bit"; văn bản, mã nguồn, tệp thực thi phải đúng từng byte (Nhận xét 11.3).
- **Quyết định:** thêm (deck cũ không có Mệnh đề 11.2).
- **Âm tiết:** ~35.
- **Âm tiết (`deck_lint`, bản III.5):** 50 (bản v1: 35).
- **Sửa III.5:** tiêu đề "Giới hạn của bộ nén rút ngắn mọi ảnh"; "Chứng minh." thêm bước kết luận về $\psi$.

#### `lec11-s01-09` — Bài tập: chọn hệ số chất lượng theo ngưỡng sai số
- **Chức năng:** NT24 bài của cụm "hai đặc tả" (D-SB1), bước kiểm tra của hành trình NT8; lấy từ bài tập cuối mục 1.1 của ghi chú.
- **Mặt trang:** "**Bài tập 11.1(b).** **Câu hỏi:** Hai ảnh xám CHEETAH.GS và CLOWN.GS, mỗi ảnh $64\,000$ byte, được nén bằng chương trình nén ảnh của Nelson và Gailly ở năm hệ số chất lượng:" bảng `$q$ | CHEETAH.GS: byte | CHEETAH.GS: RMS | CLOWN.GS: byte | CLOWN.GS: RMS`: 1 | $27\,809$ | $4{,}3$ | $20\,835$ | $3{,}7$; 2 | $18\,367$ | $6{,}9$ | $14\,243$ | $5{,}6$; 5 | $10\,232$ | $10{,}9$ | $8\,636$ | $8{,}6$; 10 | $7\,167$ | $13{,}6$ | $6\,355$ | $10{,}9$; 25 | $5\,094$ | $17{,}4$ | $4\,811$ | $14{,}1$. "(b) Với yêu cầu $E_{\mathrm{RMS}}\le10$, chọn trong năm hệ số trên hệ số lớn nhất cho mỗi ảnh và so số byte của hai ảnh."
- **Nguồn:** ghi chú Bài tập 11.1 (dòng 176–188), câu (b) giữ nguyên câu chữ, riêng "chương trình DCT của NG" viết "chương trình nén ảnh của Nelson và Gailly" vì DCT và NG chưa được giới thiệu ở mạch 1 (NT9); câu (a), (c), (d), (e) là bài về nhà. Dữ liệu NG Hình 11.14, tr. 287 (nguồn ghi trong ghi chú diễn giả, không trên mặt trang, NT-DSFA-8).
- **Ghi chú diễn giả:** **Gợi ý:** đọc cột RMS từ trên xuống và dừng ở dòng cuối cùng còn không quá 10. Bài này đọc đánh đổi giữa số byte và sai số của Định nghĩa 11.1. Nhầm lẫn dễ gặp: chọn hệ số nhỏ nhất đạt ngưỡng thay cho lớn nhất. Nguồn: Nelson và Gailly, Hình 11.14, tr. 287.
- **Quyết định:** thêm (D-SB1).
- **Âm tiết:** ~48 (số trong bảng không tính). **Ngoại lệ dòng** (mục 8): 7 dòng (câu dẫn + bảng dữ liệu 5 hàng + câu hỏi) > 6; lý do: đề giữ đủ năm hệ số của bảng nguồn (NT24).
- **Âm tiết (`deck_lint`, bản III.5):** 59 (bản v1: 63).
- **Sửa III.5:** tiêu đề bảng hai tầng (CHEETAH.GS, CLOWN.GS / byte, RMS); "chương trình của Nelson và Gailly".

#### `lec11-s01-10` — Bài tập: chọn hệ số chất lượng theo ngưỡng sai số (lời giải)
- **Chức năng:** NT24 "Lời giải:" trang kế tiếp cùng tiêu đề; câu kết là câu nối sang mạch 2 (NT13; nội dung Mục 1.2; bước 1 của cụm LZ77, NT-DSFA-2), đặt sau bài tập đúng thứ tự ghi chú (1.1 rồi 1.2).
- **Mặt trang:** "**Lời giải:**"
  - "CHEETAH.GS: RMS $6{,}9\le10$ ở $q=2$, $10{,}9>10$ ở $q=5$; chọn $q=2$, $18\,367$ byte."
  - "CLOWN.GS: RMS $8{,}6\le10$ ở $q=5$, $10{,}9>10$ ở $q=10$; chọn $q=5$, $8\,636$ byte."
  - Câu kết: "Với văn bản, chỉ còn khai thác được cụm lặp; mã Huffman theo tần suất từng ký hiệu trả cho lần lặp thứ hai của `aac` trong `aacaacabcabaaac` cùng số bit như lần đầu." (giả thiết mô hình bậc 0 của ghi chú dòng 211 viết bằng lời: "theo tần suất từng ký hiệu")
- **Nguồn:** ghi chú lời giải Bài tập 11.1(b) (dòng 197), Mục 1.2 (dòng 209–213).
- **Ghi chú diễn giả:** cùng ngưỡng, CLOWN.GS chỉ cần khoảng 47% số byte của CHEETAH.GS; câu (c): hệ số chung $q=2$ trả thêm $5\,607$ byte, khoảng 21%; kiểm tra: số byte giảm và RMS tăng khi $q$ tăng nên "lớn nhất còn đạt ngưỡng" là dòng cuối thỏa; cầu nối: một mã từng ký hiệu trả số bit tỷ lệ với độ dài cụm ở mỗi lần lặp, nên cần trỏ ngược tới lần xuất hiện trước.
- **Quyết định:** thêm (D-SB1); câu nối thay trang `L00` "LZ77: trỏ về dữ liệu vừa thấy"; câu nối giữ giả thiết mô hình bậc 0 (cổng III.2).
- **Âm tiết:** ~58.
- **Âm tiết (`deck_lint`, bản III.5):** 59 (bản v1: 48).
- **Sửa III.5:** thêm dòng so số byte (CLOWN.GS khoảng 47%); câu nối tách thành đoạn riêng (`ex-takeaway`), theo ghi chú "phần còn khai thác được là cụm lặp"; ghi chú diễn giả nêu hai mức $q=3,4$ của Hình 11.14.

### Mạch 2 — Nén bằng cửa sổ trượt LZ77 (Mục 2; `lec-11-topic-04`, `-05`, `-06`)

Tám bước NT-DSFA-2: (1) giới hạn có số: câu kết `lec11-s01-10` (lần lặp của `aac` tốn đủ bit); (2) ý tưởng "tương tự … khác ở": `s02-01`; (3) nhận xét cấu trúc (văn bản vừa đọc là từ điển; độ khớp được vượt khoảng lùi): `s02-01`, `s02-03`; (4) chạy tay: `s02-02` (mã hóa), `s02-05` (giải mã); (5) "Đầu vào:"/"Đầu ra:" ngay trước giả mã: `s02-04`, `s02-05`; (6) đọc giả mã: dòng cuối `s02-04`; với bộ giải mã, ghi chú diễn giả `s02-05` (trang giữ 6 dòng); (7) tính đúng: `s02-06`, `s02-07`; (8) chi phí: `s02-08`.

#### `lec11-s02-00` — 2. Nén bằng cửa sổ trượt LZ77 (trang tiêu đề mạch)
- **Chức năng:** NT12, điểm vào mạch 2, `id="mach-2"`, `#/2`; ngoài chu trình khái niệm.
- **Mặt trang:** `h2` "2. Nén bằng cửa sổ trượt LZ77"; dòng dẫn: "Mỗi lần lặp của một cụm được thay bằng một bộ ba trỏ ngược vào phần vừa đọc." (18 âm tiết); từ khóa: "cửa sổ trượt · bộ ba · sao chép chồng lấn · khôi phục đúng".
- **Ghi chú diễn giả (40–100):** kế thừa đặc tả khôi phục đúng (Định nghĩa 11.1) và cụm lặp `aac`; mạch dựng bộ ba, bộ mã hóa tham lam, bộ giải mã chép tuần tự, chứng minh khôi phục đúng và đếm chi phí; trao cho mạch 3 giới hạn của cửa sổ $W$.
- **Quyết định:** sửa (`LT`): tên mạch theo tên mục ghi chú; dòng dẫn trần thuật thay dòng "nhu cầu".
- **Âm tiết:** ~30.
- **Âm tiết (`deck_lint`, bản III.5):** 18.

#### `lec11-s02-01` — Con trỏ ngược vào phần vừa đọc
- **Chức năng:** NT8 vấn đề + trực quan; NT-DSFA-1 tình huống (một lượt, bộ nhớ hữu hạn); NT13 câu hỏi của mạch; NT-DSFA-2 bước 2–3.
- **Mặt trang:**
  - "Bộ mã hóa đọc `aacaacabcabaaac` một lượt và chỉ giữ một đoạn hữu hạn của phần đã đọc."
  - "**Câu hỏi:** mã mỗi lần lặp của một cụm bằng số bit cố định thế nào, chỉ dùng đoạn đang giữ, để bộ giải mã dựng lại đúng chuỗi?"
  - "**Trực quan.** Mỗi bộ ba $(d,\ell,c)$ là một lệnh cho bộ giải mã: lùi $d$ ký tự, chép $\ell$ ký tự, viết thêm ký tự $c$."
  - "Mã từng ký hiệu thay mỗi ký hiệu bằng một từ mã; LZ77 thay cả một cụm độ dài thay đổi bằng một bộ ba cỡ cố định." (so với thuật toán đã biết, NT-DSFA-2 bước 2; ghi chú dòng 222; câu cũ "mỗi bộ ba có số bit cố định như mã từng ký hiệu" sai vì từ mã Huffman có độ dài thay đổi, cổng III.2)
- **Nguồn:** ghi chú Mục 2 mở (dòng 217), 2.1 (dòng 222; NG tr. 174). CMU LZ tc. 3 (LZ77, biến thể LZSS, ứng dụng gzip), tc. 4 (cửa sổ trượt, con trỏ).
- **Ghi chú diễn giả:** Ziv và Lempel công bố năm 1977; trong cài đặt của Nelson và Gailly cửa sổ dài vài nghìn ký tự, phần chưa mã hóa mười tới một trăm ký tự (Nelson và Gailly, tr. 174); bài giảng CMU 15-499 xếp LZSS, gzip vào họ LZ77 (Blelloch, CMU 15-499, phần nén bằng từ điển, trang chiếu 3).
- **Quyết định:** gộp (`L00` + phần chữ của `L01`): mở bằng chuỗi của CMU thay "luồng nhật ký" không số.
- **Âm tiết:** ~58.
- **Âm tiết (`deck_lint`, bản III.5):** 59 (bản v1: 57).
- **Sửa III.5:** câu hỏi thêm bộ mã hóa (encoder), bộ giải mã (decoder).

#### `lec11-s02-02` — Ví dụ: chuỗi `aacaacabcabaaac`, ba bộ ba đầu
- **Chức năng:** NT23 ví dụ chạy tay (bước 4); NT-DSFA-2 bước 4 cho bộ mã hóa.
- **Mặt trang:** dữ kiện và yêu cầu: "$W=6$, $L=4$; con trỏ $p$ là số ký tự đã mã hóa. Xác định ba bộ ba đầu." Bảng `$p$ | đã mã hóa | so khớp | bộ ba`: $0$ | rỗng | không có khoảng lùi | $(0,0,\mathrm a)$; $1$ | `a` | $d=1$: $\ell=1$, ký tự kế $\mathrm c$ | $(1,1,\mathrm c)$; $3$ | `aac` | $d=1,2,3$: $\ell=0,1,4$ | $(3,4,\mathrm b)$. Hình `lz77-cua-so-trang-chieu.svg` (trạng thái $p=3$, mũi tên lùi $d=3$). "**Diễn giải:** ba bộ ba phủ $1+2+5=8$ ký tự; ở $p=3$, nguồn $x_4$ nằm ngay trong đoạn đang mã, nên độ khớp vượt khoảng lùi."
- **Nguồn:** ghi chú Ví dụ 11.2 (dòng 224–246), hình `note-lz77-cua-so.svg`. CMU LZ tc. 5, ba hàng đầu (hai hàng "?" còn lại là Bài tập 11.12 của recitation). CMU ghi bộ ba đầu là $(\_,0,\mathrm a)$, ghi chú ghi $(0,0,\mathrm a)$.
- **Ghi chú diễn giả:** đọc bước 3: thử ba khoảng lùi, $d=3$ khớp đủ $L=4$; vì sao $x_8=\mathrm b$ nằm ngoài vùng so khớp ($L$ chặn độ dài khớp, không chặn vị trí ký tự kế).
- **Quyết định:** sửa (`L04` + hình của `L01`): vết theo ghi chú, hình vẽ lại từ dữ liệu ghi chú.
- **Âm tiết:** ~45.
- **Âm tiết (`deck_lint`, bản III.5):** 60 (bản v1: 55).
- **Sửa III.5:** gọi tên $W$ (cỡ cửa sổ), $L$ (độ khớp tối đa) tại chỗ.

#### `lec11-s02-03` — Cửa sổ, vùng nhìn trước và bộ ba
- **Chức năng:** NT8 phát biểu (Định nghĩa 11.4) sau ví dụ; bước 3 (độ khớp được vượt khoảng lùi).
- **Mặt trang:** "**Định nghĩa 11.4.** Cho $W,L\ge1$, con trỏ $0\le p<n$."
  - "Cửa sổ trượt (sliding window) tại $p$ gồm lịch sử (search buffer) $x[\max(1,p-W+1)..p]$ và vùng nhìn trước (look-ahead buffer) $x[p+1..\min(p+L,n)]$."
  - "Bộ ba (token) $(d,\ell,c)$ gồm khoảng lùi (distance), độ dài khớp (match length), ký tự kế: $0\le\ell\le L$, $p+\ell+1\le n$, $c=x_{p+\ell+1}$."
  - "Nếu $\ell=0$ thì $d=0$; nếu $\ell\ge1$ thì $1\le d\le\min(W,p)$ và $x_{p+j}=x_{p+j-d}$, $j=1,\ldots,\ell$."
  - "Bộ ba mô tả $x[p+1..p+\ell+1]$; con trỏ lên $p+\ell+1$."
  - "**Lưu ý:** định nghĩa không đòi $\ell\le d$."
- **Nguồn:** ghi chú Định nghĩa 11.4 (dòng 248–261). CMU LZ tc. 4 ("position … relative to the cursor" là khoảng lùi).
- **Ghi chú diễn giả:** bộ ba $(3,4,\mathrm b)$ của ví dụ có $\ell=4>d=3$; Nelson và Gailly ghi vị trí trong bộ đệm (offset), cùng thông tin khi hai phía biết vị trí con trỏ; $d\le p$ để vị trí nguồn đầu tiên không nhỏ hơn 1; $p+\ell+1\le n$ để bộ ba cuối vẫn có ký tự kế thật, nên dòng bộ ba không cần `EOS`; bộ đệm nhìn trước $L+1$ ký tự của Nelson và Gailly ứng với độ dài khớp tối đa $L$.
- **Quyết định:** sửa (`L02` "Hai dạng bộ ba"): bỏ bộ ba `EOS` (outline D5), thêm điều kiện chồng lấn.
- **Âm tiết:** ~58.
- **Âm tiết (`deck_lint`, bản III.5):** 60 (bản v1: 57).
- **Sửa III.5:** "Lưu ý: có thể $\ell>d$, khi đó nguồn chồng lên đích."

#### `lec11-s02-04` — Thuật toán: mã hóa LZ77 tham lam
- **Chức năng:** NT-DSFA-2 bước 5–6; GC-DSFA-9 giả mã tiếng Việt.
- **Mặt trang:** "**Đầu vào:** chuỗi $x_1\cdots x_n$; $W,L\ge1$." "**Đầu ra:** dãy bộ ba theo Định nghĩa 11.4." Giả mã:
  1. Đặt $p\leftarrow0$.
  2. Trong khi $p<n$:
     1. Với mỗi $d=1,\ldots,\min(W,p)$, so $x_{p+i}$ với $x_{p+i-d}$, $i=1,2,\ldots$, tới lần đầu không khớp; $\ell(d)$ là số lần khớp, không quá $\min(L,n-p-1)$.
     2. Đặt $\ell\leftarrow\max_d\ell(d)$, với $\ell=0$ khi $p=0$; $d$ là khoảng lùi nhỏ nhất đạt $\ell$, hoặc $d=0$ khi $\ell=0$.
     3. Phát $(d,\ell,x_{p+\ell+1})$; đặt $p\leftarrow p+\ell+1$.
  - Dòng đọc: "Bước 2.1 quyết định và tốn kém nhất; hai khoảng lùi hòa nhau thì chọn cái nào bộ giải mã cũng giải đúng."
- **Nguồn:** ghi chú Thuật toán 11.5 (dòng 265–300). CMU LZ tc. 4 ("Repeat: output $(p,l,c)$ … advance window by $l+1$").
- **Ghi chú diễn giả:** bất biến của bộ mã hóa: trước mỗi lượt, các bộ ba đã phát mô tả nối tiếp đúng $x[1..p]$ (khởi tạo $p=0$; duy trì nhờ điều kiện khớp; kết thúc $p=n$); dừng sau không quá $n$ lượt; tham lam không bảo đảm ít bit nhất (75 so với 68 bit trong ví dụ của Nelson và Gailly, Nhận xét 11.10).
- **Quyết định:** sửa (`L03`): giả mã tiếng Việt theo ghi chú, đứng sau ví dụ và định nghĩa.
- **Âm tiết:** ~62 (giả mã có tính, NT-DSFA-7). Nếu `deck_lint` > 60: bỏ vế "hai khoảng lùi hòa nhau …" khỏi dòng đọc, chuyển vào ghi chú diễn giả.
- **Âm tiết (`deck_lint`, bản III.5):** 58 (bản v1: 51).
- **Sửa III.5:** "Đầu vào/Đầu ra" thêm giả thiết ($W$ chung, đóng khung); câu đọc giả mã gộp vào bước 2.1 để trang giữ 6 dòng.

#### `lec11-s02-05` — Thuật toán: giải mã LZ77
- **Chức năng:** NT-DSFA-2 bước 4 (chạy tay bộ giải mã, Ví dụ 11.3) rồi bước 5–6; trực quan sao chép chồng lấn bằng hình.
- **Mặt trang:**
  - "**Ví dụ 11.3.** Giải $(3,4,\mathrm b)$ sau $y=$ `aac`: $y_{3+j}\leftarrow y_j$ với $j=1,\ldots,4$, rồi $y_8\leftarrow\mathrm b$; bước $j=4$ đọc $y_4$ vừa ghi ở bước $j=1$." Hình `lz77-chep-chong-lan-trang-chieu.svg` (một hàng ô $y_1\ldots y_8$, bốn mũi tên chép).
  - "**Đầu vào:** dãy bộ ba $(d_t,\ell_t,c_t)$, $t=1,\ldots,\tau$. **Đầu ra:** chuỗi $y$."
  - Giả mã: 1. Đặt $y$ rỗng, $p\leftarrow0$. 2. Với $t=1,\ldots,\tau$: nếu $\ell_t\ge1$ và $d_t>p$, báo dòng hỏng; với $j=1,\ldots,\ell_t$ theo thứ tự tăng, gán $y_{p+j}\leftarrow y_{p+j-d_t}$; gán $y_{p+\ell_t+1}\leftarrow c_t$ và $p\leftarrow p+\ell_t+1$. 3. Trả về $y$.
  - Không có dòng đọc riêng trên mặt trang: thứ tự tăng của $j$ đã nằm trong bước 2, ý đọc giả mã nằm trong ghi chú diễn giả để trang giữ 6 dòng (cổng III.2).
- **Nguồn:** ghi chú Ví dụ 11.3 (dòng 307–324), hình `note-lz77-chep-chong-lan.svg`, Thuật toán 11.6 (dòng 326–354). CMU LZ tc. 6 ("What if $l>p$?"; ví dụ `abcd`, $(2,9,\mathrm e)$ để dành cho Bài tập 11.13).
- **Ghi chú diễn giả:** bộ giải mã chỉ chép theo $j$ tăng dần, không so khớp; thứ tự đó đủ để chép đúng cả khi đoạn nguồn chồng lên đoạn đích. Phản ví dụ: một lệnh chép khối $y[1..4]$ đọc $y_4$ khi chưa ghi; 100 chữ A của Nelson và Gailly, một bộ ba mã mười ký tự khi bản giải mã mới có một ký tự; bộ giải mã tốn $\sum_t(\ell_t+1)=n$ phép ghi, gần như không đổi khi $W$, $L$ lớn lên (Nelson và Gailly, tr. 178).
- **Quyết định:** gộp (`L05` "Sao chép chồng lấn" + `L06` "Giải mã không cần tìm kiếm"): ví dụ chồng lấn đặt ngay trước giả mã giải mã.
- **Âm tiết:** ~60.
- **Âm tiết (`deck_lint`, bản III.5):** 35; 7 dòng (bản v1: 39).
- **Sửa III.5:** giả mã đánh số 2.1–2.2 theo ghi chú (2.2 gộp ghi $c_t$ và tiến $p$); "Đầu vào" thêm "đóng khung, không hỏng"; Ví dụ 11.3 rút một dòng; hình `stream-mini`, cao 178.

#### `lec11-s02-06` — Tính đúng: giải mã LZ77
- **Chức năng:** NT5 trang kết quả (Định lý 11.8 là kết quả chính); NT-DSFA-2 bước 7.
- **Mặt trang:** "**Định lý 11.8.** **Giả thiết:** $x\in\Sigma^n$; $W,L\ge1$; dãy bộ ba do Thuật toán 11.5 sinh ra từ $x$; Thuật toán 11.6 giải dãy đó, chép tuần tự và giữ ít nhất $W$ ký tự cuối của $y$; dòng bộ ba không hỏng. **Kết luận:** Thuật toán 11.6 trả về $y=x$." "**Ý nghĩa:** kết luận đúng với mọi dãy bộ ba hợp lệ nối từ $p=0$ tới $p=n$, kể cả dãy không tham lam."
- **Nguồn:** ghi chú Định lý 11.8 (dòng 378–386).
- **Ghi chú diễn giả (≤250):** định lý chỉ nói tính đúng, không nói dòng bộ ba ngắn hơn $x$; vai trò hai điều kiện áp dụng; vì sao giải mã giữ $W$ ký tự là đủ (mọi $d\le W$); gzip không tham lam vẫn được bảo đảm nhờ phần Phạm vi (Tình huống 11.4).
- **Quyết định:** sửa (`L07` "Hai nhánh đều bảo toàn lịch sử"): bỏ nhánh `EOS`; phát biểu theo khối của ghi chú.
- **Âm tiết:** ~55.
- **Âm tiết (`deck_lint`, bản III.5):** 58 (bản v1: 60).
- **Sửa III.5:** "Ý nghĩa:" đổi thành "Lưu ý: chứng minh chỉ dùng Định nghĩa 11.4, nên kết luận còn đúng cho dãy hợp lệ không tham lam."

#### `lec11-s02-07` — Ý tưởng chứng minh: LZ77 khôi phục đúng
- **Chức năng:** NT6 (trang riêng, 4 bước, giả thiết ghi ở bước dùng); NT7 nhắc kỹ thuật bất biến vòng lặp; NT8 kiểm tra bằng phản ví dụ.
- **Mặt trang:** "**Nhắc lại:** bất biến vòng lặp đúng trước lượt đầu và được giữ qua mỗi lượt." `ol`:
  1. Đặt $p_1=0$, $p_{t+1}=p_t+\ell_t+1$; bất biến: trước lượt $t$, $y=x[1..p_t]$.
  2. Khởi tạo: trước lượt 1, $y$ rỗng và $p_1=0$.
  3. Duy trì: nguồn $p_t+j-d_t$ thuộc $[1;\,p_t+j-1]$, đã ghi, vì $1\le d_t\le p_t$ và chép theo $j$ tăng dần (giả thiết chép tuần tự); rồi ghi $c_t=x_{p_t+\ell_t+1}$.
  4. Kết thúc: $p_{\tau+1}=n$, nên $y=x$.
  - "Bỏ chép tuần tự: lệnh chép khối $y[1..4]$ cho $(3,4,\mathrm b)$ đọc $y_4$ trước khi ghi."
- **Nguồn:** ghi chú Bổ đề 11.7 (dòng 356–376; kết quả phụ, chỉ dẫn ở bước 3), chứng minh Định lý 11.8 (dòng 388–401); Bài 05, chứng minh Mệnh đề 05.19 (bất biến).
- **Ghi chú diễn giả (~200):** Bổ đề 11.7 bằng quy nạp theo $j$; bước 3 dùng bất biến của bộ mã hóa (bộ ba hợp lệ tại $p_t$); bất biến đặt trên chính văn bản đã giải mã; bỏ "giữ ít nhất $W$ ký tự": bộ giải mã chỉ giữ $W'<W$ không đọc được nguồn của bộ ba có $d>W'$.
- **Quyết định:** thêm (NT6).
- **Âm tiết:** ~58.
- **Âm tiết (`deck_lint`, bản III.5):** 72 (bản v1: 60).
- **Sửa III.5:** tiêu đề "Ý tưởng chứng minh: tính đúng của giải mã LZ77"; bước duy trì nêu giả thiết quy nạp và điều kiện khớp $x_{p_t+j-d_t}=x_{p_t+j}$.

#### `lec11-s02-08` — Chi phí: LZ77
- **Chức năng:** NT-DSFA-3 (dòng "Mô hình:", bảng bốn cột, tách thời gian, bộ nhớ, số bit); NT-DSFA-2 bước 8; câu nối sang mạch 3 (NT13).
- **Mặt trang:** "**Mô hình:** đếm phép so hai ký tự khi mã hóa, phép ghi một ký tự khi giải mã, trường hợp xấu nhất; $\tau\le n$ bộ ba." Bảng `Bước | Số lần | Chi phí mỗi lần | Đóng góp`: mã hóa, bước 2.1 | $\tau$ | $\le\min(W,p)\,(L+1)$ phép so | $O(nWL)$; mã hóa, bước 2.2–2.3 | $\tau$ | $O(W)$ | $O(nW)$; giải mã | $\tau$ | $\ell_t+1$ phép ghi | $n$. "Bộ nhớ: bộ mã hóa $W+L+1$ ký tự, bộ giải mã $W$ ký tự." "Mỗi bộ ba $\lceil\log_2W\rceil+\lceil\log_2(L+1)\rceil+8$ bit; với $W=6$, $L=4$ là 14 bit, có lợi khi mô tả trung bình hơn $1{,}75$ ký tự (Mệnh đề 11.9)." Câu kết: "Một cụm chỉ dùng lại được khi lần trước còn trong $W$ ký tự cuối; tăng $W$ từ $4\,096$ lên $65\,536$ làm phép tìm vét cạn chậm 16 lần."
- **Nguồn:** ghi chú Mệnh đề 11.9 (dòng 408–433), Bài tập 11.2(c) (dòng 456), kết Mục 2 (dòng 481). CMU LZ tc. 7–9 (LZSS, tối ưu của gzip, bảng băm), tc. 10 (Wyner–Ziv) chỉ ở ghi chú diễn giả.
- **Ghi chú diễn giả:** Nhận xét 11.10: $W=4\,096$, $L=15$ cho bộ ba 24 bit; LZSS phát cặp 17 bit hoặc ký tự rời 9 bit; gzip băm mọi chuỗi con dài 3, giới hạn số vị trí thử mỗi ngăn, mã Huffman các trường (Blelloch, CMU 15-499, phần nén bằng từ điển, trang chiếu 8–9); tối ưu tiệm cận khi cửa sổ đủ dài nằm ngoài phạm vi (Blelloch, CMU 15-499, phần nén bằng từ điển, trang chiếu 10).
- **Quyết định:** sửa (`L08`): bảng chi phí theo NT-DSFA-3, thêm số bit và điểm hòa vốn; bỏ "$O(W+L)$" không phân tách.
- **Âm tiết:** ~75 (trần 80 của bảng chi phí, NT-DSFA-7); 7 dòng (bảng 3 hàng, cho tới 8).
- **Âm tiết (`deck_lint`, bản III.5):** 80.
- **Sửa III.5:** "(Mệnh đề 11.9(d))"; quy ước ghi $d-1$ ở ghi chú diễn giả.

### Mạch 3 — Nén bằng từ điển cụm LZ78 (Mục 3; `lec-11-topic-07`, `-08`, `-09`)

Tám bước: (1) giới hạn có số: câu kết `s02-08` và dòng đầu `s03-01` (tên 9 ký tự cách $10\,000$ vị trí); (2) ý tưởng "tương tự LZ77, khác ở chỉ số trỏ vào danh sách cụm": `s03-01`; (3) nhận xét cấu trúc (từ điển đóng với tiền tố nên là cây, tìm cụm khớp dài nhất bằng cách đi xuống cây): `s03-02`; (4) chạy tay: `s03-01` (mã hóa), dòng Ví dụ 11.5 ở `s03-04` (giải mã); (5)–(6): `s03-03`, `s03-04`; (7): `s03-05`, `s03-06`; (8): `s03-07`.

#### `lec11-s03-00` — 3. Nén bằng từ điển cụm LZ78 (trang tiêu đề mạch)
- **Chức năng:** NT12, `id="mach-3"`, `#/3`; ngoài chu trình khái niệm.
- **Mặt trang:** "3. Nén bằng từ điển cụm LZ78"; dòng dẫn: "Hai phía dựng cùng một từ điển cụm từ chính dòng cặp, nên không cần truyền từ điển." (19); từ khóa: "từ điển cụm · cây từ điển · cặp mã–ký tự · đồng bộ hai từ điển".
- **Ghi chú diễn giả:** kế thừa bộ ba, Định lý 11.8 và giới hạn cửa sổ; mạch dựng từ điển cụm, hai thuật toán, chứng minh đồng bộ bằng quy nạp, chi phí; trao cho mạch 4 giới hạn: mỗi cặp mang một ký tự thô.
- **Quyết định:** sửa (`ZT`).
- **Âm tiết:** ~32.
- **Âm tiết (`deck_lint`, bản III.5):** 20 (bản v1: 18).
- **Sửa III.5:** dòng dẫn "…từ chính dòng mã nhận được…"; ghi chú diễn giả viết lại thành câu thường.

#### `lec11-s03-01` — Ví dụ: chuỗi `aabaacabcabcb`, bốn cặp đầu
- **Chức năng:** trang nội dung đầu của mạch: giới hạn có số, câu hỏi của mạch (NT13), ý tưởng (NT-DSFA-2 bước 1–2), chạy tay (bước 4); NT14 vào thẳng dữ kiện.
- **Mặt trang:**
  - "Với $W=4\,096$, một tên 9 ký tự ở vị trí $1\,000$ lặp lại ở vị trí $11\,000$ phải mã lại."
  - "**Câu hỏi:** giữ những cụm nào, và bộ giải mã biết các cụm đó bằng cách nào khi không có cửa sổ để trỏ vào?"
  - "**Trực quan.** Như LZ77, mỗi đơn vị mã thay một cụm đã gặp; khác ở chỗ chỉ số trỏ vào danh sách cụm, và mỗi lần mã một đoạn, hai phía cùng thêm đúng đoạn đó."
  - "Xác định bốn cặp đầu." Bảng `cụm khớp + ký tự phá khớp | cặp | mục thêm`: `a` | $(0,\mathrm a)$ | 1 = `a`; `a`+`b` | $(1,\mathrm b)$ | 2 = `ab`; `a`+`a` | $(1,\mathrm a)$ | 3 = `aa`; rỗng+`c` | $(0,\mathrm c)$ | 4 = `c`.
- **Nguồn:** ghi chú Mục 3 mở (dòng 485–487; NG tr. 208–210), Ví dụ 11.4 (dòng 494–513). CMU LZ tc. 11 ("dictionary is maintained differently"), tc. 12, tc. 13 bốn hàng đầu (hai hàng "?" là Bài tập 11.15).
- **Ghi chú diễn giả:** vị trí $11\,000$ ứng với $p=10\,999$, lịch sử chỉ gồm $x[6\,904..10\,999]$ (giả sử); cách đọc bảng theo từng ký tự (cụm kéo dài khi còn trong danh sách; $x_2$, $x_4$ chỉ kéo dài); Ziv và Lempel 1978; bộ giải mã dựng lại danh sách từ chính dòng cặp (Nelson và Gailly, tr. 209–210).
- **Quyết định:** gộp (`Z00` + `Z02`): giới hạn và câu hỏi đặt cùng ví dụ để giữ 55 trang; bảng rút về bốn hàng phát cặp.
- **Âm tiết:** ~58; 7 dòng (bảng vết 4 hàng, NT-DSFA-7 cho tới 8).
- **Âm tiết (`deck_lint`, bản III.5):** 59.
- **Sửa III.5:** câu "Trực quan." sửa diễn đạt; giới hạn tên 9 ký tự vẫn ở ghi chú diễn giả, kèm dòng kiểm tra.

#### `lec11-s03-02` — Từ điển cụm, cặp LZ78 và cây từ điển
- **Chức năng:** NT8 phát biểu (Định nghĩa 11.11); bước 3 (Bổ đề 11.12, kết quả phụ, một dòng); hình cây.
- **Mặt trang:** "**Định nghĩa 11.11.**"
  - "Từ điển cụm (phrase dictionary) $D$ gán mỗi mã $0,\ldots,\lvert D\rvert-1$ một chuỗi; $D[0]$ là chuỗi rỗng."
  - "Cặp $(i,c)$ mô tả $D[i]\,c$; sau cặp, hai phía thêm $D[\lvert D\rvert]\leftarrow D[i]\,c$. Cặp cuối có thể là $(i,\texttt{EOS})$."
  - "Cây từ điển (dictionary tree, trie, multiway tree): mục $j$ thêm từ cặp $(i,c)$ là con của nút $i$ qua cạnh $c$."
  - Hình `lz78-cay-trang-chieu.svg` (cây sau bốn cặp: gốc 0; 1 = `a`, 4 = `c`; 3 = `aa`, 2 = `ab`).
  - "**Bổ đề 11.12.** Mọi tiền tố của một cụm trong $D$ cũng là cụm trong $D$, nên cụm khớp dài nhất tìm được bằng cách đi xuống cây."
- **Nguồn:** ghi chú Định nghĩa 11.11 (dòng 517–523), Bổ đề 11.12 (dòng 525–545), hình `note-lz78-cay.svg` (dòng 603–605; ghi chú đặt hình sau Ví dụ 11.5, deck dùng sớm hơn vì hình vẽ đúng bốn cặp của `s03-01`). CMU LZ tc. 11 (trie, bảng word–id).
- **Ghi chú diễn giả:** cặp không cần trường độ dài vì bộ giải mã biết $\lvert D[i]\rvert$; đọc cụm của nút $j$ bằng cách nối nhãn cạnh từ gốc; chứng minh bổ đề bằng quy nạp theo số mục; từ điển nhận `ab` khi chưa có `a` thì không đóng với tiền tố.
- **Quyết định:** sửa (`Z01`): định nghĩa theo ghi chú, hình vẽ lại thay `lz78-trie.svg`.
- **Âm tiết:** ~58.
- **Âm tiết (`deck_lint`, bản III.5):** 78 (bản v1: 67).
- **Sửa III.5:** giải nghĩa `EOS` tại chỗ; Bổ đề 11.12 nêu giả thiết "với phép thêm $D[i]\,c$, $i$ đã có"; hình cây cao 270, nhãn cạnh có nền trắng.

#### `lec11-s03-03` — Thuật toán: mã hóa LZ78
- **Chức năng:** NT-DSFA-2 bước 5–6; bất biến của bộ mã hóa (dùng ở `s03-06`).
- **Mặt trang:** "**Đầu vào:** chuỗi $x_1\cdots x_n$. **Đầu ra:** dãy cặp $(i_1,c_1),\ldots,(i_\tau,c_\tau)$." Giả mã:
  1. Đặt $D$ chỉ gồm $D[0]$ rỗng và nút hiện tại $i\leftarrow0$.
  2. Với mỗi ký tự $c=x_1,\ldots,x_n$: nếu nút $i$ có con $j$ qua cạnh $c$, đặt $i\leftarrow j$; nếu không, phát $(i,c)$, thêm nút $\lvert D\rvert$ làm con của $i$ qua $c$, đặt $i\leftarrow0$.
  3. Nếu sau ký tự cuối $i\ne0$, phát $(i,\texttt{EOS})$.
  - "**Bất biến:** các cặp đã phát mô tả $x[1..p]$, và $D[i]$ là các ký tự đã đọc sau vị trí $p$."
  - Dòng đọc: "Bước 2 tra một con mỗi ký tự; cụm mới luôn chưa có trong $D$."
- **Nguồn:** ghi chú Thuật toán 11.13 (dòng 547–581). CMU LZ tc. 12.
- **Ghi chú diễn giả:** khởi tạo–duy trì–kết thúc của bất biến; trường hợp biên: ký tự chưa gặp luôn cho $(0,c)$, chuỗi kết thúc ngay sau một cặp thường thì không có cặp `EOS`.
- **Quyết định:** tách (`Z03` "Hai phía dùng cùng phép cập nhật" thành `s03-03` và `s03-04`).
- **Âm tiết:** ~60.
- **Âm tiết (`deck_lint`, bản III.5):** 58; 7 dòng (bản v1: 54).
- **Sửa III.5:** "Đầu vào/Đầu ra" thêm giả thiết; giả mã đánh số 2.1, 2.2 theo ghi chú.

#### `lec11-s03-04` — Thuật toán: giải mã LZ78
- **Chức năng:** chạy tay bộ giải mã (Ví dụ 11.5, một dòng) rồi NT-DSFA-2 bước 5–6.
- **Mặt trang:**
  - "**Ví dụ 11.5.** Giải $(0,\mathrm a)$, $(1,\mathrm b)$, $(1,\mathrm a)$, $(0,\mathrm c)$: xuất `a`, `ab`, `aa`, `c` và thêm mục 1–4 trùng mục của bộ mã hóa."
  - "**Đầu vào:** dãy cặp $(i_t,c_t)$, $t=1,\ldots,\tau$. **Đầu ra:** chuỗi $y$."
  - Giả mã: 1. Đặt $D$ chỉ gồm $D[0]$ rỗng và $y$ rỗng. 2. Với mỗi cặp $(i_t,c_t)$: nếu $i_t\ge\lvert D\rvert$, báo dòng hỏng; nếu $c_t=\texttt{EOS}$, nối $D[i_t]$ vào $y$ và dừng; nếu không, nối $D[i_t]\,c_t$ vào $y$ và thêm $D[\lvert D\rvert]\leftarrow D[i_t]\,c_t$. 3. Trả về $y$.
  - Không có dòng đọc riêng trên mặt trang (giữ 6 dòng, cổng III.2); ý đọc giả mã nằm trong ghi chú diễn giả.
- **Nguồn:** ghi chú Ví dụ 11.5 (dòng 588–601), Thuật toán 11.14 (dòng 607–635). CMU LZ tc. 14, bốn hàng đầu.
- **Ghi chú diễn giả:** bộ giải mã chỉ cần cùng từ điển với bộ mã hóa trước mỗi cặp; nó đọc cụm từ từ điển theo mã nhận được. Bảng giải mã đầy đủ của Ví dụ 11.5 (bản giải mã `a`, `aab`, `aabaa`, `aabaac`); đọc $D[i_t]$ bằng cách đi từ nút $i_t$ lên gốc rồi đảo thứ tự.
- **Quyết định:** tách (từ `Z03`).
- **Âm tiết:** ~60.
- **Âm tiết (`deck_lint`, bản III.5):** 54; 8 dòng (bản v1: 50).
- **Sửa III.5:** "Đầu vào" thêm "đóng khung, không hỏng"; giả mã đánh số 2.1–2.3.

#### `lec11-s03-05` — Tính đúng: LZ78
- **Chức năng:** NT5 (Định lý 11.15, kết quả chính); NT-DSFA-2 bước 7.
- **Mặt trang:** "**Định lý 11.15.** **Giả thiết:** dãy cặp do Thuật toán 11.13 sinh ra từ $x$; Thuật toán 11.14 giải dãy đó; hai phía bắt đầu từ cùng từ điển, thêm mục theo cùng quy tắc và đánh mã theo cùng thứ tự; từ điển không giới hạn; dòng cặp không hỏng. **Kết luận:** với mọi $t$, sau cặp thứ $t$: (a) hai từ điển có cùng số mục và $D'[j]=D[j]$ với mọi mã $j$; (b) $y=x[1..p_t]$. Nói riêng, khi dừng $y=x$."
- **Nguồn:** ghi chú Định lý 11.15 (dòng 637–645).
- **Ghi chú diễn giả:** $p_t$ là số ký tự mà $t$ cặp đầu mô tả; phạm vi: khi từ điển đầy, hai phía còn phải chung quy tắc xử lý từ điển đầy.
- **Quyết định:** sửa (`Z04` "Quy nạp theo số cặp" tách thành phát biểu và ý tưởng chứng minh).
- **Âm tiết:** ~58.
- **Âm tiết (`deck_lint`, bản III.5):** 59 (bản v1: 60).
- **Sửa III.5:** kết luận gọi tên $D'$ (từ điển của bộ giải mã) và $p_t$ tại chỗ.

#### `lec11-s03-06` — Ý tưởng chứng minh: đồng bộ từ điển của LZ78
- **Chức năng:** NT6; NT8 kiểm tra bằng phản ví dụ.
- **Mặt trang:** "Quy nạp theo số cặp $t$." `ol`:
  1. Cơ sở $t=0$: hai từ điển chỉ có mã 0 là chuỗi rỗng; $y$ rỗng.
  2. Cặp thường $(i_t,c_t)$: theo bất biến của bộ mã hóa, đoạn kế tiếp của $x$ là $D[i_t]\,c_t$; theo (a), $D'[i_t]=D[i_t]$, nên bộ giải mã nối đúng đoạn đó.
  3. Hai phía thêm cùng chuỗi $D[i_t]\,c_t$ ở cùng mã (giả thiết cùng quy tắc), nên (a) được giữ.
  4. Cặp `EOS`: đoạn cuối là $D[i_\tau]$, nên $y=x$.
  - "Bỏ cùng quy tắc: bộ giải mã chỉ thêm mục khi $i_t\ge1$ sẽ gặp mã 1 chưa có ở cặp $(1,\mathrm b)$."
- **Nguồn:** ghi chú chứng minh Định lý 11.15 (dòng 647–661).
- **Ghi chú diễn giả (~200):** so với Định lý 11.8: LZ77 giữ bất biến trên văn bản đã giải mã, LZ78 giữ bất biến trên từ điển, văn bản đúng là hệ quả; quy tắc lệch nhẹ hơn (đánh mã mới từ 2) không làm bộ giải mã báo lỗi nhưng mọi mã sau trỏ sai cụm.
- **Quyết định:** thêm (NT6).
- **Âm tiết:** ~60.
- **Âm tiết (`deck_lint`, bản III.5):** 59 (bản v1: 60).
- **Sửa III.5:** dòng phản ví dụ viết lại thành câu đủ chủ ngữ.

#### `lec11-s03-07` — Chi phí: LZ78
- **Chức năng:** NT-DSFA-3; bước 8; ứng dụng (từ điển đầy, NT-DSFA-1); câu nối sang mạch 4.
- **Mặt trang:** "**Mô hình:** đếm phép tra con, phép thêm nút, phép ghi ký tự; bảng băm với giả thiết băm đều và hệ số tải hằng tra, thêm trong thời gian kỳ vọng $O(1)$." Bảng `Bước | Số lần | Chi phí mỗi lần | Đóng góp`: mã hóa, tra con | $n$ | $O(1)$ kỳ vọng; $O(\lvert\Sigma\rvert)$ với danh sách con | $O(n)$ kỳ vọng; mã hóa, thêm nút | $\tau\le n$ | $O(1)$ | $O(\tau)$; giải mã | $\tau$ | $\lvert D[i_t]\rvert+1$ phép ghi | $n$. "Mỗi cặp $\lceil\log_2M\rceil+9$ bit; với $M=2^{16}$ là 25 bit, có lợi khi mô tả hơn $3{,}125$ ký tự (Mệnh đề 11.16)." "Từ điển đầy: ngừng thêm, xóa khi tỷ lệ nén xấu đi (`compress`), hoặc bỏ mục ít được dùng gần đây nhất (BTLZ)." Câu kết: "Mỗi cặp vẫn mang một ký tự thô; trên `aabaacabcabcb`, 6 trong 13 ký tự đi qua dòng nén ở dạng thô."
- **Nguồn:** ghi chú Mệnh đề 11.16 (dòng 668–693), Nhận xét 11.17 (dòng 695–700), kết Mục 3 (dòng 736). CMU LZ tc. 18 (từ điển quá lớn: GIF, `compress`, BTLZ).
- **Ghi chú diễn giả:** bảng băm với giả thiết băm đều và hệ số tải hằng tra, chèn trong thời gian kỳ vọng $O(1)$ (Cormen và cộng sự, Chương 11); mảng 256 con mỗi nút nhanh nhưng phí bộ nhớ; GIF bỏ cả từ điển khi đạt cỡ tối đa; so với LZ77: $n$ phép tra thay $O(nWL)$ phép so, nhưng cặp 25 bit dài hơn bộ ba 24 bit; ký tự phá khớp là ký tự đầu của đoạn kế tiếp.
- **Quyết định:** sửa (`Z05`): bảng chi phí NT-DSFA-3; thêm số bit và câu nối.
- **Âm tiết:** ~78 (trần 80); 7 dòng (bảng 3 hàng).
- **Âm tiết (`deck_lint`, bản III.5):** 78 (bản v1: 93).
- **Sửa III.5:** "Mô hình:" nêu $M$; dòng "Nhắc lại:" về bảng băm; thêm bộ nhớ $\le M$ nút; dòng "Từ điển đầy" chuyển vào ghi chú diễn giả (kèm `compress`, GIF, BTLZ của British Telecom, LRU).

### Mạch 4 — Nén LZW với từ điển nạp sẵn (Mục 4; `lec-11-topic-10`, `-11`, `-12`)

Tám bước: (1) câu kết `s03-07`; (2) "như LZ78 …; khác LZ78 …": `s04-01`; (3) mục thêm $w_t\operatorname{first}(w_{t+1})$ có ký tự cuối thuộc cụm kế tiếp, nên bộ giải mã chậm một mục: `s04-02`, `s04-03`; (4) chạy tay: `s04-01` (mã hóa), `s04-03` (giải mã, mã chưa có); (5)–(6): `s04-02`, `s04-04`; (7): `s04-05`, `s04-06`; (8): `s04-07`.

#### `lec11-s04-00` — 4. Nén LZW với từ điển nạp sẵn (trang tiêu đề mạch)
- **Chức năng:** NT12, `id="mach-4"`, `#/4`; ngoài chu trình khái niệm.
- **Mặt trang:** "4. Nén LZW với từ điển nạp sẵn"; dòng dẫn: "Bộ giải mã chậm hơn bộ mã hóa một mục nhưng vẫn dựng lại đúng mọi cụm." (16); từ khóa: "từ điển nạp sẵn · mã kế tiếp · độ trễ một mục · mã chưa có trong từ điển".
- **Ghi chú diễn giả:** kế thừa cặp LZ78 và Định lý 11.15; mạch bỏ ký tự thô, dựng hai thuật toán, xử lý mã chưa có, chứng minh khôi phục đúng, đếm chi phí; trao cho mạch 5 giới hạn: cả ba thuật toán chỉ khai thác cụm khớp đúng từng ký tự.
- **Quyết định:** sửa (`WT`): tên mạch thêm "với từ điển nạp sẵn" để khác tiêu đề trang đầu.
- **Âm tiết:** ~32.
- **Âm tiết (`deck_lint`, bản III.5):** 20 (bản v1: 17).
- **Sửa III.5:** dòng dẫn "Bộ giải mã dựng lại đúng mọi cụm dù luôn biết từ điển muộn hơn bộ mã hóa một bước."; ghi chú diễn giả viết lại.

#### `lec11-s04-01` — Ví dụ: chuỗi `aabaacabcabcb`, mã LZW
- **Chức năng:** trang nội dung đầu: câu hỏi của mạch (NT13), ý tưởng (bước 2), chạy tay (bước 4); quy ước mã.
- **Mặt trang:**
  - "**Câu hỏi:** bỏ ký tự thô khỏi mỗi đơn vị mã thế nào mà bộ giải mã vẫn dựng lại được từ điển và chuỗi?"
  - "Từ điển nạp sẵn (preloaded dictionary) 256 cụm một byte, $\mathrm a\mapsto97$, $\mathrm b\mapsto98$, $\mathrm c\mapsto99$; mã của cụm mới bắt đầu từ 256." "**Trực quan.** Như LZ78, cụm kéo dài khi còn trong từ điển; khác LZ78, ký tự phá khớp mở cụm kế tiếp." "Xác định dòng mã."
  - Bảng hai cặp cột `mã phát (cụm) | mục thêm`, đọc theo cột: 97 (`a`) | 256 = `aa`; 97 (`a`) | 257 = `ab`; 98 (`b`) | 258 = `ba`; 256 (`aa`) | 259 = `aac`; 99 (`c`) | 260 = `ca` ‖ 257 (`ab`) | 261 = `abc`; 260 (`ca`) | 262 = `cab`; 98 (`b`) | 263 = `bc`; 99 (`c`) | 264 = `cb`; 98 (`b`) | —.
- **Nguồn:** ghi chú Mục 4 mở (dòng 740–742; NG tr. 214), Ví dụ 11.6 (dòng 749–775). CMU LZ tc. 15 (không gửi ký tự $c$; nạp sẵn 256 mục), tc. 17 (vết mã hóa, CMU in 112–114, ghi chú dùng mã byte 97–99, outline D3).
- **Ghi chú diễn giả:** Welch 1984; dòng mã đóng khung bằng số mã, không dành mã cho `EOS`; kiểm: 10 mã, 9 mục mới, các cụm nối lại đủ 13 ký tự; mã 256 phát ở mã thứ tư sau khi thêm ở mã thứ nhất; với $M=2^{16}$ bỏ trường ký tự thì mỗi đơn vị còn 16 bit thay 25 bit.
- **Quyết định:** gộp (`W00` + `W02`): thay chuỗi tự dựng `ppqpprpqrpqrq` và mã 112–114 bằng chuỗi CMU với mã byte; bỏ hình `lzw-trace.svg` (bảng HTML đủ).
- **Âm tiết:** ~58; bảng 5 hàng, tổng 7 dòng.
- **Âm tiết (`deck_lint`, bản III.5):** 78 (bản v1: 73).
- **Sửa III.5:** bảng thêm cột $t$ (1–5, 6–10); "Xác định dòng mã." thành dòng riêng; mã byte của $\mathrm a,\mathrm b,\mathrm c$ chuyển vào ghi chú diễn giả.

#### `lec11-s04-02` — Thuật toán: mã hóa LZW
- **Chức năng:** NT-DSFA-2 bước 5–6; nhận xét cấu trúc (bước 3); Định nghĩa 11.18 nằm trong giả mã.
- **Mặt trang:** "**Đầu vào:** chuỗi byte $x_1\cdots x_n$. **Đầu ra:** dòng mã $k_1,\ldots,k_\tau$, đóng khung bằng số mã $\tau$." Giả mã:
  1. Nạp sẵn $D[v]$, $v=0,\ldots,255$; đặt mã kế tiếp $\texttt{next\_code}\leftarrow256$ và $w\leftarrow x_1$.
  2. Với mỗi $c=x_2,\ldots,x_n$: nếu $w\,c$ có trong $D$, đặt $w\leftarrow w\,c$; nếu không, phát mã của $w$, thêm $D[\texttt{next\_code}]\leftarrow w\,c$, tăng $\texttt{next\_code}$, đặt $w\leftarrow c$.
  3. Phát mã của $w$.
  - "Mục thêm khi phát $k_t$ là $w_t\operatorname{first}(w_{t+1})$ (Định nghĩa 11.18): ký tự cuối của mục thuộc cụm kế tiếp."
- **Nguồn:** ghi chú Định nghĩa 11.18 (dòng 777–783), Thuật toán 11.19 (dòng 785–813). CMU LZ tc. 15.
- **Ghi chú diễn giả:** bất biến: $w\in D$ và các cụm đã phát nối với $w$ cho đúng phần đã đọc; bước 2 tra khóa (mã của $w$, $c$), như đi xuống cây ở LZ78; hệ quả của thay đổi: bộ giải mã chỉ biết mục mới sau khi giải cụm kế tiếp.
- **Quyết định:** sửa (`W01`).
- **Âm tiết:** ~55. Dòng cuối dùng dấu hai chấm sau công thức; người viết có thể đổi thành "…, với ký tự cuối thuộc cụm kế tiếp".
- **Âm tiết (`deck_lint`, bản III.5):** 53; 7 dòng (bản v1: 48).
- **Sửa III.5:** "Đầu vào" thêm "từ điển không giới hạn"; giả mã đánh số 2.1, 2.2; câu cuối thêm $t<\tau$.

#### `lec11-s04-03` — Ví dụ: mã chưa có trong từ điển của bộ giải mã
- **Chức năng:** chạy tay bộ giải mã (Ví dụ 11.7, Ví dụ 11.8(b)); trực quan độ trễ một mục bằng hình; bước 3–4.
- **Mặt trang:**
  - "Giải 97, 97, 98: chỉ khi đọc mã thứ hai bộ giải mã mới thêm được $D[256]=$ `aa`; bộ giải mã chậm hơn bộ mã hóa một mục."
  - "**Ví dụ 11.8.** Giả sử đầu vào `abababa`; bộ mã hóa phát $97,98,256,258$." Hình `lzw-ma-chua-co-trang-chieu.svg`.
  - "Đọc $258=\texttt{next\_code}$: cụm vừa xuất là $w=$ `ab`, nên cụm mới là $w\operatorname{first}(w)=$ `aba`; thêm $258=$ `aba`."
  - "**Diễn giải:** các cụm `a`, `b`, `ab`, `aba` nối lại thành `abababa`."
- **Nguồn:** ghi chú Ví dụ 11.7 (dòng 820–846), Ví dụ 11.8 (dòng 848–867), hình `note-lzw-ma-chua-co.svg`. CMU LZ tc. 16 ("one step behind"; chuỗi `…SSc…`, để dành cho Bài tập 11.16), tc. 19 (vết giải mã).
- **Ghi chú diễn giả:** bảy mã còn lại của Ví dụ 11.7 thêm 258–264 trùng Ví dụ 11.6, mọi mã đọc vào nhỏ hơn `next_code`; Ví dụ 11.8(a) IWOMBAT của Nelson và Gailly (tr. 217); dạng "ký tự, chuỗi, ký tự, chuỗi, ký tự" $\chi S\chi S\chi$ với $\chi=\mathrm a$, $S=$ `b`.
- **Quyết định:** gộp (`W03` + `W04`): thay `lzw-kwkwk.svg` và ví dụ tự dựng ($w=$ `aba`, `next_code` = 271) bằng vết của ghi chú.
- **Âm tiết:** ~55.
- **Âm tiết (`deck_lint`, bản III.5):** 59.

#### `lec11-s04-04` — Thuật toán: giải mã LZW
- **Chức năng:** NT-DSFA-2 bước 5–6; giả mã 9 dòng đứng một mình với một câu dẫn (NT-DSFA-7).
- **Mặt trang:** câu dẫn: "Nhánh 3.2 xử lý mã mà bộ mã hóa vừa thêm." "**Đầu vào:** dòng mã $k_1,\ldots,k_\tau$. **Đầu ra:** chuỗi $y$." Giả mã:
  1. Nạp sẵn $D[v]$, $v=0,\ldots,255$; $\texttt{next\_code}\leftarrow256$; nếu $\tau=0$, trả về $y$ rỗng.
  2. Nếu $k_1\ge256$, báo dòng hỏng; ngược lại $w\leftarrow D[k_1]$, $y\leftarrow w$.
  3. Với $t=2,\ldots,\tau$ và $k=k_t$:
     1. nếu $k<\texttt{next\_code}$: $e\leftarrow D[k]$;
     2. nếu $k=\texttt{next\_code}$: $e\leftarrow w\operatorname{first}(w)$;
     3. nếu $k>\texttt{next\_code}$: báo dòng hỏng;
     4. nối $e$ vào $y$; thêm $D[\texttt{next\_code}]\leftarrow w\operatorname{first}(e)$, tăng $\texttt{next\_code}$; đặt $w\leftarrow e$.
  4. Trả về $y$.
- **Nguồn:** ghi chú Thuật toán 11.20 (dòng 869–899). CMU LZ tc. 16, 19.
- **Ghi chú diễn giả:** nhánh 3.2 dựa trên Mệnh đề 11.22(b), nhánh 3.3 dựa trên Mệnh đề 11.22(a); ở nhánh 3.2, $\operatorname{first}(e)=\operatorname{first}(w)$ nên mục thêm cũng là $e$; ghi cụm bằng ngăn xếp (Nelson và Gailly, tr. 221).
- **Quyết định:** sửa (`W05` "Giải mã đầy đủ kiểm soát độ trễ một mục").
- **Âm tiết:** ~50; 10 dòng giả mã (đứng một mình).
- **Âm tiết (`deck_lint`, bản III.5):** 58; 9 dòng (bản v1: 45).
- **Sửa III.5:** "Đầu vào" thêm "đóng khung; hai phía cùng nạp sẵn, cùng mã đầu 256".

#### `lec11-s04-05` — Tính đúng: giải mã LZW
- **Chức năng:** NT5 (Định lý 11.23, kết quả chính); bước 7.
- **Mặt trang:** "**Định lý 11.23.** **Giả thiết:** $x$ là chuỗi byte, $n\ge1$; dòng mã $k_1,\ldots,k_\tau$ do Thuật toán 11.19 sinh ra, $w_t=D[k_t]$; Thuật toán 11.20 giải dòng đó; hai phía cùng từ điển nạp sẵn, cùng mã đầu 256, cùng quy tắc thêm mục; dòng không hỏng; từ điển không giới hạn. **Kết luận:** sau khi xử lý $k_t$: (a) $y=w_1\cdots w_t$; (b) $w=w_t$; (c) các mục $256,\ldots,254+t$ của hai phía trùng nhau. Nói riêng $y=x$."
- **Nguồn:** ghi chú Định lý 11.23 (dòng 952–960).
- **Ghi chú diễn giả:** (c) chậm một mục so với Định lý 11.15; phạm vi: với từ điển $M$ mục, hai phía còn phải chung quy tắc xử lý từ điển đầy; giá của việc bỏ ký tự thô là nhánh 3.2 cùng Mệnh đề 11.22.
- **Quyết định:** sửa (`W05`, phần bất biến).
- **Âm tiết:** ~60.
- **Âm tiết (`deck_lint`, bản III.5):** 59.

#### `lec11-s04-06` — Ý tưởng chứng minh: LZW khôi phục đúng
- **Chức năng:** NT6; Bổ đề 11.21 và Mệnh đề 11.22 phát biểu ở bước dùng (kết quả phụ của trang này; chứng minh đầy đủ ở ghi chú; Bài tập 11.16 của recitation áp dụng Mệnh đề 11.22(b), không chứng minh lại); NT8 phản ví dụ.
- **Mặt trang:** "Quy nạp theo $t$." `ol`:
  1. **Bổ đề 11.21.** Bộ mã hóa thêm mục $255+t=w_t\operatorname{first}(w_{t+1})$ khi phát $k_t$, nên $k_{t+1}\le255+t$; bộ giải mã có $\texttt{next\_code}=255+t$ khi đọc $k_{t+1}$.
  2. Nếu $k_{t+1}<255+t$: mục đã có ở bộ giải mã và theo (c) trùng mục bộ mã hóa, nên $e=w_{t+1}$.
  3. **Mệnh đề 11.22.** Nếu $k_{t+1}=255+t$ thì $w_{t+1}=w_t\operatorname{first}(w_t)$, đúng giá trị nhánh 3.2 trả về.
  4. Mục thêm ở mã $255+t$ là $w_t\operatorname{first}(w_{t+1})$, trùng mục bộ mã hóa, nên (c) được giữ; sau $k_\tau$, $y=x$.
  - "Bỏ nhánh 3.2: dòng $97,98,256,258$ không giải được."
- **Nguồn:** ghi chú Bổ đề 11.21 (dòng 901–923), Mệnh đề 11.22 (dòng 925–950), chứng minh Định lý 11.23 (dòng 962–983).
- **Ghi chú diễn giả (~220):** cơ sở $t=1$: $w_1=x_1$, $k_1<256$; vì sao $\operatorname{first}(w_{t+1})=\operatorname{first}(w_t)$ khi $w_t$ là tiền tố của $w_{t+1}$ (chứng minh đầy đủ ở Mệnh đề 11.22 của ghi chú bài giảng); bỏ "cùng mã đầu 256": bộ giải mã dành 256 cho kết thúc dòng đọc mã 256 thành lệnh dừng; bỏ "không hỏng": mã lớn hơn `next_code` xuất hiện và nhánh 3.3 dừng.
- **Quyết định:** thêm (NT6).
- **Âm tiết:** ~68. **Ngoại lệ mật độ** (mục 8): hai kết quả phụ phải phát biểu tại bước dùng.
- **Âm tiết (`deck_lint`, bản III.5):** 81 (bản v1: 67).
- **Sửa III.5:** tiêu đề "Ý tưởng chứng minh: tính đúng của giải mã LZW"; Bổ đề 11.21 tách (a), (b), (c) và sửa quan hệ suy ra của (b); Mệnh đề 11.22 ghi (a), (b).

#### `lec11-s04-07` — Chi phí: LZW
- **Chức năng:** NT-DSFA-3; bước 8; câu nối sang mạch 5.
- **Mặt trang:** "**Mô hình:** một phép tra $D$ với khóa (mã của $w$, $c$), một phép thêm, một phép ghi ký tự đều tính một đơn vị; bảng băm băm đều, hệ số tải $\alpha<1$ hằng." Bảng: mã hóa, tra $w\,c$ | $n-1$ | $O(1)$ kỳ vọng | $O(n)$; mã hóa, phát và thêm | $\tau-1$ | $O(1)$ | $O(\tau)$; giải mã | $\tau$ | $\lvert w_t\rvert$ phép ghi | $n$. "Dòng mã $\tau b$ bit; bộ nhớ $O(M)$ mục (Mệnh đề 11.24). Trên `aabaacabcabcb` với mã 9 bit: 90 bit so với 104 bit." Câu kết: "Cả ba thuật toán LZ chỉ khai thác cụm khớp đúng từng ký tự; trên ảnh chụp, một hai điểm trong mỗi hai mươi điểm lệch một mức xám so với hàng kề."
- **Nguồn:** ghi chú Mệnh đề 11.24 (dòng 990–1013), Nhận xét 11.25 (dòng 1015–1020), kết Mục 4 (dòng 1058; NG tr. 247).
- **Ghi chú diễn giả:** điểm hòa vốn $9/8$ ký tự, chỉ ba trong mười mã là cụm hai ký tự; LZW12 của Nelson và Gailly: mã 12 bit, mã 256 là `END_OF_STREAM`, bảng băm $5\,021$ ô, $\alpha\le0{,}765$, tìm không thành công kỳ vọng $\le4{,}25$ lần dò nếu băm đều, hàm băm thật dùng dịch bit và XOR; `compress` của UNIX và GIF dùng LZW (Nelson và Gailly, tr. 214, 170).
- **Quyết định:** sửa (`W06` "Định dạng bit là hợp đồng riêng"): bỏ đổi độ rộng mã $T=2^b$, `MAX`, early/late change (outline D6, nguồn không trình bày); giữ mã cố định.
- **Âm tiết:** ~78 (trần 80); 7 dòng.
- **Âm tiết (`deck_lint`, bản III.5):** 78 (bản v1: 93).
- **Sửa III.5:** "Mô hình:" nêu $b$, $M=2^b$; câu nối mạch 4 → 5 "Trên ảnh chụp, cụm khớp đúng rất ngắn, nên ba thuật toán LZ gần như không rút ngắn được ảnh."; số liệu một hai trên hai mươi điểm (cùng một đường nét) ở ghi chú diễn giả.

### Mạch 5 — Nén ảnh JPEG dựa trên biến đổi cosine rời rạc (Mục 5; `lec-11-topic-13`…`-16`)

Một mạch, một câu hỏi (NT13), 11 trang (D-SB1, D-SB3). Hành trình: DCT (`s05-02` trực quan + ví dụ → `s05-03` định nghĩa, Ví dụ 11.10; Mệnh đề 11.28 phát biểu tại bước dùng ở `s05-06`); lượng tử hóa và cận sai số (`s05-04` trực quan, định nghĩa, Ví dụ 11.11 → `s05-05` Định lý 11.31 → `s05-06` ý tưởng chứng minh, Mệnh đề 11.30 tại bước dùng); mã hệ số (`s05-07` chạy tay, định nghĩa → `s05-08` ví dụ, Mệnh đề 11.33); cụm thuật toán 11.34: (1) giới hạn có số: câu kết `s04-07`; (2) ý tưởng ba giai đoạn: `s05-01`; (3) nhận xét cấu trúc (năng lượng dồn về tần số thấp; sai số trên điểm ảnh bằng sai số trên hệ số): `s05-03`, `s05-06`; (4) chạy tay: `s05-02`, `s05-04`, `s05-08`; (5)–(6): `s05-09`; (7): `s05-05`, `s05-06`, `s05-08`, dòng "Bảo đảm:" `s05-10`; (8): `s05-10`.

#### `lec11-s05-00` — 5. Nén ảnh JPEG dựa trên biến đổi cosine rời rạc (trang tiêu đề mạch)
- **Chức năng:** NT12, `id="mach-5"`, `#/5`; ngoài chu trình khái niệm.
- **Mặt trang:** "5. Nén ảnh JPEG dựa trên biến đổi cosine rời rạc"; dòng dẫn: "Chỉ bước lượng tử hóa bỏ dữ liệu, và sai số của mỗi khối bị chặn theo bước lượng tử." (19); từ khóa: "dịch mức · biến đổi cosine · lượng tử hóa · thứ tự zigzag · mã độ dài loạt".
- **Ghi chú diễn giả:** kế thừa đặc tả khôi phục gần đúng (Định nghĩa 11.1) và giới hạn của nén từ điển trên ảnh chụp; mạch dựng DCT, lượng tử hóa với cận sai số, mã hệ số và đường ống cả ảnh; trao cho mạch 6 bảo đảm $E_{\mathrm{RMS}}\le\beta(q)+\tfrac12$ và chi phí $\Theta(m)$.
- **Quyết định:** sửa (`JT`): tên mạch theo tên mục ghi chú, viết đầy đủ "biến đổi cosine rời rạc" vì trang "Nội dung" chưa giới thiệu chữ viết tắt (NT9).
- **Âm tiết:** ~35.
- **Âm tiết (`deck_lint`, bản III.5):** 21 (bản v1: 20).
- **Sửa III.5:** dòng dẫn "Chỉ bước lượng tử hóa bỏ dữ liệu, và sai số tái tạo bị chặn theo độ thô của bước đó."; ghi chú diễn giả viết lại.

#### `lec11-s05-01` — Ba giai đoạn nén ảnh
- **Chức năng:** trang nội dung đầu: bài toán có số (NT-DSFA-1), câu hỏi của mạch (NT13), ý tưởng (bước 2); hình đường ống.
- **Mặt trang:**
  - "Nén ảnh CHEETAH.GS, $64\,000$ điểm 8 bit, xuống tốc độ bit thấp với $E_{\mathrm{RMS}}$ không vượt một ngưỡng chọn trước, bộ nhớ vài hàng điểm, thời gian tỷ lệ số điểm."
  - "**Câu hỏi:** bỏ phần nào của mỗi khối để giảm byte mà sai số vẫn bị chặn?"
  - "JPEG (Joint Photographic Experts Group) làm ba giai đoạn: biến đổi cosine rời rạc (discrete cosine transform, DCT), lượng tử hóa (quantization) các hệ số, mã không mất thông tin các hệ số đã lượng tử."
  - Hình `jpeg-duong-ong-trang-chieu.svg` (hàng nén, hàng giải nén; khối lượng tử hóa viền nét đứt đậm).
- **Nguồn:** ghi chú Mục 5 mở (dòng 1062–1066; NG tr. 250–251), hình `note-jpeg-duong-ong.svg`. CMU L tc. 13 (JPEG: mã hóa biến đổi, lượng tử vô hướng, mã sai phân, mã độ dài loạt, Huffman hoặc mã số học), tc. 14 (sơ đồ JPEG).
- **Ghi chú diễn giả:** đọc hình: mỗi khối hàng dưới đảo ngược khối trên, trừ lượng tử hóa (từ $\hat F$ chỉ dựng được $Q\hat F$); ảnh màu nén như ba ảnh xám (Nelson và Gailly, tr. 264); mã hóa biến đổi tuyến tính viết $\Theta=Ax$, mỗi hàng của $A$ là một hàm cơ sở (Blelloch, CMU 15-499, phần nén mất dữ liệu, trang chiếu 7–8).
- **Quyết định:** gộp (`J00` + `J02`): hình vẽ lại thay `jpeg-pipeline.svg`; bỏ lấy mẫu thưa màu (ngoài phạm vi Q9); thêm tên đầy đủ của JPEG (NT21, cổng III.2).
- **Âm tiết:** ~59.
- **Âm tiết (`deck_lint`, bản III.5):** 60 (bản v1: 61).
- **Sửa III.5:** mở bằng "Ảnh chỉ cần khôi phục gần đúng:"; thêm mã hóa entropy (entropy coding); ghi chú diễn giả: JPEG cơ sở dùng Huffman, ảnh màu theo R, G, B hoặc độ sáng–sắc độ.

#### `lec11-s05-02` — Ví dụ: khối $8\times8$ của CHEETAH.GS và hệ số DC
- **Chức năng:** NT8 trực quan rồi ví dụ (trước định nghĩa); NT23; dữ kiện của ví dụ xuyên suốt "khối Hình 11.9 của NG".
- **Mặt trang:**
  - "**Trực quan.** Các điểm trong một khối có giá trị gần nhau; viết khối thành tổng 64 mẫu cosine thì phần lớn năng lượng, tức tổng bình phương, dồn vào vài hệ số tần số thấp."
  - "Tính hệ số DC của khối:" ma trận $P$ của Ví dụ 11.9 (một công thức hiển thị).
  - "Tổng $9\,680$, trung bình $151{,}25$; dịch mức $A=P-128$ cho tổng $1\,488$."
  - "Mẫu tần số 0 gồm tám giá trị $1/\sqrt8$, nên $F_{00}=\tfrac18\sum_{\xi,\eta}A_{\xi\eta}=1\,488/8=186$."
- **Nguồn:** ghi chú 5.1 mở (dòng 1071–1073; NG tr. 254–255), Ví dụ 11.9 (dòng 1075–1105; NG Hình 11.9, tr. 258). CMU L tc. 9.
- **Ghi chú diễn giả:** vì sao khối $8\times8$: khối $256\times256$ cần $256^4\approx4{,}3\cdot10^9$ số hạng, và tương quan giữa các điểm gần như mất sau mười lăm, hai mươi vị trí (Nelson và Gailly, tr. 255); $F_{00}$ bằng 8 lần độ sáng trung bình sau dịch mức; Nelson và Gailly in 186 ở ô $(0,0)$.
- **Quyết định:** sửa (`J03` "Khối 8×8 tạo đơn vị xử lý cục bộ"): mở bằng khối có số của sách.
- **Âm tiết:** ~57 (ma trận không tính).
- **Âm tiết (`deck_lint`, bản III.5):** 54 (bản v1: 56).
- **Sửa III.5:** xếp dọc: "Trực quan.", ma trận $P$, rồi phép tính; gọi tên hàng $\xi$, cột $\eta$ tại chỗ.

#### `lec11-s05-03` — Dịch mức, DCT và IDCT
- **Chức năng:** NT8 phát biểu (Định nghĩa 11.26); hình mẫu cosine đọc ma trận $T$; Ví dụ 11.10 một dòng (nhận xét cấu trúc, bước 3).
- **Mặt trang:** "**Định nghĩa 11.26.**"
  - "Dịch mức (level shift): $A=P-128$, giá trị trong $\{-128,\ldots,127\}$."
  - Hiển thị (`aligned`): với $u,\xi\in\{0,\ldots,7\}$, $T_{0\xi}=\tfrac1{\sqrt8}$, $T_{u\xi}=\tfrac12\cos\tfrac{(2\xi+1)u\pi}{16}$ khi $u\ge1$ (miền chỉ số theo ghi chú dòng 1110; chỉ số đánh từ 0).
  - "DCT của $A$ là $F=TAT^{\top}$; $F_{00}$ là hệ số DC (DC coefficient). Biến đổi ngược (inverse DCT, IDCT) của $G$ là $T^{\top}GT$."
  - Hình `dct-ham-co-so-trang-chieu.svg` (tám hàng của $T$): "Hàng $u$ của $T$ đổi dấu đúng $u$ lần."
  - "**Ví dụ 11.10.** Trên khối CHEETAH.GS, hệ số DC chiếm khoảng $80\%$ tổng bình phương các hệ số."
- **Nguồn:** ghi chú Định nghĩa 11.26 (dòng 1107–1129; NG tr. 255–256, 268), hình `note-dct-ham-co-so.svg` (dòng 1131–1133), Ví dụ 11.10 (dòng 1213–1237). CMU L tc. 8 (hệ số $\Theta_i=\sum_jx_j\phi_i(j)$), tc. 9, tc. 12 (dồn năng lượng).
- **Ghi chú diễn giả:** dạng tổng kép với $\gamma(u)$; $F_{uv}$ đo mức khối giống mẫu tần số $u$ theo chiều dọc, $v$ theo chiều ngang; Nelson và Gailly gọi ma trận DCT là $C$; Ví dụ 11.10 đầy đủ: tổng bình phương $43\,372$, hệ số DC $186^2=34\,596$, 28 hệ số có $u+v\ge8$ chỉ khoảng $4{,}4\%$; DCT không rút ngắn khối, mỗi hệ số cần 11 bit (Nelson và Gailly, tr. 258).
- **Quyết định:** gộp (`J04` + `J05` và trang "DCT trực chuẩn" của bản storyboard đầu, D-SB1): định nghĩa trước, hình mẫu cosine vẽ từ số của $T$ (thay `dct-basis.svg` "minh họa định tính"); Mệnh đề 11.28 chuyển sang bước 1–2 của `s05-06`.
- **Âm tiết:** ~52.
- **Âm tiết (`deck_lint`, bản III.5):** 53.
- **Sửa III.5:** công thức $T$ một dòng; "Hàng $u$ …" và Ví dụ 11.10 tách hai dòng.

#### `lec11-s05-04` — Lượng tử hóa
- **Chức năng:** NT8 trực quan (kèm chạy tay một ô) → phát biểu (Định nghĩa 11.29) → ví dụ (Ví dụ 11.11), đúng thứ tự ghi chú.
- **Mặt trang:**
  - "**Trực quan.** Như đo bằng thước có vạch thưa: $F_{01}=-18$ với bước 5 ghi thành $-4$, tái tạo $-20$; mọi giá trị trong $(-22{,}5;\,-17{,}5]$ cũng cho $-4$."
  - "**Định nghĩa 11.29.** Ma trận lượng tử $Q_{uv}=1+(1+u+v)\,q$ với hệ số chất lượng $q$; lượng tử hóa $\hat F_{uv}=\operatorname{round}(F_{uv}/Q_{uv})$; giải lượng tử $\tilde F_{uv}=Q_{uv}\hat F_{uv}$."
  - "**Ví dụ 11.11.** Khối CHEETAH.GS, $q=2$, $Q_{uv}=3+2(u+v)$:" ma trận $\hat F$ (một công thức hiển thị). "Có 30 số khác 0; hàng cuối toàn 0."
- **Nguồn:** ghi chú 5.2 mở (dòng 1242–1246; NG tr. 259), Định nghĩa 11.29 (dòng 1248–1257; NG tr. 260), Ví dụ 11.11 (dòng 1259–1303; NG Hình 11.10). CMU L tc. 3 (lượng tử hóa vô hướng), tc. 15 (bảng lượng tử chuẩn chia đều cho hệ số chất lượng).
- **Ghi chú diễn giả:** round làm tròn xa 0 khi phần lẻ đúng $\tfrac12$; bước tăng theo đường chéo $u+v$, mỗi đường chéo hơn đường trước $q$; $q$ ghi vào tệp nén (Nhận xét 11.3); vài ô: $186/3=62$, $-34/7\approx-4{,}86\to-5$, $15/25=0{,}6\to1$; nhầm lẫn "chỉ làm tròn nên không đáng kể": bước 31 ở ô $(7,7)$ đưa mọi hệ số từ $-15$ tới $15$ về 0; ISO có bảng chuẩn (Blelloch, CMU 15-499, phần nén mất dữ liệu, trang chiếu 15).
- **Quyết định:** gộp (`J07` + phần định nghĩa của `J06` + trang ví dụ lượng tử hóa của bản storyboard đầu, D-SB1): bỏ hình `quantization.svg`; ô $(0,2)$, $(0,4)$ của Hình 11.11 là Bài tập 11.8 (bài về nhà); CMU đặt lượng tử hóa vô hướng (L tc. 3) trước biến đổi (tc. 7–12), deck theo thứ tự ghi chú (NT2).
- **Âm tiết:** ~58 (ma trận không tính); 5 dòng và hai công thức hiển thị.
- **Âm tiết (`deck_lint`, bản III.5):** 54 (bản v1: 60).
- **Sửa III.5:** "Trực quan." và Định nghĩa 11.29 toàn bề rộng, rồi Ví dụ 11.11 cạnh ma trận; thêm "xa 0 khi phần lẻ $\tfrac12$", giải lượng tử (dequantization).

#### `lec11-s05-05` — Sai số tái tạo của một khối
- **Chức năng:** NT5 (Định lý 11.31, kết quả chính); ứng dụng vào ví dụ xuyên suốt. Tiêu đề theo tên kết quả, không tiền tố "Tính đúng:" vì đây là định lý, không phải thuật toán (NT-DSFA-2, cổng III.2).
- **Mặt trang:**
  - "**Định lý 11.31.** **Giả thiết:** $F=TAT^{\top}$ và $\tilde A=T^{\top}\tilde FT$ tính bằng số thực chính xác; lượng tử hóa làm tròn tới số nguyên gần nhất; $\tilde A$ chưa làm tròn, chưa cắt. **Kết luận:**" hiển thị $E_{\mathrm{RMS}}(A,\tilde A)=\sqrt{\tfrac1{64}\sum_{u,v}(F_{uv}-\tilde F_{uv})^2}\le\beta(q)=\tfrac12\sqrt{\tfrac1{64}\sum_{u,v}Q_{uv}^2}$ (`aligned`, hai dòng).
  - "Với $q=2$, $\beta(2)\approx9{,}10$; khối CHEETAH.GS tái tạo có $E_{\mathrm{RMS}}(A,\tilde A)=4{,}18$ mức xám (Ví dụ 11.12)."
  - "**Ý nghĩa:** cận không phụ thuộc nội dung ảnh, nên chọn được $q$ trước khi nén."
- **Nguồn:** ghi chú Định lý 11.31 (dòng 1340–1354), $\beta(2)$ (dòng 1383), Ví dụ 11.12 (dòng 1385–1412), Tình huống 11.1 (dòng 1744).
- **Ghi chú diễn giả (≤250):** Ví dụ 11.12: sai số trên hệ số $4{,}12$ (hệ số làm tròn), $4{,}18$ (hệ số chính xác) bằng đúng $E_{\mathrm{RMS}}(A,\tilde A)$; điểm lệch nhiều nhất 11 mức; cận đạt khi mọi hệ số lệch đúng nửa bước; định lý không cho số bit; sau khi làm tròn và cắt điểm ảnh, sai số đo được là $4{,}21$.
- **Quyết định:** sửa (`J09` "IDCT tái tạo hệ số đã lượng tử"): thêm định lý cận sai số của ghi chú. Bước 7 (tính đúng) của cụm Thuật toán 11.34 rút gọn thành định lý này, ý tưởng chứng minh `s05-06` và dòng "Bảo đảm:" ở `s05-10` ngay sau thuật toán: giữ thứ tự ghi chú (NT2, D-SB8) và trần 55 trang. Số so với cận là $4{,}18$ (đại lượng định lý chặn), không phải $4{,}21$ (sau làm tròn điểm ảnh) (cổng III.2).
- **Âm tiết:** ~52.
- **Âm tiết (`deck_lint`, bản III.5):** 55.

#### `lec11-s05-06` — Ý tưởng chứng minh: sai số tái tạo bị chặn theo bước lượng tử
- **Chức năng:** NT6 (3 bước); Mệnh đề 11.28 và 11.30 (kết quả phụ) phát biểu tại bước dùng, như Bổ đề 11.21 và Mệnh đề 11.22 ở `s04-06`; NT8 phản ví dụ khi bỏ giả thiết.
- **Mặt trang:** "**Nhắc lại:** $X$ trực chuẩn khi $XX^{\top}=I$; khi đó $X^{-1}=X^{\top}$." `ol`:
  1. **Mệnh đề 11.28.** $TT^{\top}=I$, nên $A-\tilde A=T^{\top}(F-\tilde F)T$ (giả thiết tính chính xác).
  2. **Kỹ thuật.** Biến đổi trực chuẩn giữ tổng bình phương, nên sai số trên điểm ảnh bằng sai số trên hệ số (Mệnh đề 11.28(c)).
  3. **Mệnh đề 11.30.** Vì $\lvert z-\operatorname{round}(z)\rvert\le\tfrac12$ (giả thiết làm tròn), công thức hiển thị $\lvert F_{uv}-\tilde F_{uv}\rvert\le Q_{uv}/2$; cộng bình phương, chia 64, lấy căn.
- **Nguồn:** ghi chú Bổ đề 11.27 (dòng 1135–1164), Mệnh đề 11.28 (dòng 1166–1211), Mệnh đề 11.30 (dòng 1305–1336), chứng minh Định lý 11.31 (dòng 1356–1381). CMU L tc. 12 (biến đổi trực chuẩn, $\sum x^2=\sum\Theta^2$).
- **Ghi chú diễn giả (~220):** vết thỏa $\operatorname{tr}(XY)=\operatorname{tr}(YX)$, dùng cho Mệnh đề 11.28(c); chứng minh $TT^{\top}=I$: tích hai hàng khác nhau là tổng cosine $\sum_{\xi=0}^{7}\cos((2\xi+1)\mu\pi/16)=0$ với $0<\mu<16$ (Bổ đề 11.27); cắt về 0 thay cho làm tròn thì cận nhân đôi; Mệnh đề 11.30(a): mỗi giá trị $\hat F_{uv}$ ứng với cả một khoảng nên lượng tử hóa không khả nghịch; biến đổi $\tfrac12TAT^{\top}$ không trực chuẩn làm sai số gấp đôi; phép cắt về $[0;255]$ không làm sai số tăng, làm tròn điểm ảnh cộng tối đa $\tfrac12$.
- **Quyết định:** thêm (NT6); nhận phát biểu của Mệnh đề 11.28, 11.30 (D-SB1); "Nhắc lại:" và "Kỹ thuật." lên mặt trang (NT9, NT7, cổng III.2).
- **Âm tiết:** ~58; một công thức hiển thị (bất đẳng thức then chốt, NT6). Câu "cắt về 0 thì cận nhân đôi" chuyển vào ghi chú diễn giả; "Nhắc lại:" và nhãn "Kỹ thuật." thêm theo cổng III.2 (NT9, NT7).
- **Âm tiết (`deck_lint`, bản III.5):** 57 (bản v1: 55).
- **Sửa III.5:** tiêu đề "Ý tưởng chứng minh: cận sai số tái tạo"; Mệnh đề 11.28 ghi (a), (c); bước "Kỹ thuật." áp (c) cho $T^{\top}$.

#### `lec11-s05-07` — Sai phân DC, thứ tự zigzag và mã độ dài loạt
- **Chức năng:** chạy tay trước định nghĩa (ghi chú dòng 1421) rồi phát biểu (Định nghĩa 11.32).
- **Mặt trang:**
  - "Mười bốn số đầu của $\hat F$ theo đường chéo kết thúc bằng $0,0,0,-1$, viết gọn thành $(3,1,-1)$."
  - "**Định nghĩa 11.32.**"
    - "Sai phân DC $\delta_\kappa=\hat F_{00}^{(\kappa)}-\hat F_{00}^{(\kappa-1)}$; 63 hệ số còn lại là hệ số AC (AC coefficients)."
    - "Thứ tự zigzag (zig-zag sequence): các ô theo $u+v$ tăng dần, đổi chiều sau mỗi đường chéo; vị trí zigzag của ô đếm từ 1."
    - "Mã độ dài loạt (run-length encoding, RLE): mỗi số khác $0$ là $a$ cho bộ ba $(r,s,a)$, $r$ là số các số $0$ đứng trước, $s=\lfloor\log_2\lvert a\rvert\rfloor+1$; loạt $r$ số $0$ cuối khối cho $(r,0)$."
- **Nguồn:** ghi chú 5.3 (dòng 1417–1433; NG tr. 261–264). CMU L tc. 14 (sai phân DC so với khối trước), tc. 16 (thứ tự quét khối, mã độ dài loạt cho dãy số 0).
- **Ghi chú diễn giả:** các khối xử lý theo thứ tự đọc, $\delta_1=\hat F_{00}^{(1)}$; quy tắc đầy đủ của zigzag: trong một đường chéo, $u$ tăng khi $u+v$ lẻ, giảm khi $u+v$ chẵn; bộ $(r,0)$ là quy ước của chương, không phải mã kết thúc khối của JPEG chuẩn; $s=1$ cho $\pm1$, $s=2$ cho $\pm2,\pm3$; zigzag đi theo các đường chéo có cùng bước lượng tử; mã entropy (Huffman hoặc mã số học của Bài 10) mã tiếp phần $(r,s)$.
- **Quyết định:** sửa (`J08` phần định nghĩa): thêm $s$ và bộ $(r,0)$ theo ghi chú; số trong câu viết bằng KaTeX.
- **Âm tiết:** ~60 (bản đầu ~66; giảm bằng cách chuyển quy tắc lẻ–chẵn vào ghi chú diễn giả và viết các số 0 bằng KaTeX).
- **Âm tiết (`deck_lint`, bản III.5):** 87 (bản v1: 66).
- **Sửa III.5:** mở bằng "Trực quan." nêu vấn đề (34 số 0 dồn về góc tần số cao); bỏ bộ $(3,1,-1)$ trước định nghĩa (chuyển vào ghi chú diễn giả); thêm $\hat F_{00}^{(0)}=0$.

#### `lec11-s05-08` — Ví dụ: dãy zigzag của khối đã lượng tử
- **Chức năng:** NT23; NT5 Mệnh đề 11.33 (kết quả phụ; lý do chứng minh trong ghi chú diễn giả, NT6) sau ví dụ, phát biểu đủ giả thiết như ghi chú.
- **Mặt trang:**
  - "Giả sử khối liền trước có $\hat F_{00}=60$, nên $\delta=2$. Xác định dãy bộ của khối." Hình `zigzag-khoi-luong-tu-trang-chieu.svg`.
  - "Khối cho 31 bộ: 30 bộ ba và $(9,0)$."
  - "**Mệnh đề 11.33.** **Giả thiết:** mỗi khối có đúng 64 số; các bộ được truyền đúng. **Kết luận:** bộ giải mã dựng lại đúng $\hat F^{(\kappa)}$ của mọi khối, nên lượng tử hóa là bước duy nhất làm mất dữ liệu."
- **Nguồn:** ghi chú Ví dụ 11.13 (dòng 1455–1480), hình `note-zigzag-khoi-luong-tu.svg`, Mệnh đề 11.33 (dòng 1435–1453).
- **Ghi chú diễn giả:** bộ ba DC $(0,2,2)$; số khác 0 cuối ở vị trí 55, ô $(4,7)$, nên chín vị trí cuối cho bộ $(9,0)$; phần biên độ tốn 2 bit cho DC và 39 bit cho 29 hệ số AC; vị trí 6 là ô $(0,2)$, vị trí 15 là ô $(0,4)$. Chứng minh mệnh đề: thứ tự zigzag là song ánh giữa 64 ô và 64 vị trí, và $\hat F_{00}^{(\kappa)}=\delta_1+\cdots+\delta_\kappa$; giả thiết "mỗi khối đúng 64 số" cho bộ giải mã biết khối kết thúc ở đâu.
- **Quyết định:** sửa (`J08` phần ví dụ): hình vẽ lại từ khối đã lượng tử thay `zigzag.svg`; thêm giả thiết của Mệnh đề 11.33 lên mặt trang, chuyển dòng "Chứng minh." và câu "vị trí 55" vào ghi chú diễn giả để giữ trần 60 (cổng III.2).
- **Âm tiết:** ~55.
- **Âm tiết (`deck_lint`, bản III.5):** 86 (bản v1: 60).
- **Sửa III.5:** ba bước chính lên mặt trang (DC $(0,2,2)$; vị trí 14 cho $(3,1,-1)$; $(9,0)$), "Diễn giải:" và Mệnh đề 11.33 rút gọn cùng trang (không tách trang để giữ 55 trang giảng).

#### `lec11-s05-09` — Thuật toán: nén và giải nén theo khối $8\times8$
- **Chức năng:** NT-DSFA-2 bước 5–6; giả mã 12 dòng đứng một mình, hai cột (`.ex-grid2`).
- **Mặt trang:** câu dẫn: "Chỉ bước lượng tử hóa phụ thuộc $q$." "**Đầu vào:** ảnh xám $m_{\mathrm h}\times m_{\mathrm w}$ điểm 8 bit, hai cạnh chia hết cho 8; hệ số chất lượng $q$. **Đầu ra:** dòng bit có ghi $q$; khi giải nén, ảnh $\tilde P$ cùng cỡ."
  - Cột "Nén": 1. Ghi $q$; dựng $Q$, $T$. 2. Với mỗi khối $\kappa$: $A=P-128$; $F=TAT^{\top}$; $\hat F_{uv}=\operatorname{round}(F_{uv}/Q_{uv})$; $\delta_\kappa=\hat F_{00}^{(\kappa)}-\hat F_{00}^{(\kappa-1)}$; xếp zigzag, mã độ dài loạt, mã entropy.
  - Cột "Giải nén": 1. Đọc $q$; dựng $Q$, $T$. 2. Với mỗi khối $\kappa$: giải mã entropy và mã độ dài loạt tới đủ 64 số; cộng dồn hệ số DC, đặt hệ số AC về ô theo zigzag; $\tilde F=Q\hat F$; $\tilde A=T^{\top}\tilde FT$; $\tilde P$ là $\tilde A+128$ làm tròn, cắt về $[0;255]$.
- **Nguồn:** ghi chú Thuật toán 11.34 (dòng 1487–1538). CMU L tc. 14.
- **Ghi chú diễn giả:** thứ tự đọc: từng dải 8 hàng từ trên xuống, trong dải từ trái sang phải; $\hat F_{00}^{(0)}=0$; phép quyết định là lượng tử hóa, bước duy nhất phụ thuộc $q$; trường hợp biên: khối có mọi hệ số AC bằng 0 cho bộ ba DC và $(63,0)$, cạnh không chia hết cho 8 nằm ngoài giả thiết, $q=0$ chỉ còn sai số làm tròn; mã entropy là mã Huffman hoặc mã số học của Bài 10 (Blelloch, CMU 15-499, phần nén mất dữ liệu, trang chiếu 14).
- **Quyết định:** thêm (deck cũ không có giả mã đường ống).
- **Âm tiết:** ~58 (giả mã có tính).
- **Âm tiết (`deck_lint`, bản III.5):** 73; 13 dòng (bản v1: 66).
- **Sửa III.5:** khôi phục câu dẫn "Chỉ bước lượng tử hóa phụ thuộc $q$."; bước 2.3 thêm $\hat F_{00}^{(0)}=0$.

#### `lec11-s05-10` — Chi phí: nén một ảnh theo khối
- **Chức năng:** NT-DSFA-3; bước 8; câu kết "Bảo đảm:" cho cả ảnh đứng ngay sau Thuật toán 11.34 như ghi chú (dòng 1529–1536; D-SB8).
- **Mặt trang:** "**Mô hình:** đếm phép nhân ở DCT, IDCT, phép chia ở lượng tử hóa, phép xử lý một hệ số ở các bước còn lại; $K=m/64$ khối." Bảng `Bước | Số lần | Chi phí mỗi lần | Đóng góp`: dịch mức | $K$ | 64 phép trừ | $m$; DCT | $K$ | $1\,024$ phép nhân | $16m$; lượng tử hóa | $K$ | 64 phép chia | $m$; sai phân DC, zigzag, loạt, mã entropy | $K$ | $O(64)$ | $O(m)$; giải nén | $K$ | $64+1\,024$ phép nhân, $O(64)$ | $O(m)$. "Thời gian $\Theta(m)$; bộ nhớ một dải $8\times m_{\mathrm w}$ điểm; CHEETAH.GS có $1\,000$ khối, $1\,024\,000$ phép nhân cho DCT." Câu kết: "**Bảo đảm:** theo Mệnh đề 11.33 và Định lý 11.31, ảnh tái tạo có $E_{\mathrm{RMS}}\le\beta(q)+\tfrac12$ khi DCT, IDCT tính chính xác."
- **Nguồn:** ghi chú lập luận sau Thuật toán 11.34 (dòng 1529–1536), bảng chi phí (dòng 1518–1527), đoạn chi phí (dòng 1540), Nhận xét 11.35 (dòng 1548–1553), kết Mục 5 (dòng 1646). CMU L tc. 13 (tỷ lệ khoảng 10 lần), tc. 17 ($0{,}125$ bit mỗi điểm) chỉ ở ghi chú diễn giả.
- **Ghi chú diễn giả:** bình phương sai số RMS của cả ảnh là trung bình bình phương sai số các khối, nên $\le\beta(q)^2$; làm tròn điểm ảnh cộng tối đa $\tfrac12$; tính trực tiếp theo tổng kép tốn $8\,192$ phép nhân mỗi khối, gấp 8 dạng ma trận; đánh đổi tốc độ bit–sai số trên CHEETAH.GS (Hình 11.14 của Nelson và Gailly): $q\le5$ chỉ giảm nhẹ độ nét, $q>5$ lộ hiện tượng khối; chương trình của Nelson và Gailly cắt thương về 0, cận $18{,}23$ ở $q=2$, nên số đo $6{,}9$ của nó không được $\beta(q)$ bảo đảm; số byte chỉ đo được trên từng ảnh ($18\,367$ byte trên CHEETAH.GS, $14\,243$ trên CLOWN.GS ở $q=2$); JPEG thường nén khoảng 10 lần (Blelloch, CMU 15-499, phần nén mất dữ liệu, trang chiếu 13).
- **Quyết định:** sửa (`J10` "Chi phí tỉ lệ với số điểm ảnh"): bảng NT-DSFA-3, thêm dòng bảo đảm; `J11` "Kiểm tra đường ống JPEG" bỏ (câu hỏi tự dựng; bước kiểm tra là Bài tập 11.17 của recitation).
- **Âm tiết:** ~75 (trần 80 của bảng chi phí); 8 dòng (bảng 5 hàng).
- **Âm tiết (`deck_lint`, bản III.5):** 78 (bản v1: 88).
- **Sửa III.5:** gọi tên $m_{\mathrm w}$; dòng CHEETAH.GS ($1\,000$ khối, $1\,024\,000$ phép nhân) chuyển vào ghi chú diễn giả.

### Mạch 6 — Tổng kết (Mục 6, Tình huống, Tóm tắt; `lec-11-topic-17`, `-18`, `-19`, `-21`; bài tập tổng hợp `lec11-s06-04`, `lec11-s06-05` lấy từ `lec-11-topic-20`)

Không khái niệm mới (NT15). Thứ tự trang theo NT15 và NT-DSFA-10; "Tài liệu tham khảo" là trang cuối của mạch.

#### `lec11-s06-00` — 6. Tổng kết (trang tiêu đề mạch)
- **Chức năng:** NT12, NT15, `id="mach-6"`, `#/6`.
- **Mặt trang:** "6. Tổng kết"; dòng dẫn: "Đặc tả khôi phục và dạng dư thừa của dữ liệu quyết định nên dùng bộ nén nào." (17); từ khóa: "bảng kết quả · bảng thuật toán · vấn đề trung tâm · bài tập về nhà".
- **Ghi chú diễn giả:** kế thừa bốn bảo đảm (Định lý 11.8, 11.15, 11.23, 11.31) và bốn bảng chi phí; mạch đặt chúng cạnh nhau, trả lời câu hỏi trung tâm, giao bài.
- **Quyết định:** sửa (`ST` "Tổng kết và tự kiểm tra").
- **Âm tiết:** ~30.
- **Âm tiết (`deck_lint`, bản III.5):** 18.

#### `lec11-s06-01` — Kết quả chính
- **Chức năng:** NT15 bảng tổng kết, P4 cột ba `Công thức hoặc thuật toán`.
- **Mặt trang:** bảng `Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán`:
  - Mệnh đề 11.2 | $\lvert\varphi(x)\rvert<8m$ với mọi ảnh $x$ | có $x$ với $\psi(\varphi(x))\ne x$
  - Định lý 11.8 (LZ77) | chép tuần tự; giữ $W$ ký tự cuối | $y_{p+j}\leftarrow y_{p+j-d}$, $j$ tăng dần; $y=x$
  - Định lý 11.15 (LZ78) | cùng từ điển đầu, cùng quy tắc thêm mục và đánh mã | $D'[j]=D[j]$ sau mỗi cặp; $y=x$
  - Định lý 11.23 (LZW) | cùng nạp sẵn, cùng mã đầu 256; dòng không hỏng | $k=\texttt{next\_code}\Rightarrow e=w\operatorname{first}(w)$; $y=x$
  - Định lý 11.31 | DCT chính xác; lượng tử hóa làm tròn | $E_{\mathrm{RMS}}(A,\tilde A)\le\beta(q)=\tfrac12\sqrt{\tfrac1{64}\sum Q_{uv}^2}$
  - Mệnh đề 11.33 | mỗi khối đúng 64 số | lượng tử hóa là bước duy nhất làm mất dữ liệu
- **Nguồn:** ghi chú Tóm tắt chương (dòng 1802–1851, "Giả thiết hay bị bỏ quên").
- **Ghi chú diễn giả:** mỗi giả thiết bị bỏ thì hỏng ở đâu (chép khối; quy tắc lệch; thiếu nhánh 3.2; cắt về 0 gần như nhân đôi cận, nên số đo của chương trình của Nelson và Gailly không được $\beta(q)$ bảo đảm).
- **Quyết định:** thêm.
- **Âm tiết:** ~70 (trần 80 của bảng tổng kết); 6 hàng.
- **Âm tiết (`deck_lint`, bản III.5):** 91 (bản v1: 81).
- **Sửa III.5:** cột giả thiết của Định lý 11.15, 11.23 thêm "xử lý từ điển đầy".

#### `lec11-s06-02` — Bốn thuật toán
- **Chức năng:** P4 bảng `Thuật toán | Đầu vào | Bảo đảm | Chi phí` cùng mô hình chi phí.
- **Mặt trang:** "**Mô hình:** phép so, phép tra hoặc phép ghi một ký tự; phép nhân cho DCT; kỳ vọng dưới giả thiết băm đều." Bảng:
  - LZ77 (Thuật toán 11.5, 11.6) | chuỗi $n$ ký tự; $W$, $L$ | $y=x$ | mã hóa $O(nWL)$, giải mã $n$ phép ghi; bộ ba $\lceil\log_2W\rceil+\lceil\log_2(L+1)\rceil+8$ bit
  - LZ78 (Thuật toán 11.13, 11.14) | chuỗi; từ điển $M$ mục | $y=x$ | kỳ vọng $O(n)$; cặp $\lceil\log_2M\rceil+9$ bit
  - LZW (Thuật toán 11.19, 11.20) | chuỗi byte; mã $b$ bit, $M=2^b$ | $y=x$, kể cả mã chưa có | kỳ vọng $O(n)$; $\tau b$ bit
  - Nén theo khối (Thuật toán 11.34) | ảnh $m$ điểm; $q$ | $E_{\mathrm{RMS}}\le\beta(q)$ mỗi khối | $\Theta(m)$; $1\,024$ phép nhân mỗi khối
- **Nguồn:** ghi chú bảng Mục 6 (dòng 1686–1693), Nhận xét 11.36 (dòng 1695–1699). CMU LZ tc. 20–21 (mọi biến thể LZ giữ một từ điển, khác ở cách lưu, mở rộng, đánh chỉ số, bỏ mục) ở ghi chú diễn giả.
- **Ghi chú diễn giả:** cột "dư thừa khai thác" của ghi chú (lặp gần, lặp xa, năng lượng dồn về tần số thấp) và trạng thái ($W+L+1$ ký tự; cây $\le M$ mục; một dải $8\times m_{\mathrm w}$ điểm); điểm hòa vốn $1{,}75$; $3$; $3{,}125$; $1{,}125$; $1{,}5$ ký tự.
- **Quyết định:** sửa (`S00` "Chọn cấu trúc theo hợp đồng và chi phí"): theo bảng của ghi chú, thêm số bit.
- **Âm tiết:** ~65; 4 hàng.
- **Âm tiết (`deck_lint`, bản III.5):** 93 (bản v1: 81).
- **Sửa III.5:** cột "Bảo đảm" của LZ78, LZW thêm điều kiện chung quy tắc từ điển đầy.

#### `lec11-s06-03` — Vấn đề trung tâm
- **Chức năng:** NT15, NT-DSFA-5: trả lời có điều kiện câu hỏi trung tâm cho cả bài, giả thiết nào cho phép thay mã từng ký hiệu bằng cấu trúc nào, thu hồi tình huống mở bài bằng con số; mỗi con số đi kèm giả thiết của nó (NT2).
- **Mặt trang:** danh sách:
  - "Văn bản, khôi phục đúng: cụm lặp gần dùng cửa sổ của LZ77, cụm lặp xa dùng từ điển cụm của LZ78 hoặc LZW, thời gian kỳ vọng $O(n)$ với bảng băm; cả ba cho $y=x$."
  - "Ảnh, ngưỡng 10 mức xám: nếu DCT tính chính xác và lượng tử hóa làm tròn, mỗi ảnh có $E_{\mathrm{RMS}}\le\beta(q)+\tfrac12$; $q=2$ cho $9{,}60\le10$."
  - "Danh mục $1\,000$ ảnh, 64 MB: chương trình cắt thương của Nelson và Gailly ở $q=2$ còn khoảng $18{,}4$ MB nếu mọi ảnh như CHEETAH.GS; số đo này không được $\beta(q)$ bảo đảm."
- **Nguồn:** ghi chú kết Mục 6 (dòng 1721–1723), Ví dụ 11.14 (dòng 1653–1678), Tình huống 11.1 (dòng 1733–1747), Nhận xét 11.35 (dòng 1550), Tình huống 11.4 (CMU-I tc. 10).
- **Ghi chú diễn giả:** mỗi bộ nén từ điển chỉ rút ngắn khi một đơn vị mã mô tả trung bình hơn số ký tự hòa vốn: $1{,}75$ ký tự cho bộ ba 14 bit, $3{,}125$ cho cặp LZ78 25 bit, $1{,}125$ cho mã LZW 9 bit. Trên `aabaacabcabcb`, với $W=6$, $L=4$, mã cụm LZ78 3 bit và mã LZW 9 bit, ba bộ nén tốn 70, 72, 90 bit so với 104 bit (Ví dụ 11.14). Trên bộ Calgary, gzip, một biến thể LZ77, đạt $2{,}59$ bit mỗi ký tự (Tình huống 11.4; Blelloch, CMU 15-499, phần nhập môn, trang chiếu 10). Chương trình của Nelson và Gailly cắt thương về 0 nên cận của nó ở $q=2$ là khoảng $18{,}2$, lớn hơn 10; con số $6{,}9$ trên CHEETAH.GS là số đo, không phải bảo đảm. LZ77 cho ảnh chụp với $\ell=1$ cho $96\,000$ byte, gấp $1{,}5$ ảnh gốc (Tình huống 11.2); nén mất dữ liệu cho văn bản vi phạm Định nghĩa 11.1.
- **Quyết định:** thêm. Dòng 70/72/90 bit chuyển vào ghi chú diễn giả vì cần ba giả thiết về độ rộng mã; dòng ảnh nêu ngưỡng 10 và tách cận của bộ nén làm tròn khỏi số đo của chương trình cắt thương (cổng III.2).
- **Âm tiết:** ~86. **Ngoại lệ mật độ** (mục 8): trước ~85 (bản đầu, có dòng 70/72/90), sau ~86 (thêm giả thiết của các con số); trần 60, giới hạn 90; lý do: NT-DSFA-5. Đã xét thêm con số của kho văn bản (gzip $2{,}59$ bit mỗi ký tự trên bộ Calgary) lên mặt trang theo kiểm lại cổng III.2: ước ~97 âm tiết, vượt giới hạn 90, nên con số giữ ở ghi chú diễn giả.
- **Âm tiết (`deck_lint`, bản III.5):** 88 (bản v1: 80).
- **Sửa III.5:** dòng văn bản: một lượt, bộ nhớ $W+L+1$ ký tự hoặc $M$ mục, và 70, 72, 90 so với 104 bit; "cắt thương về 0" giải nghĩa tại chỗ.

#### `lec11-s06-04` — Bài tập: LZSS kiểu gzip
- **Chức năng:** NT15 bài tập tổng hợp lấy từ `exercises.md`, không trùng recitation (NT-DSFA-10, Q3); NT24 cho cụm LZ77 (lý do đặt ở "Tổng kết": mục 6). Thứ tự trang của mạch theo NT15: bảng tổng kết, "Vấn đề trung tâm", bài tập tổng hợp, "Câu hỏi tự kiểm tra", "Bài tập về nhà", "Tài liệu tham khảo".
- **Mặt trang:** "**Bài tập 11.14.** **Câu hỏi:** LZSS kiểu gzip phát một trong hai dạng mục, với chữ số đầu là bit cờ (flag bit):"
  - "$(0,d,\ell)$, dùng khi $\ell\ge3$: chép $\ell$ ký tự từ khoảng lùi $d$, rồi tiến con trỏ $\ell$ ký tự;"
  - "$(1,c)$ với $c=x_{p+1}$, dùng khi $\ell<3$: ghi một ký tự rời $c$, rồi tiến con trỏ 1 ký tự."
  - "Tại con trỏ $p$, bộ mã hóa tính độ khớp dài nhất $\ell$ và khoảng lùi $d$ như bước 2.1–2.2 của Thuật toán 11.5, với $1\le d\le\min(W,p)$, cận $\ell\le\min(L,n-p)$ thay cho $\min(L,n-p-1)$, và cho phép $\ell>d$."
  - "Chuỗi $x=$ `aacaacabcabaaac`, $n=15$, được mã hóa với $W=6$, $L=4$; ba mục đầu là $(1,\mathrm a)$, $(1,\mathrm a)$, $(1,\mathrm c)$."
  - "(a) Xác định mục thứ tư. (b) Hoàn tất dãy mục tới hết chuỗi và đếm số mục của mỗi dạng."
- **Nguồn:** `exercises.md` (md5 `d51a0647…`) Bài tập 11.14; CMU LZ tc. 7. Giữ mọi dữ liệu, điều kiện, nhiệm vụ và hai câu hỏi; chỉ rút câu dẫn ("Biến thể LZSS dùng trong gzip" thành "LZSS kiểu gzip") và dồn câu "Nó dùng dạng thứ nhất khi $\ell\ge3$ và dạng thứ hai, với $c=x_{p+1}$, khi $\ell<3$" vào điều kiện đứng đầu hai dòng định dạng (D-SB7: dồn dữ kiện vào công thức).
- **Ghi chú diễn giả:** **Gợi ý:** sau ba mục đầu, $p=3$ và lịch sử là $x[1..3]=$ `aac`; thử $d=1,2,3$. Bài này dùng lại cửa sổ, độ khớp và phép chép chồng lấn của LZ77: hai mục dạng thứ nhất thỏa điều kiện khớp nên bộ giải mã chép tuần tự cho đúng đoạn, như trong chứng minh Định lý 11.8. Một cặp vị trí–độ dài của LZSS tốn 17 bit, một ký tự rời 9 bit (Nhận xét 11.10), nên ngưỡng 3 tránh mã cụm ngắn bằng cặp. Nguồn: Blelloch, CMU 15-499, phần nén bằng từ điển, trang chiếu 7.
- **Quyết định:** thêm (CMU LZ tc. 7 chưa có trong deck cũ; outline D10); đổi chỗ lên trước "Câu hỏi tự kiểm tra" theo thứ tự NT15 (cổng III.2).
- **Âm tiết:** ~90. **Ngoại lệ mật độ** (mục 8): trước ~118 (nguyên văn, 113 token chữ đếm trên `exercises.md` cộng nhãn), sau ~90; trần 60, giới hạn 90. Nếu `deck_lint` > 90, báo điều phối viên; không rút thêm chữ của đề.
- **Âm tiết (`deck_lint`, bản III.5):** 90 (bản v1: 111).
- **Sửa III.5:** hai dạng mục thành bảng; dữ kiện viết bằng KaTeX; ghi chú diễn giả sửa lý do ngưỡng 3 (độ khớp tối thiểu của gzip; với 17/9 bit hòa vốn ở 2, Bài tập 11.2(b)).

#### `lec11-s06-05` — Bài tập: LZSS kiểu gzip (lời giải)
- **Chức năng:** NT24 "Lời giải:" trang kế tiếp cùng tiêu đề, mỗi dòng một bước.
- **Mặt trang:** "**Lời giải:**"
  - "(a) Tại $p=3$, cận $\min(4,15-3)=4$: $\ell(1)=0$, $\ell(2)=1$, $\ell(3)=4$ vì $x[4..7]=$ `aaca` khớp $x[1..4]$; độ khớp $4\ge3$, nên mục thứ tư là $(0,3,4)$ và con trỏ lên $p=7$."
  - "(b) Tiếp theo $(1,\mathrm b)$, $(0,3,3)$, $(1,\mathrm a)$, $(1,\mathrm a)$, $(1,\mathrm a)$, $(1,\mathrm c)$; tại $p=12$, độ khớp 2 nhỏ hơn ngưỡng 3, nên bộ mã hóa ghi ký tự rời."
  - "Dãy gồm 10 mục: 2 mục dạng thứ nhất và 8 mục dạng thứ hai; các mục phủ $4+3+8=15=n$ ký tự."
- **Nguồn:** `exercises.md` lời giải 11.14 (đã chạy lại).
- **Ghi chú diễn giả:** bảng các bước: tại $p=7$, $x_8=\mathrm b$ không có trong lịch sử `acaaca`; tại $p=8$, $d=3$ cho `cab` khớp $x[6..8]$, $\ell(6)=2$; tại $p=11$ độ khớp 1 với $d=2$ và $d=5$; tại $p=12$ độ khớp 2 với $d=1$; tại $p=13$ độ khớp 1; tại $p=14$, cận $\min(4,1)=1$. Trên cùng chuỗi, LZ77 tham lam phát 5 bộ ba.
- **Quyết định:** thêm.
- **Âm tiết:** ~62. **Ngoại lệ mật độ:** trần 60, giới hạn 90; lời giải giữ kết quả của `exercises.md`.
- **Âm tiết (`deck_lint`, bản III.5):** 56.

#### `lec11-s06-06` — Câu hỏi tự kiểm tra
- **Chức năng:** NT15 (2–4 câu, lời giải ở ghi chú diễn giả, trả lời được chỉ bằng ghi chú).
- **Mặt trang:** "**Câu hỏi:** trả lời và nêu kết quả đã dùng." `ol`:
  1. Vì sao không bộ nén nào rút ngắn mọi ảnh một điểm 8 bit mà vẫn khôi phục đúng?
  2. Bộ giải mã LZ77 chép $(1,9,\mathrm A)$ sau `A` bằng một lệnh chép khối; sai ở đâu?
  3. Bộ giải mã LZ78 chỉ thêm mục khi $i_t\ge1$; cặp nào của $(0,\mathrm a)$, $(1,\mathrm b)$ hỏng?
  4. Với $q=2$, hệ số nguyên $\lvert F_{77}\rvert$ nhỏ nhất là bao nhiêu để $\hat F_{77}\ne0$?
- **Nguồn:** ghi chú Mệnh đề 11.2 và Bài tập 11.1(e); Bổ đề 11.7 (dòng 376), Bài tập 11.3; Định lý 11.15 (dòng 659); Mệnh đề 11.30(a), Bài tập 11.7(a).
- **Ghi chú diễn giả (lời giải):** (1) có 256 ảnh một điểm nhưng chỉ 255 chuỗi bit ngắn hơn 8 bit, nên hai ảnh chung một dòng bit (Mệnh đề 11.2); (2) lệnh chép khối đọc $y_2,\ldots,y_{10}$ khi bản giải mã mới có $y_1$, trong khi Bổ đề 11.7 cần chép từng ký tự theo thứ tự tăng; (3) cặp $(1,\mathrm b)$, vì mã 1 chưa có ở bộ giải mã, trái giả thiết cùng quy tắc thêm mục của Định lý 11.15; (4) $Q_{77}=31$, cần $\lvert F_{77}\rvert\ge15{,}5$, tức 16.
- **Quyết định:** sửa (`S01` "Chọn và loại phương án"): đổi thành câu hỏi tự kiểm tra theo NT15; phần chọn phương án nằm ở Bài tập 11.11 (bài về nhà); đặt sau bài tập tổng hợp theo thứ tự NT15.
- **Âm tiết:** ~62. Nếu `deck_lint` > 60, rút câu 3 thành "Bộ giải mã LZ78 chỉ thêm mục khi $i_t\ge1$; vì sao cặp $(1,\mathrm b)$ hỏng?"
- **Âm tiết (`deck_lint`, bản III.5):** 60.

#### `lec11-s06-07` — Bài tập về nhà
- **Chức năng:** NT15 bảng `Mục | Bài tập`, mỗi bài xếp vào mạch cung cấp kiến thức cuối cùng; "(trên lớp)" cho bài recitation và bài có trên trang chiếu của phần giảng (11.1, 11.14; NT15); liên kết trình xem (NT-DSFA-10, BT-DSFA-11).
- **Mặt trang:** bảng:
  - 1. Mở đầu | 11.1 (trên lớp)
  - 2. Nén bằng cửa sổ trượt LZ77 | 11.2, 11.3; 11.12, 11.13, 11.14 (trên lớp)
  - 3. Nén bằng từ điển cụm LZ78 | 11.4; 11.15 (trên lớp)
  - 4. Nén LZW với từ điển nạp sẵn | 11.5, 11.6; 11.16 (trên lớp)
  - 5. Nén ảnh JPEG dựa trên biến đổi cosine rời rạc | 11.7, 11.8, 11.9, 11.10; 11.17 (trên lớp)
  - 6. Tổng kết | 11.11
  - Dòng liên kết: "[Ghi chú bài giảng](material-viewer.html?doc=materials/lec-11/lecture-note.md&deck=lecture-11-nen-bang-tu-dien-va-nen-mat-du-lieu.html) · [Bài tập](material-viewer.html?doc=materials/lec-11/exercises.md&deck=lecture-11-nen-bang-tu-dien-va-nen-mat-du-lieu.html)".
- **Nguồn:** ghi chú Bài tập 11.1–11.11; `exercises.md` 11.12–11.17.
- **Ghi chú diễn giả:** 11.1–11.11 ở cuối các mục của ghi chú, 11.12–11.17 ở tệp bài tập; 11.15 có lời giải trong Ví dụ 11.14 nên là bài tự kiểm; 11.17 cần cả Mục 5.
- **Quyết định:** thêm. Bảng gồm cả bài cuối mục 11.1–11.11 của ghi chú theo mục và 11.12–11.17 của `exercises.md` (D-SB9, điều phối viên chấp nhận vì ≤ 80 âm tiết).
- **Âm tiết:** ~50 (một trang).
- **Âm tiết (`deck_lint`, bản III.5):** 54 (bản v1: 52).
- **Sửa III.5:** cột "Mục" theo tên mục của ghi chú; "11.1 (câu (b) trên lớp)".

#### `lec11-s06-08` — Tài liệu tham khảo
- **Chức năng:** NT15 trang cuối của mạch "Tổng kết", nguồn mà ghi chú dẫn. Không có dòng nối sang Bài 12: `sources/source.md` mục "Quan hệ tiên quyết sau điều chỉnh" chỉ có buổi 10 → buổi 11 và buổi 12 → 13 → 14, không có quan hệ buổi 11 → buổi 12, và ghi chú không có cầu nối (outline D13); điều phối viên bác phát hiện của cổng III.2 về dòng nối (D-SB6).
- **Mặt trang:**
  - "Nelson, M. và Gailly, J.-L. (1995). *The Data Compression Book*, ấn bản 2, M&T Books: Chương 7, tr. 170–171; Chương 8, tr. 174–185; Chương 9, tr. 208–226; Chương 11, tr. 245–289 (số trang bản điện tử)."
  - "Blelloch, G. CMU 15-499, *Algorithms in the Real World: Data Compression*: phần nhập môn, trang chiếu 9–10; phần nén bằng từ điển, trang chiếu 3–20; phần nén mất dữ liệu, trang chiếu 9–17."
  - "Cormen, T. H. và cộng sự (2022). *Introduction to Algorithms*, ấn bản 4, MIT Press: Chương 2, 11."
  - "Ziv và Lempel (1977, 1978); Welch (1984), theo Nelson và Gailly."
- **Nguồn:** ghi chú "Hướng dẫn đọc thêm và tài liệu tham khảo" (dòng 1859–1876).
- **Ghi chú diễn giả:** tên chương của Nelson và Gailly: Chương 7 "Dictionary-Based Compression", Chương 8 "Sliding Window Compression", Chương 9 "LZ78 Compression", Chương 11 "Lossy Graphics Compression"; bài báo gốc của Ziv và Lempel (1977, 1978) và Welch (1984) được dẫn theo sách đó. Các phần Burrows–Wheeler, lượng tử hóa véc-tơ, MPEG của bài giảng CMU nằm ngoài bài này.
- **Ghi chú (storyboard):** CMU LZ tc. 1–2, 22–31, L tc. 4–6, 10, 18–20 ngoài phạm vi ghi chú; MIT 15.564 chỉ đối chiếu, không dẫn.
- **Quyết định:** thêm (deck cũ không có trang này).
- **Âm tiết:** ~72 (trần 80 của trang tài liệu tham khảo).
- **Âm tiết (`deck_lint`, bản III.5):** 92 (bản v1: 78).
- **Sửa III.5:** Blelloch (2003), tên trang chiếu "Algorithms and Applications", khoảng trang chiếu đã dẫn (3–21; 3, 7–17); tên bài báo Ziv–Lempel, Welch; số trang Nelson và Gailly chuyển vào ghi chú diễn giả.

### Mạch 7 — Bài tập trên lớp (recitation; `<section>` ngoài riêng sau "Tổng kết", `lec-11-topic-20`)

Năm bài CMU 15-499 của `exercises.md` bản hiện hành (md5 `d51a0647c0527bb16a06f9de53898315`, commit `91b781f`): đề, câu hỏi, gợi ý và lời giải lấy đúng câu chữ của bản này; chỉ rút câu dẫn (NT-DSFA-4, BT-DSFA-6, BT-DSFA-11, D-SB7). Dòng "**Nguồn:**" chỉ trên trang đề, viết "Blelloch, CMU 15-499, phần …, trang chiếu N", không tên tệp (NT-DSFA-8, VP8). Ghi chú diễn giả gồm gợi ý, lời giải, nhầm lẫn dễ gặp, nguồn bài; không hướng dẫn chấm (NT-DSFA-12). Lời giải 11.12 và 11.13 chỉ ở ghi chú diễn giả; cụm LZ77 có lời giải trên mặt trang ở Bài tập 11.14 (`s06-05`). Đề 11.16 và 11.17 dài hơn 120 âm tiết nên mỗi đề tách hai trang cùng tiêu đề, thêm tên phần sau dấu phẩy (NT16); vì vậy mạch có 11 trang (mục 12, điểm cần xác nhận). Thời lượng: 11.12 15 phút, 11.13 8, 11.15 12, 11.16 13, 11.17 12; tổng 60.

#### `lec11-s07-00` — 7. Bài tập trên lớp (trang tiêu đề mạch)
- **Chức năng:** NT12, NT-DSFA-10: `id="mach-7"`, `#/7`, có mục 7 trong "Nội dung".
- **Mặt trang:** "7. Bài tập trên lớp"; dòng dẫn: "Năm bài trên lớp kiểm từng bước của ba bộ nén từ điển và lý do JPEG biến đổi theo khối." (19); từ khóa: "vết LZ77 · bộ ba chồng lấn · vết LZ78 · mã chưa có · mã hóa theo khối".
- **Ghi chú diễn giả:** năm bài theo đúng thứ tự các mạch 2–5: hoàn tất vết LZ77, giải mã một bộ ba chồng lấn, hoàn tất vết LZ78, mã chưa có trong từ điển của bộ giải mã LZW, chọn vùng biến đổi cho ảnh; mỗi bài dùng ký hiệu của ghi chú bài giảng. Nguồn: Blelloch, CMU 15-499, phần nén bằng từ điển, trang chiếu 5, 6, 13, 16; phần nén mất dữ liệu, trang chiếu 11.
- **Quyết định:** sửa (`XT` "Bài tập vận dụng"); `X00` "Bài tập củng cố" (trang giao nhiệm vụ) bỏ: trang tiêu đề mạch thay chức năng; dòng dẫn đổi từ dạng mệnh lệnh sang câu trần thuật đúng cho cả năm bài, gồm bài chứng minh 11.16 và bài giải thích 11.17 (cổng III.2 và kiểm lại).
- **Âm tiết:** ~35.
- **Âm tiết (`deck_lint`, bản III.5):** 21.

#### `lec11-s07-01` — Bài tập: hoàn tất vết LZ77
- **Mặt trang:** "**Bài tập 11.12.** **Câu hỏi:** Chuỗi $x=$ `aacaacabcabaaac`, $n=15$, được mã hóa bằng Thuật toán 11.5 với $W=6$ và $L=4$. Ba bộ ba đầu là $(0,0,\mathrm a)$, $(1,1,\mathrm c)$, $(3,4,\mathrm b)$; sau ba bộ ba này, con trỏ ở $p=8$."
  - "(a) Xác định hai bộ ba còn lại. Với mỗi bộ ba, ghi lịch sử, vùng nhìn trước và độ khớp $\ell(d)$ của từng khoảng lùi $d$."
  - "(b) Giải mã năm bộ ba bằng Thuật toán 11.6 và ghi bản giải mã sau mỗi bộ ba. Chỉ ra các bộ ba có $\ell>d$ và bước chép đọc một ô vừa ghi trong cùng bộ ba."
  - "(c) Tính số bit của dòng năm bộ ba theo Mệnh đề 11.9(d) và so với số bit của $x$ khi ghi 8 bit mỗi ký tự."
  - "**Nguồn:** Blelloch, CMU 15-499, phần nén bằng từ điển, trang chiếu 5."
- **Ghi chú diễn giả:** **Gợi ý:** tại $p=8$, lịch sử gồm sáu ký tự $x[3..8]$; với mỗi $d=1,\ldots,6$, so $x_9,x_{10},\ldots$ lần lượt với $x_{9-d},x_{10-d},\ldots$ tới lần đầu không khớp. **Lời giải:** tại $p=8$, lịch sử `caacab`, vùng nhìn trước `caba`, cận 4, $\ell(d)=0,0,3,0,0,2$; chỉ $d=3$ đạt độ khớp lớn nhất, bộ ba thứ tư $(3,3,\mathrm a)$, con trỏ lên 12. Tại $p=12$, lịch sử `abcaba`, vùng nhìn trước `aac`, cận 2, $\ell(d)=2,0,1,0,0,1$; bộ ba thứ năm $(1,2,\mathrm c)$, con trỏ lên $15=n$. Bản giải mã sau từng bộ ba: `a`, `aac`, `aacaacab`, `aacaacabcaba`, `aacaacabcabaaac`. Hai bộ ba có $\ell>d$: $(3,4,\mathrm b)$, bước $j=4$ đọc $y_4$ ghi ở bước 1; $(1,2,\mathrm c)$, bước $j=2$ đọc $y_{13}$ ghi ở bước 1. Mỗi bộ ba 14 bit, năm bộ ba 70 bit so với 120 bit, tỷ số khoảng $0{,}58$; trung bình 3 ký tự mỗi bộ ba, trên mức hòa vốn $1{,}75$. Nhầm lẫn dễ gặp: quên cận $\min(L,n-p-1)$ chừa ký tự kế ở cuối chuỗi. Nguồn: Blelloch, CMU 15-499, phần nén bằng từ điển, trang chiếu 5.
- **Nguồn (storyboard):** `exercises.md` Bài tập 11.12, đề, gợi ý, lời giải. Câu dẫn rút "cỡ cửa sổ", "độ dài khớp tối đa" (tên của $W$, $L$ đã có ở Định nghĩa 11.4).
- **Quyết định:** sửa (`X01`); lời giải chỉ ở ghi chú diễn giả (D-SB7).
- **Âm tiết:** ~119. **Ngoại lệ mật độ** (mục 8): trước ~127 (nguyên văn), sau ~119; trần 80, giới hạn 120.
- **Âm tiết (`deck_lint`, bản III.5):** 119 (bản v1: 129).
- **Sửa III.5:** dữ kiện viết bằng KaTeX; câu hỏi (a)(b)(c) giữ nguyên.

#### `lec11-s07-02` — Bài tập: bộ ba có độ dài lớn hơn khoảng lùi
- **Mặt trang:** "**Bài tập 11.13.** **Câu hỏi:** Bộ giải mã LZ77 (Thuật toán 11.6) đã dựng bản giải mã $y=$ `abcd`, tức $p=4$, và đọc bộ ba kế tiếp $(d,\ell,c)=(2,9,\mathrm e)$."
  - "(a) Giải mã bộ ba: ghi phép gán ở từng bước chép $j=1,\ldots,9$ và cho bản giải mã sau bộ ba."
  - "(b) Xác định các bước chép đọc một ô nguồn được ghi ngay trong lượt giải mã bộ ba này."
  - "**Nguồn:** Blelloch, CMU 15-499, phần nén bằng từ điển, trang chiếu 6."
- **Ghi chú diễn giả:** **Gợi ý:** viết vị trí nguồn của bước chép thứ $j$ theo $p$, $j$, $d$ (bước 2.1 của Thuật toán 11.6), rồi so với $p$. **Lời giải:** bộ ba hợp lệ vì $\ell=9\ge1$ và $d=2\le p=4$; với $j=1,\ldots,9$ theo thứ tự tăng, gán $y_{4+j}\leftarrow y_{2+j}$, rồi $y_{14}\leftarrow\mathrm e$; bản giải mã `abcdcdcdcdcdce`, 14 ký tự. Vị trí nguồn $2+j$ vượt $p=4$ khi $j\ge3$: bảy bước $j=3,\ldots,9$ đọc ô ghi ở bước $j-2$ của chính lượt này; hai bước đầu đọc $y_3$, $y_4$ có sẵn. Chín ký tự chép `cdcdcdcdc` lặp đoạn `cd` với chu kỳ $d=2$. Nhầm lẫn dễ gặp: đọc số đầu của bộ ba là vị trí đếm từ đầu chuỗi; ở đây nó là khoảng lùi tính từ con trỏ. Nguồn: Blelloch, CMU 15-499, phần nén bằng từ điển, trang chiếu 6.
- **Nguồn (storyboard):** `exercises.md` Bài tập 11.13, nguyên văn.
- **Quyết định:** sửa (`X02`): quy ước khoảng lùi thay vị trí tuyệt đối của deck cũ (outline D2); lời giải chỉ ở ghi chú diễn giả (D-SB7).
- **Âm tiết:** ~73.
- **Âm tiết (`deck_lint`, bản III.5):** 77.

#### `lec11-s07-03` — Bài tập: hoàn tất vết LZ78
- **Mặt trang:** "**Bài tập 11.15.** **Câu hỏi:** Chuỗi $x=$ `aabaacabcabcb`, $n=13$, được mã hóa bằng Thuật toán 11.13. Bốn cặp đầu là $(0,\mathrm a)$, $(1,\mathrm b)$, $(1,\mathrm a)$, $(0,\mathrm c)$; chúng mô tả $x[1..6]=$ `aabaac`."
  - "(a) Lập vết bước 2 của thuật toán từ $x_7$ tới hết chuỗi: với mỗi ký tự đọc, ghi nút hiện tại, kết quả phép tra con ở bước 2.1 và cặp phát ra ở bước 2.2, nếu có."
  - "(b) Liệt kê mọi mục của từ điển sau cặp cuối và vẽ cây từ điển, ghi nhãn cạnh."
  - "(c) Giải mã toàn bộ dãy cặp, gồm bốn cặp đầu và các cặp ở câu (a), bằng Thuật toán 11.14 và kiểm tra kết luận (a) của Định lý 11.15 sau mỗi cặp."
  - "**Nguồn:** Blelloch, CMU 15-499, phần nén bằng từ điển, trang chiếu 13."
- **Ghi chú diễn giả:** **Gợi ý:** cặp thứ $t$ thêm nút $t$ dưới nút $i_t$ qua cạnh $c_t$ (Định nghĩa 11.11); dựng cây sau bốn cặp đầu, rồi từ $x_7$ đi xuống từ gốc. Nhầm lẫn dễ gặp: phát cặp ngay khi cụm hiện tại đã có trong từ điển; quên rằng nút hiện tại trở về gốc sau mỗi cặp. Nguồn: Blelloch, CMU 15-499, phần nén bằng từ điển, trang chiếu 13.
- **Nguồn (storyboard):** `exercises.md` Bài tập 11.15, đề và gợi ý nguyên văn; không có câu dẫn để rút.
- **Quyết định:** sửa (`X03`).
- **Âm tiết:** ~115. **Ngoại lệ mật độ:** trước ~115, sau ~115; trần 80, giới hạn 120.
- **Âm tiết (`deck_lint`, bản III.5):** 119 (bản v1: 125).
- **Sửa III.5:** dữ kiện viết bằng KaTeX; câu hỏi (a)(b)(c) giữ nguyên.

#### `lec11-s07-04` — Bài tập: hoàn tất vết LZ78 (lời giải)
- **Mặt trang:** "**Lời giải:**"
  - "(a) $x_7=\mathrm a$, $x_8=\mathrm b$: đi $0\to1\to2$; $x_9=\mathrm c$: nút 2 không có con qua $\mathrm c$, phát $(2,\mathrm c)$, thêm nút 5 = `abc`."
  - "$x_{10},x_{11},x_{12}$: đi $0\to1\to2\to5$; $x_{13}=\mathrm b$: nút 5 không có con qua $\mathrm b$, phát $(5,\mathrm b)$, thêm nút 6 = `abcb`; chuỗi hết với $i=0$, không có cặp `EOS`."
  - "(b) $D[1..6]$: `a`, `ab`, `aa`, `c`, `abc`, `abcb`; nút 5 là con của 2 qua $\mathrm c$, nút 6 là con của 5 qua $\mathrm b$."
  - "(c) Bộ giải mã xuất `a`, `ab`, `aa`, `c`, `abc`, `abcb`; sau cặp thứ $t$ mỗi phía có $t+1$ mục và mục mới trùng nhau, cuối cùng $y=x$."
- **Ghi chú diễn giả:** cây đủ: gốc có cạnh $\mathrm a$ tới 1 và $\mathrm c$ tới 4; nút 1 có cạnh $\mathrm a$ tới 3, $\mathrm b$ tới 2; nút 2 có cạnh $\mathrm c$ tới 5; nút 5 có cạnh $\mathrm b$ tới 6; các nút 3, 4, 6 là lá. Sáu cụm dài $1+2+2+1+3+4=13$ ký tự. Hai cặp $(2,\mathrm c)$, $(5,\mathrm b)$ trùng phần LZ78 của Ví dụ 11.14.
- **Nguồn (storyboard):** `exercises.md` lời giải 11.15.
- **Quyết định:** thêm.
- **Âm tiết:** ~70. **Ngoại lệ mật độ:** trần 60, giới hạn 90; lời giải giữ kết quả của `exercises.md`.
- **Âm tiết (`deck_lint`, bản III.5):** 82 (bản v1: 80).
- **Sửa III.5:** "thêm nút 5, cụm `abc`" thay dấu "=".

#### `lec11-s07-05` — Bài tập: mã chưa có trong từ điển của bộ giải mã LZW, dữ kiện
- **Chức năng:** đề Bài tập 11.16 nguyên văn, tách hai trang cùng tiêu đề (NT16) vì cả đề khoảng 145 âm tiết, quá giới hạn 120.
- **Mặt trang:** "**Bài tập 11.16.** **Câu hỏi:** Dòng mã $k_1,\ldots,k_\tau$ của một chuỗi được tạo bằng Thuật toán 11.19 và giải bằng Thuật toán 11.20; từ điển của hai phía không giới hạn số mục."
  - "Đầu vào chứa liền nhau đoạn $\chi\,S\,\chi\,S\,\chi$, với $\chi$ là một ký tự, $S$ là một chuỗi và cụm $\chi\,S$ đã có mã trong từ điển."
  - "Bộ mã hóa phát mã $k_t$ của cụm $\chi\,S$ và thêm mục $\chi\,S\,\chi$; ngay sau đó nó phát $k_{t+1}$, mã của chính mục vừa thêm."
- **Ghi chú diễn giả:** đoạn $\chi S\chi S\chi$ là dạng duy nhất làm bộ mã hóa phát ngay mã vừa thêm (Mệnh đề 11.22). Ví dụ quen thuộc: `ababa` trong `abababa` với $\chi=\mathrm a$, $S=$ `b` (Ví dụ 11.8(b)).
- **Nguồn (storyboard):** `exercises.md` Bài tập 11.16, đoạn dữ kiện nguyên văn.
- **Quyết định:** sửa (`X04`), tách.
- **Âm tiết:** ~69.
- **Âm tiết (`deck_lint`, bản III.5):** 75.

#### `lec11-s07-06` — Bài tập: mã chưa có trong từ điển của bộ giải mã LZW, câu hỏi
- **Mặt trang:**
  - "Bộ giải mã đọc $k_t$ và xuất $\chi\,S$, rồi đọc $k_{t+1}$ và không thấy mã này trong từ điển của mình."
  - "(a) Xác định $k_{t+1}$ theo $t$ và $\texttt{next\_code}$ của bộ giải mã lúc đọc $k_{t+1}$, rồi giải thích vì sao bộ giải mã chưa có mục $k_{t+1}$."
  - "(b) Xác định cụm mà bộ giải mã gán cho $k_{t+1}$ và mục nó thêm, chỉ từ cụm $\chi\,S$ vừa xuất, rồi kiểm kết quả bằng Mệnh đề 11.22(b)."
  - "**Nguồn:** Blelloch, CMU 15-499, phần nén bằng từ điển, trang chiếu 16."
- **Ghi chú diễn giả:** **Gợi ý:** so mã của mục mà bộ mã hóa thêm khi phát $k_t$ (Bổ đề 11.21(a)) với $\texttt{next\_code}$ của bộ giải mã khi đọc $k_{t+1}$ (Bổ đề 11.21(c)). Nhầm lẫn dễ gặp: coi mã chưa có trong từ điển là dấu hiệu dòng mã hỏng. Nguồn: Blelloch, CMU 15-499, phần nén bằng từ điển, trang chiếu 16.
- **Nguồn (storyboard):** `exercises.md` Bài tập 11.16, câu cuối của đoạn dữ kiện và hai câu hỏi nguyên văn; gợi ý nguyên văn.
- **Quyết định:** sửa (`X04`), tách.
- **Âm tiết:** ~73.
- **Âm tiết (`deck_lint`, bản III.5):** 79.

#### `lec11-s07-07` — Bài tập: mã chưa có trong từ điển của bộ giải mã LZW (lời giải)
- **Mặt trang:** "**Lời giải:**"
  - "(a) Theo Bổ đề 11.21(a), khi phát $k_t$ bộ mã hóa thêm mục $255+t$, nên $k_{t+1}=255+t$. Theo Bổ đề 11.21(c), bộ giải mã đã thêm các mục $256,\ldots,254+t$, nên $\texttt{next\_code}=255+t=k_{t+1}$."
  - "Bộ giải mã chỉ thêm mục $255+t$ sau khi biết ký tự đầu của cụm kế tiếp, mà cụm đó là cụm của chính $k_{t+1}$."
  - "(b) Cụm kế tiếp bắt đầu bằng $\chi\,S$, nên ký tự đầu là $\chi$; bộ giải mã gán $e=\chi\,S\,\chi=w\operatorname{first}(w)$ với $w=\chi\,S$ (nhánh 3.2) và thêm $\chi\,S\,\chi$ ở mã $255+t$, trùng bộ mã hóa."
  - "Mệnh đề 11.22(b) với $w_t=\chi\,S$ cho $w_{t+1}=w_t\operatorname{first}(w_t)=\chi\,S\,\chi$."
- **Ghi chú diễn giả:** kiểm bằng dòng mã $97,98,256,258$ của Ví dụ 11.8(b): $t=3$, $\chi=\mathrm a$, $S=$ `b`, $k_4=258=255+3$, bộ giải mã có $\texttt{next\_code}=258$ và gán cho 258 cụm `aba`. Với $S$ rỗng, đoạn là `aaa`, như hai cụm đầu `a`, `aa` của chuỗi toàn chữ $\mathrm a$ ở Bài tập 11.6, nơi $k_2=256=255+1$.
- **Nguồn (storyboard):** `exercises.md` lời giải 11.16 (bài áp dụng Mệnh đề 11.22(b), không chứng minh lại mệnh đề).
- **Quyết định:** thêm.
- **Âm tiết:** ~78. **Ngoại lệ mật độ:** trần 60, giới hạn 90; lời giải giữ hai bước của `exercises.md`.
- **Âm tiết (`deck_lint`, bản III.5):** 82.

#### `lec11-s07-08` — Bài tập: biến đổi trên toàn ảnh và mã hóa theo khối, ba mục tiêu
- **Chức năng:** đề Bài tập 11.17 nguyên văn, tách hai trang cùng tiêu đề (NT16) vì cả đề khoảng 160 âm tiết.
- **Mặt trang:** "**Bài tập 11.17.** **Câu hỏi:** Một phép biến đổi tuyến tính dùng để nén ảnh được chọn theo ba mục tiêu:" `ol`:
  1. khử tương quan (decorrelate): các điểm ảnh gần nhau có giá trị tương quan, tức giúp đoán nhau, còn các hệ số sau biến đổi không còn tương quan với nhau;
  2. làm cho nhiều hệ số có giá trị nhỏ;
  3. có những hàm cơ sở (basis function) mà mắt bỏ qua được; với DCT của Định nghĩa 11.26, hàm cơ sở là các mẫu cosine dựng từ các hàng của ma trận $T$, và mỗi hệ số là trọng số của một mẫu.
- **Ghi chú diễn giả:** ba mục tiêu là ba tiêu chí đánh giá một phép biến đổi; câu hỏi ở trang sau còn đòi xét chi phí tính toán. Nhầm lẫn dễ gặp: chỉ trả lời bằng chi phí mà bỏ ba mục tiêu, hoặc ngược lại.
- **Nguồn (storyboard):** `exercises.md` Bài tập 11.17, câu dẫn và ba mục tiêu nguyên văn.
- **Quyết định:** sửa (`X05`), tách.
- **Âm tiết:** ~92. **Ngoại lệ mật độ:** trước ~92, sau ~92 (ba mục tiêu là dữ kiện, nghĩa tại chỗ của "khử tương quan", "hàm cơ sở" phải giữ); trần 80, giới hạn 120.
- **Âm tiết (`deck_lint`, bản III.5):** 103.

#### `lec11-s07-09` — Bài tập: biến đổi trên toàn ảnh và mã hóa theo khối, câu hỏi
- **Mặt trang:**
  - "Dựa trên ba mục tiêu trên và chi phí tính toán, trả lời hai câu sau và dẫn số hiệu các kết quả của ghi chú được dùng."
  - "(a) Giải thích vì sao áp dụng biến đổi cosine một lần trên toàn bộ ảnh là cách làm kém."
  - "(b) Nêu cách khắc phục."
  - "**Nguồn:** Blelloch, CMU 15-499, phần nén mất dữ liệu, trang chiếu 11."
- **Ghi chú diễn giả:** **Gợi ý:** mỗi hệ số của phép biến đổi là một tổng trên mọi điểm của vùng biến đổi; so số số hạng khi vùng là cả ảnh $m$ điểm và khi vùng là một khối $8\times8$. Nguồn: Blelloch, CMU 15-499, phần nén mất dữ liệu, trang chiếu 11.
- **Nguồn (storyboard):** `exercises.md` Bài tập 11.17, câu yêu cầu, hai câu hỏi và gợi ý nguyên văn. Trang chiếu CMU hỏi "Cosine or Fourier"; `exercises.md` viết "biến đổi cosine" (đã ghi ở giai đoạn II.1).
- **Quyết định:** sửa (`X05`), tách.
- **Âm tiết:** ~58.
- **Âm tiết (`deck_lint`, bản III.5):** 65.

#### `lec11-s07-10` — Bài tập: biến đổi trên toàn ảnh và mã hóa theo khối (lời giải)
- **Mặt trang:** "**Lời giải:**"
  - "(a) Các điểm cách nhau mười lăm, hai mươi vị trí hầu như không giúp đoán nhau, nên vùng lớn hơn khối $8\times8$ không khử thêm được tương quan đáng kể và ít lợi thêm cho mục tiêu 2; bước lượng tử tăng theo tần số đã khai thác mục tiêu 3 ngay trong từng khối, nên biến đổi cả ảnh không thêm lợi ích cho mục tiêu này."
  - "Trên cả ảnh $m$ điểm có $m$ hệ số, mỗi hệ số $m$ số hạng: $m^2\approx4{,}1\cdot10^9$ với CHEETAH.GS, so với $64m\approx4{,}1\cdot10^6$ khi chia khối; phải giữ cả ảnh trong bộ nhớ."
  - "(b) Biến đổi cosine từng khối $8\times8$ (mã hóa theo khối): hệ số DC chiếm khoảng $80\%$ năng lượng (Ví dụ 11.10), bước $Q_{uv}$ tăng theo tần số (Định nghĩa 11.29)."
  - "Chi phí $\Theta(m)$, bộ nhớ một dải $8\times m_{\mathrm w}$ điểm (Thuật toán 11.34); đổi lại, ảnh lộ hiện tượng khối khi $q>5$ (Nhận xét 11.35)."
- **Ghi chú diễn giả:** lời giải theo từng mục tiêu: mục tiêu 1, hai điểm cùng khối cách nhau không quá 7 vị trí; mục tiêu 2, 28 hệ số có $u+v\ge8$ chỉ chiếm khoảng $4{,}4\%$ năng lượng, và DCT bảo toàn năng lượng (Mệnh đề 11.28(c)); mục tiêu 3, với $q=2$ khối ở Ví dụ 11.11 còn 30 hệ số khác 0 trong 64, sai số mỗi khối bị chặn bởi $\beta(q)$ (Định lý 11.31). Kiểm: $m^2/(64m)=m/64=1\,000$, đúng bằng số khối $40\cdot25$ của CHEETAH.GS; bộ nhớ $8\cdot320=2\,560$ điểm. Nguồn: Nelson và Gailly, tr. 255; Blelloch, CMU 15-499, phần nén mất dữ liệu, trang chiếu 11.
- **Nguồn (storyboard):** `exercises.md` lời giải 11.17; câu tương quan theo bản hiện hành ("không khử thêm được tương quan đáng kể", "ít lợi thêm"), không khẳng định mạnh hơn.
- **Quyết định:** thêm.
- **Âm tiết:** ~88. **Ngoại lệ mật độ:** trần 60, giới hạn 90; lời giải giữ ba mục tiêu và chi phí của `exercises.md`. Vế mục tiêu 3 viết theo lý do của `exercises.md` (bước lượng tử theo tần số khai thác mục tiêu 3 trong từng khối); để giữ ≤ 90, nếu `deck_lint` > 90 thì chuyển vế "bộ nhớ một dải $8\times m_{\mathrm w}$ điểm" của dòng cuối vào ghi chú diễn giả (con số đó đã có ở `s05-10`) (kiểm lại cổng III.2).
- **Âm tiết (`deck_lint`, bản III.5):** 90 (bản v1: 88).
- **Sửa III.5:** câu (a) theo Nelson và Gailly tr. 255 (khối lớn có thể nén tốt hơn nhưng lợi giảm nhanh; $64\times64$ có thể không hơn bốn khối $16\times16$; JPEG chọn $8\times8$ vì cài đặt được); thêm block coding, blocking artifacts. Lệch câu chữ `exercises.md` theo quyết định III.5, mục 4; đề xuất sửa `exercises.md` do điều phối viên ghi.

## 4. Hành trình khái niệm, kỹ thuật, ví dụ xuyên suốt

### 4.1 Hành trình (NT8, NT-DSFA-1)

| Khái niệm hoặc kết quả | Vấn đề | Trực quan | Ví dụ | Phát biểu | Ý tưởng chứng minh | Ứng dụng, chi phí | Kiểm tra |
|---|---|---|---|---|---|---|---|
| Hai đặc tả (Định nghĩa 11.1, Mệnh đề 11.2) | `s01-06`, `s01-07` | `s01-07`, hình `s01-08` | `s01-07` (Ví dụ 11.1) | `s01-07`, `s01-08` | `s01-08` (một dòng; Mệnh đề 11.2 là kết quả phụ) | `s06-03` (danh mục ảnh) | `s01-09`, `s01-10` (Bài tập 11.1(b)); `s06-06` câu 1 |
| LZ77 (Định nghĩa 11.4, Thuật toán 11.5, 11.6, Định lý 11.8) | `s01-10` câu kết, `s02-01` | `s02-01` | `s02-02`, `s02-05` | `s02-03`–`s02-06` | `s02-07` | `s02-08`; `s06-02`, `s06-03` | `s06-04`, `s06-05` (Bài tập 11.14); `s07-01`, `s07-02`; `s06-06` câu 2 |
| LZ78 (Định nghĩa 11.11, Thuật toán 11.13, 11.14, Định lý 11.15) | `s02-08` câu kết, `s03-01` | `s03-01`, cây `s03-02` | `s03-01`, `s03-04` | `s03-02`–`s03-05` | `s03-06` | `s03-07` (từ điển đầy, `compress`, BTLZ) | `s07-03`, `s07-04`; `s06-06` câu 3 |
| LZW (Thuật toán 11.19, 11.20, Định lý 11.23) | `s03-07` câu kết, `s04-01` | `s04-01`, hình `s04-03` | `s04-01`, `s04-03` | `s04-02`, `s04-04`, `s04-05` | `s04-06` | `s04-07` | `s07-05`–`s07-07` |
| DCT (Định nghĩa 11.26, Mệnh đề 11.28) | `s05-01` | `s05-02` | `s05-02`, `s05-03` (Ví dụ 11.10) | `s05-03`; Mệnh đề 11.28 ở bước 1–2 của `s05-06` | `s05-06` (ghi chú diễn giả: Bổ đề 11.27) | `s05-10` | `s07-08`–`s07-10` |
| Lượng tử hóa, cận sai số (Định nghĩa 11.29, Mệnh đề 11.30, Định lý 11.31) | `s05-01` câu hỏi | `s05-04` | `s05-04` (Ví dụ 11.11), `s05-05` (Ví dụ 11.12) | `s05-04`, `s05-05`; Mệnh đề 11.30 ở bước 3 của `s05-06` | `s05-06` | `s05-10` ("Bảo đảm:"), `s06-03` ($q=2$, $9{,}60$) | `s06-06` câu 4; `s07-10` |
| Mã hệ số (Định nghĩa 11.32, Mệnh đề 11.33) | `s05-07` (dãy nhiều số 0) | chạy tay `s05-07` | `s05-08` | `s05-07`, `s05-08` | `s05-08` (một dòng) | `s05-10` | bài về nhà 11.10 |
| Đường ống (Thuật toán 11.34) | `s05-01` | hình `s05-01` | `s05-02`–`s05-08` | `s05-09` | `s05-05`, `s05-06`; "Bảo đảm:" `s05-10` | `s05-10` | `s07-08`–`s07-10` |

Chu trình rút gọn có lý do: mã hệ số không có trang trực quan riêng vì chạy tay ở `s05-07` làm vai trò đó và ghi chú xếp chủ đề này là "chu trình gộp" (outline mục 10). Kết quả phụ (phát biểu kèm một dòng "Chứng minh." hoặc phát biểu tại bước dùng của ý tưởng chứng minh, NT6): Mệnh đề 11.2, 11.28, 11.30, 11.33, Bổ đề 11.7, 11.12, 11.21, Mệnh đề 11.22. Kết quả chính có trang "Ý tưởng chứng minh" riêng: Định lý 11.8, 11.15, 11.23, 11.31.

### 4.2 Kỹ thuật (NT7)

| Kỹ thuật | Lần đầu trong học phần | Trang của Bài 11 |
|---|---|---|
| Bất biến vòng lặp (khởi tạo–duy trì–kết thúc) | Bài 05 (Mệnh đề 05.19) | "Nhắc lại:" một dòng ở `s02-07`; dùng lại ở `s03-03` ("Bất biến:"), `s04-06` |
| Đếm số chuỗi ngắn hơn (đơn ánh không tồn tại) | Bài 10 (Mệnh đề 10.2) | "Nhắc lại:" ở `s01-02`; dùng ở `s01-08` |
| Biến đổi trực chuẩn giữ tổng bình phương | lần đầu ở Bài 11 | dòng "Kỹ thuật." ở bước 2 của `s05-06` |
| Tổng xếp lồng (Bổ đề 11.27, Mệnh đề 11.33) | — | ghi chú diễn giả `s05-06`, dòng "Chứng minh." `s05-08` |

### 4.3 Ví dụ xuyên suốt (VP-DSFA-6, NT23)

| Tên gọi | Dữ liệu | Trang dùng (mỗi lần một câu hỏi mới) |
|---|---|---|
| chuỗi `aacaacabcabaaac` | 15 ký tự, $W=6$, $L=4$ (CMU LZ tc. 5) | `s01-10` (lặp `aac`, mã từng ký hiệu trả đủ bit); `s02-02` (ba bộ ba đầu); `s02-05` (giải mã chồng lấn); `s02-07` (phản ví dụ chép khối); `s06-04` (LZSS trên cùng chuỗi); `s07-01` (hoàn tất vết) |
| chuỗi `aabaacabcabcb` | 13 ký tự, mã byte 97–99 (CMU LZ tc. 13, 17) | `s03-01` (LZ78), `s03-04` (giải mã), `s03-07` (6 trong 13 ký tự thô), `s04-01` (LZW), `s04-07` (90 bit), `s06-03` (cấu trúc cho từng loại lặp; 70, 72, 90 so với 104 bit ở ghi chú diễn giả), `s07-03` |
| ảnh CHEETAH.GS, khối Hình 11.9 của NG | $320\times200$, $64\,000$ byte; khối $8\times8$ (NG tr. 258, 287) | `s01-07` (ba hệ số chất lượng); `s01-09` (chọn $q$ theo ngưỡng, cùng CLOWN.GS); `s05-01` (bài toán); `s05-02` (DC); `s05-03` (năng lượng); `s05-04` (lượng tử hóa); `s05-05` (4,18 so với cận 9,10); `s05-08` (zigzag); `s05-10` (1 000 khối); `s06-03` (18,4 MB, cận 9,60); `s07-10` |

Tình huống mở bài (kho văn bản; danh mục $1\,000$ ảnh, 64 MB) được thu hồi bằng con số ở `s06-03` (NT-DSFA-5).

## 5. Ánh xạ deck nguồn CMU 15-499 (P1, NT1)

Thứ tự CMU (LZ77 → LZ78 → LZW → nén mất dữ liệu) được giữ. Mọi chỗ gộp, tách, thêm, bỏ:

| Trang chiếu CMU | Nội dung | Trang mới | Quyết định, lý do |
|---|---|---|---|
| LZ tc. 1–2 | bìa, dàn bài học phần | — | bỏ: khung của học phần CMU |
| LZ tc. 3 | họ LZ77, LZ78, biến thể, ứng dụng | `s02-01` (ghi chú diễn giả), `s06-02` | giữ ý, chuyển vào ghi chú diễn giả |
| LZ tc. 4 | cửa sổ trượt, $(p,l,c)$ | `s02-01`, `s02-03`, `s02-04` | sửa: "position relative to the cursor" thành khoảng lùi $d$ theo ghi chú |
| LZ tc. 5 | vết LZ77 | `s02-02` (ba hàng đầu), `s07-01` (hai hàng "?") | tách: phần chạy tay ở giảng, phần hoàn tất ở recitation |
| LZ tc. 6 | giải mã, $\ell>p$, `abcd`, $(2,9,\mathrm e)$ | `s02-05` (ý), `s07-02` (bài) | tách như trên |
| LZ tc. 7 | LZSS của gzip, vết có "?" | `s06-04`, `s06-05` | thêm vào "Tổng kết" làm bài tổng hợp (outline D10) |
| LZ tc. 8–9 | tối ưu của gzip, bảng băm | `s02-08` (ghi chú diễn giả) | gộp vào chi phí; chi tiết cài đặt ở ghi chú (Nhận xét 11.10) |
| LZ tc. 10 | Wyner–Ziv | `s02-08` (ghi chú diễn giả) | ngoài phạm vi chứng minh của học phần |
| LZ tc. 11–12 | từ điển LZ78, trie, mã hóa | `s03-01`, `s03-02`, `s03-03` | giữ |
| LZ tc. 13–14 | vết mã hóa, giải mã LZ78 | `s03-01`, `s03-04` (bốn hàng đầu), `s07-03`, `s07-04` | tách như LZ tc. 5 |
| LZ tc. 15 | LZW | `s04-01`, `s04-02` | giữ |
| LZ tc. 16 | bộ giải mã chậm một bước, `…SSc…` | `s04-03`, `s04-06`, `s07-05`–`s07-07` | tách: ví dụ cụ thể ở giảng, bài trừu tượng ở recitation |
| LZ tc. 17, 19 | vết mã hóa, giải mã LZW | `s04-01`, `s04-03` | sửa: mã byte 97–99 thay 112–114 (outline D3) |
| LZ tc. 18 | từ điển quá lớn | `s03-07` | giữ (một dòng) |
| LZ tc. 20–21 | tóm tắt các biến thể LZ | `s06-02` (ghi chú diễn giả) | gộp vào tổng kết |
| LZ tc. 22–31 | dàn bài (tc. 22), Burrows–Wheeler, ACB (tc. 23–31) | — | bỏ: ngoài phạm vi ghi chú |
| L tc. 1–2 | bìa, dàn bài | — | bỏ |
| L tc. 3 | lượng tử hóa vô hướng | `s05-04` (ghi chú diễn giả) | đổi thứ tự: đặt sau DCT theo thứ tự ghi chú (NT2) |
| L tc. 4–6 | lượng tử hóa véc-tơ | — | bỏ: ngoài phạm vi ghi chú (Q9) |
| L tc. 7–8 | mã hóa biến đổi tuyến tính | `s05-01`, `s05-03` (ghi chú diễn giả) | gộp |
| L tc. 9 | biến đổi cosine, ví dụ | `s05-02`, `s05-03` | giữ ý, thay bằng khối có số của NG |
| L tc. 10 | đa thức, Haar | — | bỏ: ngoài phạm vi ghi chú |
| L tc. 11 | chọn biến đổi, câu hỏi toàn ảnh | `s07-08`–`s07-10` | recitation (Bài tập 11.17); phần giảng không trả lời trước |
| L tc. 12 | trực chuẩn, bảo toàn năng lượng | `s05-03`, `s05-06` | giữ; bỏ hệ số $G_{TC}$ (ghi chú không dùng) |
| L tc. 13–14 | JPEG, sơ đồ | `s05-01`, `s05-09` | giữ |
| L tc. 15 | bảng lượng tử chuẩn | `s05-04` (ghi chú diễn giả) | ghi chú dùng ma trận của NG |
| L tc. 16 | thứ tự quét, mã độ dài loạt | `s05-07`, `s05-08` | giữ |
| L tc. 17 | ví dụ $0{,}125$ bit mỗi điểm | `s05-10` (ghi chú diễn giả) | gộp |
| L tc. 18 trở đi | MPEG | — | bỏ: ngoài phạm vi (Q9) |

## 6. Bài tập trên mặt trang (NT24, BT-DSFA-11)

| Cụm khái niệm | Bài có "Lời giải:" trên trang kế tiếp | Nguồn | Loại |
|---|---|---|---|
| Hai đặc tả | Bài tập 11.1(b) (`s01-09`, `s01-10`) | ghi chú, bài cuối mục 1.1 (dữ liệu NG Hình 11.14) | trong mạch 1 (D-SB1) |
| LZ77 | Bài tập 11.14 (`s06-04`, `s06-05`) | CMU LZ tc. 7 | bài tổng hợp của "Tổng kết" |
| LZ78 | Bài tập 11.15 (`s07-03`, `s07-04`) | CMU LZ tc. 13 | recitation |
| LZW | Bài tập 11.16 (`s07-05`, `s07-06`, `s07-07`) | CMU LZ tc. 16 | recitation |
| JPEG | Bài tập 11.17 (`s07-08`–`s07-10`) | CMU L tc. 11 | recitation |

Bài tập 11.12, 11.13 có đề trên mặt trang (`s07-01`, `s07-02`), lời giải trong ghi chú diễn giả (D-SB7). Bài có lời giải trên mặt trang của cụm LZ77 đứng ở "Tổng kết" chứ không ở mạch 2: NT-DSFA-10 đòi bài tổng hợp của "Tổng kết" lấy từ `exercises.md` và không trùng recitation, và 11.14 là bài duy nhất thỏa điều đó; phần giảng đã ở trần 55 trang. Ghi chú diễn giả của `s06-04` nối bài với Định lý 11.8. Không trang nào tự dựng đề (BT-DSFA-1).

## 7. Đề xuất sửa ghi chú/bài tập (NT3)

Không phát hiện lỗi về số liệu, phát biểu hay ký hiệu của ghi chú hoặc `exercises.md` (đã chạy lại mọi vết và hằng số ở đầu tệp). Một đề xuất mức `nhẹ`, chờ tác giả; điều phối viên ghi nhận 2026-11-19, không sửa trong giai đoạn deck. Đề xuất cũ về câu dẫn của Bài tập 11.16 đã bỏ: bản `exercises.md` hiện hành (md5 `d51a0647…`) không còn câu dẫn đó (cổng III.2).

| Mức độ | Vị trí | Vấn đề | Bằng chứng | Đề xuất sửa |
|---|---|---|---|---|
| nhẹ | ghi chú, "Hướng dẫn đọc thêm", dòng 1871 | Ghi chú dẫn CMU-L "trang chiếu 9–17"; deck (P1) còn ánh xạ L tc. 3 (lượng tử hóa vô hướng) và tc. 7–8 (mã hóa biến đổi tuyến tính) trong ghi chú diễn giả | mục 5 của tệp này | Nếu muốn trang "Tài liệu tham khảo" của deck khớp từng trang chiếu đã dùng, sửa thành "trang chiếu 3, 7–17"; nếu không, deck giữ "9–17" như ghi chú |

## 8. Mật độ (NT17, NT18, NT-DSFA-7) và danh sách ngoại lệ

Trần: 60 âm tiết cho trang nội dung; 80 cho "Mục tiêu học tập", "Nội dung", bảng tổng kết, bảng chi phí, "Tài liệu tham khảo", trang đề recitation; ngoại lệ không vượt 1,5 lần trần. ≤ 6 dòng (bảng vết, bảng chi phí tới 8 hàng); ≤ 20 âm tiết mỗi dòng; ≤ 3 công thức hiển thị; giả mã dài hơn 8 dòng đứng một mình với một câu dẫn. Không thu nhỏ chữ, không `.dense`. Số âm tiết dưới đây lấy từ `deck_lint` (NT17); ước lượng của lần lập storyboard còn ghi ở từng trang (mục 3).

**Danh sách ngoại lệ cuối** (số của `deck_lint --course ds-foundation-algorithms`, bản sau biên tập III.5; cột "v1" là bản đóng băng v1 md5 `9511e68e…`; số dòng theo `deck_lint`, bảng tính một dòng):

| Trang | v1 | Sau III.5 | Trần / giới hạn 1,5× | Lý do |
|---|---:|---:|---|---|
| `lec11-s01-01` | 88 | 76 | — | bìa: `deck_lint` chỉ miễn đếm bìa có mã `LNN-1-01`; mã `lec11-s01-01` theo P7 (mục 10). Luận đề một câu đã rút (cổng III.4) |
| `lec11-s01-03` | 113 | 113 | 80 / 120 | sáu mục tiêu giữ đúng nghĩa và đủ động từ của ghi chú (NT11, NT17), tách hai trang |
| `lec11-s01-04` | 90 | 90 | 80 / 120 | như `s01-03` |
| `lec11-s01-07` | 85; 8 dòng | 84; 8 dòng | 60 / 90; 6 dòng | câu nêu vấn đề (NT13), ví dụ có bảng số và Định nghĩa 11.1 cùng trang (NT8) để giữ 55 trang; tên tiếng Anh (NT21) |
| `lec11-s02-05` | 39; 5 dòng | 35; 7 dòng | 6 dòng | giả mã đánh số 2.1–2.2 theo ghi chú để đề 11.13 dẫn đúng bước (cổng III.4, TT) |
| `lec11-s02-07` | 60 | 72 | 60 / 90 | bước duy trì nêu giả thiết quy nạp và điều kiện khớp trên mặt trang (cổng III.4, TT) |
| `lec11-s03-02` | 67 | 78 | 60 / 90 | tên tiếng Anh của cây từ điển; giải nghĩa `EOS` bằng câu đủ; giả thiết của Bổ đề 11.12 (cổng III.4) |
| `lec11-s03-03` | 54; 5 dòng | 58; 7 dòng | 6 dòng | giả mã đánh số 2.1, 2.2 để đề 11.15 dẫn đúng bước; giả mã dưới 8 dòng (NT-DSFA-7) |
| `lec11-s03-04` | 50; 5 dòng | 54; 8 dòng | 6 dòng | giả mã đánh số 2.1–2.3 theo ghi chú |
| `lec11-s04-01` | 73 | 78 | 60 / 90 | câu hỏi của mạch, từ điển nạp sẵn (mã bằng giá trị byte), trực quan và bảng vết cùng trang (gộp `W00` + `W02`, giữ 55 trang) |
| `lec11-s04-02` | 48; 5 dòng | 53; 7 dòng | 6 dòng | giả mã đánh số 2.1, 2.2 theo ghi chú |
| `lec11-s04-04` | 45; 9 dòng | 58; 9 dòng | 6 dòng | giả mã 10 dòng đứng một mình với một câu dẫn (NT-DSFA-7) |
| `lec11-s04-06` | 67 | 81 | 60 / 90 | Bổ đề 11.21 (a)(b)(c) và Mệnh đề 11.22 (a)(b) phát biểu tại bước dùng, để đề và lời giải 11.16 dẫn đúng phần (cổng III.4, SV, TT) |
| `lec11-s05-07` | 66 | 87 | 60 / 90 | câu nối từ cận sai số sang mã hệ số ("Khối $\hat F$ vẫn gồm 64 số nguyên, trong đó 34 số 0") và "Trực quan." trên mặt trang (cổng III.4, SP, mạch; quyết định III.5 mục 12); thêm $\hat F_{00}^{(0)}=0$ |
| `lec11-s05-08` | 60 | 86 | 60 / 90 | ba bước chính, "Diễn giải:" và Mệnh đề 11.33 cùng trang; không tách trang để giữ trần 55 trang giảng (quyết định III.5 mục 12) |
| `lec11-s05-09` | 66; 13 dòng | 73; 13 dòng | 60 / 90 | giả mã hai cột đứng một mình (NT-DSFA-7) với câu dẫn "Chỉ bước lượng tử hóa phụ thuộc $q$." |
| `lec11-s06-01` | 81 | 91 | 80 / 120 | bảng tổng kết thêm giả thiết từ điển đầy cho Định lý 11.15, 11.23 (cổng III.4, CG) |
| `lec11-s06-02` | 81 | 93 | 80 / 120 | bảng thuật toán: bảo đảm của LZ78 và LZW ghi đủ điều kiện từ điển đầy (cổng III.4, CG; kiểm lại SP K7) |
| `lec11-s06-03` | 80 | 88 | 60 / 90 | trả lời câu hỏi trung tâm có điều kiện: một lượt, bộ nhớ của văn bản, số bit 70/72/90 (LZ77, LZ78, LZW) so với 104, cận $9{,}60$, 18,4 MB kèm giả thiết (NT-DSFA-5, NT2); bộ nhớ nén ảnh ở ghi chú diễn giả vì vượt 90 |
| `lec11-s06-04` | 111 | 90 | 80 / 120 | đề Bài tập 11.14 chép từ CMU 15-499 (trang chiếu 7), nhóm đề chép bài nguồn của NT-DSFA-7 (quyết định III.5 mục 1); câu điều kiện giữ đúng câu chữ `exercises.md` (BT11, BT-DSFA-11); hai dạng mục thành bảng, dữ kiện chuỗi bằng KaTeX |
| `lec11-s06-08` | 78 | 92 | 80 / 120 | đủ năm, khoảng trang chiếu đã dẫn và tên ba bài báo gốc (quyết định III.5 mục 13); tên trang chiếu "Algorithms and Applications" ở ghi chú diễn giả |
| `lec11-s07-01` | 129 | 119 | 80 / 120 | đề recitation: dữ kiện viết bằng KaTeX, ba câu hỏi giữ nguyên câu chữ; không tách trang |
| `lec11-s07-02` | 77 | 77 | 80 | dưới trần 80 của đề recitation |
| `lec11-s07-03` | 125 | 119 | 80 / 120 | như `s07-01` |
| `lec11-s07-04` | 80 | 82 | 60 / 90 | lời giải mỗi dòng một bước |
| `lec11-s07-07` | 82 | 82 | 60 / 90 | lời giải hai bước của `exercises.md` |
| `lec11-s07-08` | 103 | 103 | 80 / 120 | ba mục tiêu là dữ kiện của đề; nghĩa tại chỗ của "khử tương quan", "hàm cơ sở" giữ nguyên |
| `lec11-s07-10` | 88 | 90 | 60 / 90 | lời giải theo Nelson và Gailly tr. 255 ("có thể không tốt hơn nhiều"; quyết định III.5 mục 4) và chi phí; chi tiết ba mục tiêu ở ghi chú diễn giả |

Dưới trần, không cần ngoại lệ (số `deck_lint` sau III.5): `s01-02` 60, `s01-09` 59, `s01-10` 59, `s02-01` 59, `s02-02` 60, `s02-03` 60, `s02-04` 58 (6 dòng), `s02-06` 58, `s03-01` 59, `s03-05` 59, `s03-06` 59, `s05-01` 60, `s05-04` 54, `s06-05` 56, `s06-06` 60; bảng chi phí `s02-08` 80, `s03-07` 78, `s04-07` 78, `s05-10` 78 (trần 80); đề recitation `s07-05` 75, `s07-06` 79, `s07-09` 65 (trần 80).

`deck_lint` dùng trần 60 cho mọi trang trừ tiêu đề "Mục tiêu học tập", "Nội dung", "Tổng kết…", "So sánh…", nên báo `SYLL60` cho bảng chi phí, bảng tổng kết, trang tài liệu tham khảo và đề recitation dưới 80; các dòng đó là ngoại lệ đã biết (mục 10, NT-DSFA-7). Các phát hiện còn lại của `deck_lint` là `STRUCT` đã biết ở mục 10.

## 9. Hình (NT25)

Mọi hình là SVG trong `2627-1/img/lec-11/`, hậu tố `-trang-chieu.svg` như Bài 10 (D-SB4), vẽ lại từ đúng dữ liệu của hình ghi chú bằng một script mới `tools/courses/ds-foundation-algorithms/2627-1/img/lec-11/generate_slide_svg.py` (hoặc mở rộng `generate_note_svg.py`); không sửa SVG của ghi chú. Yêu cầu chung: bố cục ngang (khung khoảng $1\,200\times280$–$340$ đơn vị, như `img/lec-10/*-trang-chieu.svg`), chữ đo được ≥ 16 px ở cả 1600×900 và 390×844 (nếu ở 390 px dưới 16 px thì vẽ thêm bản `-trang-chieu-hep.svg` cho màn hẹp); `role="img"`, `<title>`, `alt` cụ thể trên `<img>`; màu không là tín hiệu duy nhất (viền nét đứt, độ đậm); không công thức trong SVG (nhãn bằng chữ, mũi tên vẽ); mọi số trên hình mà chữ dùng tới đều có trong chữ trên mặt trang.

| Tệp mới | Từ hình ghi chú | Trang | Nội dung và thay đổi so với hình ghi chú |
|---|---|---|---|
| `hai-dac-ta-trang-chieu.svg` | `note-hai-dac-ta.svg` | `s01-08` | hai hàng bộ nén, dòng bit, bộ giải nén; bỏ câu chú thích dài (đưa vào `alt` và ghi chú diễn giả) |
| `lz77-cua-so-trang-chieu.svg` | `note-lz77-cua-so.svg` | `s02-02` | 15 ô, con trỏ sau ô 3, lịch sử 1–3, vùng nhìn trước 4–7, ký tự kế ô 8, mũi tên lùi 3 |
| `lz77-chep-chong-lan-trang-chieu.svg` | `note-lz77-chep-chong-lan.svg` | `s02-05` | một hàng 8 ô $y_1\ldots y_8$ với bốn mũi tên chép $j=1..4$ và ô $y_4$ viền nét đứt; thay sáu hàng của ghi chú để vừa trang |
| `lz78-cay-trang-chieu.svg` | `note-lz78-cay.svg` | `s03-02` | cây sau bốn cặp; bỏ cột cặp bên phải (đã có ở bảng `s03-01`) |
| `lzw-ma-chua-co-trang-chieu.svg` | `note-lzw-ma-chua-co.svg` | `s04-03` | hai hàng bốn cột `abababa`, mũi tên chéo lệch một cột, ô cuối viền nét đứt |
| `jpeg-duong-ong-trang-chieu.svg` | `note-jpeg-duong-ong.svg` | `s05-01` | hai hàng sáu khối, chỉ tên bước bằng chữ (công thức ở `s05-03`, `s05-04`, `s05-09`) |
| `dct-ham-co-so-trang-chieu.svg` | `note-dct-ham-co-so.svg` | `s05-03` | tám ô cột trên một hàng, nhãn $u=0..7$ |
| `zigzag-khoi-luong-tu-trang-chieu.svg` | `note-zigzag-khoi-luong-tu.svg` | `s05-08` | lưới $8\times8$ giá trị khác 0 và đường zigzag; ba ô viền đậm (vị trí 6, 15, 55); bỏ số vị trí ở mọi ô để chữ đủ lớn |

Không dùng trên deck: `note-cau-truc-chuong-11.svg` (trang tổng quan viết bằng lời, NT9), `note-cheetah-byte-rms.svg` (số liệu đã ở bảng `s01-07`, `s01-09`).

**Xóa SVG cũ (D-SB5):** mười hai tệp của deck cũ `two-contracts.svg`, `lz77-window.svg`, `lz77-overlap.svg`, `lz77-roundtrip.svg`, `lz78-trie.svg`, `lz78-roundtrip.svg`, `lzw-trace.svg`, `lzw-kwkwk.svg`, `jpeg-pipeline.svg`, `dct-basis.svg`, `quantization.svg`, `zigzag.svg` được xóa trong commit deck, sau khi `grep` xác nhận deck mới và ghi chú không tham chiếu. Không raster.

## 10. Ngoại lệ `deck_lint` dự kiến (`NGUYEN-TAC-HOC-PHAN.md` mục 5, NT28)

| Mã | Trang | Lý do |
|---|---|---|
| `STRUCT` "bìa không có ID LNN-1-01" | `lec11-s01-01` | P7 dùng `lecNN-sKK-mm` |
| `STRUCT` "mạch cuối không tên Tổng kết", "trang cuối không tên Tài liệu tham khảo" | mạch 7 | recitation đứng sau "Tổng kết" (NT-DSFA-10) |
| `STRUCT` số mạch (7 khi đếm cả recitation) | toàn deck | NT-DSFA-10 |
| `STRUCT` `style=""` tĩnh | chỉ ở `<img>` của các hình, nếu cần đặt chiều cao | P7 cho phép ở hình |
| `SYLL60` dưới 80 | `s02-08`, `s03-07`, `s04-07`, `s05-10` (bảng chi phí); `s01-03`, `s01-04`, `s01-05`, `s06-01`, `s06-02`, `s06-07`, `s06-08` nếu công cụ không xếp vào nhóm trần 80; `s07-02`, `s07-05`, `s07-06`, `s07-09` (đề recitation) | NT-DSFA-7, NT17 |
| `SYLL60`/`SYLL80` có ngoại lệ | các trang ở bảng mục 8 | lý do ở mục 8 |
| `NOTES150` dưới 250 | `s02-06`, `s03-05`, `s04-05`, `s05-05` (Tính đúng); `s02-07`, `s03-06`, `s04-06`, `s05-06` (ý tưởng chứng minh); trang đề và lời giải (`s01-09`, `s01-10`, `s06-04`, `s06-05`, `s07-01`–`s07-10`) | `NGUYEN-TAC-HOC-PHAN.md` mục 5; NT22 |
| Tiêu đề lặp | `s01-03`, `s01-04` ("Mục tiêu học tập"); các cặp đề–lời giải; `s07-05`/`s07-06`, `s07-08`/`s07-09` | trang mục tiêu tách hai; lời giải cùng tiêu đề với đề (NT24); đề 11.16, 11.17 tách hai trang, tên phần sau dấu phẩy (NT16) |

## 11. Ánh xạ mã trang cũ → mới

| Cũ | Tiêu đề cũ | Mới | Quyết định |
|---|---|---|---|
| `P00` | bìa | `s01-01` | sửa |
| `P01` | Mục tiêu học tập | `s01-03`, `s01-04` | sửa, tách |
| `P03` | Nội dung | `s01-05` | sửa |
| `P02` | Hai đặc tả khôi phục (`two-contracts.svg`) | `s01-07`, `s01-08` | sửa, tách |
| — | — | `s01-02`, `s01-06` (NT11); `s01-09`, `s01-10` (NT24, D-SB1) | thêm |
| `LT` | 2. Nén LZ77 với cửa sổ trượt | `s02-00` | sửa |
| `L00`, `L01` | LZ77: trỏ về dữ liệu vừa thấy; Cửa sổ chia dữ liệu thành hai miền | câu kết `s01-10`, `s02-01`, hình ở `s02-02` | gộp |
| `L02` | Hai dạng bộ ba (có `EOS`) | `s02-03` | sửa: bỏ `EOS` |
| `L04` | Vết mã hóa giữ ba trạng thái | `s02-02` | sửa |
| `L03` | Chọn cụm khớp dài nhất | `s02-04` | sửa |
| `L05`, `L06` | Sao chép chồng lấn; Giải mã không cần tìm kiếm | `s02-05` | gộp |
| `L07` | Hai nhánh đều bảo toàn lịch sử | `s02-06`, `s02-07` | tách |
| `L08` | Cửa sổ quyết định chi phí | `s02-08` | sửa |
| `L09` | Kiểm tra bộ ba chồng lấn | — | bỏ: câu hỏi tự dựng; bước kiểm tra do Bài tập 11.12, 11.13, 11.14 đảm nhận |
| `ZT` | 3. Nén LZ78 với từ điển tăng dần | `s03-00` | sửa |
| `Z00`, `Z02` | LZ78: tích lũy các cụm đã học; Bốn cặp đầu | `s03-01` | gộp |
| `Z01` | Mỗi cụm mới thêm đúng một ký tự (`lz78-trie.svg`) | `s03-02` | sửa |
| `Z03` | Hai phía dùng cùng phép cập nhật | `s03-03`, `s03-04` | tách |
| `Z04` | Quy nạp theo số cặp | `s03-05`, `s03-06` | tách |
| `Z05` | Từ điển toàn luồng cần biểu diễn gọn | `s03-07` | sửa |
| `Z06` | Kiểm tra phần còn lại của vết LZ78 | — | bỏ: trùng Bài tập 11.15 của recitation |
| `WT` | 4. Nén LZW | `s04-00` | sửa |
| `W00`, `W02` | LZW: bỏ ký tự khỏi cặp LZ78; vết `ppqpprpqrpqrq` | `s04-01` | gộp; đổi dữ liệu |
| `W01` | Mã hóa khái quát hóa vết chạy | `s04-02` | sửa |
| `W03`, `W04` | Giải mã dựng lại vết; Mã kế có thể đến trước mục từ (`lzw-kwkwk.svg`) | `s04-03` | gộp |
| `W05` | Giải mã đầy đủ kiểm soát độ trễ một mục | `s04-04`, `s04-05` | tách |
| — | — | `s04-06` | thêm (NT6) |
| `W06` | Định dạng bit là hợp đồng riêng ($T=2^b$, `MAX`) | `s04-07` | sửa: bỏ đổi độ rộng mã (D6) |
| `W07` | Kiểm tra mã chưa có | — | bỏ: trùng Bài tập 11.16 |
| `JT` | 5. Nén ảnh mất dữ liệu bằng JPEG | `s05-00` | sửa |
| `J00`, `J02` | JPEG mất dữ liệu dựa trên DCT; Hai vị trí có thể làm mất dữ liệu | `s05-01` | gộp |
| `J01` | Tốc độ bit và sai số cùng tạo đặc tả | `s01-07` | chuyển về Mục 1 như ghi chú |
| `J03` | Khối 8×8 tạo đơn vị xử lý cục bộ | `s05-02` | sửa |
| `J05`, `J04` | Trực giác tần số; DCT | `s05-03` | gộp |
| `J06`, `J07` | Lượng tử hóa tạo sai số có chủ đích (ô $(0,2)$, $(0,4)$); Ma trận lượng tử đặt ưu tiên theo tần số | `s05-04`; ô của Hình 11.11 thành Bài tập 11.8 (về nhà) | gộp |
| `J08` | DC và AC tạo hai dòng ký hiệu (`zigzag.svg`) | `s05-07`, `s05-08` | tách |
| `J09` | IDCT tái tạo hệ số đã lượng tử | `s05-05` | sửa |
| — | — | `s05-06`, `s05-09` | thêm |
| `J10` | Chi phí tỉ lệ với số điểm ảnh | `s05-10` | sửa |
| `J11` | Kiểm tra đường ống JPEG | — | bỏ: câu hỏi tự dựng |
| `ST` | 6. Tổng kết và tự kiểm tra | `s06-00` | sửa (NT15) |
| `S00` | Chọn cấu trúc theo hợp đồng và chi phí | `s06-02` | sửa |
| `S01` | Chọn và loại phương án | `s06-06` | sửa |
| — | — | `s06-01`, `s06-03`–`s06-05`, `s06-07`, `s06-08` | thêm (NT15, NT-DSFA-10) |
| `XT` | 7. Bài tập vận dụng | `s07-00` | sửa |
| `X00` | Bài tập củng cố (giao nhiệm vụ) | — | bỏ: trang tiêu đề mạch thay chức năng |
| `X01` | Hoàn tất vết LZ77 | `s07-01` | sửa; lời giải trong ghi chú diễn giả |
| `X02` | Giải mã một bộ ba LZ77 (vị trí tuyệt đối) | `s07-02` | sửa: khoảng lùi; lời giải trong ghi chú diễn giả |
| `X03` | Hoàn tất vết LZ78 | `s07-03`, `s07-04` | sửa, thêm trang lời giải |
| `X04` | Xử lý độ trễ một mục của LZW | `s07-05`, `s07-06`, `s07-07` | sửa, tách đề, thêm trang lời giải |
| `X05` | Chọn biến đổi cho nén mất dữ liệu | `s07-08`–`s07-10` | sửa, tách đề, thêm trang lời giải |

Không trang nào của học liệu khác liên kết tới `id` của deck cũ (deck chưa có trên `index.html`), nên đổi toàn bộ mã trang không làm gãy liên kết.

## 12. Số trang, thời lượng và các điểm đã quyết

| Mạch | Trang | Phút | Phút mỗi trang |
|---|---:|---:|---:|
| 1 Mở đầu | 10 | 15 | 1,5 |
| 2 LZ77 | 9 | 23 | 2,6 |
| 3 LZ78 | 8 | 17 | 2,1 |
| 4 LZW | 8 | 20 | 2,5 |
| 5 JPEG | 11 | 29 | 2,6 |
| 6 Tổng kết | 9 | 16 | 1,8 |
| **Giảng** | **55** | **120** | |
| 7 Recitation | 11 | 60 | 11.12: 15; 11.13: 8; 11.15: 12; 11.16: 13; 11.17: 12 |
| **Tổng** | **66** | **180** | |

Thời lượng chuyển 3 phút từ mạch 5 sang mạch 6 (bài tập tổng hợp 11.14, câu hỏi tự kiểm tra) và 1 phút sang mạch 1 (Bài tập 11.1(b)) (cổng III.2).

**Lý do 55 trang giảng** (NT-DSFA-11, vượt khoảng 42–50, bằng trần; điều phối viên chấp nhận, D-SB2): 19 trang cố định (6 trang khung mở đầu của NT11, trong đó mục tiêu tách hai trang; 9 trang "Tổng kết" của NT15 và NT-DSFA-10; 4 trang tiêu đề mạch 2–5); 19 trang "Thuật toán", "Tính đúng", "Ý tưởng chứng minh", "Chi phí" của bốn cụm thuật toán (NT-DSFA-2, NT6; LZ77, LZ78, LZW mỗi cụm hai trang thuật toán cho mã hóa và giải mã); 2 trang Bài tập 11.1(b) (NT24, D-SB1); còn 15 trang cho bài toán, ví dụ chạy tay, định nghĩa, DCT, lượng tử hóa, mã hệ số.

**Lý do 11 trang recitation** (NT-DSFA-11: "vượt khoảng thì ghi lý do trong storyboard"): đề Bài tập 11.16 (~142 âm tiết) và 11.17 (~150) của `exercises.md` hiện hành vượt giới hạn 120 của một trang, nên mỗi đề tách hai trang; ba cụm LZ78, LZW, JPEG chỉ có bài với "Lời giải:" trên mặt trang trong phần này (NT24), nên ba trang lời giải 11.15, 11.16, 11.17 phải giữ; lời giải 11.12, 11.13 đã ở ghi chú diễn giả. Tổng $1+1+1+2+3+3=11$. Phương án về 10 trang: đưa lời giải 11.17 vào ghi chú diễn giả, khi đó cụm JPEG không còn bài có "Lời giải:" trên mặt trang (trái NT24). Điểm cần điều phối viên xác nhận.

**Các điểm đã quyết:** D-SB1…D-SB10 ở bảng của mục 0 (điều phối viên, 2026-11-19); phát hiện của cổng III.2 ở bảng thứ hai của mục 0.

**Điểm cần điều phối viên xác nhận:** (1) recitation 11 trang (trên); (2) `s06-04` (đề 11.14) ước ~90 âm tiết, đúng giới hạn 1,5 lần trần 60, và `s07-01` (đề 11.12) ước ~119, sát giới hạn 120: nếu `deck_lint` vượt, cần quyết giữa tách trang (vượt trần trang) và ngoại lệ lớn hơn 1,5 lần.
