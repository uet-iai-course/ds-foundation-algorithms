# Bài 11 — Nén bằng từ điển và nén mất dữ liệu

> Bộ bài giảng: [Deck Bài 11](../../lecture-11-nen-bang-tu-dien-va-nen-mat-du-lieu.html) — Giải thuật nền tảng của Khoa học dữ liệu, Học kỳ 1, năm học 2026–2027.

Bài này đặt cạnh nhau hai họ thuật toán có đặc tả khác nhau. LZ77, LZ78 và LZW phải khôi phục đúng chuỗi; JPEG dựa trên biến đổi cosine rời rạc (DCT) tái tạo ảnh gần đúng. Qua các vết chạy nhỏ, ta sẽ thấy điều kiện đúng của từng thuật toán và cách chọn phương pháp theo đầu ra cần bảo toàn.

---

## 1. Hai đặc tả khôi phục — nền tảng để chọn thuật toán

Trước khi so sánh bất kỳ thuật toán nào, phải tách rõ hai hợp đồng đầu ra, vì chúng quyết định thuật toán nào dùng được.

| Đặc tả | Nghĩa | Thuật toán tiêu biểu |
|---|---|---|
| **Khôi phục đúng** | Ảnh hoặc chuỗi sau giải nén giống hệt từng ký hiệu đầu vào | LZ77, LZ78, LZW |
| **Khôi phục gần đúng** | Đầu ra gần đầu vào theo một độ đo sai số đã chọn | JPEG dựa trên DCT |

Sai một byte là phá vỡ đặc tả của LZ; với JPEG, sai số có kiểm soát lại là một phần của thiết kế. Vì thế, tiêu chí đầu tiên khi chọn thuật toán là dữ liệu có cho phép mất thông tin hay không.

- Dữ liệu nhãn, văn bản trong ảnh, phép đo cần bảo toàn tuyệt đối → **không** dùng JPEG mất dữ liệu.
- Một kho ảnh xem trước cho phép sai số và cần giảm băng thông → JPEG cho phép đổi tốc độ bit lấy sai số tái tạo.

Hình minh họa hai đặc tả: ![Hai đặc tả khôi phục](img/lec-11/two-contracts.svg)

Phần nén từ điển dựa trên Chương 8–9 của Nelson–Gailly; phần nén mất dữ liệu dựa trên Chương 11. Hai bộ slide CMU `compression3-lz` và `compression4-lossy` cung cấp khung so sánh và các bài luyện.

---

## 2. LZ77 — trỏ về dữ liệu đã thấy trong cửa sổ hữu hạn

### 2.1 Vai trò và giới hạn

Một luồng nhật ký lớn phải nén trong một lượt; bộ nén không thể giữ toàn bộ lịch sử nên chỉ duy trì một **cửa sổ hữu hạn**. Cửa sổ chia dữ liệu đang xử lý thành hai miền:

- **Từ điển** (bên trái): phần đã mã hóa, dùng làm nguồn tham chiếu.
- **Vùng nhìn trước** (bên phải): phần sắp mã hóa.

Con trỏ là biên giữa hai miền. Cửa sổ giới hạn bộ nhớ và giới hạn phạm vi lặp có thể khai thác; bù lại, chi phí tìm cụm khớp chi phối thời gian mã hóa.

Hình: ![Cửa sổ LZ77](img/lec-11/lz77-window.svg)

### 2.2 Đặc tả token

Quy ước khoảng lùi `(d, ℓ, c)` của bài:

- **Ký tự thô:** `(0, 0, c)` ghi trực tiếp ký tự `c`.
- **Tham chiếu:** `(d, ℓ, c)` chép `ℓ` ký tự từ khoảng lùi `d` (tính từ cuối đầu ra đã có), rồi ghi `c`.
- Nếu cụm khớp chạm ngay cuối dữ liệu, `c = EOS` — ký hiệu dành riêng ngoài bảng chữ cái, bộ giải mã **không phát** ký hiệu này. `EOS` chỉ hợp lệ ở token cuối.

> Nguồn CMU dùng quy ước **vị trí tuyệt đối** `(p, ℓ, c)` đánh số từ 0. Hai quy ước được đặt cạnh nhau, **không trộn**: khi làm bài giải mã CMU, `p` là vị trí tuyệt đối, không phải khoảng lùi `d`.

### 2.3 Vết chạy mã hóa theo khoảng lùi

Dữ kiện: chuỗi `aacaacabcabaaac`, cửa sổ $W=6$, vùng nhìn trước $L=4$.

| Đã xử lý | Tiền tố nhìn trước | Phát |
|---|---|---|
| (rỗng) | `aacaacabc…` | $(0,0,a)$ |
| `a` | `acaacabc…` | $(1,1,c)$ |
| `aac` | `aacabc…` | $(3,4,b)$ |
| `aacaacab` | `cabaaac` | $(3,3,a)$ |
| `aacaacabcaba` | `aac` | $(1,2,c)$ |

Năm token theo quy ước khoảng lùi là $(0,0,a)$, $(1,1,c)$, $(3,4,b)$, $(3,3,a)$, $(1,2,c)$.

### 2.4 Thuật toán mã hóa (tham lam)

Điều kiện trước: $W$, $L$, bảng chữ cái $\Sigma$ và $EOS$ được hai phía biết. Literal có $d=\ell=0$; tham chiếu có $1\le d\le\min(W,\,|output|)$ và $1\le\ell\le L$.

```text
while còn ký tự chưa mã hóa:
    tìm cụm dài nhất khớp tiền tố vùng nhìn trước
    nếu không khớp: phát (0, 0, ký_tự_đầu)
    nếu có: phát (d, ℓ, ký_tự_kế hoặc EOS)
    trượt qua ℓ + 1 ký tự, hoặc ℓ nếu c = EOS
```

Mỗi vòng tiêu thụ ít nhất một ký tự nên thuật toán dừng. Đây là biến thể tham lam; ta không tuyên bố tối ưu số bit vì chi phí token phụ thuộc định dạng.

### 2.5 Sao chép chồng lấn

Khi nguồn và đích chồng nhau, bộ giải mã phải chép **từng ký tự từ trái sang phải** để ký tự vừa sinh có thể làm nguồn cho bước kế — không được chép một lần bằng lát cắt.

Ví dụ vết: đầu ra đã có `aac`, bộ ba `(3,4,b)` đọc lần lượt `a`, `a`, `c`, rồi **đọc lại `a` vừa ghi ở bước chép thứ nhất**, tạo `aaca`, sau đó thêm `b` thành `aacab`. Ký tự chép thứ tư lấy từ dữ liệu vừa tạo.

Hình: ![Sao chép chồng lấn LZ77](img/lec-11/lz77-overlap.svg)

### 2.6 Giải mã và bất biến lịch sử

Bộ giải mã không cần tìm kiếm — mỗi token xác định trực tiếp nguồn:

```text
for mỗi (d, ℓ, c):
    nếu ℓ=0: require d=0 và c thuộc Σ
    nếu ℓ>0: require 1 ≤ d ≤ min(W, |output|), 1 ≤ ℓ ≤ L
                và c thuộc Σ ∪ {EOS}
    lặp ℓ lần: xuất output[|output| − d]
    nếu c ≠ EOS: xuất c
    nếu c = EOS: require đây là token cuối; dừng
```

**Bất biến:** trước mỗi bộ ba, cửa sổ giải mã bằng hậu tố tương ứng của dữ liệu gốc.

- **Cơ sở:** hai cửa sổ khởi tạo giống nhau.
- **Token thường:** tham chiếu nằm trong lịch sử đúng; chép tuần tự cho đúng cụm rồi thêm `c`, nên bất biến giữ cho bước kế.
- **Token cuối có EOS:** chép đúng cụm còn lại, không phát `EOS`, dừng.

Hai nhánh bao phủ toàn bộ dòng token hợp lệ, nên bộ giải mã khôi phục đúng toàn bộ chuỗi.

![Mã hóa và giải mã LZ77 duy trì cùng lịch sử, kể cả khi vùng nguồn và vùng đích chồng nhau](img/lec-11/lz77-roundtrip.svg)

::: exercise
Đầu ra hiện là `aac`. Bộ ba `(3,4,b)` bổ sung chuỗi nào? Ký tự chép thứ tư lấy từ đâu?
:::

::: hint
Chép tuần tự từng ký tự theo khoảng lùi `d=3`; khi nguồn trỏ vào vùng vừa ghi, đọc dữ liệu đã tạo.
:::

::: solution
Chép `aaca` (bốn ký tự: `a`, `a`, `c`, rồi `a` đọc lại từ ký tự thứ nhất vừa ghi), sau đó thêm `b` → bộ ba bổ sung `aacab`. Ký tự chép thứ tư là `a`, đọc lại ký tự `a` vừa được chép ở bước thứ nhất.
:::

### 2.7 Chi phí, giới hạn

| Đại lượng | Cận hoặc tác động |
|---|---|
| Mã hóa vét cạn | $O(nWL)$ — thử tối đa $W$ vị trí, so tối đa $L$ ký tự |
| Giải mã | $O(n)$ theo số ký tự đầu ra |
| Bộ nhớ làm việc | $O(W+L)$ cho cửa sổ và vùng nhìn trước |
| Chi phí token | Tham chiếu có lợi khi bit cho $d,\ell,c$ ít hơn dữ liệu thay |

Cận $O(nWL)$ là bản tìm kiếm vét cạn; băm tiền tố hoặc cấu trúc tìm kiếm khác có thể giảm ứng viên nhưng cần giả thiết riêng. Lặp xa hơn $W$ không còn nằm trong từ điển. Ta không suy ra tỷ lệ nén cố định.

---

## 3. LZ78 — tích lũy các cụm đã học trong toàn luồng

### 3.1 Vai trò và giới hạn

Luồng ký hiệu có cụm lặp cách xa nhau, chỉ đọc một lượt. Cửa sổ LZ77 có thể quên cụm cũ; LZ78 giữ một **từ điển cụm tăng dần trong toàn luồng**. Đầu ra là cặp (mã cụm, ký tự mới). Từ điển tăng dần nên định dạng phải quy định khi đầy.

### 3.2 Quy tắc mỗi cụm mới thêm đúng một ký tự

Từ điển khởi tạo với gốc mã 0 ánh xạ chuỗi rỗng $\epsilon$. Cụm mới bằng cụm đã biết nối một ký tự mới: $D[\texttt{next}]=D[i]+c$. Có thể biểu diễn từ điển bằng một cây cụm, trong đó mỗi mục mới thêm đúng một cạnh.

Hình: ![Cây từ điển LZ78](img/lec-11/lz78-trie.svg)

### 3.3 Vết chạy mã hóa

Dữ kiện: chuỗi `aabaacabcabcb`, khởi tạo $D[0]=\epsilon$, `next=1`.

| Tiền tố còn lại | Phát | Mục mới | Chuỗi đã xử lý |
|---|---|---|---|
| `aabaac…` | $(0,a)$ | $D[1]=a$ | `a` |
| `abaac…` | $(1,b)$ | $D[2]=ab$ | `aab` |
| `aac…` | $(1,a)$ | $D[3]=aa$ | `aabaa` |
| `cabc…` | $(0,c)$ | $D[4]=c$ | `aabaac` |
| `abc…` | $(2,c)$ | $D[5]=abc$ | `aabaacabc` |
| `abcb` | $(5,b)$ | $D[6]=abcb$ | `aabaacabcabcb` |

Từ điển cuối: $D[1]=a$, $D[2]=ab$, $D[3]=aa$, $D[4]=c$, $D[5]=abc$, $D[6]=abcb$.

### 3.4 Hai phía dùng cùng phép cập nhật

**Mã hóa:**

```text
D[0] ← ε; next ← 1
while còn dữ liệu:
  w ← cụm dài nhất khớp
  nếu hết ngay sau w: phát (mã(w), EOS); dừng
  c ← ký tự sau w; phát (mã(w), c)
  D[next] ← w+c; next++
```

**Giải mã:**

```text
D[0] ← ε; next ← 1
for mỗi (i, c):
  require i có trong D
  nếu c=EOS: require đây là token cuối; xuất D[i]; dừng
  phrase ← D[i]+c; xuất phrase
  D[next] ← phrase; next++
```

Hai nhánh kết thúc:

- **Token thường** `(i, c)`: cùng tạo $D[i]+c$, xuất cụm và thêm cùng mục. Token thường có thể là **token cuối** khi chỉ còn đúng một ký tự mới sau cụm đã biết.
- **Token `(i, EOS)`**: chỉ xuất $D[i]$ rồi dừng; **chỉ hợp lệ** khi nguồn hết ngay sau một cụm đã biết.

`EOS` nằm ngoài bảng chữ cái, không được thêm vào từ điển hay đầu ra. Mỗi token tiêu thụ dữ liệu hoặc kết thúc dòng nên mã hóa dừng.

### 3.5 Quy nạp chứng minh đồng bộ

**Mệnh đề:** với dòng token được đóng khung, chỉ số hợp lệ và hai phía dùng cùng chính sách từ điển, bộ giải mã khôi phục đúng chuỗi.

1. **Cơ sở:** hai phía có $D[0]=\epsilon$, `next=1`.
2. **Token thường $(i,c)$:** cả hai phía—bộ mã hóa khi chọn cụm và bộ giải mã khi đọc `(i,c)`—cùng tạo $D[i]+c$, xuất cụm giống nhau và thêm cùng mục `next`. Hai từ điển vẫn giống nhau.
3. **Token $(i,EOS)$:** không thêm mục, không phát `EOS`, chỉ xuất $D[i]$ và dừng.

Hai nhánh bao phủ cả trường hợp ký tự mới là ký tự cuối lẫn trường hợp nguồn kết thúc đúng sau một cụm đã biết, nên sự đồng bộ được duy trì khắp dòng.

![Mã hóa và giải mã LZ78 cùng tạo một mục từ sau mỗi cặp hợp lệ](img/lec-11/lz78-roundtrip.svg)

::: exercise
Từ trạng thái $D[1]=a$, $D[2]=ab$, $D[3]=aa$, $D[4]=c$, mã hóa phần còn lại `abcabcb`. Hai cặp kế tiếp là gì? $D[5]$ và $D[6]$ bằng gì? Chuỗi đầy đủ được khôi phục ra sao?
:::

::: hint
Cụm dài nhất khớp tiền tố `abcabcb` là `ab` (mã 2), còn lại ký tự `c`; rồi xử lý tiếp cụm `abcb`.
:::

::: solution
Phát `(2,c)` rồi `(5,b)`; $D[5]=abc$, $D[6]=abcb$. Ghép các cụm: `a` + `ab` + `aa` + `c` + `abc` + `abcb` = `aabaacabcabcb`, khôi phục đúng chuỗi gốc. LZ78 gửi cả mã cụm lẫn ký tự mới; LZW sẽ suy ra ký tự này từ cụm kế.
:::

### 3.6 Biểu diễn và chi phí

- Lưu mỗi mục bằng con trỏ cha + ký tự để tránh sao chép cả cụm: $O(M)$ bộ nhớ cho $M$ mục dạng (cha, ký tự).
- Với trie/băm phù hợp: thời gian gần tuyến tính hoặc kỳ vọng theo $n$.
- Nếu mỗi lần tìm/nối phải quét chuỗi, chi phí có thể tăng bậc hai.
- **Lựa chọn khi đầy:** dừng thêm (mã hợp lệ, không học cụm mới); khởi tạo lại (thích nghi lại, phải báo hiệu đồng bộ); tăng độ rộng (giữ thêm cụm, mỗi mã tốn nhiều bit hơn).

---

## 4. LZW — bỏ ký tự khỏi cặp LZ78

### 4.1 Vai trò

Luồng byte lớn đọc một lượt. LZW nạp sẵn bảng chữ cái ($D[0..255]$ là các byte, `next_code=256`) nên chỉ phát **mã cụm**; đổi lại, hai phía cùng quản lý một từ điển và phải suy ra ký tự mới từ cụm kế.

Trong vết chạy dưới đây, dòng mã nguyên đã được đóng khung và `next_code=256`. Vì vậy, **mã 256 là mục dữ liệu mới đầu tiên**, không phải `EOS`. Biến thể mã cố định 12 bit trong sách chỉ dùng để đối chiếu hợp đồng định dạng.

### 4.2 Thuật toán mã hóa

```text
D[0..255] ← các byte; next_code ← 256
nếu đầu vào rỗng: trả dòng mã rỗng
w ← byte đầu
for mỗi byte kế k:
  nếu w+k có trong D: w ← w+k
  ngược lại: phát mã(w); D[next_code] ← w+k
               next_code++; w ← k
phát mã(w)
```

Quy tắc: nếu $wk$ đã có thì kéo dài $w$; nếu chưa có thì phát mã của $w$ rồi thêm $wk$. Mỗi vòng đọc một byte nên thuật toán dừng; lệnh phát cuối xử lý cụm còn lại.

### 4.3 Vết chạy đầy đủ

Ánh xạ byte: $p\mapsto112$, $q\mapsto113$, $r\mapsto114$; `next_code=256`. Chuỗi `ppqpprpqrpqrq` cho dòng mã:

$$112,\ 112,\ 113,\ 256,\ 114,\ 257,\ 260,\ 113,\ 114,\ 113$$

Các mục mới 256–264 lần lượt: `pp`, `pq`, `qp`, `ppr`, `rp`, `pqr`, `rpq`, `qr`, `rq`.

Hình vết đầy đủ gồm cả quyết định kéo dài: ![Vết mã hóa LZW](img/lec-11/lzw-trace.svg)

### 4.4 Giải mã — đường thường

Khối dưới đây chỉ mô tả trường hợp mã kế đã có trong từ điển. Mục 4.6 ghép nó với trường hợp mã đến sớm để tạo bộ giải mã đầy đủ.

```text
old ← mã đầu; require old thuộc bảng chữ cái
w ← D[old]; xuất w
for mỗi mã k đã có trong D:
  entry ← D[k]; xuất entry
  D[next_code] ← w + first(entry)
  next_code++; w ← entry
```

Sau ba mã `112,112,113`, đầu ra là `ppq` và bộ giải mã có $D[256]=pp$, $D[257]=pq$. Trong đường này, trước mã kế, mọi mã nhỏ hơn `next_code` của bộ giải mã trùng với bộ mã hóa. Bộ mã hóa có thể vừa tạo thêm đúng một mục mà bộ giải mã chưa đủ cụm kế để suy ra → xuất hiện trường hợp **mã đến trước mục**.

### 4.5 Trường hợp $k=\texttt{next\_code}$

Vì bộ mã hóa có thể đi trước đúng một mục, một mã kế có thể **bằng** `next_code` của bộ giải mã — tức chưa có trong từ điển nhưng vẫn hợp lệ. Khi này bộ mã hóa vừa tạo `w + first(w)` rồi phát mã đó ngay, nên:

$$\text{entry} = w + \text{first}(w)$$

được xác định duy nhất: `w` là cụm trước của bộ giải mã, nối ký tự đầu của chính `w`.

Hình: ![Mã LZW chưa có](img/lec-11/lzw-kwkwk.svg)

### 4.6 Giải mã đầy đủ với độ trễ một mục

```text
nếu dòng mã rỗng: trả chuỗi rỗng
old ← mã đầu; require old thuộc bảng chữ cái
w ← D[old]; xuất w
for mỗi mã k:
  nếu k có trong D:      entry ← D[k]
  nếu k = next_code:     entry ← w + first(w)
  nếu k > next_code:     báo lỗi
  xuất entry; D[next_code] ← w + first(entry)
  next_code++; w ← entry
```

**Ba trường hợp của mã kế:**

- $k<\texttt{next\_code}$: tra bảng — mọi mục nhỏ hơn `next_code` đã đồng bộ ở hai phía.
- $k=\texttt{next\_code}$: mục duy nhất chưa có nhưng hợp lệ — suy `w + first(w)`.
- $k>\texttt{next\_code}$: độ trễ vượt một mục → dòng mã hỏng.

**Bất biến độ trễ một mục:** trước mỗi mã kế, mọi mục có mã nhỏ hơn `next_code` của bộ giải mã trùng với bộ mã hóa; bộ mã hóa chỉ có thể đi trước đúng một mục tại mã `next_code`. Sau khi xuất `entry` và thêm `w + first(entry)`, bất biến được duy trì. Hai từ điển vì thế không nhất thiết giống nhau ở mọi thời điểm: bộ giải mã có thể trễ đúng một mục.

::: exercise
Bộ giải mã có cụm trước $w=\texttt{aba}$ và `next_code=271`. So sánh ba mã kế 270, 271, 272: mã nào tra bảng, mã nào suy ra, mã nào lỗi?
:::

::: hint
Áp dụng ba trường hợp $k<\texttt{next\_code}$, $k=\texttt{next\_code}$, $k>\texttt{next\_code}$ với `next_code=271`.
:::

::: solution
Mã 270 nhỏ hơn 271 nên tra trong từ điển. Mã 271 bằng `next_code` là trường hợp duy nhất chưa có nhưng hợp lệ: `entry = w + first(w) = aba + a = abaa`; xuất `abaa`, thêm $D[271]=abaa$, rồi tăng `next_code`. Mã 272 lớn hơn `next_code` nên báo lỗi vì độ trễ vượt một mục.
:::

### 4.7 Định dạng bit là một hợp đồng riêng

- Với mã rộng $b$ bit, ngưỡng hiện tại là $T=2^b$; `MAX` là giới hạn cuối của từ điển. **Tách $T$ khỏi `MAX`**: $T$ mô tả biên biểu diễn của $b$ bit, còn `MAX` mô tả giới hạn cuối của từ điển.
- Định dạng phải công bố **mã đầu tiên bộ mã hóa phát bằng $b+1$ bit**.
- Định dạng phải công bố **vị trí bộ giải mã đổi sang $b+1$ bit trước khi đọc**, có tính đến độ trễ một mục (bộ giải mã có thể trễ bộ mã hóa một mục, nên không thể đổi cùng lúc khi `next_code` cục bộ chạm $T$).
- Khi đạt `MAX`: dừng thêm (freeze) hoặc khởi tạo lại (reset) bằng tín hiệu đã công bố.
- Các định dạng có thể chọn quy ước early-change hoặc late-change; bài không chốt công thức khi nguồn không quy định.
- Với băm kỳ vọng $O(1)$: mã hóa kỳ vọng $O(n)$, giải mã $O(n)$ theo đầu ra, mỗi mục (cha, ký tự) chiếm $O(1)$ từ máy.

---

## 5. JPEG mất dữ liệu dựa trên DCT

### 5.1 Vai trò và đặc tả tốc độ bit–sai số

Một kho ảnh lớn cần giảm dung lượng lưu trữ và băng thông; khôi phục đúng từng mẫu không còn là yêu cầu. Đặc tả là một **điểm làm việc giữa tốc độ bit và sai số**: số bit của dòng nén (hoặc bit trên mỗi điểm ảnh) và căn sai số bình phương trung bình:

$$E_{RMS}=\sqrt{\frac{1}{N}\sum_{i=1}^{N}(X_i-\hat X_i)^2}$$

trong đó $X$ là ảnh gốc, $\hat X$ là ảnh tái tạo. Hai ảnh cùng RMS vẫn có thể khác nhau về chất lượng cảm nhận, nên RMS **không thay thế** đánh giá thị giác.

- Lượng tử mạnh hơn thường tạo nhiều hệ số 0 (giảm tốc độ bit) và tăng sai lệch (tăng RMS), nhưng kết quả còn phụ thuộc nội dung ảnh và bộ mã entropy → **không có tỷ lệ kích thước–sai số cố định**.

Hình hai đặc tả: ![Hai đặc tả](img/lec-11/two-contracts.svg)

### 5.2 Đường ống JPEG dựa trên DCT

Thứ tự đầy đủ: chia khối $8\times8$ → dịch mức (trừ 128) → DCT → lượng tử hóa → tách DC/AC → zigzag → mã độ dài loạt (RLE) → mã entropy. Giải mã chạy ngược: giải mã entropy → khôi phục DC/AC → nhân bước $Q_{u,v}$ → IDCT → hoàn nguyên mức và màu.

Hình: ![Đường ống JPEG](img/lec-11/jpeg-pipeline.svg)

**Hai vị trí có thể làm mất dữ liệu:**

- **Lấy mẫu thưa sai màu** (tùy chọn, trước DCT): có thể bỏ mẫu kênh màu.
- **Lượng tử hóa:** phép làm tròn $\hat C=\operatorname{round}(C/Q)$ không khả nghịch nói chung — đây là bước mất dữ liệu chính.

Các bước còn lại **không mất thêm dữ liệu**: DCT là biến đổi khả nghịch nếu giữ chính xác hệ số; sai phân DC, zigzag, RLE và mã entropy khôi phục đúng đầu vào của từng bước.

### 5.3 Khối $8\times8$ và dịch mức

- Biến đổi phù hợp cần giảm tương quan, gom năng lượng và cho phép lược thành phần ít quan trọng.
- Biến đổi toàn ảnh theo mô hình tính trực tiếp tốn nhiều trạng thái và kém thích nghi với cấu trúc cục bộ.
- JPEG chia mỗi thành phần thành khối $8\times8$, trừ 128 (dịch miền $0..255$ thành $-128..127$) trước DCT.
- Khối giới hạn chi phí, nhưng lượng tử mạnh có thể làm lộ biên khối.

Hình minh họa định tính tần số không gian (không phải giá trị hàm cơ sở): ![Trực giác tần số](img/lec-11/dct-basis.svg)

### 5.4 DCT — biến đổi cosine rời rạc

Với $x,y,u,v\in\{0,\ldots,7\}$:

$$C_{u,v}=\alpha(u)\,\alpha(v)\sum_{x=0}^{7}\sum_{y=0}^{7} f_{x,y}\cos\!\frac{(2x+1)u\pi}{16}\cos\!\frac{(2y+1)v\pi}{16}$$

với $\alpha(0)=1/\sqrt{8}$ và $\alpha(t)=1/2$ khi $t>0$. Với chuẩn hóa này biến đổi là trực chuẩn. $C_{0,0}$ là thành phần một chiều; chỉ số lớn hơn mô tả thay đổi nhanh hơn. DCT của ảnh tự nhiên thường gom năng lượng vào một số hệ số tần số thấp.

### 5.5 Lượng tử hóa

$$ \hat C_{u,v}=\operatorname{round}\!\left(\frac{C_{u,v}}{Q_{u,v}}\right), \qquad \tilde C_{u,v}=Q_{u,v}\,\hat C_{u,v},\quad Q_{u,v}>0 $$

- $\hat C_{u,v}$ là số nguyên lượng tử (đầu vào mã hóa entropy), $\tilde C_{u,v}$ là hệ số tái tạo mà IDCT sẽ dùng.
- Bước nhỏ ở vùng tần số thấp giữ biến thiên chậm; bước lớn ở tần số cao thường tạo thêm hệ số 0.
- Ma trận giải nén phải có trong đầu mục hoặc được suy ra theo chuẩn.

**Hai ô trong Hình 11.10–11.11 của Nelson–Gailly:**

- Tại $(0,2)$: $C_{0,2}=-9$, $Q=7$ nên $\hat C=-1$ và $\tilde C=-7$. Ô này nằm ở lượt zigzag 6, đếm từ 1.
- Tại $(0,4)$: $C=3$, $Q=11$ → $\hat C=0$, $\tilde C=0$, nằm ở lượt zigzag 15; ô này góp vào một loạt 0 trong RLE.

Hình lượng tử: ![Lượng tử hóa](img/lec-11/quantization.svg)

::: exercise
Với $C_{0,2}=-9$, $Q=7$, tính $\hat C$ và $\tilde C$. Ô này ở lượt zigzag nào? Phân biệt DC, AC và nêu bước nào làm mất dữ liệu.
:::

::: hint
Nhớ $\hat C=\operatorname{round}(C/Q)$ và $\tilde C=Q\hat C$; ô $(0,2)$ là một hệ số AC, quét theo đường zigzag.
:::

::: solution
$\hat C=\operatorname{round}(-9/7)=\operatorname{round}(-1.2857)=-1$; $\tilde C=7\cdot(-1)=-7$. Ô $(0,2)$ thuộc 63 hệ số AC và nằm ở lượt zigzag 6, đếm từ 1. DC là $C_{0,0}$, được mã sai phân trong cùng thành phần; AC là 63 ô còn lại, quét zigzag rồi RLE trước mã entropy. Lượng tử hóa không khả nghịch nói chung; lấy mẫu thưa sai màu là bước mất dữ liệu tùy chọn trước DCT.
:::

### 5.6 DC/AC, zigzag, RLE

- **DC:** $C_{0,0}$; mã sai phân với DC của khối trước cùng thành phần theo thứ tự quét. Mốc khởi động lại, nếu có, tái lập dự đoán.
- **AC:** 63 ô còn lại; quét zigzag rồi RLE.
- Ô $(0,2)$ — lượt zigzag 6 và $(0,4)$ — lượt 15 (đếm từ 1); giá trị 0 ở $(0,4)$ góp một loạt 0.

Hình: ![Quét zigzag](img/lec-11/zigzag.svg)

Zigzag và RLE không làm mất thêm dữ liệu; chúng chỉ sắp xếp lại và đóng gói hệ số đã lượng tử.

### 5.7 IDCT

$$\tilde f_{x,y}=\sum_{u=0}^{7}\sum_{v=0}^{7}\alpha(u)\,\alpha(v)\,\tilde C_{u,v}\cos\!\frac{(2x+1)u\pi}{16}\cos\!\frac{(2y+1)v\pi}{16}$$

IDCT đảo DCT **đối với hệ số đầu vào** — nó tái tạo từ $\tilde C$, không phải từ $C$ gốc, nên **không phục hồi sai số lượng tử**. Nếu mã hóa đã lấy mẫu thưa sai màu, nội suy cũng không phục hồi mẫu đã bỏ.

### 5.8 Chi phí và giới hạn

| Bước | Chi phí mỗi khối $8\times8$ | Bộ nhớ làm việc |
|---|---|---|
| DCT/IDCT | hằng số phép toán cho khối cố định | một vài khối |
| Lượng tử, zigzag | 64 phép chia/làm tròn; 64 vị trí | 64 hệ số |
| Toàn ảnh $N$ mẫu | $\Theta(N)$ với khối cố định | có thể xử lý theo dải |

Trong mô hình RAM, phép toán số học có chi phí hằng; cài đặt DCT nhanh chỉ thay đổi hằng số. Độ phức tạp tuyến tính không cho một tỷ lệ nén hay RMS cố định: kết quả phụ thuộc ảnh và cách mã hóa.

---

## 6. So sánh và chọn phương pháp

| Phương pháp | Khi có thể tiết kiệm bit | Chi phí trạng thái | Tiêu chí đầu ra |
|---|---|---|---|
| LZ77 | tham chiếu ngắn hơn cụm lặp gần | cửa sổ hữu hạn | đúng từng ký tự |
| LZ78 | cặp mã ngắn hơn cụm đã học | từ điển tăng dần | đúng từng ký tự |
| LZW | mã cụm ngắn hơn dãy byte | từ điển và hợp đồng mã | đúng từng ký tự |
| JPEG/DCT | lượng tử tạo nhiều hệ số 0 | khối và hệ số | cân bằng tốc độ bit–sai số |

Không có phương pháp nào mặc nhiên nén được mọi đầu vào. LZ trả chi phí token hoặc mã từ điển; JPEG phải chọn điểm làm việc giữa tốc độ bit và sai số. Hai họ giải quyết hai hợp đồng khôi phục khác nhau.

::: exercise
Một kho ảnh xem trước cho phép sai số, cần giảm băng thông nhưng vẫn phải theo dõi chất lượng tái tạo. Chọn một phương pháp trong bài, nêu hai lý do theo ràng buộc và loại ít nhất một phương án còn lại.
:::

::: hint
Dữ liệu cho phép gần đúng nên cần một phương pháp có đặc tả khôi phục gần đúng. Các phương án LZ giữ đúng chuỗi byte và không khai thác trực tiếp tương quan không gian.
:::

::: solution
Chọn JPEG mất dữ liệu dựa trên DCT vì đầu ra cho phép gần đúng và lượng tử có thể điều chỉnh để đổi tốc độ bit lấy sai số. Loại LZ77, LZ78 hoặc LZW vì chúng giữ đúng chuỗi byte, không khai thác trực tiếp tương quan không gian và vẫn phải trả chi phí mã. Một lựa chọn khác chỉ hợp lệ khi nêu rõ đặc tả, nguồn dư thừa và chi phí trạng thái.
:::

---

## 7. Năm bài tập củng cố và lời giải

Dữ kiện giữ nguyên theo nguồn CMU; ký hiệu thống nhất với phần giảng.

### Bài 1 — Hoàn tất vết mã hóa LZ77

Chuỗi `aacaacabcabaaac`, từ điển tối đa $W=6$, vùng nhìn trước tối đa $L=4$. Ba bộ ba đầu: $(0,0,a)$, $(1,1,c)$, $(3,4,b)$.

::: exercise
Đánh dấu cửa sổ sau mỗi bộ ba; điền hai bộ ba còn lại bằng cụm khớp dài nhất; nêu bước nào dùng sao chép chồng lấn.
:::

::: hint
Theo quy ước khoảng lùi, hai bộ ba còn lại là `(3,3,a)` và `(1,2,c)`; so sánh tiền tố còn lại với cửa sổ để kiểm chứng độ dài cụm.
:::

::: solution
Với quy ước khoảng lùi, hai bộ ba còn lại là $(3,3,a)$ và $(1,2,c)$. Sao chép chồng lấn xảy ra tại $(3,4,b)$, chép `aaca` rồi thêm `b`, và $(1,2,c)$, chép `aa` rồi thêm `c`. Toàn bộ năm token giải mã thành `aacaacabcabaaac`.
:::

### Bài 2 — Giải mã một bộ ba LZ77 theo CMU

Phần giảng dùng $(d,\ell,c)$ (khoảng lùi); bài nguồn CMU dùng $(p,\ell,c)$ (vị trí tuyệt đối, đánh số từ 0). Từ điển hiện tại `abcd`; token $(2,9,e)$ với $p=2$ trỏ tới `c`.

::: exercise
Phát biểu quy ước; viết chín ký tự được chép; viết chuỗi sau khi thêm `e`; chỉ ra dữ liệu vừa tạo được đọc lại ở đâu.
:::

::: hint
Đây là vị trí tuyệt đối $p$, không phải khoảng lùi; bắt đầu tại chỉ số 2 (`c`) và chép tuần tự, nguồn dần dần gồm cả dữ liệu vừa tạo.
:::

::: solution
Với $p=2$ tuyệt đối, đếm từ 0, bắt đầu tại `c`: chép chín ký tự `cdcdcdcdc`, rồi thêm `e` thành `cdcdcdcdce`. Toàn bộ đầu ra là `abcdcdcdcdcdce`. Từ ký tự sao chép thứ ba trở đi, nguồn gồm dữ liệu vừa tạo.
:::

### Bài 3 — Hoàn tất vết mã hóa LZ78

Chuỗi `aabaacabcabcb`, khởi tạo $D[0]=\epsilon$. Bốn cặp đầu: $(0,a),(1,b),(1,a),(0,c)$.

::: exercise
Điền các cặp còn lại; vẽ cây từ điển sau mỗi cặp; giải mã lại để kiểm tra.
:::

::: hint
Từ tiền tố `abcabcb`, cụm đã biết dài nhất là `ab` mang mã 2; ký tự kế là `c`.
:::

::: solution
Hai cặp còn lại là $(2,c)$ và $(5,b)$. Từ điển cuối: $D[1]=a$, $D[2]=ab$, $D[3]=aa$, $D[4]=c$, $D[5]=abc$, $D[6]=abcb$. Ghép các cụm theo thứ tự phát: `a` + `ab` + `aa` + `c` + `abc` + `abcb` = `aabaacabcabcb`.
:::

### Bài 4 — Độ trễ một mục của LZW

Trước mã kế, mọi mã nhỏ hơn `next_code` trùng ở hai phía; bộ mã hóa có thể đi trước đúng mục `next_code`.

::: exercise
Chứng minh khi $k=\texttt{next\_code}$, cụm cần xuất là $w+\texttt{first}(w)$; viết mục mới $D[k]$; phân loại $k<\texttt{next\_code}$ và $k>\texttt{next\_code}$.
:::

::: hint
Mục từ mới mà bộ mã hóa đã tạo nhưng bộ giải mã chưa có mang mã `next_code`. Xét trường hợp cụm kế bắt đầu bằng chính ký tự đầu của $w$.
:::

::: solution
Khi $k=\texttt{next\_code}$, bộ mã hóa đã tạo mục $w+\texttt{first}(w)$ và phát mã của mục đó trước khi bộ giải mã có đủ cụm kế để thêm nó. Vì vậy bộ giải mã suy ra `entry` duy nhất là $w+\texttt{first}(w)$ rồi đặt $D[k]$ bằng cụm này. Nếu $k<\texttt{next\_code}$ thì tra mục đã đồng bộ; nếu $k>\texttt{next\_code}$ thì dòng mã hỏng.
:::

### Bài 5 — Chọn biến đổi cho nén mất dữ liệu

Một biến đổi phù hợp cần giảm tương quan, tạo nhiều hệ số nhỏ và cho phép lược thành phần ít quan trọng.

::: exercise
Theo mô hình tính trực tiếp của nguồn, nêu hai nhược điểm khi biến đổi cosine hoặc Fourier trên toàn ảnh; giải thích vì sao chia khối giảm hai nhược điểm đó; nêu một rủi ro của xử lý theo khối.
:::

::: hint
Đối chiếu với lý do JPEG dùng khối $8\times8$ ở Mục 5.3: trạng thái lớn và kém thích nghi cục bộ.
:::

::: solution
Theo mô hình tính trực tiếp, biến đổi toàn ảnh cần nhiều trạng thái và kém thích nghi với cấu trúc cục bộ. Chia ảnh thành khối nhỏ giới hạn chi phí cho mỗi khối và khai thác cấu trúc cục bộ. Đổi lại, biên khối có thể lộ khi lượng tử mạnh. Kết luận này không áp cho mọi thuật toán biến đổi nhanh toàn ảnh.
:::

---

## 8. Tóm tắt nguồn

- **Nelson–Gailly, *The Data Compression Book*** — nguồn trục.
  - **Chương 8:** LZ77 — cửa sổ hữu hạn, hai dạng bộ ba `(d,ℓ,c)`, mã hóa tham lam, giải mã tuần tự với sao chép chồng lấn, bất biến lịch sử, chi phí $O(nWL)$ (mã hóa vét cạn) / $O(n)$ (giải mã) / $O(W+L)$ (bộ nhớ). Mỗi vòng tiêu thụ ít nhất một ký tự nên thuật toán dừng. Biến thể tham lam không tối ưu bit.
  - **Chương 9:** LZ78/LZW — từ điển cụm tăng dần, quy tắc $D[next]=D[i]+c$, hai nhánh kết thúc với `(i,EOS)`, đồng bộ hai phía; LZW nạp sẵn bảng chữ cái `D[0..255]` với `next_code=256`, độ trễ một mục, hợp đồng độ rộng bit (ngưỡng $T=2^b$ so với `MAX`), biến thể mã cố định 12 bit dùng để đối chiếu định dạng.
  - **Chương 11:** JPEG dựa trên DCT — khối $8\times8$, dịch mức trừ 128, DCT, lượng tử hóa, DC/AC, zigzag, RLE, IDCT; RMS; hai ô lượng tử có nguồn ở Hình 11.10–11.11: $(0,2)$: $C=-9,Q=7\to\hat C=-1,\tilde C=-7$ (lượt 6); $(0,4)$: $C=3,Q=11\to0$ (lượt 15). Chương 10 không dùng làm nguồn JPEG.
- **CMU `compression3-lz.pdf`** — vết và bài luyện LZ: logic 5–6 cho LZ77, logic 13–14 và 18 cho LZ78, logic 16–17 và 19 cho LZW; logic 6–10 đối chiếu điều kiện dừng và chi phí.
- **CMU `compression4-lossy.pdf`** — logic 11 cho mục tiêu biến đổi, nhược điểm của biến đổi toàn ảnh theo mô hình trực tiếp, cùng lợi ích và rủi ro của chia khối.
- **MIT 15.564** — chỉ là nguồn đối chiếu tổng quan, không thay dữ kiện Nelson–Gailly hoặc CMU.

Trong phần LZ77, ký hiệu `(d,ℓ,c)` dùng khoảng lùi; riêng bài CMU dùng vị trí tuyệt đối `(p,ℓ,c)` đếm từ 0. Vết LZW dùng dòng mã nguyên đã đóng khung nên mã 256 là mục dữ liệu mới đầu tiên, không phải `EOS`. Hai ô lượng tử lấy số liệu trực tiếp từ Hình 11.10–11.11; bài tập dùng ô $(0,2)$.
