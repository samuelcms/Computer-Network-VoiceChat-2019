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

p = pyaudio.PyAudio()       # Configura o sistema de "portaudio".

stream = p.open(format=p.get_format_from_width(WIDTH), channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

# Inicializando sockets.

HOST = ''                 
PORT = 29000              
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skt.bind((HOST, PORT))
skt.listen(1)

# Socket de controle.

CTRL_PORT = 30000
ctrl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ctrl.bind((HOST, CTRL_PORT))
ctrl.listen(1)

# Threading.

def conexao(conn, addr, ctrl, addr2):  
    #os.system('clear')
    print ('Conexão vinda de:', addr)
    data = conn.recv(CHUNK) # Dados

    flag = '1' #Indica o estado da conexão.

    # O áudio é reproduzido enquanto houverem dados a serem recebidos, e o cliente estiver conectado.
    while data != '': #and flag == '1':
        
        stream.write(data)
        data = conn.recv(CHUNK)
        frames.append(data)
        
        #Apresentando problema
        #########################################################
        # Recebimento de dados de controle de estado da conexão.
        #aux = ctrl.recv(1)
        #flag = aux.decode('utf-8')

    # Fechamento stream.
    stream.stop_stream()
    stream.close()
    p.terminate()
    print('Conexão encerrada.')

def main():
    while True:
        conn, addr = skt.accept()
        controle, addr2 = ctrl.accept()
        threading.Thread(target=conexao, args=(conn, addr, controle, addr2)).start()

    
# Fechando a via conexão socket..
    
    conn.close()
    skt.close()
    controle.close()
    ctrl.close()

if __name__ == '__main__':
    main()
