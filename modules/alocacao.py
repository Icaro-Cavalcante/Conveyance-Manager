from .veiculos import *
from .motoristas import *
import sqlite3
from datetime import datetime
from .abastecimentos import Abastecimento
database = r"data\dados.db"
class Alocacao():
    '''É a classe que cuida da alocação de veículos a motoristas e da quilometragem do veículo.'''
    def __init__(self, origem, destino, data, distancia, id, motorista, veiculo):
        self.origem = origem
        self.__destino = destino
        self.data = data
        self.distancia = distancia
        self.id = id
        self.motorista = motorista
        self.veiculo = veiculo

    @property
    def destino(self):
        return self.__destino
    @destino.setter
    def destino(self, novo_destino):
        if type(novo_destino) is str:
            self.__destino = novo_destino
        else:
            print("Destino inválido")

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
        return f"Origem: {self.origem}\nDestino: {self.destino}\nDistância: {self.distancia}\n"
    
    def __eq__(self, outro):
        return self.id == outro.id
    
    def tabela_alocacao():
        '''Cria a tabela das alocações no banco de dados'''
        conexao = sqlite3.connect(database)
        cursor = conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS
                       alocacoes (origem TEXT, destino TEXT, data TEXT, distancia REAL, id INTENGER, motorista TEXT, veiculo TEXT)''')
        
        conexao.commit()
        cursor.close()
        conexao.close()

    def associar_registrar():
        '''Recebe origem, destino, distância, placa do veículo e CPF do motorista e associa o veículo a um motorista e registra a viagem.'''
        Alocacao.tabela_alocacao()
        placa = str(input("Digite a placa do veiculo: "))
        Abastecimento.atualizar_status(placa, False)
        permissao = Alocacao.permissao_alocacao(placa)

        if permissao == False:
            print("Alocação negada. O veículo está inativo ou em manutenção.")
        elif permissao:
            cpf = str(input("Digite o CPF do motorista: "))
            existe = Motorista.ler_motorista(cpf)
            if existe == None:
                print("Um motorista com esse CPF não existe.")
            else:
                motorista = Motorista.mostrar_motorista(cpf).cpf
                veiculo = Veiculo.mostrar_veiculo(placa).placa
                origem = str(input("Digite a origem: "))
                destino = str(input("Digite o destino: "))
                distancia = float(input("Digite a distancia: "))
                agora = datetime.now()
                data = agora.strftime("%d/%m/%Y. Às %H:%M:%S.")
                id = int(input("Digite o ID: "))
                nova_alocacao = Alocacao(origem, destino, data, distancia, id, motorista, veiculo)
                e_valido = nova_alocacao.validar_cnh()
                combustivel_validado = nova_alocacao.validar_combustivel()

                if e_valido == False:
                    print("A categoria da CNH é incompatível com o Veículo.")
                elif combustivel_validado == False:
                    print("Não há combustível suficiente para realizar essa viagem.")
                else:
                    conexao = sqlite3.connect(database)
                    cursor = conexao.cursor()
                    cursor.execute('''INSERT OR IGNORE INTO alocacoes
                                (origem, destino, data, distancia, id, motorista, veiculo)
                                VALUES (?, ?, ?, ?, ?, ?, ?)''', (nova_alocacao.origem, nova_alocacao.destino, nova_alocacao.data, nova_alocacao.distancia, nova_alocacao.id, nova_alocacao.motorista, nova_alocacao.veiculo))
                    
                    conexao.commit()
                    nova_alocacao.atualizar_quilometragem()
                    cursor.close()
                    conexao.close()
                    print("\nAlocação registrada.\n")
                
    def atualizar_quilometragem(self):
        '''Recebe a distancia da viagem, a placa do veiculo e atualiza a quilometragem do veículo após a viagem.'''
        # Atualizar quilometragem automaticamente após cada viagem.
        outro_veiculo = Veiculo.ler_veiculo(self.veiculo)
        if outro_veiculo == None:
            print("O veículo com essa placa não existe.")
        else:
            quilometragem = float(outro_veiculo[5])
            nova_quilometragem = quilometragem + self.distancia
            conexao = sqlite3.connect(database)
            cursor = conexao.cursor()
            cursor.execute('''UPDATE veiculos
                           SET quilometragem = ?
                           WHERE placa = ?''', (nova_quilometragem, self.veiculo))
            
            conexao.commit()
            cursor.close()
            conexao.close()


    def permissao_alocacao(placa):
        '''Recebe a placa do veículo e caso esteja em manutenção ou inativo, bloqueia a alocação. Do contrário, permite.'''
        veiculo = Veiculo.ler_veiculo(placa)
        if veiculo == None:
            print("O veículo com essa placa não existe.")
        else:
            status = veiculo[7]
            if status == "inativo" or status == "manutencao":
                permitido = False
            else:
                permitido = True
            return permitido
        
    def validar_cnh(self):
        cnh = Motorista.mostrar_motorista(self.motorista).categoria_cnh
        tipo = Veiculo.mostrar_veiculo(self.veiculo).tipo

        if cnh.upper() == "A" and tipo.lower() == "moto":
            valido = True
        elif cnh.upper() == "B" and tipo.lower() == "carro":
            valido = True
        elif cnh.upper() == "C" and tipo.lower() == "caminhao":
            valido = True
        else:
            valido = False
        return valido
    
    def validar_combustivel(self):
        veiculo = Veiculo.mostrar_veiculo(self.veiculo)
        quilometros_possiveis = veiculo.consumo_medio * veiculo.combustivel
        if quilometros_possiveis < self.distancia:
            combustivel_validado = False
        else:
            combustivel_validado = True
        return combustivel_validado
