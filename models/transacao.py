from abc import ABC, abstractproperty, abstractclassmethod

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @classmethod
    @abstractclassmethod
    def registrar(self, conta):
        pass