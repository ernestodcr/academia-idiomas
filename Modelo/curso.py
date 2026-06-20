
class Curso:
    def __init__(self, id, nombre, idioma, profesor=None):
        self.__id = id
        self.__nombre = nombre
        self.__idioma = idioma
        self.__profesor = profesor  # Objeto Profesor
        self.__alumnos = []  # Lista de objetos Alumno

    # Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_idioma(self):
        return self.__idioma

    def get_profesor(self):
        return self.__profesor

    def get_alumnos(self):
        return self.__alumnos

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_idioma(self, idioma):
        self.__idioma = idioma

    def set_profesor(self, profesor):
        self.__profesor = profesor

    # Métodos para manejar alumnos
    def add_alumno(self, alumno):
        if alumno not in self.__alumnos:
            self.__alumnos.append(alumno)
            alumno.set_curso(self)

    def remove_alumno(self, alumno):
        if alumno in self.__alumnos:
            self.__alumnos.remove(alumno)
            alumno.set_curso(None)