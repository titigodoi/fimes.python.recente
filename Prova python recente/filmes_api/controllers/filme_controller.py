from models.filme_models import Filme
from db import db
import json
from flask import make_response

def create_filme(filme_data):
    novo_filme = Filme(
        titulo=filme_data['titulo'],
        genero=filme_data['genero'],
        duracao=filme_data['duracao'],
        ano=filme_data['ano'],
        diretor=filme_data['diretor']
    )

    db.session.add(novo_filme)
    db.session.commit()

    response = make_response(
        json.dumps({
            'mensagem': 'Filme cadastrado com sucesso.',
            'filme': novo_filme.json()
        }, ensure_ascii=False)
    )

    response.headers['Content-Type'] = 'app'
    return response, 201


def get_filmes():
    filmes = Filme.query.all()

    response = make_response(
        json.dumps({
            'mensagem': 'Lista de filmes',
            'dados': [filme.json() for filme in filmes]
        }, ensure_ascii=False)
    )

    response.headers['Content-Type'] = 'app'
    return response, 200


def get_filme_by_id(id):
    filme = Filme.query.get(id)

    if filme:
        response = make_response(
            json.dumps(filme.json(), ensure_ascii=False)
        )
        response.headers['Content-Type'] = 'app'
        return response, 200
    else:
        response = make_response(
            json.dumps({'mensagem': 'Filme não encontrado'}, ensure_ascii=False)
        )
        response.headers['Content-Type'] = 'app'
        return response, 404