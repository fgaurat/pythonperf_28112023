import requests
from bs4 import BeautifulSoup
import time
import concurrent.futures

def download(url_log):
    print(url_log)
    log = url_log.split('/')[-1]
    r = requests.get(url_log)
    log_content = r.text
    with open(log,"w") as f:
        f.write(log_content)


def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    all_href = [f"{url}{link['href']}" for link in soup.find_all('a') if link['href'].endswith('.log')]

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download,all_href)

    
    end = time.perf_counter()

    print(end-start)
if __name__=='__main__':
    main()
