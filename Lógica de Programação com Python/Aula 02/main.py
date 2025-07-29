from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

elogios = [
    "você tem um futuro brilhante!",
    "você é muito criativo!",
    "o mundo precisa de mais pessoas como você!",
    "você será um(a) programador(a) incrível!",
    "hoje é um ótimo dia para você brilhar!"
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/elogio", methods=["POST"])
def elogio():
    data = request.get_json()
    nome = data.get("nome", "amigo")
    resposta = random.choice(elogios)
    return jsonify({"mensagem": f"{nome}, {resposta}"})


app.run(host="0.0.0.0", port=81)
