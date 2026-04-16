from flask import render_template, request, redirect, url_for, flash
from . import alumnos_bp
from models import db, Alumnos
from forms import UserForm

@alumnos_bp.route('/')
def consultar_alumnos():
    alumnos = Alumnos.query.all()
    return render_template('Alumnos/alumnos_list.html', alumnos=alumnos)

@alumnos_bp.route('/registrar', methods=['GET', 'POST'])
def registrar_alumno():
    form = UserForm()
    if form.validate_on_submit():
        nuevo_alumno = Alumnos(
            nombre=form.nombre.data,
            apaterno=form.apaterno.data,
            amaterno=form.amaterno.data,
            edad=form.edad.data,
            correo=form.correo.data
        )
        db.session.add(nuevo_alumno)
        db.session.commit()
        flash('Alumno registrado con éxito', 'success')
        return redirect(url_for('alumnos.consultar_alumnos'))
    return render_template('Alumnos/registrar_alumno.html', form=form)

@alumnos_bp.route('/detalles/<int:id>')
def detalles_alumno(id):
    alumno = Alumnos.query.get_or_404(id)
    return render_template('Alumnos/detalles.html', alumno=alumno)

@alumnos_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_alumno(id):
    alumno = Alumnos.query.get_or_404(id)
    form = UserForm(obj=alumno)
    if form.validate_on_submit():
        alumno.nombre = form.nombre.data
        alumno.apaterno = form.apaterno.data
        alumno.amaterno = form.amaterno.data
        alumno.edad = form.edad.data
        alumno.correo = form.correo.data
        db.session.commit()
        flash('Alumno actualizado correctamente', 'success')
        return redirect(url_for('alumnos.consultar_alumnos'))
    return render_template('Alumnos/modificar.html', form=form, alumno=alumno)

@alumnos_bp.route('/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar_alumno(id):
    alumno = Alumnos.query.get_or_404(id)
    form = UserForm(obj=alumno)
    if request.method == 'POST':
        db.session.delete(alumno)
        db.session.commit()
        flash('Alumno eliminado', 'danger')
        return redirect(url_for('alumnos.consultar_alumnos'))
    return render_template('Alumnos/eliminar.html', form=form, alumno=alumno)