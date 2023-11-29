from abc import ABCMeta,abstractmethod


class ICalcGeoABC(metaclass=ABCMeta):
    
    @property
    @abstractmethod
    def surface(self):
        pass