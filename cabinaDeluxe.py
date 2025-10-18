from cabina import Cabina

class CabinaDeluxe(Cabina):

    def __init__(self, idCabina, nLetti, nPonte, prezzo, tipologia):

        # assegnazione degli attributi della classe madre: Cabina
        super().__init__(idCabina, nLetti, nPonte, prezzo)

        #il prezzo subisce un incremento
        self._prezzo = int(prezzo) * 1.20

        # tipologia di cabina: Classica, Moderna, Lussuosa
        self._tipologia = tipologia

    '''definisco i metodi getter e setter'''
    @property
    def prezzo(self):
        return self._prezzo
    @prezzo.setter
    def prezzo(self, prezzo):
        self._prezzo = prezzo

    ## i metodi getter e setter per la tipologia sono ereditati






