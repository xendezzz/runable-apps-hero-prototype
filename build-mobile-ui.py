from pathlib import Path
from html import escape
out=Path('dist/assets/mobile-apps')
def text(x,y,s,size=24,color='#202526',weight=400): return f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" fill="{color}" font-weight="{weight}">{escape(s)}</text>'
def rect(x,y,w,h,c,r=18): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{c}"/>'
def svg(name,w,h,body): (out/(name+'.svg')).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{body}</svg>')
def phone(body,bg='#fff'): return rect(300,38,280,550,'#172124',36)+rect(306,44,268,538,bg,30)+text(326,72,'9:41',12)+rect(402,55,75,15,'#172124',8)+body+rect(402,562,75,4,'#293737',2)
configs=[('install','#e5f0e8','TRAIL','Your next adventure'),('edit','#e8eafa','FOLIO','Make room for ideas'),('login','#fae8d9','STORYTIME','A world of stories'),('pay','#eee4f5','STUDIO','Move at your pace'),('notify','#e4eff6','DRIFT','Time for a little calm'),('update','#f8ebc9','PANTRY','Fresh ideas, daily')]
for i,(key,bg,brand,title) in enumerate(configs):
 body=rect(0,0,880,650,bg,0)+text(48,65,f'0{i+1}',16,'#687377')
 ui=text(328,118,brand,16,'#344749',700)
 if i==0:
  ui+=text(328,161,'Find your trail',25,'#1e4439',700)+rect(325,183,230,180,'#bdd8bb')+'<path d="M326 360L385 230L426 300L480 205L555 360Z" fill="#568069"/><path d="M430 355Q380 320 455 290T480 235" stroke="#f8edd5" stroke-width="5" fill="none"/>'+text(329,394,'Cedar Ridge',23)+text(329,422,'4.2 km · Easy · 55 min',14)+rect(325,454,230,46,'#254e3b')+text(372,483,'Start exploring',16,'white')
  body+=rect(61,254,186,112,'#fff')+text(82,289,'Build ready',22)+text(82,318,'Open on your phone',14)+text(214,424,'→',50,'#426e55')
 elif i==1:
  ui+=text(328,164,'Your creative space',21,weight=700)
  for j,(c,t) in enumerate([('#d9d5f2','Moodboards'),('#ffd59f','Sketchbook'),('#ccd9e5','Saved ideas')]): ui+=rect(326,188+j*101,228,84,c)+text(344,228+j*101,t,19)
  body+=rect(48,430,267,111,'#fff')+text(66,463,'Add a sketchbook tab',18)+text(66,498,'Ask for your next change',13,'#777')
 elif i==2:
  ui+='<circle cx="440" cy="214" r="65" fill="#e9b480"/>'+text(408,233,'Aa',49,'#713f32')+text(337,316,'Your story starts here',21,weight=700)
  for j,t in enumerate(['Continue with Apple','Continue with Google','Use email']): ui+=rect(326,342+j*57,228,43,'#272323' if j==0 else '#f0eae4')+text(342,369+j*57,t,15,'white' if j==0 else '#333')
 elif i==3:
  ui+=text(328,162,'Find your flow',26,weight=700)+rect(326,186,228,115,'#bba4d5')+text(347,230,'STUDIO PLUS',15)+text(347,272,'$12 / month',27)+text(328,345,'A practice that fits you',19)
  for j,t in enumerate(['Unlimited classes','Your personal plan','Offline sessions']): ui+=text(330,385+j*31,'✓  '+t,15)
  ui+=rect(326,487,228,43,'#644977')+text(386,515,'Join Studio',16,'white')
 elif i==4:
  ui+=text(328,165,'Take a breath',27,weight=700)+'<circle cx="440" cy="291" r="90" fill="#c5e0e5"/><circle cx="440" cy="291" r="65" fill="#86b3c3"/><circle cx="440" cy="291" r="37" fill="#477e99"/>'+text(402,297,'Breathe',20,'white')+text(358,433,'A little space for you.',17)
  body+=rect(208,455,448,86,'white')+rect(227,474,43,43,'#477e99',12)+text(287,485,'DRIFT',13,weight=700)+text(287,512,'Your evening wind-down is ready.',17)
 else:
  ui+=text(328,162,'What’s cooking?',26,weight=700)+rect(326,182,228,190,'#f3d88d')+'<circle cx="440" cy="276" r="78" fill="#fff8e7"/><circle cx="440" cy="276" r="58" fill="#ce8d43"/><path d="M411 254Q468 215 475 287Q425 321 411 254" fill="#668d49"/>'+text(328,410,'Something seasonal',22)+text(328,442,'Fresh recipes, just for you',15)
  body+=rect(175,482,530,70,'white')+text(201,513,'Version 1.2 is live',21)+text(201,538,'Your latest changes, delivered.',14,'#667')
 body+=phone(ui,bg='#fffefa') if i not in [4,5] else phone(ui,bg='#fffefa')
 # Floating banners in front of the phone.
 if i==4: body+=rect(208,455,448,86,'white')+text(235,485,'DRIFT',13,weight=700)+text(235,512,'Your evening wind-down is ready.',17)
 if i==5: body+=rect(175,482,530,70,'white')+text(201,513,'Version 1.2 is live',21)+text(201,538,'Your latest changes, delivered.',14,'#667')
 svg('feature-'+key,880,650,body)
# Two different mobile projects shown inside Runable's own editing surfaces.
mark=Path('dist/assets/hero/runable-mark.svg').read_text()
import base64
logo='data:image/svg+xml;base64,'+base64.b64encode(mark.encode()).decode()
def runable(x,y):return f'<image href="{logo}" x="{x}" y="{y-23}" width="26" height="26"/>'+text(x+37,y,'Runable',24,weight=700)
body=rect(0,0,420,840,'#fcfcfa',28)+text(26,31,'9:41',13)+runable(25,85)+text(26,139,'FLORA / garden journal',19,weight=700)+rect(25,160,370,405,'#e6efdd')
body+=text(47,200,'Grow something good.',25,'#365e40',700)
for i,(a,b) in enumerate([('Monstera','New leaf today'),('Olive tree','Water tomorrow'),('Herb garden','Ready to harvest')]):
 body+=rect(43,229+i*100,334,84,'#fafbf5')+f'<ellipse cx="81" cy="{267+i*100}" rx="18" ry="27" fill="#678752"/>'+text(117,264+i*100,a,18,weight=700)+text(117,287+i*100,b,14,'#687561')
body+=text(29,608,'Your garden app is ready.',18)+rect(25,637,370,73,'#eff0ec')+text(43,667,'Add a photo journal for each plant.',15)+rect(25,751,370,57,'white')+text(45,786,'Ask anything',17,'#898989')+text(351,788,'↑',26)
svg('manage-mobile',420,840,body)
body=rect(0,0,1440,940,'#fafaf8',22)+rect(0,0,1440,58,'#eeefed',22)+text(36,37,'●  ●  ●',18,'#a2aaa7')+text(610,36,'Runable / WAVE',15)+runable(28,110)+rect(20,147,340,745,'#f1f2ef')+text(43,191,'Build a podcast discovery app.',20)+text(43,226,'Deep blue, with bold cover art.',18)+text(43,301,'Your mobile app is ready.',20)+text(43,339,'Three screens. One experience.',16)+rect(38,800,302,62,'white')+text(55,837,'Describe your next change…',16,'#888')
for i,(title,caption,col) in enumerate([('Listen closer.','Discover','#e88f55'),('The daily edit','Your library','#a8bedd'),('Now playing','A slower morning','#adbb7c')]):
 x=403+i*335;body+=rect(x,130,302,665,'#132a4a',30)+text(x+22,164,'9:41',13,'white')+text(x+22,211,'WAVE',19,'#bad0e9',700)+text(x+22,257,title,26,'white',700)+rect(x+20,286,262,250,col)+f'<circle cx="{x+151}" cy="411" r="76" fill="#193657"/>'+text(x+86,421,'WAVE',32,'white',700)+text(x+22,578,caption,20,'white')+text(x+22,615,'Stories worth your time',16,'#bfcada')+rect(x+24,656,250,5,'#749fc5',2)+text(x+130,720,'▶',28,'white')
body+=text(407,851,'Preview your mobile experience',23)+text(407,885,'Discover   /   Library   /   Player',16,'#64717c')
svg('manage-desktop',1440,940,body)
# Static overview artwork for the walkthrough slot, until a video is supplied.
body=rect(0,0,1440,810,'#ecebe2',0)+text(80,135,'An idea. A conversation.',53,'#28382f',700)+text(80,204,'An app in your hands.',53,'#28382f',700)+rect(80,302,570,142,'white')+text(108,351,'Create a cycling companion with routes,',23)+text(108,389,'ride stats and a weekly challenge.',23)+text(80,536,'VELO',74,'#335244',700)+text(85,582,'Your next ride starts here.',25,'#687567')
body+=rect(825,45,365,740,'#faf9f1',35)+text(850,89,'9:41',14)+text(853,147,'VELO',28,'#335244',700)+text(853,203,'Take the scenic route.',24)+rect(850,238,315,270,'#c5d7b5')+'<path d="M855 470Q1100 465 1030 390T1140 260" fill="none" stroke="#5c8260" stroke-width="19"/>'+text(859,560,'Riverside loop',28,weight=700)+text(859,602,'18.4 km     240 m     Easy',19)+rect(851,644,313,69,'#335244')+text(948,687,'Start ride',22,'white')
svg('process-overview',1440,810,body)
