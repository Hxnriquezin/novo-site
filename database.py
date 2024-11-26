import sqlite3

def conectar_banco():

    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
    (id INTEGER PRIMARY KEY, usuario TEXT, email TEXT)''')

    conexao.commit()

    conexao.close()

if __name__ == '__main__':
  
    conectar_banco()
