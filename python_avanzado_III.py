"""
Este archivo reproduce los codigos mostrados como ejemplo en el
PDF Python Avanzado: OOP
"""

import os

os.getcwd() # 'C:\\Python34'

os.chdir('C:\\Windows\\System32')
os.getcwd() # 'C:\\Windows\\System32'

ruta = 'C:/Windows/System32'
print(os.path.exists(ruta)) # True si existe, False si no

archivo = 'C:/Windows/System32/notepad.exe'
print(os.path.isfile(archivo)) # True si es archivo, False si no

carpeta = 'C:/Windows/System32'
print(os.path.isdir(carpeta)) # True si es carpeta, False si no

ruta_completa = 'C:/Users/Usuario/Documentos/proyecto/final.py'

directorio, archivo = os.path.split(ruta_completa)

print("Directorio:", directorio)
print("Archivo:", archivo)

archivo = 'C:/Users/Usuario/Documents/ejemplo.txt'
tamaño = os.path.getsize(archivo)

print(f"El tamaño del archivo es: {tamaño} bytes")

carpeta = 'C:/Users/Usuario/Documentos'
contenido = os.listdir(carpeta)

print("Contenido de la carpeta:")
for elemento in contenido:
    print(elemento)

ruta = 'C:/Users/Usuario/Documentos/ejemplo.txt'

# Verificar si la ruta existe
if os.path.exists(ruta):
    print("La ruta existe.")
else:
    print("La ruta no existe.")

# Verificar si el archivo existe
if os.path.isfile(ruta):
    print("Es un archivo.")
else:
    print("No es un archivo.")

# Verificar si la carpeta existe
if os.path.isdir(ruta):
    print("Es una carpeta.")
else:
    print("No es una carpeta.")

