from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from config import DevelopmentConfig
import forms

from models import db, Alumnos, Maestros
from forms import UserForm, MaestroForm

app = Flask("__main__")
app.config.from_object(DevelopmentConfig)
db.init_app(app)
migrate = Migrate(
    app, db
)  # Inicializa Flask-Migrate con la aplicación y la base de datos
csrf = CSRFProtect(app)


@app.route("/", methods=["GET", "POST"])
@app.route("/index")
def index():
    create_alumno = forms.UserForm(request.form)
    alumno = Alumnos.query.all()
    maestros = Maestros.query.all()
    return render_template(
        "index.html", form=create_alumno, alumno=alumno, maestros=maestros
    )


@app.route("/Alumnos", methods=["GET", "POST"])
def alumnos():
    create_form = forms.UserForm(request.form)
    if request.method == "POST":
        alum = Alumnos(
            nombre=create_form.nombre.data,
            amaterno=create_form.amaterno.data,
            apaterno=create_form.apaterno.data,
            edad=create_form.edad.data,
            correo=create_form.correo.data,
        )
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("Alumnos.html", form=create_form)

@app.route("/maestros")
def lista_maestros():
    form_maestro = MaestroForm(request.form)
    maestros = Maestros.query.all()
    return render_template("maestros.html", form=form_maestro, maestros=maestros)


if __name__ == "__main__":
    csrf.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)
