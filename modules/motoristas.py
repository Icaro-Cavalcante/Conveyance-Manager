class Motorista:
    def __init__(self, nome, cpf, categoria_cnh, experiencia, disponibilidade, historico):
        self.nome = nome
        self.cpf = cpf
        self.categoria_cnh = categoria_cnh
        self.experiencia = experiencia
        self.disponibilidade = disponibilidade
        self.historico = historico

class Cadastro_motorista:
    def __init__(self):
        self.motorista = []

    # CRUD

    def criar_motorista(self, nome, cpf, categoria_cnh, experiencia, disponibilidade, historico):
        pass

    def ler_motorista(self, cpf):
        pass

    def atualizar_motorista(self, cpf):
        pass

    def remover_motorista(self, cpf):
        pass

    # Validação automática (só pode dirigir veiculos compatíveis com sua categoria)

    def validar(self, categoria_cnh, tipo_veiculo):
        pass