import pandas as pd
import easyocr
import cv2
import pytesseract
import os
import matplotlib.pyplot as plt
import cv2
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

def filtrado(filtro, imagen):
    if filtro==1:
        return cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    elif filtro==2:
        pass
    elif filtro==3:
        pass
    elif filtro==4:
        pass
    
def leeImagen(libreria, imagen):
    if libreria == "easyocr":
        return easyOcr(imagen)
    elif libreria == "pytesseract":
        return pyTesseract(imagen)
    elif libreria == "kerasocr":
        return kerasOcr(imagen)
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
        if len(resultadoLeeImagen[0]) > 0 and len(resultadoLeeImagen[1]) > 0:
            print("Texto encontrado en la imagen: " + resultadoLeeImagen[0])
            print("Numeros encontrados en la imagen: " + resultadoLeeImagen[1])
        elif len(resultadoLeeImagen[0]) > 0:
            print("Texto encontrado en la imagen: " + resultadoLeeImagen[0])
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

import keras_ocr

def kerasOcr(img):
    nombre = ""
    dorsal = ""
    pipeline = keras_ocr.pipeline.Pipeline()
    prediction_groups = pipeline.recognize([img])
    for predictions in prediction_groups:
        for text_result in predictions:
            text = text_result[0]
            if text.isalpha():
                nombre += text + " "
            elif text.isdigit():
                dorsal = text
    
    return [nombre, dorsal]

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

    cv2.imwrite("original_con_rectangulos.png", img)
    
    return [textoRes, dorsal, img]

def imprimir_jugadores_y_equipos_sin_repetir(filas, dataframe):
    long_names = dataframe.loc[filas, "long_name"].tolist()
    long_names_sin_repetir = list(set(long_names))

    for long_name in long_names_sin_repetir:
        fila = dataframe[dataframe["long_name"] == long_name].iloc[0]
        equipo = fila["club_name"]
        dorsalEquipo = fila["club_jersey_number"]
        print(f"Jugador detectado: {long_name}, lleva el número {dorsalEquipo} en el equipo: {equipo}")

def buscar_por_dorsal(db, dorsal, filas_a_comprobar):
    return [i for i, fila in enumerate(db.itertuples()) if i in filas_a_comprobar and (lambda x: x if x is None else int(x))(getattr(fila, "club_jersey_number")) == int(dorsal)]

def encontrar_jugadores(cadena, listaJugadores):
    cadena_minusculas = (str(cadena)).lower()
    posiciones = [i for i, jugador in enumerate(listaJugadores) if jugador.lower() in cadena_minusculas]
    return posiciones

def compruebaDB(string):
    db = pd.read_csv("male_players.csv")
    selected_columns = ["short_name", "long_name", "club_jersey_number", "nation_jersey_number", "club_name"]
    selected_data = db[selected_columns]
    seleccionada = db["short_name"].values.tolist()
    listaApellidos = [max(name.split(), key=len) for name in seleccionada]
    selected_data["apellidos"] = listaApellidos

    dorsal = (string[1])
    resultado = encontrar_jugadores(string[0], listaApellidos)
    if len(resultado) > 1 and dorsal and any(str(d).isdigit() for d in dorsal):
        res=buscar_por_dorsal(selected_data, dorsal, resultado)
        imprimir_jugadores_y_equipos_sin_repetir(res, selected_data)
    else:
        print(int(str(dorsal)))
        imprimir_jugadores_y_equipos_sin_repetir(resultado, selected_data)
            
if __name__ == "__main__":
    db = pd.read_csv("male_players.csv")
    selected_columns = ["short_name", "long_name", "club_jersey_number", "nation_jersey_number", "club_name"]
    selected_data = db[selected_columns]
    seleccionada = db["short_name"].values.tolist()
    listaApellidos = [max(name.split(), key=len) for name in seleccionada]
    selected_data["apellidos"] = listaApellidos
    menus.main()