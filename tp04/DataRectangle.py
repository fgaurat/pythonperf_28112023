from dataclasses import dataclass

@dataclass
class DataRectangle:
    longueur:int=0
    largeur:int=0

    @property
    def surface(self):
        return self.longueur*self.largeur