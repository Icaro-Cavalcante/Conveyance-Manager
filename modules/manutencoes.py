class Manutencoes:
    def __init__(self, data, tipo, descricao):
        self.data = data
        self.tipo = tipo # (preventiva, corretiva)
        self.custo = self.calcular_custo()
        self.descricao = descricao

    def calcular_custo(self, tipo_veiculo):
        # calcular custo médio de manutenção por tipo de veículo
        pass

    def marcar_veiculo(self, veiculo):
        # permitir marcar veículo como em manutenção e liberá-lo ao concluir o serviço
        pass

    def registrar_manutencao(self, data, tipo, custo, descricao):
        pass

    def associar_veiculo(self, veiculo):
        # Associar a um veículo e armazenar no histórico.
        pass
