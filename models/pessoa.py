from interfaces import IRelatorio

class Pessoa(IRelatorio):
    def __init__(self, nome: str):
        self._nome = nome

    @property
    def nome(self) -> str:
        return self._nome

    def gerar_relatorio(self) -> str:
        return f"nome: {self.nome}"