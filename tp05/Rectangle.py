

class Rectangle:

    __cpt=0

    def __init__(self,longueur=1,largeur=1):
        if longueur<=0 or largeur<=0:
            raise Exception("bad init values")
        
        Rectangle.__cpt+=1

        self.__longueur = longueur
        self.__largeur = largeur

    @classmethod
    def fromStr(cls,value): # value=5;6
        # arr = value.split(';') # ["5","6"]
        longueur,largeur = [int(v) for v in value.split(';')]
        return cls(longueur,largeur)
    
    @classmethod
    def fromDict(cls,value):
        longueur = value['longueur']
        largeur = value['largeur']
        return cls(longueur,largeur)

    @property
    def surface(self):
        return self.__longueur*self.__largeur

    @property
    def longueur(self):
        return self.__longueur    
    
    @longueur.setter
    def longueur(self,l):
        if l <=0:
            raise Exception('bad longueur !')
        self.__longueur = l    

    @property
    def largeur(self):
        return self.__largeur    
    
    @largeur.setter
    def largeur(self,l):
        if l <=0:
            raise Exception('bad largeur !')
        self.__largeur = l    

    def __str__(self) -> str:
        return f"{__class__.__name__} {self.__longueur=}, {self.__largeur=}"

    # r1 == r2
    # r1.__eq__(r2)
    def __eq__(self, __value: object) -> bool:
        return self.largeur == __value.largeur and self.longueur == __value.longueur 

    @staticmethod
    def get_cpt():
        return Rectangle.__cpt


    #destructeur
    def __del__(self):
        print("__del__(self)")
        Rectangle.__cpt-=1
