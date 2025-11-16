class Abastecimento:
    def __init__(self, data, tipo_combustivel, litros, valor):
        self.data = data
        self.tipo_combustivel = tipo_combustivel
        self.litros = litros
        self.valor = valor

    def registrar_abastecimento(self, data, tipo_combustivel, litros, valor):
        # Registrar abastecimentos (data, tipo de combustível, litros, valor pago.)
        pass

    def calcular_consumo(self, veiculo):
        # calcular consumo médio por veículo,
        pass

    def consumo_padrao(self, veiculo):
        # exibir veículos com consumo fora do padrão definido
        pass