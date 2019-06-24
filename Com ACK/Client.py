# Client.py

from datetime import datetime
import threading
import pyaudio
import socket
import os

opcao = 1

def getchar():
    global opcao
    opcao = str(input())
    
getch = threading.Thread(target=getchar)
getch.start()

# Inicializando os parâmetros da biblioteca pyaudio.

CHUNK = 2048                # Número de quadros no buffer.
FORMAT = pyaudio.paInt16    # Formato das amostras de áudio.
CHANNELS = 1                # Cada quadro tem 1 amostra ("CHANNELS = 1)
RATE = 52250                # Número de amostras coletadas por segundo.

# Inicializando o socket de dados.

SERVER = 'localhost'        
PORT = 16000                
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skt.connect((SERVER, PORT))

# Inicializando o socket de controle.

CTRL_PORT = 61000   
ctrl_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ctrl_skt.connect((SERVER, CTRL_PORT))

# Configura o sistema de "portaudio".
voz = pyaudio.PyAudio()
# Inicialização da stream de áudio.
stream = voz.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

#os.system('clear')
print("\n\tChamada em execução...\n")
print("Para interromper a chamada, pressione 0 e tecle ENTER.")
frames = []

flag = '1' # Indica o estado da conexão.

# Envia audio enquanto a chamada não for finalizada.
while  opcao != '0':
    data  = stream.read(CHUNK)
    frames.append(data)
    skt.sendall(data)
    ctrl_skt.sendall(flag.encode('utf-8')) # Envia dados de controle.

stream.stop_stream()
stream.close()
voz.terminate()
skt.close()

# Dado de encerramento da conexão.
flag = '0'
ctrl_skt.sendall(flag.encode('utf-8'))
ctrl_skt.close()

end = datetime.now() # Hora de finalização da chamada.
print("Chamada encerrada em {}".format(end))
