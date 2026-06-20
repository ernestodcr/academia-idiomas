from flask import Flask, render_template, request, redirect, url_for, abort, send_file
from markupsafe import escape  # <--- Importamos la herramienta de escape
from Modelo.gestorObjetos import GestorObjetos

app = Flask(__name__)
gestor = GestorObjetos()

# ---------------------------------------------------------------------
# INICIO
# ---------------------------------------------------------------------
@app.route("/")
def index():
    """Página de bienvenida"""
    return render_template("inicio.html")


# ---------------------------------------------------------------------
# PROFESORES
# ---------------------------------------------------------------------
@app.route("/profesores")
def mostrar_profesores():
    """Mostrar todos los profesores"""
    try:
        profesores = gestor.obtener_profesores()
        return render_template("profesores.html", profesores=profesores)
    except Exception as e:
        return render_template("500.html", error=str(e)), 500

@app.route("/agregar_profesor", methods=["GET", "POST"])
def agregar_profesor():
    """Agregar un profesor con escape de datos"""
    try:
        if request.method == "POST":
            # Aplicamos escape() a los campos de texto para limpiar scripts maliciosos
            gestor.insertar_profesor(
                id=int(request.form["id"]),
                nombre=escape(request.form["nombre"]),
                apellido=escape(request.form["apellido"]),
                email=escape(request.form["email"]),
                telefono=escape(request.form["telefono"])
            )
            return redirect(url_for("mostrar_profesores"))
        return render_template("agregar_profesor.html")
    except ValueError:
        return "Error: Datos inválidos", 400
    except Exception as e:
        return render_template("500.html", error=str(e)), 500

@app.route("/editar_profesor/<int:id>", methods=["GET", "POST"])
def editar_profesor(id):
    """Modificar un profesor con escape de datos"""
    try:
        if request.method == "POST":
            gestor.actualizar_profesor(
                id=id,
                nombre=escape(request.form["nombre"]),
                apellido=escape(request.form["apellido"]),
                email=escape(request.form["email"]),
                telefono=escape(request.form["telefono"])
            )
            return redirect(url_for("mostrar_profesores"))

        profesor = gestor.obtener_profesor_por_id(id)
        return render_template("editar_profesor.html", profesor=profesor)
    except Exception as e:
        return render_template("500.html", error=str(e)), 500

@app.route("/eliminar_profesor/<int:id>", methods=["POST"])
def eliminar_profesor(id):
    """Eliminar un profesor"""
    try:
        gestor.eliminar_profesor(id)
        return redirect(url_for("mostrar_profesores"))
    except Exception as e:
        return render_template("500.html", error=str(e)), 500

# ---------------------------------------------------------------------
# CURSOS
# ---------------------------------------------------------------------
@app.route("/cursos")
def mostrar_cursos():
    """Mostrar todos los cursos"""
    try:
        cursos = gestor.obtener_todos_cursos()
        return render_template("cursos.html", cursos=cursos)
    except Exception as e:
        return render_template("500.html", error=str(e)), 500

@app.route("/agregar_curso", methods=["GET", "POST"])
def agregar_curso():
    """Agregar un curso con escape de datos"""
    try:
        profesores = gestor.obtener_profesores()
        if request.method == "POST":
            gestor.insertar_curso(
                id=int(request.form["id"]),
                nombre=escape(request.form["nombre"]),
                idioma=escape(request.form["idioma"]),
                profesor_id=int(request.form["profesor_id"])
            )
            return redirect(url_for("mostrar_cursos"))
        return render_template("agregar_curso.html", profesores=profesores)
    except ValueError:
        return "Error: Datos inválidos", 400
    except Exception as e:
        return render_template("500.html", error=str(e)), 500

@app.route("/editar_curso/<int:id>", methods=["GET", "POST"])
def editar_curso(id):
    """Modificar un curso con escape de datos"""
    try:
        profesores = [(int(p[0]), p[1], p[2]) for p in gestor.obtener_profesores()]
        if request.method == "POST":
            gestor.actualizar_curso(
                id=id,
                nombre=escape(request.form["nombre"]),
                idioma=escape(request.form["idioma"]),
                profesor_id=int(request.form["profesor_id"])
            )
            return redirect(url_for("mostrar_cursos"))

        curso = list(gestor.obtener_curso_por_id(id))
        curso[3] = int(curso[3]) if curso[3] else None
        return render_template("editar_curso.html", curso=curso, profesores=profesores)
    except Exception as e:
        return render_template("500.html", error=str(e)), 500

@app.route("/eliminar_curso/<int:id>", methods=["POST"])
def eliminar_curso(id):
    """Eliminar un curso"""
    try:
        gestor.eliminar_curso(id)
        return redirect(url_for("mostrar_cursos"))
    except Exception as e:
        return render_template("500.html", error=str(e)), 500

# ---------------------------------------------------------------------
# ALUMNOS
# ---------------------------------------------------------------------
@app.route("/alumnos")
def mostrar_alumnos():
    """Mostrar todos los alumnos"""
    try:
        alumnos = gestor.obtener_alumnos()
        return render_template("alumnos.html", alumnos=alumnos)
    except Exception as e:
        return render_template("500.html", error=str(e)), 500

@app.route("/agregar_alumno", methods=["GET", "POST"])
def agregar_alumno():
    """Agregar un alumno con escape de datos"""
    try:
        cursos = gestor.obtener_cursos()
        if request.method == "POST":
            gestor.insertar_alumno(
                id=int(request.form["id"]),
                nombre=escape(request.form["nombre"]),
                apellido=escape(request.form["apellido"]),
                email=escape(request.form["email"]),
                telefono=escape(request.form["telefono"]),
                curso_id=int(request.form["curso_id"])
            )
            return redirect(url_for("mostrar_alumnos"))
        return render_template("agregar_alumno.html", cursos=cursos)
    except ValueError:
        return "Error: Datos inválidos", 400
    except Exception as e:
        return render_template("500.html", error=str(e)), 500

@app.route("/editar_alumno/<int:id>", methods=["GET", "POST"])
def editar_alumno(id):
    """Modificar un alumno con escape de datos"""
    try:
        cursos = gestor.obtener_cursos()
        if request.method == "POST":
            gestor.actualizar_alumno(
                id=id,
                nombre=escape(request.form["nombre"]),
                apellido=escape(request.form["apellido"]),
                email=escape(request.form["email"]),
                telefono=escape(request.form["telefono"]),
                curso_id=int(request.form["curso_id"])
            )
            return redirect(url_for("mostrar_alumnos"))

        alumno = gestor.obtener_alumno_por_id(id)
        return render_template("editar_alumno.html", alumno=alumno, cursos=cursos)
    except Exception as e:
        return render_template("500.html", error=str(e)), 500

@app.route("/eliminar_alumno/<int:id>", methods=["POST"])
def eliminar_alumno(id):
    """Eliminar un alumno"""
    try:
        gestor.eliminar_alumno(id)
        return redirect(url_for("mostrar_alumnos"))
    except Exception as e:
        return render_template("500.html", error=str(e)), 500

# ---------------------------------------------------------------------
# MANEJO DE ERRORES (ROBUSTEZ)
# ---------------------------------------------------------------------
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template("404.html"), 404

@app.errorhandler(500)
def error_interno(error):
    return render_template("500.html", error=str(error)), 500

# Metodo descargar todos datos en un mismo Excel
@app.route("/descargar_reporte")
def descargar_reporte():
    try:
        ruta_archivo = gestor.generar_reporte_excel()
        return send_file(ruta_archivo, as_attachment=True)
    except Exception as e:
        return render_template("500.html")

# Metodo mostrar grafico estadisticas
@app.route("/estadisticas")
def mostrar_estadisticas():
    try:
        # Mandamos al gestor que cree la imagen más reciente
        gestor.generar_grafico_ocupacion()
        # Obtenemos el nuevo análisis de cupo
        analisis_plazas = gestor.obtener_analisis_cupo()
        return render_template("estadisticas.html", plazas=analisis_plazas)
    except Exception as e:
        return render_template("500.html")

if __name__ == "__main__":
    app.run(debug=True)