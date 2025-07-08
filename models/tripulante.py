from .pessoa import Pessoa

class Tripulante(Pessoa):
    def __init__(self, nome: str, funcao: str):
        super().__init__(nome)
        self._funcao = funcao

    @property
    def funcao(self) -> str:
        return self._funcao
        
    def gerar_relatorio(self) -> str:
        return f"{self.funcao}: {self.nome}"