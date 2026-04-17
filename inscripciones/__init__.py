from flask import Blueprint

# Creamos el Blueprint
inscripciones_bp = Blueprint('inscripciones', __name__, template_folder='../templates')

from . import routes
