import requests
from bs4 import BeautifulSoup
import time

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

    all_href = [link['href'] for link in soup.find_all('a') if link['href'].endswith('.log')]

    for log in all_href:
        url_log = f"{url}{log}"
        download(url_log)
    
    end = time.perf_counter()

    print(end-start)
if __name__=='__main__':
    main()
