# Arquitectura Cliente servidor
# Jefferson David Arteaga Bedoya
# Taller procesos - hilos Ejercicio 9

from datetime import datetime, timedelta
import time
import uuid
import random
from concurrent.futures import ThreadPoolExecutor

class OrdersManager:
    __orders = []
    __orders_processed = 0
    __last_printed_log = datetime.now()

    def __init__(self) -> None:
        self.__generate_fake_orders(quantity=1_000)

    def __generate_fake_orders(self, quantity):
        self.__log(f"Generating fake orders")
        self.__orders = [(uuid.uuid4(), x) for x in range(quantity)]
        self.__log(f"{len(self.__orders)} generated...")

    def __log(self, message):
        print(f"{datetime.now()} > {message}")

    def __fake_save_on_db(self, order):
        id, number = order
        time.sleep(random.uniform(0, 1))  # Simulación de tiempo de procesamiento
        return f"Order [{id}] {number} was successfully prosecuted."

    def process_orders(self):
        with ThreadPoolExecutor(max_workers=10) as executor:  # Ejecutar en paralelo con 10 hilos
            results = list(executor.map(self.__fake_save_on_db, self.__orders))

        self.__orders_processed = len(self.__orders)
        self.__log(f"Total orders executed: {self.__orders_processed}/{len(self.__orders)}")

# ---
orders_manager = OrdersManager()

start_time = time.time()
orders_manager.process_orders()
delay = time.time() - start_time

print(f"{datetime.now()} > Tiempo de ejecución: {delay:.2f} segundos...")
