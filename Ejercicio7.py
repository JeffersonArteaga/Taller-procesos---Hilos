# Arquitectura Cliente servidor
# Jefferson David Arteaga Bedoya
# Taller procesos - hilos Ejercicio 7

import os
import psutil

def list_processes():
    print("PID\tProcess Name")
    print("---------------------------")
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            print(f"{proc.info['pid']}\t{proc.info['name']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

def kill_process(pid):
    try:
        os.kill(pid, 9)
        print(f"Process {pid} terminated successfully.")
    except ProcessLookupError:
        print(f"Process {pid} not found.")
    except PermissionError:
        print(f"Permission denied to terminate process {pid}.")

def main():
    list_processes()
    try:
        pid = int(input("Enter the PID of the process to terminate: "))
        kill_process(pid)
    except ValueError:
        print("Invalid input. Please enter a valid PID.")

if __name__ == "__main__":
    main()
