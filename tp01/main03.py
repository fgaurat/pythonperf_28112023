def mult2(l):
    r = []
    for i in l:
        r.append(i*2)

    return r

def map_mult2(i):
    return i*2

def main():
    l = [1,2,3,4]
    v = mult2(l) # [2,4,6,8]
    print(v)

    # v = list(map(map_mult2,l)) 
    
    v = list(map(lambda a:a*2 ,l)) 
    
    print(v)

    r = [i*2 for i in l if i*2>2]
    print(r)
    r = [12 if i*2>2 else i*2 for i in l] # i*2>2 ? 12:i*2 
    print(r)

if __name__=='__main__':
    main()
