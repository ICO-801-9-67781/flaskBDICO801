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
