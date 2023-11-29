import la_lib
import sys
import copy

a = "toto"


def main():
    la_liste = [10,20,30,40,50]
    l2 = la_liste[:]
    l3 = la_liste.copy()
    la_liste[0] = 1000
    print("la_liste",la_liste)
    print("l2",l2)
    print("l3",l3)
    # print(la_liste[1:3])
    # print(la_liste[-1])
    print(50*"-")
    la_liste = [
        [10,20],
        [30,40],
        [50,60]
    ]
    print(la_liste)
    print(la_liste[1][1])
    # la_liste2 = la_liste[:]
    la_liste2 = copy.deepcopy(la_liste)
    la_liste[1][1] = 1000
    print(la_liste)
    print(la_liste2)

def main01():
    # global a
    print("getrefcount",sys.getrefcount(2))
    a=2
    print("getrefcount",sys.getrefcount(2))
    c=2
    print("getrefcount",sys.getrefcount(2))

    print("Hello")
    la_lib.hello('Fred')
    print(a)
    # if True:
    #     a=2

    print("a : "+str(a))
    print("a : "*a)

    print(50*'-')
    
    a =2
    print(a)
    print(hex(id(a)))
    a=3
    b=3
    print(a)
    print(hex(id(a)))
    print(b)
    print(hex(id(b)))




if __name__ == "__main__":
    # print("avant",a)
    main()  
    # print("après",a)

