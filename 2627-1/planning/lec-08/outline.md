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
| Đối chiếu | `sources/reference-slides/stanford-cs246/16-streams.pdf` | bản CS246 ngày 26/02/2026; phép đếm K01 và đường cong B11 |
| Đối chiếu | `sources/reference-slides/stanford-cs246-2017/streams-2.pdf` | bản Jeffrey D. Ullman tạo ngày 01/03/2017; ví dụ Bloom 11 bit B05 |

MMDS được ưu tiên ở mọi cụm. Stanford được dùng tại K01 vì phép đếm số truy vấn phân biệt rõ hơn, tại B05 vì có trọn vết 11 bit và tại B11 để đối chiếu hình dạng đường cong. Mọi công thức được kiểm chứng bằng sách; ví dụ B05 giữ nguyên dữ kiện nguồn. Ghi công: <http://www.mmds.org>.

## Mạch phần giảng

1. P00–P02: tình huống dòng truy vấn và sản phẩm học tập.
2. A00–A04: mô hình dòng, trạng thái và mô hình chi phí.
3. K00–K08: lấy mẫu nhất quán theo khóa.
4. R00, R01, R03, R02, R04–R08: vấn đề → phân biệt → chạy tay → đặc tả → thuật toán và chứng minh hồ chứa.
5. B00, B02, B05, B01, B03–B12: tình huống → vị trí hệ thống → ví dụ → đặc tả → thuật toán, bảo đảm và xác suất dương giả.
6. C00–C02: chọn cấu trúc theo câu hỏi, nguồn và phạm vi.
7. X00–X05: bốn bài tập trực tiếp từ MMDS.

## Thuật ngữ và ký hiệu

| Ký hiệu | Nghĩa |
|---|---|
| $t$, $K(t)$ | một bộ trên dòng và khóa của bộ |
| $a/b$ | tỷ lệ khóa cần lấy mẫu |
| $h(K)<a$ | điều kiện chọn khi $h$ có miền $0,\ldots,b-1$ |
| $s$ | sức chứa hồ chứa, $s\ge1$ |
| $n$ | số vị trí đã thấy; trong cụm Bloom là số bit |
| $m$ | số khóa được đưa vào Bloom filter |
| $k$ | số hàm băm của Bloom filter |
| $p_{FP}$ | xác suất dương giả theo mô hình xấp xỉ |

## Kiểm kê nội dung và hình

- Định nghĩa: mô hình dòng, mẫu theo khóa, mẫu hồ chứa, Bloom filter.
- Thuật toán: `LẤY-MẪU-THEO-KHÓA`, `HỒ-CHỨA`, `XÂY-BLOOM`, `KIỂM-TRA-BLOOM`.
- Chứng minh: tính nhất quán theo khóa; quy nạp xác suất $s/n$; điều kiện không âm giả.
- Phân tích: $\Theta(s)$ bộ nhớ hồ chứa; $\Theta(km)$ xây và $\Theta(k)$ truy vấn Bloom; mật độ bit hữu hạn và FPR xấp xỉ.
- Sáu SVG tự vẽ: mô hình dòng, mẫu theo khóa, vết hồ chứa, ví dụ Bloom 11 bit, luồng kiểm tra Bloom, đường cong FPR.
- Không dùng ảnh raster, mã trình diễn hoặc tài nguyên mạng cốt lõi.
