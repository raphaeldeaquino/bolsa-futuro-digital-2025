from flask import Flask, render_template, redirect, url_for, session, flash
from flask_bootstrap import Bootstrap5
from cliente_form import ClienteForm

app = Flask(__name__)
app.secret_key = "chave-super-secreta"
bootstrap = Bootstrap5(app)

# Simulação de banco de dados em memória
clientes = []

# Página inicial: lista de clientes
@app.route("/")
def index():
    ultimo = session.get("ultimo_cadastrado")
    return render_template("index.html", clientes=clientes, ultimo=ultimo, title="Clientes Cadastrados")

# Página de cadastro
@app.route("/cadastro", methods=["GET", "POST"])
def cadastrar_cliente():
    form = ClienteForm()
    if form.validate_on_submit():
        cliente = {
            "nome": form.nome.data,
            "email": form.email.data,
            "telefone": form.telefone.data
        }
        clientes.append(cliente)
        flash("Cliente cadastrado com sucesso!", "success")
        return redirect(url_for("cadastrar_cliente"))
    elif form.is_submitted():
        flash("Erro ao cadastrar. Verifique os campos.", "danger")
    return render_template("cadastro.html", form=form)

# Limpar lista (simula exclusão de todos)
@app.route("/limpar")
def limpar():
    clientes.clear()
    session.pop("ultimo_cadastrado", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
