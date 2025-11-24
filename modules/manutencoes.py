class Manutencoes:
    '''É a classe que cuida da manutenção de veículos.'''
    def __init__(self, data, tipo, descricao, id):
        self._data = data
        self.tipo = tipo # (preventiva, corretiva)
        self.custo = self.calcular_custo()
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

    def calcular_custo(self, tipo_veiculo):
        '''Recebe o tipo de veículo, calcula o custo e retorna o resultado.'''
        # calcular custo médio de manutenção por tipo de veículo
        pass

    # permitir marcar veículo como em manutenção e liberá-lo ao concluir o serviço

    def marcar_veiculo(self, veiculo):
        '''Recebe o veículo e altera seu status para (manutencao).'''
        pass

    def liberar_veiculo(self,veiculo):
        '''Recebe o veículo e altera seu status para (ativo).'''
        pass

    def registrar_manutencao(self, data, tipo, custo, descricao):
        '''Recebe a data, o tipo, o custo e descrição da manutenção e registra ela no banco de dados.'''
        pass

    def associar_veiculo(self, veiculo):
        '''Recebe um veículo, associa a manutenção a ele e armazena no histórico.'''
        # Associar a um veículo e armazenar no histórico.
        pass
