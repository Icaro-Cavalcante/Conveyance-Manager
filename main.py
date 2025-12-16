from modules.abastecimentos import Abastecimento
from modules.alocacao import Alocacao
from modules.manutencoes import Manutencoes
from modules.motoristas import *
from modules.relatorios import Relatorio
from modules.veiculos import *
from modules.configuracoes import Configuracao

def main():
    '''Função principal.'''
    while True:
        print(f"Conveyance Manager")
        print("-" * 20)
        print(f"Escolha uma opção:\n1 - Abastecimento\n2 - Alocação\n3 - Manutenções\n4 - Cadastro de motoristas\n5 - Relatórios\n6 - Cadastro de veículos\n7 - Configurações\n8 - Sair")
        escolha = int(input("Sua escolha: "))
        print("")
        if escolha == 1:
            menu_abastecimentos()
        elif escolha == 2:
            menu_alocacao()
        elif escolha == 3:
            menu_manutencao()
        elif escolha == 4:
            menu_motoristas()
        elif escolha == 5:
            menu_relatorios()
        elif escolha == 6:
            menu_veiculos()
        elif escolha == 7:
            menu_config()
        elif escolha == 8:
            break
        else:
            print("Escolha inválida.\n")

def menu_config():
    '''Menu para interagir com as configurações'''
    while True:
        print("Menu de configurações")
        print("-" * 20)
        print(f"Escolha uma opção:\n1 - Preço gasolina\n2 - Preço manutenção\n3 - Compatibilidade da CNH\n4 - Quilometragem limite para manutenção\n5 - Consumo km/l padrão\n6 - Voltar")
        escolha = int(input("Digite sua escolha: "))
        if escolha == 1:
            Configuracao.configurar_gasolina()
        elif escolha == 2:
            Configuracao.configurar_manutencao()
        elif escolha == 3:
            Configuracao.configurar_compatibilidade()
        elif escolha == 4:
            Configuracao.configurar_limite()
        elif escolha == 5:
            Configuracao.configurar_consumo_padrao()
        elif escolha == 6:
            break
        else:
            print("Escolha inválida.")

def menu_abastecimentos():
    '''Menu para interagir com o sistema de abastecimentos.'''
    while True:
        print("Menu de abastecimentos")
        print("-" * 20)
        print(f"Escolha uma opção:\n1 - Abastecer\n2 - Verificar se o consumo está no padrão\n3 - Voltar")
        escolha = int(input("Digite sua escolha: "))
        print("")
        if escolha == 1:
            Abastecimento.registrar_abastecimento()
        elif escolha == 2:
            placa = str(input("Informe a placa do veículo: "))
            Abastecimento.consumo_padrao(placa)
        elif escolha == 3:
            break
        else:
            print("Escolha inválida")

def menu_relatorios():
    '''Menu para interagir com os relatórios.'''
    while True:
        print("Menu de relatórios")
        print("-" * 20)
        print(f"Escolha uma opção:\n1 - Relatório inicial\n2 - Total de viagens por motorista\n3 - Gerar quilometragem média por tipo de veículo\n4 - Gerar custo de manutenção\n5 - Voltar")
        escolha = int(input("Digite sua escolha: "))
        print("")
        if escolha == 1:
            Relatorio.relatorio_inicial()
        elif escolha == 2:
            Relatorio.gerar_viagens()
        elif escolha == 3:
            Relatorio.gerar_quilometragem()
        elif escolha == 4:
            Relatorio.gerar_custo_manutenção()
        elif escolha == 5:
            break
        else:
            print("Escolha inválida")

def menu_alocacao():
    '''Menu para interagir com o sistema de alocação.'''
    while True:
        print("Menu de alocações")
        print("-" * 20)
        print(f"Escolha uma opção:\n1 - Realizar alocação\n2 - Procurar alocação\n3 - Voltar")
        escolha = int(input("Digite sua escolha: "))
        print("")
        if escolha == 1:
            Alocacao.associar_registrar()
        elif escolha == 2:
            id = str(input("Qual o ID da alocação? "))
            print(Alocacao.procurar_alocacao(id))
        elif escolha == 3:
            break
        else:
            print("Escolha inválida.\n")


def menu_manutencao():
    '''Menu para interagir com o sistema de manutenção.'''
    while True:
        print("Menu de manutenções:")
        print("-" * 20)
        print("Escolha uma opção:\n1 - Calcular custo\n2 - Realizar manutenção\n3 - Liberar veículo\n4 - Procurar manutenção\n5 - Voltar")
        escolha = int(input("Sua escolha: "))
        print("")
        if escolha == 1:
            tipo = str(input("Qual o tipo de manutenção(Corretiva/Preventiva)? "))
            tipo_veiculo = str(input("Qual o tipo de veículo(Carro/Moto/Caminhão)? "))
            tipo = tipo.lower()
            tipo_veiculo = tipo_veiculo.lower()
            custo = Manutencoes.calcular_custo(tipo, tipo_veiculo)
            print(f"\nA manutenção custa R${custo}")
        elif escolha == 2:
            placa = str(input("\nQual a placa do veículo que deseja colocar em manutenção? "))
            Manutencoes.registrar_manutencao(placa)
        elif escolha == 3:
            placa = str(input("\nInforme a placa do veículo: "))
            Manutencoes.liberar_veiculo(placa)
        elif escolha == 4:
            id = int(input("\nInsira o ID da manutenção: "))
            Manutencoes.consultar_manutenao(id)
        elif escolha == 5:
            break

def menu_motoristas():
    '''Menu para interagir com o sistema de motoristas.'''
    while True:
        print("Menu de motoristas:")
        print("-" * 20)
        print(f"1 - Cadastrar motoristas\n2 - Procurar motoristas\n3 - Editar motoristas\n4 - Remover motoristas\n5 - Voltar")
        escolha = int(input("Sua escolha: "))
        print("")
        if escolha == 1:
            Motorista.criar_motorista()
        elif escolha == 2:
            outro_cpf = str(input("Digite o CPF do motorista que deseja procurar: "))
            print(Motorista.mostrar_motorista(outro_cpf))
        elif escolha == 3:
            menu_edicao_motoristas()
        elif escolha == 4:
            outro_cpf = str(input("Digite o CPF do motorista que deseja procurar: "))
            Motorista.remover_motorista(outro_cpf)
        elif escolha == 5:
            break
        else:
            print("Escolha inválida")

def menu_edicao_motoristas():
    '''Menu para editar os motoristas.'''
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
            Motorista.atualizar_motorista(cpf, atributo)

def menu_veiculos():
    '''Menu para interagir com o sistema de veículos.'''
    while True:
        print("Menu de veículos")
        print(f"-" * 20)
        print(f"Escolha uma opção:\n1 - Cadastrar veículos\n2 - Procurar veículos\n3 - Editar veículos\n4 - Remover veículos\n5 - Voltar\n")
        escolha = int(input("Sua escolha: "))
        print("")
        if escolha == 1:
            Veiculo.criar_veiculo()
        elif escolha == 2:
            placa = str(input("Qual a placa do veículo que deseja procurar? "))
            print(Veiculo.mostrar_veiculo(placa))
        elif escolha == 3:
            menu_edicao_veiculos()
        elif escolha == 4:
            placa = str(input("Qual a placa do veículo que deseja remover? "))
            Veiculo.remover_veiculo(placa)
        elif escolha == 5:
            break
        else:
            print("Escolha inválida")

def menu_edicao_veiculos():
    '''Menu para editar os veículos.'''
    while True:
        print("Menu de edição de veículos")
        print(f"-" * 20)
        print("O que deseja editar?\n1 - Marca\n2 - Modelo\n3 - Tipo\n4 - Ano\n5 - Quilometragem\n6 - Consumo médio\n7 - Status\n8 - Combustível\n9 - Voltar\n")
        atributo = int(input("Qual atributo deseja editar? "))
        if atributo >9 or atributo <1:
            print("Selecione um atributo válido.")
        elif atributo == 9:
            break
        else:
            placa = str(input("Qual a placa do veículo que deseja editar? "))
            Veiculo.atualizar_veiculo(placa, atributo)

main()