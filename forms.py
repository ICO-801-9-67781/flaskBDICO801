from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, PasswordField, SubmitField, SelectField, TextAreaField

class UserForm(FlaskForm):
    id = IntegerField("ID")  # Este es el nombre que Jinja2 buscará
    nombre = StringField("Nombre")
    apaterno = StringField("APaterno")
    amaterno = StringField("AMaterno")
    edad = IntegerField("Edad")
    correo = EmailField("Correo")

class MaestroForm(FlaskForm):
    id = IntegerField("ID")
    nombre = StringField("Nombre")
    apellidos = StringField("Apellidos")
    especialidad = StringField("Especialidad")
    email = EmailField("Email")

class CursoForm(FlaskForm):
    id = IntegerField("ID")
    nombre = StringField("Nombre")
    descripcion = TextAreaField("Descripción")
    maestro_id = SelectField("Maestro", coerce=int, choices=[])

class InscripcionForm(FlaskForm):
    id = IntegerField("ID")
    alumno_id = SelectField("Alumno", coerce=int, choices=[])
    curso_id = SelectField("Curso", coerce=int, choices=[])
