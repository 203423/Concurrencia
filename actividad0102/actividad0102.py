import threading
import time
import random

#declaración de elementos
items=8
itemlist=list()
consume=threading.Semaphore(0)
remainding=threading.Semaphore(items)
queue=threading.Semaphore(1)

def show_items():
    print("Items in the warehouse: ", itemlist) if len(itemlist)>0 else print("Warehouse empty")

class Productor(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id=id
    def run(self):
        while True:
            item=random.randint(0,50)
            remainding.acquire()
            queue.acquire()
            show_items()
            print(f"Producto {item} creado por el productor {self.id}")
            itemlist.append(item)
            queue.release()
            consume.release()
            time.sleep(2)

class Consumidor(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id=id
    def run(self):
        while True:
            consume.acquire()
            queue.acquire()
            item=itemlist.pop(random.randint(0,len(itemlist)-1))
            print(f"El item {item} ha sido consumido por el consumidor {self.id}")
            queue.release()
            remainding.release()
            time.sleep(5)

if __name__=='__main__':
    producers=[]
    consumers=[]
    for i in range(5):
        producers.append(Productor(i+1))
    for i in range(5):
        consumers.append(Consumidor(i+1))

    for i in producers:
        i.start()
    for j in consumers:
        j.start()

