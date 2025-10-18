
class Passeggero:
    def __init__(self, idPasseggero, nome, cognome):
        self._idPasseggero = idPasseggero
        self._nome = nome
        self._cognome = cognome

    '''definisco i metodi getter e setter'''
    @property
    def idPasseggero(self):
        return self._idPasseggero
    @idPasseggero.setter
    def idPasseggero(self, idPasseggero):
        self._idPasseggero = idPasseggero

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cognome(self):
        return self._cognome
    @cognome.setter
    def cognome(self, cognome):
        self._cognome = cognome

    def __str__(self):
        return (f'Codice univoco "{self._idPasseggero}":'
                f' sig. {self.nome} {self.cognome}')
