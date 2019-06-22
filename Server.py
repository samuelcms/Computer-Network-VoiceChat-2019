# Server.py

import socket
import pyaudio
import wave
import time
import os

# Inicializando os parâmetros da biblioteca pyaudio.

CHUNK = 2048 * 5    # Número de quadros no buffer.
CHANNELS = 1        # Cada quadro tem 1 amostra ("CHANNELS = 1)".
RATE = 52250        # Número de amostras coletadas por segundo.
WIDTH = 2
frames = []

p = pyaudio.PyAudio()   # Configura o sistema de "portaudio".

stream = p.open(format=p.get_format_from_width(WIDTH), channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

# Inicializando sockets.

HOST = '127.0.0.1'                 
PORT = 29000              
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print ('Conexão vinda de: ', addr)

data = conn.recv(CHUNK)     # Dados.

contador = 1    # Conta as interações.

while data != '':       # Enquanto os dados forem diferentes de NULL.
    stream.write(data)
    data = conn.recv(CHUNK)
    frames.append(data)
    #contador = contador + 1
    #print(contador)
    #os.system('clear')
 
stream.stop_stream()
stream.close()
p.terminate()
conn.close()
s.close()           # Fechando a via conexão socket.
