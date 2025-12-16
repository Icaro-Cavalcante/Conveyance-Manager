import sqlite3
database = r"data\dados.db"


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

    def tabela_motoristas():
        conexao = sqlite3.connect(database)
        cursor = conexao.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS motoristas(nome TEXT, cpf TEXT UNIQUE, categoria_cnh TEXT, experiencia TEXT, disponibilidade TEXT, historico TEXT)''')

        cursor.close()
        conexao.close()

    def criar_motorista():
        '''Recebe os dados do motorista e cadastra o motorista no banco de dados.'''
        Motorista.tabela_motoristas()
        nome = str(input("Insira o nome do motorista: "))
        cpf = str(input("Insira o CPF do motorista: "))
        cnh = str(input("Insira a categoria da cnh do motorista: "))
        experiencia = str(input("Insira a experiencia do motorista: "))
        disponibilidade = str(input("Insira a disponibilidade do motorista: "))
        historico = str(input("Insira o histórico do motorista: "))
        novo_motorista = Motorista(nome, cpf, cnh, experiencia, disponibilidade, historico)
        
        conexao = sqlite3.connect(database)
        cursor = conexao.cursor()
        cursor.execute('''INSERT OR IGNORE INTO motoristas (nome, cpf, categoria_cnh, experiencia, disponibilidade, historico) VALUES (?, ?, ?, ?, ?, ?)''', (novo_motorista.nome, novo_motorista.cpf, novo_motorista.categoria_cnh, novo_motorista.experiencia, novo_motorista.disponibilidade, novo_motorista.historico))

        conexao.commit()
        cursor.close()
        conexao.close()
        print("\nMotorista cadastrado\n")

    def ler_motorista(outro_cpf):
        '''Recebe um CPF e retorna os dados do motorista com esse CPF.'''
        Motorista.tabela_motoristas()
        conexao = sqlite3.connect(database)
        cursor = conexao.cursor()
        cursor.execute('''SELECT * FROM motoristas WHERE cpf = ?''', (outro_cpf,))
        motorista = cursor.fetchone()

        cursor.close()
        conexao.close()
        return motorista
    
    def mostrar_motorista(outro_cpf):
        '''Recebe um CPF e mostra os dados do motorista com esse CPF.'''
        dados = Motorista.ler_motorista(outro_cpf)
        if dados == None:
            print("O motorista com esse CPF não existe.\n")
        else:
            nome = dados[0]
            cpf = dados[1]
            cnh = dados[2]
            experiencia = dados[3]
            disponibilidade = dados[4]
            historico = dados[5]

            motorista = Motorista(nome, cpf, cnh, experiencia, disponibilidade, historico)
            return motorista
        

    def atualizar_motorista(outro_cpf, atributo):
        '''Recebe um CPF e atualiza os dados do motorista com esse CPF.'''
        motorista = Motorista.ler_motorista(outro_cpf)
        if motorista == None:
            print("O motorista com esse CPF não existe.\n")
        else:
            conexao = sqlite3.connect(database)
            cursor = conexao.cursor()
            if atributo == 1:
                novo_nome = str(input("Digite o novo nome: "))
                cursor.execute('''UPDATE motoristas
                               SET nome = ?
                               WHERE cpf = ?''', (novo_nome, outro_cpf))
            elif atributo == 2:
                nova_cnh = str(input("Digite a nova CNH: "))
                cursor.execute('''UPDATE motoristas
                               SET categoria_cnh = ?
                               WHERE cpf = ?''', (nova_cnh, outro_cpf))
            elif atributo == 3:
                nova_experiencia = str(input("Digite a nova experiência: "))
                cursor.execute('''UPDATE motoristas
                               SET experiencia = ?
                               WHERE cpf = ?''', (nova_experiencia, outro_cpf))
            elif atributo == 4:
                nova_disponibilidade = str(input("Digite a nova disponibilidade: "))
                cursor.execute('''UPDATE motoristas
                               SET disponibiidade = ?
                               WHERE cpf = ?''', (nova_disponibilidade, outro_cpf))
            elif atributo == 5:
                novo_historico = str(input("Digite a novo histórico: "))
                
                cursor.execute('''UPDATE motoristas
                               SET historico = ?
                               WHERE cpf = ?''', (novo_historico, outro_cpf))
                
            conexao.commit()
            cursor.close()
            conexao.close()
            print("\nAtributo editado.\n")

    def remover_motorista(outro_cpf):
        '''Recebe um CPF e remove o motorista com esse CPF do banco de dados.'''
        motorista = Motorista.ler_motorista(outro_cpf)
        if motorista == None:
            print("O motorista com esse cpf não existe.\n")
        else:
            conexao = sqlite3.connect(database)
            cursor = conexao.cursor()
            cursor.execute('''DELETE from motoristas
                           WHERE cpf = ?''', (outro_cpf,))
            
            conexao.commit()
            cursor.close()
            conexao.close()
            print("\nMotorista deletado.\n")
