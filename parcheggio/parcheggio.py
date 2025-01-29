#Filippo Zamponi
#4BS
#parcheggio
from datetime import datetime, timedelta

mezzi = ["auto", "autobus"]
costi = [1.5, 2.4]

class Parcheggio:
    def __init__(self):
        self.__parcheggiauto = 1000
        self.__parcheggiautobus = 100
        self.__postioccupati = {}  # Dizionario {targa: (tipologia, orario_inizio, orario_fine)}

        self.caricaDati()
#-------------------------------------------------------------------------
    def __str__(self):
        return "Parcheggio:" + str(self.__dict__)
    def __repr__(self):
        return "Parcheggio:" + str(self.__dict__)
#-------------------------------------------------------------------------
    @property
    def parcheggiautobus(self):
        return self.__parcheggiautobus

    @property
    def parcheggiauto(self):
        return self.__parcheggiauto

#-------------------------------------------------------------------------    
    def occupaPosto(self, tipologiamezzo, targa, inizio, ore):
        tipologiamezzo = tipologiamezzo.lower()

        if tipologiamezzo not in mezzi:
            raise ValueError("Tipologia di mezzo non valida")
        if targa in self.__postioccupati:
            raise ValueError("Veicolo già parcheggiato.")

        orario_inizio = inizio
        orario_fine = inizio + timedelta(hours=ore)

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
#-------------------------------------------------------------------------
    def liberaPosto(self, targa):
        if targa not in self.__postioccupati:
            raise ValueError("Veicolo non presente")

        tipologiamezzo = self.__postioccupati.pop(targa)[0]

        if tipologiamezzo == "autobus":
            self.__parcheggiautobus += 1
        elif tipologiamezzo == "auto":
            self.__parcheggiauto += 1
#-------------------------------------------------------------------------
    def conto(self, tipologiamezzo, ore):
        conto = 0
        if tipologiamezzo.lower() == "auto":
            pagamento = costi[0] * ore
            conto += pagamento

        elif tipologiamezzo.lower() == "autobus":
            pagamento = costi[1] * ore
            conto += pagamento

        return conto
#-------------------------------------------------------------------------
    def salvadati(self):
        f = open("park.data", "w")
        
        f.write(f"{self.__parcheggiauto},{self.__parcheggiautobus}\n")

        for targa, (tipologia, orario_inizio, orario_fine) in self.__postioccupati.items():
            f.write(f"{targa}|{tipologia}|{orario_inizio.strftime('%Y-%m-%d %H:%M:%S')}|{orario_fine.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.close()
#-------------------------------------------------------------------------
    def caricaDati(self):
        f = open("park.data", "r")
        lines = f.readlines()
        f.close()

        if len(lines) == 0:
            return  # Se il file è vuoto, non carica nulla

        # Carica i posti liberi
        dati_posti = lines[0].strip().split(",")
        self.__parcheggiauto = int(dati_posti[0])
        self.__parcheggiautobus = int(dati_posti[1])

        # Carica i veicoli parcheggiati
        for line in lines[1:]:
            parts = line.strip().split("|")
            if len(parts) == 4:
                targa, tipologia, orario_inizio, orario_fine = parts
                self.__postioccupati[targa] = (tipologia,datetime.strptime(orario_inizio, "%Y-%m-%d %H:%M:%S"),datetime.strptime(orario_fine, "%Y-%m-%d %H:%M:%S"))

# -------------------------------------------------------------------------
if __name__ == "__main__":
    p = Parcheggio()
    print(p)

    print("--------------------------------------------------")

    # Occupo un posto per auto e ci sto un ora
    p.occupaPosto("auto", "AB123CD", datetime.now(), 1)
    print(p)

    print("--------------------------------------------------")

    # Pagamento dell'entrata dell'auto
    costo = p.conto("auto", 1)
    print("La macchina deve pagare :", costo)

    print("--------------------------------------------------")

    # Occupo un posto per autobus e ci sto 3 ore
    p.occupaPosto("autobus", "EF456GH", datetime.now(), 3)
    print(p)

    print("--------------------------------------------------")

    # Pagamento dell'entrata dell'autobus
    costo = p.conto("autobus", 5)
    print("L'autobus deve pagare :", costo)

    print("--------------------------------------------------")


    # Libero un posto per autobus
    p.liberaPosto("EF456GH")
    print(p)

    # Salvo i dati
    p.salvadati()