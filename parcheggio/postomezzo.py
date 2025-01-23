#Filippo Zamponi
#4BS
#classe PostoMezzo

from datetime import datetime

mezzi = ["autobus", "auto"]

class PostoMezzo:
    def __init__(self):
        self.__parcheggiautobus = 20
        self.__parcheggiauto = 100
        self.__postioccupati = {}  # Dizionario {targa: (tipologia, data/ora)}

    # -------------------------------------------------------------------------
    def __str__(self):
        return "PostoMezzo:" + str(self.__dict__)
    def __repr__(self):
        return "PostoMezzo:" + str(self.__dict__)
    # -------------------------------------------------------------------------
    @property
    def parcheggiautobus(self):
        return self.__parcheggiautobus

    @property
    def parcheggiauto(self):
        return self.__parcheggiauto

    # -------------------------------------------------------------------------
    def occupaPosto(self, tipologiamezzo, targa, data_ora_termine):
        tipologiamezzo = tipologiamezzo.lower()
        
        if tipologiamezzo not in mezzi:
            raise ValueError("Tipologia di mezzo non valida")
        if targa in self.__postioccupati:
            raise ValueError("Veicolo già parcheggiato.")

        if tipologiamezzo == "autobus":
            if self.__parcheggiautobus > 0:
                self.__parcheggiautobus -= 1
                self.__postioccupati[targa] = (tipologiamezzo, data_ora_termine)
            else:
                raise ValueError("Nessun posto disponibile per autobus")
        
        elif tipologiamezzo == "auto":
            if self.__parcheggiauto > 0:
                self.__parcheggiauto -= 1
                self.__postioccupati[targa] = (tipologiamezzo, data_ora_termine)
            else:
                raise ValueError("Nessun posto disponibile per auto")
# -------------------------------------------------------------------------
    def liberaPosto(self, targa):
        if targa not in self.__postioccupati:
            raise ValueError("Veicolo non presente")

#ordino le targhe con pop
        tipologiamezzo = self.__postioccupati.pop(targa)
        
        if tipologiamezzo == "autobus":
            self.__parcheggiautobus += 1
        elif tipologiamezzo == "auto":
            self.__parcheggiauto += 1

# -------------------------------------------------------------------------
if __name__ == "__main__":
    p = PostoMezzo()
    print(p)
    
    print("--------------------------------------------------")
    
    # Occupo un posto per auto
    p.occupaPosto("auto", "AB123CD", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(p)
    
    print("--------------------------------------------------")
    
    # Occupo un posto per autobus
    p.occupaPosto("autobus", "EF456GH", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(p)
    
    print("--------------------------------------------------")

    # Libero un posto per auto
    p.liberaPosto("AB123CD")
    print(p)
    
    print("--------------------------------------------------")

    # Libero un posto per autobus
    p.liberaPosto("EF456GH")
    print(p)