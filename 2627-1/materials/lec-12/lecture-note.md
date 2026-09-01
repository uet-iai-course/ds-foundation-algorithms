# Bài 12 — Mô hình I/O và sắp xếp ngoài bộ nhớ

> Bộ bài giảng: [Deck Bài 12](lecture-12-mo-hinh-io-va-sap-xep-ngoai-bo-nho.html) — Giải thuật nền tảng của Khoa học dữ liệu, Học kỳ 1, năm học 2026–2027.

## Mở bài

Xét một bảng sự kiện lớn hơn bộ nhớ chính. Truy vấn `ORDER BY` trên một cột khóa phải trả về các dòng đã sắp, nhưng không thể đọc toàn bộ bảng vào RAM rồi dùng thuật toán sắp xếp trong bộ nhớ. Khi đó, thời gian CPU không đủ để mô tả chi phí: thuật toán còn phải kiểm soát số lần truyền khối và số lần định vị.

Bài này đi qua bốn sản phẩm quan sát được:

1. Mô hình hóa dữ liệu theo **bản ghi**, **khối**, **khung**, phân biệt **lần truyền khối** với **lần định vị (seek)**.
2. Chạy và chứng minh **sắp xếp trộn ngoài**: tạo dãy ban đầu, trộn nhiều đường và đếm số lượt.
3. Tính chi phí theo **điều kiện sau** (lần ghi cuối được tính hay không) và đánh giá hai đòn bẩy giảm lượt: tăng hệ số trộn $k$ hoặc giảm số dãy ban đầu $r_0$.
4. Chạy **chọn thay thế** (replacement selection) để tạo các dãy dài hơn.

## 1. Bài toán `ORDER BY` khi dữ liệu vượt RAM

Tình huống xuyên suốt: toán tử sắp xếp nhận một luồng đầu vào là bảng $N$ khối và phải cấp ra một luồng đầu ra đã sắp theo khóa. Có hai cách tiêu thụ đầu ra: **vật chất hóa** — ghi toàn bộ kết quả thành tệp rồi mới truyền tiếp; hoặc **truyền dòng** — cấp từng khối kết quả trực tiếp cho toán tử sau. Quyết định này thay đổi lần ghi cuối có được tính hay không, nên nó ảnh hưởng đến mọi công thức chi phí phía sau.

Giới hạn bộ nhớ được phát biểu bằng **số khung đệm** $B$: trong bộ nhớ chính chỉ có $B$ chỗ đặt khối dữ liệu. Mọi thuật toán phải tổ chức truy cập sao cho trạng thái thường trực không vượt $B$.

Vì bộ nhớ hạn chế, ta không thể đưa toàn bộ tệp vào một lần. Ý tưởng nền: chia dữ liệu thành các **đoạn con sắp xếp được trong bộ nhớ** (các dãy), rồi **trộn** các dãy lại thành một bằng nhiều lượt, mỗi lượt chỉ cần một phần nhỏ các khối cùng lúc.

## 2. Từ bản ghi đến khối và khung

Trước khi nói đến chi phí, cần chốt bốn đơn vị:

- **Bản ghi**: một phần tử dữ liệu của tệp, ví dụ `(kangaroo, 17)`. Trong mô hình này, bản ghi có kích thước cố định và không bắc qua biên khối.
- **Khối (block)**: đơn vị vật lý mà thiết bị đọc/ghi trong một lần truy cập, gồm một số bản ghi. Ký hiệu $b$ là số bản ghi mỗi khối chứa; số khối của tệp là
$$N=\lceil n/b\rceil$$
với $n$ là số bản ghi.
- **Khung (frame)**: một ô nhớ trong bộ nhớ chính vừa đúng một khối dữ liệu. Tổng số khung là $B$.
- **Thiết bị lưu trữ**: nơi lưu tệp; dữ liệu chỉ vào RAM bằng cách **truyền khối** vào một khung.

Khoảng cách giữa RAM và thiết bị rất lớn nên việc tải đi tải lại cùng một khối cần được hạn chế.

![Phân cấp lưu trữ và đơn vị truyền giữa thiết bị với bộ nhớ](img/lec-12/io-hierarchy.svg)

Dữ liệu đi từ thiết bị qua khối vào các khung đệm. Chú ý: dù tệp có $b$ bản ghi/khối, ta vẫn tính ngân sách theo **khối**, không theo bản ghi, vì truy cập nhỏ nhất là cả khối.

**Hệ số trộn.** Trong mô hình chung dành một khung đầu ra, ta phân bổ $B$ khung thành $k$ khung đầu vào và $1$ khung đầu ra, vậy hệ số trộn là
$$k = B-1.$$
Chẳng hạn $B=3$ cho $k=2$; $B=5$ cho $k=4$. Điều kiện để có thể trộn ($k\ge2$) là $B\ge3$.

::: exercise
Trong Bài 15.1, tệp có $n=12$ bản ghi và mỗi khối chứa $b=1$ bản ghi. Tính $N$.
:::

::: hint
Dùng $N=\lceil n/b\rceil$.
:::

::: solution
$N=\lceil 12/1\rceil=12$ khối.
:::

## 3. Bộ quản lý đệm và hai thước đo I/O

Bộ quản lý đệm trả lời câu hỏi "khối này đang ở khung nào trong bộ nhớ, hay phải đọc mới". Nó duy trì một bảng (hoặc cấu trúc tra cứu) từ mã khối đến vị trí khung.

![Yêu cầu khối rẽ thành trúng hoặc trượt trong bộ quản lý đệm](img/lec-12/buffer-manager.svg)

- **Trúng đệm (hit)**: yêu cầu trả về ngay vị trí khung đã chứa khối; không phát sinh truy cập thiết bị.
- **Trượt đệm (miss)**: chọn một **nạn nhân** để trục xuất; nếu khối nạn nhân **bẩn** (đã bị sửa trong RAM), phải **ghi** nó ra trước khi đọc khối mới vào khung đó.

Ví dụ với hai khung đang chứa `A` sạch và `B` bẩn, chuỗi yêu cầu `A, C` diễn ra như sau: yêu cầu `A` trúng đệm nên không có I/O; yêu cầu `C` trượt, nếu chọn `B` làm nạn nhân thì phải ghi `B` ra thiết bị trước, rồi đọc `C` vào khung vừa giải phóng. Vết ngắn này cho thấy một lần trượt có thể gây cả ghi lẫn đọc, tùy trạng thái của khối bị thay.

Từ đây có hai thước đo I/O riêng biệt:

- **Lần truyền khối (block transfer)**: mỗi lần đọc một khối từ thiết bị hoặc ghi một khối ra thiết bị. Đây là đơn vị chính để đếm chi phí.
- **Lần định vị / seek**: thao tác đặt đầu đọc về đúng vị trí trước một đoạn truy cập. Cùng số lần truyền khối có thể có số seek khác nhau, vì seek phụ thuộc thứ tự và vị trí các khối.

Không gộp hai khái niệm này: một kỹ thuật có thể giảm seek nhờ đọc nhiều khối liền nhau khi có nhiều khung mỗi dãy, dù số lần truyền khối không đổi.

::: exercise
Một lượt trộn đọc $N=12$ khối rồi ghi lại toàn bộ. Tính tổng số lần truyền khối.
:::

::: hint
Mỗi lượt gồm đọc toàn bộ $N$ khối và ghi toàn bộ $N$ khối.
:::

::: solution
$N$ lần đọc cộng $N$ lần ghi, tức $2N=24$ lần truyền khối.
:::

## 4. Đặc tả và tạo dãy ban đầu

**Đặc tả.** Đầu vào là tệp $N$ khối cần sắp theo khóa không giảm. Khả dụng là $B$ khung đệm. Điều kiện cần: $B\ge1$ để tạo dãy; nếu $N>B$, mô hình một khung đầu ra cần $B\ge3$. Xử lý ba trường hợp:

- $N=0$: tệp rỗng, không cần làm gì.
- $0<N\le B$: đọc hết rồi sắp trực tiếp trong bộ nhớ, chỉ tạo một dãy, $r_0=1$.
- $N>B$: đọc tối đa $B$ khối, sắp trong bộ nhớ, ghi thành dãy; lặp cho đến hết tệp.

**Pha 1 — tạo dãy ban đầu theo mẻ.** Lặp cho đến hết tệp: đọc tối đa $B$ khối vào bộ nhớ; sắp xếp các bản ghi trong mẻ; ghi kết quả thành một dãy đã sắp.

Số dãy ban đầu được xác định trước:
$$r_0=\left\lceil N/B\right\rceil.$$

```text
createRuns(file, B):
    runs ← danh sách rỗng
    while file còn khối chưa đọc:
        batch ← đọc tối đa B khối
        sắp các bản ghi trong batch theo khóa
        ghi batch thành một dãy; thêm dãy vào runs
    return runs
```

Mỗi vòng đọc ít nhất một khối nên thuật toán dừng. Mẻ cuối có thể chứa ít hơn $B$ khối.

![Hai pha tạo dãy rồi trộn của sắp xếp ngoài bộ nhớ](img/lec-12/external-sort.svg)

**Vết nguồn xuyên suốt.** Dùng 12 bản ghi của Bài 15.1, một bản ghi mỗi khối, sắp theo thuộc tính thứ nhất (tên con vật):

$$(kangaroo,17),(wallaby,21),(emu,1),(wombat,13),(platypus,3),(lion,8),$$
$$(warthog,4),(zebra,11),(meerkat,6),(hyena,9),(hornbill,2),(baboon,12).$$

Với $N=12$, $B=3$, mỗi lần đọc $B=3$ khối (3 bản ghi) và sắp theo tên. Bốn dãy ban đầu:

- $R_1=$ `emu, kangaroo, wallaby`
- $R_2=$ `lion, platypus, wombat`
- $R_3=$ `meerkat, warthog, zebra`
- $R_4=$ `baboon, hornbill, hyena`

Sau khi tạo, $r_0=4$.

::: exercise
Với $N=80$, $B=5$, tính $k$ và $r_0$.
:::

::: hint
$k=B-1$ và $r_0=\lceil N/B\rceil$.
:::

::: solution
$k=5-1=4$ và $r_0=\lceil 80/5\rceil=16$.
:::

## 5. Trộn nhiều đường

**Pha 2 — trộn.** Một lượt trộn lấy $k=B-1$ dãy (hoặc ít hơn ở nhóm cuối), dùng $k$ khung chứa **đầu của mỗi dãy** và một khung đầu ra. Lặp:

1. Chọn bản ghi nhỏ nhất trong số các đầu dãy (theo thứ tự sắp).
2. Chuyển nó sang khung đầu ra; khi khung đầu ra đầy thì ghi ra thiết bị.
3. Nếu khung đầu vào của dãy vừa rỗng, nạp khối kế tiếp của dãy đó; nếu hết thì loại dãy đó khỏi vòng lặp.

Điều kiện dừng: tất cả các khung đầu vào rỗng (đã xuất hết toàn bộ dữ liệu của các dãy).

```text
mergeGroup(runs, B):
    require 1 ≤ số dãy ≤ B − 1
    nạp khối đầu của mỗi dãy; giữ một khung đầu ra
    while còn dãy chưa cạn:
        x ← đầu dãy nhỏ nhất
        chuyển x sang khung đầu ra
        nếu khung nguồn cạn: nạp khối kế của dãy đó, nếu có
        nếu khung đầu ra đầy: ghi khung và làm rỗng nó
    nếu khung đầu ra còn dữ liệu: ghi phần còn lại
```

![Hai dãy đã sắp được trộn bằng cách chọn khóa đầu nhỏ nhất](img/lec-12/kway-merge.svg)

**Bất biến.** Mỗi dãy nguồn đã được sắp, nên đầu dãy là bản ghi nhỏ nhất trong phần chưa xuất của dãy đó. Khi lấy đầu nhỏ nhất ra, bản ghi kế tiếp trong cùng dãy có khóa $\ge$ bản ghi vừa lấy ra. Kết hợp với quy tắc "chọn đầu nhỏ nhất", đầu ra của lượt trộn là không giảm.

**Tính đúng (đúng đa tập, khóa không giảm).** Quy nạp theo số bản ghi đã xuất: tại mỗi bước, phần tử được xuất là nhỏ nhất trong toàn bộ dữ liệu chưa xuất, vì mỗi dãy là không giảm và ta luôn chọn đầu nhỏ nhất. Do đó:

- **Đúng đa tập**: mỗi bản ghi xuất hiện đúng một lần; nội dung được gộp lại đúng toàn bộ đầu vào.
- **Khóa không giảm**: dãy khóa xuất ra là không giảm từng cặp kề nhau.
- Khóa trùng vẫn cho thứ tự không giảm. Muốn phép sắp **ổn định**, tức giữ nguyên thứ tự ban đầu giữa các bản ghi có cùng khóa, phải thêm vị trí gốc làm khóa phụ; thuật toán cơ bản không có tính chất này.

**Vết.** Trộn $R_1$ và $R_2$ với $k=2$: đầu dãy là `emu` và `lion`; phép trộn xuất `emu` đầu tiên rồi `kangaroo`, `wallaby`, v.v., cho ra một dãy ghép sắp theo tên.

::: exercise
Vì sao chỉ cần giữ đầu hiện tại của mỗi dãy để chọn bản ghi kế tiếp?
:::

::: hint
Mỗi dãy đã được sắp, nên mọi bản ghi phía sau không nhỏ hơn đầu dãy hiện tại.
:::

::: solution
Phần tử nhỏ nhất còn lại của mỗi dãy nằm ngay ở đầu dãy. Vì vậy, phần tử nhỏ nhất trên toàn bộ dữ liệu chưa xuất phải là phần tử nhỏ nhất trong các đầu dãy.
:::

## 6. Số lượt và cây trộn

Mỗi lượt trộn hợp các nhóm $k$ dãy thành một, tức số dãy sau một lượt là $\lceil r/k\rceil$ với $r$ là số dãy hiện có. Ta lặp lượt trộn cho đến khi còn đúng một dãy.

Nếu bắt đầu với $r_0$ dãy, số lượt trộn thỏa
$$k^p \ge r_0 \quad\Longleftrightarrow\quad p=\lceil\log_k r_0\rceil,$$
chỉ dùng khi $N>B$ và $k\ge2$.

**Vết:** $r_0=4$, $k=2$: $4\rightarrow2\rightarrow1$ trong hai lượt, nên $p=2$.

![Bốn dãy được trộn theo cặp qua hai lượt để thành một dãy](img/lec-12/merge-tree.svg)

Cây trộn mô tả sự giảm số dãy: bốn dãy $R_1..R_4$ ghép cặp thành $M_1,M_2$, rồi thành một dãy kết quả. Chiều cao của cây (số mức trộn) chính là $p$.

Giá trị $p$ quyết định chi phí truyền khối phía sau, nên có hai hướng giảm $p$: tăng $k$ hoặc giảm $r_0$. Tuy nhiên, cách tiêu thụ kết quả còn quyết định lần ghi cuối có được tính hay không.

## 7. Vật chất hóa, truyền dòng và chi phí

Toán tử sau quyết định lần ghi cuối có được tính hay không:

- **Vật chất hóa**: mọi lượt (kể cả lượt cuối) ghi toàn bộ $N$ khối ra tệp; toán tử sau đọc lại tệp đó, nên lần ghi cuối **được tính**.
- **Truyền dòng**: các lượt trung gian vẫn ghi tệp, nhưng dãy kết quả của lượt cuối được **cấp trực tiếp** từng khối cho toán tử nhận và không ghi ra đĩa. Lần ghi cuối **không được tính**; chi phí của toán tử nhận cũng không tính chung.

![So sánh ghi tệp kết quả với truyền trực tiếp sang toán tử nhận](img/lec-12/materialize-pipeline.svg)

**Chi phí truyền dòng.** Mỗi lượt trung gian đọc $N$ và ghi $N$ khối. Với truyền dòng ta bỏ lần ghi cuối nhưng vẫn phải đọc dữ liệu vào lượt cuối:

$$C_{\mathrm{pipe}}=0 \quad (N=0);$$
$$C_{\mathrm{pipe}}=N \quad (0<N\le B,\text{ sắp trực tiếp trong bộ nhớ});$$
$$C_{\mathrm{pipe}}=N(2p+1) \quad (p\ge1).$$

**Chi phí vật chất hóa.** Nếu ghi mọi lượt, kể cả sao chép nhóm chỉ có một dãy:

$$C_{\mathrm{mat}}=2N(1+p).$$

Đây là cận trên khi triển khai bỏ qua việc sao chép nhóm chỉ gồm một dãy (nhóm đó không cần đọc–ghi lại).

**Vết nguồn:** $N=12$, $B=3$, $k=2$, $p=2$:

$$C_{\mathrm{mat}}=2\cdot12(1+2)=72,\qquad C_{\mathrm{pipe}}=12(2\cdot2+1)=60.$$

Hai công thức trên đếm **lần truyền khối**, không đếm seek, CPU, khối cuối chưa đầy hay chồng lấp I/O–CPU.

::: exercise
Với $N=80$, $B=5$ ta có $k=4$, $r_0=16$, $p=2$. Tính $C_{\mathrm{mat}}$ và giải thích vì sao truyền dòng tiết kiệm đúng một lần ghi $N$ khối.
:::

::: hint
Mỗi lượt tốn $2N$ lần truyền khối (đọc + ghi), có $1+p$ lượt. Truyền dòng bỏ đi đúng lần ghi của lượt cuối.
:::

::: solution
$$C_{\mathrm{mat}}=2N(1+p)=2\cdot80\cdot3=480.$$
Truyền dòng chỉ bỏ lần ghi $N$ khối cuối, nên $C_{\mathrm{pipe}}=480-N=400$, đúng bằng $N(2p+1)=80\cdot5=400$.
:::

## 8. Chi phí ngoài số lần truyền khối

Chi phí truyền khối không phải thước đo duy nhất; cần tách bốn loại:

- **Lần truyền khối**: mỗi lần đọc/ghi một khối. Đây là thước đo chính ($C_{\mathrm{mat}}, C_{\mathrm{pipe}}$ đếm loại này).
- **Lần định vị (seek)**: thao tác đặt đầu đọc trước một đoạn truy cập. Cùng số lần truyền khối có thể có số seek khác nhau, vì seek phụ thuộc thứ tự và vị trí các khối trên đĩa.
- **Thời gian CPU**: thời gian so sánh và trộn trong bộ nhớ; thường nhỏ hơn nhiều so với truy cập thiết bị nên bị bỏ qua trong ước lượng khối.
- **Bộ nhớ**: số khung đệm $B$ là giới hạn trạng thái thường trực; vượt $B$ là vi phạm điều kiện trước của thuật toán.

Nếu các đầu dãy được giữ trong hàng đợi ưu tiên, mỗi bản ghi tốn $O(\log k)$ để chọn và cập nhật đầu nhỏ nhất. Qua $p$ lượt, phần trộn tốn $O(np\log k)$ thời gian CPU; chi phí sắp các mẻ ban đầu được tính riêng. Bộ nhớ làm việc của phép trộn là $O(B)$ khối.

Đòn bẩy giảm seek là cấp **nhiều khung cho mỗi dãy đầu vào**, gọi là **đệm dài**. Gọi $b_b\in\mathbb{Z}$, $b_b\ge1$ là số khung dành cho mỗi dãy. Với một khung đầu ra:

$$k=\left\lfloor\frac{B-1}{b_b}\right\rfloor.$$

Nếu đầu ra cũng dùng $b_b$ khung:

$$k=\left\lfloor\frac{B}{b_b}\right\rfloor-1.$$

Hai công thức trên được suy ra từ phân bổ khung; nguồn Bài 15.9 chỉ nêu đánh đổi định tính. Với $B=11$, $b_b=2$: hai giá trị lần lượt là $5$ và $4$. Mỗi khung thêm cho một dãy giúp đọc nhiều khối liền nhau hơn, ít seek hơn, nhưng làm giảm $k$ (ít dãy trộn đồng thời) nên có thể tăng $p$.

::: exercise
Với $B=11$, $b_b=2$ và mô hình một khung đầu ra, tính $k$. Nếu đầu ra cũng dùng $b_b$ khung, tính $k$ theo công thức thứ hai.
:::

::: hint
Dùng $k=\lfloor(B-1)/b_b\rfloor$ rồi $k=\lfloor B/b_b\rfloor-1$.
:::

::: solution
$$k=\left\lfloor\frac{11-1}{2}\right\rfloor=5;\qquad k'=\left\lfloor\frac{11}{2}\right\rfloor-1=4.$$
:::

## 9. Chọn thay thế: trạng thái và vết chạy

**Chọn thay thế** (Replacement Selection) giảm $r_0$ từ phía tạo dãy: thay vì đọc $B$ khối rồi ghi hẳn thành dãy, nó xây dựng các dãy dài hơn bằng một **đống** (heap) chứa $H$ bản ghi. Giữ $B$ tính theo khối, $H$ tính theo bản ghi — không được trộn lẫn.

Khi đọc một bản ghi mới, phân loại theo khóa của bản ghi cuối cùng đã xuất ra của dãy hiện tại:

- **Hoạt động**: khóa $\ge$ khóa cuối đã xuất → đưa vào đống của dãy hiện tại.
- **Đóng băng**: khóa $<$ khóa cuối đã xuất → tách riêng, làm hạt giống của dãy kế tiếp.

![Hàng đợi ưu tiên xuất khóa nhỏ nhất và đóng băng khóa quá nhỏ](img/lec-12/replacement-selection.svg)

![Ba dãy chọn thay thế lần lượt có bảy, ba và hai khóa](img/lec-12/replacement-runs.svg)

Hai trạng thái tách biệt nhau: đống hiện tại chỉ chứa bản ghi hoạt động; phần đóng băng không được kích hoạt cho tới khi dãy hiện tại kết thúc.

```text
replacementSelection(input, H):
    nạp tối đa H bản ghi đầu vào vào đống hoạt động
    while đống hoạt động hoặc còn bản ghi đóng băng:
        nếu đống hoạt động rỗng:
            kết thúc dãy; kích hoạt mọi bản ghi đóng băng
        x ← lấy khóa nhỏ nhất đang hoạt động; xuất x
        nếu đầu vào còn bản ghi y:
            nếu key(y) ≥ key(x): thêm y vào đống hoạt động
            ngược lại: đánh dấu y là đóng băng
    kết thúc dãy cuối nếu dãy này có dữ liệu
```

**Vết chạy trên 12 tên.** Vết nguồn có một bản ghi mỗi khối nên giá trị số $H=B=3$ trùng nhau. Thứ tự đọc: `kangaroo, wallaby, emu, wombat, platypus, lion, warthog, zebra, meerkat, hyena, hornbill, baboon`.

**Dãy 1:** nạp đống `{emu, kangaroo, wallaby}` → xuất `emu`; nạp `wombat` vào trạng thái hoạt động → xuất `kangaroo`; nạp `platypus` vào trạng thái hoạt động → xuất `platypus`; đóng băng `lion` → xuất `wallaby`; nạp `warthog` vào trạng thái hoạt động → xuất `warthog`; nạp `zebra` vào trạng thái hoạt động → xuất `wombat`; đóng băng `meerkat` → xuất `zebra`, rồi đóng băng `hyena`. Dãy thứ nhất là `emu, kangaroo, platypus, wallaby, warthog, wombat, zebra`.

**Dãy 2:** kích hoạt `{hyena, lion, meerkat}` → xuất `hyena`; vì `hornbill < hyena`, đóng băng `hornbill`; xuất `lion`, rồi đóng băng `baboon`; xuất `meerkat`. Dãy thứ hai là `hyena, lion, meerkat`.

**Dãy 3:** kích hoạt `{baboon, hornbill}` rồi xuất `baboon`, `hornbill`. Ba dãy cuối:

$$[\text{emu, kangaroo, platypus, wallaby, warthog, wombat, zebra}],$$
$$[\text{hyena, lion, meerkat}],\quad [\text{baboon, hornbill}].$$

Với 12 tên và $H=3$, chọn thay thế chỉ tạo $r_0=3$ dãy thay vì 4 như tạo theo mẻ, nhờ các bản ghi nhỏ được chuyển sang dãy sau.

## 10. Tính đúng và giới hạn của chọn thay thế

Chọn thay thế giảm $r_0$ từ phía tạo dãy ban đầu thay vì đổi hệ số trộn $k$. Mệnh đề cần chứng minh là: mỗi dãy sinh ra có khóa không giảm và hợp của các dãy đúng bằng đa tập đầu vào.

### Tính đúng
- **Bất biến:** trước mỗi lần xuất, đống hoạt động chứa đúng các bản ghi đã đọc nhưng chưa xuất và đủ điều kiện thuộc dãy hiện tại; mọi khóa hoạt động không nhỏ hơn khóa vừa xuất. Lấy khóa nhỏ nhất rồi chỉ kích hoạt khóa mới không nhỏ hơn nó duy trì bất biến.
- **Đa tập:** mỗi bản ghi được xuất đúng một lần; tan băng chỉ chuyển bản ghi sang dãy sau, không nhân đôi cũng không làm mất.
- **Điều kiện dừng:** đóng dãy khi đống không còn bản ghi hoạt động; toàn bộ thuật toán dừng khi cạn bản ghi đầu vào và ghi xong dãy cuối cùng.

### Chi phí
- Mỗi bản ghi được chèn và lấy khỏi hàng đợi ưu tiên một lần, nên thời gian là $O(n\log H)$.
- Đống chứa $O(H)$ bản ghi. $H$ đo theo bản ghi còn $B$ đo theo khung; chỉ trong vết một bản ghi/khối mới có cùng giá trị số $H=B=3$.

### Giới hạn $2H$ chỉ là quy tắc kinh nghiệm
Wisconsin CS764 nêu rằng độ dài dãy trung bình thường khoảng $2H$. Nguồn không đặc tả không gian xác suất, nên đây là quy tắc kinh nghiệm, không phải định lý hay bảo đảm trường hợp xấu. Dữ liệu gần như ngược thứ tự có thể cho dãy ngắn gần $H$; dữ liệu gần như đã sắp có thể cho dãy rất dài. Vì vậy:
- Không quy $r_0\approx \lceil N/(2H)\rceil$ thành công thức chính xác;
- Dùng $2H$ như một **điểm tham chiếu** để so sánh với mẻ tạo dãy $\lceil N/B\rceil$, vẫn phải đếm theo $N>B$ và $k\ge2$ như thường lệ.

::: exercise
Trong vết nguồn, sau khi xuất `platypus`, bản ghi kế tiếp là `lion`. Bản ghi này thuộc dãy hiện tại hay phải đóng băng?
:::

::: hint
So sánh theo thứ tự từ điển giữa `lion` và khóa vừa xuất `platypus`.
:::

::: solution
`lion < platypus`, nên `lion` phải đóng băng và chỉ được kích hoạt cho dãy kế tiếp.
:::

## 11. Từ ngân sách bộ nhớ đến chi phí

Toàn bộ Bài 12 cô đọng thành một chuỗi: từ **bộ nhớ** suy ra **dãy ban đầu và hệ số trộn**, từ đó suy ra **số lượt**, rồi **chi phí** theo đúng đầu ra.

| Bước | Công thức | Điều kiện dùng |
|---|---|---|
| Số khối dữ liệu | $N=\lceil n/b\rceil$ | luôn đúng |
| Dãy ban đầu (mẻ) | $r_0=\lceil N/B\rceil$ | ưu tiên mặc định |
| Hệ số trộn | $k=B-1$ | một khung đầu ra |
| Số lượt trộn | $p=\lceil\log_k r_0\rceil$ | **chỉ khi** $N>B$ và $k\ge2$ |
| Chi phí vật chất hóa | $C_{\mathrm{mat}}=2N(1+p)$ | ghi tệp cuối mỗi lượt (cận trên) |
| Chi phí truyền dòng | $C_{\mathrm{pipe}}=N(2p+1)$ | lượt cuối truyền dòng, không ghi |

### Ba vùng chi phí truyền dòng

$$
C_{\mathrm{pipe}}=
\begin{cases}
0, & N=0,\\
N, & 0<N\le B,\\
N(2p+1), & p\ge1.
\end{cases}
$$

Ở trường hợp giữa, thuật toán đọc $N$ khối, sắp trong bộ nhớ rồi cấp trực tiếp cho toán tử nhận; không ghi tệp trung gian.

### Chọn đầu ra quyết định chi phí
- **Vật chất hóa** ghi tệp kết quả cuối, nên tính cả lần ghi $N$ khối cuối.
- **Truyền dòng** cấp trực tiếp kết quả cho toán tử nhận, nên bỏ lần ghi cuối.
- Phải chốt cách tiêu thụ kết quả trước khi chọn công thức $C$.

### Hai đòn bẩy giảm số lượt

- Phân bổ ít khung hơn cho mỗi dãy có thể tăng $k$ và giảm $p$, nhưng có thể làm tăng số seek.
- Chọn thay thế có thể giảm $r_0$, đổi lại chi phí CPU $O(n\log H)$ và không có bảo đảm dãy dài $2H$.

Chuỗi quyết định là $B\to(r_0,k)\to p\to C$: cách tạo dãy quyết định $r_0$, cách chia khung quyết định $k$, hai đại lượng này quyết định $p$, còn điều kiện đầu ra quyết định công thức $C$.

## 12. Bài tập từ giáo trình

Ba bài dưới đây được dịch và chia bước nhưng giữ nguyên dữ kiện cùng yêu cầu toán học của nguồn.

### Bài 15.1
::: exercise
Giả sử mỗi khối chỉ chứa một bản ghi và bộ nhớ chứa tối đa ba khối. Hãy chỉ ra các dãy được tạo ở mỗi lượt của sắp xếp trộn ngoài khi sắp theo thuộc tính thứ nhất:

`(kangaroo,17), (wallaby,21), (emu,1), (wombat,13), (platypus,3), (lion,8), (warthog,4), (zebra,11), (meerkat,6), (hyena,9), (hornbill,2), (baboon,12)`.
:::
::: hint
Trước hết chia đầu vào thành bốn nhóm liên tiếp, mỗi nhóm ba bản ghi, rồi sắp từng nhóm. Lời giải nguồn trộn ba dãy đầu ở lượt kế; cần giải thích vì sao lịch ba khung đó khả thi khi một bản ghi lấp đầy một khối.
:::
::: solution
Lượt tạo dãy cho:

- $R_1=$ `[emu,kangaroo,wallaby]`;
- $R_2=$ `[lion,platypus,wombat]`;
- $R_3=$ `[meerkat,warthog,zebra]`;
- $R_4=$ `[baboon,hornbill,hyena]`.

Theo lời giải nguồn, lượt kế trộn $R_1,R_2,R_3$ thành `[emu,kangaroo,lion,meerkat,platypus,wallaby,warthog,wombat,zebra]` và giữ $R_4$. Lượt cuối cho `[baboon,emu,hornbill,hyena,kangaroo,lion,meerkat,platypus,wallaby,warthog,wombat,zebra]`.

Lịch ba khung khả thi trong đúng bài này vì một bản ghi lấp đầy một khối: xuất đầu nhỏ nhất làm rỗng một khung, bản ghi đó cũng làm đầy khối đầu ra để ghi ngay, rồi khung vừa dùng nạp đầu kế của chính dãy. Đây là biến thể nguồn, không cho quy tắc trộn chung $k=B$; phần giảng vẫn dành một khung đầu ra và dùng $k=B-1$.
:::

### Bài 15.9
::: exercise
Trong sắp xếp trộn ngoài, giả sử dùng $b_b$ khung cho mỗi dãy thay vì một khung. Khi tổng bộ nhớ không đổi, việc tăng $b_b$ ảnh hưởng thế nào đến tổng số lần truyền khối và số lần định vị?
:::
::: hint
Cấp nhiều khung hơn cho mỗi dãy cho phép đọc một đoạn dài hơn sau mỗi lần định vị, nhưng làm giảm số dãy trộn đồng thời.
:::
::: solution
Cấp nhiều khung cho mỗi dãy giảm số lần định vị vì mỗi lần có thể đọc một đoạn dài hơn. Tuy nhiên, với tổng $B$ cố định, hệ số trộn $k$ giảm và số lượt $p$ có thể tăng; khi đó tổng số lần truyền khối cũng có thể tăng. Vì vậy phải cân bằng số lần định vị với số dãy trộn đồng thời. Hai công thức ở Phần 8 chỉ là suy ra từ cách chia khung; bài nguồn nêu đánh đổi này ở mức định tính.
:::

### Bài 13.5
::: exercise
Bộ quản lý đệm phải nhanh chóng biết một khối có đang ở trong đệm hay không và, nếu có, nó nằm ở khung nào. Với một đệm cơ sở dữ liệu rất lớn, nên dùng cấu trúc dữ liệu trong bộ nhớ nào?
:::
::: hint
Dùng mã khối làm khóa tra cứu và vị trí khung làm giá trị.
:::
::: solution
Dùng bảng băm ánh xạ mã khối đến vị trí khung. Hàm băm xác định xô; trong xô có thể tìm tuyến tính hoặc dùng một cách xử lý va chạm tương đương. Cấu trúc này cho phép xác định nhanh cả sự hiện diện của khối lẫn khung đang chứa nó.
:::

---

## Nguồn

- *Database System Concepts*, 7e, Chương 12–13 và phần sắp xếp ngoài bộ nhớ Chương 15 (trục).
  - Ch.12, trang chiếu 10–11 và 32–33: hệ phân cấp và truy cập khối; Ch.13, trang chiếu 2–3 và 19–20: bản ghi–khối và bộ quản lý đệm.
  - Ch.15, trang chiếu 17–23: hai pha External Merge Sort; 51–59: truyền dòng không ghi kết quả cuối.
- Wisconsin CS764, bài 2, trang 16–20: Replacement Selection; nhận định độ dài trung bình **khoảng $2H$** là quy tắc kinh nghiệm, không gán mô hình xác suất.
- Recitation: Bài 15.1 (đề trang in 47; lời giải PDF 1/trang in 111), Bài 15.9 (đề PDF 2/trang in 48; lời giải PDF 5/trang in 115), Bài 13.5 (đề PDF 2/trang in 42; lời giải PDF 5/trang in 95).
- Hình SVG trong `img/lec-12/`.
