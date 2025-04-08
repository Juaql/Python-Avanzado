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

