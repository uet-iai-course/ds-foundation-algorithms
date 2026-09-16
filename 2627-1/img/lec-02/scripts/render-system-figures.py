"""Rebuild the section-5 diagrams; coordinates denote relations, not data sizes."""
from pathlib import Path
from html import escape
OUT = Path(__file__).resolve().parents[1]
N='#2f3e7a'; B='#edf4ff'; G='#526070'; R='#b23b3b'; T='#e8f5e9'
def text(x,y,s,size=25,anchor='middle',color=N):return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" fill="{color}">{escape(s)}</text>'
def box(x,y,w,h,lines,fill=B,size=25):
 z=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{fill}" stroke="{N}" stroke-width="2"/>'
 start=y+h/2-(len(lines)-1)*17+9
 return z+''.join(text(x+w/2,start+i*34,s,size) for i,s in enumerate(lines))
def arrow(x,y,xx,yy,label='',dy=-10,dash=False):
 return f'<path d="M{x},{y} L{xx},{yy}" stroke="{N}" stroke-width="2.5" fill="none" marker-end="url(#arr)"'+(' stroke-dasharray="7 5"' if dash else '')+'/>'+ (text((x+xx)/2,(y+yy)/2+dy,label,22) if label else '')
def cross(x,y,w,h):return f'<path d="M{x},{y} l{w},{h} M{x+w},{y} l{-w},{h}" stroke="{R}" stroke-width="5"/>'
def save(n,body,h,desc):
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{escape(desc,quote=True)}" font-family="Arial, sans-serif" viewBox="0 0 1120 {h}"><defs><marker id="arr" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="{N}"/></marker></defs>{body}</svg>'
 (OUT/f'sys-{n}.svg').write_text(svg)
# Split / task / assigned machine: each pair of rows is one machine's sequence.
b=text(170,30,'6 phần dữ liệu')+text(515,30,'6 tác vụ Map')+text(925,30,'3 máy, nhiều lượt')
for i in range(3):
 y=62+i*88
 b+=box(40,y,260,62,[f'S{i+1}, S{i+4}'])+arrow(303,y+31,375,y+31)+box(380,y,270,62,[f'M{i+1}, M{i+4}'])+arrow(655,y+31,770,y+31)+box(775,y,305,62,[f'Máy {chr(65+i)}: M{i+1} rồi M{i+4}'])
save('02',b,335,'Sáu phần dữ liệu S1 đến S6 tạo sáu Map M1 đến M6. Ba máy A, B, C nhận lần lượt các cặp M1/M4, M2/M5, M3/M6. Mỗi máy chạy một tác vụ mỗi lượt trong ví dụ.')
# Locality: read same B1 replica from A; third worker C is remote; D stores replica.
b=box(15,40,520,235,[],fill='#f8fafc')+box(585,40,520,235,[],fill='#f8fafc')+text(275,29,'Tủ rack 1')+text(845,29,'Tủ rack 2')
b+=box(35,72,220,80,['A: bản sao B₁','Map đọc tại máy'],T,23)+box(300,72,215,80,['B: không có B₁'],size=23)+box(605,72,220,80,['C: không có B₁'],size=23)+box(860,72,220,80,['D: bản sao B₁'],T,23)
b+=arrow(260,118,294,118)+text(275,190,'Nếu Map chạy ở B: đọc từ A.',23)
b+=arrow(150,160,150,220)+arrow(150,220,715,220,'C đọc từ A: đi qua đường nối hai rack',dy=34)+arrow(715,220,715,160)
b+=text(840,190,'Map ở D cũng đọc tại máy.',23)
save('03',b,295,'Hai rack: A và D giữ bản sao cùng khối B1. Map chạy ở A hoặc D đọc cục bộ; B cùng rack A đọc qua mạng trong rack; C đọc bản ở A phải qua đường nối hai rack. Mỗi Map chỉ xử lý một bản của dữ liệu logic.')
# Same partitions across slides 04 and 05.
b=text(245,28,'Tác vụ Map')+text(570,28,'Phần cho R₀')+text(920,28,'Phần cho R₁')
for y,name,inp,p0,p1 in [(60,'M₁','mèo chó mèo','(mèo,1), (mèo,1)','(chó,1)'),(185,'M₂','chó chim','(chim,1)','(chó,1)')]:
 b+=box(30,y,325,85,[name,inp])+arrow(359,y+43,400,y+43)+box(410,y,320,85,[p0],size=24)+box(760,y,320,85,[p1],size=24)
b+=text(560,312,'f(mèo) = 0; f(chim) = 0; f(chó) = 1 — quy tắc minh họa',25)
save('04',b,340,'Không Combine: M1 đọc mèo chó mèo, lưu hai cặp mèo vào phần R0 và cặp chó vào phần R1; M2 đọc chó chim, lưu chim vào phần R0 và chó vào phần R1. Quy tắc f cho trước với hai Reduce.')
b=box(20,40,320,100,['Đĩa của M₁','R₀: mèo, mèo | R₁: chó'],size=23)+box(20,230,320,100,['Đĩa của M₂','R₀: chim | R₁: chó'],size=23)
b+=box(785,40,315,100,['R₀ nhận','mèo, mèo, chim'],size=24)+box(785,230,315,100,['R₁ nhận','chó, chó'],size=24)
b+=arrow(342,73,779,73,'phần 0')+arrow(342,105,779,264)+text(435,120,'phần 1',22)+arrow(342,261,779,106)+text(435,275,'phần 0',22)+arrow(342,296,779,296,'phần 1')
b+=text(560,365,'Mỗi từ trong hình đại diện cho một cặp (từ, 1).',23)
save('05',b,390,'R0 lấy phần 0 từ cả M1 và M2, nhận mèo mèo chim; R1 lấy phần 1 từ cả hai Map, nhận chó chó. Mỗi từ là một cặp từ và số 1; các đường nối thể hiện phần trung gian đi tới đúng Reduce.')
b=box(20,70,285,155,['R₀ sau sắp xếp','(chim,1)','(mèo,1), (mèo,1)'],size=24)+arrow(310,147,405,147)+box(415,70,330,155,['Reduce theo từng khóa','chim: tổng = 1','mèo: 0 → 1 → 2'],size=24)+arrow(750,147,835,147)+box(845,70,250,155,['Kết quả','(chim,1)','(mèo,2)'],T,24)
b+=text(560,280,'Bộ đếm đọc từng giá trị; hệ thống có thể ghép các đoạn đã sắp xếp trên đĩa.',24)
save('06',b,315,'R0 sắp xếp nhóm chim trước mèo. Reduce cho chim nhận một giá trị 1, trả 1; Reduce cho mèo đọc hai giá trị 1, tổng lần lượt 0 rồi 1 rồi 2. Không cần chứa mọi giá trị đếm từ trong RAM.')
b=box(30,60,260,100,['Chờ'])+box(430,60,260,100,['Đang chạy','ghi rõ máy nhận'])+box(830,60,260,100,['Hoàn tất','ghi vị trí đầu ra'])+arrow(295,109,422,109,'giao việc')+arrow(695,109,823,109,'báo xong')
b+=arrow(560,166,560,250)+arrow(560,250,160,250,'mất liên lạc / lỗi: xếp lại hàng chờ',dy=35)+arrow(160,250,160,166)
save('07',b,310,'Tác vụ từ chờ được giao cho máy, chuyển đang chạy rồi hoàn tất khi báo xong. Khi lỗi hoặc mất liên lạc, tác vụ chưa hoàn tất được đưa về hàng chờ để giao lại. Trường hợp mất đầu ra Map đã xong được xét riêng.')
b=box(25,45,315,140,['Máy A hỏng','M₁ đã xong','Đầu ra Map cục bộ'],fill='#ffebee',size=24)+cross(45,77,272,85)
b+=box(405,45,310,140,['Máy B còn hoạt động','Đọc bản sao B₁','Chạy lại M₁'],T,24)+arrow(345,115,397,115)
b+=box(805,45,290,140,['Reduce đang đợi','Lấy phần trung gian','từ địa chỉ mới'],size=24)+arrow(720,115,797,115)
b+=text(560,250,'Đầu vào còn bản sao; đầu ra trung gian đã mất phải được tính lại.',26)
save('09',b,300,'Máy A hỏng làm đầu ra cục bộ của M1 đã hoàn tất không truy cập được. Máy B đọc bản sao B1, chạy lại M1, thông báo địa chỉ mới cho Reduce chưa lấy phần đó.')
b=box(20,35,310,150,['R₀ trên máy hỏng','Chưa hoàn tất','Đầu ra tạm bỏ đi'],fill='#ffebee',size=24)+arrow(336,110,398,110)+box(405,35,310,150,['R₀ trên máy khác','Lấy phần trung gian','Tính và ghi O₀'],size=24)+arrow(720,110,784,110)+box(790,35,310,150,['Hệ tệp phân tán','O₀: khi hoàn tất','O₁: đã có, giữ lại'],T,24)
b+=text(560,250,'Giả sử các phần trung gian Map và bản sao O₁ vẫn truy cập được.',25)
save('10',b,300,'R0 chưa hoàn tất trên máy hỏng bỏ đầu ra tạm, chạy lại ở máy khác từ các phần Map còn truy cập được, ghi O0 khi xong. O1 của R1 đã hoàn tất được giữ trong hệ tệp phân tán.')
print('Generated section-5 SVGs')
b=box(20,25,1080,70,['HDFS: quản lý tệp, vị trí khối và các bản sao'],size=27)
for x,lines in [(20,['Vị trí bản sao','Giao Map gần dữ liệu']),(395,['Đầu vào có bản sao','Map có thể đọc lại']),(770,['Lưu kết quả Reduce','Giữ đầu ra đã hoàn tất'])]:
 b+=arrow(x+165,100,x+165,150)+box(x,155,330,110,lines,T,24)
b+=text(560,318,'NameNode giữ thông tin vị trí; DataNode lưu khối và phục vụ đọc/ghi.',24)
save('02a',b,355,'HDFS quản lý tệp và các bản sao, cung cấp vị trí để giao Map gần dữ liệu, giữ đầu vào để đọc lại và lưu kết quả Reduce. NameNode giữ thông tin vị trí; DataNode lưu các khối. MapReduce chịu trách nhiệm lập lịch tác vụ.')
