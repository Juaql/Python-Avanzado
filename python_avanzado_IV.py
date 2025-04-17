"""
Este archivo reproduce los codigos mostrados como ejemplo en el
PDF Python Avanzado: OOP
"""

import os
import shutil

# shutil.copy()

shutil.copy('C:\\spam.txt', 'C:\\delicious')

# shutil.move()
shutil.move('C:\\MisArchivos\\documento.txt', 'C:\\Backup')

# shutil.move() cambiar nombre
shutil.move('C:\\MisArchivos\\documento.txt', 'C:\\Backup\\documento_respaldo.txt')

# Borrar archivos y carpetas de manera permanente

os.unlink('C:\\archivos\\archivo.txt')

os.rmdir('C:\\archivos\\carpeta_vacia')

shutil.rmtree('C:\\archivos\\carpeta_contenido')

#Recorrer un árbol de directorios
for folderName, subfolders, filenames in os.walk('C:\\MiCarpeta'):
    print(f'Carpeta actual: {folderName}')
    
    for subfolder in subfolders:
        print(f'  Subcarpeta de {folderName}: {subfolder}')
        
    for filename in filenames:
        print(f'  Archivo en {folderName}: {filename}')
