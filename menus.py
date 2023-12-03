import mainFile
import cv2
import os
import matplotlib.pyplot as plt
import cv2

def main():
    while True:
        print("Selecciona una opción:")
        print("1. Libreria easyocr")
        print("2. Libreria kerasOcr")
        print("3. Libreria pytesseract")
        print("4. Mostrar lectura cruda de todas las librerias")
        print("0. Salir")

        opcion = input("Ingresa el número de la opción que deseas: ")

        if opcion == "1":
            print("Has seleccionado la libreria easyocr")
            libreria="easyocr"
            menu2(libreria)
            break
        elif opcion == "2":
            print("Has seleccionado la libreria kerasOcr")
            libreria="kerasOcr"
            menu2(libreria)
            break
        elif opcion == "3":
            print("Has seleccionado la libreria pytesseract")
            libreria="pytesseract"
            menu2(libreria)
            break
        elif opcion == "4":
            print("Has seleccionado ver la lectura de las 4 librerias")
            libreria="todas"
            menu2(libreria)
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
        print("2. Imagenes intermedias")
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
            dificultad="intermedio"
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
    directorio = mainFile.listar_archivos_en_directorio(dificultad)
    print("\nImágenes en el directorio:")
    for i, imagen in enumerate(directorio):
        print(f"{i + 1}. {imagen}")
    opcion = input("¿Qué imagen deseas abrir? (Ingresa el número): ")

    try:
        opcion = int(opcion)
        if 1 <= opcion <= len(directorio):
            img_seleccionada = directorio[opcion - 1]
            imagen = mainFile.cargar_imagen(dificultad, img_seleccionada)
            imagen_filtrada = mainFile.filtrado(filtro, imagen)

            plt.subplot(1,2,1)
            plt.title("Imagen original")
            plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
            plt.subplot(1,2,2)
            plt.title("Imagen con el filtro aplicado")
            plt.imshow(cv2.cvtColor(imagen_filtrada, cv2.COLOR_BGR2RGB))            
            plt.show()

            print("\nTratando de leer la imagen filtrada con la liberia selecionada...")
            resultadoLeeImagen = mainFile.leeImagen(libreria, imagen)
            mainFile.pintaLeeImagen(libreria,resultadoLeeImagen)
            if(len(resultadoLeeImagen[0])>0):
                print("\n Buscando coincidencias en la base de datos de EASport FC 24...")
                mainFile.compruebaDB(resultadoLeeImagen)
            else:
                print("Al no encontrase ningun texto en la imagen, no se pueden buscar coincidencias con la base de datos.")
            menu5()
        else:
            print("Número fuimagenera de rango. Inténtalo de nuevo.")
            menu5()

    except ValueError:
        print("Entrada no válida. Ingresa un número válido.")

def menu5():
    while True:
        print("\n ¿Desea leer una nueva imagen o salir?")
        print("1. Leer nueva imagen")
        print("0. Salir")

        opcion = input("Ingresa el número de la opción que deseas: ")

        if opcion == "1":
            main()
            break
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")