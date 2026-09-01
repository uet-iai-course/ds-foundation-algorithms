# Goal ghi chú Bài 08

## 1. Goal

Hoàn thiện ghi chú tự học **Bài 08 — Dòng dữ liệu: mô hình, lấy mẫu và lọc** tại `2627-1/materials/lec-08/lecture-note.md`. Tài liệu phải giúp sinh viên chọn đúng trạng thái cho dòng một lượt, lấy mẫu nhất quán theo khóa, chứng minh lấy mẫu hồ chứa và dùng Bloom filter với bảo đảm cùng sai số được phát biểu chính xác.

## 2. Vấn đề trung tâm

Dòng sự kiện đến liên tục, chưa biết độ dài cuối và không thể lưu toàn bộ lịch sử trong bộ nhớ chính. Thuật toán phải xử lý mỗi phần tử khi nó đến, giữ một trạng thái nhỏ và trả đúng loại đầu ra: mẫu theo nhóm, mẫu vị trí kích thước cố định hoặc phép lọc thành viên xác suất.

## 3. Bằng chứng hoàn thành

- Người học đặc tả mô hình dòng một lượt và phân biệt chi phí cập nhật, truy vấn, bộ nhớ, số lượt quét.
- Người học chọn khóa lấy mẫu theo đơn vị thống kê, chạy quy tắc $h(K)<a$ và nêu đúng điều kiện để tỷ lệ là $a/b$.
- Người học chạy lấy mẫu hồ chứa, nêu bất biến và chứng minh mỗi vị trí trong $n$ phần tử đã thấy có xác suất biên $s/n$.
- Người học xây và truy vấn Bloom filter, chứng minh không có âm giả khi trạng thái không bị xóa hoặc hỏng.
- Người học phân biệt $q=1-(1-1/n)^{km}$ với các xấp xỉ FPR và dẫn xuất $k^*=(n/m)\ln2$.
- Bốn bài MMDS 4.2.1 và 4.3.1–4.3.3 giữ nguyên dữ kiện, yêu cầu và nguồn; không thêm bài hồ chứa.
- Viewer, Markdown, KaTeX, SVG, liên kết, bàn phím, màn hình rộng/hẹp, bản in và an toàn đường dẫn đều đạt trước khi cập nhật index.

## 4. Đầu ra

- `2627-1/materials/lec-08/lecture-note.md`.
- Cập nhật phần ghi chú trong `2627-1/planning/lec-08/{outline,storyboard,review-log}.md`.
- Dùng sáu SVG hiện có trong `2627-1/img/lec-08/`.
- Thêm liên kết ghi chú Bài 08 vào `2627-1/index.html` sau khi viewer đạt.
- Không sửa deck trừ khi phát hiện lỗi nội dung dùng chung cần đồng bộ.

## 5. Nguồn và quyết định chọn nguồn

- MMDS Chương 4 mục 4.1–4.3 và hai bộ slide MMDS là trục chính.
- Stanford CS246 2026 dùng để đối chiếu chứng minh hồ chứa và đường cong FPR.
- Stanford CS246 2017 dùng riêng cho ví dụ Bloom 11 bit.
- Bài tập trực tiếp: MMDS Ex.4.2.1 tr.138, Ex.4.3.1–4.3.2 tr.141 và Ex.4.3.3 tr.142.
- MMDS được ưu tiên khi tương đương. Với sai khác số, tự tính lại từ công thức: $k=2$ cho ví dụ một tỷ khóa cho 0,048929… (sách in 0,0493); cấu hình $n/m=8,k=6$ cho khoảng 0,02158.
- Ngoài phạm vi: Rejection Sampling, Flajolet–Martin, moment, DGIM, cửa sổ trượt và suy giảm theo thời gian.

## 6. Bản đồ chủ đề

| `note-topic-id` | Nhãn | Chủ đề và sản phẩm | Nguồn, kết nối |
|---|---|---|---|
| `L08-N01` | cốt lõi | Mô hình dòng một lượt và bốn trục chi phí | MMDS 4.1; đặt hợp đồng cho ba cấu trúc sau |
| `L08-N02` | cốt lõi | Sai lệch của lấy mẫu độc lập từng bộ khi cần thống kê theo nhóm | MMDS 4.2.1; tạo nhu cầu chọn khóa |
| `L08-N03` | cốt lõi | Lấy mẫu nhất quán theo khóa | MMDS 4.2.2–4.2.3; đặc tả, ví dụ, thuật toán, chứng minh và chi phí |
| `L08-N04` | cầu nối | Điều chỉnh tỷ lệ mẫu bằng ngưỡng băm | MMDS 4.2.4; một đoạn ngắn, không mở rộng thành thuật toán mới |
| `L08-N05` | cốt lõi | Lấy mẫu hồ chứa | MMDS/Stanford slide; vết $s=2$, giả mã và chứng minh quy nạp $s/n$ |
| `L08-N06` | cốt lõi | Đặc tả và cơ chế Bloom filter | MMDS 4.3.1–4.3.2; ví dụ 11 bit từ Stanford 2017 |
| `L08-N07` | cốt lõi | Không âm giả và giới hạn bảo đảm | MMDS 4.3.2; điều kiện không xóa bit và băm nhất quán |
| `L08-N08` | cốt lõi | Mật độ bit và xác suất dương giả | MMDS 4.3.3; tách chính xác khỏi xấp xỉ |
| `L08-N09` | cốt lõi | Chọn số hàm băm | MMDS Ex.4.3.3; dẫn xuất $k^*$ và quy tắc làm tròn |
| `L08-N10` | cốt lõi | Chọn cấu trúc theo đầu ra | Tổng hợp ba nhánh, không xếp hạng phổ quát |
| `L08-N11` | cốt lõi | Bốn bài tập MMDS | Dữ kiện và sản phẩm giữ nguyên nguồn |

Đồ thị tiên quyết: `N01→N02→N03→N04`; `N01→N05`; `N01→N06→N07→N08→N09`; ba nhánh hội tụ tại `N10`, rồi dẫn sang `N11`.

## 7. Khuôn trình bày và ký hiệu

Mỗi chủ đề cốt lõi đi theo vai trò; đặc tả; ví dụ chạy tay; trực quan; thuật toán hoặc mệnh đề; chứng minh/lập luận; chi phí, giới hạn và tự kiểm. Công thức Markdown chỉ dùng `$...$` và `$$...$$`; khối tùy biến không lồng nhau.

- Ở phần hồ chứa, $r$ là số vị trí đã thấy và $s\ge1$ là sức chứa.
- Ở phần Bloom, $n$ là số bit, $m$ là số khóa, $k$ là số hàm băm.
- Lấy mẫu theo khóa dùng $h:\mathcal K\to\{0,\dots,b-1\}$ và nhận khi $h(K(t))<a$; tỷ lệ $a/b$ cần $h(K)$ phân bố đều trên toàn miền.
- Với Bloom, $q=1-(1-1/n)^{km}$ là xác suất một bit bằng 1 dưới $km$ phép băm iid. $q^k$ là xấp xỉ chuẩn cho FPR do trạng thái bit và vị trí truy vấn có phụ thuộc; $(1-e^{-km/n})^k$ còn dùng xấp xỉ mũ khi $n$ lớn.

## 8. Rủi ro và điểm cần duyệt

- Không dùng chung ký hiệu $n$ cho hồ chứa và Bloom trong cùng cụm; dùng $r$ cho số phần tử đã thấy ở hồ chứa.
- Không gọi tính nhất quán theo khóa là độc lập giữa các bộ cùng khóa.
- Không hứa Bloom filter không có dương giả; bảo đảm không âm giả chỉ đúng khi không xóa bit và dùng cùng hàm băm.
- Ví dụ Bloom 11 bit phải giữ đúng quy ước chỉ số, hàm băm và kết quả tra cứu của Stanford 2017.
- Đáp án/rubric bốn bài tập là lời giải giảng viên suy ra từ đề vì kho không có lời giải chính thức; phải ghi rõ trong planning.
- Không đưa mã trang, thời lượng, worker, reviewer, prompt, goal hoặc quy trình sản xuất vào ghi chú công khai.

## 9. Kế hoạch tác tử

1. Ba reader `z-ai/glm-5.3-flash` qua OpenRouter lập kế hoạch, ánh xạ nguồn và đề xuất chủ đề độc lập.
2. Codex chính hợp nhất và duyệt goal trước writer.
3. Một writer `deepseek/deepseek-v4-flash-0731` soạn trong gốc tạm hẹp.
4. Năm reviewer `z-ai/glm-5.3-flash` kiểm nguồn, toán–thuật toán, mạch sư phạm, tính liên tục và viewer.
5. Codex chính áp dụng sửa có căn cứ; hai reviewer GLM tái kiểm toán–thuật toán và mạch.
6. Dùng `$no-ai-slop` và `$quill`, không tạo `quill.json`; kiểm viewer thật, rồi mới cập nhật index, commit, push và xác minh SHA.

## 10. Trạng thái

**Sẵn sàng soạn.** Ba reader đã hoàn tất với đúng model và provider. Codex chính đã đối chiếu nguồn, quyết định dùng MMDS làm trục, giữ ví dụ Bloom 11 bit từ Stanford 2017, chốt ranh giới chính xác/xấp xỉ và loại mọi nội dung ngoài phạm vi.
