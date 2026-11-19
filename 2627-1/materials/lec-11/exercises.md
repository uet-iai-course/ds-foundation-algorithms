# Bài tập Bài 11 — Nén bằng từ điển và nén mất dữ liệu

Các bài tập củng cố 11.12–11.17 dưới đây lấy từ các câu hỏi trên trang chiếu của bài giảng *Algorithms in the Real World: Data Compression* của Blelloch cho học phần CMU 15-499, ở phần nén bằng từ điển (tệp `compression3-lz.pdf`) và phần nén mất dữ liệu (tệp `compression4-lossy.pdf`), kèm gợi ý và lời giải. Mọi số hiệu Định nghĩa, Định lý, Mệnh đề, Bổ đề, Nhận xét, Thuật toán, Ví dụ và Tình huống 11.k là của [ghi chú Bài 11](material-viewer.html?doc=materials/lec-11/lecture-note.md&deck=lecture-11-nen-bang-tu-dien-va-nen-mat-du-lieu.html), nơi Bài tập 11.1–11.11 đứng ngay sau các mục; ký hiệu dùng như trong bảng ký hiệu của ghi chú. Bài tập 11.12 và 11.15 dùng cùng chuỗi với Ví dụ 11.2 và Ví dụ 11.4. Năm bài 11.12, 11.13, 11.15, 11.16 và 11.17 là bài tập trên lớp (recitation) của [bộ trang chiếu Bài 11](lecture-11-nen-bang-tu-dien-va-nen-mat-du-lieu.html). Bài tập xếp theo ba mức.

## Mục tiêu và bài tập

| Mục tiêu học tập của ghi chú | Bài tập trong ghi chú | Bài tập trong tệp này |
|---|---|---|
| 1. Hai đặc tả khôi phục, tốc độ bit, sai số RMS, bộ nén rút ngắn mọi đầu vào (Mục 1) | 11.1 | — |
| 2. LZ77: mã hóa, giải mã chồng lấn, tính đúng, chi phí (Mục 2) | 11.2, 11.3 | 11.12, 11.13, 11.14 |
| 3. LZ78: mã hóa, giải mã, cây từ điển, đồng bộ hai từ điển (Mục 3) | 11.4 | 11.15 |
| 4. LZW: mã hóa, giải mã, mã chưa có trong từ điển (Mục 4) | 11.5, 11.6 | 11.16 |
| 5. DCT, lượng tử hóa, zigzag, mã độ dài loạt, cận sai số (Mục 5) | 11.7, 11.8, 11.9, 11.10 | 11.17 (mã hóa theo khối và chi phí của DCT) |
| 6. Chọn phương pháp nén cho một kho dữ liệu (Mục 6) | 11.11 | — |

## Mức nhận biết

::: exercise Bài tập 11.13 (Bộ ba có độ dài lớn hơn khoảng lùi; CMU 15-499, compression3-lz.pdf, trang chiếu 6)
Bộ giải mã LZ77 (Thuật toán 11.6) đã dựng bản giải mã $y=$ `abcd`, tức $p=4$, và đọc bộ ba kế tiếp $(d,\ell,c)=(2,9,\mathrm e)$.

- (a) Giải mã bộ ba: ghi phép gán ở từng bước chép $j=1,\ldots,9$ và cho bản giải mã sau bộ ba.
- (b) Xác định các bước chép đọc một ô nguồn được ghi ngay trong lượt giải mã bộ ba này.
:::

::: hint
Viết vị trí nguồn của bước chép thứ $j$ theo $p$, $j$, $d$ (bước 2.1 của Thuật toán 11.6), rồi so với $p$.
:::

::: solution
**Câu (a).** Bộ ba hợp lệ cho bước 2.1 của Thuật toán 11.6, vì $\ell=9\ge1$ và $d=2\le p=4$. Với $j=1,\ldots,9$, theo thứ tự tăng, gán $y_{4+j}\leftarrow y_{2+j}$:

| $j$ | Phép gán | Ký tự ghi |
|---|---|---|
| 1 | $y_5\leftarrow y_3$ | $\mathrm c$ |
| 2 | $y_6\leftarrow y_4$ | $\mathrm d$ |
| 3 | $y_7\leftarrow y_5$ | $\mathrm c$ |
| 4 | $y_8\leftarrow y_6$ | $\mathrm d$ |
| 5 | $y_9\leftarrow y_7$ | $\mathrm c$ |
| 6 | $y_{10}\leftarrow y_8$ | $\mathrm d$ |
| 7 | $y_{11}\leftarrow y_9$ | $\mathrm c$ |
| 8 | $y_{12}\leftarrow y_{10}$ | $\mathrm d$ |
| 9 | $y_{13}\leftarrow y_{11}$ | $\mathrm c$ |

Bước 2.2 ghi $y_{14}\leftarrow\mathrm e$. Bản giải mã là `abcdcdcdcdcdce`, 14 ký tự.

**Câu (b).** Vị trí nguồn $2+j$ vượt $p=4$ khi $j\ge3$. Bảy bước $j=3,\ldots,9$ đọc ô $y_{2+j}$ được ghi ở bước $j-2$ của chính lượt này; chẳng hạn bước 3 đọc $y_5$, ô ghi ở bước 1. Hai bước đầu đọc $y_3$, $y_4$, hai ô đã có trước bộ ba.

**Kiểm tra lại.** Bản giải mã dài $4+9+1=14$ ký tự. Chín ký tự chép `cdcdcdcdc` lặp đoạn `cd` $=y_3y_4$ với chu kỳ $d=2$, đúng phép gán $y_{4+j}=y_{2+j}$ ở mọi bước.
:::

## Mức tính toán hoặc chứng minh

::: exercise Bài tập 11.12 (Hoàn tất vết LZ77; CMU 15-499, compression3-lz.pdf, trang chiếu 5)
Chuỗi $x=$ `aacaacabcabaaac`, $n=15$, được mã hóa bằng Thuật toán 11.5 với cỡ cửa sổ $W=6$ và độ dài khớp tối đa $L=4$. Ba bộ ba đầu là $(0,0,\mathrm a)$, $(1,1,\mathrm c)$, $(3,4,\mathrm b)$; sau ba bộ ba này, con trỏ ở $p=8$.

- (a) Xác định hai bộ ba còn lại. Với mỗi bộ ba, ghi lịch sử, vùng nhìn trước và độ khớp $\ell(d)$ của từng khoảng lùi $d$.
- (b) Giải mã năm bộ ba bằng Thuật toán 11.6 và ghi bản giải mã sau mỗi bộ ba. Chỉ ra các bộ ba có $\ell>d$ và bước chép đọc một ô vừa ghi trong cùng bộ ba.
- (c) Tính số bit của dòng năm bộ ba theo Mệnh đề 11.9(d) và so với số bit của $x$ khi ghi 8 bit mỗi ký tự.
:::

::: hint
Tại $p=8$, lịch sử gồm sáu ký tự $x[3..8]$. Với mỗi $d=1,\ldots,6$, so $x_9,x_{10},\ldots$ lần lượt với $x_{9-d},x_{10-d},\ldots$ tới lần đầu không khớp.
:::

::: solution
**Câu (a).** Tại $p=8$, lịch sử là $x[3..8]=$ `caacab`, vùng nhìn trước là $x[9..12]=$ `caba`, và cận của độ khớp là $\min(L,n-p-1)=4$. Tại $p=12$, lịch sử là $x[7..12]=$ `abcaba`, vùng nhìn trước là $x[13..15]=$ `aac`, và cận là $\min(4,15-12-1)=2$, chừa $x_{15}$ làm ký tự kế. Độ khớp theo bước 2.1 của Thuật toán 11.5:

| $d$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| $\ell(d)$ tại $p=8$ | 0 | 0 | 3 | 0 | 0 | 2 |
| $\ell(d)$ tại $p=12$ | 2 | 0 | 1 | 0 | 0 | 1 |

Tại $p=8$, chỉ $d=3$ đạt độ khớp lớn nhất: $x_9x_{10}x_{11}=$ `cab` khớp $x_6x_7x_8$, còn $x_{12}=\mathrm a$ khác $x_9=\mathrm c$. Bộ ba thứ tư là $(3,3,\mathrm a)$, và con trỏ lên $p=8+3+1=12$. Tại $p=12$, $d=1$ cho độ khớp lớn nhất: $x_{13}=\mathrm a$ khớp $x_{12}$, $x_{14}=\mathrm a$ khớp $x_{13}$, và cận 2 dừng phép so. Bộ ba thứ năm là $(1,2,\mathrm c)$ với $c=x_{15}$; con trỏ lên $p=15=n$ và thuật toán dừng.

**Câu (b).** Thuật toán 11.6 chép rồi ghi ký tự kế ở mỗi bộ ba:

| Bộ ba | Phép chép | Ký tự kế | Bản giải mã |
|---|---|---|---|
| $(0,0,\mathrm a)$ | không có | $y_1\leftarrow\mathrm a$ | `a` |
| $(1,1,\mathrm c)$ | $y_2\leftarrow y_1$ | $y_3\leftarrow\mathrm c$ | `aac` |
| $(3,4,\mathrm b)$ | $y_{3+j}\leftarrow y_j$, $j=1,\ldots,4$ | $y_8\leftarrow\mathrm b$ | `aacaacab` |
| $(3,3,\mathrm a)$ | $y_{8+j}\leftarrow y_{5+j}$, $j=1,2,3$ | $y_{12}\leftarrow\mathrm a$ | `aacaacabcaba` |
| $(1,2,\mathrm c)$ | $y_{12+j}\leftarrow y_{11+j}$, $j=1,2$ | $y_{15}\leftarrow\mathrm c$ | `aacaacabcabaaac` |

Hai bộ ba có $\ell>d$:

- $(3,4,\mathrm b)$: bước $j=4$ đọc $y_4$, ô ghi ở bước $j=1$;
- $(1,2,\mathrm c)$: bước $j=2$ đọc $y_{13}$, ô ghi ở bước $j=1$.

Bộ ba $(3,3,\mathrm a)$ có $\ell=d$, nên các ô nguồn $y_6,y_7,y_8$ đều có trước khi chép. Theo Bổ đề 11.7, chép theo thứ tự tăng của $j$ cho đúng cả hai bộ ba chồng lấn.

**Câu (c).** Theo Mệnh đề 11.9(d), mỗi bộ ba tốn $\lceil\log_26\rceil+\lceil\log_25\rceil+8=3+3+8=14$ bit. Năm bộ ba tốn $70$ bit, so với $15\cdot8=120$ bit của $x$, tức $70/120\approx0{,}58$. Mỗi bộ ba mô tả trung bình $15/5=3$ ký tự, trên mức hòa vốn $14/8=1{,}75$ ký tự.

**Kiểm tra lại.** Năm bộ ba phủ $1+2+5+4+3=15=n$ ký tự, và bản giải mã cuối cùng trùng $x$.
:::

::: exercise Bài tập 11.14 (LZSS kiểu gzip; CMU 15-499, compression3-lz.pdf, trang chiếu 7)
Biến thể LZSS dùng trong gzip phát một trong hai dạng mục, với chữ số đầu là bit cờ (flag bit):

- $(0,d,\ell)$: chép $\ell$ ký tự từ khoảng lùi $d$, rồi tiến con trỏ $\ell$ ký tự;
- $(1,c)$: ghi một ký tự rời $c$, rồi tiến con trỏ 1 ký tự.

Tại con trỏ $p$, bộ mã hóa tính độ khớp dài nhất $\ell$ và khoảng lùi $d$ như bước 2.1–2.2 của Thuật toán 11.5, với $1\le d\le\min(W,p)$, cận $\ell\le\min(L,n-p)$ thay cho $\min(L,n-p-1)$, và cho phép $\ell>d$. Nó dùng dạng thứ nhất khi $\ell\ge3$ và dạng thứ hai, với $c=x_{p+1}$, khi $\ell<3$. Chuỗi $x=$ `aacaacabcabaaac`, $n=15$, được mã hóa với $W=6$, $L=4$; ba mục đầu là $(1,\mathrm a)$, $(1,\mathrm a)$, $(1,\mathrm c)$.

- (a) Xác định mục thứ tư.
- (b) Hoàn tất dãy mục tới hết chuỗi và đếm số mục của mỗi dạng.
:::

::: hint
Sau ba mục đầu, $p=3$ và lịch sử là $x[1..3]=$ `aac`; thử $d=1,2,3$.
:::

::: solution
**Câu (a).** Tại $p=3$, cận là $\min(4,15-3)=4$. Với $d=1$, $x_4=\mathrm a$ khác $x_3=\mathrm c$, nên $\ell(1)=0$. Với $d=2$, $x_4$ khớp $x_2$ nhưng $x_5=\mathrm a$ khác $x_3$, nên $\ell(2)=1$. Với $d=3$, $x[4..7]=$ `aaca` khớp $x[1..4]$, nên $\ell(3)=4$; ô nguồn $x_4$ nằm ngay trong đoạn đang mã. Độ khớp $4\ge3$, nên mục thứ tư là $(0,3,4)$ và con trỏ lên $p=7$.

**Câu (b).** Các mục tiếp theo:

| $p$ | Độ khớp lớn nhất | Mục | $p$ mới |
|---|---|---|---|
| 7 | 0: $x_8=\mathrm b$ không có trong lịch sử $x[2..7]=$ `acaaca` | $(1,\mathrm b)$ | 8 |
| 8 | 3 với $d=3$: $x[9..11]=$ `cab` khớp $x[6..8]$; $\ell(6)=2$, các $d$ khác cho 0 | $(0,3,3)$ | 11 |
| 11 | 1, với $d=2$ và $d=5$ | $(1,\mathrm a)$ | 12 |
| 12 | 2 với $d=1$: $x_{13}x_{14}=$ `aa` khớp $x_{12}x_{13}$, $x_{15}=\mathrm c$ khác $x_{14}$ | $(1,\mathrm a)$ | 13 |
| 13 | 1, với $d=1,2,4$ | $(1,\mathrm a)$ | 14 |
| 14 | 1 với $d=6$, cận $\min(4,1)=1$ | $(1,\mathrm c)$ | 15 |

Dãy gồm 10 mục: $(1,\mathrm a)$, $(1,\mathrm a)$, $(1,\mathrm c)$, $(0,3,4)$, $(1,\mathrm b)$, $(0,3,3)$, $(1,\mathrm a)$, $(1,\mathrm a)$, $(1,\mathrm a)$, $(1,\mathrm c)$. Có 2 mục dạng thứ nhất và 8 mục dạng thứ hai. Tại $p=12$, độ khớp 2 nhỏ hơn ngưỡng 3, nên bộ mã hóa ghi ký tự rời.

**Kiểm tra lại.** Các mục phủ $4+3+8\cdot1=15=n$ ký tự. Hai mục dạng thứ nhất có $1\le d\le p$ và thỏa điều kiện khớp $x_{p+j}=x_{p+j-d}$ với $j=1,\ldots,\ell$, đúng hai điều kiện mà chứng minh Bổ đề 11.7 dùng, nên chép tuần tự cho lại đúng hai đoạn. Cùng tám ký tự rời, bộ giải mã dựng lại đúng $x$.
:::

::: exercise Bài tập 11.15 (Hoàn tất vết LZ78; CMU 15-499, compression3-lz.pdf, trang chiếu 13)
Chuỗi $x=$ `aabaacabcabcb`, $n=13$, được mã hóa bằng Thuật toán 11.13. Bốn cặp đầu là $(0,\mathrm a)$, $(1,\mathrm b)$, $(1,\mathrm a)$, $(0,\mathrm c)$; chúng mô tả $x[1..6]=$ `aabaac`.

- (a) Lập vết bước 2 của thuật toán từ $x_7$ tới hết chuỗi: với mỗi ký tự đọc, ghi nút hiện tại, kết quả phép tra con ở bước 2.1 và cặp phát ra ở bước 2.2, nếu có.
- (b) Liệt kê mọi mục của từ điển sau cặp cuối và vẽ cây từ điển, ghi nhãn cạnh.
- (c) Giải mã toàn bộ dãy cặp, gồm bốn cặp đầu và các cặp ở câu (a), bằng Thuật toán 11.14 và kiểm tra kết luận (a) của Định lý 11.15 sau mỗi cặp.
:::

::: hint
Cặp thứ $t$ thêm nút $t$ dưới nút $i_t$ qua cạnh $c_t$ (Định nghĩa 11.11). Dựng cây sau bốn cặp đầu, rồi từ $x_7$ đi xuống từ gốc.
:::

::: solution
**Câu (a).** Bốn cặp đầu thêm nút 1 = `a` dưới gốc qua cạnh $\mathrm a$, nút 2 = `ab` dưới nút 1 qua $\mathrm b$, nút 3 = `aa` dưới nút 1 qua $\mathrm a$, nút 4 = `c` dưới gốc qua $\mathrm c$. Sau cặp $(0,\mathrm c)$, nút hiện tại là gốc 0. Từ $x_7$:

| Ký tự đọc | Nút hiện tại | Kết quả tra con | Bước, cặp phát |
|---|---|---|---|
| $x_7=\mathrm a$ | 0 | nút 1 | 2.1: $i\leftarrow1$ |
| $x_8=\mathrm b$ | 1 | nút 2 | 2.1: $i\leftarrow2$ |
| $x_9=\mathrm c$ | 2 | không có | 2.2: phát $(2,\mathrm c)$, thêm nút 5 = `abc` dưới nút 2 qua $\mathrm c$, $i\leftarrow0$ |
| $x_{10}=\mathrm a$ | 0 | nút 1 | 2.1: $i\leftarrow1$ |
| $x_{11}=\mathrm b$ | 1 | nút 2 | 2.1: $i\leftarrow2$ |
| $x_{12}=\mathrm c$ | 2 | nút 5 | 2.1: $i\leftarrow5$ |
| $x_{13}=\mathrm b$ | 5 | không có | 2.2: phát $(5,\mathrm b)$, thêm nút 6 = `abcb` dưới nút 5 qua $\mathrm b$, $i\leftarrow0$ |

Chuỗi hết với $i=0$, nên bước 3 không phát cặp `EOS`; vết phát hai cặp $(2,\mathrm c)$ và $(5,\mathrm b)$.

**Câu (b).** Từ điển có bảy mục: $D[0]$ rỗng, $D[1]=$ `a`, $D[2]=$ `ab`, $D[3]=$ `aa`, $D[4]=$ `c`, $D[5]=$ `abc`, $D[6]=$ `abcb`. Cây từ điển có gốc 0 và sáu nút:

- gốc 0: cạnh $\mathrm a$ tới nút 1, cạnh $\mathrm c$ tới nút 4;
- nút 1: cạnh $\mathrm a$ tới nút 3, cạnh $\mathrm b$ tới nút 2;
- nút 2: cạnh $\mathrm c$ tới nút 5;
- nút 5: cạnh $\mathrm b$ tới nút 6.

Các nút 3, 4, 6 là lá. Nối nhãn cạnh trên đường từ gốc tới nút 6 được $\mathrm a\,\mathrm b\,\mathrm c\,\mathrm b$, đúng $D[6]$.

**Câu (c).** Thuật toán 11.14 xử lý sáu cặp:

| Cặp | $D'[i_t]$ | Xuất | Mục thêm | Bản giải mã |
|---|---|---|---|---|
| $(0,\mathrm a)$ | rỗng | `a` | 1 = `a` | `a` |
| $(1,\mathrm b)$ | `a` | `ab` | 2 = `ab` | `aab` |
| $(1,\mathrm a)$ | `a` | `aa` | 3 = `aa` | `aabaa` |
| $(0,\mathrm c)$ | rỗng | `c` | 4 = `c` | `aabaac` |
| $(2,\mathrm c)$ | `ab` | `abc` | 5 = `abc` | `aabaacabc` |
| $(5,\mathrm b)$ | `abc` | `abcb` | 6 = `abcb` | `aabaacabcabcb` |

Sau cặp thứ $t$, mỗi phía có $t+1$ mục $D[0],\ldots,D[t]$, và mục bộ giải mã thêm ở cặp $t$ trùng mục bộ mã hóa thêm ở cùng cặp (câu (a) và (b)). Vậy kết luận (a) của Định lý 11.15 đúng sau mỗi cặp $t=1,\ldots,6$; cột cuối cho kết luận (b), $y=x[1..p_t]$.

**Kiểm tra lại.** Sáu cụm dài $1+2+2+1+3+4=13=n$ ký tự và nối lại được $x$. Hai cặp $(2,\mathrm c)$, $(5,\mathrm b)$ và hai mục 5 = `abc`, 6 = `abcb` trùng phần LZ78 của Ví dụ 11.14.
:::

::: exercise Bài tập 11.16 (Mã chưa có trong từ điển của bộ giải mã LZW; CMU 15-499, compression3-lz.pdf, trang chiếu 16)
Dòng mã $k_1,\ldots,k_\tau$ của một chuỗi được tạo bằng Thuật toán 11.19 và giải bằng Thuật toán 11.20; từ điển của hai phía không giới hạn số mục. Đầu vào chứa liền nhau đoạn $\chi\,S\,\chi\,S\,\chi$, với $\chi$ là một ký tự, $S$ là một chuỗi và cụm $\chi\,S$ đã có mã trong từ điển. Bộ mã hóa phát mã $k_t$ của cụm $\chi\,S$ và thêm mục $\chi\,S\,\chi$; ngay sau đó nó phát $k_{t+1}$, mã của chính mục vừa thêm. Bộ giải mã đọc $k_t$ và xuất $\chi\,S$, rồi đọc $k_{t+1}$ và không thấy mã này trong từ điển của mình.

- (a) Xác định $k_{t+1}$ theo $t$ và $\texttt{next\_code}$ của bộ giải mã lúc đọc $k_{t+1}$, rồi giải thích vì sao bộ giải mã chưa có mục $k_{t+1}$.
- (b) Xác định cụm mà bộ giải mã gán cho $k_{t+1}$ và mục nó thêm, chỉ từ cụm $\chi\,S$ vừa xuất, rồi kiểm kết quả bằng Mệnh đề 11.22(b).
:::

::: hint
So mã của mục mà bộ mã hóa thêm khi phát $k_t$ (Bổ đề 11.21(a)) với $\texttt{next\_code}$ của bộ giải mã khi đọc $k_{t+1}$ (Bổ đề 11.21(c)).
:::

::: solution
**Câu (a).** Theo Bổ đề 11.21(a), khi phát $k_t$ bộ mã hóa thêm mục $255+t$. Theo dữ kiện, $k_{t+1}$ là mã của chính mục này, nên $k_{t+1}=255+t$. Theo Bổ đề 11.21(c), khi đọc $k_{t+1}$ bộ giải mã đã thêm $t-1$ mục $256,\ldots,254+t$, và $\texttt{next\_code}=255+t$. Vậy $k_{t+1}=\texttt{next\_code}$. Bộ giải mã chỉ thêm mục $255+t$ sau khi biết ký tự đầu của cụm kế tiếp, mà cụm kế tiếp lại là cụm của chính $k_{t+1}$.

**Câu (b).** Theo Bổ đề 11.21(a), mục $255+t$ là $\chi\,S$ nối với ký tự đầu của cụm kế tiếp. Cụm kế tiếp là chính mục này, nên nó bắt đầu bằng $\chi\,S$ và ký tự đầu của nó là $\chi=\operatorname{first}(\chi\,S)$. Do đó bộ giải mã gán cho $k_{t+1}$ cụm $e=\chi\,S\,\chi$, tức $w\operatorname{first}(w)$ với $w=\chi\,S$ là cụm vừa xuất; đó là nhánh 3.2 của Thuật toán 11.20. Ở bước 3.4, nó thêm mục $w\operatorname{first}(e)=\chi\,S\,\chi$ với mã $255+t$, trùng mục bộ mã hóa đã thêm. Mệnh đề 11.22(b) với $w_t=\chi\,S$ và $k_{t+1}=\texttt{next\_code}=255+t$ cho $w_{t+1}=w_t\operatorname{first}(w_t)=\chi\,S\,\chi$, đúng cụm vừa xác định.

**Kiểm tra lại.** Dòng mã $97,98,256,258$ của Ví dụ 11.8(b) có $t=3$, $\chi=\mathrm a$, $S=$ `b`: $k_4=258=255+3$, bộ giải mã có $\texttt{next\_code}=258$, và cụm gán cho 258 là `aba`. Với $S$ rỗng, đoạn là `aaa`, như hai cụm đầu `a`, `aa` của chuỗi toàn chữ $\mathrm a$ ở Bài tập 11.6, nơi $k_2=256=255+1$.
:::

## Mức vận dụng

::: exercise Bài tập 11.17 (Biến đổi trên toàn ảnh và mã hóa theo khối; CMU 15-499, compression4-lossy.pdf, trang chiếu 11)
Một phép biến đổi tuyến tính dùng để nén ảnh được chọn theo ba mục tiêu:

1. khử tương quan (decorrelate): các điểm ảnh gần nhau có giá trị tương quan, tức giúp đoán nhau, còn các hệ số sau biến đổi không còn tương quan với nhau;
2. làm cho nhiều hệ số có giá trị nhỏ;
3. có những hàm cơ sở (basis function) mà mắt bỏ qua được; với DCT của Định nghĩa 11.26, hàm cơ sở là các mẫu cosine dựng từ các hàng của ma trận $T$, và mỗi hệ số là trọng số của một mẫu.

Dựa trên ba mục tiêu trên và chi phí tính toán, trả lời hai câu sau và dẫn số hiệu các kết quả của ghi chú được dùng.

- (a) Giải thích vì sao áp dụng biến đổi cosine một lần trên toàn bộ ảnh là cách làm kém.
- (b) Nêu cách khắc phục.
:::

::: hint
Mỗi hệ số của phép biến đổi là một tổng trên mọi điểm của vùng biến đổi. So số số hạng khi vùng là cả ảnh $m$ điểm và khi vùng là một khối $8\times8$.
:::

::: solution
**Câu (a).** Gọi $m$ là số điểm của ảnh.

- Mục tiêu 1. Khối lớn hơn có lẽ nén tốt hơn, nhưng lợi giảm nhanh, vì các điểm cách nhau mười lăm, hai mươi vị trí ít giúp đoán nhau: một khối $64\times64$ có thể không nén tốt hơn nhiều so với bốn khối $16\times16$, trong khi thời gian tính tăng nhanh. JPEG chọn khối $8\times8$ để cài đặt được (NG, tr.255). Biến đổi trên cả ảnh vì vậy chỉ thêm được ít lợi so với khối nhỏ.
- Mục tiêu 2. Trên một khối $8\times8$ của ảnh CHEETAH.GS, năng lượng đã dồn vào vài hệ số tần số thấp (Ví dụ 11.10). Vì các điểm xa nhau ít giúp đoán nhau, mở rộng vùng biến đổi ít lợi thêm cho mục tiêu này (NG, tr.255).
- Mục tiêu 3. DCT của mỗi khối $8\times8$ đã có các mẫu cosine tần số cao, là những hàm cơ sở mà mục tiêu này nhắm tới (Định nghĩa 11.26). Bước lượng tử tăng theo tần số (Định nghĩa 11.29) khai thác các mẫu đó ngay trong từng khối, nên biến đổi cả ảnh không thêm lợi ích cho mục tiêu 3.
- Chi phí và bộ nhớ. Theo định nghĩa trực tiếp, mỗi hệ số là tổng trên mọi điểm của vùng (Định nghĩa 11.26, với vùng $8\times8$). Trên cả ảnh có $m$ hệ số, mỗi hệ số $m$ số hạng, tổng $m^2$ số hạng. Chia ảnh thành $m/64$ khối $8\times8$, tổng là $(m/64)\cdot64\cdot64=64m$ số hạng, ít hơn $m/64$ lần. Với ảnh CHEETAH.GS, $m=64\,000$: $m^2\approx4{,}1\cdot10^9$ số hạng so với $64m\approx4{,}1\cdot10^6$ số hạng. Phép biến đổi trên cả ảnh còn phải giữ cả $m$ điểm trong bộ nhớ, còn Thuật toán 11.34 chỉ giữ một dải $8\times m_{\mathrm w}$ điểm, với CHEETAH.GS là $8\cdot320=2\,560$ điểm.

Vậy biến đổi trên cả ảnh chỉ lợi ít về ba mục tiêu, nhưng tốn gấp $m/64$ lần số số hạng và phải giữ cả ảnh trong bộ nhớ.

**Câu (b).** Chia ảnh thành các khối $8\times8$ và biến đổi cosine từng khối, tức mã hóa theo khối (block coding), như Thuật toán 11.34 với DCT của Định nghĩa 11.26.

- Mục tiêu 1. Hai điểm cùng khối cách nhau không quá 7 vị trí theo mỗi chiều, gần hơn khoảng mười lăm, hai mươi vị trí mà ở đó các điểm ít giúp đoán nhau (NG, tr.255).
- Mục tiêu 2. Trên khối của ảnh CHEETAH.GS ở Ví dụ 11.10, hệ số DC chiếm khoảng $80\%$ năng lượng, sáu hệ số có $u+v\le2$ chiếm khoảng $85\%$, còn 28 hệ số có $u+v\ge8$ chỉ chiếm khoảng $4{,}4\%$. DCT bảo toàn năng lượng (Mệnh đề 11.28(c)), nên bỏ 28 hệ số đó chỉ làm mất khoảng $4{,}4\%$ năng lượng của khối.
- Mục tiêu 3. Trong mỗi khối, bước lượng tử $Q_{uv}=1+(1+u+v)q$ tăng theo tần số (Định nghĩa 11.29), nên hệ số của các mẫu cosine tần số cao bị chia cho bước lớn và phần lớn về 0. Với $q=2$, khối ở Ví dụ 11.11 còn 30 hệ số khác 0 trong 64, và hàng cuối toàn số 0. Sai số của mỗi khối bị chặn bởi $\beta(q)$ (Định lý 11.31). Trên phần lớn năm ảnh xám của NG, $q\le5$ chỉ làm giảm nhẹ độ nét (Nhận xét 11.35).
- Chi phí và bộ nhớ. DCT tốn $1\,024$ phép nhân mỗi khối và $\Theta(m)$ cho cả ảnh, với bộ nhớ một dải $8\times m_{\mathrm w}$ điểm (Thuật toán 11.34).

Đổi lại, khi $q>5$ ảnh bắt đầu lộ hiện tượng khối, tức đường biên giữa các khối $8\times8$ nhìn thấy được (Nhận xét 11.35).

**Kiểm tra lại.** $m^2/(64m)=m/64=1\,000$ khi $m=64\,000$, đúng bằng số khối $40\cdot25$ của CHEETAH.GS. Ở Ví dụ 11.10, $34\,596/43\,333\approx0{,}80$ và $1\,925/43\,333\approx0{,}044$.
:::
