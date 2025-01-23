#Filippo Zamponi
#4BS
#classe parcheggio 

from datetime import datetime, timedelta

mezzi = ["auto","autobus"]
costi = [1.5,2.4]
class Parcheggio:
    def __init__(self):
        self.__parcheggiauto = 1000
        self.__parcheggiautobus = 100
        
        self.__postioccupati = {}  # Dizionario {targa: (tipologia, orario_inizio, orario_fine)}

    # -------------------------------------------------------------------------
    def __str__(self):
        return "Parcheggio:" + str(self.__dict__)
    
    def __repr__(self):
        return "Parcheggio:" + str(self.__dict__)
    
    # -------------------------------------------------------------------------
    @property
    def parcheggiautobus(self):
        return self.__parcheggiautobus

    @property
    def parcheggiauto(self):
        return self.__parcheggiauto

    # -------------------------------------------------------------------------
    def occupaPosto(self, tipologiamezzo, targa, inizio , ore):
        tipologiamezzo = tipologiamezzo.lower()
        
        if tipologiamezzo not in mezzi:
            raise ValueError("Tipologia di mezzo non valida")
        if targa in self.__postioccupati:
            raise ValueError("Veicolo già parcheggiato.")

        # Calcolo l'orario di fine (aggiungo 1 ora all'orario di inizio)
        orario_inizio = inizio
        orario_fine = inizio + timedelta(hours=ore)  # Aggiungo 1 ora

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
    
    def conto(self,tipologiamezzo,ore):
        conto = 0 
        if tipologiamezzo.lower() == "auto":
            pagamento = costi[0] * ore
            conto += pagamento
        
        elif tipologiamezzo.lower() == "autobus":
            pagamento = costi[1] * ore
            conto += pagamento
        
        return conto 
                
            

# -------------------------------------------------------------------------
if __name__ == "__main__":
    p = Parcheggio()
    print(p)
    
    print("--------------------------------------------------")
    
    # Occupo un posto per auto e ci sto un ora
    p.occupaPosto("auto", "AB123CD", datetime.now(),1)
    print(p)
    
    print("--------------------------------------------------")
    
    #pagamento dell'entrata dell'auto
    costo = p.conto("auto",1)
    print("La macchina deve pagare :", costo)
    
    print("--------------------------------------------------")
    
    # Occupo un posto per autobus e ci sto 3 ore
    p.occupaPosto("autobus", "EF456GH", datetime.now(),3)
    print(p)
    
    print("--------------------------------------------------")
    
    #pagamento dell'entrata dell'auto
    costo = p.conto("autobus",5)
    print("L'autobus deve pagare :", costo)
    
    print("--------------------------------------------------")

    # Libero un posto per auto
    p.liberaPosto("AB123CD")
    print(p)
    
    print("--------------------------------------------------")

    # Libero un posto per autobus
    p.liberaPosto("EF456GH")
    print(p)
    