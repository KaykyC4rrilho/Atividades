import sqlite3
conexao= sqlite3.connect("produtos.db")
cursor = conexao.cursor()
cursor.execute('''

    create table produt (
        nome text, 
        preco float)



''')


print("Bem vindo ao estoque Cp2!")
nome= input("Qual seu nome?")

print("Muito Obrigado por sua presença", nome)
inserir= input(" Você deseja inserir produtos no nosso estoque?(S/s ou N)")

controlador = 0

while inserir == "S" or inserir == "s":
    nProduto= input("Nome do produto:\n")
    precoP= float(input("Preço do Produto: \n "))
    cursor.execute('''
    insert into produt (nome, preco) values(?,?)
    ''', (nProduto, precoP))
    print("Os produtos foram cadastrados com sucesso!")
    inserir = input(" Você deseja inserir mais produtos no nosso estoque?(S/s ou N)")
    conexao.commit()

escolha= input("Deseja consultar os produtos inseridos? s/n ")
while escolha == "s":

    escolha2= input(" Suas opções de consulta:\n 1- Consultar produtos pelo nome\n 2- Consultar produtos pelos preços\n 3- Sair\n")
    if escolha2 == "1" :
        nomeProcurar = input("Digite o nome do produto:\t")
        cursor.execute("select * from produt where nome = ?", (nomeProcurar))
        while True:
            resultado= cursor.fetchone()
            if resultado is None:
                if controlador==0:
                    print("nada foi encontrado")
                break
            else:
                controlador+= 1
                print("Nome{}\n Preço{}".format(resultado[0], resultado[1]))

    elif escolha2 == "2":
        precomin = input("Digite o preço minimo do produto:\t")
        precomax = input("Digite o preço maximo  do produto:\t")

        cursor.execute("select * from produt where preco>?  and preco< ?", (precomin, precomax ))
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                if controlador == 0:
                    print("nada foi encontrado")
                break
            else:
                controlador += 1
                print("Nome{}\n Preço{}".format(resultado[0], resultado[1]))
print("Progama finalizado")

conexao.commit()
cursor.close()
conexao.close()
