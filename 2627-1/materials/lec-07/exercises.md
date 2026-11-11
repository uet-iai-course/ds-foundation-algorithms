# Bài tập Bài 07 — Chỉ mục hàng xóm gần đúng

Các bài tập củng cố 07.15–07.19 dưới đây lấy từ bài giảng 8 (class 8) của học phần Princeton COS 597A *Vector Search* (viết tắt P8), và từ sổ thực hành `class-08-runbook-for-students.ipynb` đi kèm (gọi tắt là sổ, ô đánh số từ 0), kèm gợi ý và lời giải. Mọi số hiệu Định nghĩa, Định lý, Mệnh đề, Bổ đề, Hệ quả, Nhận xét, Thuật toán, Ví dụ và Tình huống 07.k là của [ghi chú Bài 07](material-viewer.html?doc=materials/lec-07/lecture-note.md&deck=lecture-07-chi-muc-hang-xom-gan-dung.html), nơi Bài tập 07.1–07.14 đứng ngay sau các mục; ký hiệu dùng như trong bảng ký hiệu của ghi chú. Ba nhiệm vụ chạy mã, Bài tập 07.17–07.19, là bài tập trên lớp (recitation) của [bộ trang chiếu Bài 07](lecture-07-chi-muc-hang-xom-gan-dung.html).

## Mục tiêu và bài tập

| Mục tiêu học tập của ghi chú | Bài tập trong ghi chú | Bài tập trong tệp này |
|---|---|---|
| 1. Tìm đúng, tìm gần đúng, độ thu hồi, hai nguồn thiếu điểm (Mục 1) | 07.1, 07.2, 07.3, 07.13 | 07.19 |
| 2. Tìm kiếm tham lam, tìm kiếm chùm, `SEARCH-LAYER` (Mục 2) | 07.4, 07.5 | — |
| 3. Truy vấn và chèn HNSW, phân phối tầng, bộ nhớ (Mục 3) | 07.6, 07.7 | — |
| 4. Lượng tử hóa véc-tơ, lượng tử hóa tích, bảng tra, cận sai số (Mục 4) | 07.8, 07.9, 07.10 | 07.15, 07.17, 07.18 |
| 5. Truy vấn IVF-PQ và chi phí (Mục 5) | 07.11, 07.12, 07.13 | 07.16, 07.19 |
| 6. So sánh bốn cấu trúc và chọn chỉ mục (Mục 6) | 07.14 | — |

## Mức nhận biết

::: exercise Bài tập 07.15 (Tái dựng véc-tơ thứ 123 từ mã PQ; sổ, ô mã 83–97, nhiệm vụ ô mã 96)
Sổ tạo lượng tử hóa tích `pq = faiss.ProductQuantizer(d, 4, 8)` với $D=d=64$, $m=4$ và 8 bit mỗi chỉ số (ô mã 83), học nó trên tập huấn luyện (ô mã 85), tính mã của $10^4$ véc-tơ kho `xb_codes = pq.compute_codes(xb)` (ô mã 86) và giải mã `pq_reconstruction = pq.decode(xb_codes)` (ô mã 87). Ô mã 92 lấy các bộ mã con `pq_centroids = get_pq_centroids(pq)`, với bố cục (số đoạn, số tâm mỗi đoạn, số chiều mỗi đoạn) theo ô mã 94. Ô mã 96 để trống vế phải:

```python
# reconstruct vector no 123 -- TODO implement the re-construction!
xb123_recons =
```

và ô mã 97 kiểm `np.all(pq_reconstruction[123] == xb123_recons)`.

- (a) Viết vế phải của ô mã 96 theo Định nghĩa 07.27, không gọi `decode`.
- (b) Giải thích vì sao ô mã 97 in `True` với phép so bằng nhau chính xác.
:::

::: hint
Phần tử `xb_codes[123, j]` là chỉ số tâm con của đoạn thứ $j+1$ trong mã của véc-tơ 123 (biến `j` của mã đếm từ 0).
:::

::: solution
**Câu (a).** `xb123_recons = np.hstack([pq_centroids[j, xb_codes[123, j]] for j in range(pq.M)])`. Với mỗi `j`, biểu thức lấy tâm con có chỉ số `xb_codes[123, j]` trong bộ mã con của đoạn thứ $j+1$, rồi ghép bốn tâm con theo thứ tự đoạn, đúng $\widehat x=\big(c^{(1)}_{i_1}\mid\cdots\mid c^{(4)}_{i_4}\big)$ của Định nghĩa 07.27; `np.concatenate` cho cùng kết quả.

**Câu (b).** Véc-tơ tái dựng của lượng tử hóa tích là phép ghép các tâm con (P8, tr.31), nên `decode` chép nguyên các số thực của tâm con, không qua phép tính nào. Hai mảng gồm cùng các số thực ở cùng vị trí, nên phép so bằng nhau chính xác đúng ở mọi tọa độ.

**Kiểm tra lại.** Kết quả có $4\cdot16=64$ tọa độ, bằng $D$. Ghép sai thứ tự đoạn đặt tâm con của đoạn này vào tọa độ của đoạn khác, và ô mã 97 in `False`.
:::

## Mức tính toán hoặc chứng minh

::: exercise Bài tập 07.16 (Số tâm thô tối ưu khi cố định $\mathit{nprobe}$; P8, tr.22; sổ, ô mã 49–50)
Theo P8 (tr.22), với tệp đảo $k_c$ tâm thô trên kho $N$ véc-tơ, bước lượng tử hóa thô tốn $k_c$ phép tính khoảng cách, và khi các danh sách cân bằng, bước quét tốn $\mathit{nprobe}\cdot N/k_c$ phép tính khoảng cách; P8 viết $k$, $n$ cho $k_c$, $N$. Trang chiếu đặt bài tập: tìm $k_c$ tối ưu như một hàm của $N$ khi cố định $\mathit{nprobe}$. Ô mã 50 vẽ tổng chi phí

$$
g(k_c)=k_c+\frac{\mathit{nprobe}\cdot N}{k_c}
$$

với $\mathit{nprobe}=15$, $k_c\in\{64,256,1024,4096\}$ và $N=2^{10},2^{11},\ldots,2^{24}$.

- (a) Với $\mathit{nprobe}$ và $N$ cố định, coi $k_c$ là số thực dương; tìm $k_c^{\mathrm{opt}}$ làm $g$ nhỏ nhất và giá trị $g(k_c^{\mathrm{opt}})$.
- (b) Với $\mathit{nprobe}=15$ và $N=2^{20}$, tính $k_c^{\mathrm{opt}}$, $g(k_c^{\mathrm{opt}})$ và $g$ tại bốn giá trị $k_c$ của ô mã 50; xác định giá trị tốt nhất trong bốn giá trị đó.
- (c) Với hai giá trị liền nhau $k_c$ và $4k_c$ của ô mã 50, tìm $N$ tại đó hai chi phí bằng nhau, rồi xác định khoảng $N$ mà mỗi giá trị là tốt nhất trong bốn giá trị.
:::

::: hint
Với $c>0$, bất đẳng thức giữa trung bình cộng và trung bình nhân cho $k_c+c/k_c\ge2\sqrt c$.
:::

::: solution
**Câu (a).** Đặt $c=\mathit{nprobe}\cdot N>0$. Với mọi $k_c>0$, $k_c+c/k_c-2\sqrt c=(\sqrt{k_c}-\sqrt{c/k_c})^2\ge0$, dấu bằng khi và chỉ khi $k_c=c/k_c$. Do đó

$$
\begin{aligned}
k_c^{\mathrm{opt}}&=\sqrt{\mathit{nprobe}\cdot N},\\
g(k_c^{\mathrm{opt}})&=2\sqrt{\mathit{nprobe}\cdot N}.
\end{aligned}
$$

Tại $k_c^{\mathrm{opt}}$, chi phí lượng tử hóa thô bằng chi phí quét.

**Câu (b).** $k_c^{\mathrm{opt}}=\sqrt{15\cdot2^{20}}=1024\sqrt{15}\approx3\,965{,}9$ và $g(k_c^{\mathrm{opt}})\approx7\,931{,}9$. Tại bốn giá trị của ô mã 50:

| $k_c$ | $15\cdot2^{20}/k_c$ | $g(k_c)$ |
|---|---|---|
| 64 | $245\,760$ | $245\,824$ |
| 256 | $61\,440$ | $61\,696$ |
| 1024 | $15\,360$ | $16\,384$ |
| 4096 | $3\,840$ | $7\,936$ |

Giá trị tốt nhất là $k_c=4096$, gần $k_c^{\mathrm{opt}}$ nhất.

**Câu (c).** $g(k_c)=g(4k_c)$ khi $k_c+c/k_c=4k_c+c/(4k_c)$, tức $c=4k_c^2$, hay $N=4k_c^2/15$: $1\,092{,}3$ giữa 64 và 256; $17\,476{,}3$ giữa 256 và 1024; $279\,620{,}3$ giữa 1024 và 4096. Trong dải $N$ của ô mã 50, $k_c=64$ tốt nhất khi $N\le1\,092$, $k_c=256$ khi $1\,092\le N\le17\,476$, $k_c=1024$ khi $17\,476\le N\le279\,620$, và $k_c=4096$ khi $N\ge279\,620$.

**Kiểm tra lại.** $N=2^{20}\approx1{,}05\cdot10^6>279\,620$, khớp Câu (b); $g(4096)-g(k_c^{\mathrm{opt}})\approx4{,}1$. Với dữ kiện của Tình huống 07.2 ($N=10^4$, $\mathit{nprobe}=13$), $k_c^{\mathrm{opt}}=\sqrt{1{,}3\cdot10^5}\approx361$, nhỏ hơn nhiều $k_c=4096$ của sổ.
:::

## Mức vận dụng (thực hành)

Ba nhiệm vụ dưới đây chạy sổ của P8 với Python, NumPy, Matplotlib và Faiss bản CPU. Ô mã 1 đặt 32 luồng theo máy của tác giả sổ; đặt lại theo máy đang dùng, và ghi phiên bản Faiss, số luồng, phần cứng cùng kết quả, vì các số đo thời gian phụ thuộc chúng. Trước mỗi nhiệm vụ, chạy các ô mã 0–4, 17 và 21–24. Ô mã 2 tạo dữ liệu tổng hợp `SyntheticDataset(64, 1000_000, 10000, 100)`, và ô mã 21 tính tập đúng bằng quét đầy đủ (Thuật toán 07.2):

| Mảng | Kích thước | Vai trò |
|---|---|---|
| `xt` | $10^6\times64$ | tập huấn luyện bộ mã |
| `xb` | $10^4\times64$ | kho, $N=10^4$, $D=64$ |
| `xq` | $100\times64$ | truy vấn |
| `gt` | $100\times10$ | chỉ số của $\mathcal N_{10}(q)$ cho mỗi truy vấn |

Trong Faiss, số đoạn $m$ gọi là `M` (khác $M$ của HNSW) và số bit mỗi chỉ số $\log_2k^*$ gọi là `nbits`. Lời giải cho các đại lượng suy ra từ cấu hình; MSE, thời gian và `nok` là số đo của máy chạy.

::: exercise Bài tập 07.17 (Mã PQ trên dữ liệu tổng hợp; sổ, ô mã 82–95)
Ô mã 83 tạo `pq = faiss.ProductQuantizer(d, 4, 8)`, tức $D=64$, $m=4$, $\log_2k^*=8$.

- (a) Trước khi chạy, dự đoán `pq.code_size` (byte, ô mã 84), `pq_centroids.shape` (ô mã 93) và `xb_codes.shape` (ô mã 86); chạy ô mã 83–95 rồi đối chiếu.
- (b) Ghi MSE mà ô mã 88 in ra. Ô mã 89 ghi rằng MSE này tốt hơn MSE của lượng tử hóa véc-tơ 4096 tâm (mã 12 bit) học bằng k-means ở ô mã 6–7; so độ dài mã, số véc-tơ tái dựng khác nhau và số thực trong bộ mã của hai cách theo Mệnh đề 07.28(c).
:::

::: hint
Theo Mệnh đề 07.28(c), mã dài $m\log_2k^*$ bit; bố cục của `pq_centroids` là (số đoạn, số tâm mỗi đoạn, số chiều mỗi đoạn).
:::

::: solution
**Câu (a).** `code_size` $=4\cdot8/8=4$ byte; `pq_centroids.shape` $=(m,k^*,D/m)=(4,256,16)$; `xb_codes.shape` $=(N,\texttt{code\_size})=(10\,000,4)$, phần tử `xb_codes[i, j]` là chỉ số tâm con của đoạn thứ $j+1$ của véc-tơ $i$.

**Câu (b).** Lượng tử hóa tích $4\times8$: mã 32 bit, $256^4=2^{32}$ véc-tơ tái dựng, bộ mã con $4\cdot256\cdot16=16\,384$ số. Lượng tử hóa véc-tơ 4096 tâm: mã 12 bit, $4096$ véc-tơ tái dựng, bộ mã $4096\cdot64=262\,144$ số. Lượng tử hóa tích dùng mã dài gần gấp ba và có nhiều véc-tơ tái dựng hơn $2^{20}$ lần với bộ mã nhỏ hơn 16 lần; nhiều véc-tơ tái dựng hơn cho phép véc-tơ tái dựng gần véc-tơ gốc hơn, phù hợp nhận định của ô mã 89. Phép so không cùng độ dài mã, nên không cho biết cách nào tốt hơn ở cùng ngân sách bit; Bài tập 07.18 xét câu hỏi đó.

**Kiểm tra lại.** `code_size` nhân $N$ cho $40\,000$ byte cho cả kho, so với $10^4\cdot64\cdot4=2\,560\,000$ byte của `xb`, tỷ lệ 64.
:::

::: exercise Bài tập 07.18 (Ba cấu hình cùng ngân sách 6 byte; sổ, ô mã 98–99; P8, tr.33)
Ô mã 99 giữ ngân sách 6 byte, tức 48 bit, mỗi véc-tơ và thử $m\in\{4,8,16\}$ với `nbits` $=48/m$. Với mỗi cấu hình, ô in `dsub`, `ksub`, `code_size`, học bộ mã, đo thời gian mã hóa cộng giải mã `xb`, rồi in MSE.

- (a) Trước khi chạy, dự đoán `dsub` $=D/m$, `ksub` $=k^*$ và `code_size` của ba cấu hình.
- (b) Chạy ô mã 99, ghi MSE và thời gian; xếp hạng ba cấu hình theo từng đại lượng.
- (c) Giải thích thứ hạng thời gian bằng chi phí mã hóa của Mệnh đề 07.28(c), và so thứ hạng MSE với nhận định của P8 (tr.33) cho cùng độ dài mã.
:::

::: hint
Với $D=64$, chi phí mã hóa một véc-tơ là $k^*D$ phép toán trên tọa độ; giải mã chỉ chép tâm con.
:::

::: solution
**Câu (a).**

| $m$ | `nbits` | `dsub` | `ksub` | `code_size` |
|---|---|---|---|---|
| 4 | 12 | 16 | 4096 | 6 |
| 8 | 6 | 8 | 64 | 6 |
| 16 | 3 | 4 | 8 | 6 |

**Câu (b).** Thứ hạng lấy từ ba cặp (MSE, thời gian) in ra.

**Câu (c).** Mã hóa tốn $k^*D=262\,144$; $4\,096$; $512$ phép toán mỗi véc-tơ cho $m=4,8,16$, nên với cùng phần cứng, cấu hình $4\times12$ mã hóa chậm nhất; giải mã chỉ chép $m$ tâm con, chi phí $\Theta(D)$ cho cả ba. P8 (tr.33) ghi rằng với cùng độ dài mã, $k^*$ lớn hơn và $m$ nhỏ hơn cho độ chính xác cao hơn nhưng bảng tâm lớn hơn và chậm hơn, với đầu mút $m=1$ là k-means trên cả véc-tơ; nhận định này dự đoán $4\times12$ có MSE nhỏ nhất.

**Kiểm tra lại.** $m\log_2k^*=4\cdot12=8\cdot6=16\cdot3=48$ bit ở cả ba dòng; tỷ lệ chi phí mã hóa giữa hai dòng liền nhau là $64$ và $8$.
:::

::: exercise Bài tập 07.19 (Chỉ mục IVF-PQ; sổ, ô mã 148–155)
Ô mã 149–151 xây chỉ mục:

```python
index = faiss.index_factory(d, "IVF200,PQ16x8np")   # ô mã 149
index.train(xt)                                     # ô mã 150
index.add(xb)                                       # ô mã 151
```

Ô mã 155 chạy với $\mathit{nprobe}\in\{2,5,10,20,50\}$:

```python
for nprobe in 2, 5, 10, 20, 50:
    index.nprobe = nprobe
    t0 = time.time()
    for _ in range(50):
        D, I = index.search(xq, 10)
    t1 = time.time()
    nok = (I[:, 0] == gt[:, 0]).sum()
    print(f"{nprobe=:} {nok=:} {(t1 - t0)*1000:.3f} ms")
```

Hậu tố `np` của chuỗi cấu hình tắt bước huấn luyện *mã đa nghĩa* (polysemous codes); nó không phải giá trị $\mathit{nprobe}$.

- (a) Từ chuỗi cấu hình và dữ liệu, xác định $k_c$, $m$, số bit mỗi chỉ số, số byte mã mỗi véc-tơ và cỡ danh sách trung bình; nêu việc ô mã 150 và ô mã 151 làm theo Định nghĩa 07.34 và Mệnh đề 07.35.
- (b) Chạy ô mã 149–155 và điền bảng: $\mathit{nprobe}$; `nok/100`; tổng mili giây; mili giây trung bình mỗi truy vấn trong lô; số mã được chấm khi danh sách cân bằng.
- (c) Vẽ `nok/100` theo thời gian trung bình mỗi truy vấn; so xu hướng thời gian với dự đoán của Mệnh đề 07.37(a) và xét xem `nok/100` có nhất thiết tăng theo $\mathit{nprobe}$ không.
:::

::: hint
`nok/100` là $\overline{\operatorname{recall@}1}$ (Nhận xét 07.5); vòng lặp trong của ô mã 155 chạy 50 lượt, mỗi lượt 100 truy vấn.
:::

::: solution
**Câu (a).** `IVF200` cho $k_c=200$; `PQ16x8` cho $m=16$, 8 bit mỗi chỉ số, mã 16 byte cho phần dư mỗi véc-tơ; cỡ danh sách trung bình $N/k_c=10^4/200=50$. Ô mã 150 học 200 tâm thô và lượng tử hóa tích của phần dư trên `xt`; ô mã 151 gán mỗi véc-tơ của `xb` vào danh sách của tâm thô gần nhất và lưu mã phần dư.

**Câu (b).** Cột số mã được chấm là $50\,\mathit{nprobe}$: $100$; $250$; $500$; $1\,000$; $2\,500$. Thời gian trung bình mỗi truy vấn bằng tổng mili giây chia $50\cdot100=5\,000$; đây là thời gian trung bình khi chạy theo lô với nhiều luồng, không là độ trễ của một truy vấn đơn lẻ.

**Câu (c).** Mô hình của Mệnh đề 07.37(a) dự đoán mỗi truy vấn tốn $k_cD=12\,800$ cho tâm thô, $\mathit{nprobe}\cdot k^*D=16\,384\,\mathit{nprobe}$ cho bảng tra và $16\cdot50\,\mathit{nprobe}=800\,\mathit{nprobe}$ lần tra khi danh sách cân bằng, tức thời gian tăng gần tuyến tính theo $\mathit{nprobe}$. Khi $\mathit{nprobe}$ tăng, tập $S$ chỉ lớn thêm, nên một hàng xóm gần nhất đã thuộc $S$ không rời $S$, và số truy vấn thiếu vì Mệnh đề 07.7(b) không tăng. Tuy nhiên, một mã mới được chấm có thể có $\widetilde d$ nhỏ hơn hàng xóm gần nhất và chiếm vị trí đầu, nên `nok/100` không nhất thiết tăng theo $\mathit{nprobe}$.

**Kiểm tra lại.** Với $\mathit{nprobe}=50$, chỉ mục mở $50/200=25\%$ số danh sách và chấm khoảng $2\,500$ trên $10^4$ mã. Cột số mã chỉ đúng khi danh sách cân bằng; Tình huống 07.2 cho thấy trên cùng loại dữ liệu, danh sách được mở lớn hơn danh sách trung bình khoảng $3{,}3$ lần ($106/13$ so với $10^4/4096$).
:::
