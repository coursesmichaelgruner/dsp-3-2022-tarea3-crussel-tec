import pyaudio
import numpy as np

DELAY=250

RATE = 44100
CHUNK = int((DELAY/1000)*RATE) #2**5
LEN = 10

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK)
player = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, output=True, frames_per_buffer=CHUNK)


for i in range(int(LEN*RATE/CHUNK)): #go for a LEN seconds
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    player.write(data,CHUNK)


stream.stop_stream()
stream.close()
p.terminate()