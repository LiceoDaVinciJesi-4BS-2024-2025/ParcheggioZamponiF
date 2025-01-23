#Filippo Zamponi
#4BS
#classe PostoMezzo


from datetime import datetime, timedelta

mezzi = ["autobus", "auto"]

class PostoMezzo:
    def __init__(self):
        self.__parcheggiautobus = 1
        self.__parcheggiauto = 1
        self.__postioccupati = {}  # Dizionario {targa: (tipologia, orario_inizio, orario_fine)}

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
    def occupaPosto(self, tipologiamezzo, targa, inizio):
        tipologiamezzo = tipologiamezzo.lower()
        
        if tipologiamezzo not in mezzi:
            raise ValueError("Tipologia di mezzo non valida")
        if targa in self.__postioccupati:
            raise ValueError("Veicolo già parcheggiato.")

        # Calcolo l'orario di fine (aggiungo 1 ora all'orario di inizio)
        orario_inizio = inizio
        orario_fine = inizio + timedelta(hours=1)  # Aggiungo 1 ora

        if tipologiamezzo == "autobus":
            if self.__parcheggiautobus > 0:
                self.__parcheggiautobus -= 1
                self.__postioccupati[targa] = (tipologiamezzo, orario_inizio, orario_fine)
            else:
                raise ValueError("Nessun posto disponibile per autobus")
        
        elif tipologiamezzo == "auto":
            if self.__parcheggiauto > 0:
                self.__parcheggiauto -= 1
                self.__postioccupati[targa] = (tipologiamezzo, orario_inizio, orario_fine)
            else:
                raise ValueError("Nessun posto disponibile per auto")

    # -------------------------------------------------------------------------
    def liberaPosto(self, targa):
        if targa not in self.__postioccupati:
            raise ValueError("Veicolo non presente")

#ordino le targhe con pop , estrapolando l elemento associato a targa al posto 0
        tipologiamezzo = self.__postioccupati.pop(targa)[0]
        
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
    p.occupaPosto("auto", "AB123CD", datetime.now())
    print(p)
    
    print("--------------------------------------------------")
    
    # Occupo un posto per autobus
    p.occupaPosto("autobus", "EF456GH", datetime.now())
    print(p)
    
    print("--------------------------------------------------")

    # Libero un posto per auto
    p.liberaPosto("AB123CD")
    print(p)
    
    print("--------------------------------------------------")

    # Libero un posto per autobus
    p.liberaPosto("EF456GH")
    print(p)