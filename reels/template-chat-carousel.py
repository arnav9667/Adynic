import asyncio, os
from brand import render
F='node_modules/@fontsource/'
EXTRA=f"""
@font-face{{font-family:Anton;src:url({F}anton/files/anton-latin-400-normal.woff2)}}
.p{{width:1080px;height:1350px;position:relative;overflow:hidden;background:#FFD23F;font-family:Inter,sans-serif;color:#1A1423}}
.p .noise{{position:absolute;inset:0;background:radial-gradient(circle at 20% 15%,rgba(255,255,255,.55),transparent 40%),radial-gradient(circle at 85% 90%,rgba(230,57,70,.25),transparent 45%)}}
.top{{position:absolute;top:56px;left:70px;right:70px;display:flex;justify-content:space-between;align-items:center}}
.cnt{{background:#1A1423;color:#FFD23F;font-weight:800;font-size:24px;padding:10px 20px;border-radius:999px}}
.poster{{font-family:Anton,sans-serif;text-transform:uppercase;line-height:.92;letter-spacing:1px}}
.tape{{display:inline-block;background:#1A1423;color:#FFD23F;padding:6px 22px 2px;transform:rotate(-2deg)}}
.red{{color:#E63946}}
.phone{{position:absolute;left:150px;right:150px;top:250px;bottom:150px;background:#F4EFE6;border:10px solid #1A1423;border-radius:56px;overflow:hidden;box-shadow:18px 18px 0 #1A1423}}
.bar{{background:#1A1423;color:#fff;display:flex;align-items:center;gap:18px;padding:26px 30px}}
.av{{width:64px;height:64px;border-radius:50%;background:#FFD23F;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:28px;color:#1A1423}}
.nm{{font-weight:800;font-size:28px}} .st{{font-size:20px;color:#B9B4C2}}
.msgs{{padding:30px 26px;display:flex;flex-direction:column;gap:26px}}
.m{{max-width:78%;padding:20px 24px 14px;border-radius:26px;font-size:35px;line-height:1.3;position:relative}}
.in{{background:#fff;align-self:flex-start;border-top-left-radius:6px}}
.out{{background:#1A1423;color:#fff;align-self:flex-end;border-top-right-radius:6px}}
.out b{{color:#FFD23F}}
.t{{display:block;text-align:right;font-size:17px;opacity:.55;margin-top:6px}}
.cap{{position:absolute;left:70px;right:70px;bottom:52px;display:flex;justify-content:space-between;align-items:center;font-weight:800;font-size:26px}}
.sw{{background:#E63946;color:#fff;padding:14px 28px;border-radius:999px;font-size:24px}}
.stk{{position:absolute;font-family:Anton;font-size:46px;color:#E63946;transform:rotate(-8deg)}}
"""
def frame(n,T,inner,last=False):
    sw='Swipe &#8594;' if not last else 'Save &amp; Share'
    return f'''<style>{EXTRA}</style><div class="p"><div class="noise"></div>
<div class="top"><img src="adynic-logo.png" style="height:54px"><span class="cnt">{n}/{T}</span></div>
{inner}
<div class="cap"><span>adynic.com</span><span class="sw">{sw}</span></div></div>'''
def chat(name,status,msgs,head):
    ms=''.join(f'<div class="m {k}">{txt}<span class="t">{tm}{" &#10003;&#10003;" if k=="out" else ""}</span></div>' for k,txt,tm in msgs)
    return f'''<div style="position:absolute;top:140px;left:70px;right:70px" class="poster"><span style="font-size:76px">{head}</span></div>
<div class="phone"><div class="bar"><div class="av">{name[0]}</div><div><div class="nm">{name}</div><div class="st">{status}</div></div></div><div class="msgs">{ms}</div></div>'''
T=5
slides=[
frame(1,T,'''<div style="position:absolute;top:250px;left:70px;right:70px" class="poster">
<div style="font-size:150px">Har business</div><div style="font-size:150px">owner ka</div>
<div style="font-size:170px;margin-top:10px"><span class="tape">yahi rona</span></div><div style="font-size:150px;margin-top:14px" class="red">hai</div></div>
<div style="position:absolute;left:70px;right:70px;top:1000px;font-size:40px;font-weight:600;line-height:1.35">Ye baatein hum roz sunte hain<br>Swipe karo, shayad aapki bhi kahani ho</div>'''),
frame(2,T,chat('Sharma ji (Client)','online',[('in','Bhai 30 hazaar ke ads chala diye, ek bhi sale nahi aayi','10:02'),('out','Ads kahan se chalaye the?','10:03'),('in','Post pe Boost button dabaya tha','10:03'),('out','Wahi toh problem hai. <b>Ads Manager</b> se Sales campaign chalao, Pixel ke saath','10:04')],'Dukh no. 1: <span class="red">Boost button</span>')),
frame(3,T,chat('Gupta ji (Client)','typing...',[('in','Followers 10K hain, phir bhi koi kharidta nahi','4:15'),('out','Followers kahan se aaye the?','4:16'),('in','Woh... ek giveaway kiya tha','4:16'),('out','Free cheez ke liye aaye log <b>customer nahi</b> hote. Sahi audience pe content banao','4:17')],'Dukh no. 2: <span class="red">Fake followers</span>')),
frame(4,T,chat('Verma ji (Client)','online',[('in','Website pe log aate hain, cart mein daalte hain, phir gayab','9:40'),('out','Checkout mein kitne step hain?','9:41'),('in','Shayad 5-6... aur COD bhi nahi hai','9:41'),('out','Bas yahi. <b>1-page checkout</b> aur COD lagao, abandoned cart pe WhatsApp reminder bhejo','9:42')],'Dukh no. 3: <span class="red">Cart abandon</span>')),
frame(5,T,'''<div style="position:absolute;top:230px;left:70px;right:70px" class="poster">
<div style="font-size:120px">Aapka kaunsa</div><div style="font-size:150px"><span class="tape">dukh hai?</span></div></div>
<div style="position:absolute;top:640px;left:70px;right:70px;font-size:44px;font-weight:600;line-height:1.4">
Comment mein <b class="red">1, 2 ya 3</b> likho<br>Ya seedha DM karo <b class="red">"AUDIT"</b><br>Free mein batayenge problem kahan hai</div>
<div style="position:absolute;top:1000px;left:70px;font-family:Anton;font-size:58px;text-transform:uppercase"><span class="tape">Follow @adynic_</span></div>''',last=True),
]
asyncio.run(render(slides,'genz-chat'))
