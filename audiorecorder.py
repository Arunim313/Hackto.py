import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
freq=44100
#recording freq
duration=10
#recording duration
recording=sd.rec(int(duration*freq),samplerate=freq,channels=2)

sd.wait()
write("recording0.wav",freq,recording)
wv.write("recording1.wav",freq,sampwidth=2)