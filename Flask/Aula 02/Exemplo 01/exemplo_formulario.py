from flask import Flask, session, redirect, url_for
from flask import render_template
from flask_bootstrap import Bootstrap5
from nome_form import NomeForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'alguma senha que ninguém saiba'
bootstrap = Bootstrap5(app)

@app.route('/', methods=["GET", "POST"])
def index():
    form = NomeForm()

    # se o nome já estiver na sessão, mostra a mensagem direto
    if "nome" in session:
        nome = session["nome"]
        return render_template("index.html", nome=nome)

    # se o formulário for enviado corretamente, salva o nome e recarrega a página
    if form.validate_on_submit():
        session["nome"] = form.nome.data
        return redirect(url_for("index"))

    # se ainda não tem nome, mostra o formulário
    return render_template("index.html", form=form, nome=None)

# Rota para limpar a sessão
@app.route("/reset")
def reset():
    session.pop("nome", None)
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run()