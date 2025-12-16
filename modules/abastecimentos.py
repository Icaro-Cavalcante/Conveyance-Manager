import json
import sqlite3
from .veiculos import Veiculo
from datetime import datetime
caminho_json = r"config\settings.json"
database = r"data\dados.db"
gasolina = 6.05
class Abastecimento:
    '''É a classe que cuida do abastecimento dos veículos e do consumo de combustível.'''
    def __init__(self, data, tipo_combustivel, litros, valor, veiculo, id):
        self.data = data
        self.tipo_combustivel = tipo_combustivel
        self.litros = litros
        self.valor = valor
        self.veiculo = veiculo
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

    def __str__(self):
        return f"Data: {self.data}\nTipo de combustível: {self.tipo_combustivel}\nLitros: {self.litros}\nValor: {self.valor}\nID: {self.id}"
    
    def __eq__(self, outro):
        return self.id == outro.id
    
    def tabela_abastecimento():
        '''Cria a tabela de abastecimentos no banco de dados caso ela não exista.'''
        conexao = sqlite3.connect(database)
        cursor = conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS abastecimentos
                       (data TEXT, tipo_combustivel TEXT, litros REAL, valor REAL, veiculo TEXT, ID INTENGER UNIQUE)''')
        
        cursor.close()
        conexao.close()

    def registrar_abastecimento():
        '''Recebe o tipo de combustível, os litros e o veículo e registra o abastecimento no banco de dados.'''
        Abastecimento.tabela_abastecimento()
        agora = datetime.now()
        data = agora.strftime("%d/%m/%Y. Às %H:%M:%S")
        placa = str(input("Qual a placa do veículo que deseja abastecer? "))
        veiculo = Veiculo.ler_veiculo(placa)
        if veiculo == None:
            print("O veículo com essa placa não existe.\n")
        else:
            tipo = str(input("Qual o tipo de combustível? "))
            litros = float(input("Quantos litros vc vai abastecer? "))
            valor = Abastecimento.calcular_valor(litros)
            id = int(input("Qual o id? "))
            novo_abastecimento = Abastecimento(data, tipo, litros, valor, placa, id)

            conexao = sqlite3.connect(database)
            cursor = conexao.cursor()
            cursor.execute('''INSERT OR IGNORE INTO abastecimentos
                           (data, tipo_combustivel, litros, valor, veiculo, id)
                           VALUES (?, ?, ?, ?, ?, ?)''', (novo_abastecimento.data, novo_abastecimento.tipo_combustivel, novo_abastecimento.litros, novo_abastecimento.valor, novo_abastecimento.veiculo, novo_abastecimento.id))
            
            conexao.commit()
            cursor.close()
            conexao.close()
            novo_abastecimento.abastecer_veiculo()
            Abastecimento.atualizar_status(novo_abastecimento.veiculo, False)

    def calcular_consumo(self, veiculo):
        '''Recebe o veiculo, calcula seu consumo médio e retorna o resultado.'''
        # calcular consumo médio por veículo,
        pass

    def consumo_padrao(self, consumo_padrao, consumo_medio):
        # exibir veículos com consumo fora do padrão definido
        '''Recebe o consumo padrão e o consumo médio e exibe se o veículo está com o consumo fora do padrão.'''
        pass

    def calcular_valor(litros):
        '''Recebe a quantidade de litros e calcula o valor a ser pago pelo abastecimento.'''
        Abastecimento.tabela_abastecimento()
        with open(caminho_json, "r") as f:
            dados = json.load(f)
        gasolina = dados["configs"]["abastecimentos"]["valor_gasolina"]
        valor = gasolina * litros
        return valor

    def abastecer_veiculo(self):
        '''Recebe a placa do veículo e os litros para atualizar o combustível do veículo.'''
        combustivel = Veiculo.mostrar_veiculo(self.veiculo).combustivel
        novo_combustivel = self.litros + combustivel
        conexao = sqlite3.connect(database)
        cursor = conexao.cursor()

        cursor.execute('''UPDATE veiculos
                       SET combustivel = ?
                       WHERE placa = ?''', (novo_combustivel, self.veiculo))
        conexao.commit()
        cursor.close()
        conexao.close()

    def atualizar_status(placa, liberar_manutencao):
        veiculo = Veiculo.mostrar_veiculo(placa)
        if liberar_manutencao or veiculo.status != "manutencao":
            combustivel = veiculo.combustivel
            conexao = sqlite3.connect(database)
            cursor = conexao.cursor()

            if combustivel == 0:
                status = "inativo"
            else:
                status = "ativo"
            cursor.execute('''UPDATE veiculos
                        SET status = ?
                        WHERE placa = ?''', (status, placa))
            conexao.commit()
            cursor.close()
            conexao.close()
        else:
            print("O veículo ainda está em manutenção.")

