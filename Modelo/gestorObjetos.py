from Modelo.GestorBBDD_Sqlite import GestorBBDD_SQLITE
from Modelo.curso import Curso
from Modelo.alumno import Alumno
from Modelo.profesor import Profesor

import pandas as pd
import sqlite3
import os
import openpyxl
import matplotlib 
matplotlib.use('Agg') 
import matplotlib.pyplot as plt


class GestorObjetos:
    
    # Constructor
    def __init__(self):
        self.__gBD = GestorBBDD_SQLITE("academiaIdiomas.db")
    
    # Método crear_tablas
    def crear_tablas(self):
        try:
            self.__gBD.ejecuta("""
                CREATE TABLE IF NOT EXISTS Profesor (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT,
                    apellido TEXT,
                    email TEXT,
                    telefono TEXT
                )
            """)
            self.__gBD.ejecuta("""
                CREATE TABLE IF NOT EXISTS Curso (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT,
                    idioma TEXT,
                    profesor_id INTEGER,
                    FOREIGN KEY (profesor_id) REFERENCES Profesor(id)
                )
            """)
            self.__gBD.ejecuta("""
                CREATE TABLE IF NOT EXISTS Alumno (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT,
                    apellido TEXT,
                    email TEXT,
                    telefono TEXT,
                    curso_id INTEGER,
                    FOREIGN KEY (curso_id) REFERENCES Curso(id)
                )
            """)
        except Exception as e:
            print(f"Error al crear tablas: {e}")

    # Método insertar profesor
    def insertar_profesor(self, id, nombre, apellido, email, telefono):
        try:
            sql = f"""
            INSERT INTO Profesor (id, nombre, apellido, email, telefono)
            VALUES ({id}, '{nombre}', '{apellido}', '{email}', '{telefono}')
            """
            self.__gBD.ejecuta(sql)
        except Exception as e:
            print(f"Error al insertar profesor: {e}")

    # Método insertar curso
    def insertar_curso(self, id, nombre, idioma, profesor_id):
        try:
            profesor_obj = self.obtener_objeto_profesor(profesor_id)
            profesor_id_sql = profesor_obj.get_id() if profesor_obj else "NULL"
            sql = f"""
            INSERT INTO Curso (id, nombre, idioma, profesor_id)
            VALUES ({id}, '{nombre}', '{idioma}', {profesor_id_sql})
            """
            self.__gBD.ejecuta(sql)
        except Exception as e:
            print(f"Error al insertar curso: {e}")
    
    # Método insertar alumno
    def insertar_alumno(self, id, nombre, apellido, email, telefono, curso_id):
        try:
            sql = f"""
            INSERT INTO Alumno (id, nombre, apellido, email, telefono, curso_id)
            VALUES ({id}, '{nombre}', '{apellido}', '{email}', '{telefono}', {curso_id})
            """
            self.__gBD.ejecuta(sql)
        except Exception as e:
            print(f"Error al insertar alumno: {e}")

    # Modificar un profesor por id
    def actualizar_profesor(self, id, nombre=None, apellido=None, email=None, telefono=None):
        try:
            campos = []
            if nombre: campos.append(f"nombre='{nombre}'")
            if apellido: campos.append(f"apellido='{apellido}'")
            if email: campos.append(f"email='{email}'")
            if telefono: campos.append(f"telefono='{telefono}'")
            if campos:
                sql = f"UPDATE Profesor SET {', '.join(campos)} WHERE id={id}"
                self.__gBD.ejecuta(sql)
        except Exception as e:
            print(f"Error al actualizar profesor: {e}")

    # Eliminar un profesor por id
    def eliminar_profesor(self, profesor_id):
        try:
            sql = f"DELETE FROM Profesor WHERE id={profesor_id}"
            self.__gBD.ejecuta(sql)
        except Exception as e:
            print(f"Error al eliminar profesor: {e}")

    # Modificar un curso por id
    def actualizar_curso(self, id, nombre=None, idioma=None, profesor_id=None):
        try:
            campos = []
            if nombre: campos.append(f"nombre='{nombre}'")
            if idioma: campos.append(f"idioma='{idioma}'")
            if profesor_id is not None:
                prof_obj = self.obtener_objeto_profesor(profesor_id)
                prof_id_sql = prof_obj.get_id() if prof_obj else "NULL"
                campos.append(f"profesor_id={prof_id_sql}")
            if campos:
                sql = f"UPDATE Curso SET {', '.join(campos)} WHERE id={id}"
                self.__gBD.ejecuta(sql)
        except Exception as e:
            print(f"Error al actualizar curso: {e}")

    # Eliminar un curso por id
    def eliminar_curso(self, curso_id):
        try:
            sql = f"DELETE FROM Curso WHERE id={curso_id}"
            self.__gBD.ejecuta(sql)
        except Exception as e:
            print(f"Error al eliminar curso: {e}")

    # Modificar un alumno por id
    def actualizar_alumno(self, id, nombre=None, apellido=None, email=None, telefono=None, curso_id=None):
        try:
            campos = []
            if nombre: campos.append(f"nombre='{nombre}'")
            if apellido: campos.append(f"apellido='{apellido}'")
            if email: campos.append(f"email='{email}'")
            if telefono: campos.append(f"telefono='{telefono}'")
            if curso_id is not None: campos.append(f"curso_id={curso_id}")
            if campos:
                sql = f"UPDATE Alumno SET {', '.join(campos)} WHERE id={id}"
                self.__gBD.ejecuta(sql)
        except Exception as e:
            print(f"Error al actualizar alumno: {e}")

    # Eliminar un alumno por id
    def eliminar_alumno(self, alumno_id):
        try:
            sql = f"DELETE FROM Alumno WHERE id={alumno_id}"
            self.__gBD.ejecuta(sql)
        except Exception as e:
            print(f"Error al eliminar alumno: {e}")

    # Metodo obtener datos
    def obtener_profesores(self):
        sql = "SELECT * FROM Profesor"
        return self.__gBD.ejecuta(sql)

    def obtener_cursos(self):
        sql = """
        SELECT Curso.id, Curso.nombre, Curso.idioma, Profesor.nombre, Profesor.apellido
        FROM Curso
        LEFT JOIN Profesor ON Curso.profesor_id = Profesor.id
        LEFT JOIN Alumno ON Curso.id = Alumno.curso_id
        GROUP BY Curso.id
    HAVING COUNT(Alumno.id) < 10
        """
        resultado = self.__gBD.ejecuta(sql)
        return resultado.fetchall()
    
    def obtener_todos_cursos(self):
        sql = """
        SELECT Curso.id, Curso.nombre, Curso.idioma, Profesor.nombre, Profesor.apellido
        FROM Curso
        LEFT JOIN Profesor ON Curso.profesor_id = Profesor.id
        """
        resultado = self.__gBD.ejecuta(sql)
        return resultado.fetchall()

    def obtener_alumnos(self):
        sql = """
        SELECT Alumno.id, Alumno.nombre, Alumno.apellido, Alumno.email, Alumno.telefono,
            Curso.nombre
        FROM Alumno
        LEFT JOIN Curso ON Alumno.curso_id = Curso.id
        """
        resultado = self.__gBD.ejecuta(sql)
        return resultado.fetchall()

    # Obtener objetos por ID
    def obtener_objeto_profesor(self, profesor_id):
        for p in self.obtener_profesores():
            if p[0] == profesor_id:
                return Profesor(p[0], p[1], p[2], p[3], p[4])
        return None

    def obtener_curso_por_id(self, id):
        resultado = self.__gBD.ejecuta(f"SELECT * FROM Curso WHERE id={id}")
        return resultado.fetchone()

    def obtener_profesor_por_id(self, id):
        resultado = self.__gBD.ejecuta(f"SELECT * FROM Profesor WHERE id={id}")
        return resultado.fetchone()

    def obtener_alumno_por_id(self, id):
        resultado = self.__gBD.ejecuta(f"SELECT * FROM Alumno WHERE id={id}")
        return resultado.fetchone()
    
    # Metodo generar reporte excel
    def generar_reporte_excel(self):
        """Extrae los datos y crea un Excel con 3 pestañas"""
        ruta_dir = "static"
        if not os.path.exists(ruta_dir):
            os.makedirs(ruta_dir)
            
        ruta_archivo = os.path.join(ruta_dir, "reporte_academia.xlsx")
        conn = sqlite3.connect("academiaIdiomas.db")
        
        try:
            # 1. Alumnos: Según tu UML, Alumno tiene un "curso"
            # Probablemente la columna en la BD sea 'curso_id'
            df_alumnos = pd.read_sql_query("""
                SELECT Alumno.id, Alumno.nombre, Alumno.apellido, Alumno.email, 
                    Curso.nombre AS nombre_curso
                FROM Alumno 
                LEFT JOIN Curso ON Alumno.curso_id = Curso.id
            """, conn)
            
            # 2. Cursos: Según tu UML, Curso tiene un "profesor"
            # Probablemente la columna en la BD sea 'profesor_id'
            df_cursos = pd.read_sql_query("""
                SELECT Curso.id, Curso.nombre, Curso.idioma, 
                    Profesor.nombre || ' ' || Profesor.apellido AS nombre_profesor
                FROM Curso 
                LEFT JOIN Profesor ON Curso.profesor_id = Profesor.id
            """, conn)
            
            # 3. Profesores: Lista directa
            df_profesores = pd.read_sql_query("SELECT id, nombre, apellido, email, telefono FROM Profesor", conn)

            with pd.ExcelWriter(ruta_archivo, engine='openpyxl') as writer:
                df_alumnos.to_excel(writer, sheet_name='Alumnos', index=False)
                df_cursos.to_excel(writer, sheet_name='Cursos', index=False)
                df_profesores.to_excel(writer, sheet_name='Profesores', index=False)
                
            return ruta_archivo

        finally:
            conn.close()
    
    # Metodo obtener en png un grafico
    def generar_grafico_ocupacion(self):
        """Crea un gráfico de barras basado en la ocupación actual"""
        # 1. Ruta donde guardaremos la imagen
        ruta_grafico = "static/grafico_ocupacion.png"
        
        # 2. Conexión y Consulta SQL (Contamos alumnos agrupados por curso)
        conn = sqlite3.connect("academiaIdiomas.db")
        query = """
            SELECT Curso.nombre as nombre_curso, COUNT(Alumno.id) as total_alumnos
            FROM Curso
            LEFT JOIN Alumno ON Curso.id = Alumno.curso_id
            GROUP BY Curso.nombre
        """
        df = pd.read_sql_query(query, conn)
        conn.close()

        # 3. Diseño del gráfico
        plt.figure(figsize=(10, 7)) # Aumentamos un poco el alto (de 6 a 7)
        plt.bar(df['nombre_curso'], df['total_alumnos'], color='#4CAF50')
        
        plt.title('Alumnos inscritos por Curso', pad=20)
        plt.ylabel('Cantidad de Alumnos')
        plt.xlabel('Cursos Ofertados', labelpad=15)

        # --- LAS LÍNEAS MÁGICAS PARA LA VISIBILIDAD ---
        # Rotamos 45 grados y alineamos al final del nombre
        plt.xticks(rotation=45, ha='right', fontsize=10)
        
        # Ajuste automático para que nada se corte al guardar
        plt.tight_layout() 

        # 4. Guardar archivo físico
        plt.savefig(ruta_grafico)
        plt.close() 
        return ruta_grafico
    
    def obtener_analisis_cupo(self):
        """Calcula el estado de plazas de cada curso (Lógica de Negocio ADP)"""
        conn = sqlite3.connect("academiaIdiomas.db")
        # Consultamos inscritos por curso
        query = """
            SELECT Curso.nombre, COUNT(Alumno.id) as inscritos
            FROM Curso
            LEFT JOIN Alumno ON Curso.id = Alumno.curso_id
            GROUP BY Curso.nombre
        """
        df = pd.read_sql_query(query, conn)
        conn.close()

        LIMITE = 10
        resultados = []

        for index, row in df.iterrows():
            n_inscritos = row['inscritos']
            
            # Aplicamos la lógica de decisión
            if n_inscritos >= LIMITE:
                estado = "🔴 COMPLETO"
                color_css = "estado-rojo"
            elif n_inscritos >= 7: # Del 70% al 90% de ocupación
                estado = "🟠 ÚLTIMAS PLAZAS"
                color_css = "estado-naranja"
            else:
                estado = "🟢 DISPONIBLE"
                color_css = "estado-verde"
            
            resultados.append({
                "curso": row['nombre'],
                "inscritos": n_inscritos,
                "estado": estado,
                "clase": color_css,
                "libres": LIMITE - n_inscritos
            })
        
        return resultados