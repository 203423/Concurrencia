from threading import Thread, Semaphore
from pytube import YouTube
semaforo=Semaphore(1) #Crea la variable semáforo



def descargar_videos():
    videos_url= ["https://www.youtube.com/watch?v=adX5nuYZUZs","https://www.youtube.com/watch?v=fiUfLIYhgsw","https://www.youtube.com/watch?v=shR-bJGyF0o","https://www.youtube.com/watch?v=Kgfvch7syos","https://www.youtube.com/watch?v=Ie6KJ-bTHUY"]
    for link in videos_url:
        th2=threading.Thread(target=videos,args={link})
        th2.start()

def videos(y):  
    yt1= YouTube(y)
    resoluciones1=yt1.streams.filter(file_extension='mp4').order_by("resolution").desc()
    resolucion1=resoluciones1.first()
    print("Descargando vídeo "+ y)
    video=resolucion1.download(output_path="C:\\Users\\trasf\\Documents\\Concurrente")
    print("descarga "+ y +" terminada")



def crito(id):
    global x;
    x = x + id
    print("Hilo =" +str(id) + " => " +str(x))
    x=1

class Hilo(Thread):
    def __init__(self,id):
        Thread.__init__(self)
        self.id=id

    def run(self):
        semaforo.acquire() #inicializa semáforo, lo adquiere
        crito(self.id)
        semaforo.release() #

threads_semaphore = [Hilo(1),Hilo(2),Hilo(3)]
x=1;
for t in threads_semaphore:
    t.start()
