from flask import Blueprint

# Creamos el Blueprint
alumnos_bp = Blueprint('alumnos', __name__, template_folder='../templates')

from . import routes