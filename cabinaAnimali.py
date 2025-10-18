from cabina import Cabina

class CabinaAnimali(Cabina):

    def __init__(self, idCabina, nLetti, nPonte, prezzo, nAnimali):

        # assegnazione degli attributi della classe madre: Cabina
        super().__init__(idCabina, nLetti, nPonte, prezzo)

        self._nAnimali = int(nAnimali)
        #il prezzo subisce un incremento
        self._prezzo = int(prezzo) * (1 + 0.10 * self._nAnimali)

        self._tipologia = 'Animali'

