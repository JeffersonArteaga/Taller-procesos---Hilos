# Arquitectura Cliente servidor
# Jefferson David Arteaga Bedoya
# Taller procesos - hilos Ejercicio 2

import threading

def secuencia_compartida(n1, n2):
    if n1 < n2:
        print(f"Secuencia compartida: {list(range(n1, n2 + 1))}")
    else:
        print("n1 debe ser menor que n2")

if __name__ == "__main__":
    n1 = int(input("Ingrese el primer número (n1): "))
    n2 = int(input("Ingrese el segundo número (n2): "))
    
    hilo = threading.Thread(target=secuencia_compartida, args=(n1, n2))
    hilo.start()
    hilo.join()  
    
    print(f"Resta (n2 - n1): {n2 - n1}")