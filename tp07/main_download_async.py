

import asyncio
import time
from bs4 import BeautifulSoup
from pprint import pprint
import httpx

async def download(url_log):
    async with httpx.AsyncClient() as client:
        response = await client.get(url_log)
        file_name = url_log.split('/')[-1]
        with open(file_name,'w') as f:
            f.write(response.text)

async def main():
    start = time.perf_counter()
    url="https://logs.eolem.com/"
    response = httpx.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = soup.find_all('a')
    all_logs = [url+a["href"] for a in all_a if ".log" in a["href"]]
    
        
    tasks = [download(url_log) for url_log in all_logs]
    await asyncio.gather(*tasks)
    
    end = time.perf_counter()
    print(end-start)
    # 0.5712224000017159

if __name__=='__main__':
    asyncio.run(main())









