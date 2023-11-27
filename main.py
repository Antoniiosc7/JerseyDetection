import pandas as pd
import easyocr
import matplotlib.pyplot as plt
import cv2
import pytesseract
import PIL


def main():
    # ----------------------- lee bd ----------------------- #
    db = pd.read_csv("male_players.csv")
    selected_columns = ["short_name", "long_name", "club_jersey_number", "nation_jersey_number"]
    selected_data = db[selected_columns]
    todaLaDB = selected_data.values.tolist()
    seleccionada = db["short_name"].values.tolist()
    listaApellidos = [max(name.split(), key=len) for name in seleccionada]
    # -------------------------- . -------------------------- #
    ruta = input("\n Ingresa el nombre de la foto que deseas abrir: ")
    #ruta="rodrigo.jpg"
    nombre, dorsal = easyOcr(ruta)

    escribeResultadoEasyOcr(nombre, dorsal)
    print("")
 
    coincidencias = buscar_coincidencias_con_posiciones(listaApellidos, nombre, dorsal, db)
    print(coincidencias)
    if coincidencias:
        listaFin=listaResultante(coincidencias,db,dorsal)
        print(listaFin)
        print(listaFin[0][0])
    else:
        print(f"No se encontró ninguna coincidencia para {nombre}.")



    
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#- 
def listaResultante(coincidencias,db, dorsal):
    lista = []
    if(dorsal!=""):
        if coincidencias:
            for a, posicion in coincidencias:
                nonbreCompleto=db['long_name'].iloc[posicion]
                dorsalJugador= db['club_jersey_number'].iloc[posicion]
                dorsalSeleccion = db['nation_jersey_number'].iloc[posicion]
                if int(dorsal)==int(dorsalJugador):
                    b=(nonbreCompleto, int(dorsalJugador))
                    lista.append(b)            

    return lista


def buscar_coincidencias_con_posiciones(lista, nombre_jugador, dorsal, db):
    coincidencias = []
    posiciones_encontradas = set()

    for palabra in nombre_jugador.split():
        for i, elemento in enumerate(lista):
            if palabra.lower() in elemento.lower() and i not in posiciones_encontradas:
                coincidencias.append((palabra, i))
                posiciones_encontradas.add(i)
    return coincidencias



def filtroImagen(imagen):
    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    return gray

def easyOcr(ruta):
    nombre = ""
    dorsal = ""
    reader = easyocr.Reader(['en'])
    img = cv2.imread(ruta)
    #img = filtroImagen(img) Descomentar esto cuando tengamos un filtro bueno
    result = reader.readtext(img)
    cajas = pytesseract.image_to_data(img)
    for i, caja in enumerate(cajas.splitlines()):
        if i == 0:
            continue
        caja = caja.split('\t') 
        if len(caja) == 12:
            x, y, w, h = map(int, caja[6:10]) 
            x, y, w, h = x - 1, y - 1, w + 1, h + 1
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)

    for detection in result:
        text = detection[1]
        if text.isalpha(): 
            nombre += text + " "
        elif text.isdigit(): 
            dorsal = text
    return [nombre, dorsal]

def escribeResultadoEasyOcr(nombre, dorsal):
    if(len(nombre)>1):
        print("La libreria easyOCR ha detectado el siguiente texto: " + nombre)
    else:
        print("No se ha encontrado texto")
    if(dorsal != ""):
        print("La libreria easyOCR ha detectado el siguiente numero: " + str(dorsal))
    else:
        print("No se ha encontrado ningun numero")



if __name__ == "__main__":
    main()