from .passageiro import Passageiro

class Assento:
    def __init__(self, identificador: str):
        self._identificador = identificador
        self._ocupado = False
        self._passageiro = None

    @property
    def identificador(self) -> str:
        return self._identificador

    @property
    def ocupado(self) -> bool:
        return self._ocupado

    @property
    def passageiro(self) -> Passageiro:
        return self._passageiro
    
    def reservar(self, passageiro: Passageiro):
        if not self.ocupado:
            self._ocupado = True
            self._passageiro = passageiro
            return True
        return False
        
    def __str__(self):
        return self.identificador