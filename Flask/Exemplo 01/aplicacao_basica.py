from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <html>
    <head><title>Bolsa Futuro Digital</title></head>
    <body>
    <h1>Backend com Python</h1>
    <p>Esta é a página Web do curso</p>
    <p>Os slides estão disponíveis <a href="slides">aqui</a>.</p>
    </body>
    </html>
    """


@app.route('/slides')
def slides():
    return """
    <html>
    <head><title>Bolsa Futuro Digital</title></head>
    <body>
    <h1>Slides</h1>
    <ul>
    <li>Introdução</li>
    <li>O que é Software?</li>
    </ul>
    <p>Voltar para <a href="/">home</a>.</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run()
