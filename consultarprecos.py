import sqlite3
conexao= sqlite3.connect("precos.db")
cursor = conexao.cursor()
cursor.execute("select * from precos")

while True:
    resultado= cursor.fetchone()
    if resultado is None:
        break
    print("\tNome: {}\n\n\tPreço :{}".format(resultado[0], resultado[1]))


cursor.close()
conexao.close()