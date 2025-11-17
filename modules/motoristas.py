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
        '''Recebe os dados do motorista e cadastra o motorista no banco de dados.'''
        pass

    def ler_motorista(self, cpf):
        '''Recebe um CPF e retorna os dados do motorista com esse CPF.'''
        pass

    def atualizar_motorista(self, cpf):
        '''Recebe um CPF e atualiza os dados do motorista com esse CPF.'''
        pass

    def remover_motorista(self, cpf):
        '''Recebe um CPF e remove o motorista com esse CPF do banco de dados.'''
        pass

    # Validação automática (só pode dirigir veiculos compatíveis com sua categoria)

    def validar(self, categoria_cnh, tipo_veiculo):
        '''Recebe a categoria da CNH e o tipo de veículo e valida se o veículo é compatível com a CNH.'''
        pass