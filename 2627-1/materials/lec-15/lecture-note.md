# Bài 15 — Thuật toán kết nối dữ liệu

> Bộ bài giảng: [Trang chiếu Bài 15](lecture-15-thuat-toan-ket-noi-du-lieu.html) — Giải thuật nền tảng của Khoa học dữ liệu, Học kỳ 1, năm học 2026–2027.

## Mở bài

Bài 12 cung cấp sắp xếp ngoài bộ nhớ; Bài 13 cung cấp B+-Tree và băm tĩnh. Bài 15 dùng lại ba công cụ đó để tính phép nối hai quan hệ nằm trên đĩa. Hai quan hệ `student` và `takes` đều không vừa bộ nhớ, nên mọi thuật toán phải tạo đúng tích các nhóm khóa trùng, nhưng cách tổ chức lại phép đọc — theo tuple, nhóm khối, chỉ mục, thứ tự hay phân hoạch — quyết định số lần truyền khối và seek.

Bài xét sáu thuật toán: Nested-Loop Join theo tuple, Block Nested-Loop Join, Indexed Nested-Loop Join, Sort-Merge Join, Hash Join trong bộ nhớ và Grace Hash Join. Mỗi thuật toán được đặc tả, chạy trên ví dụ nhỏ, chứng minh tính đúng và phân tích chi phí theo mô hình I/O. Ngoài phạm vi là tối ưu hóa thứ tự nhiều phép nối, ước lượng lực lượng kết quả, nối song song, nối không gian, outer join, pipelining và cache-conscious join.

## 1. Tình huống, đặc tả phép nối và mô hình I/O

**Vai trò và nhu cầu.** Bảng sự kiện `takes` ghi mỗi sinh viên đăng ký môn nào; bảng thực thể `student` ghi thông tin sinh viên. Muốn biết tên sinh viên cho từng dòng đăng ký, phải nối hai bảng theo `ID`. Cả hai bảng nằm trên đĩa và không vừa bộ nhớ, nên không thể nạp trọn một bảng rồi quét bảng kia trong RAM.

![Kết nối bảng takes bốn trăm khối với bảng student một trăm khối theo ID](img/lec-15/join-usecase.svg)

Dữ kiện nguồn: `student` có $n_{student}=5.000$ tuple, $b_{student}=100$ khối; `takes` có $n_{takes}=10.000$ tuple, $b_{takes}=400$ khối. Kịch bản $M=20$ khối bộ nhớ dùng xuyên suốt bài: không quan hệ nào vừa bộ nhớ. Đầu ra là mọi cặp có cùng `ID`.

**Đặc tả phép nối.** Gọi $r,s$ là hai quan hệ đầu vào và $\theta$ là điều kiện nối. Phép nối theta trả về

$$r\bowtie_\theta s=\{t_r\bullet t_s:\theta(t_r,t_s)\},$$

trong đó $t_r\bullet t_s$ là ghép hai tuple. Bài dùng ngữ nghĩa đa tập: mọi tuple cùng khóa ở hai phía tạo thành một cặp kết quả. Khóa nối được giả thiết khác `NULL`; ngữ nghĩa ba trị của SQL nằm ngoài phạm vi. Nested-Loop áp dụng cho điều kiện theta bất kỳ; Sort-Merge và Hash tập trung vào nối bằng hoặc nối tự nhiên.

**Ký hiệu chung.** $n_r,n_s$ là số tuple; $b_r,b_s$ là số khối; $M$ là số khối bộ nhớ dành cho phép nối. Các ký hiệu $q$, $b_b$, $p_h$, $\alpha$ được giới thiệu tại thuật toán cần chúng, không phải hằng số toàn cục.

**Truyền khối và seek.** Chi phí I/O gồm hai đại lượng khác đơn vị:

$$C=b\,t_T+S\,t_S,$$

trong đó $b$ là số lần truyền khối, $S$ là số seek, $t_T$ là thời gian truyền một khối và $t_S$ là thời gian một seek. Đọc tuần tự nhiều khối giảm seek nhưng không giảm số khối phải truyền. Không cộng hai số thành một "số I/O" khi so chi tiết.

**Giả thiết chi phí.** Không có khối đầu vào sẵn trong bộ đệm; không tính ghi kết quả cuối ra đĩa; chi phí CPU và mạng nằm ngoài công thức; bộ nhớ khả dụng là $M$ khối trong suốt phép nối.

::: exercise
Hai thuật toán truyền cùng số khối có luôn cùng thời gian không?
:::

::: hint
So số seek và mẫu truy cập tuần tự hay ngẫu nhiên của hai thuật toán.
:::

::: solution
Không. Số seek và mẫu truy cập có thể khác nhau. Một thuật toán đọc tuần tự nhiều khối liên tiếp có ít seek hơn một thuật toán đọc ngẫu nhiên cùng số khối, nên thời gian thật khác dù số lần truyền khối bằng nhau.
:::

## 2. Nested-Loop Join theo tuple

**Vai trò và nhu cầu.** Nested-Loop Join là đường cơ sở tổng quát: không cần thứ tự, hàm băm hoặc chỉ mục. Nó áp dụng trực tiếp cho điều kiện theta bất kỳ. Đổi lại, thuật toán xét mọi cặp tuple.

**Trực giác.** Chọn một tuple $t_r$ từ quan hệ ngoài, quét toàn bộ quan hệ trong, kiểm $\theta(t_r,t_s)$ và xuất cặp thỏa; lặp đến khi quan hệ ngoài cạn. Tên "ngoài" và "trong" mô tả vị trí vòng lặp, không phải vai trò khóa ngoại. Hoán đổi hai phía không đổi kết quả nhưng đổi chi phí.

**Ví dụ chạy tay.** Quan hệ ngoài $r$ có ba tuple khóa $1,2,4$; quan hệ trong $s$ có bốn tuple khóa $1,1,3,4$.

![Vết Nested-Loop Join quét toàn bộ quan hệ trong cho từng tuple ngoài](img/lec-15/tuple-nested-trace.svg)

Tuple khóa 1 xuất hai cặp vì phía trong có hai bản sao khóa 1. Tuple khóa 2 không xuất cặp nào. Tuple khóa 4 xuất một cặp. Vết này dùng để phát biểu bất biến.

**Giả mã:**

```text
cho mỗi tuple tᵣ trong r:
  cho mỗi tuple tₛ trong s:
    nếu θ(tᵣ,tₛ): xuất tᵣ • tₛ
```

**Bất biến.** Trước mỗi lần kiểm, mọi cặp đứng trước $(t_r,t_s)$ theo thứ tự hai vòng lặp đã được quyết định đúng một lần.

**Dừng.** Hai vòng lặp hữu hạn nên thuật toán dừng.

**Tính đúng.** Mọi cặp đầu vào xuất hiện đúng một vị trí trong thứ tự lồng của hai vòng lặp. Kiểm điều kiện $\theta$ tại vị trí đó cho tính đúng: cặp được xuất khi và chỉ khi thỏa $\theta$.

**Chi phí.** Với $r$ ngoài, chi phí là $b_r+n_r b_s$ lần truyền khối và $b_r+n_r$ seek theo mô hình nguồn. Áp dụng cho `student/takes`:

- `student` ngoài: $100+5.000\cdot400=2.000.100$ lần truyền.
- `takes` ngoài: $400+10.000\cdot100=1.000.400$ lần truyền.

`takes` có nhiều tuple hơn nhưng phía trong `student` chỉ 100 khối, nên tích nhỏ hơn. Quan hệ nhiều tuple hơn lại nên đặt ngoài ở đây vì phía trong của nó nhỏ.

::: exercise
Với $r$ ngoài, số seek là bao nhiêu theo mô hình nguồn, và vì sao `takes` ngoài lại rẻ hơn dù có nhiều tuple hơn?
:::

::: hint
Số seek với $r$ ngoài là $b_r+n_r$; so tích $n_r b_s$ của hai hướng.
:::

::: solution
Số seek với $r$ ngoài là $b_r+n_r$. Với `student` ngoài, seek là $100+5.000=5.100$; với `takes` ngoài, seek là $400+10.000=10.400$. Dù `takes` có nhiều tuple hơn, phía trong `student` chỉ 100 khối nên tích $n_r b_s=10.000\cdot100=1.000.000$ nhỏ hơn tích $5.000\cdot400=2.000.000$ của hướng ngược lại. Vì vậy `takes` ngoài rẻ hơn về số lần truyền khối.
:::

## 3. Block Nested-Loop Join và hai bố trí bộ đệm

**Vai trò và nhu cầu.** Vòng lặp theo tuple đọc lại phía trong quá nhiều: mỗi tuple ngoài mở một lượt quét toàn bộ phía trong. Block Nested-Loop Join giữ một nhóm khối ngoài trong bộ nhớ và quét toàn bộ phía trong một lần cho cả nhóm, giảm số lượt quét.

**Kích thước nhóm ngoài.** Gọi $q$ là số khối ngoài giữ trong mỗi nhóm. Giá trị $q$ được suy từ bố trí bộ đệm, không phải hằng số toàn cục:

- Khi đầu ra được vật chất hóa, dành một khối đọc phía trong và một khối đầu ra, nên $q=M-2$.
- Khi đầu ra được chuyển tiếp hoặc không chiếm bộ đệm riêng, $q=M-1$.

![Hai cách bố trí bộ đệm của Block Nested-Loop Join](img/lec-15/block-nested.svg)

**Ví dụ chạy tay.** Với $M=4$ và đầu ra vật chất hóa, giữ hai khối ngoài $R=[r_A,r_B]$, trong đó khóa của $r_A,r_B$ lần lượt là $A,B$; đọc $S_1=[s_B]$ rồi $S_2=[s_A,s_C]$, với chỉ số dưới là khóa. Các cặp khớp là:

$$R\bowtie S_1=\{(r_B,s_B)\},\qquad R\bowtie S_2=\{(r_A,s_A)\}.$$

Mỗi khối trong được đọc một lần cho cả nhóm ngoài. Hai khối còn lại của bộ nhớ là một khối đọc phía trong và một khối đầu ra, nên nhóm ngoài có $M-2=2$ khối.

**Giả mã:**

```text
cho mỗi nhóm R gồm tối đa q khối của r:
  cho mỗi khối Bₛ của s:
    cho mỗi tᵣ trong R và tₛ trong Bₛ:
      nếu θ(tᵣ,tₛ): xuất tᵣ • tₛ
```

**Bất biến.** Trước mỗi khối $B_s$, mọi cặp giữa nhóm $R$ và các khối trong đã đọc được quyết định. Các nhóm $R$ phân hoạch $r$, nên mọi cặp đầu vào vẫn được kiểm đúng một lần.

**Dừng.** Số nhóm ngoài hữu hạn và mỗi nhóm quét hết phía trong hữu hạn, nên thuật toán dừng.

**Chi phí.** Với $r$ ngoài:

$$T=b_r+\left\lceil\frac{b_r}{q}\right\rceil b_s,\qquad S\approx2\left\lceil\frac{b_r}{q}\right\rceil.$$

Với $M=20$ và đầu ra vật chất hóa, $q=18$. `student` ngoài cần $100+\lceil100/18\rceil\cdot400=100+6\cdot400=2.500$ lần truyền và khoảng $2\cdot6=12$ seek. Đưa quan hệ có ít khối hơn ra ngoài thường giảm số lượt quét trong. Thay $q$ theo đúng bố trí bộ đệm đã chọn; không dùng $M-2$ như quy ước toàn cục.

::: exercise
Với $M=20$ và đầu ra được chuyển tiếp, $q$ bằng bao nhiêu, và `student` ngoài cần bao nhiêu lần truyền khối?
:::

::: hint
Khi đầu ra chuyển tiếp, không giữ bộ đệm ra riêng nên $q=M-1$.
:::

::: solution
Khi đầu ra chuyển tiếp, $q=M-1=19$. `student` ngoài cần $100+\lceil100/19\rceil\cdot400=100+6\cdot400=2.500$ lần truyền khối. Số lượt quét trong vẫn là $\lceil100/19\rceil=6$ vì 100 chia 19 được 5 dư 5, làm tròn lên 6.
:::

## 4. Indexed Nested-Loop Join và chỉ mục thứ cấp

**Vai trò và nhu cầu.** Nếu phía trong có chỉ mục trên thuộc tính nối, thay lượt quét toàn bộ phía trong bằng phép tra chỉ mục cho từng tuple ngoài. Điều kiện áp dụng là nối bằng hoặc nối tự nhiên và phía trong có chỉ mục trên thuộc tính nối.

**Ví dụ chạy tay.** Quan hệ ngoài có ba tuple khóa $17,23,17$; phía trong có chỉ mục B+-Tree trên `ID`. Khóa 17 trỏ tới hai bản sao $s_1,s_2$; khóa 23 trỏ tới danh sách rỗng.

![Ba khóa phía ngoài tra chỉ mục và giữ đủ hai bản sao khóa 17](img/lec-15/indexed-nested.svg)

Mỗi tuple ngoài khóa 17 ghép với cả hai bản sao, nên đầu ra có bốn cặp. Khóa 23 không khớp tuple nào phía trong nên trả danh sách rỗng, nhưng vòng ngoài vẫn tiến.

**Giả mã:**

```text
cho mỗi tuple tᵣ của r:
  L ← tra_chỉ_mục(key(tᵣ))
  cho mỗi RID trong L:
    đọc tₛ tại RID
    nếu key(tᵣ)=key(tₛ): xuất tᵣ • tₛ
ghi chú: L rỗng hoặc đã cạn thì chuyển sang tᵣ kế tiếp
```

**Dừng.** Mỗi vòng hữu hạn: $r$ hữu hạn và mỗi danh sách RID hữu hạn. Không dừng ở RID đầu nếu khóa không duy nhất; phép so khóa bảo vệ trước ứng viên sai.

**Tính đúng.** Mỗi tuple ngoài tra chỉ mục và duyệt hết danh sách RID của khóa đó. Phép so khóa thật loại các ứng viên do va chạm hoặc chỉ mục thứ cấp trả về nhầm. Vì vậy mọi cặp cùng khóa được xuất đúng một lần.

**Chi phí.** Chi phí là thời gian:

$$C=b_r(t_T+t_S)+n_r c,$$

trong đó $c$ là thời gian tra chỉ mục và đọc mọi tuple trong khớp một tuple ngoài. Công thức nguồn tính mỗi khối của lượt quét ngoài với một lần truyền và một seek; nếu hệ thống đọc ngoài thành lô tuần tự thì phải thay số hạng seek bằng chi phí của đúng cách đọc đó. $C$ là thời gian, nên không so trực tiếp với một số lần truyền khối của thuật toán khác. Chỉ mục thứ cấp với nhiều bản sao nằm rải rác làm $c$ lớn.

::: exercise
Chỉ mục tồn tại có đủ để Indexed Nested-Loop Join luôn tốt hơn các thuật toán khác không?
:::

::: hint
Xét chỉ mục thứ cấp với nhiều bản sao nằm rải rác và đơn vị chi phí là thời gian.
:::

::: solution
Không. Chỉ mục thứ cấp với nhiều bản sao nằm rải rác trên đĩa làm $c$ lớn vì mỗi bản sao có thể ở một khối khác nhau, gây nhiều lần đọc ngẫu nhiên. Chi phí $C=b_r(t_T+t_S)+n_r c$ là thời gian; muốn so với số lần truyền khối của thuật toán khác, phải đổi mọi đại lượng về cùng đơn vị thời gian theo cùng mô hình.
:::

## 5. Sort-Merge Join, nhóm khóa trùng và chi phí vật chất hóa

**Vai trò và nhu cầu.** Nếu không có chỉ mục nhưng có thể sắp theo khóa, hai con trỏ trên hai dãy đã sắp thay nhiều phép tra ngẫu nhiên. Sort-Merge Join áp dụng cho equi-join và natural join. Quan hệ chưa sắp phải trả chi phí External Merge Sort trước khi nối.

**Trực giác.** Hai con trỏ chỉ tiến về trước trên hai dãy đã sắp theo cùng thứ tự khóa. Nếu khóa nhỏ hơn khóa hiện tại phía kia, nó không thể khớp với bất kỳ tuple chưa đọc nào vì dãy đã sắp.

**Ví dụ chạy tay.** Hai dãy:

$$r=[1,2,2,4],\qquad s=[2,2,2,3,4].$$

Bước 1: $1<2$, bỏ nhóm khóa 1 của $r$. Bước 2: $2=2$, giữ đầu hai nhóm khóa 2 và xuất đủ sáu cặp. Bước 3: bỏ hai nhóm khóa 2; lúc này $4>3$, nên bỏ nhóm khóa 3 của $s$. Bước 4: $4=4$, xuất một cặp rồi cả hai dãy cạn. Không tiến sang khóa mới trước khi ghép hết nhóm hiện tại.

**Nhóm khóa trùng.** Nhóm khóa 2:

$$G_r(2)=\{r_{21},r_{22}\},\qquad G_s(2)=\{s_{21},s_{22},s_{23}\}.$$

Tích hai nhóm có $2\cdot3=6$ cặp. Nếu chỉ tiến đồng thời từng tuple, thuật toán sẽ xuất ít hơn sáu cặp và làm mất bản sao. Phải giữ hoặc đánh dấu đầu một nhóm trong khi quét nhóm kia.

![Sort-Merge Join tạo tích Descartes giữa hai nhóm tuple có cùng khóa](img/lec-15/sort-merge-groups.svg)

**Giả mã:**

```text
while r và s chưa cạn:
  nếu key(r) < key(s): bỏ nhóm hiện tại của r
  ngược lại nếu key(r) > key(s): bỏ nhóm hiện tại của s
  ngược lại:
    Gᵣ ← nhóm hiện tại của r; Gₛ ← nhóm hiện tại của s
    nếu một nhóm vừa RAM:
      giữ nhóm đó, quét nhóm kia, rồi tiến cả hai qua nhóm
    ngược lại:
      xử lý tích hai nhóm bằng tệp tạm hoặc thuật toán dự phòng
      tiến cả hai qua nhóm
```

**Điều kiện trước.** Hai đầu vào đã sắp theo cùng thứ tự khóa. **Điều kiện sau.** Mọi cặp cùng khóa được xuất đúng một lần.

**Bất biến.** Trước mỗi vòng, mọi cặp kết quả có khóa nhỏ hơn ít nhất một khóa hiện tại đã được xuất đúng một lần. Nhóm nhỏ hơn không thể khớp về sau. Hai nhóm bằng nhau được xuất bằng tích Descartes.

**Dừng.** Mỗi vòng bỏ ít nhất một nhóm hữu hạn, nên thuật toán dừng. Khi một dãy cạn, không còn khóa chung chưa xử lý.

**Nhóm trùng không vừa bộ nhớ.** Nếu một nhóm vừa RAM, giữ nhóm đó và quét nhóm còn lại đúng một lần để xuất tích. Nếu cả hai nhóm không vừa, phải ghi tạm hoặc chuyển thuật toán. Cận quét một lần $b_r+b_s$ chỉ giữ khi không phát sinh đọc lại.

**Chi phí vật chất hóa.** Bài này dùng phương án ghi hai dãy đã sắp ra đĩa rồi đọc lại khi nối, khớp lời giải Bài 15.3. Với

$$f=\left\lfloor\frac{M}{b_b}\right\rfloor-1>1,\qquad P(b)=\left\lceil\log_f\left\lceil\frac{b}{M}\right\rceil\right\rceil,$$

chi phí sắp vật chất hóa là

$$T_{sort}^{mat}(b)=2b(P(b)+1),$$

và seek sắp là

$$S_{sort}^{mat}(b)=2\left\lceil\frac{b}{M}\right\rceil+2P(b)\left\lceil\frac{b}{b_b}\right\rceil.$$

Ví dụ $M=20$, $b_b=2$: $f=\lfloor20/2\rfloor-1=9$; nếu $b\le20$ thì $P(b)=0$ và $T=2b$. Tổng chi phí nối là $T_{sort}^{mat}(b_r)+T_{sort}^{mat}(b_s)+b_r+b_s$. Cộng quét tuyến tính chỉ khi một nhóm trùng vừa bộ nhớ hoặc cơ chế đánh dấu/ghi tạm không gây đọc lại khối.

::: exercise
Hai dãy đã sắp nhưng khóa 7 lặp trên nhiều khối hơn bộ nhớ. Có còn khẳng định mỗi khối chỉ đọc một lần không?
:::

::: hint
Xét điều kiện nhóm trùng vừa bộ nhớ và cơ chế giữ, đánh dấu hoặc ghi tạm.
:::

::: solution
Không, nếu không có cơ chế giữ, đánh dấu hoặc ghi tạm nhóm. Khi nhóm khóa 7 không vừa bộ nhớ, phải đọc lại các khối của nhóm để xuất tích Descartes, phá giả thiết quét một lần. Cận $b_r+b_s$ chỉ áp dụng khi không phát sinh đọc lại.
:::

## 6. Hash Join trong bộ nhớ

**Vai trò và nhu cầu.** Equi-join còn cho phép gom khóa bằng băm thay vì thứ tự. Khi phía xây vừa bộ nhớ, Hash Join đọc mỗi đầu vào một lần.

**Điều kiện bộ nhớ.** Quan hệ xây $s$ phải thỏa

$$\alpha b_s+b_{in}+b_{out}\le M,\qquad b_{in}=b_{out}=1,$$

trong đó $\alpha\ge1$ là hệ số phụ trội của bảng băm so với số khối dữ liệu xây, $b_{in}$ là bộ đệm đọc phía dò và $b_{out}$ là bộ đệm đầu ra. Chọn phía có bảng băm nhỏ hơn làm phía xây.

**Trực giác.** Xây một lần, dò một lần: đọc $s$ và xây bảng băm theo khóa nối; đọc từng tuple $t_r$ của $r$; dò ngăn $h(\mathrm{key}(t_r))$; kiểm khóa thật và xuất mọi tuple khớp. Hàm băm thu hẹp ứng viên; phép so sánh khóa quyết định kết quả.

**Va chạm và bản sao.** Hai khóa khác nhau có thể va chạm cùng ngăn, nên phải kiểm khóa thật. Nhiều tuple cùng khóa là bản sao hợp lệ của quan hệ và đều phải được giữ để tạo đủ cặp nối.

![Bảng băm phân biệt hai tuple trùng khóa với hai khóa khác nhau va chạm cùng ngăn](img/lec-15/hash-build-probe.svg)

**Giả mã:**

```text
yêu cầu α·bₛ + b_in + b_out ≤ M; b_in=b_out=1
H ← bảng băm rỗng
cho mỗi tₛ trong s: thêm tₛ vào danh sách H[h(key(tₛ))]
cho mỗi tᵣ trong r:
  cho mỗi tₛ trong H[h(key(tᵣ))]:
    nếu key(tᵣ) = key(tₛ): xuất tᵣ • tₛ
```

**Bất biến khi dò.** Trước mỗi $t_r$, bảng băm chứa mọi tuple của $s$; mọi tuple $r$ đã đọc đã được ghép với toàn bộ tuple $s$ cùng khóa. Cùng khóa cho cùng giá trị băm; kiểm khóa loại va chạm giả.

**Tính đúng.** Mệnh đề cần chứng minh là mọi cặp equi-join xuất đúng một lần. Mỗi $t_r$ được dò một lần, và danh sách ngăn duyệt từng $t_s$ đúng một lần cho $t_r$ đó. Phép so khóa thật giữ đúng các cặp cùng khóa và loại các ứng viên va chạm.

**Dừng.** Pha xây duyệt $s$ hữu hạn; pha dò duyệt $r$ hữu hạn và mỗi danh sách ngăn hữu hạn, nên thuật toán dừng.

**Chi phí.** Khi bảng băm vừa RAM:

$$\alpha b_s+b_{in}+b_{out}\le M\Longrightarrow T=b_r+b_s.$$

Công thức bỏ chi phí ghi đầu ra và giả thiết không có spill.

::: exercise
Nếu $s$ có hai tuple cùng khóa, bảng băm được phép chỉ giữ tuple cuối không?
:::

::: hint
Xét số cặp kết quả cần xuất khi phía dò có một tuple cùng khóa.
:::

::: solution
Không. Bảng băm phải lưu danh sách mọi tuple theo khóa, không ghi đè bản sao. Nếu chỉ giữ tuple cuối, một tuple $t_r$ cùng khóa chỉ ghép được với một trong hai bản sao, làm mất một cặp kết quả. Bảo toàn bản sao là yêu cầu của ngữ nghĩa đa tập.
:::

## 7. Grace Hash Join: phân hoạch và vết xây–dò

**Vai trò và nhu cầu.** Khi phía xây không vừa vùng bảng băm của pha xây–dò, Grace Hash Join chia cả hai quan hệ bằng cùng hàm $h$ thành các cặp phân hoạch, ghi ra đĩa, rồi nối từng cặp phân hoạch. Grace Hash Join có hai pha với hai bố trí bộ đệm khác nhau: pha phân hoạch giữ bộ đệm vào và các bộ đệm ra; pha xây–dò giữ bảng băm cùng bộ đệm dò và đầu ra.

**Ví dụ chạy tay — phân hoạch.** Với $h_1(k)=k\bmod2$:

- phía xây $s$: $s_0=[2,4]$, $s_1=[1]$;
- phía dò $r$: $r_0=[2,6]$, $r_1=[3]$.

Chỉ $(r_0,s_0)$ và $(r_1,s_1)$ cần được nối. Cặp đúng duy nhất là khóa 2; khóa 4 và 6 cùng phân hoạch nhưng không bằng nhau. Bài này dùng $p_h$ phân hoạch đánh số $0..p_h-1$, gồm $r_i$ và $s_i$.

**Ví dụ chạy tay — dò.** Trong $(r_0,s_0)$, dùng hàm băm nội bộ $h_2(k)=\lfloor k/2\rfloor\bmod2$, khác $h_1$. Tính lại: $h_2(4)=0$; $h_2(2)=h_2(6)=1$. Ngăn 0 có tuple khóa 4 của $s_0$; ngăn 1 có tuple khóa 2 của $s_0$. Dò tuple khóa 2 của $r_0$ vào ngăn 1 và xuất cặp hai tuple khóa 2. Tuple khóa 6 của $r_0$ cũng vào ngăn 1 nhưng không tạo kết quả vì $6\ne2$. Va chạm chỉ tạo ứng viên; phép so khóa loại ứng viên sai.

**Pha phân hoạch.** Pha này cần một bộ đệm vào và $p_h$ bộ đệm ra:

$$(p_h+1)b_b\le M,$$

trong đó $b_b$ là số khối trong mỗi lô đọc hoặc ghi liên tiếp của mô hình seek. Ở pha phân hoạch, chọn bộ đệm lô cũng rộng $b_b$ khối: một tham số thiết kế phải đồng thời thỏa ràng buộc dung lượng và quyết định số seek. $b_b$ độc lập với $b_{in},b_{out}$ của pha xây–dò.

![Grace Hash Join chia hai quan hệ thành bảy cặp phân hoạch với bố trí bộ đệm khả thi](img/lec-15/grace-partition.svg)

Với $M=20$, $b_b=2$, $p_h=7$: phía xây 100 khối chia thành $15;15;14;14;14;14;14$ khối. Pha phân hoạch dùng $(7+1)\cdot2=16\le20$ khối.

**Pha xây–dò.** Pha này không giữ các bộ đệm ra của pha phân hoạch. Nó tái dùng bộ nhớ cho bảng băm, một khối dò và một khối đầu ra. Bảng băm của $s_i$ phải thỏa

$$\alpha\max_i b_{s_i}+b_{in}+b_{out}\le M,\qquad b_{in}=b_{out}=1.$$

Với $\alpha=1{,}2$: $1{,}2\cdot15+1+1=20$. Bài này dùng $s_i$ làm phía xây và $r_i$ làm phía dò.

::: exercise
Vì sao điều kiện bộ nhớ của pha xây–dò phải dùng $\max_i b_{s_i}$ thay vì kích thước trung bình của các phân hoạch?
:::

::: hint
Xét phân hoạch lớn nhất có vừa vùng bảng băm hay không.
:::

::: solution
Điều kiện phải giữ cho mọi phân hoạch, kể cả phân hoạch lớn nhất. Kích thước trung bình không bảo đảm phân hoạch lớn nhất vừa bộ nhớ; nếu phân hoạch lớn nhất tràn, pha xây–dò của cặp đó không chạy được. Vì vậy dùng $\alpha\max_i b_{s_i}+b_{in}+b_{out}\le M$.
:::

## 8. Grace Hash Join: skew, đường lui, tính đúng và chi phí

**Vai trò.** Khi pha xây–dò không vừa, nhận diện skew rồi chọn một trong ba nhánh hữu hạn. Phân hoạch lệch làm một ngăn không vừa bộ nhớ và cần phân hoạch lại hoặc Block Nested-Loop Join.

![Phân hoạch lệch làm một ngăn không vừa bộ nhớ và cần phân hoạch lại hoặc Block Nested](img/lec-15/skew-fallback.svg)

**Ba nhánh cho mỗi phân hoạch.** Dùng hàng đợi công việc:

```text
Q ← [(r,s)]
while Q không rỗng:
  (R,S) ← lấy_đầu(Q); chia bằng hàm h mới
  cho mỗi cặp (Rᵢ,Sᵢ):
    nếu α·b(Sᵢ)+b_in+b_out ≤ M: build–probe(Rᵢ,Sᵢ)
    ngược lại nếu max(b(Rᵢ),b(Sᵢ)) < max(b(R),b(S)):
      thêm (Rᵢ,Sᵢ) vào Q
    ngược lại: Block-Nested(Rᵢ,Sᵢ)
```

Ba nhánh loại trừ nhau nên mỗi cặp con được xử lý đúng một lần. Nhánh đệ quy chỉ được xếp lại khi kích thước lớn nhất giảm; nếu không tiến triển do skew khóa, Block Nested kết thúc trên hai quan hệ hữu hạn. Băm lại bằng hàm khác có thể sửa hàm băm xấu. Nếu nhiều tuple có cùng khóa, mọi hàm theo khóa vẫn đặt chúng cùng phân hoạch; dùng Block Nested cho phân hoạch tràn để bảo đảm tiến triển và tính đúng.

Ví dụ, với $M=20$, một cặp phân hoạch có phía xây 25 khối không thể build–probe. Nếu băm lại làm phân hoạch lớn nhất giảm từ 25 xuống 14 khối, cặp đó đi vào hàng đợi và được xử lý ở lượt sau. Nếu phân hoạch lớn nhất vẫn là 25 khối, thuật toán chuyển ngay sang Block Nested để tránh lặp vô hạn.

**Tính đúng.** Mệnh đề cần chứng minh là mỗi cặp đầu vào được quyết định đúng một lần.

- **Khởi tạo:** toàn bộ cặp nằm trong $(r,s)$.
- **Duy trì:** một lần phân hoạch thay một cặp bằng các cặp con rời nhau; cặp cùng khóa đi vào đúng một con vì cùng khóa cho cùng giá trị $h$.
- **Kết thúc:** mỗi lá dùng build–probe hoặc Block Nested, đều xuất đúng các cặp bằng khóa.

Các phân hoạch rời nhau và mỗi tuple thuộc đúng một phân hoạch. Build–probe hoặc đường lui kiểm cặp đó đúng một lần và so khóa thật.

**Chi phí.** Khi không đệ quy và không tràn, mỗi khối đi qua ba lần truyền lý tưởng: đọc để phân hoạch, ghi phân hoạch, đọc để nối.

![Ba lượt truyền khối của Grace Hash Join gồm đọc ghi phân hoạch và đọc để nối](img/lec-15/grace-cost.svg)

Với `student/takes`:

- lý tưởng: $3(100+400)=1.500$ lần truyền;
- kể cả khối biên: khối cuối của mỗi phân hoạch có thể chưa đầy và phải đọc hoặc ghi riêng; cận tăng tối đa $4p_h$, nên số lần truyền là $1.500+4\cdot7=1.528$;
- seek tổng theo công thức nguồn với $b_b=2$: $2(\lceil100/2\rceil+\lceil400/2\rceil)=2(50+200)=500$ seek.

Các số áp dụng khi mọi phân hoạch xây thỏa điều kiện pha xây–dò ngay sau lượt đầu. Nếu đệ quy hoặc dùng đường lui, phải cộng chi phí phát sinh.

::: exercise
Những phát biểu nào cần để Grace Hash Join chạy đúng và dừng?
:::

::: hint
Xét ba điều kiện: cùng khóa cùng phân hoạch, bảng băm giữ bản sao và kiểm khóa, điều kiện bộ nhớ hoặc đường lui hữu hạn.
:::

::: solution
Cả ba đều cần. Điều 1 cho bao phủ: cùng khóa đi vào đúng một cặp phân hoạch. Điều 2 xử lý đa tập và va chạm: bảng băm giữ mọi bản sao và kiểm khóa thật. Điều 3 cho khả năng thực thi và dừng: $\alpha b_{s_i}+b_{in}+b_{out}\le M$, hoặc có đường lui hữu hạn khi phân hoạch tràn.
:::

## 9. Chọn thuật toán theo điều kiện và đơn vị chi phí

**Vai trò.** Các cụm trước xây từng thuật toán riêng. Cụm này gộp lại để chọn thuật toán theo điều kiện nối, bộ nhớ, thứ tự, chỉ mục và độ lệch phân hoạch.

**Bản đồ điều kiện nối.** Trong các biến thể được dạy ở bài này, theta tổng quát giữ Nested hoặc Block Nested; equi-join mở thêm Indexed Nested, Sort-Merge và Hash.

![Bản đồ chọn thuật toán nối theo điều kiện nối, chỉ mục, thứ tự, bộ nhớ và độ lệch](img/lec-15/join-cost-map.svg)

**Bảng so sánh.**

| Thuật toán | Điều kiện | Tái sử dụng | Rủi ro chính |
|---|---|---|---|
| Nested | theta | không | $n_r b_s$ |
| Block Nested | theta | $q$ khối | nhiều lượt quét |
| Indexed Nested | nối bằng + chỉ mục | tra cứu | I/O ngẫu nhiên |
| Sort-Merge | nối bằng + thứ tự | nhóm khóa | sắp, nhóm lớn |
| Hash/Grace | nối bằng | ngăn/phân hoạch | lệch, tràn |

Dòng Indexed dùng chi phí thời gian có tra chỉ mục; không thể so trực tiếp con số đó với số lần truyền khối nếu chưa đổi về cùng đơn vị.

**Ba trạng thái giả định của `student/takes`.** Đây là ba giả định thay thế. Kịch bản gốc không có sẵn chỉ mục hay thứ tự theo `ID`; với $M=20$, nó cũng không thỏa điều kiện bộ nhớ của giả định thứ ba.

- `takes` có chỉ mục `ID`: ước lượng Indexed Nested.
- Hai phía đã sắp `ID`: Sort-Merge quét 500 khối nếu nhóm trùng không gây đọc lại.
- `student` đủ vùng xây: Hash đọc 500 khối nếu $\alpha\cdot100+b_{in}+b_{out}\le M$.

Các con số 500 ở đây chỉ so số lần truyền khối và bỏ chi phí ghi kết quả; số seek còn phụ thuộc cách đọc lô và trạng thái vật lý của đầu vào. Sort-Merge còn cần một nhóm trùng vừa RAM hoặc cơ chế ngoài bộ nhớ không phát sinh đọc lại. Với Indexed Nested phải đổi $c$ và seek về cùng đơn vị trước khi so.

**Quy trình chọn thuật toán nối:**

1. Chốt nối theta hay nối bằng.
2. Chốt $n_r,n_s,b_r,b_s,M$ và bản sao khóa.
3. Kiểm trạng thái sắp và chỉ mục.
4. Tính truyền khối và seek cho cả hai hướng.
5. Kiểm nhóm lớn, phân hoạch lệch và đường lui.

Bước cuối ngăn việc chọn công thức chi phí lý tưởng khi giả thiết bộ nhớ không giữ.

::: exercise
Vì sao không thể dùng một vùng $M-2$ cho mọi thuật toán?
:::

::: hint
So bố trí bộ đệm của Block Nested, pha phân hoạch và pha xây–dò.
:::

::: solution
Block Nested, pha phân hoạch và pha xây–dò giữ các loại bộ đệm khác nhau. Block Nested dùng $q$ khối ngoài; pha phân hoạch dùng một bộ đệm vào và $p_h$ bộ đệm ra; pha xây–dò dùng bảng băm cùng bộ đệm dò và đầu ra. Phụ trội bảng băm $\alpha$ còn làm dung lượng dữ liệu nhỏ hơn dung lượng khối thô. Vì vậy phải khai báo bố trí bộ đệm tại thuật toán dùng nó, không áp một vùng chung.
:::

## 10. Recitation 15.3–15.4

Ba bài dưới đây dùng nguyên đề và lời giải chính thức của *Database System Concepts* 7e, Practice Exercises Chương 15. Không đổi dữ kiện hoặc yêu cầu; ghi rõ các giả thiết vật chất hóa và bố trí bộ đệm dùng khi tính.

### 10.1. Bài 15.3 — ước lượng chi phí bốn chiến lược nối

**Đặc tả.** Quan hệ $r_1(A,B,C)$ có 20.000 tuple, 25 tuple/khối; quan hệ $r_2(C,D,E)$ có 45.000 tuple, 30 tuple/khối. Yêu cầu: ước lượng truyền khối và seek cho Nested-Loop, Block Nested-Loop, Merge và Hash Join của $r_1\bowtie r_2$.

**Số khối.** $b_{r_1}=20.000/25=800$ và $b_{r_2}=45.000/30=1.500$. Lời giải xét $M\le800$; nếu $M>800$, quan hệ nhỏ vừa bộ nhớ.

**Nested-Loop.** Với $r_1$ ngoài: $b_{r_1}+n_{r_1}b_{r_2}=800+20.000\cdot1.500=30.000.800$ lần truyền và $b_{r_1}+n_{r_1}=20.800$ seek. Với $r_2$ ngoài: $b_{r_2}+n_{r_2}b_{r_1}=1.500+45.000\cdot800=36.001.500$ lần truyền và $46.500$ seek.

**Block Nested-Loop.** Gọi $q$ là số khối ngoài giữ mỗi nhóm:

$$T_{BNL}=b_o+\left\lceil\frac{b_o}{q}\right\rceil b_i.$$

Với $r_1$ ngoài: $800+\lceil800/q\rceil\cdot1.500$; với $r_2$ ngoài: $1.500+\lceil1500/q\rceil\cdot800$. Seek xấp xỉ $2\lceil b_o/q\rceil$. Lời giải dùng $q=M-1$ vì không giữ riêng đầu ra; nếu vật chất hóa đầu ra bằng một bộ đệm riêng thì $q=M-2$.

**Merge Join.** Đặt $f=\lfloor M/b_b\rfloor-1>1$ và $P(b)=\lceil\log_f\lceil b/M\rceil\rceil$. Với kết quả sắp được vật chất hóa:

$$T_{sort}^{mat}(b)=2b(P(b)+1),\qquad S_{sort}^{mat}(b)=2\left\lceil\frac{b}{M}\right\rceil+2P(b)\left\lceil\frac{b}{b_b}\right\rceil.$$

Tổng nối cộng $2.300$ lần truyền và $\lceil1500/b_b\rceil+\lceil800/b_b\rceil$ seek. Khi $P=0$, vẫn có một lượt đọc–ghi run; công thức không sinh số seek âm. Với $b_b=1$, cơ số là $M-1$, đúng dạng lời giải $F_M(b)=b(2\lceil\log_{M-1}(b/M)\rceil+2)$. Giả thiết nhóm cùng khóa không gây đọc lại.

**Grace Hash Join.** Chọn $r_1$ có 800 khối làm phía xây. Fan-out phải thỏa $(p_h+1)b_b\le M$; pha xây–dò cần $\alpha\max_i b_{s_i}+b_{in}+b_{out}\le M$, với $b_{in}=b_{out}=1$. Điều kiện trung bình không thay thế việc kiểm phân hoạch lớn nhất. Nếu một lượt đủ và không tràn, truyền $3(800+1.500)=6.900$, cận khối biên cộng tối đa $4p_h$, còn seek tổng là $2(\lceil800/b_b\rceil+\lceil1500/b_b\rceil)$. Nếu điều kiện bảng băm không giữ, phân hoạch lại bằng hàm khác hoặc dùng đường lui.

::: exercise
Với $r_1$ ngoài trong Nested-Loop, hãy tính số lần truyền khối và số seek, rồi giải thích vì sao $r_2$ ngoài lại đắt hơn dù $r_2$ có nhiều tuple hơn.
:::

::: hint
Dùng $b_r+n_r b_s$ cho truyền và $b_r+n_r$ cho seek; so tích $n_r b_s$ của hai hướng.
:::

::: solution
Với $r_1$ ngoài: truyền $800+20.000\cdot1.500=30.000.800$, seek $800+20.000=20.800$. Với $r_2$ ngoài: truyền $1.500+45.000\cdot800=36.001.500$, seek $46.500$. $r_2$ ngoài đắt hơn vì số tuple ngoài lớn làm tích $n_{r_2}b_{r_1}=45.000\cdot800=36.000.000$ vượt tích $n_{r_1}b_{r_2}=20.000\cdot1.500=30.000.000$; đây là cùng quy tắc so $n_r b_s$ đã dùng với `student/takes`.
:::

### 10.2. Bài 15.4 — giảm đọc ngẫu nhiên của chỉ mục thứ cấp

**Đặc tả.** So hai đường lấy tuple trong khi phía trong có chỉ mục thứ cấp trên thuộc tính nối.

- **Biến thể chỉ mục:** tra lá cho từng tuple ngoài → gom RID → sắp RID → đọc tuple trong.
- **Hybrid Merge:** sắp phía ngoài → trộn với mục lá → sắp RID → đọc tuple trong.

RID là địa chỉ bản ghi. Yêu cầu: giải thích nguồn I/O ngẫu nhiên và nêu điều kiện đường chỉ mục tốt hơn.

**Nguyên nhân I/O ngẫu nhiên.** Mỗi tuple ngoài có thể kéo nhiều tuple trong nằm ở các khối khác nhau, và việc lặp khóa làm đọc lại các khối. Đọc tuple trong theo thứ tự RID rải rác gây nhiều seek.

**Hoãn đọc tuple trong.** Ba bước:

1. Nối tuple ngoài với các mục lá của chỉ mục thứ cấp.
2. Ghi cặp cùng địa chỉ tuple trong rồi sắp theo địa chỉ.
3. Quét quan hệ trong theo thứ tự vật lý để hoàn tất nối.

**So bằng tổng chi phí I/O.** Biến thể chỉ mục trả chi phí tra cho từng tuple ngoài; Hybrid Merge trả chi phí sắp phía ngoài rồi trộn với mục lá. Hai phương án còn cùng trả chi phí sắp địa chỉ tuple trong và đọc vật lý, nên có thể khử các số hạng chung khi so:

$$C_{index}<C_{sort\ outer}+C_{merge\ leaf}.$$

Kích thước phía ngoài, tự nó, không quyết định bất đẳng thức. Lời giải nguồn nói trường hợp phía ngoài lớn hơn nhiều có thể thuận lợi cho tra chỉ mục; phát biểu đó không phải bảo đảm nếu chưa ước lượng độ cao chỉ mục, độ lặp khóa và I/O ngẫu nhiên.

::: exercise
Vì sao kích thước phía ngoài, tự nó, không đủ để quyết định đường chỉ mục tốt hơn Hybrid Merge?
:::

::: hint
So tổng chi phí I/O gồm độ cao chỉ mục, độ lặp khóa và I/O ngẫu nhiên, không chỉ kích thước phía ngoài.
:::

::: solution
Bất đẳng thức $C_{index}<C_{sort\ outer}+C_{merge\ leaf}$ phụ thuộc nhiều đại lượng: độ cao chỉ mục, độ lặp khóa, số RID phải sắp và mức I/O ngẫu nhiên. Kích thước phía ngoài chỉ là một yếu tố. Một phía ngoài lớn nhưng khóa lặp nhiều có thể làm $C_{index}$ lớn vì nhiều lần tra và đọc ngẫu nhiên; phải ước lượng tổng chi phí, không suy từ kích thước đơn thuần.
:::

## 11. Recitation 15.5 và khép học phần

**Đặc tả.** $r,s$ chưa sắp và không có chỉ mục. Yêu cầu: tìm cách nối có số I/O thấp nhất và lượng bộ nhớ cần. "Bộ nhớ vô hạn" cho phép giữ toàn bộ quan hệ nhỏ, nhưng vẫn phải đọc cả hai đầu vào.

**Thuật toán.** Hai bước:

1. Nạp toàn bộ quan hệ nhỏ hơn vào bộ nhớ.
2. Đọc quan hệ lớn hơn từng khối và nối với quan hệ nhỏ.

**Chi phí và bộ nhớ.**

$$T=b_r+b_s,\qquad M_{\text{cần}}=\min(b_r,b_s)+2\text{ khối}.$$

**Lập luận cận.** Cận dưới là $b_r+b_s$ vì không có chỉ mục và thuật toán phải đọc cả hai quan hệ để bảo đảm không bỏ tuple. Hai khối thêm dành cho đầu vào lớn và đầu ra.

::: exercise
Vì sao cận dưới của số lần truyền khối là $b_r+b_s$, và vì sao cần thêm hai khối bộ nhớ ngoài quan hệ nhỏ?
:::

::: hint
Xét yêu cầu không bỏ tuple khi không có chỉ mục, và hai bộ đệm cho đầu vào lớn cùng đầu ra.
:::

::: solution
Không có chỉ mục nên thuật toán phải đọc mọi tuple của cả hai quan hệ để bảo đảm không bỏ cặp nào; mỗi quan hệ đọc đúng một lần cho $b_r+b_s$ lần truyền. Ngoài quan hệ nhỏ được giữ trong bộ nhớ, cần một khối đọc quan hệ lớn và một khối đầu ra, nên tổng là $\min(b_r,b_s)+2$ khối.
:::

## Tổng hợp

Bài đã đi qua sáu thuật toán nối theo năm cách tổ chức lại phép đọc. **Nested-Loop Join** xét mọi cặp tuple, áp dụng cho theta bất kỳ, chi phí $b_r+n_r b_s$. **Block Nested-Loop Join** giữ một nhóm $q$ khối ngoài và quét phía trong một lần cho cả nhóm, với $q=M-2$ khi vật chất hóa đầu ra và $q=M-1$ khi đầu ra chuyển tiếp. **Indexed Nested-Loop Join** tra chỉ mục cho từng tuple ngoài, chi phí là thời gian $b_r(t_T+t_S)+n_r c$, không so trực tiếp với số lần truyền khối. **Sort-Merge Join** dùng hai con trỏ trên hai dãy đã sắp, xuất tích Descartes của hai nhóm khóa trùng, và phải vật chất hóa hai dãy rồi đọc lại khi nối. **Hash Join trong bộ nhớ** xây bảng băm trên phía nhỏ thỏa $\alpha b_s+b_{in}+b_{out}\le M$, đọc mỗi đầu vào một lần. **Grace Hash Join** chia cả hai quan hệ bằng cùng hàm $h$, nối từng cặp phân hoạch, với pha phân hoạch cần $(p_h+1)b_b\le M$ và pha xây–dò cần $\alpha\max_i b_{s_i}+b_{in}+b_{out}\le M$; skew được xử lý bằng băm lại hoặc Block Nested.

Để chọn thuật toán, trước hết chốt nối theta hay nối bằng; tiếp đó chốt $n_r,n_s,b_r,b_s,M$ và bản sao khóa; kiểm trạng thái sắp và chỉ mục; tính truyền khối và seek cho cả hai hướng; cuối cùng kiểm nhóm lớn, phân hoạch lệch và đường lui. Ba ranh giới cần giữ là truyền khối với seek, bố trí bộ đệm của từng pha, và chi phí thời gian của chỉ mục với số lần truyền khối của thuật toán khác.
