import threading


the_lock = threading.Lock()

def traitement_long_1():
    with the_lock:
        for i in range(5):
            print("traitement_long_1",i)

def traitement_long_2():
    with the_lock:
        for i in range(5):
            print("traitement_long_2",i)

def main():
    th1 = threading.Thread(target = traitement_long_1)
    th2 = threading.Thread(target = traitement_long_2)
    th1.start()
    th2.start()

    th1.join()
    th2.join()
    
    print("la fin")

if __name__=='__main__':
    main()
