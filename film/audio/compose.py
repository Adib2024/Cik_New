# Procedural score for the Pagewise promo (no ElevenLabs key): soft pad + pluck arpeggio, sections on the cuts,
# a dip before the lock badge, three hand-placed hits. Deterministic (fixed seed).
import numpy as np, wave, json
SR=48000; D=15.0; N=int(SR*D); t=np.arange(N)/SR
rng=np.random.default_rng(7)
def note(f): return 440*2**((f-69)/12)
def env(n,a,r):
    e=np.ones(n); a=int(a*SR); r=int(r*SR)
    if a: e[:a]=np.linspace(0,1,a)
    if r: e[-r:]*=np.linspace(1,0,r)
    return e
def tone(freq,dur,harm=(1,.5,.25,.12),det=0.0):
    n=int(dur*SR); tt=np.arange(n)/SR; s=np.zeros(n)
    for k,a in enumerate(harm,1):
        s+=a*np.sin(2*np.pi*freq*k*tt)
        if det: s+=a*np.sin(2*np.pi*freq*k*(1+det)*tt)
    return s
mix=np.zeros((N,2))
def add(sig,start,gain=1.0,pan=0.0):
    i=int(start*SR); j=min(N,i+len(sig)); sig=sig[:j-i]*gain
    mix[i:j,0]+=sig*(1-pan)/1; mix[i:j,1]+=sig*(1+pan)/1
BPM=96; beat=60/BPM; bar=4*beat
chords=[[53,57,60,64],[57,60,64,67],[50,57,62,65],[58,62,65,69],[48,55,60,64]]  # Fmaj7 Am7 Dm Bbmaj7 C
# pad: one chord per bar, slow attack
for b in range(7):
    st=b*bar
    if st>=D: break
    ch=chords[b%4] if st<13.2 else chords[4]
    dur=min(bar+0.6,D-st)
    for m in ch: add(tone(note(m),dur,(1,.35,.12),det=0.003)*env(int(dur*SR),0.9,0.8),st,0.035)
# pluck arpeggio on 8ths from 0.3 s, thinned while the viewer reads and gone in the dip
step=beat/2
for i in range(int(D/step)):
    st=0.3+i*step
    if st>D-0.3: break
    if 8.55<st<9.07: continue                       # silence before the lock badge
    ch=chords[int(st/bar)%4] if st<13.27 else chords[4]
    m=ch[[0,2,1,3,2,1,3,2][i%8]]+12
    n=int(0.5*SR); e=np.exp(-np.arange(n)/SR*7)
    g=0.05 if 2.5<st<7.67 else 0.065
    add(tone(note(m),0.5,(1,.3,.08))*e,st,g,pan=0.25*((i%2)*2-1))
# soft kick from the proof onward (not in the dip, not after the logo)
for i in range(int(D/beat)):
    st=i*beat
    if st<2.5 or 8.4<st<9.07 or st>13.2: continue
    n=int(0.25*SR); tt=np.arange(n)/SR; f=55+70*np.exp(-tt*30)
    add(np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-tt*14),st,0.18)
ev=json.load(open('draft.mp4.events.json'))
evs=ev['events'] if isinstance(ev,dict) else ev
# typing texture: a tiny tick per character event (quiet)
for e in evs:
    if e.get('type')=='type':
        n=int(0.03*SR); add(rng.standard_normal(n)*np.exp(-np.arange(n)/SR*180)*0.5,e['t'],0.05,pan=0.1)
# hits: stamp complete (soft thump), lock badge (chime), whip (air), logo (warm bell chord)
def thump(): n=int(.35*SR); tt=np.arange(n)/SR; return np.sin(2*np.pi*(70+60*np.exp(-tt*25))*tt)*np.exp(-tt*10)
def chime(ms):
    n=int(1.6*SR); tt=np.arange(n)/SR; s=np.zeros(n)
    for m in ms: s+=np.sin(2*np.pi*note(m)*tt)*np.exp(-tt*2.2)+.3*np.sin(2*np.pi*note(m)*2.76*tt)*np.exp(-tt*5)
    return s/len(ms)
def air(dur=.5):
    n=int(dur*SR); x=rng.standard_normal(n); x=np.convolve(x,np.ones(30)/30,'same'); e=np.sin(np.linspace(0,np.pi,n))**2; return x*e
T=lambda f:f/30
add(thump(),T(135),0.35)
add(chime([84,88,91]),T(272),0.16)
add(air(.45),T(335)-0.08,0.22)
add(chime([72,76,79,84]),T(398),0.17)
# master: gentle limiter, then normalise loudness approx -14 LUFS via RMS proxy
mix=np.tanh(mix*1.6)/1.6
rms=np.sqrt(np.mean(mix**2)); mix*= (10**(-17/20))/rms
pk=np.max(np.abs(mix)); 
if pk>0.89: mix*=0.89/pk
fade=int(0.25*SR); mix[-fade:]*=np.linspace(1,0.0,fade)[:,None]
w=wave.open('audio/mix.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((mix*32767).astype('<i2').tobytes()); w.close(); print('ok', pk)
