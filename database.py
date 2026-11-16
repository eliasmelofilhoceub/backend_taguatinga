import sqlite3

def conectar_banco():
    conexao = sqlite3.connect("biblioteca.db")
    conexao.row_factory = sqlite3.Row
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao

def tabelas():

    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL, 
        email TEXT NOT NULL UNIQUE, 
        senha TEXT NOT NULL, 
        perfil TEXT NOT NULL DEFAULT "usuario" 
        )
        """)

    conexao.commit()
    conexao.close()

print("Tabelas criadas")