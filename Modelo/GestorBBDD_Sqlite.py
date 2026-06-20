import sqlite3

class GestorBBDD_SQLITE:
    # Constructor
    def __init__(self, nombre_bd):
        self.__nombre_bd = nombre_bd
        # check_same_thread=False permite usar la BD desde varios threads (Flask)
        self.__conexion = sqlite3.connect(nombre_bd, check_same_thread=False)
        self.__cursor = self.__conexion.cursor()
    
    # Destructor: cerrar conexión
    def __del__(self):
        try:
            self.__cursor.close()
            self.__conexion.close()
            print("La BD se ha cerrado correctamente")
        except Exception as e:
            print(f"Error al cerrar la BD: {e}")
    
    # Ejecutar sentencia SQL con manejo de errores
    def ejecuta(self, sql):
        try:
            if sql.strip().upper().startswith("SELECT"):
                resultado = self.__cursor.execute(sql)
                return resultado
            else:
                self.__cursor.execute(sql)
                self.__conexion.commit()
                return True  # Éxito
        except sqlite3.IntegrityError as ie:
            print(f"Error de integridad en la BD: {ie}")
            return False
        except sqlite3.OperationalError as oe:
            print(f"Error operacional en la BD: {oe}")
            return False
        except Exception as e:
            print(f"Error desconocido al ejecutar SQL: {e}")
            return False