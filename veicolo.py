#Filippo Zamponi
#4BS
#classe Veicolo

marche = ["Fiat","BMW","Audi","Mercedes","Citroen","Jaguar","Aston Martin","Ferrari"]
colori = ["Rosso","Blu","Verde","Nero","Bianco"]
alimentazioni = ["Benzina","Diesel","Elettrico"]

class Veicolo:
    def __init__ (self,marca,modello,colore,cilindrata : int,alimentazione,targa):
        
#da fare i controlli anche qua       
        self.__marca = marca
        self.__modello = modello
        self.__colore = colore
        self.__cilindrata = cilindrata
        self.__alimentazione = alimentazione
        self.__targa = targa
#----------------------------------------------------------------------------------------------        
    def __str__(self):
        return "Veicolo:" + str(self.__dict__)
    def __repr__(self):
        return "Veicolo:" + str(self.__dict__)
#----------------------------------------------------------------------------------------------        
    
    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, value):
        # Verifico che la marca sia nella lista
        if self.__marca not in marche:
            raise ValueError("La marca non è nella lista marche..")
        self.__marca = value
        return 
#----------------------------------------------------------------------------------------------        
        
    @property
    def modello(self):
        return self.__modello
#----------------------------------------------------------------------------------------------        
    
    @property
    def colore(self):
        return self._colore

    @colore.setter
    def colore(self, value):
        if self.__colore:
            raise ValueError(f"Colore non valido. I colori accettabili sono: {', '.join(Veicolo.colori_accettabili)}.")
        self._colore = value
        return

#----------------------------------------------------------------------------------------------        


#----------------------------------------------------------------------------------------------        

#----------------------------------------------------------------------------------------------        


#----------------------------------------------------------------------------------------------        

    
if __name__ == "__main__":
    Veicolo1 = Veicolo("tgflbhsj","Punto","Rosso",1000,"Benzina","AD124FB")
    print(Veicolo1)
    
    
    
    
    