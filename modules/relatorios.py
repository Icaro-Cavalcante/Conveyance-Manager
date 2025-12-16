import sqlite3
import json
from .motoristas import Motorista
data_veiculos = r"data\veiculos.db"
caminho_json = r"config\settings.json"
class Relatorio():
    '''É a classe que cria os relatórios.'''
    def __init__(self):
        pass

    def relatorio_inicial():
        '''Faz o relatório inicial, mostrando os dados de todos os veículos e mostrando quantos estão ativos, inativo e em manutenção.'''
        conexao = sqlite3.connect(data_veiculos)
        cursor = conexao.cursor()
        lista_ativo = []
        lista_inativo = []
        lista_manutencao = []
        qtd_ativo = 0
        qtd_inativo = 0
        qtd_manutencao = 0

        cursor.execute('''SELECT * FROM veiculos''')
        veiculos = cursor.fetchall()
        for veiculo in veiculos:
            placa = veiculo[0]
            marca = veiculo[1]
            modelo = veiculo[2]
            tipo = veiculo[3]
            ano = veiculo[4]
            quilometragem = veiculo[5]
            consumo_medio = veiculo[6]
            status = veiculo[7]
            combustivel = veiculo[8]

            if status.lower() == "ativo":
                qtd_ativo += 1
                lista_ativo.append(placa)
            elif status.lower() == "inativo":
                qtd_inativo += 1
                lista_inativo.append(placa)
            elif status.lower() == "manutencao":
                qtd_manutencao += 1
                lista_manutencao.append(placa)

            print(f"Placa: {placa}\nMarca: {marca}\nModelo: {modelo}\nTipo: {tipo}\nAno: {ano}\nQuilometragem: {quilometragem}\nConsumo médio: {consumo_medio}\nStatus: {status}\nCombustível: {combustivel}\n")

        print(f"{qtd_ativo} veículos ativos: {lista_ativo}\n{qtd_inativo} veículos inativos: {lista_inativo}\n{qtd_manutencao} veículos em manutenção: {lista_manutencao}")

    def gerar_custo_manutenção():
        '''Gera um relatório do custo total e médio de manutenção por tipo de veículo.'''
        with open(caminho_json, "r") as f:
            data = json.load(f)
        peso_carro = data["configs"]["manutencoes"]["peso"]["carro"]
        peso_moto = data["configs"]["manutencoes"]["peso"]["moto"]
        peso_caminhao = data["configs"]["manutencoes"]["peso"]["caminhao"]
        custo_corretiva = data["configs"]["manutencoes"]["custo"]["corretiva"]
        custo_preventiva = data["configs"]["manutencoes"]["custo"]["preventiva"]

        print(f"\nCarro:\nCorretiva: {peso_carro * custo_corretiva}\nPreventiva: {peso_carro * custo_preventiva}\n\nMoto:\nCorretiva: {peso_moto * custo_corretiva}\nPreventiva: {peso_moto * custo_preventiva}\n\nCaminhão:\nCorretiva: {peso_caminhao * custo_corretiva}\nPreventiva: {peso_caminhao * custo_preventiva}\n")
        pass

    def gerar_ranking(self):
        '''Gera um relatório do ranking de veículos por eficiência de combustível.'''

        pass

    def gerar_viagens():
        '''Gera um relatório do total de viagens por motorista.'''
        conexao = sqlite3.connect(r"data\dados.db")
        cursor = conexao.cursor()
        num = 0
        cpf = str(input("Digite o CPF do motorista: "))
        motorista = Motorista.ler_motorista(cpf)
        if motorista == None:
            print("O motorista não existe")
        else:
            nome = Motorista.mostrar_motorista(cpf).nome
            cursor.execute('''SELECT * FROM alocacoes''')
            viagens = cursor.fetchall()
            for viagem in viagens:
                if viagem[5] == cpf:
                    num+= 1
            if num > 0:
                print(f"O motorista {nome} tem um total de {num} viagens.\n")
            elif num == 0:
                print(f"O motorista não tem viagens.\n")
        cursor.close()
        conexao.cursor()

    def gerar_quilometragem():
        '''Gera um relatório da quilometragem média por tipo de veículo..'''
        conexao = sqlite3.connect(r"data\dados.db")
        cursor = conexao.cursor()
        num_carro = 0
        num_moto = 0
        num_caminhao = 0
        km_moto = 0
        km_carro = 0
        km_caminhao = 0
        media_carro = 0
        media_moto = 0
        media_caminhao = 0

        cursor.execute('''SELECT * FROM veiculos''')
        veiculos = cursor.fetchall()
        for veiculo in veiculos:
            if veiculo[3] == "carro":
                km_carro += veiculo[5]
                num_carro += 1
            elif veiculo[3] == "moto":
                km_moto += veiculo[5]
                num_moto += 1
            elif veiculo[3] == "caminhao":
                km_caminhao += veiculo[5]
                num_caminhao += 1
        if num_carro > 0:
            media_carro = km_carro / num_carro
        if num_moto > 0:
            media_moto = km_moto / num_moto
        if num_caminhao > 0:
            media_caminhao = km_caminhao / num_caminhao

        print(f"\nMédia carro: {media_carro}\nMédia moto: {media_moto}\nMédia caminhão: {media_caminhao}\n")
            

        pass