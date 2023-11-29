from Rectangle import Rectangle 
from Carre import Carre 
from Cercle import Cercle 

def main():
    r = Rectangle(5,2)
    c = Carre(5)
    print(c.surface)
    print(c)
    ce = Cercle(2)
    print("ce.surface",ce.surface)

if __name__=='__main__':
    main()
