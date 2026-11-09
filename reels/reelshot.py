import asyncio, sys, subprocess, os
from playwright.async_api import async_playwright
H=os.path.dirname(os.path.abspath(__file__))
async def main(mode):
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg=await b.new_page(viewport={'width':1080,'height':1920})
        await pg.goto('file://'+H+'/reel.html'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
        if mode=='preview':
            for t in (2.4,4.0,6.5,12.0,20.5):
                await pg.evaluate(f'setT({t})')
                await pg.screenshot(path=f'{H}/pv-{t}.jpg',type='jpeg',quality=85)
        else:
            scenes=[(0,3),(3,8),(8,13),(13,18),(18,22)]
            for n,(a,bb) in enumerate(scenes):
                tmp=f'{H}/sc{n}.tmp.mp4'
                ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-framerate','30','-c:v','mjpeg','-i','-','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-r','30',tmp],stdin=subprocess.PIPE)
                for f in range(int((bb-a)*30)):
                    await pg.evaluate(f'setT({a+f/30})')
                    ff.stdin.write(await pg.screenshot(type='jpeg',quality=92))
                ff.stdin.close(); ff.wait()
                if ff.returncode==0: os.replace(tmp,f'{H}/sc{n}.mp4')
                else: sys.exit('ffmpeg failed')
        await b.close()
asyncio.run(main(sys.argv[1]))
