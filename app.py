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


@app.route("/detalles", methods=["GET", "POST"])
def detalles():
    create_form = forms.UserForm(request.form)
    if request.method == "GET":
        id = request.args.get("id")
        # select * from alumnos where id == id
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        id = request.args.get("id")
        nombre = alum1.nombre
        apaterno = alum1.apaterno
        amaterno = alum1.amaterno
        edad = alum1.edad
        correo = alum1.correo

    return render_template(
        "detalles.html",
        id=id,
        nombre=nombre,
        apaterno=apaterno,
        amaterno=amaterno,
        edad=edad,
        correo=correo,
    )


@app.route("/modificar", methods=["GET", "POST"])
def modificar():
    create_form = forms.UserForm(request.form)
    if request.method == "GET":
        id = request.args.get("id")
        #  select * from alumnos where id == id
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get("id")
        create_form.nombre.data = alum1.nombre
        create_form.apaterno.data = alum1.apaterno
        create_form.amaterno.data = alum1.amaterno
        create_form.edad.data = alum1.edad
        create_form.correo.data = alum1.correo

    if request.method == "POST":
        id = request.args.get("id")
        #  select * from alumnos where id == id
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum1.id = id
        alum1.nombre = create_form.nombre.data
        alum1.apaterno = create_form.apaterno.data
        alum1.amaterno = create_form.amaterno.data
        alum1.edad = create_form.edad.data
        alum1.correo = create_form.correo.data
        db.session.add(alum1)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("modificar.html", form=create_form)


@app.route("/eliminar", methods=["GET", "POST"])
def eliminar():
    create_form = forms.UserForm(request.form)
    if request.method == "GET":
        id = request.args.get("id")
        #  select * from alumnos where id == id
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get("id")
        create_form.nombre.data = alum1.nombre
        create_form.apaterno.data = alum1.apaterno
        create_form.amaterno.data = alum1.amaterno
        create_form.edad.data = alum1.edad
        create_form.correo.data = alum1.correo
    if request.method == "POST":
        id = request.form.get("id")
        alum = Alumnos.query.get_or_404(id)
        # delete from alumnos where id=id
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("eliminar.html", form=create_form)


# --- RUTAS DE MAESTROS ---


@app.route("/maestros")
def maestros_view():
    maestros = Maestros.query.all()
    return render_template("maestros.html", maestros=maestros)


@app.route("/registrar_maestro", methods=["GET", "POST"])
def registrar_maestro():
    form = forms.MaestroForm(request.form)

    if request.method == "POST":
        nuevo_maestro = Maestros(
            matricula=form.id.data,
            nombre=form.nombre.data,
            apellidos=form.apellidos.data,
            especialidad=form.especialidad.data,
            email=form.email.data,
        )
        db.session.add(nuevo_maestro)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("registrar_maestro.html", form=form)


@app.route("/editar_maestro", methods=["GET", "POST"])
def editar_maestro():
    create_form = forms.MaestroForm(request.form)

    if request.method == "GET":
        id = request.args.get("id")
        # select * from maestros where matricula == id
        maestro1 = db.session.query(Maestros).filter(Maestros.matricula == id).first()

        # Llenamos el formulario con los datos de la base de datos
        create_form.id.data = id
        create_form.nombre.data = maestro1.nombre
        create_form.apellidos.data = maestro1.apellidos
        create_form.especialidad.data = maestro1.especialidad
        create_form.email.data = maestro1.email

    if request.method == "POST":
        id = request.args.get("id")
        # select * from maestros where matricula == id
        maestro1 = db.session.query(Maestros).filter(Maestros.matricula == id).first()

        maestro1.matricula = id
        maestro1.nombre = create_form.nombre.data
        maestro1.apellidos = create_form.apellidos.data
        maestro1.especialidad = create_form.especialidad.data
        maestro1.email = create_form.email.data

        db.session.add(maestro1)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("editar_maestro.html", form=create_form)


@app.route("/detalles_maestro", methods=["GET"])
def detalles_maestro():
    id_maestro = request.args.get("id")
    maestro = Maestros.query.get_or_404(id_maestro)
    return render_template("detalles_maestro.html", maestro=maestro)


@app.route("/eliminar_maestro", methods=["GET", "POST"])
def eliminar_maestro():
    create_form = forms.MaestroForm(request.form)

    if request.method == "GET":
        id = request.args.get("id")
        # select * from maestros where matricula == id
        maestro = db.session.query(Maestros).filter(Maestros.matricula == id).first()

        # Llenamos el formulario con los datos de la base de datos
        create_form.id.data = request.args.get("id")
        create_form.nombre.data = maestro.nombre
        create_form.apellidos.data = maestro.apellidos
        create_form.especialidad.data = maestro.especialidad
        create_form.email.data = maestro.email

    if request.method == "POST":
        id = request.form.get("id")
        maestro = Maestros.query.get_or_404(id)
        db.session.delete(maestro)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("eliminar_maestro.html", form=create_form)


if __name__ == "__main__":
    csrf.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)
