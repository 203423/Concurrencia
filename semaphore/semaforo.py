from threading import Thread, Semaphore
from pytube import YouTube
semaforo=Semaphore(1) #Crea la variable semáforo

def crito(id,url):
    print("Hilo =" +str(id) + " => " +url)
    yt=YouTube(url)
    yt.streams.filter(progressive="True", file_extension='mp4').order_by('resolution').desc().first().download()
    print(yt)
    print("video descargado con exito")

class Hilo(Thread):
    def __init__(self,id,url):
        Thread.__init__(self)
        self.id=id
        self.url=url

    def run(self):
        semaforo.acquire() #inicializa semáforo, lo adquiere
        crito(self.id)
        semaforo.release() #

threads_semaphore = [
    Hilo(1,"https://www.youtube.com/watch?v=adX5nuYZUZs"),
    Hilo(2,"https://www.youtube.com/watch?v=fiUfLIYhgsw"),
    Hilo(3,"https://www.youtube.com/watch?v=shR-bJGyF0o"),
    Hilo(4,"https://www.youtube.com/watch?v=Kgfvch7syos"),
    Hilo(5,"https://www.youtube.com/watch?v=Ie6KJ-bTHUY")
    ]
for t in threads_semaphore:
    t.start()
