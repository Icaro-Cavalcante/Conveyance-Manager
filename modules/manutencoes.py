import json
import sqlite3
from .veiculos import *
from datetime import datetime
from .abastecimentos import Abastecimento
caminho_json = r"config\settings.json"
data_veiculos = r"data\veiculos.db"
data_manutencao = r"data\manutencoes.db"

class Manutencoes:
    '''É a classe que cuida da manutenção de veículos.'''
    def __init__(self, data, tipo, custo, descricao, id):
        self._data = data
        self.tipo = tipo # (preventiva, corretiva)
        self.custo = custo
        self.descricao = descricao
        self.__id = id

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, novo_id):
        if type(novo_id) is int:
            self.__id = novo_id
        else:
            print("ID inválido.")

    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, nova_data):
        self._data = nova_data

    def __str__(self):
        return f"Data: {self.data}\nTipo: {self.tipo}\nCusto: {self.custo}\nDescrição: {self.descricao}\nID: {self.id}\n"
    
    def __eq__(self, outro):
        return self.id == outro.id
    
    def ler_manutencao(id):
        '''Recebe o ID e retorna os dados da manutenção'''
        Manutencoes.tabela_manutencao()
        conexao = sqlite3.connect(data_manutencao)
        cursor = conexao.cursor()
        cursor.execute('''SELECT * FROM manutencoes where id = ?''', (id,))

        manutencao = cursor.fetchone()
        cursor.close()
        conexao.close()
        return manutencao

    def consultar_manutenao(id):
        '''Recebe o ID e mostra os dados da manutenção'''
        dados = Manutencoes.ler_manutencao(id)
        if dados == None:
            print("Não existe uma manutenção com esse ID.")
        else:
            data = dados[0]
            tipo = dados[1]
            custo = dados[2]
            descricao = dados[3]
            outro_id = dados[4]

            manutencao = Manutencoes(data, tipo, custo, descricao, outro_id)
            print(manutencao)
    
    def tabela_manutencao():
        '''Cria a tabela manutenção no banco de dados, caso ela não exista.'''
        conexao = sqlite3.connect(data_manutencao)
        cursor = conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS manutencoes
                       (data TEXT, tipo TEXT, custo REAL, descricao TEXT, id INTENGER)''')
        conexao.commit()
        cursor.close()
        conexao.close()

    def calcular_custo(tipo, tipo_veiculo):
        '''Recebe o tipo de manutenção e de veículo, calcula o custo e retorna o resultado.'''
        tipo_veiculo = tipo_veiculo.lower()
        with open(caminho_json, "r") as f:
            data = json.load(f)
        peso = data["configs"]["manutencoes"]["peso"][tipo_veiculo]
        custo = data["configs"]["manutencoes"]["custo"][tipo]
        custo_total = peso * custo
        return custo_total

    # permitir marcar veículo como em manutenção e liberá-lo ao concluir o serviço

    def marcar_veiculo(placa_veiculo):
        '''Recebe a placa do veículo e altera seu status para (manutencao).'''
        conexao = sqlite3.connect(data_veiculos)
        cursor = conexao.cursor()
        veiculo = Cadastro_veiculos.ler_veiculo(placa_veiculo)
        if veiculo == None:
            print("O veículo com essa placa não existe")
        else:
            cursor.execute('''UPDATE veiculos
                           SET status = ?
                           WHERE placa = ?''', ("manutencao", placa_veiculo))
            print("O veículo agora está em manutenção.\n")

        conexao.commit()
        cursor.close()
        conexao.close()

    def liberar_veiculo(placa_veiculo):
        '''Recebe o veículo e altera seu status para (ativo).'''
        conexao = sqlite3.connect(data_veiculos)
        cursor = conexao.cursor()
        veiculo = Cadastro_veiculos.ler_veiculo(placa_veiculo)
        if veiculo == None:
            print("O veículo com essa placa não existe")
        elif veiculo[7] == "inativo" or veiculo[7] == "ativo":
            print("O veículo informado não está em manutenção.")
        else:
            Abastecimento.atualizar_status(placa_veiculo, True)
            print("O veículo agora saiu da manutenção.\n")

        conexao.commit()
        cursor.close()
        conexao.close()

    def registrar_manutencao(placa_veiculo):
        '''Recebe a placa do veículo da manutenção e registra ela no banco de dados.'''
        Manutencoes.tabela_manutencao()
        veiculo = Cadastro_veiculos.ler_veiculo(placa_veiculo)
        if veiculo == None:
            print("O veículo com essa placa não existe.")
        else:
            conexao = sqlite3.connect(data_manutencao)
            cursor = conexao.cursor()
            agora = datetime.now()
            data = agora.strftime("%d/%m/%Y. Às %H:%M:%S")
            tipo = str(input("Informe se a manutenção é preventiva ou corretiva: "))
            tipo_veiculo = veiculo[3]
            descricao = str(input("Qual a descrição da manutenção? "))
            custo = Manutencoes.calcular_custo(tipo, tipo_veiculo)
            id = int(input("Qual o id da manutenção? "))

            manutencao = Manutencoes(data, tipo, custo, descricao, id)
            cursor.execute('''INSERT OR IGNORE INTO manutencoes
                           (data, tipo, custo, descricao, id)
                           VALUES (?, ?, ?, ?, ?)''', (manutencao.data,
                            manutencao.tipo, manutencao.custo, manutencao.descricao, manutencao.id))
            Manutencoes.marcar_veiculo(placa_veiculo)
            conexao.commit()
            cursor.close()
            conexao.close()
            

    def associar_veiculo(self, veiculo):
        '''Recebe um veículo, associa a manutenção a ele e armazena no histórico.'''
        # Associar a um veículo e armazenar no histórico.
        pass
