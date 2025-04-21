"""
Este archivo reproduce los codigos mostrados como ejemplo en el
PDF Python Avanzado: OOP
"""

import time
import threading
import subprocess

now = time.time()
round(now, 2)
round(now, 4)
round(now)


def print_numbers():
    for i in range(5):
        print(f"Número: {i}")
        time.sleep(1)

def print_letters():
    for letter in 'ABCDE':
        print(f"Letra: {letter}")
        time.sleep(1)

# Crear los hilos
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Iniciar los hilos
thread1.start()
thread2.start()

# Esperar a que terminen
thread1.join()
thread2.join()

print("Tareas finalizadas.")


# Abrir el Bloc de notas (en Windows)
subprocess.Popen(['notepad.exe'])
subprocess.Popen(['notepad.exe', 'documento.txt'])
