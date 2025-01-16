#Filippo Zamponi
#4BS
#classe Veicolo

marche = ["Fiat", "BMW", "Audi", "Mercedes", "Citroen", "Jaguar", "Aston Martin", "Ferrari"]
colori = ["Rosso", "Blu", "Verde", "Nero", "Bianco"]
alimentazioni = ["Benzina", "Diesel", "Elettrico"]
alfabeto = "QWERTYUIOPASDFGHJKLZXCVBNM"
numeri = "1234567890"

class Veicolo:
    def __init__(self, marca, modello, colore, cilindrata: int, alimentazione, targa):
        if marca not in marche:
            raise ValueError("La marca non è nella lista marche.")
        self.__marca = marca

        self.__modello = modello

        if colore not in colori:
            raise ValueError("Colore non valido")
        self.__colore = colore

        if cilindrata % 100 != 0:
            raise ValueError("La cilindrata non è multiplo di 100.")
        self.__cilindrata = cilindrata

        if alimentazione not in alimentazioni:
            raise ValueError("Errore l'alimentazione non è accettabile.")
        self.__alimentazione = alimentazione

        if len(targa) != 7:
            raise ValueError
        if targa[0] not in alfabeto or targa[1] not in alfabeto or targa[2] not in numeri or targa[3] not in numeri or targa[4] not in numeri or targa[5] not in alfabeto or targa[6] not in alfabeto:
            raise ValueError("Targa non valida")
        self.__targa = targa

    def __str__(self):
        return "Veicolo:" + str(self.__dict__)
    def __repr__(self):
        return "Veicolo:" + str(self.__dict__)

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, value):
        if value not in marche:
            raise ValueError("La marca non è nella lista marche.")
        self.__marca = value

    @property
    def modello(self):
        return self.__modello

    @property
    def colore(self):
        return self.__colore

    @colore.setter
    def colore(self, value):
        if value not in colori:
            raise ValueError("Colore non valido")
        self.__colore = value

    @property
    def cilindrata(self):
        return self.__cilindrata

    @cilindrata.setter
    def cilindrata(self, value):
        if value % 100 != 0:
            raise ValueError("La cilindrata non è multiplo di 100.")
        self.__cilindrata = value

    @property
    def alimentazione(self):
        return self.__alimentazione

    @alimentazione.setter
    def alimentazione(self, value):
        if value not in alimentazioni:
            raise ValueError("Errore l'alimentazione non è accettabile.")
        self.__alimentazione = value

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
    Veicolo1 = Veicolo("Fiat", "Punto", "Rosso", 1000, "Benzina", "AD124FB")
    print(Veicolo1)