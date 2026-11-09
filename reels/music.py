# Generates a soft royalty-free background track: python3 music.py <seconds> <out.wav> [seed]
import numpy as np, wave, sys
D=float(sys.argv[1]); outp=sys.argv[2]; seed=int(sys.argv[3]) if len(sys.argv)>3 else 1
sr=48000; n=int(sr*D); t=np.arange(n)/sr; out=np.zeros(n); rng=np.random.default_rng(seed)
note=lambda m:440*2**((m-69)/12)
progs=[[[57,60,64],[53,57,60],[48,52,55],[55,59,62]],[[50,53,57],[55,59,62],[48,52,55],[57,60,64]],[[52,55,59],[48,52,55],[55,59,62],[50,54,57]]]
chords=progs[seed%len(progs)]; seg=D/8
for k in range(8):
    a=int(k*seg*sr); b=min(n,int((k+1)*seg*sr)); tt=np.arange(b-a)/sr
    env=np.minimum(1,tt/0.6)*np.minimum(1,(seg-tt)/0.6)
    for m in chords[k%4]:
        f=note(m); out[a:b]+=0.05*env*(np.sin(2*np.pi*f*tt)+0.3*np.sin(2*np.pi*2*f*tt))
    out[a:b]+=0.07*env*np.sin(2*np.pi*note(chords[k%4][0]-12)*tt)
beat=60/100
for bt in np.arange(0,D,beat):
    a=int(bt*sr); tt=np.arange(min(int(0.25*sr),n-a))/sr
    out[a:a+len(tt)]+=0.35*np.exp(-tt*18)*np.sin(2*np.pi*(55+90*np.exp(-tt*30))*tt)
for bt in np.arange(beat/2,D,beat):
    a=int(bt*sr); tt=np.arange(min(int(0.05*sr),n-a))/sr
    out[a:a+len(tt)]+=0.04*np.exp(-tt*90)*rng.standard_normal(len(tt))
whoosh=[float(x) for x in sys.argv[4].split(',')] if len(sys.argv)>4 else []
for w in whoosh:
    a=int((w-0.5)*sr); L=int(0.7*sr)
    if a<0 or a+L>n: continue
    tt=np.arange(L)/sr; nz=np.convolve(rng.standard_normal(L),np.ones(8)/8,'same')
    out[a:a+L]+=0.12*np.sin(np.pi*tt/0.7)**2*nz
out*=np.minimum(1,np.minimum(t/0.5,(D-t)/1.5)); out/=np.max(np.abs(out))*1.25
pcm=(out*32767).astype(np.int16); w=wave.open(outp,'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes(np.stack([pcm,pcm],1).tobytes()); w.close()
