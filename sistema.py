from models import Voo

class SistemaReservas:
    def __init__(self):
        self._voos = {}

    def adicionar_voo(self, voo: Voo):
        self._voos[voo.id_voo] = voo
        
    def buscar_voo(self, id_voo: str) -> Voo:
        return self._voos.get(id_voo)
        
    def gerar_relatorio_geral(self):
        print("="*40)
        print("relatorio geral de voos do sistema")
        print("="*40)
        if not self._voos:
            print("nenhum voo cadastrado no sistema.")
            return
            
        for voo in self._voos.values():
            print(voo.gerar_relatorio())
            print("-" * 40)