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

# Clase base (padre)
class Person:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def greet(self):
        print(f"Hola, soy {self.name} {self.lastname} y tengo {self.age} años.")

# Clase hija con método sobrescrito
class Student(Person):
    def __init__(self, name, lastname, student_id):
        super().__init__(name, lastname)
        self.student_id = student_id

    def greet(self):  # Sobrescribimos el método greet
        print(f"Soy {self.name} {self.lastname}, mi ID de estudiante es {self.student_id}.")

# Creamos una instancia de Student
persona = Person("Carlos", "Pérez")
estudiante = Student("Ana", "López", "S1234")

persona.greet()     # Imprime: Hola, soy Carlos Pérez.
estudiante.greet()  # Imprime: Hola, soy Ana López y mi ID de estudiante es S1234.

# Clase padre
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

# Clase hija
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

# Creamos una instancia de Perro
mi_mascota = Perro("Firulais", "Labrador")

# Verificamos con isinstance()
print(isinstance(mi_mascota, Perro))   # True
print(isinstance(mi_mascota, Animal))  # True
print(isinstance(mi_mascota, object))  # True


# Objeto tipo cadena
str_obj = "Polimorfismo"

# Objeto tipo lista
list_obj = ["Java", "Python", "Ruby", "C#", "PHP", "C++"]

# Objeto tipo diccionario
dict_obj = {
    "marca": "Tesla",
    "modelo": "Nombres divertidos :)",
    "año": 2023
}

# La función len() se comporta diferente según el tipo de objeto
print(len(str_obj))    # Devuelve la cantidad de caracteres de la cadena
print(len(list_obj))   # Devuelve la cantidad de elementos en la lista
print(len(dict_obj))   # Devuelve la cantidad de claves en el diccionario


# Clase padre
class Person:
    def __init__(self, name, dob, id_number):
        self.name = name
        self.dob = dob
        self.id_number = id_number

    def info(self):
        print("Nombre:", self.name)
        print("Fecha de nacimiento:", self.dob)
        print("Número de ID:", self.id_number)

# Clase hija
class Employee(Person):
    def __init__(self, name, dob, id_number, salary, position):
        # Usamos super() para llamar al constructor de la clase padre
        super().__init__(name, dob, id_number)
        self.salary = salary
        self.position = position

    def info(self):
        # Llamamos al método info() de la clase padre
        super().info()
        print("Salario:", self.salary)
        print("Puesto:", self.position)

# Crear una instancia de la clase Person
persona = Person("Ana López", "1990-04-15", "12345678")
print("----- Información de la persona -----")
persona.info()

# Crear una instancia de la clase Employee
empleado = Employee("Carlos Méndez", "1985-11-23", "87654321", 50000, "Gerente")
print("\n----- Información del empleado -----")
empleado.info()

# Introspección de código en Python
print(type(5))           # <class 'int'>
print(type("Hola"))      # <class 'str'>

x = 42
print(id(x))  # Ej: 140737488351312

print(dir("Python"))
class Persona:
    nombre = "Juan"

p = Persona()
print(hasattr(p, 'nombre'))  # True

print(getattr(p, 'nombre'))  # Juan

def saludar():
    print("Hola")
print(callable(saludar))  # True

print(isinstance(p, Persona))  # True

# Métodos más comunes
class Libro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas

    def __str__(self):
        return f"Libro: {self.titulo} ({self.paginas} páginas)"

    def __len__(self):
        return self.paginas

    def __add__(self, otro_libro):
        return self.paginas + otro_libro.paginas

# Crear objetos
libro1 = Libro("Python Fácil", 300)
libro2 = Libro("POO en Profundidad", 200)

print(libro1)             # __str__: Libro: Python Fácil (300 páginas)
print(len(libro1))        # __len__: 300
print(libro1 + libro2)    # __add__: 500

# Herencias multiples
# Clase 1
class Estudiante:
    def __init__(self, nombre, materia):
        self.nombre = nombre
        self.materia = materia

    def mostrar_estudiante(self):
        print(f"Estudiante: {self.nombre}, Materia: {self.materia}")

# Clase 2
class Atleta:
    def __init__(self, deporte):
        self.deporte = deporte

    def mostrar_deporte(self):
        print(f"Deporte: {self.deporte}")

# Clase hija que hereda de Estudiante y Atleta
class EstudianteDeportivo(Estudiante, Atleta):
    def __init__(self, nombre, materia, deporte):
        # Llamamos a los constructores de ambas clases padre
        Estudiante.__init__(self, nombre, materia)
        Atleta.__init__(self, deporte)

    def mostrar_todo(self):
        self.mostrar_estudiante()
        self.mostrar_deporte()

persona = EstudianteDeportivo("Lucía", "Matemática", "Natación")
persona.mostrar_todo()
