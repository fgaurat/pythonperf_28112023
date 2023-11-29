from Rectangle import Rectangle 
from DataRectangle import DataRectangle 

def main():
    r = Rectangle(5,2) # __init__(self,5,2)

    # print(r.get_surface()) # 10
    print(r.surface) # 10
    print(r.longueur) # 5
    r.longueur = -6
    print(r.longueur) # 6
    r2 = DataRectangle(5,6)
    print(r2.longueur)
    print(r2.surface)

if __name__=='__main__':
    main()
