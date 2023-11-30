import httpx
from bs4 import BeautifulSoup
import time
import asyncio

async def download(url_log):
    log = url_log.split('/')[-1]
    async with httpx.AsyncClient() as client:
        r = await client.get(url_log)
        log_content = r.text
        with open(log,"w") as f:
            f.write(log_content)


async def main():
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
if __name__=='__main__':
    asyncio.run(main())

