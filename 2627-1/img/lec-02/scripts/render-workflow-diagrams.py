from pathlib import Path
from html import escape
out=Path(__file__).resolve().parent.parent
HEAD='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 340" role="img" aria-labelledby="title desc"><title id="title">{}</title><desc id="desc">{}</desc><defs><marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#2f3e7a"/></marker></defs>'
def box(x,y,w,lines,fill='#edf4ff'):
 h=35*len(lines)+24
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="#2f3e7a" stroke-width="2"/>'+''.join(f'<text x="{x+w/2}" y="{y+34+i*35}" text-anchor="middle" font-family="sans-serif" font-size="27" fill="#263238">{escape(t)}</text>' for i,t in enumerate(lines))
def arrow(x,y,xx,yy):return f'<path d="M{x},{y} L{xx},{yy}" fill="none" stroke="#2f3e7a" stroke-width="3" marker-end="url(#a)"/>'
def save(name,title,desc,body): (out/(name+'.svg')).write_text(HEAD.format(escape(title),escape(desc))+body+'</svg>')
s=box(10,50,230,['Tài liệu A/B','2 chuỗi'])+box(320,50,230,['Tách từ','8 lần xuất hiện'])+box(630,50,230,['Bỏ “và”','7 lần xuất hiện'])+box(940,15,250,['Đếm theo từ','5 cặp kết quả'])+box(940,205,250,['Đếm tổng số từ','7'])
s+=arrow(240,90,310,90)+arrow(550,90,620,90)+arrow(860,90,930,65)+arrow(860,120,930,245)
s+='<text x="470" y="290" text-anchor="middle" font-family="sans-serif" font-size="27" fill="#263238">Dữ liệu sau lọc phục vụ cả hai nhánh</text>'
save('ch2-van-ban-luong','Chuỗi xử lý văn bản','Tách, lọc rồi dùng các từ còn lại để đếm theo từ hoặc đếm tổng.',s)
s=''
items=[['HDFS','Văn bản A/B'],['Map','Tách, lọc','phát (w,1)'],['Nhóm khóa','Cùng từ','về cùng nơi'],['Reduce','Cộng theo từ'],['HDFS','Các số đếm']]
for i,lines in enumerate(items):
 s+=box(5+240*i,80,220,lines)
 if i<4:s+=arrow(225+240*i,130,240+240*i,130)
s+='<text x="600" y="305" text-anchor="middle" font-family="sans-serif" font-size="27" fill="#263238">Tách và lọc nằm trong cùng hàm Map</text>'
save('ch2-hadoop-van-ban','Đếm từ trong Hadoop MapReduce','Một công việc MapReduce đọc HDFS, tách lọc trong Map, nhóm khóa, cộng và ghi HDFS.',s)
s=box(10,105,290,['Tách → lọc','Theo từng phần'])+box(425,105,330,['Dữ liệu sạch','Đánh dấu lưu đệm'])+box(870,20,320,['Lưu số đếm','Tính và lưu lần đầu'])+box(870,215,320,['sach.count() → 7','Dùng phần còn lưu'])+arrow(300,150,415,150)+arrow(755,135,860,70)+arrow(755,175,860,255)
save('ch2-spark-dung-lai','Dùng lại dữ liệu sau lọc','Đánh dấu lưu đệm trước hành động đầu; lần tính đầu lưu các phần, hành động sau dùng lại phần còn lưu.',s)
s=box(10,40,230,['HDFS còn A','Đọc lại A'])+box(325,40,220,['Tách từ','5 từ'])+box(630,40,220,['Bỏ “và”','4 từ'])+box(935,40,255,['Tái tạo phần A','Dữ liệu sạch'])+arrow(240,85,315,85)+arrow(545,85,620,85)+arrow(850,85,925,85)+box(325,220,525,['Phần B còn lưu: giữ nguyên'], '#e8f5e9')
save('ch2-spark-khoi-phuc','Khôi phục phần sạch của A','Nguồn A còn trên HDFS; đọc lại, tách và lọc để tái tạo phần A đã mất; phần B còn lưu được giữ.',s)
