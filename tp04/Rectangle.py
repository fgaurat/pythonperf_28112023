

class Rectangle:

    def __init__(self,longueur,largeur):

        if longueur<=0 or largeur<=0:
            raise Exception("bad init values")
        
        self.__longueur = longueur
        self.__largeur = largeur
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

