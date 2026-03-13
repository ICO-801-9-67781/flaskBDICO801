from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Alumnos(db.Model):
    __tablename__ = "alumnos"
    matricula = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apaterno = db.Column(db.String(50), nullable=False)
    amaterno = db.Column(db.String(50), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    correo = db.Column(db.String(50), nullable=False)

    def __init__(self, matricula, nombre, apaterno, amaterno, edad, correo):
        self.matricula = matricula
        self.nombre = nombre
        self.apaterno = apaterno
        self.amaterno = amaterno
        self.edad = edad
        self.correo = correo

class Maestros(db.Model):
    __tablename__ = 'maestros'
    matricula = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellidos = db.Column(db.String(50))
    especialidad = db.Column(db.String(50))
    email = db.Column(db.String(50))

    def __init__(self, matricula, nombre, apellidos, especialidad, email):
        self.matricula = matricula
        self.nombre = nombre
        self.apellidos = apellidos
        self.especialidad = especialidad
        self.email = email