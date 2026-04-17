from flask import render_template, request, redirect, url_for, flash
from . import inscripciones_bp
from models import db, Inscripcion, Alumnos, Curso
from forms import InscripcionForm

@inscripciones_bp.route('/')
def consultar_inscripciones():
    inscripciones = Inscripcion.query.order_by(Inscripcion.fecha_inscripcion.desc()).all()
    return render_template('Inscripciones/inscripciones.html', inscripciones=inscripciones)

@inscripciones_bp.route('/registrar', methods=['GET', 'POST'])
def registrar_inscripcion():
    form = InscripcionForm()
    alumnos = Alumnos.query.all()
    cursos = Curso.query.all()
    form.alumno_id.choices = [(a.id, f"{a.nombre} {a.apaterno} {a.amaterno}") for a in alumnos]
    form.curso_id.choices = [(c.id, c.nombre) for c in cursos]

    if not alumnos or not cursos:
        flash('Debe registrar al menos un alumno y un curso antes de crear una inscripción', 'danger')
        return redirect(url_for('index'))

    if form.validate_on_submit():
        nueva_inscripcion = Inscripcion(
            alumno_id=form.alumno_id.data,
            curso_id=form.curso_id.data,
        )
        db.session.add(nueva_inscripcion)
        db.session.commit()
        flash('Inscripción registrada con éxito', 'success')
        return redirect(url_for('inscripciones.consultar_inscripciones'))

    return render_template('Inscripciones/registrar_inscripcion.html', form=form)

@inscripciones_bp.route('/detalles/<int:id>')
def detalles_inscripcion(id):
    inscripcion = Inscripcion.query.get_or_404(id)
    return render_template('Inscripciones/detalles_inscripcion.html', inscripcion=inscripcion)

@inscripciones_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_inscripcion(id):
    inscripcion = Inscripcion.query.get_or_404(id)
    form = InscripcionForm(obj=inscripcion)
    alumnos = Alumnos.query.all()
    cursos = Curso.query.all()
    form.alumno_id.choices = [(a.id, f"{a.nombre} {a.apaterno} {a.amaterno}") for a in alumnos]
    form.curso_id.choices = [(c.id, c.nombre) for c in cursos]

    if form.validate_on_submit():
        inscripcion.alumno_id = form.alumno_id.data
        inscripcion.curso_id = form.curso_id.data
        db.session.commit()
        flash('Inscripción actualizada correctamente', 'success')
        return redirect(url_for('inscripciones.consultar_inscripciones'))

    return render_template('Inscripciones/editar_inscripcion.html', form=form, inscripcion=inscripcion)

@inscripciones_bp.route('/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar_inscripcion(id):
    inscripcion = Inscripcion.query.get_or_404(id)
    form = InscripcionForm(obj=inscripcion)
    alumnos = Alumnos.query.all()
    cursos = Curso.query.all()
    form.alumno_id.choices = [(a.id, f"{a.nombre} {a.apaterno} {a.amaterno}") for a in alumnos]
    form.curso_id.choices = [(c.id, c.nombre) for c in cursos]

    if request.method == 'POST':
        db.session.delete(inscripcion)
        db.session.commit()
        flash('Inscripción eliminada', 'danger')
        return redirect(url_for('inscripciones.consultar_inscripciones'))

    return render_template('Inscripciones/eliminar_inscripcion.html', form=form, inscripcion=inscripcion)
