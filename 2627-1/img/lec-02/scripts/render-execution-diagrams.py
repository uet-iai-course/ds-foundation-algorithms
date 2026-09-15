from pathlib import Path
from html import escape
out=Path(__file__).resolve().parent.parent;out.mkdir(exist_ok=True)
def svg(name,title,desc,body,h=360):
 s=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc><defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="#2f3e7a"/></marker></defs><style>text{{font-family:Arial,sans-serif;font-size:25px;fill:#263238}}.head{{font-weight:bold;fill:#2f3e7a}}.arrow{{fill:none;stroke:#2f3e7a;stroke-width:2.5;marker-end:url(#arrow)}}.fault{{fill:#fff0ee;stroke:#b3392e;stroke-width:2}}.box{{fill:#edf4ff;stroke:#2f3e7a;stroke-width:2}}.good{{fill:#edf7ef;stroke:#387343;stroke-width:2}}</style>{body}</svg>'''
 (out/name).write_text(s)
def t(x,y,text,cls=''):return f'<text x="{x}" y="{y}" class="{cls}">{escape(text)}</text>'
def box(x,y,w,h,cls='box'):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" class="{cls}"/>'
def a(path):return f'<path d="{path}" class="arrow"/>'
# Map tasks: data ownership, not a machine assignment.
b=t(20,32,'Phần dữ liệu đầu vào','head')+t(460,32,'Tác vụ được tạo','head')+t(825,32,'Lời gọi hàm','head')
for y,idx,doc,calls in [(70,0,'D1: dữ liệu lớn','Map(D1)'),(205,1,'D2: lớn lớn','Map(D2)')]:
 b+=box(20,y,310,95)+t(38,y+37,f'Phần {idx}')+t(38,y+73,doc)+a(f'M330 {y+48} L450 {y+48}')+box(460,y,280,95)+t(480,y+40,f'Tác vụ Map {idx}')+t(480,y+75,f'Đọc phần {idx}')+a(f'M740 {y+48} L805 {y+48}')+t(825,y+55,calls)
b+=t(20,343,'Minh họa: mỗi phần chứa một tài liệu; hai tác vụ dùng cùng hàm Map.')
svg('ch2-tao-tac-vu-map.svg','Chia đầu vào để tạo tác vụ Map','Phần 0 chứa D1 được giao Map 0, phần 1 chứa D2 được giao Map 1. Hai tác vụ cùng mã hàm, khác phần dữ liệu.',b)
# Partition across all mappers.
b=t(20,30,'Tệp trung gian trên máy chạy Map','head')+t(750,30,'Đầu vào tác vụ Reduce','head')
for y,idx,machine in [(65,0,'A'),(225,1,'B')]:
 b+=box(20,y,445,120)+t(38,y+30,f'Map {idx} · đĩa cục bộ máy {machine}','head')
 b+=t(38,y+67,'Gửi R0: (dữ,1), (liệu,1)' if idx==0 else 'Gửi R0: rỗng')
 b+=t(38,y+102,'Gửi R1: (lớn,1)' if idx==0 else 'Gửi R1: (lớn,1), (lớn,1)')
b+=box(750,65,325,120,'good')+t(770,97,'R0: h(k) = 0','head')+t(770,135,'dữ → [1]')+t(770,168,'liệu → [1]')
b+=box(750,225,325,120,'good')+t(770,257,'R1: h(k) = 1','head')+t(770,300,'lớn → [1, 1, 1]')
b+=a('M465 130 L738 130')+a('M465 165 C600 165 615 275 738 275')+a('M465 325 L620 325 L738 310')
svg('ch2-phan-vung-reduce.svg','Mọi Map cùng phân chia đầu ra theo một hàm khóa','Minh họa h(dữ)=h(liệu)=0,h(lớn)=1. Map 0 trên A phát hai tệp, Map 1 trên B có tệp R0 rỗng. R0 thu dữ và liệu; R1 thu ba số1 của lớn từ cả hai Map.',b,370)
# Master schedules workers; dashed status return represented labels rather than crossed arrows.
b=box(280,20,540,100)+t(310,58,'Bộ điều phối (Master)','head')+t(310,95,'Chờ → đang chạy → hoàn thành')
for x,worker,task in [(20,'A','Map 0'),(295,'B','Map 1'),(570,'C','Reduce 0'),(845,'D','Reduce 1')]:
 b+=box(x,205,235,105)+t(x+17,243,f'Máy {worker} · Worker','head')+t(x+17,282,f'Chạy {task}')+a(f'M{max(310,min(x+117,790))} 120 L{x+117} 193')
b+=t(20,350,'Worker báo hoàn thành; bộ điều phối cập nhật trạng thái rồi giao việc tiếp.')
svg('ch2-phan-bo-tac-vu.svg','Bộ điều phối giao tác vụ cho tiến trình trên các máy','Sơ đồ phân công minh họa dựa Hình2.3. Master giao Map0,Map1 cho Worker ở máyA,B; giao Reduce0,Reduce1 cho Worker ở máyC,D. Các mũi tên là phân công, không phải dữ liệu; không khẳng định bốn tác vụ chạy đồng thời.',b,375)
# Failure diagrams explicit sequence, one slide per failure.
for kind in ['map','reduce']:
 ismap=kind=='map';task='Map 0' if ismap else 'Reduce 1';machine='A' if ismap else 'D';new='E' if ismap else 'F'
 steps=[('1. Phát hiện',f'Máy {machine} không', 'phản hồi kiểm tra'),('2. Đưa về chờ',f'{task} về chờ','Kể cả đã xong' if ismap else 'Tác vụ đang chạy'),('3. Giao máy khác',f'Máy {new} chạy {task}' if ismap else 'Chạy lại trên máy F','Đọc lại D1 từ hệ tệp' if ismap else 'Đọc lại tệp Map'),('4. Hoàn thành','Tạo tệp Map mới' if ismap else 'Ghi kết quả mới','Báo nơi lưu mới' if ismap else 'vào hệ tệp phân tán')]
 b=''
 for i,(head,l1,l2) in enumerate(steps):
  x=10+i*275;b+=box(x,55,252,150,'fault' if i==0 else 'box')+t(x+14,88,head,'head')+t(x+14,135,l1)+t(x+14,177,l2)
  if i<3:b+=a(f'M{x+252} 125 L{x+270} 125')
 b+=box(10,245,1075,72,'good')+t(30,290,'Map 1 trên máy B còn hoạt động: không chạy lại.' if ismap else 'Reduce 0 đã xong: giữ kết quả trong hệ tệp phân tán.')
 svg(f'ch2-phuc-hoi-{kind}.svg',f'Phục hồi khi máy {kind.title()} hỏng',f'Bộ điều phối phát hiện máy {machine} không phản hồi, đặt {task} về chờ, giao máy {new} thực hiện lại. '+('Đầu ra cục bộ mất nên Map0 đã xong cũng phải chạy lại; cập nhật vị trí tệp mới cho Reduce.' if ismap else 'Chỉ chạy lại Reduce1 đang thực hiện; đầu ra Reduce0 đã hoàn tất vẫn còn trong hệ tệp phân tán.'),b,345)
print('created',len(list(out.glob('*.svg'))),'SVG')
