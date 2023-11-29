def add(*l):
    """add function

    Args:
        l (int): integer list

    Returns:
        int: sum of all values
    """
    print(l)
    r = 0
    for i in l:
        r+=i

    return r


# def hello(**kwargs):
# def hello(name,first_name,/): #pos only
def hello(*,name,first_name):  # kw only
    # print("hello",kwargs)
    print("hello",first_name,name)


def main():
  
    l = [1,2,3,4]
    # r = add(l)
    # print(r) # 10
    r = add(1,2,3,4)
    print(r) # 10
    print(l)
    print(*l,sep=";")
    # print(1,2,3,4)

    l = [1,2,3,4]
    a,b,*le_reste = l
    print(a,b,le_reste)


    a,b,*le_reste = [1,2,3,4]
    a,b = 0,1
    print(a,b)

    t = 0,1
    print(t)
    hello("GAURAT","Frédéric")
    # hello("Frédéric","GAURAT")
    hello(name="GAURAT",first_name="Frédéric")
    hello(first_name="Frédéric",name="GAURAT")
    info = {'name': 'GAURAT', 'first_name': 'Frédéric'}
    hello(**info)
    # s = "a:, b:".format(1,2,3,4)
    s = "a:{0}, b:{1}".format(*l)
    # s = "a:{}, b:{}".format(*l)
    print(s)
    s = "Bonjour {name}, {first_name}".format(name="gaurat",first_name="fred")
    print(s)
    s = "Bonjour {name}, {first_name}".format(**info)
    print(s)

if __name__=='__main__':
    main()
