class Iterador:
    def __init__(self, lista):
        self.lista = lista
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            valor = self.lista[self.indice]
            self.indice += 1
            return valor
        except:
            raise StopIteration