import random
from faker import Faker
from sistema import SistemaReservas
from models import Voo, Passageiro, Tripulante

def popular_sistema(sistema: SistemaReservas, num_voos=10):
    faker = Faker('pt_BR')
    precos_base = [1250.00, 899.50, 2100.00, 1540.75, 750.00, 3200.00, 999.00, 1800.20, 2500.00, 1100.50]
    
    for i in range(num_voos):
        id_voo = f"g3-{random.randint(1000, 2000)}"
        preco = precos_base[i]
        voo = Voo(id_voo=id_voo, preco=preco)
        
        voo.adicionar_tripulante(Tripulante(nome=faker.name(), funcao="piloto"))
        voo.adicionar_tripulante(Tripulante(nome=faker.name(), funcao="copiloto"))
        for _ in range(4):
            voo.adicionar_tripulante(Tripulante(nome=faker.name(), funcao="comissario de bordo"))
            
        sistema.adicionar_voo(voo)
    print(f"{num_voos} voos criados e populados com tripulacao")
    
def encher_voos_com_passageiros(sistema: SistemaReservas):
    faker = Faker('pt_BR')
    print("iniciando embarque de 250 passageiros em cada voo..")

    for voo in sistema._voos.values():
        assentos_para_reservar = list(voo.assentos.values())
        
        for assento in assentos_para_reservar:
            novo_passageiro = Passageiro(nome=faker.name(), cpf=faker.cpf())
            voo.reservar_assento(assento.identificador, novo_passageiro)

    print("embarque finalizado em todos os voos")

if __name__ == "__main__":
    
    sistema_de_voos = SistemaReservas()
    
    popular_sistema(sistema_de_voos)
    
    encher_voos_com_passageiros(sistema_de_voos)
    
    print("\n")
    sistema_de_voos.gerar_relatorio_geral()