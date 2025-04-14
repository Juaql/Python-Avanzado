"""
Este archivo reproduce los codigos mostrados como ejemplo en el
PDF Python Avanzado: OOP
"""

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

# Ejemplo de uso:
print(isPhoneNumber("415-555-4242"))  # True
print(isPhoneNumber("Hola-mundo-2025"))  # False

# Buscar dentro de un texto largo
message = "Call me at 415-555-1011 tomorrow. 123-456-7890 is my office number."

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print("Phone number found:", chunk)

import re

phoneRegex = re.compile(r'\d{3}-\d{3}-\d{4}')


mo = phoneRegex.search('My number is 415-555-4242.')

if mo:
    print('Phone number found:', mo.group())
else:
    print('No phone number found.')


text = "Llama al 415-555-4242"
pattern = re.compile(r"(\d{3})-(\d{3}-\d{4})")
match = pattern.search(text)

if match:
    print("Código de área:", match.group(1))       # 415
    print("Número:", match.group(2))               # 555-4242

pattern = re.compile(r"gato|perro")
text = "Mi mascota es un perro."

match = pattern.search(text)

if match:
    print("Encontrado:", match.group())


pattern = re.compile(r"colou?r")
text1 = "My favorite color is blue."
text2 = "My favourite colour is blue."

print(pattern.search(text1).group())  # color
print(pattern.search(text2).group())  # colour


pattern = re.compile(r"lo*l")

print(pattern.match("ll"))         # match
print(pattern.match("lol"))        # match
print(pattern.match("loool"))      # match
print(pattern.match("loooooool"))  # match


pattern = re.compile(r"lo+l")

print(pattern.match("lol"))        # match
print(pattern.match("loool"))      # match
print(pattern.match("loooooool"))  # match
print(pattern.match("ll"))         # None


# Número específico de repeticiones
pattern = re.compile(r"\d{3}")
match = pattern.match("123")
print(match.group())  # 123

# Rango de repeticiones
pattern = re.compile(r"\d{2,4}")
match = pattern.match("4567")
print(match.group())  # 4567

# Al menos un número de repeticiones
pattern = re.compile(r"\d{2,}")
match = pattern.match("12345")
print(match.group())  # 12345

# Greedy
pattern = re.compile(r"(Ha){3,5}")
match = pattern.search("HaHaHaHaHa")
print(match.group())  # HaHaHaHaHa

# Not Greedy
pattern = re.compile(r"(Ha){3,5}?")
match = pattern.search("HaHaHaHaHa")
print(match.group())  # HaHaHa


# Definir la expresión regular para un número de teléfono
pattern = re.compile(r'\d{3}-\d{3}-\d{4}')

# Texto en el que buscar
text = "Aquí están los números: 415-555-1234, 408-555-5678, 650-555-9999."

# Usar findall() para obtener todas las coincidencias
matches = pattern.findall(text)

print(matches) # ['415-555-1234', '408-555-5678', '650-555-9999']