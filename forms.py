from wtforms import Form, StringField,IntegerField,EmailField,PasswordField,SubmitField

class UserForm(Form):
    nombre=StringField("Nombre")
    apaterno=StringField("APaterno")
    amaterno=StringField("AMaterno")
    edad=IntegerField("Edad")
    correo=EmailField("Correo")
    matricula=IntegerField("Matricula")

class MaestroForm(Form):
    matricula = IntegerField("Matricula")
    nombre = StringField("Nombre")
    apellidos = StringField("Apellidos")
    especialidad = StringField("Especialidad")
    email = EmailField("Email")