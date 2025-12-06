from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "segredo123"

usuarios = {"ana": "123", "joao": "abc"}

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    user = request.form["usuario"]
    senha = request.form["senha"]

    if user in usuarios and usuarios[user] == senha:
        session["usuario"] = user
        return redirect("/dashboard")
    return "Login inválido"

@app.route("/dashboard")
def dashboard():
    if "usuario" not in session:
        return redirect("/")
    return f"Olá, {session['usuario']}!"

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
