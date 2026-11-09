import asyncio
from brand import render
F='node_modules/@fontsource/'
CSS=f"""
@font-face{{font-family:Anton;src:url({F}anton/files/anton-latin-400-normal.woff2)}}
.p{{width:1080px;height:1350px;position:relative;overflow:hidden;background:#07070D;color:#F5F3FF;font-family:Inter,sans-serif}}
.grid{{position:absolute;left:-200px;right:-200px;bottom:-120px;height:620px;background-image:linear-gradient(rgba(255,59,59,.22) 2px,transparent 2px),linear-gradient(90deg,rgba(255,59,59,.22) 2px,transparent 2px);background-size:90px 90px;transform:perspective(700px) rotateX(62deg);transform-origin:bottom;mask-image:linear-gradient(to top,#000 10%,transparent 85%);-webkit-mask-image:linear-gradient(to top,#000 10%,transparent 85%)}}
.halo{{position:absolute;width:1100px;height:1100px;border-radius:50%;left:-10px;top:120px;background:radial-gradient(circle,rgba(255,59,59,.28),transparent 60%)}}
.top{{position:absolute;top:54px;left:64px;right:64px;display:flex;justify-content:space-between;align-items:center;z-index:5}}
.logo{{height:52px;filter:drop-shadow(0 0 1.5px rgba(255,244,222,.85)) drop-shadow(0 0 14px rgba(255,244,222,.18))}}
.cnt{{border:1.5px solid rgba(255,255,255,.25);padding:8px 18px;border-radius:999px;font-weight:600;font-size:22px;color:#C9C4DA}}
.bot{{position:absolute;bottom:48px;left:64px;right:64px;display:flex;justify-content:space-between;align-items:center;font-weight:600;font-size:24px;color:#C9C4DA;z-index:5}}
.sw{{background:#FF3B3B;color:#fff;padding:14px 28px;border-radius:999px;font-weight:800;box-shadow:0 0 30px rgba(255,59,59,.55)}}
.poster{{font-family:Anton,sans-serif;text-transform:uppercase;line-height:.95}}
.red{{color:#FF3B3B}} .gold{{color:#FFC24B}}
.tag{{display:inline-block;font-weight:800;letter-spacing:5px;font-size:22px;color:#FF3B3B;border:2px solid #FF3B3B;padding:8px 16px;border-radius:8px}}
.glass{{background:linear-gradient(160deg,rgba(255,255,255,.10),rgba(255,255,255,.03));border:1.5px solid rgba(255,255,255,.16);border-radius:28px;backdrop-filter:blur(6px);box-shadow:0 30px 80px rgba(0,0,0,.5)}}
.fix{{background:linear-gradient(135deg,#FFC24B,#FF8A3D);color:#140C02;border-radius:22px;padding:30px 34px;font-size:36px;line-height:1.38;font-weight:600;box-shadow:0 0 40px rgba(255,194,75,.35)}}
.fix b{{font-weight:800;color:#140C02 !important}}
.prob{{font-size:30px;line-height:1.4;color:#D9D4EA}}
.chip{{display:inline-block;background:rgba(255,59,59,.15);border:1.5px solid rgba(255,59,59,.6);color:#FF8F8F;border-radius:999px;padding:10px 22px;font-size:26px;font-weight:600;margin:0 12px 12px 0}}
.okc{{background:rgba(61,220,151,.14);border-color:rgba(61,220,151,.6);color:#7CF0BE}}
"""
def page(n,T,inner,last=False):
    return f'''<style>{CSS}</style><div class="p"><div class="halo"></div><div class="grid"></div>
<div class="top"><img class="logo" src="adynic-logo.png"><span class="cnt">{n}/{T}</span></div>{inner}
<div class="bot"><span>adynic.com</span><span class="sw">{'Save &amp; Share' if last else 'Swipe &#8594;'}</span></div></div>'''

def funnel(leaks=True, fixed=False, w=640):
    col = '#FFC24B' if fixed else '#FF3B3B'
    drips=''
    if leaks and not fixed:
        for i,(x,y) in enumerate([(150,150),(470,250),(205,340),(452,425)],1):
            drips+=f'''<g><path d="M{x} {y} q -10 26 0 44 q 10 -18 0 -44z" fill="#FF3B3B"/><circle cx="{x}" cy="{y+70}" r="9" fill="#FF3B3B" opacity=".8"/><circle cx="{x}" cy="{y+105}" r="6" fill="#FF3B3B" opacity=".5"/>
<circle cx="{x}" cy="{y-8}" r="26" fill="#07070D" stroke="#FF3B3B" stroke-width="3"/><text x="{x}" y="{y+1}" text-anchor="middle" font-family="Anton" font-size="26" fill="#FF3B3B">0{i}</text></g>'''
    bands=''
    labels=['AD','LANDING PAGE','CART','CHECKOUT']
    for i,(y,h,l,r) in enumerate([(60,95,40,600),(165,95,95,545),(270,95,150,490),(375,95,205,435)]):
        bands+=f'<path d="M{l} {y} L{r} {y} L{r-50} {y+h} L{l+50} {y+h} Z" fill="url(#g{1 if fixed else 0})" stroke="{col}" stroke-width="2.5" opacity="{1-i*0.12}"/>'
        bands+=f'<text x="320" y="{y+h/2+10}" text-anchor="middle" font-family="Inter" font-weight="800" font-size="24" letter-spacing="3" fill="#fff">{labels[i]}</text>'
    out = f'<rect x="255" y="480" width="130" height="60" rx="10" fill="{col}"/><text x="320" y="520" text-anchor="middle" font-family="Anton" font-size="30" fill="#07070D">SALES</text>'
    return f'''<svg width="{w}" height="{w*600/640:.0f}" viewBox="0 0 640 600"><defs>
<linearGradient id="g0" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF3B3B" stop-opacity=".35"/><stop offset="1" stop-color="#FF3B3B" stop-opacity=".08"/></linearGradient>
<linearGradient id="g1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFC24B" stop-opacity=".45"/><stop offset="1" stop-color="#FF8A3D" stop-opacity=".12"/></linearGradient>
<filter id="gl"><feGaussianBlur stdDeviation="8" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>
<g filter="url(#gl)">{bands}{out}</g>{drips}</svg>'''

T=7
s=[]
s.append(page(1,T,f'''<div style="position:absolute;top:170px;left:64px;right:64px;z-index:3">
<span class="tag">AD BUDGET DIAGNOSIS</span>
<div class="poster" style="font-size:118px;margin-top:26px">Aapke ads ka<br><span class="red">paisa</span> yahan<br>leak ho raha hai</div></div>
<div style="position:absolute;left:220px;top:690px;z-index:3">{funnel(w=640)}</div>'''))
s.append(page(2,T,f'''<div style="position:absolute;top:160px;left:64px;right:64px;z-index:3">
<span class="tag">THE LEAK MAP</span>
<div class="poster" style="font-size:84px;margin-top:22px">Problem ads nahi,<br><span class="red">funnel</span> hai</div>
<div class="prob" style="margin-top:22px">Customer 4 jagah se nikal jaata hai. Ek-ek karke band karte hain</div></div>
<div style="position:absolute;left:150px;top:600px;z-index:3">{funnel(w=780)}</div>'''))

def leak(n,title,where,mock,problems,fixtxt):
    chips=''.join(f'<span class="chip">{p}</span>' for p in problems)
    return page(n,T,f'''<div style="position:absolute;top:150px;left:64px;right:64px;z-index:3">
<span class="tag">LEAK 0{n-2} &middot; {where}</span>
<div class="poster" style="font-size:78px;margin-top:20px">{title}</div></div>
<div style="position:absolute;top:450px;left:64px;right:64px;z-index:3">{mock}
<div style="margin-top:26px">{chips}</div>
<div class="fix" style="margin-top:10px"><b>FIX:</b> {fixtxt}</div></div>''')

adm=f'''<div class="glass" style="padding:26px;display:flex;gap:26px;align-items:center">
<div style="width:320px;height:340px;border-radius:20px;background:linear-gradient(135deg,#2A2440,#151222);display:flex;align-items:center;justify-content:center;font-family:Anton;font-size:40px;color:#6E6788;text-align:center">PRODUCT<br>PHOTO</div>
<div style="flex:1"><div style="font-size:22px;color:#9A94B2;font-weight:600">SPONSORED</div>
<div style="font-size:38px;font-weight:800;margin:10px 0 20px">"New collection available. Shop now"</div>
<div style="font-size:22px;color:#9A94B2">Viewer attention</div>
<div style="height:16px;border-radius:8px;background:rgba(255,255,255,.1);margin-top:8px;overflow:hidden"><div style="width:18%;height:100%;background:#FF3B3B"></div></div>
<div style="font-size:22px;color:#FF8F8F;margin-top:8px;font-weight:600">Scroll ho gaya in 1.2 sec</div></div></div>'''
s.append(leak(3,'Ad dekhte hi<br><span class="red">scroll</span>',"AD",adm,['Koi hook nahi','Sirf product photo','Benefit gayab'],
 'Pehle 3 second mein <b>problem ya result</b> dikhao. Har hafte 3–4 naye hooks test karo'))

lp=f'''<div class="glass" style="padding:24px;display:flex;gap:22px">
<div style="flex:1;border-radius:18px;background:#14111F;padding:18px;position:relative;height:420px">
<div style="height:180px;border-radius:12px;background:linear-gradient(135deg,#2A2440,#1B1729)"></div>
<div style="height:18px;width:70%;background:#2C2742;border-radius:6px;margin-top:16px"></div>
<div style="height:14px;width:50%;background:#2C2742;border-radius:6px;margin-top:10px"></div>
<div style="height:14px;width:60%;background:#2C2742;border-radius:6px;margin-top:10px"></div>
<div style="position:absolute;left:18px;right:18px;bottom:18px;height:46px;border-radius:10px;background:#2C2742;display:flex;align-items:center;justify-content:center;font-size:18px;color:#6E6788;font-weight:700">BUY BUTTON (neeche chhupa)</div>
<div style="position:absolute;right:-12px;top:-12px;background:#FF3B3B;color:#fff;font-weight:800;font-size:20px;padding:8px 14px;border-radius:10px">LOAD 6s</div></div>
<div style="width:300px;display:flex;flex-direction:column;gap:14px;justify-content:center">
<div style="font-size:28px;color:#FF8F8F;font-weight:700">&#10007; Reviews nahi</div>
<div style="font-size:28px;color:#FF8F8F;font-weight:700">&#10007; Price clear nahi</div>
<div style="font-size:28px;color:#FF8F8F;font-weight:700">&#10007; Ad ka offer page pe nahi</div>
<div style="font-size:28px;color:#FF8F8F;font-weight:700">&#10007; Slow page</div></div></div>'''
s.append(leak(4,'Page khula,<br>bharosa <span class="red">nahi</span> bana',"LANDING PAGE",lp,['Generic homepage','No social proof'],
 'Ad se seedha <b>product page</b> pe bhejo. Upar price, reviews aur buy button, aur page 3 sec se kam mein load ho'))

steps=''.join(f'<div style="flex:1;text-align:center"><div style="width:100px;height:100px;margin:0 auto;border-radius:50%;border:3px solid {"#FF3B3B" if i>1 else "#7CF0BE"};display:flex;align-items:center;justify-content:center;font-family:Anton;font-size:44px">{i}</div><div style="font-size:24px;color:#9A94B2;margin-top:12px;font-weight:600">{l}</div></div>' for i,l in enumerate(['Cart','Login','Address','OTP','Pay'],1))
ck=f'''<div class="glass" style="padding:44px 30px"><div style="display:flex;align-items:flex-start">{steps}</div>
<div style="margin-top:34px;font-size:30px;color:#FF8F8F;font-weight:700;text-align:center">Har extra step pe customer kam hote jaate hain</div></div>'''
s.append(leak(5,'Cart bhara,<br>order <span class="red">gayab</span>',"CHECKOUT",ck,['5 step checkout','Login zaroori','COD nahi'],
 '<b>1-page checkout</b>, guest checkout aur COD option. Shipping charge pehle hi dikhao'))

tl=''.join(f'<div style="display:flex;gap:20px;align-items:center;margin-bottom:28px"><div style="width:170px;font-family:Anton;font-size:40px;color:{c}">{t}</div><div style="flex:1;font-size:31px;font-weight:600">{d}</div></div>' for t,d,c in [('0 MIN','Visitor cart chhod ke gaya','#FF8F8F'),('30 MIN','WhatsApp reminder: "Aapka cart wait kar raha hai"','#FFC24B'),('1 DAY','Retargeting ad with reviews','#FFC24B'),('2 DAYS','Chhota offer, sirf unke liye','#7CF0BE')])
fu=f'<div class="glass" style="padding:30px">{tl}</div>'
s.append(leak(6,'Gaya customer<br>kabhi <span class="red">wapas nahi</span>',"FOLLOW-UP",fu,['No retargeting','No WhatsApp/email'],
 'Retargeting aur <b>automatic WhatsApp reminders</b> set karo. Ye log aapko pehle se jaante hain'))

s.append(page(7,T,f'''<div style="position:absolute;top:150px;left:64px;right:64px;z-index:3">
<span class="tag" style="color:#FFC24B;border-color:#FFC24B">LEAK FIXED</span>
<div class="poster" style="font-size:96px;margin-top:20px">Same budget<br><span class="gold">zyada sales</span></div></div>
<div style="position:absolute;left:300px;top:540px;z-index:3">{funnel(leaks=False,fixed=True,w=480)}</div>
<div style="position:absolute;left:64px;right:64px;top:1040px;z-index:3;font-size:32px;line-height:1.45;font-weight:600">Comment karo <span class="gold" style="font-weight:800">"LEAK"</span>, hum aapka funnel free check karke batayenge<br><span style="color:#C9C4DA">Follow <b class="gold">@adynic_</b></span></div>''',last=True))
asyncio.run(render(s,'leak'))
