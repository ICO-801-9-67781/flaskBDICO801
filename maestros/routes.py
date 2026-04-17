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
    otros_maestros = Maestros.query.filter(Maestros.matricula != id).all()
    if request.method == 'POST':
        if maestro.cursos:
            action = request.form.get('action')
            if action == 'reassign':
                if not otros_maestros:
                    flash('No hay otro maestro disponible para reasignar los cursos.', 'danger')
                    return render_template('Maestros/eliminar_maestro.html', form=form, maestro=maestro, otros_maestros=otros_maestros)
                nuevo_maestro_id = request.form.get('nuevo_maestro_id', type=int)
                if not nuevo_maestro_id:
                    flash('Seleccione un maestro válido para la reasignación.', 'danger')
                    return render_template('Maestros/eliminar_maestro.html', form=form, maestro=maestro, otros_maestros=otros_maestros)
                nuevo_maestro = Maestros.query.get(nuevo_maestro_id)
                if not nuevo_maestro or nuevo_maestro.matricula == maestro.matricula:
                    flash('Seleccione un maestro válido para la reasignación.', 'danger')
                    return render_template('Maestros/eliminar_maestro.html', form=form, maestro=maestro, otros_maestros=otros_maestros)
                for curso in list(maestro.cursos):
                    curso.maestro = nuevo_maestro
            elif action == 'delete_courses':
                for curso in list(maestro.cursos):
                    db.session.delete(curso)
            else:
                flash('Selecciona una opción válida antes de eliminar.', 'danger')
                return render_template('Maestros/eliminar_maestro.html', form=form, maestro=maestro, otros_maestros=otros_maestros)
        db.session.delete(maestro)
        db.session.commit()
        flash('Maestro eliminado', 'danger')
        return redirect(url_for('maestros.consultar_maestros'))
    return render_template('Maestros/eliminar_maestro.html', form=form, maestro=maestro, otros_maestros=otros_maestros)