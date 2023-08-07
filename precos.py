import sqlite3
conexao= sqlite3.connect("precos.db")
cursor = conexao.cursor()
cursor.execute('''

    create table precos (
        nome text, 
        preco float)



''')

cursor.execute('''
    insert into precos (nome, preco)
    values (?,?)

''', ("Nilo", 54.50))

conexao.commit()
cursor.close()
conexao.close()
