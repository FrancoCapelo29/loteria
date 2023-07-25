def mascotas_premiadas(mascota_ingresada):
    mascotas_ganadoras = {
        "ornitorinco": "es la mascota ganadora",
        "pato": "estás en el segundo lugar",
        "lagarto" : "tercer lugar"
    }

    premio = mascotas_ganadoras.get(mascota_ingresada)
    if premio:
        print(f"{mascota_ingresada}, {premio}.")
    else:
        print("Buena suerte para la próxima vez!")

nombre_mascota = input("Ingresa el nombre de un animal: ")


mascotas_premiadas(nombre_mascota.lower())  