from celery import Celery
import httpx

app = Celery('tasks', broker='pyamqp://guest@localhost//',backend="redis://localhost:6379/0")

# celery -A celery_task worker --loglevel=INFO -P solo
@app.task
def add(x, y):
    return x + y

@app.task
def download(url):
    response = httpx.get(url)
    d = {
        "data":response.text,
        "file_name":url.split('/')[-1]
    }
    return d
    

@app.task        
def save(d):
    print(d)
    file_content = d['data']
    file_name= d['file_name']
    with open(file_name,'w') as f:
        f.write(file_content)


