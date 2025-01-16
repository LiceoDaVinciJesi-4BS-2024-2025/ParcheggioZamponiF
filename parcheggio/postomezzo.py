#Filippo Zamponi
#4BS
#classe PostoMezzo
from veicolo import *
from auto import *
from autobus import *

class PostoMezzo:
    def __init__(self):
        
        
#-------------------------------------------------------------------------
    def __str__(self):
        return "PostoMezzo:" + str(self.__dict__)
    def __repr__(self):
        return "PostoMezzo:" + str(self.__dict__)
#-------------------------------------------------------------------------    
    @property
    def passeggeriMax(self):
        return self.__passeggeriMax

    @passeggeriMax.setter
    def passeggeriMax(self, value):
        if passeggeriMax != 40:
            raise ValueError("ERRORE")
        self.__passeggeriMax = value

if __name__ == "__main__":
    