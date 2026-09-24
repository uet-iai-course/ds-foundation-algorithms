# Thực hành 04 — PageRank theo chủ đề, TrustRank và HITS

> **Thời lượng:** 60 phút. **Yêu cầu trước:** Python 3 (chỉ thư viện chuẩn),
> kiến thức đồ thị có hướng và nội dung Bài 03. Chạy cục bộ, không cần cài
> thêm gói, không cần mạng.

## Tài liệu mở kèm

- Ghi chú bài giảng: [Ghi chú bài giảng](material-viewer.html?doc=materials/lec-04/lecture-note.md&deck=lecture-04-pagerank-theo-chu-de-lien-ket-rac-va-hits.html)
- Bộ trang chiếu: [Bộ trang chiếu](lecture-04-pagerank-theo-chu-de-lien-ket-rac-va-hits.html)

## Chuẩn bị (5 phút)

Mở các liên kết bên dưới, lưu tệp theo đúng tên vào **một thư mục chung**, rồi mở cửa sổ lệnh tại thư mục đó:

| Tệp | Nhãn | Vai trò |
|---|---|---|
| [link_analysis.py](materials/lec-04/code/link_analysis.py) | mã tham chiếu | có đáp án, dùng để đối chiếu |
| [hits_student.py](materials/lec-04/code/hits_student.py) | khung cần hoàn thiện | sinh viên tự cài `hits_step` |
| [check_practice.py](materials/lec-04/code/check_practice.py) | kiểm tự chạy | kiểm mã tham chiếu và khung sinh viên |
| [practice-README.md](materials/lec-04/code/practice-README.md) | hướng dẫn chung | bản đồ tệp, lệnh chạy, số đối chiếu |

Mã tham chiếu **đã có đáp án**: hãy hoàn thiện khung trước, rồi mới đối chiếu.
Kiểm tra môi trường:

```bash
python3 --version
```

## Lộ trình 60 phút

| Bài | Nội dung | Thời gian |
|---|---|---|
| — | Chuẩn bị | 5 phút |
| 1 | PageRank theo chủ đề (MMDS 5.3.1) | 15 phút |
| 2 | TrustRank và khối lượng rác (MMDS 5.4.2) | 15 phút |
| 3 | HITS (MMDS 5.5.1) | 20 phút |
| — | Nộp bài | 5 phút |

Đồ thị dùng chung **G4** (MMDS Hình 5.1 và 5.15): $A \to [B,C,D]$,
$B \to [A,D]$, $C \to [A]$, $D \to [B,C]$. Đồ thị **G5** (Hình 5.18, thay
$C\to A$ bằng $C\to E$, $E$ không có cạnh ra) **chỉ dùng để đối chiếu ví dụ
HITS 5.14**, không thay đề G4 của bài này.

---

## Đọc kết quả chương trình

Chương trình in dữ liệu JSON: `graph` ghi tên đồ thị, `order` ghi thứ tự nút;
`params` chứa các tham số của lệnh; `results` chứa vector điểm, số vòng,
`delta` và cờ `converged`. Nếu đã đọc JSON vào biến `payload` trong Python,
vector PageRank nằm ở `payload["results"]["rank"]`.

## Bài 1 — PageRank theo chủ đề (MMDS 5.3.1, tr.199/PDF25)

**Đề (dịch từ nguồn).** Với đồ thị G4 và tập hạt giống $S$, tính PageRank
theo chủ đề (topic-sensitive PageRank) với $\beta = 4/5$ (như Ví dụ 5.10) cho
hai trường hợp: $S = \{A\}$ và $S = \{A, C\}$.

### Dữ kiện cần để làm độc lập

- Phương trình điểm bất động (MMDS §5.3.2), với $P$ là ma trận **cột-nguồn**
  (mỗi cột tổng 1):

$$r = \beta\, P\, r + (1-\beta)\, q_S$$

- $\beta$ là **hệ số theo liên kết**; phần $1-\beta$ là **phần dịch chuyển**,
  phân bố trên $S$ qua $q_S$.
- $q_S$ là phân bố đều trên $S$: $q_S(v) = 1/|S|$ nếu $v \in S$, ngược lại $0$.
- Khối lượng của nút cụt (không có cạnh ra) được bù đều cho mọi nút (G4 không
  có nút cụt).
- Cấu hình $\beta=4/5$, khởi tạo $r_0=q_S$, ngưỡng $10^{-12}$ và tối đa 1000
  vòng là cách triển khai của môn học.

### Nhiệm vụ lập trình (do môn biên soạn)

Trước khi chạy, viết ra giấy: $q_S$ cho từng trường hợp và **một phương trình
tọa độ** (ví dụ tại $A$) của $r=\beta Pr+(1-\beta)q_S$, để giải thích vì sao
hai tập hạt giống cho hai nghiệm khác nhau.

Sau đó chạy chương trình dòng lệnh với hai bộ hạt giống:

```bash
python3 link_analysis.py topic --graph g4 --seeds A --beta 0.8 --tol 1e-12 --max-iter 1000
python3 link_analysis.py topic --graph g4 --seeds A C --beta 0.8 --tol 1e-12 --max-iter 1000
```

Kiểm tra bốn điểm trên kết quả in ra:

1. Tổng $r$ bằng 1 theo dung sai: `abs(sum(r.values()) - 1) <= 1e-10`
   (không đòi bằng đúng).
2. Mọi thành phần không âm.
3. Trường `converged` là `true`.
4. `delta` (chênh $L_1$ giữa hai vector liên tiếp) nhỏ hơn hoặc bằng `tol`.

So số float với phân số bằng dung sai `1e-10`, ví dụ
`abs(r["A"] - 3/7) <= 1e-10`. Kết quả lặp chỉ là **xấp xỉ** nghiệm, không đòi
hỏi bằng đúng phân số.

### Sản phẩm

Hai dòng kết quả trong `report.md`: mỗi dòng ghi hạt giống, vector $r$ (4 số),
số vòng lặp, `converged`.

### Tiêu chí đạt

- [ ] Cả hai lệnh chạy không lỗi, `converged: true`.
- [ ] Vector xấp xỉ nghiệm phân số trong dung sai `1e-10`.
- [ ] Tổng bằng 1 (dung sai `1e-10`) và không có thành phần âm.

::: hint
Phần dịch chuyển mỗi vòng có khối lượng toàn cục $1-\beta$, được phân bố theo
$q_S(v)$ — **không** phải mỗi nút giữ riêng phần hạng của chính nó. Nút cụt
(không có ở G4) sẽ được bù đều. Không đồng nhất `tol` với sai số tới nghiệm:
`tol` chỉ đo độ thay đổi liên tiếp giữa hai vòng, nghiệm xấp xỉ có thể lệch
nhiều hơn `tol`.
:::

::: solution
Với $S=\{A\}$: $q_S = (1,0,0,0)$, lặp hội tụ về $r = (3/7, 4/21, 4/21, 4/21)$.
Với $S=\{A,C\}$: $q_S = (1/2, 0, 1/2, 0)$, nghiệm
$r = (27/70, 6/35, 19/70, 6/35)$. Kiểm tổng: $27/70 + 12/70 + 19/70 + 12/70 = 1$.
So sánh bằng Python:

```python
r = {"A": 27/70, "B": 6/35, "C": 19/70, "D": 6/35}
assert abs(sum(r.values()) - 1) <= 1e-10
```
:::

---

## Bài 2 — TrustRank và khối lượng rác (MMDS 5.4.2, tr.204/PDF30)

**Đề (dịch từ nguồn).** Đề gồm hai phần: (a) tính TrustRank trên G4 với duy
nhất hạt giống tin cậy $B$; (b) tính khối lượng rác (spam mass) của mỗi nút
từ PageRank nền và TrustRank.

### Dữ kiện cần để làm độc lập

- **PageRank nền** của đề nguồn là PageRank với $\beta = 1$ (không suy giảm
  theo liên kết), lấy từ Ví dụ 5.2 và dùng lại trong Ví dụ 5.12:

$$r = \left(\tfrac{1}{3},\; \tfrac{2}{9},\; \tfrac{2}{9},\; \tfrac{2}{9}\right)$$

- **TrustRank** dùng $\beta = 4/5$, tập tin cậy $T = \{B\}$. Hai quy ước
  $\beta$ khác nhau là quy ước của đề nguồn MMDS; khi ứng dụng so điểm phải
  dùng cùng $\beta$ và bù cụt.
- Khối lượng rác, chỉ tính khi $r(v)>0$ (nếu không tỷ số không xác định):

$$s(v) = \frac{r(v) - t(v)}{r(v)}$$

- $s(B) < 0$ là **hợp lệ**: khối lượng rác âm giữ nguyên giá trị, không phải
  xác suất hay phân loại; ở bài này nó chỉ nói rằng điểm TrustRank của $B$ lớn
  hơn PageRank nền.

### Nhiệm vụ lập trình

Một lệnh duy nhất, in cả PageRank nền, TrustRank và khối lượng rác, kèm
`delta` trong `results`:

```bash
python3 link_analysis.py trust --seeds B --tol 1e-12 --max-iter 1000
```

PageRank nền với $\beta=1$ được lấy từ nguồn. Lệnh trên chỉ lặp TrustRank với $\beta=4/5$ rồi tính khối lượng rác.

### Sản phẩm

Một hàng `report.md`: $t$, $s$, trạng thái `converged`, và một câu giải thích
vì sao $s(B)$ âm.

### Tiêu chí đạt

- `trust_rank` và `spam_mass` khớp lời giải đối chiếu trong dung sai `1e-10`.
- `converged` là `true`, `delta` không vượt ngưỡng đã chọn.
- Giải thích đúng: khối lượng rác âm hợp lệ, không kết luận phân loại.

::: hint
PageRank nền với $\beta=1$ lấy sẵn từ đề nguồn (không chạy lại); chỉ TrustRank được
lặp với $\beta=4/5$ và hạt giống $B$. Khối lượng rác $(r-t)/r$ tính theo từng nút;
giữ giá trị âm nguyên vẹn, không kẹp về 0.
:::

::: solution
Theo thứ tự $(A,B,C,D)$, các vector đối chiếu là

$$t=(198,263,116,158)/735,$$

$$s=\left(\frac{47}{245},-\frac{299}{490},\frac{71}{245},\frac{8}{245}\right).$$

Phép tính tại $B$: $s(B) = \dfrac{2/9 - 263/735}{2/9}$. Quy đồng:
$2/9 = 490/2205$ và $263/735 = 789/2205$, nên

$$s(B) = \frac{490/2205 - 789/2205}{490/2205} = -\frac{299}{490}.$$

Trong bài này, $t_B>r_B$ nên khối lượng rác của $B$ âm. Điều này chỉ là so sánh hai điểm trong bài
tập này, không phải suy luận về xác suất hay khả năng phân loại. Không dùng
một $\beta$ chung cho hai phép tính.
:::

---

## Bài 3 — HITS (MMDS 5.5.1, tr.208/PDF34)

**Đề (dịch từ nguồn).** Tính điểm trung tâm $h$ và điểm thẩm quyền $a$ cho
đồ thị **G4** (Hình 5.1) — đề chỉ yêu cầu tính trên G4, không phải G5 của
Ví dụ 5.14/Hình 5.18.

### Dữ kiện cần để làm độc lập

Một vòng HITS gồm hai nửa với chuẩn hóa **max** (chia cho phần tử lớn nhất),
không chuẩn hóa tổng. Hai cặp công thức riêng biệt:

$$a_{\text{thô}}(v) = \sum_{u:\, u \to v} h_{\text{cũ}}(u), \qquad
a_{\text{mới}} = a_{\text{thô}} / \max(a_{\text{thô}})$$

$$h_{\text{thô}}(u) = \sum_{v:\, u \to v} a_{\text{mới}}(v), \qquad
h_{\text{mới}} = h_{\text{thô}} / \max(h_{\text{thô}})$$

- Khởi tạo $h_0 = \mathbf{1}$ (vector toàn 1), $a_0 = \mathbf{0}$ (chỉ là mốc
  đo chênh).
- Kiểm tra $\max = 0$ **trước khi chia**: nếu max bằng 0, trả hai dict 0.
- Tổng thô là **điểm chưa chuẩn hóa**, chưa phải điểm cuối; điểm cuối là kết
  quả sau khi chia cho max.
- Dừng khi **cả hai** chênh $L_\infty$ (điểm thẩm quyền và điểm trung tâm) $\le \tau$;
  `delta` là max của hai độ chênh.
- Chuẩn max đặt phần tử lớn nhất bằng 1; tổng các thành phần HITS không bị ràng buộc bằng 1.
- Chi phí mỗi vòng: hai quét cạnh + quét đỉnh, $\Theta(n+m)$; không dựng ma
  trận $L$, $L^\top$ đặc, không dựng $LL^T$.

### Nhiệm vụ lập trình

Hoàn thiện `hits_student.hits_step` trên **danh sách kề** (hai TODO: cộng theo
cạnh, chuẩn hóa max). Hợp đồng hàm (đồng bộ với `link_analysis.hits_step`):

```python
def hits_step(adj, hub):
    """adj: dict nút -> list đích; đồ thị đơn, mọi đích được kê.
    hub: dict điểm trung tâm không âm, cùng tập khóa với adj.
    Trả về (authority_new, hub_new) là hai dict mới trên cùng khóa."""
```

Yêu cầu: dùng dữ liệu đầu vào đã hợp lệ, không sửa `adj` hay `hub`; trả hai
dict mới trên cùng khóa. Khung chưa cài phải báo "Chưa hoàn thiện" khi chạy
kiểm tra. Chạy:

```bash
python3 check_practice.py --student
```

Khung chưa cài sẽ báo "Chưa hoàn thiện hits_student.hits_step" và thoát với
mã 1; hoàn thiện đúng thì bộ kiểm đạt hết. Sau đó chạy mã tham chiếu đầy đủ:

```bash
python3 link_analysis.py hits --graph g4 --tol 0.001 --max-iter 1000
python3 link_analysis.py hits --graph g4 --tol 0.001 --max-iter 1
python3 link_analysis.py hits --graph g4 --tol 0.001 --max-iter 2
python3 check_practice.py
```

Lệnh `--max-iter 1` và `--max-iter 2` dùng để kiểm vết từng vòng; hai vòng G4
và vector ở vòng 11 có trong phần lời giải dưới đây để đối chiếu sau khi chạy.
Lệnh `check_practice.py` (mặc định) chỉ kiểm mã tham chiếu và phải đạt hết,
không phụ thuộc khung sinh viên. Chương trình còn kiểm G5 một vòng và đồ thị
không cạnh — đó là kiểm chương trình, đề bài vẫn là G4.

Với `--max-iter 1`, `converged: false` — không phải lỗi chương trình.

### Sản phẩm

- `hits_student.py` đã cài `hits_step`.
- Đoạn đối chiếu vết hai vòng G4 với kết quả chương trình trong `report.md`.

### Tiêu chí đạt

- `python3 check_practice.py --student` đạt hết sau khi hoàn thiện (khung chưa
  cài thì báo chưa hoàn thiện, mã thoát 1).
- `python3 check_practice.py` (mặc định, mã tham chiếu) đạt hết.
- Vết hai vòng do mình tính khớp phần đối chiếu trong lời giải.

::: hint
Thứ tự trong một vòng: dùng $h_{\text{cũ}}$ tính $a_{\text{thô}}$ (quét cạnh,
cộng điểm trung tâm của nguồn vào đích), chuẩn max thành $a_{\text{mới}}$; rồi dùng
$a_{\text{mới}}$ tính $h_{\text{thô}}$ (mỗi nút cộng điểm thẩm quyền của các đích kề),
chuẩn max thành $h_{\text{mới}}$. Không phần dịch chuyển, không chia 0: nếu
max bằng 0 trả hai vector 0. Đồ thị không cạnh cũng trả hai vector 0.
:::

::: solution
Vết hai vòng G4:

| Vòng | $a_{\text{thô}}$ | $a$ | $h_{\text{thô}}$ | $h$ |
|---|---|---|---|---|
| 1 | $(2,2,2,2)$ | $(1,1,1,1)$ | $(3,2,1,2)$ | $(1,\tfrac23,\tfrac13,\tfrac23)$ |
| 2 | $(1,\tfrac53,\tfrac53,\tfrac53)$ | $(\tfrac35,1,1,1)$ | $(3,\tfrac85,\tfrac35,2)$ | $(1,\tfrac8{15},\tfrac15,\tfrac23)$ |

Với $\tau=10^{-3}$, chương trình đạt ngưỡng sau 11 vòng, với $\delta\approx0.0007450739557$. Đây là trạng thái dừng theo ngưỡng, không phải nghiệm giới hạn chính xác:
$h \approx (1, 0.392369, 0.103046, 0.710676)$,
$a \approx (0.289993, 1, 1, 0.814221)$.
Hai chỗ hay sai: (1) dùng $a_{\text{cũ}}$ thay vì $a_{\text{mới}}$ khi tính
điểm trung tâm; (2) chuẩn hóa tổng thay vì chuẩn max. Đối chiếu cuối cùng bằng
`check_practice.py --student`, không tự đặt lại quy ước.
:::

---

## Nộp bài (5 phút)

Nộp hai tệp:

1. `hits_student.py` — đã cài `hits_step`, `check_practice.py --student` đạt hết.
2. `report.md` — bốn hàng kết quả: 2 hàng PageRank theo chủ đề (hạt giống A; hạt giống A,C), 1 hàng
   TrustRank/khối lượng rác, 1 hàng HITS; mỗi hàng ghi tham số (hạt giống, beta/tol/tau) và
   trạng thái dừng (`converged`, số vòng, `delta`); kèm 3 giải thích ngắn:
   nguồn phần dịch chuyển ở TSP, ý nghĩa khối lượng rác âm ở TrustRank, khác cách chuẩn
   hóa của HITS (max, không tổng 1).

### Tiêu chí tự kiểm (4 mục, đạt cụ thể là đủ)

| # | Mục | Bằng chứng đạt |
|---|---|---|
| 1 | TSP đúng nghiệm và trạng thái | 2 lệnh `topic`, `converged: true`, vector khớp phân số trong `1e-10` |
| 2 | TrustRank và khối lượng rác, giữ hai quy ước beta | hàng Trust có PageRank nền $\beta=1$ và TrustRank $\beta=4/5$ ghi rõ; $s(B) = -299/490$ |
| 3 | HITS khung hoàn thiện | `check_practice.py --student` đạt hết; `hits --graph g4 --tol 0.001` đạt ngưỡng sau 11 vòng |
| 4 | Báo cáo đủ 4 hàng + 3 giải thích | đọc lại báo cáo khớp kết quả chương trình |

---

## Nguồn

- [Mining of Massive Datasets](http://www.mmds.org), 3e, chương 5:
  §5.3 (PageRank theo chủ đề, thuật toán §5.3.2), §5.4 (spam, TrustRank,
  §5.4.4–5.4.5), §5.5 (HITS, cập nhật §5.5.2); Hình 5.1, 5.15, 5.18.
- Đề bài gốc: 5.3.1 (tr.199/PDF25), 5.4.2 (tr.204/PDF30), 5.5.1 (tr.208/PDF34).
- Đề bài và dữ kiện đồ thị thuộc nguồn MMDS; mã chương trình, ngưỡng dừng,
  thời lượng và lời giải/vết tính tay là biên soạn của môn học.
- Ghi chú môn học: [Ghi chú bài giảng](material-viewer.html?doc=materials/lec-04/lecture-note.md&deck=lecture-04-pagerank-theo-chu-de-lien-ket-rac-va-hits.html)
- Mã và khung (do môn biên soạn): [link_analysis.py](materials/lec-04/code/link_analysis.py),
  [hits_student.py](materials/lec-04/code/hits_student.py),
  [check_practice.py](materials/lec-04/code/check_practice.py),
  [practice-README.md](materials/lec-04/code/practice-README.md)
