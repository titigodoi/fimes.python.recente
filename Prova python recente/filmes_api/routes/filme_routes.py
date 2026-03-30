from flask import Blueprint, request
from controllers.filme_controllers import create_filme, get_filmes, get_filme_by_id

filme_routes = Blueprint('filme_routes', __name__)

# POST
@filme_routes.route('/filmes', methods=['POST'])
def filmes_post():
    return create_filme(request.json)


# GET - todos
@filme_routes.route('/filmes', methods=['GET'])
def filmes_get():
    return get_filmes()


# GET - por ID
@filme_routes.route('/filmes/<int:id>', methods=['GET'])
def filme_get_id(id):
    return get_filme_by_id(id)