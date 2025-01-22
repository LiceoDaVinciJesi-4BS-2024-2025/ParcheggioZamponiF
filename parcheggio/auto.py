#Filippo Zamponi
#4BS
#classe Auto
from Veicolo import *

class Auto(Veicolo):
    def __init__(self, marca, modello, colore, cilindrata, alimentazione, targa,passeggeriMax = int,passeggeri = int,capacità = int,chili = int):
        super().__init__(marca, modello, colore, cilindrata, alimentazione, targa)
        if passeggeriMax != 4:
            raise ValueError("ERRORE")
        self.__passeggeriMax = passeggeriMax
        
        if passeggeri > 4 or passeggeri < 0:
            raise ValueError("Troppi Passeggeri")
        self.__passeggeri = passeggeri
        
        if capacità != 1000 :
            raise ValueError("ERRORE")
        self.__capacità = capacità
        
        if chili > 1000:
            raise ValueError("ERRORE")
        self.__chili = chili
#-------------------------------------------------------------------------
    def __str__(self):
        return "Auto:" + str(self.__dict__)
    def __repr__(self):
        return "Auto:" + str(self.__dict__)
#-------------------------------------------------------------------------    
    @property
    def passeggeriMax(self):
        return self.__passeggeriMax

    @passeggeriMax.setter
    def passeggeriMax(self, value):
        if passeggeriMax != 4:
            raise ValueError("ERRORE")
        self.__passeggeriMax = value
#-------------------------------------------------------------------------    
    @property
    def passeggeri(self):
        return self.__passeggeri

    @passeggeri.setter
    def passeggeri(self, value):
        if passeggeri > 4 or passeggeri < 0:
            raise ValueError("Troppi Passeggeri")
        self.__passeggeri = value
    
#-------------------------------------------------------------------------    
    @property
    def capacità(self):
        return self.__capacità

    @capacità.setter
    def capacità(self, value):
        if capacità != 1000:
            raise ValueError("ERRORE")
        self.__capacità = value
            
#-------------------------------------------------------------------------    
    @property
    def chili(self):
        return self.__chili

    @chili.setter
    def chili(self, value):
        if chili > 1000:
            raise ValueError("ERRORE")
        self.__chili = value

if __name__ == "__main__":
    Auto1 = Auto("Fiat", "Punto", "Rosso", 1000, "Benzina", "AD154FB",4,1,1000,70)
    print(Auto1)