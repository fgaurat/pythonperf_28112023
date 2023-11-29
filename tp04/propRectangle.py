

class Rectangle:

    def __init__(self,longueur,largeur):

        if longueur<=0 or largeur<=0:
            raise Exception("bad init values")
        
        self.__longueur = longueur
        self.__largeur = largeur

    def get_surface(self):
        return self.__longueur*self.__largeur

    def get_longueur(self):
        return self.__longueur    

    def set_longueur(self,l):
        if l <=0:
            raise Exception('bad longueur !')
        self.__longueur = l    

    def get_largeur(self):
        return self.__largeur    

    def set_largeur(self,l):
        if l <=0:
            raise Exception('bad largeur !')
        self.__largeur = l    

    longueur = property(get_longueur,set_longueur,doc="property longueur")
    largeur = property(get_largeur,set_largeur,doc="property largeur")
    surface = property(get_surface,doc="property surface")