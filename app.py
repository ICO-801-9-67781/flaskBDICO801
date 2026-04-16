from flask import Flask, render_template
from config import DevelopmentConfig
from models import db
from maestros.routes import maestros_bp
from alumnos.routes import alumnos_bp
from cursos.routes import cursos_bp

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db.init_app(app)

# BLUEPRINTS
app.register_blueprint(maestros_bp, url_prefix='/maestros')
app.register_blueprint(alumnos_bp, url_prefix='/Alumnos')
app.register_blueprint(cursos_bp, url_prefix='/cursos')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)