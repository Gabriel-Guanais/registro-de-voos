from abc import ABC, abstractmethod

class IRelatorio(ABC):
    """
    vai definir uma interface para objetos que podem gerar um relatorio e retorna uma 
    string formatada coma as informacoes do objeto
    """
    @abstractmethod
    def gerar_relatorio(self) -> str:
        pass