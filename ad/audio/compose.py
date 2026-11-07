# Energetic procedural score for the Pagewise ad (no ElevenLabs key). 128.57 bpm = one beat every 14 frames at 30 fps,
# so every cut lands on the beat. Deterministic.
import numpy as np, wave, json
SR=48000; D=23.0; N=int(SR*D); rng=np.random.default_rng(11)
mix=np.zeros((N,2)); beat=14/30; s16=beat/4
def note(m): return 440*2**((m-69)/12)
def add(sig,st,g=1.0,pan=0.0):
    i=int(st*SR)
    if i>=N or i<0: return
    j=min(N,i+len(sig)); x=sig[:j-i]*g; mix[i:j,0]+=x*(1-pan); mix[i:j,1]+=x*(1+pan)
def tt(d): return np.arange(int(d*SR))/SR
def kick(): t=tt(.32); return np.sin(2*np.pi*np.cumsum(48+110*np.exp(-t*38))/SR)*np.exp(-t*9)
def clap():
    t=tt(.22); x=rng.standard_normal(len(t)); x=x-np.convolve(x,np.ones(8)/8,'same'); return x*np.exp(-t*22)
def hat(o=False):
    t=tt(.12 if o else .04); x=rng.standard_normal(len(t)); x=x-np.convolve(x,np.ones(3)/3,'same'); return x*np.exp(-t*(30 if o else 120))
def saw(f,d,h=10):
    t=tt(d); return sum(np.sin(2*np.pi*f*k*t)/k for k in range(1,h+1))
chords=[[57,60,64],[53,57,60],[48,52,55],[55,59,62]]   # Am F C G
roots=[45,41,36,43]
silent=lambda t: 16.95<t<17.27
nb=int(D/beat)
for b in range(nb+1):
    t=b*beat; bar=(b//4)%4
    if silent(t) or t>D-0.05: continue
    end_section = t>17.27+beat*8          # CTA tail: thinner after 2 bars
    add(kick(),t,0.55 if not end_section else 0.35)
    if b%2==1 and not end_section: add(clap(),t,0.22,pan=0.05)
    for k in range(4):
        th=t+k*s16
        if silent(th): continue
        add(hat(k==2),th,0.07 if k!=2 else 0.09,pan=0.3)
    # bass on 8ths (off-beat pump)
    for k in (0,2):
        th=t+k*s16
        if silent(th): continue
        f=note(roots[bar]); d=s16*1.8; x=saw(f,d,6)*np.exp(-tt(d)*6)
        add(np.tanh(x*1.5),th+ (s16 if k==0 else 0),0.10)
    # chord stab on beat 1 and the "and" of 2
    if b%4 in (0,) or (b%4==1):
        st=t if b%4==0 else t+beat/2
        if not silent(st):
            d=0.28; x=sum(saw(note(m+12),d,5) for m in chords[bar])*np.exp(-tt(d)*9)
            add(x,st,0.035,pan=-0.2)
# hits
def boom(): t=tt(1.2); return np.sin(2*np.pi*np.cumsum(40+90*np.exp(-t*12))/SR)*np.exp(-t*3.2)+0.3*rng.standard_normal(len(t))*np.exp(-t*18)
def chime(ms,d=1.4):
    t=tt(d); return sum(np.sin(2*np.pi*note(m)*t)*np.exp(-t*2.5)+.3*np.sin(2*np.pi*note(m)*2.76*t)*np.exp(-t*6) for m in ms)/len(ms)
def click(): t=tt(.03); return rng.standard_normal(len(t))*np.exp(-t*250)
def whoosh(d=.35): t=tt(d); x=rng.standard_normal(len(t)); x=np.convolve(x,np.ones(20)/20,'same'); return x*np.sin(np.linspace(0,np.pi,len(t)))**2
F=lambda f:f/30
add(boom(),F(2),0.55)
add(chime([84,88,91]),F(64),0.16)
add(boom()*0.6,F(260),0.35); add(chime([81,84,88],1.0),F(266),0.12)
for f in (84,210,322,378,434): add(whoosh(),F(f)-0.12,0.18)
add(boom(),F(518),0.5); add(chime([69,76,81,85]),F(518),0.15)
add(click(),F(588),0.35); add(chime([88,93],0.9),F(590),0.14)
ev=json.load(open('stills/events.json')); evs=ev['events'] if isinstance(ev,dict) else ev
for e in evs:
    if e.get('type')=='type': add(click(),e['t'],0.06,pan=0.1)
for f in range(238,260,3): add(click(),F(f),0.05)
mix=np.tanh(mix*1.4)/1.4
mix*=10**(-15.5/20)/np.sqrt(np.mean(mix**2))
pk=np.max(np.abs(mix)); mix*=min(1,0.75/pk)
fd=int(.3*SR); mix[-fd:]*=np.linspace(1,0,fd)[:,None]
w=wave.open('audio/mix.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix*32767).astype('<i2').tobytes()); w.close()
