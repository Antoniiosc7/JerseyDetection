import cv2, filtros, mainFile
import matplotlib.pyplot as plt

def eligeDirectorio():
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
            eligeFoto(dificultad)
            break
        elif opcion == "2":
            print("Has seleccionado la dificultad intermedia")
            dificultad="intermedio"
            eligeFoto(dificultad)
            break
        elif opcion == "3":
            print("Has seleccionado la dificultad dificil")
            dificultad="dificil"
            eligeFoto(dificultad)
            break
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def eligeFoto(dificultad):
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
            imagen_filtrada1 = filtros.filtrado(1, imagen)
            imagen_filtrada2 = filtros.filtrado(2, imagen)
            imagen_filtrada3 = filtros.filtrado(3, imagen)
            imagen_filtrada4 = filtros.filtrado(4, imagen)
            imagen_filtrada5 = filtros.filtrado(5, imagen)
            leeimagen = str(mainFile.easyOcr(imagen))
            leeimagen1 = str(mainFile.easyOcr(imagen_filtrada1))
            leeimagen2 = str(mainFile.easyOcr(imagen_filtrada2))
            leeimagen3 = str(mainFile.easyOcr(imagen_filtrada3))
            leeimagen4 = str(mainFile.easyOcr(imagen_filtrada4))
            leeimagen5 = str(mainFile.easyOcr(imagen_filtrada5))
            plt.subplot(2, 3, 1)
            plt.title("Original")
            plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
            plt.text(0.5, -0.1, leeimagen, horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
            plt.axis('off')
            print("Lectura imagen original: \n PyTesseract: " + str(mainFile.pyTesseractCrudo(imagen)) + "\n easyOcr: " + leeimagen)
            
            plt.subplot(2, 3, 2)
            plt.title("Blanco y negro")
            plt.imshow(imagen_filtrada1, cmap='gray')
            plt.text(0.5, -0.1, leeimagen1, horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
            plt.axis('off')
            print("Lectura imagen blanca y negra: \n PyTesseract: " + str(mainFile.pyTesseractCrudo(imagen_filtrada1)) + "\n easyOcr: " + leeimagen1)
            
            plt.subplot(2, 3, 3)
            plt.title("contorno")
            plt.imshow(imagen_filtrada2, cmap='gray')
            plt.text(0.5, -0.1, leeimagen2, horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
            plt.axis('off')
            print("Lectura imagen con contorno: \n PyTesseract: " + str(mainFile.pyTesseractCrudo(imagen_filtrada2)) + "\n easyOcr: " + leeimagen2)
            
            # Segunda fila
            plt.subplot(2, 3, 4)
            plt.title("Contraste")
            plt.imshow(imagen_filtrada3, cmap='gray')
            plt.text(0.5, -0.1, leeimagen3, horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
            plt.axis('off')
            print("Lectura imagen con mejora del contraste: \n PyTesseract: " + str(mainFile.pyTesseractCrudo(imagen_filtrada3)) + "\n easyOcr: " + leeimagen3)
            
            plt.subplot(2, 3, 5)
            plt.title("Gaussiano")
            plt.imshow(imagen_filtrada4, cmap='gray')
            plt.text(0.5, -0.1, leeimagen4, horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
            plt.axis('off')
            print("Lectura imagen suavizada (Gaussiano): \n PyTesseract: " + str(mainFile.pyTesseractCrudo(imagen_filtrada4)) + "\n easyOcr: " + leeimagen4)
            
            plt.subplot(2, 3, 6)
            plt.title("Laplaciano")
            plt.imshow(imagen_filtrada5, cmap='gray')
            plt.text(0.5, -0.1, leeimagen5, horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
            plt.axis('off')            
            print("Lectura de mejora de nitidez Laplaciano: \n PyTesseract: " + str(mainFile.pyTesseractCrudo(imagen_filtrada5)) + "\n easyOcr: " + leeimagen5)
                  
            plt.show()
            menuFinal()

        else:
            print("Número fuimagenera de rango. Inténtalo de nuevo.")
            menuFinal()

    except ValueError:
        print("Entrada no válida. Ingresa un número válido.")

def menuFinal():
    while True:
        print("\n ¿Desea leer una nueva imagen o salir?")
        print("1. Leer nueva imagen")
        print("0. Salir")

        opcion = input("Ingresa el número de la opción que deseas: ")

        if opcion == "1":
            eligeDirectorio()
            break
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    eligeDirectorio()