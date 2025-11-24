class Motorista:
    '''É a classe dos motoristas.'''
    def __init__(self, nome, cpf, categoria_cnh, experiencia, disponibilidade, historico):
        self.nome = nome
        self.__cpf = cpf
        self.categoria_cnh = categoria_cnh
        self.experiencia = experiencia
        self.disponibilidade = disponibilidade
        self.historico = historico

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, novo_cpf):
        if len(novo_cpf) == 11:
            self.__cpf = novo_cpf
        else:
            print("CPF inválido.")

    def __str__(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nCategoia da CNH: {self.categoria_cnh}\nExperiência: {self.experiencia}\nDisponibilidade: {self.disponibilidade}\nHistórico: {self.historico}\n"
    
    def __eq__(self, outro):
        return self.nome == outro.nome

class Cadastro_motorista:
    '''É a classe que cuida do CRUD dos motoristas.'''
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