class Alocacao():
    '''É a classe que cuida da alocação de veículos a motoristas e da quilometragem do veículo.'''
    def __init__(self, origem, destino, distancia, id):
        self.origem = origem
        self.__destino = destino
        self.distancia = distancia
        self.id = id

    @property
    def destino(self):
        return self.__destino
    @destino.setter
    def destino(self, novo_destino):
        if type(novo_destino) is str:
            self.__destino = novo_destino
        else:
            print("Destino inválido")

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
        return f"Origem: {self.origem}\nDestino: {self.destino}\nDistância: {self.distancia}\n"
    
    def __eq__(self, outro):
        return self.id == outro.id

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

