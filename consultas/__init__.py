from flask import Blueprint

# Creamos el Blueprint
consultas_bp = Blueprint('consultas', __name__, template_folder='../templates')

from . import routes
