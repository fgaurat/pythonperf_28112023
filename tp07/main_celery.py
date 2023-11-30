from celery import Celery,signature,group,chain

import httpx
from bs4 import BeautifulSoup
import time

def main():
    app = Celery('tasks', broker='pyamqp://guest@localhost//',backend="redis://localhost:6379/0")
    r = app.send_task('celery_task.add',args=(3,2))
    print(r.get())

    url = "https://logs.eolem.com/"
    r = httpx.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    all_href = [url+link['href'] for link in soup.find_all('a') if link['href'].endswith('.log')]


    # download = signature('celery_task.download')
    # r = download.delay(all_href[0])
    # result = r.get()
    # print(result)

    # Tous les téléchargements
    # g = group(signature('celery_task.download', args=[url]) for url in all_href)()
    # results = g.get()
    # toutes les sauvegardes
    # g = group(signature('celery_task.save', args=[result]) for result in results)()
    
    # chainage d'un téléchargement et d'une sauvegarde, le sortie du premier (download )est l'entrée du second (save)
    # download(url) | save
    
    for url in all_href:
        res = chain(
            signature('celery_task.download',args=[url]), 
            signature('celery_task.save')
        )()

    # r = res.get()
    # print(r)



if __name__=='__main__':
    main()
