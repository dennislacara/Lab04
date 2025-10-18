from csv import reader
from cabina import Cabina
from cabinaDeluxe import CabinaDeluxe
from cabinaAnimali import CabinaAnimali
from passeggero import Passeggero
from operator import attrgetter

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self._nome = nome
        self.cabineTotali = {} #cabineTotali = { idCabina: [oggettoCabina, disponibilita], ...}
        self.passeggeriTotali = {} #passeggeriTotali = { idPasseggero: oggettoPasseggero, ...}
        self.cabineAssegnatePasseggeri = {} # { idPasseggero : oggettoCabina, ...}
        # TODO

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        try:
            f = open(file_path, "r")
        except FileNotFoundError:
            raise FileNotFoundError

        #smistamento degli elementi presenti nel file
        # ogni cabina è aggiunta al dizionario cabineTotali specificando la disponibilita
        # nella forma: cabineTotali = { idCabina: [oggettoCabina, disponibilita], ...}
        disponibilita = True
        for riga in reader(f):
            #print(riga)
            if len(riga) == 3: #passeggero
                self.passeggeriTotali[riga[0]]=Passeggero(riga[0], riga[1], riga[2])

            elif len(riga) == 4: #cabina Standard
                self.cabineTotali[riga[0]] =[Cabina(riga[0], riga[1], riga[2], riga[3]), disponibilita]

            elif len(riga) == 5 and riga[4].isalpha(): #cabina deluxe
                self.cabineTotali[riga[0]] = [CabinaDeluxe(riga[0], riga[1], riga[2], riga[3], riga[4]), disponibilita]

            elif len(riga) == 5 and riga[4].isdigit(): #cabina animali
                self.cabineTotali[riga[0]] = [CabinaAnimali(riga[0], riga[1], riga[2], riga[3], riga[4]), disponibilita]
            else:
                raise Exception('file mal formattato')

        # TODO

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        #controllo che esistano i dati nel sistema
        if codice_cabina in self.cabineTotali and codice_passeggero in self.passeggeriTotali:
            #controllo che il passeggero non sia assegnato ad altra stanza
            if codice_passeggero not in self.cabineAssegnatePasseggeri:
                #controllo che la cabina sia libera
                if self.cabineTotali[codice_cabina][1] == True:
                    #assegno la cabina al passeggero
                    self.cabineAssegnatePasseggeri[codice_passeggero] = self.cabineTotali[codice_cabina]
                    #cambio la disponibilità della cabina
                    self.cabineTotali[codice_cabina][1] = False
                    #print(self.cabineAssegnatePasseggeri[codice_passeggero][0])

                else:
                    raise Exception('Cabina non disponibile')
            else:
                raise Exception('Il passeggero ha già una cabina assegnata')
        else:
            raise Exception('cabina/passeggero non trovata/o')

        # TODO

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        listaCabine = []
        for cab in self.cabineTotali:
            oggettoCabina = self.cabineTotali[cab][0]
            listaCabine.append(oggettoCabina)
        listaCabineOrdinate = sorted(listaCabine, key= attrgetter('prezzo'), reverse=False)

        listaCabineOrdinateDisponibilita = []
        for cab2 in listaCabineOrdinate:
            idCabina = cab2.idCabina
            disponibilitaCabina = self.cabineTotali[idCabina][1]
            listaCabineOrdinateDisponibilita.append([cab2, disponibilitaCabina])
            #print((cab2, disponibilitaCabina))
        return listaCabineOrdinateDisponibilita

        # TODO


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        for id_passeggero in self.passeggeriTotali:

            if id_passeggero in self.cabineAssegnatePasseggeri:
                print(f'{self.passeggeriTotali[id_passeggero]};'
                      f' Assegnato alla cabina:\n{self.cabineAssegnatePasseggeri[id_passeggero][0]}')
                print()
            else:
                print(f'{self.passeggeriTotali[id_passeggero]}')
                print()
        # TODO

