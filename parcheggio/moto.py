#Filippo Zamponi
#4BS
#classe Moto

class Moto:
    def __init__(self,passeggeri,passeggeriMax,capacità,chili):
        if passeggeri > 2 or passeggeri < 0:
            raise ValueError("Troppi Passeggeri")
        self.__passeggeri = passeggeri
        
        if passeggeriMax != 2:
            raise ValueError("
        self.__passeggeriMax = passeggeriMax
        self.__capacità = capacità
        self.__chili = chili
    
    @property
    def targa(self):
        return self.__targa
    @targa.setter
    def targa(self, value):
        if len(targa) != 7:
            raise ValueError
        if targa[0] not in alfabeto or targa[1] not in alfabeto or targa[2] not in numeri or targa[3] not in numeri or targa[4] not in numeri or targa[5] not in alfabeto or targa[6] not in alfabeto:
            raise ValueError("Targa non valida")
        self.__targa = value
    
        
        
        
    
    

if __name__ == "__main__":
    Moto1 = Moto(2,1,100,60)
    print(Moto1)