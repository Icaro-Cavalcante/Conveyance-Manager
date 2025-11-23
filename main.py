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
        print("")
        if escolha == 6:
            menu_veiculos()
        if escolha == 7:
            break

def menu_veiculos():
    while True:
        print("Menu de veículos")
        print(f"-" * 20)
        print(f"Escolha uma opção:\n1 - Cadastrar veículos\n2 - Procurar veículos\n3 - Editar veículos\n4 - Remover veículos\n5 - Voltar\n")
        escolha = int(input("Sua escolha: "))
        print("")
        if escolha == 1:
            Cadastro_veiculos.criar_veiculo()
        elif escolha == 2:
            placa = str(input("Qual a placa do veículo que deseja procurar? "))
            Cadastro_veiculos.ler_veiculo(placa)
        if escolha == 5:
            break
main()