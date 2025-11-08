from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from database import init_db

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from models import Livro

with app.app_context():
    init_db()

@app.route('/livros', methods=['POST'])
def cadastrar_livro():
    dados = request.get_json()
    
    novo_livro = Livro(
        titulo=dados['titulo'],
        autor=dados['autor'],
        isbn=dados.get('isbn'),
        ano_publicacao=dados.get('ano_publicacao'),
        preco=dados.get('preco'),
        disponivel=dados.get('disponivel', True)
    )
    
    db.session.add(novo_livro)
    db.session.commit()
    
    return jsonify({
        'mensagem': 'Livro cadastrado com sucesso!',
        'livro': novo_livro.to_dict()
    }), 201

@app.route('/livros', methods=['GET'])
def listar_livros():
    livros = db.session.query(Livro).all()
    
    return jsonify({
        'total': len(livros),
        'livros': [livro.to_dict() for livro in livros]
    })

@app.route('/livros/<int:id>', methods=['GET'])
def buscar_livro(id):
    livro = db.session.query(Livro).filter(Livro.id == id).first()

    if not livro:
        return jsonify({'erro': 'Livro não encontrado'}), 404
    
    return jsonify(livro.to_dict())

@app.route('/livros/autor/<nome_autor>', methods=['GET'])
def buscar_por_autor(nome_autor):
    livros = db.session.query(Livro).filter(
        Livro.autor.ilike(f'%{nome_autor}%')
    ).all()
    
    if not livros:
        return jsonify({
            'mensagem': 'Nenhum livro encontrado para este autor'
        }), 404
    
    return jsonify({
        'autor': nome_autor,
        'total': len(livros),
        'livros': [livro.to_dict() for livro in livros]
    })

@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    livro = db.session.query(Livro).filter(Livro.id == id).first()
    
    if not livro:
        return jsonify({'erro': 'Livro não encontrado', 'id': id}), 404    

    titulo = livro.titulo  # Salva para mensagem
    
    db.session.delete(livro)
    db.session.commit()
    
    return jsonify({
        'mensagem': f'Livro "{titulo}" excluído com sucesso!'
    }), 200

@app.route('/livros/<int:id>', methods=['PUT'])
def atualizar_livro(id):
    """Atualiza um livro com validações completas."""
    try:
        livro = db.session.query(Livro).filter(Livro.id == id).first()
        
        if not livro:
            return jsonify({'erro': 'Livro não encontrado'}), 404
        
        dados = request.get_json()
        
        if not dados:
            return jsonify({'erro': 'Nenhum dado fornecido'}), 400
        
        # Salva estado anterior para log
        estado_anterior = livro.to_dict()
        campos_alterados = []
        
        # Validações e atualizações
        if 'titulo' in dados:
            if not dados['titulo'] or len(dados['titulo']) > 200:
                return jsonify({
                    'erro': 'Título inválido',
                    'regra': 'Deve ter entre 1 e 200 caracteres'
                }), 400
            if livro.titulo != dados['titulo']:
                livro.titulo = dados['titulo']
                campos_alterados.append('titulo')
        
        if 'autor' in dados:
            if not dados['autor'] or len(dados['autor']) > 100:
                return jsonify({
                    'erro': 'Autor inválido',
                    'regra': 'Deve ter entre 1 e 100 caracteres'
                }), 400
            if livro.autor != dados['autor']:
                livro.autor = dados['autor']
                campos_alterados.append('autor')
        
        if 'isbn' in dados:
            if not dados['isbn']:
                return jsonify({'erro': 'ISBN não pode ser vazio'}), 400
            
            # Verifica se ISBN já existe em outro livro
            isbn_existente = g.db_session.query(Livro).filter(
                Livro.isbn == dados['isbn'],
                Livro.id != id
            ).first()
            
            if isbn_existente:
                return jsonify({
                    'erro': 'ISBN já cadastrado em outro livro',
                    'livro_existente': {
                        'id': isbn_existente.id,
                        'titulo': isbn_existente.titulo
                    }
                }), 409  # Conflict
            
            livro.isbn = dados['isbn']
            if not livro.validar_isbn():
                return jsonify({
                    'erro': 'ISBN inválido',
                    'regra': 'Deve ter 10 ou 13 dígitos'
                }), 400
            campos_alterados.append('isbn')
        
        if 'ano_publicacao' in dados:
            ano = dados['ano_publicacao']
            if ano and (ano < 1000 or ano > 2100):
                return jsonify({
                    'erro': 'Ano de publicação inválido',
                    'regra': 'Deve estar entre 1000 e 2100'
                }), 400
            if livro.ano_publicacao != ano:
                livro.ano_publicacao = ano
                campos_alterados.append('ano_publicacao')
        
        if 'preco' in dados:
            preco = dados['preco']
            if preco < 0:
                return jsonify({
                    'erro': 'Preço inválido',
                    'regra': 'Deve ser maior ou igual a zero'
                }), 400
            if livro.preco != preco:
                livro.preco = preco
                campos_alterados.append('preco')
        
        if 'disponivel' in dados:
            if livro.disponivel != dados['disponivel']:
                livro.disponivel = dados['disponivel']
                campos_alterados.append('disponivel')
        
        # Verifica se houve alguma alteração
        if not campos_alterados:
            return jsonify({
                'mensagem': 'Nenhuma alteração detectada',
                'livro': livro.to_dict()
            }), 200
        
        db.session.commit()
        
        return jsonify({
            'mensagem': 'Livro atualizado com sucesso!',
            'campos_alterados': campos_alterados,
            'livro_antes': estado_anterior,
            'livro_depois': livro.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'erro': 'Erro ao atualizar livro',
            'detalhes': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
