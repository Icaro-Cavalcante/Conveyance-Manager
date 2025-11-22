from modules.abastecimentos import Abastecimento
from modules.alocacao import Alocacao
from modules.manutencoes import Manutencoes
from modules.motoristas import *
from modules.relatorios import Relatorio
from modules.veiculos import *

def main():
    while True:
        print(f"Conveyance Manager")
        print("-" * 20)
        print(f"Escolha uma opção:\n1 - Abastecimento\n2 - Alocação\n3 - Manutenções\n4 - Cadastro de motoristas\n5 - Relatórios\n6 - Cadastro de veículos\n7 - Sair")
        escolha = int(input("Sua escolha: "))
        if escolha == 7:
            break
main()