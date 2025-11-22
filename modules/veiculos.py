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

bis = Moto("05", "HGHG6745", "Chevrolet", "bis", "CNHA", "78", "12km/l", "ativo")

print(bis.status)

class Cadastro_veiculos:
    '''É a classe que cuida do CRUD dos veículos.'''
    def __init__(self):
        self.veiculo = []

    # CRUD

    def criar_veiculo(self, placa, marca, modelo, tipo, ano, quilometragem, consumo_medio, status):
        '''Recebe os dados do veículo e cadastra o motorista no banco de dados.'''
        pass

    def ler_veiculo(self, placa):
        '''Recebe uma placa e retorna os dados do veículo com essa placa.'''
        pass

    def atualizar_veiculo(self, placa):
        '''Recebe uma placa e atualiza os dados do veículo com essa placa.'''
        pass

    def remover_veiculo(self, placa):
        '''Recebe uma placa e remove os dados do veículo com essa placa do banco de dados.'''
        pass

    # registar histórico de eventos (entrada, saída, manutenção, abastecimeto, desativação)
    
    def registrar_historico(self, data, evento):
        '''Recebe a data e o nome do evento e registra o evento no histórico.'''
        pass