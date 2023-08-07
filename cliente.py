class Cliente:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    def imprimir(self):
        print('Nome: ', self.nome)
        print('CPF: ', self.cpf)
        print('Telefone: ', self.telefone)