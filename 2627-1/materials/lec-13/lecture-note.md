# Bài 13 — Chỉ mục truyền thống và băm tĩnh

> Bộ bài giảng: [Deck Bài 13](lecture-13-chi-muc-truyen-thong-va-bam-tinh.html) — Giải thuật nền tảng của Khoa học dữ liệu, Học kỳ 1, năm học 2026–2027.

## Mở bài

Một quan hệ lớn không vừa bộ nhớ chính phải phục vụ ba dạng truy vấn: truy vấn điểm (tìm bản ghi theo đúng một giá trị khóa), truy vấn khoảng (tìm mọi bản ghi có khóa trong một miền) và bộ lọc phân tích gồm nhiều điều kiện. Quét tuần tự toàn bộ $N$ khối luôn trả lời được nhưng quá đắt. Chỉ mục giảm số khối phải đọc, nhưng lại phải trả giá bằng dung lượng lưu trữ phụ trội và chi phí cập nhật.

Bài 13 đi qua bốn nhánh cấu trúc có phạm vi khác nhau:

1. **B+-Tree**: cấu trúc có thứ tự cho cả truy vấn điểm và khoảng, nền tảng của phần lớn chỉ mục quan hệ.
2. **B-Tree**: được trình bày ngắn chỉ để đối chiếu với B+-Tree, không dạy thuật toán cập nhật riêng.
3. **Băm tĩnh**: định tuyến trực tiếp bằng hàm băm, hiệu quả chỉ cho điều kiện bằng.
4. **Bitmap Index**: mã hóa từng vị trí bản ghi thành một bit, hiệu quả cho các bộ lọc trên tập bản ghi.

Mỗi dạng truy vấn nghiêng về một cấu trúc; không có cấu trúc nào tốt nhất trong mọi tình huống. Nhiệm vụ của bài là nắm rõ cấu trúc, chạy đúng thuật toán cập nhật và phân tích được đánh đổi giữa I/O, cập nhật và dung lượng.

## 1. Bài toán chỉ mục và chi phí truy vấn – cập nhật

**Đặc tả.** Một chỉ mục nhận một **khóa tìm kiếm** (search key) — có thể là một cột hoặc tổ hợp cột — và trả về con trỏ đến bản ghi. Khóa tìm kiếm khác bản thân dữ liệu: nó là giá trị dùng để định tuyến, còn con trỏ trỏ đến nơi chứa bản ghi thật trên đĩa.

Một quan hệ có $N$ khối. Không có chỉ mục, truy vấn chọn phải quét cả tệp, tức đọc $N$ khối. Chỉ mục biến chi phí thành một hàm nhỏ hơn nhiều, nhưng mỗi chỉ mục bổ sung phải được duy trì: luôn tốn thời gian CPU và I/O thêm khi chèn hoặc xóa, có thể phải được cập nhật khi đổi bản ghi, và chiếm không gian phụ trội riêng.

Có bốn thước đo để đánh giá một chỉ mục:

| Thước đo | Nội dung |
|---|---|
| Thời gian truy cập | số khối phải đọc để trả lời một kiểu truy vấn |
| Thời gian chèn | chi phí thêm một bản ghi hoặc một giá trị khóa vào chỉ mục |
| Thời gian xóa | chi phí loại một bản ghi hoặc một giá trị khóa khỏi chỉ mục |
| Không gian phụ trội | lượng lưu trữ thêm, ngoài dữ liệu gốc |

![Đánh đổi giữa chi phí truy vấn và chi phí duy trì khi thêm chỉ mục](img/lec-13/index-cost.svg)

Chọn cấu trúc phải dựa vào **loại truy vấn chiếm ưu thế**. Truy vấn điểm thích cây có thứ tự hoặc băm; truy vấn khoảng thích cây có thứ tự vì băm không duy trì trật tự khóa; nhiều bộ lọc trên thuộc tính ít giá trị thích bitmap. Tạo chỉ mục trên mọi thuộc tính và mọi tổ hợp thuộc tính thường không đáng, vì lợi ích truy vấn giảm dần trong khi chi phí duy trì và lưu trữ tăng tuyến tính với số chỉ mục.

::: exercise
Một hệ thống chủ yếu truy vấn khoảng theo một thuộc tính có nhiều giá trị phân biệt. Trong bốn cấu trúc của bài, chọn cấu trúc phù hợp nhất và nêu một lý do loại băm tĩnh.
:::

::: hint
Cấu trúc cần duy trì thứ tự khóa và cho phép quét liên tiếp sau khi tìm biên dưới.
:::

::: solution
Chọn B+-Tree: phép dò tìm lá đầu rồi đi theo chuỗi lá. Băm tĩnh không bảo toàn thứ tự nên truy vấn khoảng phải xét nhiều hoặc toàn bộ ngăn.
:::

## 2. Cấu trúc B+-Tree và các bất biến

**Đặc tả.** B+-Tree là cây cân bằng có hai loại nút:

- **Nút trong** chỉ chứa các giá trị khóa dùng để định tuyến; mỗi mục (con trỏ, khóa) dẫn xuống một cây con.
- **Nút lá** chứa các mục khóa kèm con trỏ đến bản ghi; các lá được nối thành một **chuỗi lá** theo thứ tự khóa để quét khoảng.

![Phân bố các nút trong, nút lá và chuỗi lá trong B+-Tree](img/lec-13/bplus-layout.svg)

Ký hiệu:

- $m$ là số con tối đa của nút trong; nút trong có tối đa $m$ con, nút lá có tối đa $m-1$ khóa.
- $f=\lceil m/2\rceil$ là cận dưới số con của nút trong không phải gốc.
- $K$ là số mục khóa trong lá: với khóa duy nhất là số khóa, với khóa ghép là số cặp $(v,\mathrm{RID})$, với khóa trùng dùng danh sách RID thì là số mục khóa khác nhau.
- $d$ là số cạnh từ gốc đến lá; cây chỉ gồm một lá thì $d=0$.

Với $m=6$, nút trong có tối đa 6 con và 5 khóa, nút lá có tối đa 5 khóa.

**Các bất biến (invariant)** được giữ trong mọi thao tác:

1. **Đồng độ sâu lá**: mọi lá ở cùng một mức $d$; không có lá nằm cao hơn hay thấp hơn.
2. **Cận sức chứa nút trong**: nút trong không phải gốc có từ $\lceil m/2\rceil$ đến $m$ con.
3. **Cận sức chứa nút lá**: nút lá không phải gốc có từ $\lceil (m-1)/2\rceil$ đến $m-1$ khóa.
4. **Gốc ngoại lệ**: gốc không bị buộc vào cận dưới; gốc trong phải có ít nhất hai con, cây rỗng có gốc là một lá rỗng.

**Cận chiều sâu.** Với cây không chỉ gồm gốc và $f=\lceil m/2\rceil\ge2$, mỗi nút trong không phải gốc có ít nhất $f$ con. Vì số lá tăng ít nhất theo cấp số nhân qua các mức, còn mỗi lá chứa một số hữu hạn mục khóa, số cạnh từ gốc đến lá thỏa
$$d=O(\log_f K).$$
Ngoại lệ ở gốc chỉ thay đổi một thừa số hằng. Lập luận này giải thích vì sao tăng hệ số phân nhánh làm giảm số khối nút phải đọc trên đường dò.

Mỗi giá trị xuất hiện trong một nút trong là **khóa phân cách**: nó bằng giá trị nhỏ nhất của cây con bên phải. Khi tìm một khóa bằng một khóa phân cách, phép dò phải đi sang cây con bên phải.

**Khóa trùng.** Đặc tả cơ sở giả sử khóa phân biệt. Nếu quan hệ cho phép khóa trùng, một mục khóa có thể trỏ đến danh sách **mã định danh bản ghi** (record identifier, RID) đặt ngoài lá. Khi đó:

- Chèn một RID mà khóa đã có chỉ thêm RID vào danh sách, không tăng số khóa.
- Xóa: chỉ xóa mục khóa khi danh sách RID đã rỗng.

Thay cho danh sách, có thể dùng khóa **ghép** $(v,\mathrm{RID})$ biến khóa trùng thành khóa duy nhất; khi đó mỗi khóa ghép là một mục khóa riêng.

::: exercise
Với $m=6$, nêu cận số con của nút trong không phải gốc và cận số khóa của lá không phải gốc.
:::

::: hint
Dùng $\lceil m/2\rceil$ cho số con và $\lceil(m-1)/2\rceil$ cho số khóa lá.
:::

::: solution
Nút trong có từ $3$ đến $6$ con; lá có từ $3$ đến $5$ khóa. Gốc là ngoại lệ đối với các cận dưới này.
:::

## 3. Tìm điểm, tìm khoảng và chi phí I/O

**Đặc tả.** Đầu vào là cây B+-Tree và một khóa cần tìm. Nếu khóa duy nhất: trả về một mục khóa. Nếu khóa ghép hay khóa trùng bằng danh sách RID: trả về mọi RID thỏa mãn. Tìm khoảng $[a,b]$: trả về mọi bản ghi có khóa trong đoạn.

**Giả mã — tìm điểm (text):**

```text
find(cây, key):
    nút ← gốc
    while nút là nút trong:
        chọn con kế theo khóa phân cách
        nút ← con đó
    tìm khóa trong nút lá (hoặc mục khóa/danh sách RID)
    nếu không thấy: trả về không có
```

**Bất biến.** Tại mỗi nút trong, mọi khóa của cây con trái nhỏ hơn khóa phân cách còn của cây con phải không nhỏ hơn khóa phân cách. Cụ thể, chọn cây con trái nhất nếu khóa tìm nhỏ hơn khóa phân cách đầu; nếu không, chọn cây con ngay bên phải khóa phân cách lớn nhất không vượt khóa tìm. Quy tắc này luôn giữ khóa cần tìm, nếu tồn tại, trong cây con được chọn.

**Tính đúng.** Do khóa phân cách là khóa nhỏ nhất của cây con phải, quy ước tìm khóa bằng khóa phân cách đi sang phải đảm bảo không bỏ sót: nếu khóa cần tìm trùng khóa phân cách, mọi mục mang khóa đó nằm trong cây con phải.

**Dừng.** Mỗi bước rẽ xuống một con, số mức hữu hạn do cây cân bằng có $d$ mức, nên thuật toán dừng.

**Chi phí điểm.** Gọi $J$ là số khối RID-list ngoài lá, $D$ là số khối dữ liệu kết quả:

$$d+1+J+D.$$

Với một khóa đơn giản không có danh sách ngoài lá, đặt $J=0$.

![Đường đi từ gốc xuống lá trong truy vấn điểm](img/lec-13/bplus-search.svg)

**Tìm khoảng.** Tìm lá đầu tiên có khóa không nhỏ hơn biên dưới, rồi dùng chuỗi lá để quét tới khi vượt biên trên. Đặt $L$ là số khối lá phải đọc thêm:

$$d+1+L+J+D.$$

![Quét chuỗi lá cho truy vấn khoảng](img/lec-13/bplus-range.svg)

**Chi phí và biên.** Các mục khóa trong lá được đếm bằng $K$. Với $d$ mức, phải đọc một nút mỗi mức ($d$ lần) cộng một lá, nên phần dò là $d+1$ khối. Nếu chỉ mục không phân cụm (bản ghi thật ở bất kỳ đâu), $D$ có thể thống trị khối lượng vì nhiều bản ghi nằm rải rác trên đĩa. Nếu các RID nằm ngay trong lá thì $J=0$; nếu danh sách RID ngoài lá thì $J$ phải được tính.

::: exercise
Trong cây có gốc nối trực tiếp tới lá, một truy vấn điểm có $J=0$ và dữ liệu kết quả nằm trong một khối. Tính số khối đọc theo mô hình của bài.
:::

::: hint
Khi gốc nối trực tiếp tới lá, số cạnh từ gốc đến lá là $d=1$.
:::

::: solution
Chi phí là $d+1+J+D=1+1+0+1=3$ khối: gốc, lá và một khối dữ liệu.
:::

## 4. Chèn và tách lá, tách nút trong

**Đặc tả.** Chèn một mục khóa (hoặc cặp $(khóa, RID)$) vào đúng vị trí. Thuật toán phải giữ nguyên mọi bất biến ở Phần 2: không một nút nào vượt cận sức chứa, lá luôn đồng độ sâu.

**Giả mã — chèn (text):**

```text
insert(cây, key):
    dò từ gốc xuống lá như find
    nếu lá còn chỗ (ít hơn m−1 khóa):
        chèn đúng vị trí theo thứ tự
    ngược lại:
        tách lá thành hai: lá trái và lá phải
        sao chép khóa nhỏ nhất của lá phải lên cha (khóa phân cách)
        nếu cha tràn (có nhiều hơn m con):
            tách nút trong: đẩy khóa phân cách giữa lên cha
            nếu gốc tràn: tạo gốc mới, độ sâu d tăng 1
```

**Cơ chế tách lá.** Khi một lá chứa $m$ khóa là $m-1$ mục cộng khóa mới, chia thành hai lá có $\lceil m/2\rceil$ và $\lfloor m/2\rfloor$ khóa; với $m=6$, phép tách là 3–3. Lá trái giữ các khóa nhỏ, lá phải giữ các khóa còn lại, và **sao chép** khóa nhỏ nhất của lá phải lên cha làm khóa phân cách. Khóa này vẫn còn trong lá phải; bản ở cha chỉ dùng để định tuyến.

**Cơ chế tách nút trong.** Nếu cha (là nút trong) lại hết chỗ sau khi nhận khóa phân cách, tách nút trong thành hai và **đẩy** khóa phân cách giữa lên cha cấp trên rồi bỏ khóa đó khỏi hai nút mới. Đây khác hẳn sao chép ở lá: khóa phân cách của nút trong không còn lại trong các nút con.

![Tách nút trong và đẩy khóa phân cách giữa lên trên](img/lec-13/bplus-internal-split.svg)

Nếu gốc tràn, tách gốc thành hai nút rồi tạo một gốc mới chứa một khóa: độ sâu $d$ tăng 1, trong khi mọi lá vẫn đồng độ sâu.

**Vết chèn (bài 14.3(b), $m=6$).** Chèn tăng dần $2,3,5,7,11,17,19,23,29,31$ cho cây:

$$\text{gốc}=[7,19];\qquad \text{lá } [2,3,5],\ [7,11,17],\ [19,23,29,31].$$

Sau đó chèn $9,10$: lá giữa trở thành $[7,9,10,11,17]$, chưa tràn. Chèn $8$: lá giữa có 6 khóa nên tách 3–3 thành $[7,8,9]$ và $[10,11,17]$; sao chép khóa nhỏ nhất của lá phải là $10$ lên gốc, gốc trở thành $[7,10,19]$.

![Chèn khóa gây tách lá và sao chép khóa phân cách lên cha](img/lec-13/bplus-insert.svg)

**Lỗi in của nguồn 9→19.** Trong kết quả sau chèn 8, lá phải nhất phải bắt đầu bằng $19$: $[19,23,29,31]$. Lời giải nguồn in nhầm khóa đầu thành $9$. Đây là lỗi in: thao tác chèn 8 chỉ tách lá giữa và sao chép $10$ lên gốc, không hề động đến lá phải. Giữ $19$ là cần thiết để bảo toàn đa tập khóa của toàn cây.

**Bất biến sau tách.** Cây vẫn đồng độ sâu (chỉ gốc có thể đổi), mọi nút lá không phải gốc có từ $\lceil(6-1)/2\rceil=3$ đến 5 khóa, các nút trong không phải gốc có từ $f$ đến $m$ con. Mọi mục dữ liệu vẫn xuất hiện đúng một lần ở các lá; khóa phân cách có thể xuất hiện thêm ở nút trong để định tuyến.

**Chi phí.** Chèn dò xuống $d+1$ nút và trong trường hợp xấu nhất tràn lên mọi mức, cần ghi tối đa $O(d+1)$ khối. **Dừng:** mỗi mức chứa hữu hạn, cuối cùng hoặc đủ chỗ hoặc tạo gốc mới rồi dừng.

::: exercise
Khi tách một lá và khi tách một nút trong, khóa phân cách giữa được xử lý khác nhau thế nào?
:::

::: hint
Theo dõi xem khóa được đưa lên cha còn nằm trong nút con hay không.
:::

::: solution
Tách lá **sao chép** khóa nhỏ nhất của lá phải lên cha nên khóa vẫn ở lá. Tách nút trong **đẩy** khóa giữa lên cha và bỏ khóa đó khỏi hai nút mới.
:::

## 5. Xóa, phân phối lại, gộp và co gốc

**Đặc tả.** Xóa một mục khóa hoặc một RID. Khi xóa khóa khỏi một lá, nếu lá rơi xuống cận dưới (dưới $\lceil (m-1)/2\rceil$ khóa) phải xử lý kiểu yếu: mượn từ anh em nếu được, ngược lại gộp với anh em.

**Giả mã — xóa (text):**

```text
delete(cây, key):
    dò tới lá có thể chứa key
    nếu không thấy key: dừng, cây không đổi
    xóa mục (hoặc RID khỏi danh sách)
    nếu RID-list vẫn còn phần tử: dừng
    nếu lá vẫn đủ khóa: dừng
    # lá thiếu
    nếu anh em còn dư sức chứa khi nhận thêm 1 khóa:
        phân phối lại (mượn) một khóa từ anh em; cập nhật khóa phân cách ở cha
    ngược lại:
        gộp lá với anh em thành một lá; xóa khóa phân cách tương ứng từ cha
        nếu cha có thể thiếu: lặp lại ở mức trên
        nếu gốc chỉ còn một con: thay gốc bằng con đó (co gốc)
```

**Mượn (phân phối lại).** Nếu nút thiếu nhưng anh em lân cận có thừa khóa, chuyển một khóa từ anh em sang và cập nhật khóa phân cách tương ứng ở cha. Cây vẫn đủ mọi cận và không mất khóa.

**Gộp.** Nếu anh em không dư, gộp nút thiếu vào anh em thành một rồi xóa khóa phân cách từ cha. Việc xóa khóa này có thể làm cha thiếu, vậy thuật toán lặp lại ở mức trên.

**Co gốc.** Khi việc xử lý thiếu lan tới gốc và gốc chỉ còn một con, thay gốc bằng con duy nhất. Điều này giảm $d$ đúng một mức và bảo toàn bất biến đồng độ sâu.

**Vết xóa (trên cây 14.3(b)).** Sau chèn, cây là gốc $[7,10,19]$ với các lá $[2,3,5]$, $[7,8,9]$, $[10,11,17]$, $[19,23,29,31]$.

- Xóa $23$: lá phải $[19,29,31]$ còn 3 khóa, đủ, xong.
- Xóa $19$: lá phải $[29,31]$ chỉ còn 2 khóa, thiếu (cần ít nhất 3). Anh em trái không có khóa dư để cho mượn, nên gộp hai lá thành $[10,11,17,29,31]$; xóa khóa phân cách $19$ ở gốc, để gốc còn $[7,10]$ và ba con. Trường hợp này không co gốc.

![Gộp lá, lan lên và co gốc khi xóa](img/lec-13/bplus-delete.svg)

**Bất biến xóa.** Sau mỗi bước, mọi nút không phải gốc nằm trong cận sức chứa của nó; đồng độ sâu được duy trì hoặc bằng mượn hoặc bằng gộp, và khi cần co gốc thì $d$ giảm đúng 1. **Dừng:** mỗi mức xử lý một lần, số mức hữu hạn, và khi lên quá đỉnh thì dừng. **Chi phí:** xóa đọc $O(d+1)$ và ghi tối đa $O(d+1)$ khối.

**Biên RID-list.** Xóa một RID chỉ giảm danh sách, không xóa mục khóa; chỉ khi danh sách rỗng mới xóa cả mục khóa. Điều này tránh làm mất một khóa mà còn bản ghi thật thỏa mãn.

::: exercise
Trong vết trên, vì sao xóa $19$ cần gộp nhưng không cần co gốc?
:::

::: hint
So cận ba khóa của lá với số con còn lại của gốc sau khi gộp.
:::

::: solution
Lá $[29,31]$ có hai khóa nên thiếu; anh em $[10,11,17]$ không dư để cho mượn, vì vậy phải gộp. Sau gộp, gốc vẫn có ba con và hai khóa $[7,10]$, nên chưa thỏa điều kiện co gốc là chỉ còn một con.
:::

## 6. B-Tree: đối chiếu với B+-Tree

**Đặc tả và so sánh.** B+-Tree lưu dữ liệu và con trỏ bản ghi chỉ tại lá; các nút trong chỉ chứa khóa để định tuyến. **B-Tree** khác ở chỗ các nút trong lưu cả khóa lẫn con trỏ đến dữ liệu của chính giá trị khóa đó, không phải chỉ để định tuyến.

![B+-Tree lưu dữ liệu tại lá; B-Tree lưu dữ liệu kèm khóa ngay trong nút trong](img/lec-13/btree-compare.svg)

Hệ quả quan trọng:

- **Điểm truy cập:** trên B-Tree một bản ghi có thể được thỏa mãn ngay tại một nút trong, nên số lần đọc có thể ít hơn $d+1$. Đây là lợi ích hạn hẹp ở truy vấn điểm.
- **Quét khoảng:** trên B-Tree việc quét khoảng phải đi qua nhiều nút trong và gặp các khóa dữ liệu rải ở các mức, không gọn như B+-Tree quét dọc chuỗi lá thẳng.
- **Hệ số phân nhánh:** B+-Tree có thể nhồi nhiều khóa phân cách hơn mỗi nút trong B-Tree vì B-Tree mỗi khóa kèm con trỏ dữ liệu. Với cùng kích thước khối và tập khóa, B+-Tree vì thế có thể có độ sâu nhỏ hơn. B+-Tree còn thuận lợi cho quét khoảng nhờ chuỗi lá.

Bài không dạy thuật toán cập nhật riêng cho B-Tree; B-Tree chỉ được đối chiếu ngắn trước khi bỏ nhu cầu thứ tự để sang băm trong Phần 7.

::: exercise
Nêu một lợi thế của B-Tree cho truy vấn điểm và một lợi thế của B+-Tree cho truy vấn khoảng.
:::

::: hint
Xét nơi lưu con trỏ bản ghi và cách duyệt các khóa liên tiếp.
:::

::: solution
B-Tree có thể trả kết quả ngay tại nút trong. B+-Tree gom mọi mục dữ liệu ở lá và nối các lá theo thứ tự, nên quét khoảng trực tiếp hơn.
:::

## 7. Băm tĩnh: chuỗi tràn và chi phí

**Đặc tả.** Băm tĩnh dùng một hàm băm $h$ ánh xạ một giá trị khóa vào một trong $M$ ngăn (bucket), thường mỗi ngăn là một khối. Các phần tử khóa khác nhau có thể rơi vào cùng ngăn; toàn bộ ngăn được dò tuyến tính.

Mô hình chi phí của bài giảng giả định **một ngăn bằng một khối** và **không có bộ nhớ đệm** (dữ liệu không được giữ trong RAM giữa các truy vấn).

**Các ký hiệu:** $M$ là số ngăn, $c$ là sức chứa mỗi ngăn (số mục), $N_e$ là số mục, $t$ là số ngăn tràn phải đọc thêm khi truy vấn.

**Hệ số tải (dẫn xuất).** Gọi $\alpha$ là tỉ số giữa tổng số mục và tổng sức chứa:

$$\alpha=\frac{N_e}{Mc}.$$

$\alpha$ được suy ra trực tiếp từ định nghĩa: có $N_e$ mục, tổng sức chứa của $M$ ngăn là $Mc$. Đây là một **dẫn xuất của bài giảng trong mô hình đã nêu**, không phải công thức được trích nguyên văn tại các trang nguồn được dẫn.

![Băm tĩnh: hàm h và ngăn, các khối tràn được nối thành chuỗi](img/lec-13/static-hash.svg)

**Khi tràn và chuỗi tràn.** Tràn xảy ra khi số ngăn hoặc sức chứa không đủ, hoặc khi phân bố lệch vì nhiều khóa trùng hay hàm băm không đều. **Chuỗi tràn** (overflow chaining) nối các ngăn tràn của một ngăn thành danh sách liên kết. Khi tra cứu một giá trị, đọc ngăn nhà rồi đi theo chuỗi cho tới khi tìm thấy khóa hoặc hết chuỗi.

**Giả mã — tra cứu (text):**

```text
lookup(giá trị key):
    i ← h(key)
    đọc ngăn nhà i
    dò tuyến tính trong ngăn nhà cho khóa thật
    p ← khởi đầu của chuỗi tràn của ngăn i
    while p khác rỗng và khóa chưa thấy:
        dò tuyến tính trong ngăn tràn p
        p ← p.kế tiếp
```

**Bất biến.** Mọi mục có khóa $k$ được đặt trong ngăn nhà $h(k)$ hoặc trong một ngăn tràn của chuỗi của $h(k)$. Vì vậy mọi thao tác bắt đầu tại chính ngăn nhà và chỉ đi theo chuỗi của nó, không bỏ sót mục nào. **Tính đúng:** phải so khóa thật (không phải so với hàm băm) vì nhiều khóa khác nhau có thể cùng $h$.

**Chèn và xóa.** Chèn: tính $h$, đặt vào ngăn nhà nếu còn chỗ, ngược lại thêm một ngăn tràn vào chuỗi. Xóa: dò như trên rồi bỏ mục; xóa khóa trùng chỉ bỏ một thể hiện. **Dừng:** mỗi chuỗi hữu hạn, vậy tra cứu dừng sau một số hữu hạn ngăn (với trường hợp xấu có thể dài tuyến tính theo $N_e$).

**Chi phí (dẫn xuất).** Đọc một ngăn nhà (1 khối), $t$ ngăn tràn phải theo, và $D$ khối dữ liệu kết quả:

$$1+t+D.$$

Công thức này được suy ra từ mô hình một ngăn bằng một khối và không bộ nhớ đệm: 1 cho ngăn nhà, $t$ cho chuỗi tràn, $D$ cho dữ liệu. Với hệ số tải $\alpha$ càng cao, $t$ càng có thể lớn. **Trường hợp xấu** (hàm băm không đều hoặc quá nhiều khóa trùng) có thể đưa chi phí về tỉ lệ tuyến tính với $N_e$, không có bảo đảm hằng số.

**Vết $c=1$.** Nếu mỗi ngăn chứa đúng 1 mục ($c=1$), các khóa khoa `Physics` và `Elec. Eng.` trong ví dụ nguồn cùng rơi vào một ngăn; mục thứ hai phải nằm ở ngăn tràn, tạo $t=1$. Việc đặt $c=1$ là biến thể dẫn xuất dùng trong bài giảng để làm rõ chi phí.

**Giới hạn và hướng dẫn.** Băm tĩnh có $M$ cố định; khi dữ liệu tăng, tràn tăng và hiệu suất suy giảm. Băm chỉ hiệu quả cho **truy vấn bằng**; truy vấn khoảng bằng băm phải quét mọi ngăn nên không được dùng. Nếu khởi tạo quá nhiều ngăn, tài nguyên bị lãng phí lúc đầu. Bài này không đi vào băm động, chỉ dừng ở băm tĩnh.

::: exercise
Trong mô hình một ngăn bằng một khối, truy vấn đi qua một ngăn nhà, một ngăn tràn và đọc một khối dữ liệu. Tính chi phí và nêu vì sao đây không phải bảo đảm hằng số tổng quát.
:::

::: hint
Thay $t=1,D=1$ vào công thức dẫn xuất; sau đó xét độ dài chuỗi tràn ở trường hợp xấu.
:::

::: solution
Chi phí của vết là $1+t+D=3$ khối. Đây không phải bảo đảm tổng quát vì $t$ có thể tăng tuyến tính khi nhiều khóa dồn vào cùng một ngăn.
:::

## 8. Bitmap Index: phép Boolean và chi phí

**Đặc tả.** Một quan hệ được đánh số vị trí bản ghi là $R$ (bảng của bài 14.13 là 12 bản ghi). Bitmap Index trên một thuộc tính có **một mảnh bit** cho mỗi giá trị (hoặc dải giá trị) của thuộc tính; bit vị trí $r$ bằng 1 nếu bản ghi $r$ có giá trị đó, ngược lại 0. Các mảnh bit được đóng gói từng từ máy (word).

![Truy vấn bằng phép Boolean trên các mảnh bit của Bitmap Index](img/lec-13/bitmap-query.svg)

Phép toán gồm **AND** (giao), **OR** (hợp) và **NOT** (bù): mỗi phép áp dụng trên từng bit tương ứng của hai mảnh và cho mảnh kết quả. Ví dụ, `10010 AND 10100 = 10000`.

**Vết 14.13 — bốn mảnh lương.** Quan hệ `instructor` có 12 bản ghi theo đúng thứ tự nguồn. Chia lương thành bốn dải:

- $S_1$: dưới 50.000,
- $S_2$: 50.000 đến dưới 60.000,
- $S_3$: 60.000 đến dưới 70.000,
- $S_4$: 70.000 trở lên.

Bốn mảnh bit dùng quy ước vị trí từ $0$ đến $11$ như bộ trang chiếu:

$$S_1=001000000000,\quad S_2=000000000000,$$
$$S_3=100010010000,\quad S_4=010101101111.$$

Diễn giải: vị trí 2 (Mozart) ở $S_1$; không ai trong dải $S_2$; vị trí 0, 4, 7 (Srinivasan, El Said, Califieri) ở $S_3$; số còn lại ở $S_4$.

**Bitmap khoa `Finance`:** Wu ở vị trí 1 và Singh ở vị trí 8:

$$\mathrm{Finance}=010000001000.$$

**Câu trả lời bài 14.13:** câu (a) yêu cầu dựng bốn mảnh $S_1..S_4$; câu (b) yêu cầu liệt kê các bước và chỉ ra bản trung gian, trình bày ở Phần 11.

**Định nghĩa chi phí.** Với $q$ là số giá trị hoặc dải không NULL được mã hóa thành bitmap:

- Các mảnh giá trị chưa nén chiếm $qR$ bit.
- Thêm $R$ bit cho mảnh tồn tại $E$ và $R$ bit cho mảnh NULL khi cần; tối đa mức lưu trữ:

$$(q+2)R\text{ bit}.$$

- Một phép Boolean trên hai mảnh cần $\lceil R/w\rceil$ phép toán từ, với $w$ là số bit một từ máy.

**Ứng dụng vết.** Với $R=12$, phép AND trên `Finance` và `S4` được làm ở Phần 11. Lưu ý bitmap chỉ **tạo ứng viên**; điều kiện dư như lương ≥ 80.000 phải được lọc lại trên bản ghi thật, vì $S_4$ chỉ co dải ≥ 70.000.

::: exercise
Với $q=4$ và $R=12$, tính dung lượng chưa nén tối đa khi giữ cả bitmap tồn tại và bitmap NULL.
:::

::: hint
Dùng $(q+2)R$ bit.
:::

::: solution
Dung lượng tối đa là $(4+2)\cdot12=72$ bit.
:::

## 9. Bitmap với vị trí đã xóa, NULL và NOT

**Vì sao cần mặt nạ.** Phép NOT — phần bù của một mảnh — là hiển nhiên trên bit: `NOT 100110 = 011001`. Nhưng trên một quan hệ thật, vị trí bản ghi đã bị xóa (thẻ rỗng) và vị trí có NULL không có giá trị so sánh được. Nếu chỉ đảo bit, phép NOT sẽ bật nhầm các vị trí đã xóa và các vị trí NULL mà lẽ ra phải loại.

**Đặc tả mặt nạ.** Giới thiệu hai mảnh phụ trợ:

- $E$ — **bitmap tồn tại** (existence): vị trí $r$ bằng 1 nếu có một bản ghi hợp lệ còn đang nằm tại vị trí $r$.
- $V_{\mathrm{NULL}}$ — **bitmap NULL**: vị trí $r$ bằng 1 nếu thuộc tính đang xét có giá trị NULL tại bản ghi $r$.

**Công thức NOT có mặt nạ.** Với mảnh $V_v$ của giá trị $v$:

```text
not(A = v) = (NOT V_v) AND E AND (NOT V_NULL)
```

- `(NOT V_v)` lấy các vị trí không có giá trị $v$;
- `AND E` loại bỏ các vị trí không còn bản ghi;
- `(NOT V_NULL)` loại bỏ các vị trí có NULL, vì NULL không so sánh được với $v$ trong ngữ nghĩa SQL.

**Tính đúng.** Bất biến từng vị trí: $E(r)=1$ đúng khi vị trí còn hiệu lực; $V_{\mathrm{NULL}}(r)=1$ đúng khi vị trí có NULL; $V_v(r)=1$ đúng khi vị trí có giá trị $v$. Do đó `(NOT V_v) AND E AND (NOT V_NULL)` bật 1 chính xác tại các vị trí còn hiệu lực, không NULL, và không mang giá trị $v$ — tức đúng là câu trả lời `A ≠ v` trong SQL.

Không thể thay công thức trên bằng `NOT V_v` khi có vị trí đã xóa hoặc NULL: phép đảo bit sẽ bật cả hai loại vị trí vốn không phải kết quả hợp lệ.

::: exercise
Trong công thức cho `A ≠ v`, $E$ và $V_{\mathrm{NULL}}$ loại hai loại vị trí nào?
:::

::: hint
Một mặt nạ nói vị trí còn bản ghi; mặt nạ kia nói thuộc tính không có giá trị so sánh.
:::

::: solution
$E$ loại vị trí bản ghi đã xóa hoặc không tồn tại. $V_{\mathrm{NULL}}$ loại vị trí có NULL, vì so sánh `NULL ≠ v` không cho giá trị đúng trong ngữ nghĩa SQL.
:::

## 10. Ma trận chọn cấu trúc

Toàn bài thu gọn vào bốn cấu trúc, mỗi cấu trúc ưu tiên một dạng truy cập:

| Truy vấn chiếm ưu thế | Cấu trúc đề xuất | Lý do |
|---|---|---|
| Điểm + khoảng | B+-Tree | dò $O(\log_f K)$ rồi quét thêm $L$ lá cho khoảng |
| Chỉ điểm, không khoảng | Băm tĩnh | $1+t+D$; không giữ thứ tự |
| Bộ lọc nhiều điều kiện trên thuộc tính ít giá trị | Bitmap Index | phép AND/OR trên từ máy; phải lọc dư |
| Cần quét khoảng dài | B+-Tree (lá liên kết) | B-Tree phải gặp dữ liệu ở nhiều mức |

**I/O:** B+-Tree điểm $d+1+J+D$, khoảng $d+1+L+J+D$; B-Tree có thể giảm $d$ cho điểm nhưng quét khoảng tệ; băm $1+t+D$; bitmap đọc các mảnh cần thiết rồi $D$ khối ứng viên.

**Cập nhật:** B+-Tree đọc $O(d+1)$ và ghi tối đa $O(d+1)$; băm tĩnh cập nhật ngăn nhà/tràn của $h(key)$; bitmap phải duy trì $E$, $V_{\mathrm{NULL}}$ và cập nhật mọi $V_v$ khi đổi bản ghi.

**Dung lượng:** B+-Tree $O(K)$ mục + nút; B-Tree tốn dữ liệu; băm cố định $M$ ngăn; bitmap tối đa $(q+2)R$ bit khi cần đủ $E$ và $V_{\mathrm{NULL}}$, một bit/bản ghi/mảnh.

Quy tắc chọn rút gọn: thuộc tính có ít giá trị phân biệt phù hợp với bitmap; thuộc tính có nhiều giá trị phân biệt và cần khoảng phù hợp với B+-Tree; truy vấn chủ yếu bằng khóa, không cần thứ tự và dữ liệu ổn định có thể dùng băm tĩnh.

::: exercise
Một bảng có truy vấn điểm và khoảng thường xuyên trên cùng khóa, còn dữ liệu được cập nhật đều. Chọn cấu trúc trong bảng trên và nêu chi phí cập nhật tiệm cận cần dự trù.
:::

::: hint
Cần một cấu trúc giữ thứ tự và hỗ trợ cả hai dạng truy vấn.
:::

::: solution
Chọn B+-Tree. Mỗi cập nhật phải dò đường cao $d$ và có thể lan tách hoặc gộp qua các mức, nên đọc và ghi ở bậc $O(d+1)$ khối.
:::

## 11. Bài tập từ giáo trình

Bốn bài dưới đây được dịch và giữ nguyên dữ kiện cùng yêu cầu toán học của nguồn.

### Bài 14.1

::: exercise
Chỉ mục làm nhanh quá trình xử lý truy vấn, nhưng thường là ý tưởng xấu khi tạo chỉ mục trên mọi thuộc tính và mọi tổ hợp thuộc tính có thể trở thành khóa tìm kiếm. Giải thích vì sao.
:::

::: hint
Nhắc lại bốn thước đo ở Phần 1: I/O khi chèn/xóa, cập nhật, và không gian phụ trội.
:::

::: solution
Mỗi chỉ mục thêm vào tốn thời gian CPU và I/O đĩa khi chèn và xóa, nên chỉ mục càng nhiều thì chi phí cập nhật càng tăng. Chỉ mục trên thuộc tính không phải khóa chính có thể phải được cập nhật khi giá trị đó đổi, còn chỉ mục trên khóa chính thường không. Mỗi chỉ mục thêm lại chiếm thêm không gian lưu trữ. Cuối cùng, khi đã có nhiều chỉ mục, lợi ích của một chỉ mục thêm bị giảm vì truy vấn nhờ được nhiều chỉ mục hiện có rồi; do đó thêm chỉ mục không còn cải thiện đáng kể hiệu suất trong khi chi phí ngày một cao.
:::

### Bài 14.3(b)

::: exercise
Dựng một B+-Tree cho tập khóa $(2,3,5,7,11,17,19,23,29,31)$ với trường hợp số con trỏ vừa đủ trong một nút là sáu. Giả sử cây ban đầu rỗng và các giá trị được thêm theo thứ tự tăng dần.
:::

::: hint
Với $m=6$, nút trong có tối đa 6 con và nút lá có tối đa 5 khóa. Chèn từng khóa, và khi một lá đầy hãy xem nó có tràn hay không trước khi chèn khóa kế tiếp.
:::

::: solution
Cây cuối: gốc $[7,19]$; lá $[2,3,5]$, $[7,11,17]$, $[19,23,29,31]$.
Vết với $m=6$ (nút lá tối đa 5 khóa): chèn $2,3,5,7,11$ vào cùng một lá; chèn $17$ làm lá tràn, tách thành $[2,3,5]$ và $[7,11,17]$, sao chép $7$ lên gốc. Chèn $19,23$ vào lá phải; chèn $29$ làm lá tràn, tách thành $[7,11,17]$ và $[19,23,29]$, sao chép $19$ lên gốc thành $[7,19]$; chèn $31$ hoàn tất lá $[19,23,29,31]$. Mỗi lá có từ 3 đến 5 khóa và nằm cùng độ sâu $d=1$.
:::

### Bài 14.4 trên cây của 14.3(b)

::: exercise
Với B+-Tree dựng được trong Bài 14.3(b), chỉ ra dạng của cây sau mỗi thao tác trong chuỗi sau:

a. Chèn 9.
b. Chèn 10.
c. Chèn 8.
d. Xóa 23.
e. Xóa 19.
:::

::: hint
Theo dõi theo thứ tự từng bước trên cùng cây của 14.3(b). Chèn 9, 10 thuộc lá giữa; chèn 8 làm lá giữa tràn và gây tách; sau đó xóa 23, rồi xóa 19 gây thiếu và cần gộp lá.
:::

::: solution
Sau bước a (chèn 9): gốc $[7,19]$; lá $[2,3,5]$, $[7,9,11,17]$, $[19,23,29,31]$.

Sau bước b (chèn 10): lá giữa $[7,9,10,11,17]$, chưa tràn.

Sau bước c (chèn 8): lá giữa có 6 khóa, tách 3–3 thành $[7,8,9]$ và $[10,11,17]$; sao chép $10$ lên gốc, gốc thành $[7,10,19]$; lá phải nhất vẫn là $[19,23,29,31]$.

Sau bước d (xóa 23): lá phải $[19,29,31]$, vẫn đủ khóa.

Sau bước e (xóa 19): lá phải $[29,31]$ thiếu; gộp với $[10,11,17]$ thành $[10,11,17,29,31]$; gốc giảm còn $[7,10]$.

Lưu ý lỗi in của nguồn ở bước c: lá phải nhất phải là $[19,23,29,31]$, nguồn in nhầm khóa đầu thành $9$; giữ $19$ để bảo toàn đa tập khóa.
:::

### Bài 14.13

::: exercise
Xét quan hệ `instructor` trong Hình 14.1:

- (a) Dựng bitmap index trên thuộc tính `salary`, chia giá trị lương thành bốn dải: dưới 50.000; từ 50.000 đến dưới 60.000; từ 60.000 đến dưới 70.000; và từ 70.000 trở lên.
- (b) Nêu các bước trả lời truy vấn lấy mọi giảng viên thuộc khoa `Finance` có lương từ 80.000 trở lên, và chỉ ra các bitmap cuối và trung gian được dựng để trả lời truy vấn.
:::

::: hint
Các mảnh lương $S_1..S_4$ đã được dựng và giải thích ở Phần 8. Ở câu (b), giao bitmap khoa `Finance` với $S_4$ trước, rồi quét các bản ghi ứng viên để lọc lương ≥ 80.000.
:::

::: solution
Dữ liệu 12 bản ghi theo thứ tự nguồn: `10101 Srinivasan Comp. Sci. 65000; 12121 Wu Finance 90000; 15151 Mozart Music 40000; 22222 Einstein Physics 95000; 32343 El Said History 60000; 33456 Gold Physics 87000; 45565 Katz Comp. Sci. 75000; 58583 Califieri History 62000; 76543 Singh Finance 80000; 76766 Crick Biology 72000; 83821 Brandt Comp. Sci. 92000; 98345 Kim Elec. Eng. 80000`.

(a) Bốn mảnh lương:

$$S_1=001000000000,\quad S_2=000000000000,$$
$$S_3=100010010000,\quad S_4=010101101111.$$

(b) Giao bitmap `Finance` với $S_4$. Theo quy ước đánh số từ 0, bitmap `Finance` = `010000001000` (Wu ở vị trí 1, Singh ở vị trí 8); giao với $S_4$ giữ nguyên hai vị trí đó:

$$\text{Finance AND } S_4 = 010000001000.$$

Quét các bản ghi ứng viên (Wu, Singh) để lọc lương ≥ 80.000: Cả hai đều thỏa, vậy kết quả là Wu và Singh. Điều kiện ≥ 80.000 là điều kiện dư so với dải $S_4$ ≥ 70.000, nên bắt buộc phải lọc trên bản ghi thật, không chỉ dựa vào bitmap.
:::

---

## Nguồn

- *Database System Concepts*, 7e, Chương 14 — khái niệm chỉ mục, B+-Tree, B-Tree, băm tĩnh và Bitmap Index (trục).
  - Trang chiếu 3–16: bài toán chỉ mục, bốn thước đo; 17–45: B+-Tree; 46–48: B-Tree đối chiếu; 51–59: băm tĩnh và chuỗi tràn; 71–75: bitmap.
- *Database System Concepts*, 7e, Chương 24, trang chiếu 11–15: bitmap tồn tại và NULL cho phép NOT.
- Recitation: Bài 14.1 (đề trang 43; lời giải trang 99), Bài 14.3(b) (đề trang 43; lời giải trang 100), Bài 14.4 trên cây 14.3(b) (đề trang 43; lời giải trang 102), Bài 14.13 (đề trang 45; lời giải trang 108–109).
- Hai công thức băm $1+t+D$ và $\alpha=N_e/(Mc)$ là dẫn xuất của bài giảng trong mô hình một ngăn bằng một khối và không bộ nhớ đệm, không trích nguyên văn tại các trang nguồn được dẫn.
- Lỗi in sau chèn 8 của lời giải 14.4: lá phải nhất được sửa từ 9 thành 19 để bảo toàn đa tập khóa.
- Hình SVG trong `img/lec-13/`.
