from flask import render_template, request, flash
from . import consultas_bp
from models import Alumnos, Maestros, Curso

@consultas_bp.route('/')
def index_consultas():
    return render_template('Consultas/consultas.html')

@consultas_bp.route('/cursos_por_alumno', methods=['GET', 'POST'])
def cursos_por_alumno():
    alumnos = Alumnos.query.order_by(Alumnos.nombre).all()
    cursos = []
    selected_alumno = None

    if request.method == 'POST':
        alumno_id = request.form.get('alumno_id', type=int)
        if not alumno_id:
            flash('Seleccione un alumno válido antes de consultar.', 'danger')
        else:
            selected_alumno = Alumnos.query.get(alumno_id)
            if selected_alumno:
                cursos = selected_alumno.cursos
                if not cursos:
                    flash('No se encontraron cursos vinculados a este alumno.', 'danger')
            else:
                flash('Alumno no encontrado.', 'danger')

    return render_template(
        'Consultas/cursos_por_alumno.html',
        alumnos=alumnos,
        cursos=cursos,
        selected_alumno=selected_alumno,
    )

@consultas_bp.route('/cursos_por_maestro', methods=['GET', 'POST'])
def cursos_por_maestro():
    maestros = Maestros.query.order_by(Maestros.nombre).all()
    cursos = []
    selected_maestro = None

    if request.method == 'POST':
        maestro_id = request.form.get('maestro_id', type=int)
        if not maestro_id:
            flash('Seleccione un maestro válido antes de consultar.', 'danger')
        else:
            selected_maestro = Maestros.query.get(maestro_id)
            if selected_maestro:
                cursos = selected_maestro.cursos
                if not cursos:
                    flash('No se encontraron cursos para el maestro seleccionado.', 'danger')
            else:
                flash('Maestro no encontrado.', 'danger')

    return render_template(
        'Consultas/cursos_por_maestro.html',
        maestros=maestros,
        cursos=cursos,
        selected_maestro=selected_maestro,
    )

@consultas_bp.route('/alumnos_por_curso', methods=['GET', 'POST'])
def alumnos_por_curso():
    cursos = Curso.query.order_by(Curso.nombre).all()
    alumnos = []
    selected_curso = None

    if request.method == 'POST':
        curso_id = request.form.get('curso_id', type=int)
        if not curso_id:
            flash('Seleccione un curso válido antes de consultar.', 'danger')
        else:
            selected_curso = Curso.query.get(curso_id)
            if selected_curso:
                alumnos = selected_curso.alumnos
                if not alumnos:
                    flash('No se encontraron alumnos inscritos en este curso.', 'danger')
            else:
                flash('Curso no encontrado.', 'danger')

    return render_template(
        'Consultas/alumnos_por_curso.html',
        cursos=cursos,
        alumnos=alumnos,
        selected_curso=selected_curso,
    )
