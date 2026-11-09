import asyncio, os
from playwright.async_api import async_playwright
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
F = 'node_modules/@fontsource/'
CSS = f"""
@font-face{{font-family:Cinzel;font-weight:700;src:url({F}cinzel/files/cinzel-latin-700-normal.woff2)}}
@font-face{{font-family:Corm;font-style:italic;font-weight:600;src:url({F}cormorant-garamond/files/cormorant-garamond-latin-600-italic.woff2)}}
@font-face{{font-family:Inter;font-weight:400;src:url({F}inter/files/inter-latin-400-normal.woff2)}}
@font-face{{font-family:Inter;font-weight:600;src:url({F}inter/files/inter-latin-600-normal.woff2)}}
@font-face{{font-family:Inter;font-weight:800;src:url({F}inter/files/inter-latin-800-normal.woff2)}}
*{{box-sizing:border-box}}
body{{margin:0}}
.s{{width:1080px;height:1350px;position:relative;overflow:hidden;background:#160A24;color:#FFF4DE;font-family:Inter,sans-serif;padding:72px 84px;display:flex;flex-direction:column}}
.glow{{position:absolute;width:900px;height:900px;border-radius:50%;right:-380px;top:-380px;background:radial-gradient(circle,rgba(240,123,29,.22),rgba(240,123,29,0) 65%)}}
.ring{{position:absolute;width:620px;height:620px;border-radius:50%;left:-260px;bottom:-260px;border:1.5px solid rgba(242,181,68,.16)}}
.ring2{{position:absolute;width:460px;height:460px;border-radius:50%;left:-180px;bottom:-180px;border:1.5px dashed rgba(242,181,68,.12)}}
.top{{display:flex;justify-content:space-between;align-items:center;position:relative}}
.logo{{height:56px;filter:drop-shadow(0 0 1.5px rgba(255,244,222,.85)) drop-shadow(0 0 14px rgba(255,244,222,.18))}}
.count{{font-size:24px;font-weight:600;letter-spacing:2px;color:#CDBBA0}}
.mid{{flex:1;display:flex;flex-direction:column;justify-content:center;position:relative}}
.bot{{display:flex;justify-content:space-between;align-items:center;position:relative;font-size:24px;font-weight:600;letter-spacing:1px}}
.swipe{{background:#F2B544;color:#160A24;padding:16px 30px;border-radius:999px;font-weight:800;font-size:24px;letter-spacing:1px}}
.num{{font-family:Cinzel,serif;font-weight:700;font-size:200px;line-height:.9;color:#F2B544}}
.tag{{font-size:24px;font-weight:800;letter-spacing:6px;color:#F07B1D;margin:28px 0 18px}}
.h{{font-weight:800;font-size:70px;line-height:1.08;letter-spacing:-1px}}
.line{{width:96px;height:4px;background:#F2B544;margin:44px 0 36px;border-radius:2px}}
.fix{{font-size:34px;line-height:1.45;color:#FFF4DE}}
s.myth{{text-decoration:line-through;text-decoration-color:#F07B1D;text-decoration-thickness:5px;color:#CDBBA0}}
.fix b{{color:#F2B544;font-weight:800}}
.it{{font-family:Corm,serif;font-style:italic;font-weight:600;color:#F2B544}}
"""

def page(inner, n, total, last=False):
    swipe = '<span class="swipe">Swipe &#8594;</span>' if not last else '<span class="swipe">Save &amp; Share</span>'
    return f'''<div class="s"><div class="glow"></div><div class="ring"></div><div class="ring2"></div>
<div class="top"><img class="logo" src="adynic-logo.png"><span class="count">{n}/{total}</span></div>
<div class="mid">{inner}</div>
<div class="bot"><span>adynic.com</span>{swipe}</div></div>'''


async def render(slides, prefix):
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg = await b.new_page(viewport={'width':1080,'height':1350})
        for i,s in enumerate(slides, start=1):
            path = os.path.join(HERE, 'slide.html')
            open(path,'w',encoding='utf-8').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{s}</body></html>')
            await pg.goto('file://'+path); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(300)
            png = os.path.join(HERE, f'{prefix}-{i}.png')
            await pg.screenshot(path=png, clip={'x':0,'y':0,'width':1080,'height':1350})
            Image.open(png).convert('RGB').save(os.path.join(HERE, f'{prefix}-{i}.jpg'), quality=78, optimize=True)
        await b.close()
    ims=[Image.open(os.path.join(HERE,f'{prefix}-{i}.png')).resize((360,450)) for i in range(1,len(slides)+1)]
    sheet=Image.new('RGB',(370*4+10,460*((len(ims)+3)//4)+10),'#444')
    for k,im in enumerate(ims): sheet.paste(im,((k%4)*370+10,(k//4)*460+10))
    sheet.save(os.path.join(HERE,f'{prefix}-sheet.png'))
