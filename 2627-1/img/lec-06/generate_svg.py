#!/usr/bin/env python3
"""Tái tạo hình Bài 06 bằng thư viện chuẩn Python; không cần mạng."""
from pathlib import Path
from html import escape
from math import cos, sin, pi

OUT = Path(__file__).resolve().parent
BLUE, ORANGE, GREEN, INK = '#2f3e7a', '#a85b23', '#26704e', '#233247'

def text(x, y, value, size=28, color=INK, anchor='middle'):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}">{escape(str(value))}</text>'

def line(x1,y1,x2,y2,color=BLUE,dash='',arrow=False):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="3"'+(f' stroke-dasharray="{dash}"' if dash else '')+(' marker-end="url(#arrow)"' if arrow else '')+'/>'

def box(x,y,w,h,label,fill='#edf4ff',color=BLUE):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{fill}" stroke="{color}" stroke-width="2"/>'+text(x+w/2,y+h/2+9,label,color=color)

def svg(name,w,h,title,desc,body):
    data=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>
<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="{BLUE}"/></marker></defs>
<g font-family="Arial, sans-serif">{body}</g></svg>'''
    (OUT/name).write_text(data)

def main():
    # Quan hệ khái niệm của quy trình, không biểu diễn số lượng giả định.
    b=''
    for i,label in enumerate(['Chữ ký','Khóa dải','Ứng viên','Kiểm tập gốc']):
        x=15+i*270;b+=box(x,40,230,80,label)
        if i<3:b+=line(x+236,80,x+264,80,arrow=True)
    b+=text(555,172,'Tập cặp duy nhất trước khi xác minh',30)
    svg('quy-trinh-cap.svg',1100,205,'Quy trình tạo và xác minh cặp','Chữ ký đi qua khóa dải, sinh ứng viên duy nhất rồi kiểm tập gốc.',b)

    # Ma trận chỉ ký hiệu vị trí; các ví dụ số được dựng bằng bảng HTML.
    b=''
    for j in range(4):
        y=32+j*72
        b+=box(95,y,190,54,f'Dải {j+1}', '#edf4ff' if j%2==0 else '#fff4e9')
        b+=line(298,y+27,370,y+27,arrow=True)
        b+=box(386,y,228,54,f'({j+1}, tuple)')
    b+=text(45,180,'n',30)+text(325,337,'b dải, mỗi dải r hàng; n = br',28)
    svg('phan-dai-chu-ky.svg',660,360,'Chia chữ ký thành các dải','Bốn dải minh họa, mỗi dải tạo một khóa gồm số dải và tuple của cột.',b)

    # Đường xác suất tính trực tiếp, trục và chú giải giữ đơn vị xác suất.
    w,h=1100,390;left,top,pw,ph=100,45,740,260
    b=line(left,top,left,top+ph)+line(left,top+ph,left+pw,top+ph)
    for q in [0,.2,.4,.6,.8,1]:
        x=left+pw*q;y=top+ph*(1-q)
        b+=line(x,top+ph,x,top+ph+6)+text(x,top+ph+34,f'{q:g}',24)
        b+=line(left-6,y,left+pw,y,'#dce2ec','4 6')+text(left-18,y+8,f'{q:g}',24,anchor='end')
    for bb,rr,color,dash in [(20,5,BLUE,''),(10,10,ORANGE,'12 7')]:
        pts=' '.join(f'{left+pw*i/300:.2f},{top+ph*(1-(1-(1-(i/300)**rr)**bb)):.2f}' for i in range(301))
        b+=f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="4" stroke-dasharray="{dash}"/>'
    b+=text(470,382,'Jaccard thật s',28)+text(100,28,'P(s)',28)
    b+=line(870,90,940,90,BLUE)+text(957,98,'20 × 5',26,anchor='start')
    b+=line(870,145,940,145,ORANGE,'12 7')+text(957,153,'10 × 10',26,anchor='start')
    b+=text(970,210,'b × r',25)+text(970,248,'n = 100',25)
    svg('xac-suat-phan-dai.svg',w,h,'Xác suất tạo ứng viên của hai cấu hình','Hai đường P(s)=1−(1−s^r)^b với b,r bằng 20,5 và 10,10. Cùng độ dài chữ ký 100.',b)

    b=box(40,60,280,90,'Gần: d ≤ d₁')+box(355,60,280,90,'d₁ < d < d₂','#f8fafc','#788597')+box(670,60,280,90,'Xa: d ≥ d₂','#fff4e9',ORANGE)
    b+=text(180,205,'Pr[h(x)=h(y)] ≥ p₁')+text(495,205,'Không có cận chung')+text(810,205,'Pr[h(x)=h(y)] ≤ p₂')
    b+=line(40,265,950,265,arrow=True)+text(930,310,'Khoảng cách d',26,anchor='end')
    svg('mien-gan-xa.svg',1000,335,'Ba miền của họ nhạy cảm','Miền gần có cận dưới p1, miền xa có cận trên p2, miền giữa không có bảo đảm từ định nghĩa.',b)

    b=''
    for j in range(4):
        y=35+j*68
        for k in range(4):b+=box(20+k*105,y,85,45,f'h{4*j+k+1}',color=BLUE)
        b+=line(425,y+22,480,y+22,arrow=True)+box(492,y,150,45,'AND 4')
        b+=line(651,y+22,722,148,arrow=True)
    b+=box(736,125,180,65,'OR 4','#fff4e9',ORANGE)
    b+=text(330,342,'Mỗi dải tạo một tuple',28)+text(800,250,'Hợp cặp',28)
    svg('ghep-and-or.svg',970,370,'AND bốn phép thử rồi OR bốn nhóm','Mười sáu hàm chia bốn nhóm. Mỗi nhóm AND bốn hàm thành tuple; hợp cặp của bốn nhóm thực hiện OR.',b)

    # Đồ thị tọa độ tỉ lệ đều: (2,7), (6,4), độ lệch 4 và 3.
    b=line(75,410,575,410,arrow=True)+line(75,410,75,20,arrow=True)
    X=lambda x:75+50*x;Y=lambda y:410-50*y
    for x in range(1,9):b+=text(X(x),446,x,32)
    for y in range(1,8):b+=text(47,Y(y)+10,y,32)
    b+=line(X(2),Y(7),X(6),Y(4),BLUE)+line(X(2),Y(7),X(6),Y(7),ORANGE,'8 5')+line(X(6),Y(7),X(6),Y(4),ORANGE,'8 5')
    for x,y in [(2,7),(6,4)]:b+=f'<circle cx="{X(x)}" cy="{Y(y)}" r="7" fill="{BLUE}"/>'
    b+=text(147,35,'x = (2,7)',34)+text(478,245,'y = (6,4)',34)
    b+=text(300,42,'Δ₁ = 4',32,ORANGE)+text(463,137,'Δ₂ = 3',32,ORANGE)+text(246,168,'L₂ = 5',36,BLUE)
    b+=text(604,419,'x₁',34)+text(32,35,'x₂',32)
    svg('chuan-vector.svg',650,470,'Khoảng cách giữa hai điểm','Hai điểm (2,7) và (6,4). Hai trục dùng cùng tỷ lệ 50 đơn vị ảnh cho một đơn vị tọa độ; độ lệch 4 và 3 tạo đoạn nối dài 5.',b)

    # Hình phẳng minh họa mặt phân chia; không gán tọa độ 4D vào hình.
    b=f'<path d="M40,40 H580 V180 H40 Z" fill="#edf4ff"/><path d="M40,180 H580 V315 H40 Z" fill="#fff4e9"/>'
    b+=line(40,180,580,180,BLUE)+line(310,180,310,48,ORANGE,arrow=True)
    b+=text(440,162,'v · x = 0',28)+text(356,60,'v',32,ORANGE)+text(115,105,'Dấu +',32)+text(115,265,'Dấu −',32)
    b+=text(310,356,'Pháp tuyến vuông góc mặt phân chia',26)
    svg('phap-tuyen-dau.svg',630,390,'Pháp tuyến và hai nửa không gian','Mặt phân chia v nhân x bằng 0 nằm ngang; pháp tuyến vuông góc và hướng vào miền dấu dương. Hình hai chiều mô tả quan hệ, không phải tọa độ của ví dụ bốn chiều.',b)

    cx,cy,R=200,205,145;theta=pi/3
    def point(a):return(cx+R*cos(a),cy-R*sin(a))
    def sector(a1,a2):
        x1,y1=point(a1);x2,y2=point(a2)
        return f'<path d="M{cx},{cy} L{x1},{y1} A{R},{R} 0 0 0 {x2},{y2} Z" fill="#ffe5c6" stroke="{ORANGE}" stroke-dasharray="6 4"/>'
    b=f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#f6f8fc" stroke="{BLUE}" stroke-width="2"/>'+sector(pi/2,pi/2+theta)+sector(3*pi/2,3*pi/2+theta)
    for a,label in [(0,'x'),(theta,'y')]:
        x,y=point(a);b+=line(cx,cy,x,y,arrow=True)+text(x+22,y+5,label,30)
    b+=f'<path d="M{cx+65},{cy} A65,65 0 0 0 {cx+65*cos(theta)},{cy-65*sin(theta)}" fill="none" stroke="{GREEN}" stroke-width="3"/>'
    b+=text(274,171,'θ',32,GREEN)
    b+=text(108,53,'θ',30,ORANGE)+text(286,377,'θ',30,ORANGE)
    b+=text(510,115,'Hai miền tách',27)+text(510,164,'Tổng góc 2θ',28,ORANGE)+text(510,213,'trên góc 2π',27)+text(330,411,'Hướng hình chiếu pháp tuyến đều trên vòng tròn',26)
    svg('goc-tach-sieu-phang.svg',650,435,'Hai miền hướng làm khác dấu','Hai hướng x,y tạo góc theta, có cung theta giữa hai mũi tên. Hai miền hướng pháp tuyến đối nhau làm dấu khác nhau, mỗi miền có góc theta; chú giải nằm ngoài vòng tròn.',b)

    b=''
    for i in range(6):
        x=35+i*100;b+=f'<rect x="{x}" y="95" width="100" height="120" fill="'+('#edf4ff' if i%2==0 else '#fff4e9')+'"/>'+line(x,75,x,245)
        if i<5:b+=text(x+50,275,f'k = {i-2}'.replace('-','−'),24)
    b+=line(35,170,635,170,arrow=True)+text(315,35,'Biên: ka − δ',30)
    b+=f'<circle cx="265" cy="170" r="8" fill="{BLUE}"/><circle cx="320" cy="170" r="8" fill="{ORANGE}"/>'
    b+=text(260,140,'u·x',24)+text(312,140,'u·y',24)+line(265,305,320,305,ORANGE)+text(292,343,'ℓ',30,ORANGE)
    svg('chia-khoang-dich.svg',670,365,'Chia khoảng trên trục hình chiếu','Các khoảng nửa mở có độ rộng a; biên có dạng ka−delta. Hai hình chiếu cách nhau ell, có thể bị biên tách.',b)

    # Quan hệ hình chiếu trong mặt phẳng, vẽ lại Hình 3.14 MMDS.
    # Tỷ lệ tam giác có ý nghĩa hình học; không ấn định quan hệ với độ rộng a.
    b=line(55,240,575,240,arrow=True)+line(90,240,380,65,BLUE)
    b+=line(380,65,380,240,ORANGE,'8 5')
    b+=line(90,273,380,273,ORANGE)
    b+=f'<path d="M362,240 V222 H380" fill="none" stroke="{ORANGE}" stroke-width="2"/>'
    b+=f'<path d="M158,240 A68,68 0 0 0 148.2,204.9" fill="none" stroke="{GREEN}" stroke-width="3"/>'
    b+=text(183,224,'φ',36,GREEN)+text(218,135,'ρ',38,BLUE)+text(240,312,'ℓ = ρ |cos φ|',32,ORANGE)
    b+=text(548,220,'u',34)+text(75,218,'x',32)+text(402,65,'y',32)
    for x,y in [(90,240),(380,65)]:b+=f'<circle cx="{x}" cy="{y}" r="6" fill="{BLUE}"/>'
    svg('hinh-chieu-euclid.svg',610,335,'Độ dài đoạn nối và hình chiếu','Đoạn nối x với y dài rho tạo góc nhọn phi với trục chiếu u. Đường vuông góc nét đứt xác định đoạn chiếu dài ell bằng rho nhân trị tuyệt đối cos phi. Hình biểu diễn quan hệ chiếu, không ấn định độ rộng thùng a.',b)

    b=box(15,50,250,70,'Tên')+box(15,145,250,70,'Địa chỉ')+box(15,240,250,70,'Điện thoại')
    for y in [85,180,275]:b+=line(277,y,365,180,arrow=True)
    b+=box(380,135,235,90,'Hợp ứng viên')+line(630,180,715,180,arrow=True)+box(730,135,285,90,'Chấm điểm, xác minh')
    svg('khoa-thuc-the.svg',1050,360,'Ba khóa tạo ứng viên thực thể','Khớp tên, địa chỉ hoặc điện thoại đều có thể sinh cặp; hợp các tập cặp trước khi chấm điểm và xác minh.',b)

    b='';chosen={(1,1),(3,2),(2,4)}
    for i in range(5):
        for j in range(5):
            x=30+j*54;y=35+i*54;chosen_here=(i,j) in chosen
            b+=f'<rect x="{x}" y="{y}" width="54" height="54" fill="'+('#edf4ff' if chosen_here else '#fff')+f'" stroke="{BLUE}" stroke-width="2"/>'
            if chosen_here:b+=text(x+27,y+37,'×',34,BLUE)
    b+=text(165,344,'Ba ô chọn từ lưới',26)+line(315,180,365,180,arrow=True)
    b+=box(385,65,245,95,'Có đủ ba ô')+text(508,198,'→ thùng chung',27)
    b+=box(385,235,245,65,'Thiếu ít nhất một ô','#fff4e9',ORANGE)+text(508,344,'→ thùng riêng',27)
    svg('phep-thu-van-tay.svg',665,380,'Phép thử ba ô vân tay','Lưới khái niệm đánh dấu ba ô được chọn trước khi xét ảnh. Ảnh có đủ ba ô vào một thùng chung; mỗi ảnh thiếu ô nhận thùng đơn riêng.',b)

if __name__ == '__main__':main()
