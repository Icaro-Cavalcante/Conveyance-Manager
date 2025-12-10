import sqlite3
database = r"data\dados.db"

class Veiculo:
    '''É a classe dos veículos.'''
    def __init__(self, placa, marca, modelo, tipo, ano, quilometragem, consumo_medio, status, combustivel):
        self.__placa = placa
        self.marca = marca
        self._modelo = modelo
        self.tipo = tipo
        self.ano = ano
        self.quilometragem = quilometragem
        self.consumo_medio = consumo_medio
        self.status = status
        self.combustivel = combustivel

    @property
    def placa(self):
        return self.__placa
    
    @placa.setter
    def modelo(self, nova_placa):
        if type(nova_placa) is str and len(nova_placa) > 0:
            self.__placa = nova_placa
        else:
            print("Placa inválida.")
    
    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, novo_modelo):
        if type(novo_modelo) is str and len(novo_modelo) > 0:
            self._modelo = novo_modelo
        else:
            print("Modelo inválido.")

    def __str__(self):
        return f"Placa: {self.placa}\nMarca: {self.marca}\nModelo: {self._modelo}\nTipo: {self.tipo}\nAno: {self.ano}\nQuilometragem: {self.quilometragem}\nConsumo médio: {self.consumo_medio}\nStatus: {self.status}\nCombustível: {self.combustivel}\n"
    
    def __eq__(self, outro):
        return self.modelo == outro.modelo

class Moto(Veiculo):
    '''É a classe das motos.'''
    pass

class Caminhao(Veiculo):
    '''É a classe dos caminhões.'''
    pass

class Carro(Veiculo):
    '''É a classe dos carros.'''
    pass

class Cadastro_veiculos:
    '''É a classe que cuida do CRUD dos veículos.'''
    # CRUD

    def tabela_veiculos():
        conexao = sqlite3.connect(database)
        cursor = conexao.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS veiculos(placa TEXT UNIQUE, marca TEXT, modelo TEXT, tipo TEXT, ano INTERGER, quilometragem REAL, consumo_medio REAL, status TEXT, combustivel REAL)           
        ''')

        conexao.commit()
        cursor.close()
        conexao.close()

    def criar_veiculo():
        '''Recebe os dados do veículo e cadastra o motorista no banco de dados.'''
        placa = str(input("Digite a placa do veículo: "))
        marca = str(input("Digite a marca do veículo: "))
        modelo = str(input("Digite o modelo do veículo: "))
        tipo = str(input("Digite o tipo do veículo: "))
        ano = str(input("Digite o ano do veículo: "))
        quilometragem = float(input("Digite a quilometragem do veículo: "))
        consumo_medio = float(input("Digite o consumo médio do veículo: "))
        status = str(input("Digite o status do veículo: "))
        combustivel = str(input("Digite o combustivel do veículo: "))

        Cadastro_veiculos.tabela_veiculos()
        conexao = sqlite3.connect(database)
        cursor = conexao.cursor()
        novo_veiculo = Veiculo(placa, marca, modelo, tipo, ano, quilometragem, consumo_medio, status, combustivel)
        cursor.execute('''
        INSERT OR IGNORE INTO veiculos (placa, marca, modelo, tipo, ano, quilometragem, consumo_medio, status, combustivel) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (novo_veiculo.placa, novo_veiculo.marca, novo_veiculo.modelo, novo_veiculo.tipo, novo_veiculo.ano, novo_veiculo.quilometragem, novo_veiculo.consumo_medio, novo_veiculo.status, novo_veiculo.combustivel))

        conexao.commit()
        cursor.close()
        conexao.close()
        
        print("Veículo Criado\n")

    def ler_veiculo(placa):
        '''Recebe uma placa e retorna os dados do veículo com essa placa.'''
        Cadastro_veiculos.tabela_veiculos()
        conexao = sqlite3.connect(database)
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM veiculos WHERE placa = ?', (placa,))
        veiculo = cursor.fetchone()

        cursor.close()
        conexao.close()
        return veiculo

    def mostrar_veiculo(placa):
        '''Recebe uma placa e mostra os dados do veículo com essa placa.'''
        atributos = Cadastro_veiculos.ler_veiculo(placa)
        if atributos == None:
            print("O veículo com essa placa não existe.\n")
        else:
            outra_placa = atributos[0]
            marca = atributos[1]
            modelo = atributos[2]
            tipo = atributos[3]
            ano = atributos[4]
            quilometragem = atributos[5]
            consumo_medio = atributos[6]
            status = atributos[7]
            combustivel = atributos[8]

            veiculo = Veiculo(outra_placa, marca, modelo, tipo, ano, quilometragem, consumo_medio, status, combustivel)
            return veiculo

    def atualizar_veiculo(outra_placa, atributo):
        '''Recebe uma placa e atualiza os dados do veículo com essa placa.'''
        veiculo = Cadastro_veiculos.ler_veiculo(outra_placa)
        if veiculo == None:
            print("O veículo com essa placa não existe.\n")
        else:
            conexao = sqlite3.connect(database)
            cursor = conexao.cursor()
            if atributo == 1:
                nova_marca = str(input("Digite a nova marca: "))
                cursor.execute('''UPDATE veiculos
                            SET marca = ?
                            WHERE placa = ?''', (nova_marca, outra_placa))
            elif atributo == 2:
                novo_modelo = str(input("Digite o novo modelo: "))
                cursor.execute('''UPDATE veiculos
                            SET modelo = ?
                            WHERE placa = ?''', (novo_modelo, outra_placa))
            elif atributo == 3:
                novo_tipo = str(input("Digite o novo tipo: "))
                cursor.execute('''UPDATE veiculos
                            SET tipo = ?
                            WHERE placa = ?''', (novo_tipo, outra_placa))
            elif atributo == 4:
                novo_ano = int(input("Digite o novo ano: "))
                cursor.execute('''UPDATE veiculos
                            SET ano = ?
                            WHERE placa = ?''', (novo_ano, outra_placa))
            elif atributo == 5:
                nova_quilometragem = float(input("Digite a nova quilometragem: "))
                cursor.execute('''UPDATE veiculos
                            SET quilometragem = ?
                            WHERE placa = ?''', (nova_quilometragem, outra_placa))
            elif atributo == 6:
                novo_consumo = float(input("Digite o novo consumo médio: "))
                cursor.execute('''UPDATE veiculos
                            SET consumo_medio = ?
                            WHERE placa = ?''', (novo_consumo, outra_placa))
            elif atributo == 7:
                novo_status = str(input("Digite o novo status: "))
                cursor.execute('''UPDATE veiculos
                            SET status = ?
                            WHERE placa = ?''', (novo_status, outra_placa))
            elif atributo == 8:
                novo_combustivel = str(input("Digite o novo combustivel: "))
                cursor.execute('''UPDATE veiculos
                            SET combustivel = ?
                            WHERE placa = ?''', (novo_combustivel, outra_placa))
            conexao.commit()
            cursor.close()
            conexao.close()
            print("\nAtributo editado.\n")

    def remover_veiculo(placa):
        '''Recebe uma placa e remove os dados do veículo com essa placa do banco de dados.'''
        veiculo = Cadastro_veiculos.ler_veiculo(placa)
        if veiculo == None:
            print("O veículo com essa placa não existe.\n")
        else:
            conexao = sqlite3.connect(database)
            cursor = conexao.cursor()
            cursor.execute('''DELETE FROM veiculos
                        WHERE placa = ?''', (placa,))
            
            conexao.commit()
            cursor.close()
            conexao.close()

            print(f"\nVeículo com placa {placa} removido\n")

    # registar histórico de eventos (entrada, saída, manutenção, abastecimeto, desativação)
    
    def registrar_historico(data, evento):
        '''Recebe a data e o nome do evento e registra o evento no histórico.'''
        pass