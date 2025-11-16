class Veiculo:
    def __init__(self, placa, marca, modelo, tipo, ano, quilometragem, consumo_medio, status):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.ano = ano
        self.quilometragem = quilometragem
        self.consumo_medio = consumo_medio
        self.status = status

class Cadastro_veiculos:
    def __init__(self):
        self.veiculo = []

    # CRUD

    def criar_veiculo(self, placa, marca, modelo, tipo, ano, quilometragem, consumo_medio, status):
        pass

    def ler_veiculo(self, placa):
        pass

    def atualizar_veiculo(self, placa):
        pass

    def remover_veiculo(self, placa):
        pass

    # registar histórico de eventos (entrada, saída, manutenção, abastecimeto, desativação)
    
    def registrar_historico(self):
        pass