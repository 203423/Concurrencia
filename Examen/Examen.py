import threading as thread
import time


cliente=[False,False,False,False,False,False,False,False]
clientes=[False]
palilloIzq=thread.Lock()
palilloDer = thread.Lock()
def crito(id):
    cliente[id-1]=False
    print("cliente #" +str(id)+ " => Comiendo" )
    time.sleep(1)

def crito2(id):
    print("cliente #" +str(id)+ " => Terminó de comer" )
    cliente[id-1]=True

def validar():
    if cliente[::]== [True,True,True,True,True,True,True,True]:
        clientes[0]=True

class Hilo(thread.Thread):
     def __init__(self, id):
        thread.Thread.__init__(self)
        self.id=id

     def run(self):
        while clientes[0]==False:
            if palilloIzq.locked() ==False and palilloDer.locked()==False and cliente[self.id-1]==False:
                palilloDer.acquire()
                palilloIzq.acquire() #Inicializa semáforo , lo adquiere
                crito(self.id)
                palilloIzq.release()
                palilloDer.release() #Libera un semáforo e incrementa la varibale   
                crito2(self.id)
                validar()
                
            
            
            
        
        

hilos = [Hilo(1), Hilo(2), Hilo(3), Hilo(4), Hilo(5), Hilo(6), Hilo(7), Hilo(8)]
for h in hilos:
    h.start()