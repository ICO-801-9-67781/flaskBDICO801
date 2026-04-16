from flask import render_template, request, redirect, url_for, flash
from . import cursos_bp
from models import db, Curso, Maestros
from forms import CursoForm

@cursos_bp.route('/')
def consultar_cursos():
    cursos = Curso.query.all()
    return render_template('Cursos/cursos.html', cursos=cursos)

@cursos_bp.route('/registrar', methods=['GET', 'POST'])
def registrar_curso():
    form = CursoForm()
    maestros = Maestros.query.all()
    form.maestro_id.choices = [(m.matricula, f"{m.nombre} {m.apellidos}") for m in maestros]

    if not maestros:
        flash('Debe registrar al menos un maestro antes de crear un curso', 'danger')
        return redirect(url_for('maestros.consultar_maestros'))

    if form.validate_on_submit():
        nuevo_curso = Curso(
            nombre=form.nombre.data,
            descripcion=form.descripcion.data,
            maestro_id=form.maestro_id.data,
        )
        db.session.add(nuevo_curso)
        db.session.commit()
        flash('Curso registrado con éxito', 'success')
        return redirect(url_for('cursos.consultar_cursos'))

    return render_template('Cursos/registrar_curso.html', form=form)

@cursos_bp.route('/detalles/<int:id>')
def detalles_curso(id):
    curso = Curso.query.get_or_404(id)
    return render_template('Cursos/detalles_curso.html', curso=curso)

@cursos_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_curso(id):
    curso = Curso.query.get_or_404(id)
    form = CursoForm(obj=curso)
    maestros = Maestros.query.all()
    form.maestro_id.choices = [(m.matricula, f"{m.nombre} {m.apellidos}") for m in maestros]

    if form.validate_on_submit():
        curso.nombre = form.nombre.data
        curso.descripcion = form.descripcion.data
        curso.maestro_id = form.maestro_id.data
        db.session.commit()
        flash('Curso actualizado correctamente', 'success')
        return redirect(url_for('cursos.consultar_cursos'))

    return render_template('Cursos/editar_curso.html', form=form, curso=curso)

@cursos_bp.route('/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar_curso(id):
    curso = Curso.query.get_or_404(id)
    form = CursoForm(obj=curso)
    maestros = Maestros.query.all()
    form.maestro_id.choices = [(m.matricula, f"{m.nombre} {m.apellidos}") for m in maestros]

    if request.method == 'POST':
        db.session.delete(curso)
        db.session.commit()
        flash('Curso eliminado', 'danger')
        return redirect(url_for('cursos.consultar_cursos'))

    return render_template('Cursos/eliminar_curso.html', form=form, curso=curso)
