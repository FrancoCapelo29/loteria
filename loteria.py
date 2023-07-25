import random

def generar_numero_loteria():
    return random.randint(1000, 9999)

def jugar_loteria_principal():
    numero_loteria = generar_numero_loteria()
    
    eleccion_numeros = input("Ingresa 4 números (separados por espacios): ")
    eleccion_numeros = [int(num) for num in eleccion_numeros.split()]

    