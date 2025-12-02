from flask import Flask, jsonify, request
from flasgger import Swagger, swag_from

app = Flask(__name__)

template = {
    "swagger": "2.0",
    "info": {
        "title": "API de Cores",
        "description": "API para manipulação de cores",
        "contact": {
            "responsibleOrganization": "ME",
            "responsibleDeveloper": "Me",
            "email": "me@me.com",
            "url": "www.me.com",
        },
        "termsOfService": "http://me.com/terms",
        "version": "0.0.1"
    },
    "host": "mysite.com",
    "basePath": "/api",
    "schemes": ["http", "https"],
}

swagger = Swagger(app, template=template)


# ============================================================
# 1) ENDPOINT SIMPLES
# ============================================================
@app.route('/cores/<paleta>/')
def cores(paleta):
    """
    Endpoint que retorna uma lista de cores por paleta.
    ---
    parameters:
      - name: paleta
        description: Paleta a ser buscada
        in: path
        type: string
        enum: ['todas', 'rgb', 'cmyk']
        required: true
        default: todas

    definitions:
      Paleta:
        type: object
        properties:
          cores:
            type: array
            items:
              $ref: '#/definitions/Cor'
      Cor:
        type: string

    responses:
      200:
        description: Lista de cores (pode ser filtrada por paleta)
        schema:
          $ref: '#/definitions/Paleta'
        examples:
          rgb: ['red', 'green', 'blue']
      404:
        description: Paleta não encontrada
    """
    todas_cores = {
        'cmyk': ['cyan', 'magenta', 'yellow', 'black'],
        'rgb': ['red', 'green', 'blue'],
        'todas': ['cyan', 'magenta', 'yellow', 'black', 'red', 'green', 'blue']
    }

    if paleta not in todas_cores:
        return jsonify({"erro": "Paleta não encontrada"}), 404

    return jsonify({"cores": todas_cores[paleta]})


# ============================================================
# 2) ENDPOINT COM PARÂMETROS DE QUERY
# ============================================================
@app.route('/filtrar-cores')
def filtrar_cores():
    """
    Filtra cores que começam com uma letra específica.
    ---
    parameters:
      - name: letra
        in: query
        type: string
        required: true
        description: Letra inicial para o filtro
        default: r

    responses:
      200:
        description: Lista filtrada
        examples:
          exemplo: ['red']
    """
    letra = request.args.get("letra", "").lower()
    cores = ['red', 'green', 'blue', 'yellow']

    resultado = [c for c in cores if c.startswith(letra)]
    return jsonify(resultado)


# ============================================================
# 3) ENDPOINT COM BODY E SCHEMA (POST)
# ============================================================
@app.route('/adicionar-cor', methods=['POST'])
def adicionar_cor():
    """
    Adiciona uma nova cor à lista.
    ---
    parameters:
      - in: body
        name: cor
        description: Objeto da cor a ser inserida
        required: true
        schema:
          id: NovaCor
          required:
            - nome
          properties:
            nome:
              type: string
              example: 'violet'

    responses:
      201:
        description: Cor adicionada
      400:
        description: Erro no formato enviado
    """
    data = request.get_json()
    if not data or "nome" not in data:
        return jsonify({"erro": "Formato inválido"}), 400

    return jsonify({"mensagem": "Cor adicionada", "cor": data["nome"]}), 201


# ============================================================
# 4) ENDPOINT COM UPLOAD DE ARQUIVO
# ============================================================
@app.route('/upload-paleta', methods=['POST'])
def upload_paleta():
    """
    Faz upload de um arquivo contendo cores.
    ---
    consumes:
      - multipart/form-data
    parameters:
      - name: arquivo
        in: formData
        type: file
        required: true
        description: Arquivo contendo uma lista de cores

    responses:
      200:
        description: Confirmação de upload
    """
    arquivo = request.files.get("arquivo")
    if not arquivo:
        return jsonify({"erro": "Nenhum arquivo enviado"}), 400

    return jsonify({"mensagem": f"Arquivo {arquivo.filename} recebido"})


# ============================================================
# 5) ENDPOINT QUE USA AUTENTICAÇÃO VIA HEADER
# ============================================================
@app.route('/segredo')
def segredo():
    """
    Endpoint protegido por chave de API.
    ---
    parameters:
      - name: X-API-KEY
        in: header
        type: string
        required: true
        description: Chave de API para acesso

    responses:
      200:
        description: Acesso autorizado
      401:
        description: Chave inválida
    """
    chave = request.headers.get("X-API-KEY")
    if chave != "12345":
        return jsonify({"erro": "Chave inválida"}), 401

    return jsonify({"mensagem": "Acesso concedido"})


# ============================================================
# 6) ENDPOINT RETORNANDO LISTA COMPLETA COM SCHEMA AVANÇADO
# ============================================================
@app.route('/todas-as-cores')
def todas_as_cores():
    """
    Retorna todas as cores com mais informações.
    ---
    definitions:
      CorDetalhada:
        type: object
        properties:
          nome:
            type: string
          tipo:
            type: string
            enum: ['primária', 'secundária', 'terciária']

    responses:
      200:
        description: Lista detalhada de cores
        schema:
          type: array
          items:
            $ref: '#/definitions/CorDetalhada'
    """
    return jsonify([
        {"nome": "red", "tipo": "primária"},
        {"nome": "green", "tipo": "primária"},
        {"nome": "yellow", "tipo": "secundária"}
    ])

app.run(debug=True)
