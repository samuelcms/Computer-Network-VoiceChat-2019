# Server.py

import threading
import pyaudio
import socket
import wave
import time
import os

# Inicializando os parâmetros da biblioteca pyaudio.

CHUNK = 2048 * 5            # Número de quadros no buffer.
FORMAT = pyaudio.paInt16    # Formato das amostras de áudio.
CHANNELS = 1                # Cada quadro tem 1 amostra ("CHANNELS = 1)".
RATE = 52000                # Número de amostras coletadas por segundo.
WIDTH = 2
frames = []

voz = pyaudio.PyAudio()       # Configura o sistema de "portaudio".
stream = voz.open(format=voz.get_format_from_width(WIDTH), channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

# Inicializando sockets.

HOST = ''                 
PORT = 29000              
socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketServer.bind((HOST, PORT))
socketServer.listen(1)

# Threading.

def conexao(conn, addr):  

    #os.system('clear')
    print ('Conexão vinda de:', addr)
    data = conn.recv(CHUNK) # Dados

    # Reprodução da voz.
    while data != '':
        
        stream.write(data)
        data = conn.recv(CHUNK)
        frames.append(data)
        
    # Fechamento stream.
    stream.stop_stream()
    stream.close()
    voz.terminate()
    
def main():

    while True:
        conn, addr = socketServer.accept()
        threading.Thread(target=conexao, args=(conn, addr)).start()

# Fechando a via conexão socket.
    
    conn.close()
    socketServer.close()
    print('Conexão encerrada.')

if __name__ == '__main__':
    main()
