class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo protegido
        self.__edad = edad     # Atributo privado

    def obtener_edad(self):
        return self.__edad

    def establecer_edad(self, edad):
        if 0 < edad < 120:
            self.__edad = edad
        else:
            raise ValueError("Edad no válida")

# Uso
persona = Persona("Alice", 30)
print(persona.obtener_edad())

persona.establecer_edad(35)
print(persona.obtener_edad())

# Intento de acceso directo fallido
try:
    print(persona.__edad)
except AttributeError as e:
    print(40)
