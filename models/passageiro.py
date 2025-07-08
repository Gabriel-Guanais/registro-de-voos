# modelos/passageiro.py

from .pessoa import Pessoa

class Passageiro(Pessoa):
    def __init__(self, nome: str, cpf: str):
        super().__init__(nome)
        self._cpf = cpf

    @property
    def cpf(self) -> str:
        return self._cpf
    
    def gerar_relatorio(self) -> str:
        return f"passageiro: {self.nome} (cpf: {self.cpf})"