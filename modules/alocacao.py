class Alocacao():
    def __init__(self, origem, destino, distancia):
        self.origem = origem
        self.destino = destino
        self.distancia = distancia

    def associar_registrar(self, origem, destino, distancia, veiculo, motorista):
        '''Recebe origem, destino, distância, veiculo e motorista e associa o veículo a um motorista e registra a viagem.'''
        # Associar veículo a um motorista e registrar viagem: origem, destino, distância percorrida.
        pass

    def atualizar_quilometragem(self, distancia, veiculo):
        '''Recebe a distancia da viagem, a quilometragem do veiculo e atualiza a quilometragem do veículo após a viagem.'''
        # Atualizar quilometragem automaticamente após cada viagem.
        pass

    def bloquear_alocacao(self, status_veiculo):
        '''Recebe o status do veículo e caso esteja em manutenção ou inativo, bloqueia a alocação.'''
        # Bloquear alocação se o veículo estiver em manutenção ou inativo.
        pass

