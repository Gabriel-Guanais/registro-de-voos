import random
from interfaces import IRelatorio
from .tripulante import Tripulante
from .assento import Assento
from .passageiro import Passageiro

class Voo(IRelatorio):
    def __init__(self, id_voo: str, preco: float):
        self._id_voo = id_voo
        self._preco = preco
        self._tripulantes = []
        self._assentos = self._criar_assentos(250)
        
    @property
    def id_voo(self) -> str:
        return self._id_voo
    
    @property
    def preco(self) -> float:
        return self._preco
        
    @property
    def tripulantes(self) -> list:
        return self._tripulantes
        
    @property
    def assentos(self) -> dict:
        return self._assentos

    def _criar_assentos(self, quantidade: int) -> dict:
        assentos_criados = {}
        filas = (quantidade // 6) + 1
        letras = "abcdef"
        for fila in range(1, filas + 1):
            for letra in letras:
                if len(assentos_criados) < quantidade:
                    identificador = f"{fila}{letra}"
                    assentos_criados[identificador] = Assento(identificador)
        return assentos_criados

    def adicionar_tripulante(self, tripulante: Tripulante):
        self._tripulantes.append(tripulante)
        
    def reservar_assento(self, id_assento: str, passageiro: Passageiro) -> bool:
        assento = self._assentos.get(id_assento)
        if assento and not assento.ocupado:
            assento.reservar(passageiro)
            return True
        return False

    def gerar_relatorio(self) -> str:
        relatorio = [
            f"--- voo {self.id_voo} - preco: r$ {self.preco:.2f} ---",
            "\n[ tripulacao a bordo ]"
        ]
        for tripulante in self.tripulantes:
            relatorio.append(tripulante.gerar_relatorio())
            
        relatorio.append("\n[ passageiros a bordo nome-assento]")
        
        passageiros_a_bordo = []
        for assento in self.assentos.values():
            if assento.ocupado:
                nome_original = assento.passageiro.nome
                passageiros_a_bordo.append(f"{nome_original}-{assento.identificador}")
        
        if passageiros_a_bordo:
            relatorio.append(", ".join(passageiros_a_bordo))
        else:
            relatorio.append("nenhum passageiro embarcado neste voo.")
            
        return "\n".join(relatorio)