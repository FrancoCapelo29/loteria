import random

def generar_numero_loteria():
    return random.randint(1000, 9999)

def jugar_loteria_principal():
    numero_loteria = generar_numero_loteria()
    
    eleccion_numeros = input("Ingresa 4 números (separados por espacios): ")
    eleccion_numeros = [int(num) for num in eleccion_numeros.split()]

    if len(eleccion_numeros) != 4 or any(num < 0 or num > 9 for num in eleccion_numeros):
        print("Debes ingresar exactamente 4 números entre 0 y 9.")
        return False

    if eleccion_numeros == [int(digit) for digit in str(numero_loteria)]:
        print("¡Felicidades! Has ganado la lotería principal.")
        return True
    else:
        print(f"No acertaste los números. El número ganador era: {numero_loteria}.")
        return False

def jugar_loteria_animal():
    animales = ["perro", "gato", "pájaro", "elefante", "tigre"]
    animal_ganador = random.choice(animales)

    eleccion_animal = input(f"Ingresa el nombre de un animal "
                            f"(puedes elegir entre: {', '.join(animales)}): ")

    if eleccion_animal.lower() == animal_ganador:
        print(f"¡Felicitaciones! Has ganado la lotería del {animal_ganador}.")
    else:
        print(f"Lo siento, el animal ganador era: {animal_ganador}.")

def main():
    print("¡Bienvenido a la lotería! Ingresa 4 números para jugar.")
    
    while True:
        if jugar_loteria_principal():
            jugar_loteria_animal()

        jugar_otra_vez = input("¿Quieres jugar otra vez? (s/n): ")
        if jugar_otra_vez.lower() != 's':
            break

if __name__ == "__main__":
    main()
