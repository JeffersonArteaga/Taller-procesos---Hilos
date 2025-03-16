# Arquitectura Cliente servidor
# Jefferson David Arteaga Bedoya
# Taller procesos - hilos Ejercicio 5

import threading
import random
import time

def generate_numbers(numbers, lock, event):
    while not event.is_set():
        with lock:
            numbers.append(random.randint(1, 100))
        time.sleep(0.01)

def replace_zeros(numbers, lock, event):
    while not event.is_set():
        with lock:
            for i in range(len(numbers)):
                if numbers[i] % 10 == 0:
                    numbers[i] = -1
        time.sleep(0.01)

def monitor_sum(numbers, lock, event, start_time):
    while not event.is_set():
        with lock:
            if sum(numbers) > 20000:
                event.set()
                elapsed_time = time.time() - start_time
                print(f"Limit exceeded in {elapsed_time:.2f} seconds.")
        time.sleep(0.01)

def main():
    numbers = []
    lock = threading.Lock()
    stop_event = threading.Event()
    start_time = time.time()
    
    generator_thread = threading.Thread(target=generate_numbers, args=(numbers, lock, stop_event))
    replacer_thread = threading.Thread(target=replace_zeros, args=(numbers, lock, stop_event))
    monitor_thread = threading.Thread(target=monitor_sum, args=(numbers, lock, stop_event, start_time))
    
    generator_thread.start()
    replacer_thread.start()
    monitor_thread.start()
    
    generator_thread.join()
    replacer_thread.join()
    monitor_thread.join()
    
    print("Process terminated as the sum exceeded 20000.")

if __name__ == "__main__":
    main()
