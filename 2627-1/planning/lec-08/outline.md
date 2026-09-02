# Dàn ý Bài 8

## Phạm vi và mục tiêu

- Bài 8 theo thứ tự đề xuất trong `sources/source.md`: **Dòng dữ liệu: mô hình, lấy mẫu và lọc**.
- Đối tượng: sinh viên đã học xác suất cơ bản, băm và bất biến vòng lặp.
- Phần giảng: 120 phút. Phần bài tập: 60 phút.
- Sản phẩm học tập: đặc tả mô hình dòng; chọn đúng khóa lấy mẫu; chạy và chứng minh lấy mẫu hồ chứa; xây, truy vấn và định cỡ Bloom filter.
- Ngoài phạm vi: Rejection Sampling, Flajolet–Martin, moment, DGIM, cửa sổ trượt và suy giảm theo thời gian.

## Nguồn

| Vai trò | Tệp | Phạm vi dùng |
|---|---|---|
| Giáo trình, nguồn chuẩn | `sources/textbooks/mmds/ch4-mining-data-streams.pdf` | mục 4.1–4.3; bài tập 4.2.1 và 4.3.1–4.3.3 |
| Slide chính | `sources/reference-slides/mmds/ch04-streams1.pdf` | mô hình dòng, lấy mẫu theo khóa, hồ chứa |
| Slide chính | `sources/reference-slides/mmds/ch04-streams2.pdf` | Bloom filter và phân tích |
| Đối chiếu | `sources/reference-slides/stanford-cs246/16-streams.pdf` | bản CS246 ngày 26/02/2026; phép đếm K01 và đường cong B11 (tr.31–32) |
| Đối chiếu | `sources/reference-slides/stanford-cs246-2017/streams-2.pdf` | bản Jeffrey D. Ullman tạo ngày 01/03/2017; ví dụ Bloom 11 bit B05 |

MMDS được ưu tiên ở mọi cụm. Stanford được dùng tại K01 vì phép đếm số truy vấn phân biệt rõ hơn, tại B05 vì có trọn vết 11 bit và tại B11 để đối chiếu hình dạng đường cong. Mọi công thức được kiểm chứng bằng sách; ví dụ B05 giữ nguyên dữ kiện nguồn. Ghi công: <http://www.mmds.org>.

## Mạch phần giảng

1. P00–P02: tình huống dòng truy vấn và sản phẩm học tập.
2. A00–A04: mô hình dòng, trạng thái và mô hình chi phí.
3. K00–K08: lấy mẫu nhất quán theo khóa.
4. R00, R01, R03, R02, R04–R08: vấn đề → phân biệt → chạy tay → đặc tả → thuật toán và chứng minh hồ chứa.
5. B00, B02, B05, B01, B03–B12: tình huống → vị trí hệ thống → ví dụ → đặc tả → thuật toán, bảo đảm và xác suất dương giả.
6. C00–C02: chọn cấu trúc theo câu hỏi, nguồn và phạm vi.
7. X00–X05: bốn bài tập trực tiếp từ MMDS (Ex.4.2.1 tr.138; Ex.4.3.1–4.3.2 tr.141; Ex.4.3.3 tr.142).

## Thuật ngữ và ký hiệu

| Ký hiệu | Nghĩa |
|---|---|
| $t$, $K(t)$ | một bộ trên dòng và khóa của bộ |
| $a/b$ | tỷ lệ khóa cần lấy mẫu |
| $h(K)<a$ | điều kiện chọn khi $h$ có miền $0,\ldots,b-1$; $h$ phải phân bố đều trên toàn miền để tỷ lệ $a/b$ được bảo đảm |
| $s$ | sức chứa hồ chứa, $s\ge1$ |
| $r$ | số vị trí đã thấy ở hồ chứa |
| $n$ | số bit của mảng Bloom |
| $m$ | số khóa được đưa vào Bloom filter |
| $k$ | số hàm băm của Bloom filter |
| $q$ | mật độ bit 1 chính xác dưới mô hình $km$ phép băm iid: $q=1-(1-1/n)^{km}$ |
| $p_{FP}$ | xác suất dương giả; $q^k$ là xấp xỉ chuẩn và dạng mũ $(1-e^{-km/n})^k$ là xấp xỉ khi $n$ lớn |

## Kiểm kê nội dung và hình

- Định nghĩa: mô hình dòng, mẫu theo khóa, mẫu hồ chứa, Bloom filter.
- Thuật toán: `LẤY-MẪU-THEO-KHÓA`, `HỒ-CHỨA`, `XÂY-BLOOM`, `KIỂM-TRA-BLOOM`.
- Chứng minh: tính nhất quán theo khóa; quy nạp xác suất $s/r$; điều kiện không âm giả.
- Phân tích: $\Theta(s)$ bộ nhớ hồ chứa; $\Theta(km)$ xây và $\Theta(k)$ truy vấn Bloom; mật độ bit hữu hạn $q$ chính xác dưới băm iid, FPR $q^k$ là xấp xỉ chuẩn và dạng mũ là xấp xỉ khi $n$ lớn.
- Bài tập: X01 dùng giả thiết lược đồ `Grades` với định danh university duy nhất toàn cục; đáp án và rubric là lời giải giảng viên suy ra từ đề, không in trong sách.
- Sáu SVG tự vẽ: mô hình dòng, mẫu theo khóa, vết hồ chứa, ví dụ Bloom 11 bit, luồng kiểm tra Bloom, đường cong FPR.
- Không dùng ảnh raster, mã trình diễn hoặc tài nguyên mạng cốt lõi.

## Bản đồ chủ đề cho ghi chú tự học

| `note-topic-id` | Nhãn | Chủ đề | Sản phẩm |
|---|---|---|---|
| `L08-N01` | cốt lõi | Mô hình dòng một lượt | hợp đồng và bốn trục chi phí |
| `L08-N02` | cốt lõi | Lấy mẫu sai đơn vị | nhận ra sai lệch khi thống kê theo nhóm |
| `L08-N03` | cốt lõi | Lấy mẫu nhất quán theo khóa | đặc tả, thuật toán và chứng minh $a/b$ |
| `L08-N04` | cầu nối | Điều chỉnh tỷ lệ bằng ngưỡng | đổi tỷ lệ mà không lưu quyết định cũ |
| `L08-N05` | cốt lõi | Lấy mẫu hồ chứa | vết chạy, giả mã và quy nạp $s/r$ |
| `L08-N06` | cốt lõi | Cơ chế Bloom filter | xây, truy vấn và ví dụ 11 bit |
| `L08-N07` | cốt lõi | Bảo đảm không âm giả | điều kiện và giới hạn |
| `L08-N08` | cốt lõi | Mật độ bit và FPR | phân biệt chính xác với xấp xỉ |
| `L08-N09` | cốt lõi | Số hàm băm tối ưu | dẫn xuất và làm tròn $k^*$ |
| `L08-N10` | cốt lõi | Chọn cấu trúc | ánh xạ đầu ra sang trạng thái |
| `L08-N11` | cốt lõi | Bốn bài tập MMDS | sản phẩm recitation truy nguyên được |

Đồ thị tiên quyết: `N01→N02→N03→N04`; `N01→N05`; `N01→N06→N07→N08→N09`; ba nhánh hội tụ tại `N10`, rồi sang `N11`. Ghi chú dùng $r$ cho số phần tử đã thấy ở hồ chứa để không xung đột với $n$ bit của Bloom.
