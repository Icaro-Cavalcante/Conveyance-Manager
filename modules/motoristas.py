motoristas = []

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

    def criar_motorista():
        '''Recebe os dados do motorista e cadastra o motorista no banco de dados.'''
        nome = str(input("Insira o nome do motorista: "))
        cpf = int(input("Insira o CPF do motorista: "))
        cnh = str(input("Insira a categoria da cnh do motorista: "))
        experiencia = str(input("Insira a experiencia do motorista: "))
        disponibilidade = str(input("Insira a disponibilidade do motorista: "))
        historico = str(input("Insira o histórico do motorista: "))
        novo_motorista = Motorista(nome, cpf, cnh, experiencia, disponibilidade, historico)
        motoristas.append(novo_motorista)
        print("\nMotorista cadastrado\n")

    def ler_motorista(outro_cpf):
        '''Recebe um CPF e retorna os dados do motorista com esse CPF.'''
        for motorista in motoristas:
            if motorista.cpf == outro_cpf:
                print(motorista)

    def atualizar_motorista(outro_cpf, atributo):
        '''Recebe um CPF e atualiza os dados do motorista com esse CPF.'''
        for motorista in motoristas:
            if motorista.cpf == outro_cpf:
                update = motorista
                if atributo == 1:
                    novo_nome = str(input("Digite o novo nome: "))
                    update.nome = novo_nome
                elif atributo == 2:
                    nova_cnh = str(input("Digite a nova CNH: "))
                    update.categoria_cnh = nova_cnh
                elif atributo == 3:
                    nova_experiencia = str(input("Digite a nova experiência: "))
                    update.experiencia = nova_experiencia
                elif atributo == 4:
                    nova_disponibilidade = str(input("Digite a nova disponibilidade: "))
                    update.disponibilidade = nova_disponibilidade
                elif atributo == 5:
                    novo_historico = str(input("Digite a novo histórico: "))
                    update.historico = novo_historico
                print("\nAtributo editado.\n")

    def remover_motorista(outro_cpf):
        '''Recebe um CPF e remove o motorista com esse CPF do banco de dados.'''
        for motorista in motoristas:
            if motorista.cpf == outro_cpf:
                remove = motorista
                index = motoristas.index(remove)
                motoristas.pop(index)
                print("\nMotorista removido\n")

        pass

    # Validação automática (só pode dirigir veiculos compatíveis com sua categoria)

    def validar(self, categoria_cnh, tipo_veiculo):
        '''Recebe a categoria da CNH e o tipo de veículo e valida se o veículo é compatível com a CNH.'''
        pass