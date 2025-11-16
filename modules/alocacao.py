class Alocacao():
    def __init__(self, origem, destino, distancia):
        self.origem = origem
        self.destino = destino
        self.distancia = distancia

    def associar_registrar(self, origem, destino, distancia):
        # Associar veículo a um motorista e registrar viagem: origem, destino, distância percorrida.
        pass

    def atualizar_quilometragem(self):
        # Atualizar quilometragem automaticamente após cada viagem.
        pass

    def bloquear_alocacao(self, status_veiculo):
        # Bloquear alocação se o veículo estiver em manutenção ou inativo.
        pass

