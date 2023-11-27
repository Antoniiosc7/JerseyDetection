import os
import cv2
import matplotlib.pyplot as plt

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

def menu4(libreria, filtro, dificultad, directorio):
    # Muestra la lista de imágenes disponibles
    print("Imágenes en el directorio:")
    for i, imagen in enumerate(directorio):
        print(f"{i + 1}. {imagen}")

    # Ingresa el número de la imagen que deseas abrir
    opcion = input("¿Qué imagen deseas abrir? (Ingresa el número): ")

    try:
        opcion = int(opcion)
        if 1 <= opcion <= len(directorio):
            img_seleccionada = directorio[opcion - 1]
            img_path = os.path.join(dificultad, img_seleccionada)
            imagen = cargar_imagen(dificultad, img_seleccionada)

            # Muestra la imagen
            plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
            plt.show()

        else:
            print("Número fuera de rango. Inténtalo de nuevo.")

    except ValueError:
        print("Entrada no válida. Ingresa un número válido.")

if __name__ == "__main__":
    directorio = []
    while not directorio:
        dificultad = input("\nSelecciona una carpeta de imágenes (1, 2 o 3): ")
        directorio = listar_archivos_en_directorio(dificultad)

    menu4("easyocr", 1, dificultad, directorio)
