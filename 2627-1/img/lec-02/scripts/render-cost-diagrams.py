#!/usr/bin/env python3
"""Rebuild source-based counting diagrams for Lecture 02, MMDS §§2.5–2.6."""
from pathlib import Path
from html import escape
OUT=Path(__file__).resolve().parents[1]
BLUE='#1565c0'; GREEN='#2e7d32'; ORANGE='#ef6c00'; PURPLE='#7b1fa2'
def txt(x,y,s,size=27,color='#233247',anchor='middle'):
 return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}">{escape(s)}</text>'
def box(x,y,w,h,lines,color=BLUE):
 a=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#f6f9fc" stroke="{color}" stroke-width="2"/>'
 if isinstance(lines,str):lines=[lines]
 for i,s in enumerate(lines):a+=txt(x+w/2,y+h/2+(i-(len(lines)-1)/2)*35+9,s,27,color)
 return a
def arrow(x,y,xx,yy,color=BLUE):return f'<path d="M{x},{y} L{xx},{yy}" fill="none" stroke="{color}" stroke-width="3" marker-end="url(#arrow)"/>'
def save(name,title,desc,body):
 s=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 340" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc><defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="{BLUE}"/></marker></defs><g font-family="Arial, sans-serif">{body}</g></svg>'
 (OUT/(name+'.svg')).write_text(s)
# Each arrow enters a task: count its payload once.
b=box(20,55,230,95,['D1: dữ liệu lớn','D2: lớn lớn'])+arrow(250,105,350,105)+box(355,65,180,80,'Map')+arrow(535,105,895,105)+box(900,65,240,80,'Reduce')
b+=txt(705,80,'5 cặp trung gian')+box(265,210,275,80,['Bộ đếm đầu vào Map','Tổng byte: I'],GREEN)+box(835,210,330,80,['Bộ đếm đầu vào Reduce','Tổng byte: M'],ORANGE)+arrow(315,210,315,115)+arrow(870,210,870,115)
save('cost-input','Đếm tại hai đầu vào','Hai tài liệu đi vào Map; năm cặp đi vào Reduce. Đếm mỗi lần nhận dữ liệu, kể cả đọc cục bộ.',b)
save('cost-input-intro','Quan sát hai nơi nhận dữ liệu','Văn bản được Map đọc; năm cặp được Reduce nhận. Đặt bộ đếm tại hai đầu vào.',b.replace('Tổng byte: I','Đọc hai tài liệu').replace('Tổng byte: M','Nhận năm cặp'))
def pairs(combine=False):
 b=txt(100,70,'D1',30)+txt(100,205,'D2',30)
 for i,s in enumerate(['(dữ, 1)','(liệu, 1)','(lớn, 1)']):b+=box(190+235*i,25,210,85,[s,'B byte'])
 if not combine:
  for i in range(2):b+=box(190+235*i,160,210,85,['(lớn, 1)','B byte'],ORANGE)
  b+=txt(600,320,'3 cặp + 2 cặp = 5 cặp; mỗi cặp dài B byte',30)
 else:
  b+=box(190,155,250,95,['(lớn, 1), (lớn, 1)','Gộp tại D2'],ORANGE)+arrow(440,200,575,200)+box(585,155,250,95,['(lớn, 2)','B byte'],GREEN)+txt(600,320,'D1 giữ 3 cặp; D2 gửi 1 cặp → tổng 4 cặp',30)
 return b
save('cost-five','Đếm năm cặp','Ba cặp từ D1 và hai cặp từ D2, giả sử mỗi cặp cùng B byte.',pairs())
save('cost-combine','Gộp hai cặp trong D2','D2 thay hai cặp lớn một bằng một cặp lớn hai; số cặp trung gian từ năm còn bốn.',pairs(True))
b=box(20,75,285,115,['z bộ ma trận','(i, j, m)'],GREEN)+arrow(305,130,420,130)+box(425,90,145,85,'Map')+arrow(570,130,685,130)+box(690,75,275,115,['z cặp tích','(i, m × v[j])'],ORANGE)+arrow(965,130,1010,130)+box(1015,90,175,85,'Reduce')+txt(175,250,'Đếm z đơn vị vào Map',25,GREEN)+txt(850,250,'Đếm z đơn vị vào Reduce',25,ORANGE)+txt(600,320,'Đọc vector là khoản riêng, được đếm ở trang tiếp theo',27)
save('cost-matrix','Hai khoản z khác nhau','Mỗi phần tử ma trận lưu một bộ và phát một cặp tích. Hai bộ đếm nhận hai loại dữ liệu khác nhau.',b)
b=box(30,100,310,120,['Dải vector j','Lⱼ phần tử'],PURPLE)+arrow(340,135,690,65)+arrow(340,185,690,245)+box(700,20,430,90,['Map A: phần ma trận thứ nhất','Đọc Lⱼ phần tử'])+box(700,200,430,90,['Map B: phần ma trận thứ hai','Đọc Lⱼ phần tử'])+txt(495,55,'Lần đọc 1',25)+txt(495,255,'Lần đọc 2',25)+txt(585,330,'Hai tác vụ cùng đọc dải j → tính Lⱼ + Lⱼ = 2Lⱼ',28)
save('cost-stripe','Đọc lặp dải vector','Một dải dài L j phục vụ hai tác vụ Map xử lý hai phần ma trận; tổng hai lần đọc là hai L j.',b)
b=box(20,65,315,140,['Ma trận vào Map','z đơn vị'],GREEN)+txt(365,150,'+',44)+box(405,65,360,140,['Vector vào Map','Cộng aⱼ × Lⱼ qua các dải'],PURPLE)+txt(800,150,'+',44)+box(840,65,340,140,['Tích vào Reduce','z đơn vị'],ORANGE)+txt(600,285,'Ba khoản cùng đơn vị: bản ghi chuẩn hóa',30)
save('cost-sum','Ba khoản tạo tổng chi phí','Cộng bộ ma trận, các lần đọc dải vector và cặp tích đến Reduce. Đơn vị bản ghi chuẩn hóa.',b)
b=txt(155,80,'Tác vụ R0',30)+txt(155,200,'Tác vụ R1',30)
for i,s in enumerate(['dữ: 1','liệu: 1']):b+=box(320+240*i,30,215,85,s,GREEN)
for i in range(3):b+=box(320+240*i,150,215,85,'lớn: 1',ORANGE)
b+=txt(600,315,'Tổng: 2 + 3 = 5 giá trị     |     Lớn nhất: 3 giá trị',31)
save('cost-load','Tổng và tải lớn nhất','R0 nhận hai giá trị thuộc khóa dữ và liệu; R1 nhận ba giá trị khóa lớn. Tổng năm, lớn nhất ba.',b)
b=box(40,25,220,105,'Ảnh Pᵢ')+box(40,195,220,105,'Ảnh Pⱼ')+arrow(260,80,530,135)+arrow(260,245,530,185)+box(540,100,300,120,['Hàm s cho trước','Độ tương tự'])+arrow(840,160,955,160)+box(965,100,225,120,['Vượt τ','Giữ (i, j)'],GREEN)+txt(710,310,'Chỉ xét i < j: không tự so sánh, không lặp thứ tự',26)
save('cost-image-task','Bài toán cặp ảnh','Hai ảnh được hàm độ tương tự đã cho đánh giá; trả chỉ số cặp khác nhau nếu vượt ngưỡng. Không minh họa số đo thực nghiệm.',b)
b=''
ps=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
for k,(i,j) in enumerate(ps):
 for v in [i,j]:
  b+=arrow(240,45+80*v,765,27+54*k,BLUE if v==0 else '#a6b1bd')
for i in range(4):b+=box(40,15+80*i,200,62,f'P{i+1}',ORANGE if i==0 else BLUE)
for k,(i,j) in enumerate(ps):b+=box(775,3+54*k,400,48,f'Khóa {{{i+1}, {j+1}}}: P{i+1} và P{j+1}',ORANGE if i==0 else BLUE)
save('cost-four','Bốn ảnh tạo sáu nơi so sánh','Theo MMDS Hình 2.9: mỗi ảnh đến ba khóa cặp, mỗi khóa nhận hai ảnh; sáu cặp khác nhau.',b)
def factor(group=False):
 b=box(15,55,330,155,['Số ảnh','1 000 000','N'])+txt(377,148,'×',45)+box(410,55,370,155,['Nơi nhận mỗi ảnh','999' if group else '999 999','g − 1' if group else 'N − 1'],ORANGE)+txt(812,148,'×',45)+box(845,55,340,155,['Byte mỗi ảnh','1 000 000','B'],GREEN)
 return b+txt(600,295,'Mỗi lần gửi một ảnh được tính B byte tải ảnh',29)
save('cost-bytes-pair','Ba yếu tố tính byte khi gửi từng cặp','Một triệu ảnh, mỗi ảnh gửi đến 999999 khóa cặp, mỗi bản mang một triệu byte ảnh.',factor())
b=box(30,115,180,90,'P₁')
for k in range(3):
 y=10+105*k;b+=arrow(210,160,570,y+38)+box(580,y,250,80,[f'Khóa {{1, {k+2}}}',f'P₁ và P{k+2}'])
b+=txt(345,325,'ρ = 3 nơi nhận / ảnh',29,ORANGE)+txt(1000,130,'q = 2 ảnh',30,GREEN)+txt(1000,175,'ở mỗi khóa',27,GREEN)
save('cost-qr','Đặt tên từ hình bốn ảnh','Mỗi ảnh có ba bản gửi trung gian, rho bằng ba; mỗi khóa nhận hai ảnh, q bằng hai.',b)
b=box(30,40,340,105,['Nhóm u','1000 ảnh'],GREEN)+box(30,200,340,105,['Nhóm v','1000 ảnh'],PURPLE)+arrow(370,90,700,135)+arrow(370,250,700,175)+box(710,90,450,135,['Một khóa {u, v}','2000 ảnh đã nhận','Dùng lại để so sánh nhiều cặp'])
save('cost-groups','Hai nhóm cùng đến một nơi','Chia một triệu ảnh thành một nghìn nhóm đều. Một khóa cặp nhóm nhận hai nhóm, tổng hai nghìn ảnh.',b)
b=box(15,105,245,100,['Ảnh thuộc nhóm u','N / g ảnh mỗi nhóm'])
for k,(label,y) in enumerate([('{u, v₁}',5),('{u, v₂}',110),('{u, v cuối}',215)]):b+=arrow(260,155,540,y+43)+box(550,y,335,88,[label,'Hai nhóm: 2 × N/g'])
b+=txt(1045,100,'g − 1',35,ORANGE)+txt(1045,145,'khóa cặp nhóm',24)+txt(1045,190,'khác nhau',25)+txt(325,325,'… gửi tới mọi nhóm khác u',26)
save('cost-group-count','Đếm theo cặp nhóm','Mỗi ảnh nhóm u được gửi tới g trừ một khóa cặp nhóm. Mỗi khóa nhận hai nhóm, mỗi nhóm N trên g ảnh. Ba nhánh là phần trích, không phải chỉ ba đích.',b)
save('cost-bytes-group','Ba yếu tố tính byte khi gửi theo nhóm','Một triệu ảnh, mỗi ảnh gửi đến 999 khóa cặp nhóm, mỗi bản mang một triệu byte ảnh.',factor(True))
b=''
for i in range(4):
 b+=txt(160+i*110,28,f'P{i+1}',25)+txt(65,80+i*65,f'P{i+1}',25)
 for j in range(4):
  x=110+j*110;y=42+i*65
  b+=f'<rect x="{x}" y="{y}" width="100" height="58" fill="{"#e8f5e9" if j>i else "#f2f3f5"}" stroke="#a6b1bd"/>'
  b+=txt(x+50,y+37,f'{i+1},{j+1}' if j>i else ('—' if j==i else 'lặp'),24,GREEN if j>i else '#687584')
b+=box(625,50,550,200,['4 ảnh × 3 đối tác = 12 lượt','(1, 2) và (2, 1) là cùng một cặp','Chia 2 → 6 cặp khác nhau'])
save('cost-comparisons','Bỏ đếm đôi để đếm các cặp ảnh','Ma trận bốn ảnh có sáu ô phía trên đường chéo biểu diễn sáu cặp khác nhau; phía dưới lặp thứ tự, đường chéo tự so sánh.',b)
