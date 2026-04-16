from flask import Flask, render_template
from config import DevelopmentConfig
from models import db
from maestros.routes import maestros_bp
from alumnos.routes import alumnos_bp

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

# Inicializar DB
db.init_app(app)

# REGISTRO DE BLUEPRINTS
# Todas las rutas de maestros ahora empezarán con /maestros (ej: /maestros/registrar)
app.register_blueprint(maestros_bp, url_prefix='/maestros')
# Todas las rutas de alumnos ahora empezarán con /Alumnos (ej: /Alumnos/registrar)
app.register_blueprint(alumnos_bp, url_prefix='/Alumnos')

@app.route('/')
def index():
    # Esta es tu pantalla de bienvenida con las dos cards
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)