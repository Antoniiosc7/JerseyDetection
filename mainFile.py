import pandas as pd
import cv2
import pytesseract, easyocr, keras_ocr
import os
import matplotlib.pyplot as plt
import menus

def listar_archivos_en_directorio(ruta):
    try:
        archivos = os.listdir(ruta)
        print("\nArchivos en el directorio:")
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

   
def leeImagen(libreria, imagen):
    if libreria == "easyocr":
        return easyOcr(imagen)
    elif libreria == "pytesseract":
        return pyTesseract(imagen)
    elif libreria == "kerasocr":
        return keras0cr("facil/navas.png")
    elif libreria == "todas":
        pass

def clasificar_elementos(cadena):
    palabras = []
    numeros = []
    elementos = cadena.split()
    for elemento in elementos:
        try:
            numero = float(elemento)
            numeros.append(numero)
        except ValueError:
            palabras.append(elemento)

    if not palabras and numeros:
        return numeros
    elif palabras and not numeros:
        return palabras
    else:
        return palabras, numeros
    
def pintaLeeImagen(libreria, resultadoLeeImagen):
    if libreria == "easyocr":
        if len(resultadoLeeImagen[0]) > 0 and len(resultadoLeeImagen[1]) > 0:
            print("Texto encontrado en la imagen: " + resultadoLeeImagen[0])
            print("Numeros encontrados en la imagen: " + resultadoLeeImagen[1])
        elif len(resultadoLeeImagen[0]) > 0:
            print("Texto encontrado en la imagen: " + resultadoLeeImagen[0])
        else:
            print("No se ha podido leer nada en la foto")
    elif libreria == "pytesseract":
        if len(resultadoLeeImagen[0]) > 0 and len(resultadoLeeImagen[1]) > 0 and len(resultadoLeeImagen[2]) > 0:
            plt.title("Imagen clasificada")
            plt.imshow(resultadoLeeImagen[2])
            plt.show()
            print("Texto encontrado en la imagen: " + str(resultadoLeeImagen[0]))
            print("Numeros encontrados en la imagen: " + str(resultadoLeeImagen[1]))
        elif len(resultadoLeeImagen[0]) > 0 and len(resultadoLeeImagen[2]) > 0:
            plt.title("Imagen clasificada")
            plt.imshow(resultadoLeeImagen[2])
            plt.show()
            print("Texto encontrado en la imagen: " + resultadoLeeImagen[0])
            print("No se ha encontrado dorsal")
        elif len(resultadoLeeImagen[0]) > 0:
            print("Texto encontrado en la imagen: " + resultadoLeeImagen[0])
            print("ha entrado aqui")
            print(len(resultadoLeeImagen[1]))
        else:
            print("No se ha podido leer nada en la foto")
    elif libreria == "kerasocr":
        if resultadoLeeImagen:
            print("Texto encontrado en la imagen: " + resultadoLeeImagen)
        else:
            print("No se ha podido leer nada en la foto")

def easyOcr(img):
    nombre = ""
    dorsal = ""
    reader = easyocr.Reader(['en'])
    result = reader.readtext(img)
    for detection in result:
        text = detection[1]
        if text.isalpha(): 
            nombre += text + " "
        elif text.isdigit(): 
            dorsal = text
    return [nombre, dorsal]

def keras0cr(img):
    nombre = ""
    dorsal = ""
        # Cargar el modelo OCR
    pipeline = keras_ocr.pipeline.Pipeline()
        # Reconocer texto en la imagen
    prediction_groups = pipeline.recognize([img])
    
    for predictions in prediction_groups:
        for text_result in predictions:
            text = text_result[0]
            if text.isalpha():
                nombre += text + " "
            elif text.isdigit():
                dorsal = text
    return [nombre, dorsal]
def easyOcrCrudo(img):
    imagen = cv2.imread('ruta/a/tu/imagen.jpg')
    lector_ocr = easyocr.Reader(['en'], gpu=True) 
    return lector_ocr.readtext(img)

def pyTesseractCrudo(img):
    return pytesseract.image_to_string(img)
 
def pyTesseract(img):
    texto = pytesseract.image_to_string(img)
    cajas = pytesseract.image_to_data(img)
    for i, caja in enumerate(cajas.splitlines()):
        if i == 0:
            continue
        caja = caja.split('\t')  # Separar usando el tabulador
        if len(caja) == 12:
            x, y, w, h = map(int, caja[6:10])  # Convertir a enteros
            # Ajustar las coordenadas para centrar los rectángulos en el texto
            x, y, w, h = x - 1, y - 1, w + 1, h + 1
            # Dibujar rectángulos alrededor del texto (en rosa)
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
    textoRes, dorsal = clasificar_elementos(texto)    
    return [textoRes, dorsal, img]
            
if __name__ == "__main__":
    menus.main()