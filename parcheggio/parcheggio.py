#Filippo Zamponi
#4BS
#classe parcheggio 
class Parcheggio:
    def __init__(self):
        # Prezzi per tipo di veicolo
        self.prezzi = {"auto": 1.5, "moto": 1.2, "camion": 1.8, "autobus": 2.4}
        
        # Capacità del parcheggio
        self.capacita = {"auto": 1000, "moto": 200, "camion": 50, "autobus": 100}
        
        # Stato del parcheggio (lista per ogni tipo di veicolo)
        self.parcheggio = {"auto": [], "moto": [], "camion": [], "autobus": []}
        
        # Guadagno totale
        self.guadagno_totale = 0

    def prenota_posto(self, tipo, targa, ore):
        if len(self.parcheggio[tipo]) < self.capacita[tipo]:
            self.parcheggio[tipo].append((targa, ore))
            self.guadagno_totale += ore * self.prezzi[tipo]
            print(f"Prenotazione per {tipo} con targa {targa} per {ore} ore completata.")
        else:
            print(f"Posti per {tipo} esauriti.")

    def posti_liberi(self):
        for tipo in self.capacita:
            posti = self.capacita[tipo] - len(self.parcheggio[tipo])
            print(f"Posti liberi per {tipo}: {posti}")

    def mostra_guadagno(self):
        print(f"Guadagno totale: {self.guadagno_totale:.2f} €")


# Ciclo principale
parcheggio = Parcheggio()

while True:
    print("\n1. Prenotare un posto")
    print("2. Vedere posti liberi")
    print("3. Vedere guadagno totale")
    print("4. Uscire")

    scelta = input("Scegli un'opzione: ")

    if scelta == "1":
        tipo = input("Inserisci il tipo di veicolo (auto, moto, camion, autobus): ").lower()
        if tipo not in parcheggio.capacita:
            print("Tipo di veicolo non valido.")
            continue
        targa = input("Inserisci la targa del veicolo: ")
        ore = int(input("Inserisci il numero di ore di sosta: "))
        parcheggio.prenota_posto(tipo, targa, ore)

    elif scelta == "2":
        parcheggio.posti_liberi()

    elif scelta == "3":
        parcheggio.mostra_guadagno()

    elif scelta == "4":
        print("Uscita...")
        break

    else:
        print("Opzione non valida. Riprova.")