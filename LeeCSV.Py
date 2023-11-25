import pandas as pd
import easyocr
import matplotlib.pyplot as plt
import cv2
import pytesseract
import PIL

db = pd.read_csv("male_players.csv")

selected_columns = ["short_name", "long_name", "club_jersey_number", "nation_jersey_number"]
selected_data = db[selected_columns]
todaLaDB = selected_data.values.tolist()


seleccionada = db["short_name"].values.tolist()

# Imprime la lista resultante
#print(result_list[:100])
#print(seleccionada[:100])
listaApellidos = [max(name.split(), key=len) for name in seleccionada]
print(listaApellidos[:100])

## Trabajo con fotos 

# Instancia de EasyOCR
reader = easyocr.Reader(['en'])  # Especifica el idioma que se va a utilizar
image_path = 'rodrigo.jpg'  # Reemplaza con la ruta de tu imagen
#image_path = 'rodrygo.jpg' 
img = cv2.imread(image_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
result = reader.readtext(img)
player_name = ""
player_number = ""
cajas = pytesseract.image_to_data(img)
for i, caja in enumerate(cajas.splitlines()):
  if i == 0:
      continue
  caja = caja.split('\t')  # Separar usando el tabulador
  if len(caja) == 12:
      x, y, w, h = map(int, caja[6:10])  # Convertir a enteros
      x, y, w, h = x - 1, y - 1, w + 1, h + 1
      cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)

for detection in result:
    text = detection[1]
    if text.isalpha():  # Si el texto contiene solo letras (nombre)
        player_name += text + " "
    elif text.isdigit():  # Si el texto contiene solo dígitos (número)
        player_number = text

# Mostrar los resultados
print("Nombre del jugador:", player_name)
print("Número de la camiseta:", player_number)

# Mostrar la imagen
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
plt.axis('off')
plt.show()

'''
def buscar_coincidencia_con_posicion(lista, nombre_jugador):
    for i, elemento in enumerate(lista):
        if nombre_jugador.lower() in elemento.lower():
            return True, i
    return False, -1
'''
def buscar_coincidencia_con_posicion(lista, nombre_jugador):
    for palabra in nombre_jugador.split():
        for i, elemento in enumerate(lista):
            if palabra.lower() in elemento.lower():
                return True, i
    return False, -1


'''
coincidencia, posicion = buscar_coincidencia_con_posicion(listaApellidos, player_name)
if coincidencia:
    print(f"En esa foto se ha encontrado a {todaLaDB[1][posicion]}. \n En su club lleva el dorsal: {todaLaDB[2][posicion]} ")
else:
    print(f"No se encontró ninguna coincidencia para {player_name}.")
'''
coincidencia, posicion = buscar_coincidencia_con_posicion(listaApellidos, player_name)
if coincidencia:
    print(f"En esa foto se ha encontrado a {db['long_name'].iloc[posicion]}. \n En su club lleva el dorsal: {db['club_jersey_number'].iloc[posicion]} ")
else:
    print(f"No se encontró ninguna coincidencia para {player_name}.")


print("########################### - ###########################")
def buscar_coincidencia_con_posicion(lista, nombre_jugador):
    for palabra in nombre_jugador.split():
        for i, elemento in enumerate(lista):
            if palabra.lower() in elemento.lower():
                return True, i
    return False, -1

# Ejemplo de uso:
coincidencia = False
posicion = -1
for palabra in player_name.split():
    coincidencia, posicion = buscar_coincidencia_con_posicion(listaApellidos, palabra)
    if coincidencia:
        break

if coincidencia:
    print(f"En esa foto se ha encontrado a {db['long_name'].iloc[posicion]}. \n En su club lleva el dorsal: {db['club_jersey_number'].iloc[posicion]} ")
else:
    print(f"No se encontró ninguna coincidencia para {player_name}.")


print("##################### - ###################")




def buscar_coincidencias_con_posiciones(lista, nombre_jugador):
    coincidencias = []
    posiciones_encontradas = set()
    for palabra in nombre_jugador.split():
        for i, elemento in enumerate(lista):
            if palabra.lower() in elemento.lower() and i not in posiciones_encontradas:
                coincidencias.append((palabra, i))
                posiciones_encontradas.add(i)
    return coincidencias

# Ejemplo de uso:
coincidencias = buscar_coincidencias_con_posiciones(listaApellidos, player_name)
if coincidencias:
    for palabra, posicion in coincidencias:
        print(f"En esa foto se ha encontrado a {db['long_name'].iloc[posicion]}. \n En su club lleva el dorsal: {db['club_jersey_number'].iloc[posicion]} para la palabra: {palabra}")
else:
    print(f"No se encontró ninguna coincidencia para {player_name}.")
