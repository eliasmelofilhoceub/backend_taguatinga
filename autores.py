from flask import Blueprint, jsonify
from database import conectar_banco

autores_bp = Blueprint("autores", __name__)

@autores_bp.route("/autores", methods=["GET"])
def listar_autores():

    conexao = conectar_banco()
    try:
    
        autores = conexao.execute("""
        SELECT * FROM autores
        ORDER BY id
        """
    ).fetchall()

        resultado = []

        for autor in autores:
            resultado.append({
            "id": autor["id"],
            "nome": autor["nome"],
            "nacionalidade": autor["nacionalidade"]
        })

        return jsonify(resultado), 200

    finally:
        conexao.close()
