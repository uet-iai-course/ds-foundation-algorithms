# Bài 14 — Chỉ mục văn bản và chỉ mục không gian

> Bộ bài giảng: [Deck Bài 14](lecture-14-chi-muc-van-ban-va-chi-muc-khong-gian.html) — Giải thuật nền tảng của Khoa học dữ liệu, Học kỳ 1, năm học 2026–2027.

## Mở bài

Bài 13 đặt khóa có thứ tự vào B+-Tree hoặc ngăn băm. Các khóa đó là một cột hoặc tổ hợp cột có quan hệ so sánh tuyến tính. Bài này chuyển sang hai miền không có một khóa tuyến tính tự nhiên: thuật ngữ xuất hiện bên trong tài liệu và vị trí của vật thể trong không gian. Một từ khóa không phải một giá trị số có thứ tự; một điểm $(x,y)$ cũng không có một thứ tự duy nhất nào bảo toàn mọi quan hệ lân cận.

Một yêu cầu chung xuyên suốt bài: chỉ mục hiệu quả khi biểu diễn của nó tạo được một **tập ứng viên không bỏ nghiệm**, còn bước **tinh lọc** kiểm đúng đối tượng thật. Bài xét ba dòng truy vấn:

- **Văn bản**: thuật ngữ dẫn đến danh sách đảo rồi phép trộn Boolean.
- **Vật thể không gian**: hộp bao, lọc, rồi tinh lọc.
- **Hàng xóm gần**: miền hoặc ball, cận dưới, rồi điều kiện cắt nhánh.

Một số cấu trúc trả đáp án chính xác ngay (phép Boolean trên danh sách đảo, truy vấn 1-NN trên cây miền hoặc cây ball). Một số chỉ tạo ứng viên và phải được tinh lọc (R-tree, Z-order). Nhiệm vụ của bài là đặc tả đúng cấu trúc, chạy đúng thuật toán và phân tích chi phí theo đúng mô hình RAM hoặc I/O trang mà không trộn hai đơn vị đó với nhau.

## 1. Hai miền dữ liệu và tuyến ứng viên–tinh lọc

**Vai trò và nhu cầu.** Một kho tài liệu web nằm trên bộ nhớ phụ phải trả lời truy vấn từ khóa; một tập ảnh vệ tinh với các đối tượng có vị trí phải trả lời truy vấn vùng và lân cận. Ở quy mô lớn, quét toàn bộ dữ liệu cho mỗi truy vấn không đáp ứng được thời gian. Cả hai miền đều cần một biến đổi đưa dữ liệu về dạng định vị nhanh hơn quét, nhưng hai miền không chia sẻ một biểu diễn chung: văn bản được tổ chức theo thuật ngữ, hình học được tổ chức theo vị trí.

**Tuyến ứng viên–tinh lọc.** Với văn bản, một từ khóa tương ứng với một danh sách docID có sẵn; phép Boolean trộn các danh sách này thành tập kết quả chính xác. Với hình học, một ô hoặc hộp bao giao với vùng hỏi chỉ cho biết vật thể *có khả năng* giao; hình thật phải được kiểm lại. Đây là hai mức độ cam kết khác nhau:

- Cấu trúc trả đáp án chính xác khi mọi phần tử trong tập ứng viên của nó đều là đáp án thật.
- Cấu trúc tạo ứng viên khi một ô hoặc hộp bao có thể chứa vật thể không giao vùng; khi đó phải có bước tinh lọc.

Lập luận đúng của mọi bước lọc hoặc cắt nhánh đều quy về một mệnh đề: **mọi đối tượng thỏa điều kiện, nếu tồn tại, vẫn còn trong tập ứng viên**. Nếu lọc bỏ được một nghiệm thì chỉ mục sai. Bài dùng lại nguyên tắc này ở bốn chỗ: danh sách đảo so khớp từng docID, MBR chứa hình thật, cận dưới khoảng cách, và đoạn Z-order phủ đủ mọi ô của vùng hỏi.

## 2. Danh sách đảo, phép Boolean và chi phí

**Vai trò và nhu cầu.** Một tài liệu chứa nhiều thuật ngữ, và một thuật ngữ xuất hiện trong nhiều tài liệu. Ánh xạ tài liệu sang thuật ngữ chỉ phổ biến được một tài liệu đang xét, không giúp tìm nhanh mọi tài liệu chứa một từ. **Chỉ mục đảo** đảo ngược ánh xạ: mỗi thuật ngữ trỏ tới danh sách các docID chứa nó.

![Quy trình từ tài liệu qua tách thuật ngữ đến từ điển và danh sách tài liệu đảo](img/lec-14/text-index.svg)

**Đặc tả.** Gọi $D$ là tập tài liệu. Với thuật ngữ $t$, danh sách đảo là

$$P_t=\langle d_1,d_2,\ldots,d_m\rangle,\qquad d_1<d_2<\cdots<d_m.$$

Mỗi $d_i$ là một mã tài liệu (docID) thuộc $D$. Danh sách tăng **nghiêm ngặt**: một docID xuất hiện nhiều nhất một lần. Điều kiện trước của phép trộn là mọi danh sách đã được sắp như trên. Đây là biểu diễn có trật tự, không phải một tập toán học trừu tượng; phép trộn tận dụng trật tự này.

Ví dụ chạy tay dùng hai danh sách:

- "cây" $=[1,3,4,8]$,
- "tìm" $=[2,3,6,8]$.

Nếu thuật ngữ $t$ xuất hiện nhiều lần trong cùng một tài liệu, số lần xuất hiện là dữ liệu đi kèm docID, không phải docID lặp. Phần 3 sẽ làm rõ điều này.

Danh sách đảo **không phải một tập chưa sắp**. Hai con trỏ chỉ trộn tuyến tính khi docID nằm trong một danh sách tăng nghiêm ngặt.

**Ví dụ AND — hai con trỏ.** Để tính giao của $P=[1,3,4,8]$ và $Q=[2,3,6,8]$, dùng hai con trỏ $i,j$:

$$1<2 \Rightarrow i{+}{+}; \quad 3>2 \Rightarrow j{+}{+}; \quad 3=3 \Rightarrow \text{thêm }3,\ i{+}{+},j{+}{+}; \quad 4<6 \Rightarrow i{+}{+}; \quad 8=8 \Rightarrow \text{thêm }8.$$

Kết quả $[3,8]$. Mỗi bước so hai đầu và tiến con trỏ có giá trị nhỏ hơn, hoặc tiến cả hai khi bằng nhau và xuất kết quả.

**Giả mã — giao (AND):**

```text
i ← 0; j ← 0; A ← []
while i < |P| và j < |Q|:
  nếu P[i] = Q[j]: thêm P[i] vào A; i++; j++
  ngược lại nếu P[i] < Q[j]: i++
  ngược lại: j++
trả A
```

**Bất biến.** Sau mỗi bước, $A$ chứa đúng giao của hai tiền tố đã xử lý; mọi docID nhỏ hơn cả hai đầu hiện tại đã được quyết định. Điều này đúng vì các danh sách tăng nghiêm ngặt. Chẳng hạn, khi $P[i]<Q[j]$, không phần tử nào từ $Q[j]$ trở đi có thể bằng $P[i]$, nên bỏ $P[i]$ là an toàn.

**Dừng.** Mỗi bước tăng ít nhất một con trỏ. Hai con trỏ đều bị chặn bởi độ dài danh sách, nên vòng lặp kết thúc khi một bên cạn.

**Chi phí.** Mỗi mục của hai danh sách được xét nhiều nhất một lần, nên thời gian CPU là $O(|P|+|Q|)$. Nếu tính cả vùng chứa kết quả, bộ nhớ là $O(|A|)$.

**OR (hợp).** Phép hợp giống AND nhưng xử lý đủ ba quan hệ giữa hai đầu khác nhau. Bảng dưới tổng hợp OR ($P\cup Q$) và NOT ($S\setminus P_t$) dùng hai con trỏ:

| Hai đầu | $P\cup Q$ | $S\setminus P_t$ |
|---|---|---|
| trái < phải | xuất trái; tiến trái | xuất đầu $S$; tiến $S$ |
| trái = phải | xuất một lần; tiến cả hai | bỏ; tiến cả hai |
| trái > phải | xuất phải; tiến phải | tiến $P_t$ |

Khi một bên cạn, phép hợp chép toàn bộ đuôi của danh sách còn lại; phép hiệu chỉ chép đuôi của $S$. Slide nguồn in nhầm phép hợp thành giao; bài này giữ **hợp** theo đặc tả của sách.

**NOT (hiệu).** NOT không có nghĩa nếu chưa xác định **tập nền** $S\subseteq D$. $S$ thường là tập ứng viên của phần còn lại trong biểu thức Boolean. Phép hiệu $S\setminus P_t$ giữ mọi docID của $S$ không xuất hiện trong $P_t$.

**Ví dụ chạy tay NOT.** Với $S=[1,2,3,4,6,8]$ và $P_t=[2,3,6,8]$:

- $1<2$: xuất 1, tiến $S$;
- $2=2$: bỏ 2, tiến cả hai;
- $3=3$: bỏ 3, tiến cả hai;
- $4<6$: xuất 4, tiến $S$;
- $6=6$ và $8=8$: bỏ, tiến cả hai.

Kết quả $S\setminus P_t=[1,4]$.

**Giả mã — hiệu (NOT):**

```text
i ← 0; j ← 0; A ← []
while i < |S| và j < |Pt|:
  nếu S[i] < Pt[j]: thêm S[i] vào A; i++
  ngược lại nếu S[i] = Pt[j]: i++; j++
  ngược lại: j++
chép mọi phần tử còn lại của S vào A
trả A
```

**Bất biến.** $A$ chứa đúng hiệu của hai phần đã xử lý. Khi $S[i]=P_t[j]$, phần tử thuộc giao và bị loại; khi $S[i]>P_t[j]$, $P_t[j]$ không nằm trong $S$ ở vị trí này nên bỏ $P_t[j]$; khi $S[i]<P_t[j]$, $S[i]$ chắc chắn không bị $P_t$ chứa nên được xuất.

**Dừng.** Mỗi bước tiến ít nhất một con trỏ, hai con trỏ có cận trên hữu hạn nên vòng lặp kết thúc. Khi $P_t$ cạn, mọi phần tử còn lại của $S$ đều không thuộc $P_t$ và được chép vào kết quả.

**Chi phí.** $O(|S|+|P_t|)$ thời gian CPU; bộ nhớ phụ $O(|A|)$.

::: exercise
Cho $S=[1,2,4,5,6]$ và $P_t=[2,4,6]$. Hãy chạy phép hiệu bằng hai con trỏ và cho biết kết quả, bất biến sau khi xử lý tiền tố $S=[1,2,4]$ và điều kiện dừng.
:::

::: hint
Khi hai đầu bằng nhau thì bỏ; khi đầu $S$ nhỏ hơn thì xuất; khi đầu $S$ lớn hơn thì bỏ đầu $P_t$. Theo dõi riêng giá trị 1 và 5.
:::

::: solution
Các bước: $1<2$ xuất 1; $2=2$ bỏ; $4=4$ bỏ; $5<6$ xuất 5; $6=6$ bỏ. Kết quả $[1,5]$. Sau khi xử lý tiền tố $S=[1,2,4]$, $P_t$ đang ở 6: $A=[1]$, mọi giá trị dưới 6 đã được quyết định. Sau bước $6=6$, cả hai con trỏ cùng cạn nên vòng lặp kết thúc và không còn đuôi để chép.
:::

## 3. Vị trí–tần suất và bố trí danh sách trên đĩa

**Vai trò.** Kết quả Boolean chỉ dùng sự có mặt của thuật ngữ. Tìm kiếm toàn văn còn cần xếp hạng và truy vấn cụm từ, vì vậy mỗi mục của danh sách đảo có thể mang thêm **vị trí** (docID cùng vị trí xuất hiện trong tài liệu) và **tần suất** (số lần xuất hiện trong tài liệu). Vị trí cho phép truy vấn cụm từ; tần suất hỗ trợ xếp hạng độ liên quan.

**Đặc tả.** Dữ liệu vị trí–tần suất đi **kèm docID**, không phải docID lặp. Việc lặp docID trong danh sách sẽ phá vỡ tính tăng nghiêm ngặt và làm phép trộn Boolean sai: một tài liệu chứa từ hai lần vẫn chỉ là một docID trong kết quả. Một mục của danh sách có dạng (docID, danh sách vị trí, tần suất), và docID vẫn xuất hiện đúng một lần.

**Bố trí trên đĩa.** Một kho tài liệu lớn không vừa RAM; danh sách đảo được đặt trên bộ nhớ phụ. Bài này dùng lại tuyến xử lý của Bài 12–13:

1. Sinh các cặp (thuật ngữ, docID) cho mọi thuật ngữ có mặt trong mọi tài liệu.
2. Sắp xếp ngoài các cặp theo (thuật ngữ, docID).
3. Gom các cặp cùng thuật ngữ thành từng danh sách đảo.
4. Dùng B+-Tree ánh xạ thuật ngữ tới **trang đầu** của danh sách.
5. Đọc tuần tự các trang liên tiếp của mỗi danh sách.

![B+-Tree ánh xạ thuật ngữ tới các trang danh sách đảo liên tiếp trên đĩa](img/lec-14/inverted-disk.svg)

Xếp danh sách liên tiếp trên đĩa giảm số lần định vị: một lần tìm trong B+-Tree để lấy địa chỉ trang đầu, rồi đọc tuần tự thay vì truy nhập ngẫu nhiên từng trang.

**Đơn vị chi phí.** Phép trộn Boolean ở Phần 2 được đo theo số mục danh sách (mô hình RAM). Khi danh sách nằm trên đĩa, chi phí thật gồm số lần định vị trong B+-Tree, số trang phải đọc và số mục trong mỗi trang. Hai đơn vị này không được cộng trực tiếp với nhau. Vị trí–tần suất không đổi số mục bị quét khi trộn Boolean, nhưng làm mỗi mục lớn hơn và có thể tăng số trang phải đọc.

::: exercise
Nếu vị trí và tần suất được mô hình bằng cách chèn docID lặp thay vì dữ liệu kèm theo, phép trộn AND ở Phần 2 bị hỏng như thế nào?
:::

::: hint
Xem điều kiện tăng nghiêm ngặt và ý nghĩa của "cùng docID" trong giao.
:::

::: solution
Khi docID lặp, danh sách không còn tăng nghiêm ngặt: cùng một docID xuất hiện hai lần. Hai con trỏ trộn dựa vào trật tự nghiêm ngặt để bỏ tiền tố một cách an toàn; nếu có docID lặp, phép so $P[i]<Q[j]$ có thể quyết định sai, và một docID chứa từ có thể bị xuất hai lần hoặc bị loại nhầm. Vì vậy số lần xuất hiện phải nằm ở dữ liệu kèm theo, không phải ở danh sách.
:::

## 4. Độ chính xác và độ bao phủ

**Vai trò.** Phép trộn Boolean trả một tập docID thỏa điều kiện. Trong tìm kiếm toàn văn, hệ thống còn chọn một **ngưỡng** để xác định tập kết quả trả về từ tập các docID được xếp hạng. Hai thước đo phổ biến là **độ chính xác** (precision) và **độ bao phủ** (recall).

**Đặc tả.** Xét một truy vấn có tập phù hợp chuẩn $G$ — tập tài liệu được đánh giá là thật sự phù hợp, do con người đối chiếu, không phải do hệ thống sinh ra. Một hệ thống trả về tập $R$. Khi đó:

$$\operatorname{precision}(R)=\frac{|R\cap G|}{|R|},\qquad \operatorname{recall}(R)=\frac{|R\cap G|}{|G|}.$$

Độ chính xác đo tỷ lệ tài liệu đúng trong tập trả về. Độ bao phủ đo tỷ lệ tài liệu phù hợp chuẩn đã được tìm thấy. Thuật ngữ "độ chính xác" ở đây là chất lượng của truy hồi xếp hạng, **không phải** tính đúng của lọc–tinh lọc hay của 1-NN chính xác trong các cụm sau.

**Ví dụ chạy tay.** Dùng xuyên suốt cụm đánh giá:

- Tập phù hợp chuẩn $G=\{1,3,8\}$.
- Ngưỡng chặt cho $R_h=\{3,8\}$.
- Ngưỡng nới cho $R_l=\{1,2,3,6,8\}$.

Với $R_h$: giao với $G$ là $\{3,8\}$, nên

$$\operatorname{precision}(R_h)=\frac{|\{3,8\}|}{|\{3,8\}|}=\frac22=1,\qquad \operatorname{recall}(R_h)=\frac{|\{3,8\}|}{|G|}=\frac23.$$

Tài liệu 1 phù hợp nhưng bị ngưỡng chặt bỏ sót, nên recall chỉ đạt $2/3$.

Với $R_l$: giao với $G$ là $\{1,3,8\}$, nên

$$\operatorname{precision}(R_l)=\frac{|\{1,3,8\}|}{|\{1,2,3,6,8\}|}=\frac35,\qquad \operatorname{recall}(R_l)=\frac{|G|}{|G|}=1.$$

**Đánh đổi.** Nới ngưỡng thêm tài liệu 1 phù hợp nên recall tăng lên 1, đồng thời thêm docID 2 và 6 không phù hợp nên precision giảm từ 1 xuống $3/5$. Ví dụ này minh họa đánh đổi, nhưng không được khái quát thành định luật đơn điệu cho mọi hệ xếp hạng.

**Trường hợp biên.** Nếu $R=\varnothing$, mẫu số của precision bằng 0; nếu $G=\varnothing$, mẫu số của recall bằng 0. Một đánh giá phải nêu quy ước cho hai trường hợp này, chẳng hạn precision bằng 0 khi $R$ rỗng và recall được xem là 1 khi không có tài liệu phù hợp nào cần tìm, rồi giữ quy ước đó nhất quán.

::: exercise
Với $G=\{1,3,8\}$, một hệ thống trả về $R=\{3,4\}$. Tính precision và recall, rồi nêu tài liệu nào làm giảm precision so với ngưỡng chặt ở ví dụ trên.
:::

::: hint
$R\cap G$ là $\{3\}$; chia cho $|R|$ và $|G|$.
:::

::: solution
$R\cap G=\{3\}$, nên precision $=|\{3\}|/|\{3,4\}|=1/2$ và recall $=|\{3\}|/|\{1,3,8\}|=1/3$. Tài liệu 4 không phù hợp chuẩn làm giảm precision xuống dưới giá trị 1 của $R_h$; recall cũng thấp vì chỉ tìm được 1 trong 3 tài liệu phù hợp.
:::

## 5. Truy vấn không gian và R-tree lọc–tinh lọc

**Vai trò và nhu cầu.** Ảnh vệ tinh lớn chứa các đối tượng có vị trí như trạm xăng, các ô ảnh. Hai đầu ra điển hình là danh sách vật thể giao một cửa sổ, hoặc trạm xăng gần một điểm. Quét toàn bộ dữ liệu cho mỗi cửa sổ hoặc mỗi điểm hỏi không khai thác được thông tin vị trí.

**Phân loại truy vấn.** Loại truy vấn quyết định cấu trúc:

![Ba loại truy vấn không gian gồm điểm, phạm vi và hàng xóm gần nhất](img/lec-14/spatial-queries.svg)

- **Truy vấn điểm**: trả vật thể đúng tại một tọa độ. Nếu so sánh hai tọa độ chính xác, có thể dùng cây có thứ tự trên khóa ghép $(x,y)$.
- **Truy vấn phạm vi**: trả mọi vật thể giao một vùng. Vật thể là đa giác, không phải điểm, nên khoảng giao không quy về so sánh khóa đơn.
- **Truy vấn hàng xóm gần nhất (1-NN)**: trả điểm có khoảng cách nhỏ nhất tới điểm hỏi, và có thể có nhiều điểm đồng hạng.

**Lọc–tinh lọc.** Hình dạng thật của một vật thể đắt để kiểm giao. Mỗi vật thể gắn một **hình chữ nhật bao nhỏ nhất** (minimum bounding rectangle, MBR) chứa nó.

![Bước lọc bằng hộp bao tạo ứng viên rồi bước tinh lọc kiểm hình học thật](img/lec-14/filter-refine.svg)

Bước **lọc** kiểm nhanh xem MBR của vật thể có giao vùng hỏi hay không; nếu không giao thì vật thể chắc chắn không giao và bị loại. Bước **tinh lọc** chỉ kiểm hình thật của các ứng viên còn lại.

**Mệnh đề không bỏ nghiệm.** Nếu hình thật $F$ giao vùng $Q$ thì MBR của $F$ cũng giao $Q$, vì $F\subseteq \operatorname{MBR}(F)$. Do đó bước lọc theo MBR không bao giờ loại một vật thể thật sự giao $Q$. Chiều ngược lại không đúng: MBR có thể giao $Q$ dù hình thật không giao. Trường hợp này là **dương tính giả** và phải được bước tinh lọc loại.

**Cấu trúc R-tree.** R-tree tổ chức các MBR theo cây:

- **Nút trong** chứa MBR của từng cây con.
- **Lá** chứa vật thể hoặc MBR của từng vật thể.
- MBR của các cây con **được phép chồng lấn**, khác với B+-Tree nơi các khoảng tách rời.

![R-tree tổ chức các hộp bao có thể chồng lấn và truy vấn có thể đi nhiều nhánh](img/lec-14/rtree.svg)

Một đa giác được lưu đúng một nút; MBR của nút phải chứa nó. Vì các MBR chồng lấn, một vùng hỏi có thể giao nhiều MBR và truy vấn phải đi nhiều nhánh — không giống đường dò một nhánh của B+-Tree.

**Giả mã — gom ứng viên và tinh lọc:**

```text
gom(U,Q,A):
  nếu U là lá: thêm mục có MBR giao Q vào A
  nếu không, với mỗi con C:
    nếu MBR(C) giao Q: gom(C,Q,A)

tinh_lọc(A,Q): trả các vật thể thật sự giao Q
```

**Đặc tả.** Đầu vào là nút gốc $U$, vùng hỏi $Q$ và tập ứng viên rỗng $A$. gom đưa mọi mục có MBR giao $Q$ vào $A$; tinh_lọc kiểm hình thật, không kiểm lại MBR.

**Tính đúng.** Bước gom không bỏ nghiệm: nếu vật thể $F$ giao $Q$ thì MBR của nó giao $Q$, và vì MBR của con là tổ tiên bao nó, mọi MBR tổ tiên của nó dọc đường cũng giao $Q$. Do đó đường đệ quy xuống lá của $F$ không bị bất kỳ điều kiện nào cắt, và $F$ được đưa vào $A$. Bước tinh lọc trả đúng các vật thể trong $A$ thật sự giao $Q$. Vì thế đầu ra là đúng tập vật thể giao $Q$.

**Dừng.** Cây hữu hạn và mỗi lời gọi đi xuống một con nên gom dừng; tinh_lọc duyệt $A$ hữu hạn.

**Chi phí và giới hạn.** Đo ba thành phần riêng: CPU thực hiện các phép kiểm giao MBR–vùng, số nút hoặc trang đã đọc, và số ứng viên phải kiểm hình thật. Không có một cận I/O tổng quát nào được nêu ngoài nguồn. Hộp tách tốt dẫn tới ít nút và ít ứng viên; hộp chồng lấn dẫn tới nhiều nút và nhiều ứng viên phải tinh lọc. Cập nhật có thể mở rộng MBR, làm tăng chồng lấn và đôi khi gây tách nút; bài không dạy thuật toán chèn hoặc tách R-tree.

::: exercise
Một vùng hỏi $Q$ giao MBR của hai cây con, nhưng chỉ một vật thể trong đó thật sự giao $Q$. Hãy cho biết hai nhánh có được thăm không, và bước nào loại vật thể còn lại.
:::

::: hint
Áp dụng mệnh đề không bỏ nghiệm cho bước lọc và xác định bước phải kiểm hình thật.
:::

::: solution
Cả hai nhánh đều được thăm vì MBR của chúng giao $Q$; không được cắt nhánh dựa trên hình thật chưa biết. Sau khi gom, tinh_lọc kiểm hình thật từng vật thể trong $A$ và loại vật thể không thật sự giao $Q$.
:::

## 6. kd-tree và tìm kiếm 1-NN chính xác

**Vai trò và nhu cầu.** Trên một tập huấn luyện $n$ điểm trong $\mathbb R^p$, tìm hàng xóm gần nhất của điểm hỏi $q$ bằng quét tuyến tính cần đo $n$ khoảng cách cho mỗi truy vấn. Với tập huấn luyện lớn và nhiều truy vấn, chi phí quá cao. **kd-tree** chia không gian thành các miền hình hộp thẳng trục để tránh đo những điểm chắc chắn không gần $q$.

**Cấu trúc.** Mỗi nút trong lưu lại:

- **chiều chia** (tọa độ nào bị cắt),
- **ngưỡng** (giá trị cắt tại chiều đó),
- **hộp miền** (bounding box) của hai cây con.

Mọi điểm dữ liệu nằm ở lá; nút trong không lưu điểm, chỉ định tuyến bằng phép chia và hộp.

![kd-tree có nút trong lưu phép chia và hộp miền; mọi điểm dữ liệu nằm ở các lá](img/lec-14/kd-partition-tree.svg)

Đường từ gốc tới một lá là giao của các nửa không gian tạo bởi các đường cắt, tức một hộp thẳng trục. Mỗi đường cắt tạo hai miền và một nút trong nhị phân. Khi dựng, để phá hòa và bảo đảm cắt rõ ràng, sắp các điểm theo (tọa độ ở chiều chia, mã điểm) rồi tách theo hạng; hai tập con không rỗng và nhỏ hơn tập cha.

Ví dụ số và giả mã dưới đây do bài giảng triển khai từ cơ chế kd-tree trong Cornell CS5780, không phải dữ kiện nguyên văn của nguồn.

**Ví dụ chạy tay — 1-NN.** Cho $q=(3,2)$. Gọi thăm nhánh trái trước, gặp điểm $p=(2,2)$. Khoảng cách Euclid

$$\tau=\delta(q,p)=\sqrt{(3-2)^2+(2-2)^2}=1.$$

Miền $x\ge4$ (một nửa không gian bên kia đường cắt) cách $q$ đúng $1$: điểm gần nhất trong miền không thể gần hơn $\tau=1$, nhưng có thể **bằng** $\tau$. Vì phải trả mọi nghiệm đồng hạng, miền này được thăm và gặp điểm $s=(4,2)$ với $\delta(q,s)=1=\tau$, được thêm vào tập: $best=\{p,s\}$, $\tau=1$. Miền $x\ge5$ cách $q$ là $2>\tau$ nên được cắt: bất kỳ điểm nào trong đó cũng cách $q$ ít nhất 2, không tốt bằng $p$ hay $s$.

![Vết số kd-tree với q bằng 3 phẩy 2, hai nghiệm đồng hạng và một nhánh bị cắt](img/lec-14/kd-prune-trace.svg)

Trực giác dùng trong cắt nhánh: **điểm gần nhất trong một miền không thể gần $q$ hơn khoảng cách từ $q$ tới miền đó**. Nếu khoảng cách tới miền lớn hơn $\tau$, không điểm nào trong miền đáng đo.

**Hình thức hóa cận dưới.** Với $U$ là nút trong hoặc hộp miền của một cây con, một cận dưới hợp lệ phải thỏa

$$\operatorname{LB}(q,U)\le\delta(q,x)\quad\forall x\text{ ở các lá dưới }U.$$

Nói cách khác, $\operatorname{LB}(q,U)$ không vượt khoảng cách thật từ $q$ tới bất kỳ điểm nào dưới $U$. Với kd-tree, có thể chọn $\operatorname{LB}(q,U)$ là khoảng cách từ $q$ tới hộp miền của $U$; cũng có thể chọn cận tới nửa không gian đơn giản hơn. Cận chặt hơn cắt được nhiều nhánh hơn.

Vì mọi điểm nằm ở lá, lượng từ "với mọi $x$ ở các lá dưới $U$" bao phủ đúng các ứng viên của cây con.

**Giả mã — tìm kiếm 1-NN chính xác:**

```text
nearest(root,q): return search(root,q,∅,∞)

search(U,q,best,τ):
  nếu U là lá, với mỗi x trong U:
    d ← δ(q,x)
    nếu d < τ: best ← {x}; τ ← d
    ngược lại nếu d = τ: best ← best ∪ {x}
  nếu U là nút trong (chỉ lưu phép chia/hộp):
    near, far ← hai con theo thứ tự cố định; near chứa q
    (best,τ) ← search(near,q,best,τ)
    nếu LB(q,far) ≤ τ:       # chỉ cắt khi LB > τ
      (best,τ) ← search(far,q,best,τ)
  trả (best,τ)
```

**Điều kiện trước.** Cây hữu hạn, mọi điểm ở lá, $\delta$ và $\operatorname{LB}$ hợp lệ. **Điều kiện sau.** Kết quả chứa mọi điểm của cây con $U$ có khoảng cách tới $q$ bằng giá trị nhỏ nhất. **Dừng.** Mỗi lời gọi đi xuống một cây con nhỏ hơn, cây hữu hạn nên đệ quy kết thúc.

Nếu $q$ nằm đúng trên biên chia, một quy ước cố định chọn một con là `near`; con kia vẫn được xét vì điều kiện `LB(q,far) ≤ τ` không loại nó khi cận bằng.

**Tính đúng (quy nạp theo cây).** Ở lá, thuật toán đo hết mọi điểm nên bất biến đúng. Ở nút trong, con `near` được thăm trọn vẹn nên theo giả thiết quy nạp giữ đúng mọi nghiệm trong cây con đó. Con `far` bị bỏ chỉ khi $\operatorname{LB}(q,far)>\tau$; nhưng khi đó mọi $x$ dưới `far` thỏa $\delta(q,x)\ge\operatorname{LB}(q,far)>\tau$, nên không điểm nào trong `far` tốt bằng hoặc bằng $\tau$. Nếu `far` được thăm, giả thiết quy nạp áp dụng trọn vẹn. Kết hợp hai nhánh, kết quả tại gốc chứa đúng mọi điểm gần $q$ nhất, kể cả mọi nghiệm đồng hạng.

**Chi phí.** Trường hợp tốt, cận dưới loại nhiều nhánh và ít điểm bị đo. Trường hợp xấu — cận không loại nhánh nào — thuật toán đo tới mọi điểm: $O(n)$ phép đo khoảng cách. Với điểm $p$ chiều, một phép đo Euclid tốn $O(p)$ phép toán số học, nên trường hợp xấu là $O(pn)$. Hiệu quả thực hành thường tốt hơn, nhưng **không** có bảo đảm $O(\log n)$; đó là chỗ lời nguyền số chiều và giới hạn của mặt cắt thẳng trục.

::: exercise
Một nhánh xa có cận dưới đúng bằng $\tau$. Với đặc tả trả mọi hàng xóm gần nhất, nhánh này có được cắt không?
:::

::: hint
So dấu nghiêm ngặt: phép cắt dùng $>$ chứ không dùng $\ge$.
:::

::: solution
Không được cắt. Nhánh có chứa điểm ở đúng khoảng $\tau$ thì giữ nó là cần thiết vì ta trả mọi nghiệm đồng hạng. Điều kiện cắt chỉ kích hoạt khi $\operatorname{LB}>\tau$. Nếu đặc tả chỉ cần một nghiệm bất kỳ, có thể dùng quy ước phá hòa và cắt bằng; bài này trả mọi nghiệm nên dùng dấu nghiêm ngặt.
:::

## 7. Ball tree: cận metric, truy vấn và vết chạy

**Vai trò.** kd-tree dùng hộp thẳng trục; cận dưới tới hộp tính theo tọa độ. **Ball tree** thay hộp bằng **ball** $B(c,r)$: tập điểm cách tâm $c$ không quá bán kính $r$. Thuật toán truy vấn chỉ cần một **metric** $\delta$ (hàm khoảng cách thỏa bất đẳng thức tam giác), không cần tọa độ hay phép chiếu. Bài này tách hai mức giả thiết:

- **Truy vấn** (phần hiện tại) chỉ cần metric và mỗi ball chứa đúng các điểm của cây con theo cùng metric.
- **Dựng** (Phần 8) chuyên biệt hóa cho $\mathcal X\subseteq\mathbb R^p$, chuẩn Euclid và giới hạn lá $\ell\ge1$.

**Trực giác cận dưới.** Mọi điểm trong ball $B(c,r)$ đều cách $q$ ít nhất $\delta(q,c)-r$. Nếu $q$ nằm ngoài ball, đây là khoảng cách từ $q$ tới biên gần nhất của ball; nếu $q$ nằm trong ball, cận dưới hợp lệ là 0.

![Ball tree dùng cận dưới khoảng cách từ truy vấn đến tâm trừ bán kính](img/lec-14/ball-bound-tree.svg)

**Hình thức hóa và chứng minh.** Với mọi $x\in B(c,r)$:

$$\delta(q,c)\le\delta(q,x)+\delta(x,c)\le\delta(q,x)+r.$$

Bất đẳng thức thứ nhất là bất đẳng thức tam giác cho metric; thứ hai vì $x\in B(c,r)$ kéo theo $\delta(x,c)\le r$. Suy ra

$$\delta(q,x)\ge\delta(q,c)-r.$$

Lấy cực đại với 0 để tránh cận âm khi $q\in B$:

$$\operatorname{LB}(q,B)=\max(0,\delta(q,c)-r).$$

Lập luận chỉ dùng tính chất metric, không dùng tọa độ Euclid.

Ví dụ số và giả mã truy vấn dưới đây do bài giảng triển khai từ cơ chế ball tree trong Cornell CS5780.

**Ví dụ chạy tay truy vấn.** Cho $q=(0,0)$ và $\tau=2{,}5$. Ba ball với cặp $(\delta(q,c),r)$:

| Ball | $\delta(q,c)$ | $r$ | $\operatorname{LB}$ | Với $\tau=2{,}5$ |
|---|---|---|---|---|
| $B_1$ | 3 | 1 | 2 | thăm |
| $B_2$ | 5 | 2 | 3 | cắt |
| $B_3$ | 4 | $1{,}5$ | $2{,}5$ | thăm |

$B_1$ có cận 2 ≤ 2,5 nên được thăm. $B_2$ có cận 3 > 2,5 nên bị cắt. $B_3$ có cận 2,5 = $\tau$ nên **vẫn được thăm** để giữ nghiệm đồng hạng; một điểm trong $B_3$ cách $q$ đúng 2,5 sẽ được thêm vào $best$.

**Giả mã — truy vấn ball tree (chỉ cần metric):**

```text
search(U,q,best,τ):
  nếu U là lá, với mỗi x trong U:
    d ← δ(q,x)
    nếu d < τ: best ← {x}; τ ← d
    ngược lại nếu d = τ: best ← best ∪ {x}
  nếu không:
    L,R ← hai con theo LB tăng dần
    nếu LB(q,L) ≤ τ:
      (best,τ) ← search(L,q,best,τ)
    nếu LB(q,R) ≤ τ:
      (best,τ) ← search(R,q,best,τ)
  trả (best,τ)
```

**Đặc tả.** Cùng trạng thái $best,\tau$ và quy tắc đồng hạng như kd-tree ở Phần 6. Khởi tạo $best=\varnothing$, $\tau=\infty$. Thăm con có cận nhỏ trước để giảm $\tau$ sớm; sau khi thăm con đầu, dùng $\tau$ mới để xét con sau. Nút rỗng trả trạng thái không đổi.

**Tính đúng.** Tính đúng chỉ cần $\delta$ là metric và mỗi ball chứa mọi điểm dưới nút theo chính $\delta$. Lá đo hết mọi điểm. Ở nút trong, con bị cắt chỉ khi $\operatorname{LB}>\tau$, và khi đó theo bất đẳng thức tam giác mọi $x$ trong ball có $\delta(q,x)>\tau$, không tốt bằng hoặc bằng nghiệm hiện có. Các con được thăm giữ đúng nghiệm theo quy nạp. Do trả mọi nghiệm đồng hạng nên dấu so là `≤` chứ không phải `<`.

**Dừng và chi phí.** Cây hữu hạn, mỗi lời gọi xuống cây con nhỏ hơn nên dừng. Trường hợp xấu đo mọi điểm: $O(n)$ phép đo; với metric Euclid trên $\mathbb R^p$, $O(pn)$ phép toán số học. Với metric tổng quát, chi phí mỗi lần đo phụ thuộc hàm $\delta$ và được đo theo phép đo, không phải theo số chiều.

::: exercise
Dùng công thức $\operatorname{LB}(q,B)=\max(0,\delta(q,c)-r)$ giải lại ba ball của ví dụ với $\tau=3$. Ball nào bị cắt thêm so với trường hợp $\tau=2{,}5$?
:::

::: hint
So từng cận với 3.
:::

::: solution
Các cận vẫn là 2, 3, 2,5. Ball $B_1$ (2 ≤ 3) thăm, $B_2$ (3 ≤ 3) thăm vì dấu $\le$ giữ nghiệm hòa, $B_3$ (2,5 ≤ 3) thăm. Không ball nào bị cắt thêm so với $\tau=2{,}5$; thực tế $\tau=3$ cho thêm điểm được thăm.
:::

## 8. Dựng ball tree Euclid và cận có điều kiện

**Vai trò.** Phần này chuyên biệt hóa phép dựng cho tập hữu hạn $\mathcal X\subseteq\mathbb R^p$, với **khoảng cách chuẩn Euclid** (chuẩn 2) và sức chứa lá $\ell\ge1$. Tâm và bán kính của ball dựa trên phép trung bình và phép chiếu Euclid — hai thao tác không có nghĩa trong một metric trừu tượng. Vì vậy phép dựng **không** là một bước của thủ tục truy vấn metric tổng quát ở Phần 7.

**Ví dụ chạy tay.** Cho

$$\mathcal X=\{a=(0,0),\ b=(1,0),\ c=(3,0),\ d=(4,0)\}.$$

Các bước dựng một nút:

1. **Tâm trung bình.** $\bar{\mathcal X}=\frac{a+b+c+d}{4}=(2,0)$.
2. **Bán kính cực đại.** Khoảng cách lớn nhất từ tâm tới điểm là $\delta((2,0),(4,0))=2$, nên $r_S=2$.
3. **Chọn hai điểm xa.** Chọn $x_0=a$; điểm xa $x_0$ nhất là $x_1=d$ (khoảng cách 4); điểm xa $x_1$ nhất trong $\mathcal X$ là $x_2=a$.
4. **Phép chiếu.** Với $z(x)=(x_1-x_2)^T x$. Có $x_1-x_2=(4,0)-(0,0)=(4,0)$, nên $z(a)=0$, $z(b)=4$, $z(c)=12$, $z(d)=16$.
5. **Chia theo hạng.** Sắp theo ($z(x)$, mã điểm) cho thứ tự $a,b,c,d$; cắt sau hạng $\lfloor 4/2\rfloor=2$ thành $\mathcal X_L=\{a,b\}$ và $\mathcal X_R=\{c,d\}$.
6. **Ball của mọi nút.** Mọi nút, kể cả lá, tạo $(c,r)$.

Bảng kết quả:

| Nút | Tập điểm | Tâm | Bán kính |
|---|---|---|---|
| Cha | $\{a,b,c,d\}$ | $(2,0)$ | 2 |
| Lá trái | $\{a,b\}$ | $(0{,}5,0)$ | 0,5 |
| Lá phải | $\{c,d\}$ | $(3{,}5,0)$ | 0,5 |

Mỗi ball chứa đúng mọi điểm dưới nút theo cùng khoảng cách Euclid. Ball cha tâm $(2,0)$, bán kính 2 chứa cả bốn điểm; lá trái tâm $(0{,}5,0)$, bán kính 0,5 chứa đúng $\{a,b\}$; lá phải tương tự.

**Giả mã — dựng (Euclid):**

```text
build(𝒳), với ∅ ≠ 𝒳 ⊆ ℝᵖ và ℓ ≥ 1:
  c ← mean(𝒳); r ← maxₓ∈𝒳 ‖x-c‖₂
  nếu |𝒳| ≤ ℓ: trả lá(c,r,𝒳)
  chọn x₀ tùy ý trong 𝒳
  chọn x₁, x₂ theo hai bước điểm xa
  z(x) ← (x₁-x₂)ᵀx                  # phép chiếu Euclid
  sắp theo (z(x), mã-điểm)
  chia theo hạng trung vị thành 𝒳_L, 𝒳_R
  trả nút(c,r,build(𝒳_L),build(𝒳_R))
```

**Điều kiện trước.** $\mathcal X$ hữu hạn và khác rỗng; $\ell\ge1$; khoảng cách trong bài là chuẩn 2. **Điều kiện sau.** Mọi nút — kể cả lá — có ball $(c,r)$, và mọi điểm dưới nút nằm trong ball.

**Tiến triển về cơ sở.** Nếu $|\mathcal X|\le\ell$ trả lá. Nếu $|\mathcal X|>\ell$ thì vì $\ell\ge1$, có $|\mathcal X|\ge2$, nên phép chiếu cùng thứ tự (chiếu, mã điểm) tạo một thứ tự toàn phần. Cắt sau hạng $\lfloor|\mathcal X|/2\rfloor$ tạo hai nửa không rỗng, mỗi nửa nhỏ hơn $|\mathcal X|$. Vậy đệ quy tiến về cơ sở và dừng.

**Cận chi phí có điều kiện.** Cận sau **không** được gán cho Cornell; đây là suy ra của deck dưới ba giả thiết:

- cây cân bằng (hai cây con cùng kích thước, $O(\log n)$ mức);
- mỗi nút sắp lại các phép chiếu của $\mathcal X_L,\mathcal X_R$;
- mỗi phép đo/chiếu/tính tâm/bán kính xử lý $p$ tọa độ.

Ở mỗi mức, sắp xếp mọi điểm tốn $O(n\log n)$ và các phép đo cùng chiếu tốn $O(pn)$. Nhân với $O(\log n)$ mức cho

$$O(n\log^2 n+pn\log n).$$

Nếu các giả thiết này không giữ — ví dụ cây mất cân bằng hoặc phép chiếu xử lý nhiều hơn $p$ tọa độ — cận trên không áp dụng. Phép dựng cũng mang giả thiết Euclid: tâm trung bình và phép chiếu $(x_1-x_2)^T x$ không được định nghĩa cho một metric trừu tượng.

::: exercise
Với $\mathcal X=\{a=(0,0),b=(2,0),c=(6,0),d=(8,0)\}$ và $\ell=2$, hãy tìm tâm, bán kính của ball cha và của hai lá, rồi kiểm mọi điểm nằm trong ball tương ứng.
:::

::: hint
Làm theo vết: tâm trung bình, bán kính cực đại, hai điểm xa, phép chiếu, chia theo hạng.
:::

::: solution
$\bar{\mathcal X}=(4,0)$, bán kính cực đại $\delta((4,0),(8,0))=4$. Hai điểm xa: $x_0=a$, $x_1=d$, $x_2=a$, $z=(8,0)^T x$ cho 0,16,48,64, chia $\mathcal X_L=\{a,b\}$, $\mathcal X_R=\{c,d\}$. Lá trái tâm $(1,0)$, bán kính 1; lá phải tâm $(7,0)$, bán kính 1. Ball cha tâm $(4,0)$, bán kính 4 chứa cả bốn điểm; mỗi lá chứa đúng hai điểm của mình.
:::

## 9. Z-order, đoạn Morton, B+-Tree và tinh lọc

**Vai trò.** Bài 13 dùng B+-Tree cho khóa có thứ tự. Điểm $(x,y)$ không có một thứ tự tuyến tính duy nhất nào bảo toàn mọi lân cận. **Z-order** (đường cong Morton) gán cho mỗi ô lưới một mã số, đưa không gian về một khóa tuyến tính để dùng cây có thứ tự.

**Đặc tả.** Trên lưới $n_G\times n_G$, quy ước tọa độ **0-based**: với ô $(x,y)$ nguyên 1-based, đặt

$$u=x-1,\qquad v=y-1.$$

Mã Morton **1-based** được định nghĩa

$$z=1+\sum_{j\ge0}(2u_j+v_j)4^{j},$$

trong đó $u_j,v_j$ lần lượt là bit thứ $j$ của $u$ và $v$. Hệ số $(2u_j+v_j)$ nén hai bit $u_jv_j$ thành một chữ số hệ 4, với bit của $u$ đứng trước bit của $v$ trong mỗi cặp.

**Ví dụ lưới Morton 4×4.** Theo quy ước trên, từ hàng trên xuống dưới:

$$z=\begin{array}{cccc}6&8&14&16\\5&7&13&15\\2&4&10&12\\1&3&9&11\end{array}$$

Kiểm một vài ô: $(x,y)=(1,1)$ ứng với $u=0,v=0$ cho $z=1$. $(x,y)=(2,3)$: $u=1,v=2=(10)_2$, $v_0=0,v_1=1$; $z=1+(2\cdot1+0)+1\cdot4=1+2+4=7$, đúng ô 7 ở hàng hai cột hai. $(x,y)=(3,2)$: $u=2=(10)_2, v=1=(01)_2$, $u_0=0,u_1=1$; $z=1+(0+1)+2\cdot4=1+1+8=10$, đúng ô 10. Chạy đủ 16 ô cho kết quả khớp ma trận trên. Hình nguồn Auburn trang 13 đổi chỗ mã 6 và 7; bài giữ công thức Morton và sửa hình.

![Lưới bốn nhân bốn đánh số Morton từ 1 đến 16 với gốc ở góc dưới trái](img/lec-14/zorder-grid.svg)

**Vùng hỏi thành đoạn mã.** Xét vùng $x\in\{2,3\}, y\in\{2,3\}$ — bốn ô ở giữa. Các ô có mã:

$$\{4,7,10,13\}.$$

Vì thứ tự lân cận không được bảo toàn hoàn toàn dưới mã Morton, vùng trên không tạo một khoảng liên tục trong thứ tự mã. Cần phủ vùng bằng một hoặc nhiều **đoạn** mã để B+-Tree quét.

**Các đoạn mã và tinh lọc.** Có hai phương án hợp lệ:

- **Bốn đoạn đơn chính xác**: $[4],[7],[10],[13]$. Không có dương tính giả, nhưng cần bốn lần tìm đầu đoạn trong B+-Tree.
- **Một đoạn gộp**: $[4,13]$. Chỉ cần một lần tìm, nhưng quét thêm các mã $5,6,8,9,11,12$ không thuộc vùng.

Mã 5 là **dương tính giả**: nằm trong khoảng $[4,13]$ nhưng ứng với $(x,y)=(1,3)$, không thuộc vùng hỏi. Bước tinh lọc kiểm tọa độ thật của từng ô ứng viên để loại mã ngoài vùng.

![Các ô không gian đổi thành nhiều đoạn khóa Z-order rồi được tra bằng B+-Tree và tinh lọc](img/lec-14/zorder-btree.svg)

**Yêu cầu đúng của phương án.** Mọi phương án đoạn phải **phủ mọi mã của vùng** $\{4,7,10,13\}$; nếu thiếu một mã thì bỏ sót các ô thuộc vùng phải trả. Do đó cả hai phương án trên đều đúng — một phương án chính xác với chi phí định vị cao, một phương án gộp với dương tính giả phải lọc.

**Truy vấn qua B+-Tree và đơn vị chi phí.** Với mỗi đoạn $[a,b]$, dùng B+-Tree của Bài 13 để tìm lá đầu không nhỏ hơn $a$, rồi quét chuỗi lá tới $b$. Phương án chính xác: bốn lần tìm, ít ứng viên thừa. Phương án gộp: một lần tìm $[4,13]$, dương tính giả được đưa vào với chi phí đọc dữ liệu để kiểm hình học. Chi phí đầy đủ gồm số lần tìm đầu đoạn, số mục ứng viên quét và số trang dữ liệu. Đơn vị này không trộn với số phép đo RAM của cây miền ở Phần 6.

::: exercise
Với vùng $x\in\{1,2\}, y\in\{1,2\}$ (góc dưới trái), hãy liệt kê mọi mã Morton của bốn ô, chọn đoạn gộp nhỏ nhất phủ chúng và xác định đoạn đó có dương tính giả hay không.
:::

::: hint
Dò lưới 4×4: các ô $(1,1),(1,2),(2,1),(2,2)$ ứng với mã nào? Tìm khoảng bao trọn và các mã dư của khoảng đó.
:::

::: solution
$(1,1)\to1$, $(1,2)\to2$, $(2,1)\to3$, $(2,2)\to4$. Tập mã $\{1,2,3,4\}$ tạo đúng đoạn liên tục $[1,4]$, nên đoạn gộp nhỏ nhất không có dương tính giả. Trong ví dụ vùng giữa, đoạn $[4,13]$ quét thêm sáu mã ngoài vùng.
:::

## 10. Chọn chỉ mục theo đầu ra, giả thiết và đơn vị chi phí

**Vai trò.** Các cụm trước xây từng cấu trúc riêng. Cụm này gộp lại để chọn cấu trúc theo loại truy vấn, điều kiện đúng và đơn vị chi phí. Hai tình huống mở bài — kho web và ảnh vệ tinh với trạm xăng — được thu hồi ở đây.

**Bảng so sánh.**

| Cấu trúc | Truy vấn | Điều kiện đúng | Đơn vị chi phí |
|---|---|---|---|
| Chỉ mục đảo | Boolean | danh sách đầy đủ, tăng nghiêm ngặt | mục/trang danh sách |
| R-tree | vùng | MBR chứa hình thật (lọc không bỏ nghiệm) | trang, ứng viên, CPU |
| kd-tree / ball tree | 1-NN | LB hợp lệ và metric | phép đo; phép toán số học |
| Z-order | vùng | đoạn phủ đủ mã + tinh lọc | lần tìm, trang, ứng viên |

**Đơn vị chi phí.** kd-tree và ball tree ở đây được phân tích theo mô hình **RAM**: số phép đo khoảng cách và phép toán số học trên $p$ tọa độ. Chỉ mục đảo, R-tree và Z-order được đặt trên **trang** nên phải đo lần định vị, số trang đọc và số ứng viên. Hai đơn vị này không được so trực tiếp; nếu so, phải nêu mô hình chi phí.

**Quy trình chọn chỉ mục** — năm bước kiểm lại chất lượng đầu ra:

1. Chốt đầu vào, đầu ra, tập nền và mô hình chi phí.
2. Chốt biểu diễn sắp được, miền hoặc metric.
3. Chứng minh điều kiện cắt hoặc lọc không bỏ nghiệm.
4. Đo phần phải đọc; với truy hồi xếp hạng, thêm precision/recall.
5. Xét cập nhật: MBR có thể nở, tăng chồng lấn và tách.

**Trường hợp cụ thể.** Với kho web xếp hạng, tập nền $S$ quyết định NOT và $G$ quyết định precision/recall; đơn vị chi phí là mục/trang danh sách. Với vật thể hình học, MBR giao tạo ứng viên rồi kiểm hình thật; đo trang, CPU và số ứng viên. Với trạm xăng 1-NN, metric và quy tắc hòa quyết định cắt; đo phép đo. Với Z-order, mọi mã vùng phải được phủ bởi đoạn và ứng viên gộp phải được tinh lọc bằng tọa độ.

**Vị trí của chất lượng.** Kết quả của lọc–tinh lọc và của 1-NN được đánh giá bằng **tính đúng** (không bỏ nghiệm, không trả dương tính giả). Chỉ có truy hồi xếp hạng mới dùng precision/recall, và đó là chất lượng của tập trả về, không phải tính chính xác của thuật toán. Hai khái niệm này dễ bị nhầm vì cùng chữ "độ chính xác"; bài phân biệt chúng rõ.

::: exercise
Sinh viên nói "R-tree cho độ chính xác là 1 vì bước gom không bỏ nghiệm". Hãy nêu một cách hiểu đúng của câu đó nếu nó nói về tính đúng của đầu ra, và nếu nó nói về precision của truy hồi xếp hạng.
:::

::: hint
Xét R-tree tạo tập ứng viên; đầu ra chính xác không đồng nghĩa với recall hoặc precision cao.
:::

::: solution
Nếu nói về tính đúng, câu có thể giữ được: bước lọc không bỏ nghiệm và tinh lọc loại dương tính giả, nên đầu ra hình học của vùng là chính xác theo ngữ nghĩa đó. Nếu nói về precision của truy hồi xếp hạng, câu sai: precision đo tỉ lệ $R\cap G$ trong tập trả về, một thuộc tính của xếp hạng và ngưỡng, không phải tính đúng của bước hình học. Phải ghi rõ đang nói đại lượng nào.
:::

## 11. Bài 31.2 — hợp ít nhất $k$ danh sách bằng đống

**Đặc tả.** Có $n\ge1$ từ khóa, mỗi từ khóa $i$ có một danh sách docID $P_i$ tăng dần, có thể rỗng và không lặp docID. Cho $1\le k\le n$. Yêu cầu: tìm mọi tài liệu chứa **ít nhất** $k$ trong $n$ từ khóa. Đặt

$$T=\sum_{i=1}^{n}|P_i|.$$

Sản phẩm gồm giả mã, bất biến, điều kiện dừng, thời gian và bộ nhớ. Đây là bài nguồn của *Database System Concepts* 7e, Practice Exercise 31.2; lời giải đống dưới đây do bài giảng triển khai từ đề vì ấn bản 7 không công bố lời giải.

**Ý tưởng.** Cần gom các docID xuất hiện ở nhiều danh sách. Đặt một con trỏ vào đầu mỗi danh sách và duy trì chúng trong một **đống tối thiểu** (min-heap) khóa theo docID. Phần tử đống là `(docID, mã danh sách)` — nhớ mã danh sách để biết con trỏ nào phải tiến khi lấy một phần tử ra.

**Bất biến.** Trước mỗi lần lấy tối thiểu, đống chứa đúng đầu chưa xử lý của mỗi danh sách chưa cạn; mọi docID nhỏ hơn `min(H).docID` đã được quyết định. Vì đống lấy phần tử nhỏ nhất, mọi bản sao còn lại của docID nhỏ nhất chưa xử lý đều được lấy hết trong cùng một lượt của vòng trong.

**Giả mã:**

```text
H ← dựng đống từ các (docID đầu, mã danh sách) chưa rỗng
A ← []
while H không rỗng:
  x ← docID nhỏ nhất trong H; đếm ← 0
  while H không rỗng và min(H).docID = x:
    (x,i) ← lấy-min(H); đếm ← đếm + 1
    tiến con trỏ của Pᵢ
    nếu Pᵢ chưa cạn: đưa (đầu mới của Pᵢ,i) vào H
  nếu đếm ≥ k: thêm x vào A
trả A
```

**Giải thích.** Vòng trong gom hết mọi phần tử có docID bằng $x$: mỗi danh sách tiến một đầu mới vào đống nếu còn. `đếm` đếm số danh sách chứa $x$. Sau vòng trong, nếu `đếm ≥ k`, $x$ được đưa vào kết quả. Mỗi danh sách có tối đa một phần tử mang docID $x$ vì danh sách không lặp docID, nên `đếm` đúng là số danh sách chứa $x$.

**Tính đúng.** Ta chứng minh đầu ra chứa đúng mọi docID xuất hiện trong ít nhất $k$ danh sách, mỗi docID một lần và theo thứ tự tăng. Bất biến nói đống chứa đúng đầu chưa xử lý của mọi danh sách. Theo đó docID nhỏ nhất chưa xử lý trong toàn bộ dữ liệu chính là `x = min(H)`. Vòng trong lấy hết mọi phần tử có docID $x$ và đếm đúng. Vì vậy $x$ được giữ lại đúng khi số danh sách chứa nó ≥ $k$, và mọi docID nhỏ hơn $x$ đã được quyết định trước đó. Quy nạp theo thứ tự docID cho kết quả đúng và xếp tăng; mỗi docID xuất hiện đúng một lần.

**Dừng.** Vòng ngoài: mỗi lượt tiêu thụ hết mọi danh sách đang có đầu bằng $x$ và có thể thêm đầu mới vào đống; mỗi đầu mới là một mục của một danh sách, tổng số mục là $T$ hữu hạn. Vòng trong cạn khi đống rỗng hoặc đầu nhỏ nhất lớn hơn $x$. Vòng ngoài cạn khi đống rỗng, nghĩa là mọi danh sách đã cạn. Thuật toán dừng.

**Chi phí.** Duyệt $n$ danh sách để khởi tạo — kể cả khi tất cả đều rỗng và $T=0$ — tốn $O(n)$. Mỗi mục trong tổng $T$ khi vào hoặc khi ra đống tốn $O(\log(n+1))$ vì đống chứa tối đa $n$ phần tử (mỗi danh sách một đầu). Có $T$ lần lấy và nhiều nhất $T$ lần tái chèn, nên thời gian:

$$O(n+T\log(n+1)).$$

Bộ nhớ phụ — đống cộng các con trỏ, không tính kết quả — là $O(n)$. Nếu tính cả đầu ra $A$, tổng bộ nhớ là $O(n+|A|)$.

::: exercise
Với $n=2$, cả hai danh sách đều rỗng và $k=1$. Chạy thuật toán ở trên và cho biết số lần duyệt khởi tạo vẫn diễn ra dù đống rỗng.
:::

::: hint
Bước khởi tạo vẫn không phụ thuộc vào nội dung các danh sách.
:::

::: solution
Đống rỗng từ đầu, vòng ngoài không chạy, kết quả $A=[]$ rỗng. Nhưng bước duyệt $n$ danh sách để khởi tạo đống và xác nhận rỗng vẫn chạy, tốn $O(n)$. Đây là lý do chi phí khởi tạo được ghi rõ riêng trong phân tích.
:::

## 12. Bài 25.2–25.3 — truy vấn điểm và 1-NN qua vùng tròn

Hai bài dưới đây dùng đề và lời giải chính thức của *Database System Concepts* 6e, Practice Solutions Chương 25.

### 12.1. Bài 25.2 — so khớp điểm chính xác

**Đặc tả.** Một quan hệ chứa tọa độ $(x,y)$ và tên nhà hàng. Mọi truy vấn cho một điểm và hỏi có nhà hàng đúng tại điểm đó hay không. Yêu cầu: so sánh đường truy cập bằng R-tree và B-tree, rồi chọn một. Giả thiết rõ: so sánh hai tọa độ chính xác (không kể sai số số thực hay truy vấn lân cận).

**So sánh hai đường truy cập.**

- **B-tree (hoặc B+-Tree) trên khóa ghép $(x,y)$**: tìm trực tiếp khóa theo thứ tự từ điển. Nếu điểm có mặt trong quan hệ thì khóa ghép $(x,y)$ tồn tại và được tìm thấy ngay; nếu không thì bộ tìm dừng ở vị trí chèn. Không có dương tính giả.
- **R-tree**: phải lọc MBR tạo ứng viên, rồi vẫn phải kiểm tọa độ thật của từng ứng viên để xác nhận đúng điểm. Với tải truy vấn chỉ so khớp điểm chính xác, bước tinh lọc này thêm việc không cần thiết.

**Chọn.** Lời giải nguồn chọn cây trên khóa ghép $(x,y)$ vì tải truy vấn chỉ so khớp điểm; đường truy cập của R-tree vẫn phải kiểm tọa độ ứng viên để xác nhận điểm. Cả hai cấu trúc đều trả lời được, nhưng khóa ghép tìm trực tiếp mà không cần lọc rồi tinh lọc.

**Chi tiết bước kiểm.** Với khóa ghép $(x,y)$, tìm trong cây theo thứ tự từ điển; một mục khóa khớp đúng là đáp án. Với R-tree, ứng viên là MBR chứa $(x,y)$; kiểm tọa độ thật của mỗi ứng viên, và nếu có dương tính giả thì bỏ. Trong triển khai của học phần, có thể dùng B+-Tree với khóa ghép và dữ liệu ở lá; kết luận đường truy cập không đổi.

::: exercise
Vì sao với truy vấn điểm chính xác, R-tree không phải là lựa chọn tối ưu dù nó trả lời đúng câu hỏi?
:::

::: hint
So số bước: khóa ghép dò một đường; R-tree lọc rồi còn kiểm hình thật.
:::

::: solution
R-tree trả lời đúng nhờ lọc MBR rồi tinh lọc tọa độ thật, nhưng phải thêm bước kiểm hình thật cho ứng viên và có thể duyệt nhiều MBR chồng lấn. Khóa ghép $(x,y)$ trên B-tree/B+-Tree dò theo thứ tự khóa và không cần bước tinh lọc hình học, nên phù hợp hơn với tải chỉ so khớp điểm.
:::

### 12.2. Bài 25.3 — 1-NN bằng nhiều truy vấn vùng tròn

**Đặc tả.** Một cơ sở dữ liệu hỗ trợ truy vấn **vùng tròn đóng** nhưng không hỗ trợ trực tiếp hàng xóm gần nhất. Yêu cầu: mô tả thuật toán tìm hàng xóm gần nhất của điểm hỏi $q$ bằng nhiều truy vấn vùng tròn. Sản phẩm gồm dãy vùng, điều kiện dừng, chứng minh dừng/đúng và tập kết quả. Vùng tròn đóng chứa cả điểm cách tâm đúng bằng bán kính; quy ước này cần cho việc giữ nghiệm đồng hạng.

**Các điều kiện bổ sung hoàn thiện đặc tả.** Đề không nói rõ, và bài thêm vào để chứng minh được: tập điểm hữu hạn và không rỗng; dãy bán kính $0\le r_0<r_1<\cdots$ với $r_i\to\infty$; vùng tròn đóng. Đây là bổ sung hoàn thiện đặc tả, không phải nguyên văn đề nguồn.

**Thuật toán.** Với điểm hỏi $q$, chọn dãy tăng $0\le r_0<r_1<\cdots$ và $r_i\to\infty$. Lần lượt truy vấn vùng tròn đóng tâm $q$, bán kính $r_0, r_1,\ldots$, dừng ở bán kính $r_j$ đầu tiên mà vùng trả về **một tập $A\ne\varnothing$**. Sau đó tinh lọc trong $A$ để trả mọi điểm gần $q$ nhất.

**Chứng minh dừng.** Tập điểm hữu hạn và không rỗng, mỗi điểm có khoảng cách tới $q$ hữu hạn, và $r_i\to\infty$ khiến một vùng tròn trong dãy cuối cùng chứa ít nhất một điểm. Vì vậy tồn tại một $r_j$ đầu tiên để $A\ne\varnothing$; dãy không bị chặn bảo đảm $j$ hữu hạn. Thuật toán dừng.

**Chứng minh đúng.** Gọi $r_j$ là bán kính dừng và $A$ là tập điểm trong vùng đóng đó. Với mọi $x\notin A$, khoảng cách $\delta(q,x)>r_j$, vì mọi điểm gần hơn hoặc bằng $r_j$ đều thuộc $A$. Trong $A$, gọi $x^*$ là điểm đạt giá trị cực tiểu $\delta(q,x)$; vì $A$ không rỗng và $A$ nằm trong vùng bán kính $r_j$, có $\delta(q,x^*)\le r_j$. Giả sử có $y\notin A$ thỏa $\delta(q,y)\le\delta(q,x^*)$; thì $\delta(q,y)\le r_j$, kéo theo $y\in A$, mâu thuẫn. Vậy không điểm nào ngoài $A$ gần $q$ bằng hoặc gần hơn $x^*$. Do đó mọi hàng xóm gần nhất của $q$ đều nằm trong $A$, và tinh lọc trong $A$ trả đúng chúng.

**Đồng hạng.** Vì vùng tròn đóng chứa cả điểm cách tâm đúng $r_j$, các điểm ở khoảng cách chính xác cực tiểu đều thuộc $A$. Thuật toán trả **mọi** điểm đạt cực tiểu trong $A$, giữ nguyên mọi nghiệm đồng hạng — phù hợp đặc tả 1-NN của Phần 6–7.

**Chi phí.** Truy vấn vùng được thực hiện $j+1$ lần (các vùng $r_0,\ldots,r_j$), mỗi lần phụ thuộc vào cấu trúc chỉ mục dùng cho vùng tròn. Bài giảng suy ra thêm: nếu tinh lọc bằng khoảng cách Euclid trên $p$ tọa độ thì duyệt $|A|$ điểm tốn $O(p|A|)$ phép toán số học. Không áp đặt hệ số tăng bán kính cụ thể vì nguồn không quy định; chỉ cần dãy không bị chặn.

::: exercise
Giải thích vì sao thuật toán phải dùng dãy bán kính không bị chặn và vùng tròn đóng. Sau khi gặp tập $A$ không rỗng đầu tiên, hãy nêu bước cần làm để trả mọi hàng xóm gần nhất.
:::

::: hint
Liên hệ tính dừng với $r_i\to\infty$ và liên hệ vùng đóng với các điểm nằm đúng trên biên.
:::

::: solution
Dãy không bị chặn bảo đảm cuối cùng một vùng chứa điểm vì tập dữ liệu hữu hạn, khác rỗng và mọi khoảng cách đều hữu hạn. Vùng đóng giữ cả các điểm ở đúng bán kính $r_j$, nên không làm mất nghiệm đồng hạng trên biên. Khi gặp tập $A$ không rỗng đầu tiên, tính khoảng cách từ $q$ tới mọi điểm trong $A$ và trả tất cả điểm đạt giá trị nhỏ nhất.
:::

## Tổng hợp

Bài đã đi qua bốn cấu trúc chỉ mục theo ba mô hình. **Chỉ mục đảo** đảo ánh xạ tài liệu→thuật ngữ thành thuật ngữ→danh sách docID tăng nghiêm ngặt, và trộn AND, OR, NOT bằng hai con trỏ trong thời gian tuyến tính theo độ dài danh sách. **R-tree** tổ chức MBR thành cây có chồng lấn, lọc MBR tạo ứng viên rồi tinh lọc hình thật; bước gom không bỏ nghiệm vì MBR chứa hình thật. **kd-tree và ball tree** trả 1-NN chính xác bằng cận dưới $\operatorname{LB}(q,U)$, chỉ cắt nhánh khi $\operatorname{LB}>\tau$ để giữ mọi nghiệm đồng hạng; truy vấn ball chỉ cần metric, còn phép dựng Euclid dùng trung bình và phép chiếu với cận có điều kiện. **Z-order** gán mã tuyến tính cho ô lưới bằng công thức Morton, rồi dùng B+-Tree quét đoạn; đoạn gộp có dương tính giả phải tinh lọc tọa độ.

Để chọn cấu trúc, trước hết xác định đầu ra là Boolean, vùng hay 1-NN; tiếp đó xác định cấu trúc trả đáp án hay chỉ tạo ứng viên; cuối cùng chọn đúng đơn vị chi phí giữa mục hoặc trang, phép đo RAM và phép toán số học. Ba ranh giới cần giữ là văn bản với không gian, metric với phép dựng Euclid, và precision của truy hồi xếp hạng với tính đúng của 1-NN.
