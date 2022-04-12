from flask import Flask, render_template
from flask.globals import request
from models.personagem import Personagem


app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    """Função que exibi a pagina inicial"""

    return render_template("index.html")


@app.route("/buscar", methods=['GET', 'POST'])
def exibir():
    """Função para exibir os dados da requisição da Api"""

    # chamando a classe teste
    personagem = Personagem(request.form["nome"])

    # pegando as informações da requisição e passando para variavel
    dados = personagem.realizar_request()

    # exibindo as informações na pagina 
    return render_template("index.html",
    nome = dados[0], status = dados[1], especie = dados[2], imagem = dados[3],
    localizacao = dados[4], episodio = personagem.request_nome_episodio(dados[5]))


@app.errorhandler(KeyError)
def exibir_pagina_erro(e):
    """Função que irá redirecionar para pagina de erro, 
    caso o usuário digite um estado inválido"""

    return render_template("erro.html")


if __name__ == "__main__":
    app.run(debug=True)