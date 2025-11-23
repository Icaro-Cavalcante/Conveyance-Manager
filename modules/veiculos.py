veiculos = []

class Veiculo:
    '''É a classe dos veículos.'''
    def __init__(self, placa, marca, modelo, tipo, ano, quilometragem, consumo_medio, status):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.ano = ano
        self.quilometragem = quilometragem
        self.consumo_medio = consumo_medio
        self.status = status

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
    def __init__(self):
        self.veiculo = []

    # CRUD

    def criar_veiculo():
        '''Recebe os dados do veículo e cadastra o motorista no banco de dados.'''
        placa = str(input("Digite a placa do veículo: "))
        marca = str(input("Digite a marca do carro: "))
        modelo = str(input("Digite o modelo do veículo: "))
        tipo = str(input("Digite o tipo do veículo: "))
        ano = str(input("Digite o ano do veículo: "))
        quilometragem = float(input("Digite a quilometragem do veículo: "))
        consumo_medio = float(input("Digite o consumo médio do veículo: "))
        status = str(input("Digite o status do veículo: "))

        novo_veiculo = Veiculo(placa, marca, modelo, tipo, ano, quilometragem, consumo_medio, status)
        veiculos.append(novo_veiculo)
        pass

    def ler_veiculo(placa):
        '''Recebe uma placa e retorna os dados do veículo com essa placa.'''
        for veiculo in veiculos:
            if placa == veiculo.placa:
                print(f"Placa: {veiculo.placa}\nMarca: {veiculo.marca}\nModelo: {veiculo.modelo}\nTipo: {veiculo.tipo}\nQuilometragem: {veiculo.quilometragem}\nConsumo médio: {veiculo.consumo_medio}\nStatus {veiculo.status}")

    def atualizar_veiculo(placa):
        '''Recebe uma placa e atualiza os dados do veículo com essa placa.'''
        pass

    def remover_veiculo(placa):
        '''Recebe uma placa e remove os dados do veículo com essa placa do banco de dados.'''
        pass

    # registar histórico de eventos (entrada, saída, manutenção, abastecimeto, desativação)
    
    def registrar_historico(data, evento):
        '''Recebe a data e o nome do evento e registra o evento no histórico.'''
        pass