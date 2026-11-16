from flask import Flask, jsonify, make_response
from routes.autores import autores_bp
from routes.livros import livros_bp

app = Flask(__name__)

app.register_blueprint(autores_bp)
app.register_blueprint(livros_bp)

@app.route("/", methods=["GET"])
def inicio():
    return jsonify({
        "Aviso": "Aviso: API de Biblioteca",
        "rotas": ["/autores", "/livros"]
    }), 200

@app.route("/status", methods=["GET"])
def verificacao():

    resposta = make_response(
        jsonify({
            "Aviso": "API em estabilidade",
            "nivel": "online",
        }), 200
    )

    resposta.headers["APIBiblioteca"] = "Versao4.0"

    return resposta

@app.errorhandler(404)
def erro(erro):
    return jsonify({
        "erro": True,
        "Aviso": "Rota não encontrada",
        "status": 404
    })


if __name__ == "__main__":
    app.run(debug=True)