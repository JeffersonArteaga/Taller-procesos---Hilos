# Arquitectura Cliente servidor
# Jefferson David Arteaga Bedoya
# Taller procesos - hilos Ejercicio 4


import threading
import time
import logging
import random
import queue

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s')

BUF_SIZE = 10
q = queue.Queue(BUF_SIZE)

class HiloProductor(threading.Thread):
    def __init__(self, stop_event, name=None):
        super(HiloProductor, self).__init__()
        self.name = name
        self.stop_event = stop_event  # Evento para detener el hilo

    def run(self):
        while not self.stop_event.is_set():
            try:
                item = random.randint(1, 10)
                q.put(item, timeout=1)  # Bloquea hasta 1 segundo si está llena
                logging.debug(f'Insertando "{item}" : {q.qsize()} elementos en la cola')
                time.sleep(random.random())
            except queue.Full:
                logging.debug("Cola llena, esperando...")
        logging.debug("Finalizando productor.")

class HiloConsumidor(threading.Thread):
    def __init__(self, stop_event, name=None):
        super(HiloConsumidor, self).__init__()
        self.name = name
        self.stop_event = stop_event  # Evento para detener el hilo

    def run(self):
        while not self.stop_event.is_set() or not q.empty():
            try:
                item = q.get(timeout=1)  # Bloquea hasta 1 segundo si está vacía
                logging.debug(f'Sacando "{item}" : {q.qsize()} elementos en la cola')
                time.sleep(random.random())
            except queue.Empty:
                logging.debug("Cola vacía, esperando...")
        logging.debug("Finalizando consumidor.")

# Evento para detener los hilos
stop_event = threading.Event()

# Crear hilos
p1 = HiloProductor(stop_event, name='Productor1')
p2 = HiloProductor(stop_event, name='Productor2')
c = HiloConsumidor(stop_event, name='Consumidor')

# Iniciar hilos
p1.start()
p2.start()
c.start()

# Ejecutar por un tiempo y luego detener
time.sleep(5)
stop_event.set()

# Esperar a que los hilos terminen
p1.join()
p2.join()
c.join()

logging.debug("Finalización del programa.")
