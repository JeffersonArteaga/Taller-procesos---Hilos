# Arquitectura Cliente servidor
# Jefferson David Arteaga Bedoya
# Taller procesos - hilos Ejercicio 6

import threading
import random

def sum_random_numbers(thread_id, results):
    total = sum(random.randint(1, 1000) for _ in range(100))
    results[thread_id] = total
    print(f"Thread {thread_id}: {total}")

def main():
    threads = []
    results = {}
    
    for i in range(10):
        thread = threading.Thread(target=sum_random_numbers, args=(i, results))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    winner = max(results, key=results.get)
    print(f"Winner: Thread {winner} with {results[winner]}")

if __name__ == "__main__":
    main()
