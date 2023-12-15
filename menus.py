import mainFile, cv2, filtros, comparacionBD, comparativaGlobal
import matplotlib.pyplot as plt

def opcion():
    while True:
        print("¿Desea usar filtros y librerias indivualmente o todos a la vez?")
        print("\nINFO: La comparación con jugadores de la BD de EA Sports solo ")
        print("       está disponible con el uso de la libreria 'easyOcr' y ")
        print("       filtros individuales")
        print("\n1. De forma individual")
        print("2. Todos los filtros y librerias")
        print("0. Salir")

        opcion = input("Ingresa el número de la opción que deseas: ")

        if opcion == "1":
            print("Has seleccionado de forma individual")
            main()
            break
        elif opcion == "2":
            print("Has seleccionado todos los filtros y galerias")
            comparativaGlobal.eligeDirectorio()            
            break
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def main():
    while True:
        print("\nSelecciona una opción:")
        print("1. Libreria easyocr")
        print("2. Libreria pytesseract")
        print("3. Mostrar lectura cruda de todas las librerias")
        print("0. Salir")

        opcion = input("Ingresa el número de la opción que deseas: ")

        if opcion == "1":
            print("Has seleccionado la libreria easyocr")
            libreria="easyocr"
            menu2(libreria)
            break
        elif opcion == "2":
            print("Has seleccionado la libreria pytesseract")
            libreria="pytesseract"
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
        print("1. Filtro blanco y negro")
        print("2. Filtro de contorno")
        print("3. Filtro mejora del contraste")
        print("4. Filtro de suavizado Gaussiano")
        print("5. Filtro de mejora de nitidez (Laplaciano)")
        print("0. Salir")

        opcion = input("Ingresa el número de la opción que deseas: ")

        if opcion == "1":
            print("Has seleccionado el filtro blanco y negro")
            filtro=1
            menu3(libreria, filtro)
            break
        elif opcion == "2":
            print("Has seleccionado el filtro de mejora del contraste")
            filtro=2
            menu3(libreria, filtro)
            break
        elif opcion == "3":
            print("Has seleccionado el filtro de contraste")
            filtro=3
            menu3(libreria, filtro)
            break
        elif opcion == "4":
            print("Has seleccionado el filtro Gaussiano")
            filtro=4
            menu3(libreria, filtro)
            break
        elif opcion == "5":
            print("Has seleccionado el filtro Laplaciano")
            filtro=5
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
        print("3. Imagenes dificiles")
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
            imagen_filtrada = filtros.filtrado(filtro, imagen)

            plt.subplot(1,2,1)
            plt.title("Imagen original")
            plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
            plt.subplot(1,2,2)
            plt.title("Imagen con el filtro aplicado")
            plt.imshow(imagen_filtrada)             # type: ignore
            plt.show()

            print("\nTratando de leer la imagen filtrada con la liberia selecionada...")
            resultadoLeeImagen = mainFile.leeImagen(libreria, imagen_filtrada)
            mainFile.pintaLeeImagen(libreria,resultadoLeeImagen)
            if libreria == "easyocr":
                if(len(str(resultadoLeeImagen)[0])>0):
                    print("\n Buscando coincidencias en la base de datos de EASport FC 24...")
                    comparacionBD.compruebaDB(resultadoLeeImagen)
                else:
                    print("Al no encontrase ningun texto en la imagen, no se pueden buscar coincidencias con la base de datos.")
            menu5()
        else:
            print("Número fuera de rango. Inténtalo de nuevo.")
            menu5()

    except ValueError:
        print("Entrada no válida. Ingresa un número válido.")

def menu5():
    while True:
        print("\n ¿Desea leer una nueva imagen o salir?")
        print("1. Leer nueva imagen")
        print("0. Salir")

        opcion = input("Ingresa el número de la opción que deseas: ")
        opcion = int(opcion)
        if opcion == 1:
            main()
            break
        elif opcion == 0:
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")