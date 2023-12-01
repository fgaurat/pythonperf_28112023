import timeit

def mult2_append():
    l=[10,20,30]
    r =[]
    for i in l:
        r.append(i*2)
    return r


def mult2_map():
    l=[10,20,30]
    return list(map(lambda i:i*2,l))

def mult2_comp():
    l=[10,20,30]
    return [i*2 for i in l]


def mult2item(i):
    return i*2

def main():
    l=[10,20,30]
    l2 = mult2_append()
    print(l2)
    l2 = mult2_map()
    print(l2)
    l2 = mult2_comp()
    print(l2)
    t1 = timeit.timeit("mult2_append()",setup="from __main__ import mult2_append")
    print(t1)
    t2 = timeit.timeit("mult2_map()",setup="from __main__ import mult2_map")
    print(t2)
    t3 = timeit.timeit("mult2_comp()",setup="from __main__ import mult2_comp")
    print(t3)



def main_01():
    l=[10,20,30]
    l2 =mult2_append(l) # [20,40,60]
    print(l2)
    
    r =[]
    for i in l:
        r.append(i*2)
    print(r)
    
    # i = list(map(mult2item,l))
    i = list(map(lambda i:i*2,l))
    print(i)

    l2 = [i*2 for i in l]
    print(l)

if __name__ == '__main__':
    main()
