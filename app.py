from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
import forms

from models import db, Alumnos, Maestros
from forms import UserForm, MaestroForm 

app=Flask("__main__")
app.config.from_object(DevelopmentConfig)
db.init_app(app)
csrf=CSRFProtect(app)

@app.route("/", methods=["GET", "POST"])
@app.route("/index")
def index():
    create_alumno = forms.UserForm(request.form)
    alumno = Alumnos.query.all()
    maestros = Maestros.query.all()
    return render_template("index.html", form=create_alumno, alumno=alumno, maestros=maestros)

@app.route("/usuarios",methods=["GET","POST"])
def usuario():
    mat=0
    nom=''
    apa=''
    ama=''
    edad=0
    email=''
    usuarios_clas=UserForm(flask.request.form)
    if flask.request.method=='POST':
        mat=usuarios_clas.id.data
        nom=usuarios_clas.nombre.data
        apa=usuarios_clas.apaterno.data
        ama=usuarios_clas.amaterno.data
        edad=usuarios_clas.edad.data
        email=usuarios_clas.correo.data
    
    return flask.render_template('usuarios.html',form=usuarios_clas,mat=mat,
                           nom=nom,apa=apa,ama=ama,edad=edad,email=email)

@app.route("/maestros")
def lista_maestros():
    form_maestro = MaestroForm(request.form)
    maestros = Maestros.query.all()
    return render_template("maestros.html", form=form_maestro, maestros=maestros)
    
if __name__=="__main__":
    csrf.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True,port=5001)