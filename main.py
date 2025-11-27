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
        if escolha == 1:
            print("Feature em desenvolvimento.\n")
        elif escolha == 2:
            print("Feature em desenvolvimento.\n")
        elif escolha == 3:
            print("Feature em desenvolvimento.\n")
        elif escolha == 4:
            menu_motoristas()
        elif escolha == 5:
            print("Feature em desenvolvimento.\n")
        elif escolha == 6:
            menu_veiculos()
        elif escolha == 7:
            break
        else:
            print("Escolha inválida.\n")

def menu_motoristas():
    while True:
        print("Menu de motoristas:")
        print("-" * 20)
        print(f"1 - Cadastrar motoristas\n2 - Procurar motoristas\n3 - Editar motoristas\n4 - Remover motoristas\n5 - Voltar")
        escolha = int(input("Sua escolha: "))
        print("")
        if escolha == 1:
            Cadastro_motorista.criar_motorista()
        elif escolha == 2:
            outro_cpf = str(input("Digite o CPF do motorista que deseja procurar: "))
            Cadastro_motorista.mostrar_motorista(outro_cpf)
        elif escolha == 3:
            menu_edicao_motoristas()
        elif escolha == 4:
            outro_cpf = str(input("Digite o CPF do motorista que deseja procurar: "))
            Cadastro_motorista.remover_motorista(outro_cpf)
        elif escolha == 5:
            break
        else:
            print("Escolha inválida")

def menu_edicao_motoristas():
    while True:
        print("Menu de edição de motoristas:")
        print("-" * 20)
        print(f"1 - Nome\n2 - Categoria da CNH\n3 - Experiência\n4 - Disponibilidade\n5 - Histórico\n6 - Voltar")
        atributo = int(input("Qual atributo deseja editar? "))
        print("")
        if atributo <1 or atributo >6:
            print("Atributo inválido.")
        elif atributo == 6:
            break
        else:
            cpf = str(input("Digite o CPF do motorista que deseja editar: "))
            Cadastro_motorista.atualizar_motorista(cpf, atributo)

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
            Cadastro_veiculos.mostrar_veiculo(placa)
        elif escolha == 3:
            menu_edicao_veiculos()
        elif escolha == 4:
            placa = str(input("Qual a placa do veículo que deseja remover? "))
            Cadastro_veiculos.remover_veiculo(placa)
        elif escolha == 5:
            break
        else:
            print("Escolha inválida")

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