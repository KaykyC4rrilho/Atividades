import sqlite3

nome = input("nome a procurar:")

conexao = sqlite3.connect("agenda.db")





cursor = conexao.cursor()
cursor.execute("select * from agenda")
