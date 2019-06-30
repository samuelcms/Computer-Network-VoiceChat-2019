# Client.py

from datetime import datetime
import threading
import pyaudio
import socket
import os

opcao = '1'

def getchar():
    global opcao
    opcao = str(input())
    while opcao != '0':
        print("Opção inválida, por favor pressione 0 e tecle ENTER.")
        opcao = str(input())
    
getch = threading.Thread(target=getchar)
getch.start()

# Inicializando os parâmetros da biblioteca pyaudio.

CHUNK = 2048                # Número de quadros no buffer.
FORMAT = pyaudio.paInt16    # Formato das amostras de áudio.
CHANNELS = 1                # Cada quadro tem 1 amostra ("CHANNELS = 1)
RATE = 52250                # Número de amostras coletadas por segundo.

# Criando conexão de dados.

SERVER = 'localhost'        
PORT = 20000                
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skt.connect((SERVER, PORT))

# Criando conexão de controle.

CTRL_PORT = 40000   
ctrl_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ctrl_skt.connect((SERVER, CTRL_PORT))

# Configura o sistema de "portaudio".
voz = pyaudio.PyAudio()
# Inicialização da stream de áudio.
stream = voz.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

os.system('clear')
print('\t\t -------------------------')
print("\t\t|   Chamada em execução   |")   
print('\t\t -------------------------\n')

print("\n* Para interromper a chamada, pressione 0 e tecle ENTER.")

status = '1'                   # Indica o estado da conexão (0 = OFF | 1 = ON).

# Envia os dados enquanto a chamada não for finalizada.
while  opcao != '0':
    data  = stream.read(CHUNK)
    skt.sendall(data)
    ctrl_skt.sendall(status.encode('utf-8'))     # Envia dados de controle.

# Fechamento da stream.

stream.stop_stream()
stream.close()
voz.terminate()
skt.close()

status = '0'                                     # Confirmação do encerramento da conexão.
ctrl_skt.sendall(status.encode('utf-8'))
ctrl_skt.close()

# Data e hora de finalização da chamada.

end = str(datetime.now())                        
aux = end.split(' ')
data = aux[0].split('-')
hora = aux[1].split('.')
#end = "{}/{}/{} | {}".format(data[2],data[1],data[0],hora[0])
os.system('clear')
print(f"\n\n\tChamada encerrada em: {data[2]}/{data[1]}/{data[0]} | {hora[0]}\n\n")
