from flask import render_template, request, redirect, url_for, flash
from . import maestros_bp
from models import db, Maestros
from forms import MaestroForm

@maestros_bp.route('/')
def consultar_maestros():
    maestros = Maestros.query.all()
    return render_template('Maestros/maestros.html', maestros=maestros)

@maestros_bp.route('/registrar', methods=['GET', 'POST'])
def registrar_maestro():
    form = MaestroForm()
    if form.validate_on_submit():
        nuevo_maestro = Maestros(
            nombre=form.nombre.data,
            apellidos=form.apellidos.data,
            especialidad=form.especialidad.data,
            email=form.email.data
        )
        db.session.add(nuevo_maestro)
        db.session.commit()
        flash('Maestro registrado con éxito', 'success')
        return redirect(url_for('maestros.consultar_maestros'))
    return render_template('Maestros/registrar_maestro.html', form=form)

@maestros_bp.route('/detalles/<int:id>')
def detalles_maestro(id):
    maestro = Maestros.query.get_or_404(id)
    return render_template('Maestros/detalles_maestro.html', maestro=maestro)

@maestros_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_maestro(id):
    maestro = Maestros.query.get_or_404(id)
    form = MaestroForm(obj=maestro)
    if form.validate_on_submit():
        maestro.nombre = form.nombre.data
        maestro.apellidos = form.apellidos.data
        maestro.especialidad = form.especialidad.data
        maestro.email = form.email.data
        db.session.commit()
        flash('Maestro actualizado correctamente', 'success')
        return redirect(url_for('maestros.consultar_maestros'))
    return render_template('Maestros/editar_maestro.html', form=form, maestro=maestro)

@maestros_bp.route('/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar_maestro(id):
    maestro = Maestros.query.get_or_404(id)
    form = MaestroForm(obj=maestro)
    if request.method == 'POST':
        db.session.delete(maestro)
        db.session.commit()
        flash('Maestro eliminado', 'danger')
        return redirect(url_for('maestros.consultar_maestros'))
    return render_template('Maestros/eliminar_maestro.html', form=form, maestro=maestro)