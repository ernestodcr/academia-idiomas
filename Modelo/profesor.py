
# archivo: Modelo/profesor.py
class Profesor:
    def __init__(self, id, nombre, apellido, email, telefono):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__telefono = telefono
        self.__cursos = []  # Lista de objetos Curso

    # Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_email(self):
        return self.__email

    def get_telefono(self):
        return self.__telefono

    def get_cursos(self):
        return self.__cursos

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def set_email(self, email):
        self.__email = email

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def add_curso(self, curso):
        if curso not in self.__cursos:
            self.__cursos.append(curso)

    def remove_curso(self, curso):
        if curso in self.__cursos:
            self.__cursos.remove(curso)