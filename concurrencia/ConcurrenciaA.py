import requests
import time
import psycopg2
import threading
import concurrent.futures
from pytube import YouTube

try:
    conexion = psycopg2.connect(database='testdb', user='postgres', password='bebesitomil1')
    cursor1=conexion.cursor()
    cursor1.execute('select version()')
    version=cursor1.fetchone()
except Exception as err:
    print('Error al conecta a la base de datos')


def service(url):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_service,url)

def get_service(url):
    r = requests.get(url)
    if r.status_code== 200:
        data_list=r.json()
        for data in data_list:
            write_db(data["title"])
    else:
        pass


def connect_db():
    pass

def close_conexion():
    conexion.close()

def write_db(data):
    try:
        cursor1.execute("insert into photos(info) values ('"+data+"')")
    except Exception as err:
        print('Error en la inserción: '+ err)
    else:
        conexion.commit()

#Descargar videos con threads
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

def iterar_api():
    print('Hilo para Api iniciada')
    for x in range (0,50):
        print ('Thread API: Dato obtenido de la api',get_api())
    print('Hilo para Api cerrada')

def api_threads():
    th_api = threading.Thread(target=iterar_api)
    th_api.start()

def get_api():
    response= requests.get('https://randomuser.me/api/')
    if response.status_code==200:
        #print(f())
        result = response.json().get('results')
        name=  result[0].get('name').get('first')
        return name
    else: 
        return 'Dato no obtenido'



if __name__ == "__main__":
    init_time = time.time()
    url_site = ["https://jsonplaceholder.typicode.com/photos"]
    service(url_site)
    descargar_videos()
    api_threads()
    end_time = time.time() - init_time
    print(end_time)
    