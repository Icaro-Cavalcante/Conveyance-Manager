class Manutencoes:
    def __init__(self, data, tipo, descricao):
        self.data = data
        self.tipo = tipo # (preventiva, corretiva)
        self.custo = self.calcular_custo()
        self.descricao = descricao

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
