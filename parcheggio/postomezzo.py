#Filippo Zamponi
#4BS
#classe PostoMezzo

from datetime import datetime

mezzi = ["autobus", "auto"]

class PostoMezzo:
    def __init__(self):
        self.__capacita_autobus = 20  # Capacità massima per autobus
        self.__capacita_auto = 100   # Capacità massima per auto
        self.__parcheggiautobus = 20
        self.__parcheggiauto = 100
        self.__postioccupati = {}  # Dizionario {targa: (tipologia, data/ora)}

    # -------------------------------------------------------------------------
    def __str__(self):
        stato = (
            f"Autobus disponibili: {self.__parcheggiautobus}/{self.__capacita_autobus}, "
            f"Auto disponibili: {self.__parcheggiauto}/{self.__capacita_auto}\n"
            f"Posti occupati: {self.__postioccupati if self.__postioccupati else 'Nessuno'}"
        )
        return stato

    def __repr__(self):
        return self.__str__()

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
            raise ValueError("Tipologia di mezzo non valida.")
        if targa in self.__postioccupati:
            raise ValueError(f"Veicolo con targa '{targa}' già parcheggiato.")

        if tipologiamezzo == "autobus":
            if self.__parcheggiautobus > 0:
                self.__parcheggiautobus -= 1
                self.__postioccupati[targa] = (tipologiamezzo, data_ora_termine)
            else:
                raise ValueError("Nessun posto disponibile per autobus.")
        
        elif tipologiamezzo == "auto":
            if self.__parcheggiauto > 0:
                self.__parcheggiauto -= 1
                self.__postioccupati[targa] = (tipologiamezzo, data_ora_termine)
            else:
                raise ValueError("Nessun posto disponibile per auto.")

    def liberaPosto(self, targa):
        if targa not in self.__postioccupati:
            raise ValueError(f"Veicolo con targa '{targa}' non presente.")

        tipologiamezzo, _ = self.__postioccupati.pop(targa)
        if tipologiamezzo == "autobus":
            self.__parcheggiautobus += 1
        elif tipologiamezzo == "auto":
            self.__parcheggiauto += 1

# -------------------------------------------------------------------------
if __name__ == "__main__":
    p = PostoMezzo()
    print(p)

    # Occupa un posto per auto
    p.occupaPosto("auto", "AB 123 CD", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(p)

    # Occupa un posto per autobus
    p.occupaPosto("autobus", "EF 456 GH", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(p)

    # Libera un posto per auto
    p.liberaPosto("AB 123 CD")
    print(p)

    # Libera un posto per autobus
    p.liberaPosto("EF 456 GH")
    print(p)