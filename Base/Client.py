# Client.py

import socket
import pyaudio
import wave
import os

# Inicializando os parâmetros da biblioteca pyaudio.

CHUNK = 1024    # Número de quadros no buffer.
FORMAT = pyaudio.paInt16
CHANNELS = 1    # Cada quadro tem 1 amostra ("CHANNELS = 1)
RATE = 52250    # Número de amostras coletadas por segundo.

# Inicializando sockets.
Servidor = '127.0.0.1'
PortaServidor = 22000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((Servidor, PortaServidor))

voz = pyaudio.PyAudio()

stream = voz.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

os.system('clear')
print("\n\t*Gravando*n\n")
print("Para interromper a ligação, pressione Ctrl + C.")

# Envia audio enquanto a chamada não for finalizada.
while  1:
    data  = stream.read(CHUNK)
    clientSocket.sendall(data)

stream.stop_stream()
stream.close()
voz.terminate()
clientSocket.close()

print("Conexão fechada.")
