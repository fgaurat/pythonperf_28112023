from collections import deque

def main():
    l = [10,20,30]
    print(l)
    l.append(40)
    print(l)
    v = l.pop()
    print(l)
    print(v)
    l.insert(0,0)
    print(l)
    f = l.pop(0)
    print(l)
    print(f)
    
    d = deque(l)
    print(d) 
    d.appendleft(0)
    print(d) 
if __name__=='__main__':
    main()
