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
        elif escolha == 3:
            menu_edicao_veiculos()
        elif escolha == 5:
            break

def menu_edicao_veiculos():
    while True:
        print("Menu de edição de veículos")
        print(f"-" * 20)
        print("O que deseja editar?\n1 - Marca\n2 - Modelo\n3 - Tipo\n4 - Ano\n5 - Quilometragem\n6 - Consumo médio\n7 - Status\n8 - Voltar\n")
        atributo = int(input("Qual atributo deseja editar? "))
        if atributo >8 or atributo <1:
            print("Selecione um atributo válido.")
        elif atributo == 8:
            break
        else:
            placa = str(input("Qual a placa do veículo que deseja editar? "))
            Cadastro_veiculos.atualizar_veiculo(placa, atributo)

main()