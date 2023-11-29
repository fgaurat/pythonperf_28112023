from Rectangle import Rectangle 
from DataRectangle import DataRectangle 

def main():
    r = Rectangle(5,2) # __init__(self,5,2)

    # print(r.get_surface()) # 10
    print(r.surface) # 10
    print(r.longueur) # 5
    r.longueur = 6
    print(r.longueur) # 6
    # r2 = DataRectangle(5,6)
    # print(r2.longueur)
    # print(r2.surface)

    # print(r)
    s = str(r)
    print(s)
    r = Rectangle()
    r1 = Rectangle(5,2)
    if r==r1:
        print("ok")
    else:
        print("ko")
    
    # Rectangle.__cpt = 1000
    print(Rectangle.get_cpt())
    print(r.get_cpt())

    print(50*'-')
    r2 = Rectangle.fromStr('5;6')
    d = {"longueur":5,"largeur":2}
    r3 = Rectangle.fromDict(d)
    print(r3)
    r4 = Rectangle(**d)
if __name__=='__main__':
    main()
