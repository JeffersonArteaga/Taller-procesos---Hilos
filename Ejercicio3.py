# Arquitectura Cliente servidor
# Jefferson David Arteaga Bedoya
# Taller procesos - hilos Ejercicio 3

import threading
import time

def genera_eventos():
    for _ in range(5):
        time.sleep(2)
        ev.set()
    ev_fin.set()  # Indicar que se han generado todos los eventos

def escribe_algo():
    while True:
        ev.wait()
        print("hola")
        ev.clear()
        if ev_fin.is_set():  # Verificar si se ha terminado la generación de eventos
            break

ev = threading.Event()
ev_fin = threading.Event()

T1 = threading.Thread(target=genera_eventos)
T2 = threading.Thread(target=escribe_algo)

T1.start()
T2.start()

T1.join()
T2.join()  # Esperar a que ambos hilos terminen antes de salir
