
class Cabina:
    def __init__(self, idCabina, nLetti, nPonte, prezzo):
        self._idCabina = idCabina
        self._nLetti = nLetti
        self._nPonte = nPonte
        self._prezzo = int(prezzo)
        self._tipologia = "Standard"


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

    def __str__(self):
        return (f'Codice univoco cabina "{self._idCabina}",'
                f' Numero di letti "{self.nLetti}",'
                f' Numero di ponte "{self.nPonte}",'
                f' Prezzo € {self.prezzo} per tipologia {self.tipologia}')








