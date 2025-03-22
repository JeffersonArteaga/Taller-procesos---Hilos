# Arquitectura Cliente servidor
# Jefferson David Arteaga Bedoya
# Taller procesos - hilos Ejercicio 1

import threading

def area_rectangulo(base, altura, resultados, index):
    resultados[index] = base * altura

def area_triangulo(base, altura, resultados, index):
    resultados[index] = (base * altura) / 2

if __name__ == "__main__":
    resultados = [0, 0, 0, 0]  
    
   
    hilo1 = threading.Thread(target=area_triangulo, args=(10, 12, resultados, 0))
    hilo2 = threading.Thread(target=area_rectangulo, args=(8, 12, resultados, 1))
    hilo3 = threading.Thread(target=area_rectangulo, args=(6, 5, resultados, 2))
    hilo4 = threading.Thread(target=area_triangulo, args=(2, 5, resultados, 3))
    
  
    hilo1.start()
    hilo2.start()
    hilo3.start()
    hilo4.start()
    
  
    hilo1.join()
    hilo2.join()
    hilo3.join()
    hilo4.join()
    
    # Calcular área total
    area_total = sum(resultados)
    print(f"El área total de la figura es: {area_total} m²")
