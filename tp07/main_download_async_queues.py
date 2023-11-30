import httpx
from bs4 import BeautifulSoup
import time
import asyncio

async def old_download(url_log):
    log = url_log.split('/')[-1]
    async with httpx.AsyncClient() as client:
        r = await client.get(url_log)
        log_content = r.text
        with open(log,"w") as f:
            f.write(log_content)

async def old_main():
    start = time.perf_counter()
    url = "https://logs.eolem.com/"
    r = httpx.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    all_href = [link['href'] for link in soup.find_all('a') if link['href'].endswith('.log')]


    # tasks = [download(f"{url}{log}") for log in all_href]
    tasks=[]
    for log in all_href:
        url_log = f"{url}{log}"
        tasks.append(download(url_log))
    
    await asyncio.gather(*tasks)

    end = time.perf_counter()

    print(end-start)


async def download(download_queue,save_queue):
    while True:
        url_log = await download_queue.get()
        log = url_log.split('/')[-1]
        async with httpx.AsyncClient() as client:
            r = await client.get(url_log)
            log_content = r.text
            d = {
                "data":log_content,
                "log_file":log
            }
            save_queue.put_nowait(d)
        download_queue.task_done()


async def save(save_queue):
    while True:
        d = await save_queue.get()
        log = d['log_file']
        log_content = d['data']
        with open(log,"w") as f:
            f.write(log_content)
        save_queue.task_done()

async def main():
    start = time.perf_counter()
    download_queue = asyncio.Queue()
    save_queue = asyncio.Queue()
    nb_download_workers = 10
    nb_save_workers = 3
    
    url = "https://logs.eolem.com/"
    r = httpx.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_href = [url+link['href'] for link in soup.find_all('a') if link['href'].endswith('.log')]
    
    # create workers
    tasks=[]
    for i in range(nb_download_workers):
        task = asyncio.create_task(download(download_queue,save_queue))
        tasks.append(task)
    
    for i in range(nb_save_workers):
        task = asyncio.create_task(save(save_queue))
        tasks.append(task)

    for url in all_href:
        download_queue.put_nowait(url)
    
    await download_queue.join()
    await save_queue.join()

    [t.cancel() for t in tasks]


    end = time.perf_counter()

    print(end-start)

if __name__=='__main__':
    asyncio.run(main())

