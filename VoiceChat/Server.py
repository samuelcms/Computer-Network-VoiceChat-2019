# Server.py

from datetime import datetime
import threading
import pyaudio
import socket
import time
import os


# Inicializando os parâmetros da biblioteca pyaudio.

CHUNK = 2048 * 5            # Número de quadros no buffer.
FORMAT = pyaudio.paInt16    # Formato das amostras de áudio.
CHANNELS = 1                # Cada quadro tem 1 amostra ("CHANNELS = 1)".
RATE = 52000                # Número de amostras coletadas por segundo.
WIDTH = 2                   # Largura das amostras de áudio (em bytes).

# Criando conexão de dados.

HOST = ''                 
PORT = 20000              
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skt.bind((HOST, PORT))
skt.listen(0)

# Criando conexão de controle.

CTRL_PORT = 40000
ctrl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ctrl.bind((HOST, CTRL_PORT))
ctrl.listen(0)

def conexao(conn, addr, ctrl, addr2):  
    
    voz = pyaudio.PyAudio()         # Configura o sistema de "portaudio".
    stream = voz.open(format=voz.get_format_from_width(WIDTH), channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

    os.system('clear')
    print ('Conexão vinda de:', addr)
    data = conn.recv(CHUNK)         # Dados

    status = '1'                    # Indica o estado da conexão.

    # Enquanto o cliente estiver conectado e os dados forem diferentes de NULL, a mensagem de voz será reproduzida.
    
    while data != '' and status == '1':   
        stream.write(data)
        data = conn.recv(CHUNK)    
        aux = ctrl.recv(1)          # Recebimento do status de conexão.
        status = aux.decode('utf-8')

    end = datetime.now()            # Data e hora de finalização da chamada.

    # Fechamento da stream.

    stream.stop_stream()
    stream.close()
    voz.terminate()     
    
    # Data e hora de finalização da chamada.

    end = str(datetime.now())                        
    aux = end.split(' ')
    data = aux[0]
    hora = aux[1]
    data = data.split('-')
    hora = hora.split('.')
    end = "{}/{}/{} | {}".format(data[2],data[1],data[0],hora[0])
    os.system('clear')
    print(f"Chamada encerrada em: {end}\n\n")

    
def main():
    while True:
        conn, addr = skt.accept()
        controle, addr2 = ctrl.accept()
        threading.Thread(target=conexao, args=(conn, addr, controle, addr2)).start()

    # Fechando sockets.
    
    conn.close()
    skt.close()
    controle.close()
    ctrl.close()
    
if __name__ == '__main__':
    main()
