from database import conectar_banco

conexao = conectar_banco()

autores = [
    ("Machado de Assis", "Brasileira"),
    ("Clarice Lispector", "brasileira"),
    ("José Saramago", "Portugues"),
    ("George Orwell", "Britânica"),
    ("J. K. Rowling", "Britânica")
]

for nome, nacionalidade in autores:
    conexao.execute("""
        INSERT INTO autores (nome, nacionalidade)
        SELECT ?, ?
        WHERE NOT EXISTS (
            SELECT 1 FROM autores WHERE nome = ?
        )
    """, (nome, nacionalidade, nome))

conexao.commit()

livros = [
    ("Dom Casmurro", 1899, "Machado de Assis"),
    ("Memórias Póstumas de Brás Cubas", 1881, "Machado de Assis"),
    ("A Hora da Estrela", 1977, "Clarice Lispector"),
    ("Ensaio sobre a Cegueira", 1995, "José Saramago"),
    ("1984", 1949, "George Orwell"),
    ("A Revolução dos Bichos", 1945, "George Orwell"),
    ("Harry Potter e a Pedra Filosofal", 1997, "J. K. Rowling")
]

for titulo, ano, autor in livros:
    conexao.execute("""
        INSERT INTO livros (titulo, ano, autorid)
        SELECT ?, ?, id
        FROM autores
        WHERE nome = ?
        AND NOT EXISTS (
            SELECT 1 FROM livros WHERE titulo = ?
        )
    """, (titulo, ano, autor, titulo))

conexao.commit()
conexao.close()

print("Banco de dados conectado com sucesso!")