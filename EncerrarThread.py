#A thread vai ser executada enquanto o atributo self.kill não estiver 'set'

import threading
import time

def start():
    
    t1 = Thread()
    t1.start() #Iniciando a thread.
    
    op = 1
    
    while op != 0:
        print("Digite '0' para parar: ")
        op = int(input())
    print("Thread finalizada!")
    
    t1.stop() #Parando a thread.

class Thread(threading.Thread):

    def __init__(self):
        super(Thread, self).__init__()
        self.kill = threading.Event()

    def run(self): 
        # Enquanto a thread não estiver 'morta'
        while not self.kill.is_set():
            print("Thread executando")
            time.sleep(1)

    def stop(self):
        # Mata a thread
        self.kill.set()

if __name__ == "__main__":
    start()

'''
#Tread com Threading

import threading
import time

def loop1():
    
    i = 1
    
    while True:
        print ('Loop 1 rodadndo pela {}a vez em: {}'.format (i, time.ctime()))
        i+= 1

def loop2():
    
    i = 1
    
    while True:
        print ('Loop 2 rodadndo pela {}a vez em: {}'.format (i, time.ctime()))
        i+= 1

def main():
    th1 = threading.Thread(target=loop1, args=())
    th2 = threading.Thread(target=loop2, args=())
    th1.start()
    th2.start()
    
if __name__ == "__main__":
    main()
'''
