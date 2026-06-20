# Importar gestor y clases del modelo
from Modelo.gestorObjetos import GestorObjetos
from Modelo.profesor import Profesor
from Modelo.curso import Curso
from Modelo.alumno import Alumno


# Crear gestor de objetos (conecta con la BD)
gestor = GestorObjetos()

# Crear tablas si no existen
gestor.crear_tablas()


# Crear objeto Profesor (datos de prueba)
profesor1 = Profesor(
    1,
    "Juan",
    "Garcia",
    "juan.garcia@academia.com",
    "600123456"
)

# Insertar profesor en la BD
gestor.insertar_profesor(profesor1)


# Crear objeto Curso y asignar profesor
curso1 = Curso(
    1,
    "Ingles A1",
    "Ingles",
    profesor1
)

# Insertar curso en la BD
gestor.insertar_curso(curso1)


# Crear objeto Alumno y asignar curso
alumno1 = Alumno(
    1,
    "Ana",
    "Perez",
    "ana.perez@email.com",
    "611987654",
    curso1
)

# Insertar alumno en la BD
gestor.insertar_alumno(alumno1)


# Mensaje simple de confirmación
print("Datos insertados correctamente")