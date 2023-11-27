import pandas as pd
import easyocr
import cv2
import pytesseract
import os
import matplotlib.pyplot as plt
import cv2


def listar_archivos_en_directorio(ruta):
    try:
        # Listar todos los archivos en el directorio
        archivos = os.listdir(ruta)

        # Mostrar los nombres de los archivos
        print("Archivos en el directorio:")
        for archivo in archivos:
            print(archivo)

        return archivos

    except FileNotFoundError:
        print(f"Directorio no encontrado: {ruta}")
        return []

def cargar_imagen(ruta_directorio, nombre_imagen):
    ruta_completa = os.path.join(ruta_directorio, nombre_imagen)
    imagen = cv2.imread(ruta_completa)
    return imagen

def cargar_imagen(ruta_directorio, nombre_imagen):
    ruta_completa = os.path.join(ruta_directorio, nombre_imagen)
    imagen = cv2.imread(ruta_completa)
    return imagen


def menu_principal():
    print("\nSeleccione una opción:")
    print("1. Ejecutar Función 1")
    print("2. Ejecutar Función 2")
    print("3. Ejecutar Función 3")
    print("0. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    return opcion

def main():
    while True:
        print("Selecciona una opción:")
        print("1. Libreria easyocr")
        print("2. Libreria ____")
        print("3. Libreria pytesseract")
        print("0. Salir")

        opcion = input("Ingresa el número de la opción que deseas: ")

        if opcion == "1":
            print("Has seleccionado la libreria easyocr")
            libreria="easyocr"
            menu2(libreria)
            break
        elif opcion == "2":
            print("Has seleccionado la libreria ____")
            libreria="easyocr"
            menu2(libreria)
            break
        elif opcion == "3":
            print("Has seleccionado la libreria pytesseract")
            libreria="easyocr"
            menu2(libreria)
            break
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def menu2(libreria):
    while True:
        print("\n Ahora, selecciona un filtro para leer la imagen:")
        print("1. Filtro 1")
        print("2. Filtro 2")
        print("3. Filtro 3")
        print("4. Filtro 4")
        print("0. Salir")

        opcion = input("Ingresa el número de la opción que deseas: ")

        if opcion == "1":
            print("Has seleccionado el filtro 1")
            filtro=1
            menu3(libreria, filtro)
            break
        elif opcion == "2":
            print("Has seleccionado el filtro 2")
            filtro=2
            menu3(libreria, filtro)
            break
        elif opcion == "3":
            print("Has seleccionado el filtro 3")
            filtro=3
            menu3(libreria, filtro)
            break
        elif opcion == "4":
            print("Has seleccionado el filtro 4")
            filtro=4
            menu3(libreria, filtro)
            break
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def menu3(libreria, filtro):
    while True:
        print("\n Ahora, selecciona una carpeta de imagenes:")
        print("1. Imágenes faciles de leer")
        print("2. Imagenes no muy faciles")
        print("3. Varias camisetas")
        print("0. Salir")

        opcion = input("Ingresa el número de la opción que deseas: ")

        if opcion == "1":
            print("Has seleccionado la dificultad facil")
            dificultad="facil"
            menu4(libreria, filtro, dificultad)
            break
        elif opcion == "2":
            print("Has seleccionado la dificultad intermedia")
            dificultad="intermedia"
            menu4(libreria, filtro, dificultad)
            break
        elif opcion == "3":
            print("Has seleccionado la dificultad dificil")
            dificultad="dificil"
            menu4(libreria, filtro, dificultad)
            break
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def menu4(libreria, filtro, dificultad):
    directorio = listar_archivos_en_directorio(dificultad)
    print("Imágenes en el directorio:")
    for i, imagen in enumerate(directorio):
        print(f"{i + 1}. {imagen}")
    opcion = input("¿Qué imagen deseas abrir? (Ingresa el número): ")

    try:
        opcion = int(opcion)
        if 1 <= opcion <= len(directorio):
            img_seleccionada = directorio[opcion - 1]
            img_path = os.path.join(dificultad, img_seleccionada)
            imagen = cargar_imagen(dificultad, img_seleccionada)

            plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
            plt.show()

        else:
            print("Número fuera de rango. Inténtalo de nuevo.")

    except ValueError:
        print("Entrada no válida. Ingresa un número válido.")

if __name__ == "__main__":
    main()
