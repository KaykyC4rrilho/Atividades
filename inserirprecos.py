import sqlite3
conexao= sqlite3.connect("precos.db")
cursor = conexao.cursor()
listaDados=[("CaioCalaABoca", 454.00),
            ("Miguel", 1.00),
            ("Igor", 0.60)]

cursor.executemany('''
    insert into precos (nome, preco) values (?,?)
''', listaDados)
conexao.commit()
cursor.close()
conexao.close()