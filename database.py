import sqlite3

def conectar_banco ():
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()

    conectar_banco
    cursor.excute('''CREATE TABLE IF NOT EXISTS usuarios
    (id INTEGER PRIMARY KEY, usuario TEXT, email TEXT )''')

if __name__ =='__main__':
    conectar_banco()

    
    conexao.commit()
