# Client.py

import socket
import pyaudio
import wave

# Inicializando os parâmetros da biblioteca pyaudio.

CHUNK = 1024 # Número de quadros no buffer.
FORMAT = pyaudio.paInt16
CHANNELS = 1 # Número de amostras coletadas por segundo.
RATE = 44100

# RECORD_SECONDS = 40

HOST = '127.0.0.1'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("*Gravando")

frames = []

while 1: #for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):

 data  = stream.read(CHUNK)
 frames.append(data)
 s.sendall(data)


stream.stop_stream()
stream.close()
p.terminate()
s.close()

print("Conexão fechada.")