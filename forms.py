from wtforms import Form, StringField,IntegerField,EmailField,PasswordField,SubmitField, validators



class UserForm(Form):
    nombre=StringField("Nombre")
    apaterno=StringField("APaterno")
    amaterno=StringField("AMaterno")
    edad=IntegerField("Edad")
    correo=EmailField("Correo")
    matricula=IntegerField("Matricula")