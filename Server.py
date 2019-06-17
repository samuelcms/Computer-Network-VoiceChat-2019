# Server.py

import socket
import pyaudio
import wave
import time

# Inicializando os parâmetros da biblioteca pyaudio.

CHUNK = 1024 # Número de quadros no buffer.
FORMAT = pyaudio.paInt16
CHANNELS = 1 # Cada quadro tem 1 amostra ("CHANNELS = 1)".
RATE = 44100 # Número de amostras coletadas por segundo.
WIDTH = 2
frames = []

#RECORD_SECONDS = 40
#WAVE_OUTPUT_FILENAME = "server_output.wav"
#wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb') Colocar antes de [wf.setnchannels(CHANNELS)] se necessário for.

p = pyaudio.PyAudio() #Função para calcular o tamanho de cada amostra.

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)


HOST = ''                 #Symbolic name meaning all available interfaces
PORT = 50007              #Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print ('Conexão vinda de: ', addr)
data = conn.recv(1024)# Dados

while data != '': #Enquanto os dados forem diferentes de NULL.
    stream.write(data)
    data = conn.recv(1024)
    frames.append(data)

wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

stream.stop_stream()
stream.close()
p.terminate()
conn.close()
s.close() # Fechando a conexão socket.