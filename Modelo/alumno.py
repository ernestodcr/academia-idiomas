
# Clase Alumno
class Alumno:
    def __init__(self, id, nombre, apellido, email, telefono, curso=None):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__telefono = telefono
        self.__curso = curso  # Objeto Curso

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

    def get_curso(self):
        return self.__curso

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def set_email(self, email):
        self.__email = email

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def set_curso(self, curso):
        self.__curso = curso