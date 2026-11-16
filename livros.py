from flask import Blueprint, jsonify, abort
from database import conectar_banco

livros_bp = Blueprint("livros", __name__)

@livros_bp.route("/livros", methods=["GET"])
def listar_livros():

    conexao = conectar_banco()

    livros = conexao.execute("""
        SELECT
            livros.id,
            livros.titulo,
            livros.ano,
            autores.nome AS autor,
            autores.nacionalidade
        FROM livros
        JOIN autores
            ON livros.autorid = autores.id
        ORDER BY livros.id
        """
    ).fetchall()

    conexao.close()

    resultado = []

    for livro in livros:
        resultado.append({
            "id": livro["id"],
            "titulo": livro["titulo"],
            "ano": livro["ano"],
            "autor": livro["autor"],
            "nacionalidade": livro["nacionalidade"]
        })


    return jsonify(resultado)

@livros_bp.route("/livros/<int:id>", methods=["GET"])
def buscar_livros(id):

    conexao = conectar_banco()

    livro = conexao.execute(
        "SELECT * FROM livros WHERE id = ?", (id,)
    ).fetchone()

    if livro is None:
        abort(404)

    return jsonify({
        "id": livro["id"],
        "titulo": livro["titulo"],
        "ano": livro["ano"]
    }), 200

    conexao.close()