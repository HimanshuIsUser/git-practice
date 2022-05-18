import winsound
import sounddevice as noise
from scipy.io.wavfile import write
freq = 44100
duration = 5
recording = noise.rec(int(duration*freq),
                      samplerate=freq, channels=2)
noise.wait()
write("recording2.wav", freq,recording)
filename = 'recording2.wav'
winsound.PlaySound(filename,winsound.SND_FILENAME)