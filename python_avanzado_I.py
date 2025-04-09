"""
Este archivo reproduce los codigos mostrados como ejemplo en el
PDF Python Avanzado: OOP
"""

class MiClase:
    pass

class UnEstudiante:
    pass

class Persona:
    is_person = True  # Atributo de clase

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {(self.nombre).title()} {(self.apellido).title()} y tengo {self.edad} años.")

persona1 = Persona("Ana", "lopez", 30) # Crear un objeto (instancia) de la clase Persona
persona1.saludar() # Usar un método

print(persona1.is_person)     # True
print(Persona.is_person)     # True

# @classmethod 
class Persona:
    especie = "Humano"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def cambiar_especie(cls, nueva_especie):
        cls.especie = nueva_especie

Persona.cambiar_especie("Alienígena")

# @staticmethod
class Calculadora:
    
    @staticmethod
    def sumar(a, b):
        return a + b

# Llamada desde la clase
print(Calculadora.sumar(5, 3))

# Llamada desde una instancia
calc = Calculadora()
print(calc.sumar(10, 7))

# Encapsulado
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad      # Atributo privado

    def saludar(self):
        print(f"Hola, mi nombre es {self.__nombre} y tengo {self.__edad} años.")

    def cumplir_años(self):
        self.__edad += 1

    def obtener_edad(self):
        return self.__edad

    def establecer_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre


persona1 = Persona("Ana", 30)
persona1.saludar()  # Hola, mi nombre es Ana y tengo 30 años.
persona1.cumplir_años()
print(persona1.obtener_edad())  # 31
persona1.establecer_nombre("Ana María")
persona1.saludar()  # Hola, mi nombre es Ana María y tengo 31 años.

# Abstracción
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def __procesar_nombre(self):
        # Método interno que no necesita conocer el usuario
        return self.__nombre.strip().title()

    def saludar(self):
        nombre_limpio = self.__procesar_nombre()
        print(f"Hola, mi nombre es {nombre_limpio} y tengo {self.__edad} años.")

persona1 = Persona("   ana", 25)
persona1.saludar()  # Hola, mi nombre es Ana y tengo 25 años.

# Variable publica
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre  # pública

p = Persona("Ana")
print(p.nombre)  # Acceso permitido
p.nombre = "Laura"  # Modificación permitida
print(p.nombre)

# Variable privada
class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre  # privada

p = Persona("Ana")
# print(p.__nombre) # Esto da error: AttributeError

# Acceso usando name mangling (no recomendado)
print(p._Persona__nombre)  #  Acceso posible pero no es una buena práctica

# Herencia
# Clase base (padre)
class Person:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def greet(self):
        print(f"Hola, soy {self.name} {self.lastname} y tengo {self.age} años.")

# Clase derivada (hija)
class Student(Person):
    def __init__(self, name, lastname, age, student_id):
        super().__init__(name, lastname, age)  # Llamamos al constructor de la clase padre
        self.student_id = student_id

    def mostrar_estudiante(self):
        print(f"Soy un estudiante con ID: {self.student_id}")

# Creamos una instancia de Student
estudiante = Student("Lucía", "González", 21, "A12345")
estudiante.greet()               # Método heredado de la clase Person
estudiante.mostrar_estudiante()  # Método propio de Student