# Server.py

import socket
import pyaudio
import wave
import time
import os

# Inicializando os parâmetros da biblioteca pyaudio.

CHUNK = 1024 # Número de quadros no buffer.
#FORMAT = pyaudio.paInt16
CHANNELS = 1 # Cada quadro tem 1 amostra ("CHANNELS = 1)".
RATE = 52250 # Número de amostras coletadas por segundo.
WIDTH = 2
frames = []

p = pyaudio.PyAudio() #Função para calcular o tamanho de cada amostra.

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)


HOST = ''                 
PORT = 22000              
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print ('Conexão vinda de: ', addr)
data = conn.recv(CHUNK) #Dados

i=1
while data != '': #Enquanto os dados forem diferentes de NULL.
    data = conn.recv(CHUNK)
    
    silence = 0

    

    stream.write(data)
    frames.append(data)
    i = i+1
    print(i)
    #os.system('clear')

'''
i=1
while data != '': #Enquanto os dados forem diferentes de NULL.
    stream.write(data)
    data = conn.recv(1024)
    frames.append(data)
    i = i+1
    print(i)
    #os.system('clear')
 '''   
 
stream.stop_stream()
stream.close()
p.terminate()
conn.close()
s.close() # Fechando a conexão socket.