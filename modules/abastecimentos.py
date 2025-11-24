class Abastecimento:
    '''É a classe que cuida do abastecimento dos veículos e do consumo de combustível.'''
    def __init__(self, data, tipo_combustivel, litros, valor, id):
        self._data = data
        self.tipo_combustivel = tipo_combustivel
        self.litros = litros
        self.valor = valor
        self.id = id

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

    def registrar_abastecimento(self, data, tipo_combustivel, litros, valor):
        '''Recebe a data, o tipo de combustível, os litros e o valor pago e registra o abastecimento no banco de dados.'''
        # Registrar abastecimentos (data, tipo de combustível, litros, valor pago.)
        pass

    def calcular_consumo(self, veiculo):
        '''Recebe o veiculo, calcula seu consumo médio e retorna o resultado.'''
        # calcular consumo médio por veículo,
        pass

    def consumo_padrao(self, consumo_padrao, consumo_medio):
        # exibir veículos com consumo fora do padrão definido
        '''Recebe o consumo padrão e o consumo médio e exibe se o veículo está com o consumo fora do padrão.'''
        pass