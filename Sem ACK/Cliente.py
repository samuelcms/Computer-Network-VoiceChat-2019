# Client.py

import threading
import pyaudio
import socket
import time
import wave
import os

# Inicializando os parâmetros da biblioteca pyaudio.

CHUNK = 2048                # Número de quadros no buffer.
FORMAT = pyaudio.paInt16    # Formato das amostras de áudio.
CHANNELS = 1                # Cada quadro tem 1 amostra ("CHANNELS = 1)
RATE = 52250                # Número de amostras coletadas por segundo.

# Inicializando sockets.

Servidor = '127.0.0.1'
PortaServidor = 29000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((Servidor, PortaServidor))

voz = pyaudio.PyAudio()     # Configura o sistema de "portaudio".
stream = voz.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

print("\n\tChamada em execução...\n")

def start():    
    
    opcao = 1 
    print("\tPara encerrar, digite 0: ")
    
    chamada = Thread()
    chamada.start()     # Iniciando a thread.

    while opcao != 0:
        opcao = int(input())
    
    chamada.stop()      # Parando a thread.
    #os.system('clear')
    print("\n\n\tChamada finalizada!")
    
class Thread(threading.Thread):

    def __init__(self):
        super(Thread, self).__init__()
        self.kill = threading.Event()

    def run(self): 
        while not self.kill.is_set():       # Envia audio enquanto a (chamada não for finalizada) thread não estiver 'morta'. 
            data  = stream.read(CHUNK)
            clientSocket.sendall(data)
        
        stream.stop_stream()
        stream.close()
        voz.terminate()

        #clientSocket.sendall('')     # Tentativa de finalização da chamada usando o mesmo socket.

        clientSocket.close()
        print("Conexão via socket encerrada.")
            
    def stop(self):
        self.kill.set()     # Encerra a thread.

if __name__ == "__main__":
    start()

