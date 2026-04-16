from flask import Blueprint

# Creamos el Blueprint
cursos_bp = Blueprint('cursos', __name__, template_folder='../templates')

from . import routes
