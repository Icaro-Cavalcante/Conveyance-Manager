import sqlite3
data_veiculos = r"data\veiculos.db"
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

    def gerar_custo_manutenção(self):
        '''Gera um relatório do custo total e médio de manutenção por tipo de veículo.'''

        pass

    def gerar_ranking(self):
        '''Gera um relatório do ranking de veículos por eficiência de combustível.'''

        pass

    def gerar_viagens(self):
        '''Gera um relatório do total de viagens por motorista.'''

        pass

    def gerar_quilometragem(self):
        '''Gera um relatório da quilometragem média por tipo de veículo..'''

        pass