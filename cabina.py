
class Cabina:
    def __init__(self, idCabina, nLetti, nPonte, prezzo):
        self._idCabina = idCabina
        self._nLetti = nLetti
        self._nPonte = nPonte
        self._prezzo = int(prezzo)
        self._tipologia = "Standard"
        self._disponibilita = True


    '''definisco i metodi getter e setter'''
    @property
    def idCabina(self):
        return self._idCabina
    @idCabina.setter
    def idCabina(self, idCabina):
        self._idCabina = idCabina

    @property
    def nLetti(self):
        return self._nLetti
    @nLetti.setter
    def nLetti(self, nLetti):
        self._nLetti = nLetti

    @property
    def nPonte(self):
        return self._nPonte
    @nPonte.setter
    def nPonte(self, nPonte):
        self._nPonte = nPonte

    @property
    def prezzo(self):
        return self._prezzo
    @prezzo.setter
    def prezzo(self, prezzo):
        self._prezzo = prezzo

    @property
    def tipologia(self):
        return self._tipologia
    @tipologia.setter
    def tipologia(self, tipologia):
        self._tipologia = tipologia

    @property
    def disponibilita(self):
        return self._disponibilita
    @disponibilita.setter
    def disponibilita(self, disponibilita):
        self._disponibilita = disponibilita


    def __str__(self):
        if self._disponibilita:
            disponibilita = "DISPONIBILE"
        else:
            disponibilita = "NON DISPONIBILE"
        return (f'Codice univoco cabina "{self._idCabina}",'
                f' Numero di letti "{self.nLetti}",'
                f' Numero di ponte "{self.nPonte}",'
                f' Prezzo € {self.prezzo} per tipologia {self.tipologia}'
                f' | {disponibilita}')

    def __eq__(self, other):
        return self.idCabina == other.idCabina

    def __lt__(self, other):
        #ordinamento per crescita del prezzo e, in caso di uguaglianza
        #parte numerica del codice della stanza crescente
        if self.prezzo == other.prezzo:
            return int(self.idCabina[3:]) < int(other.idCabina[3:])
        return self.prezzo < other.prezzo
