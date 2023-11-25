import pandas as pd
import easyocr
import matplotlib.pyplot as plt
import cv2
import pytesseract
db = pd.read_csv("male_players.csv")

selected_columns = ["short_name", "long_name", "club_jersey_number", "nation_jersey_number"]
selected_data = db[selected_columns]
result_list = selected_data.values.tolist()


seleccionada = db["short_name"].values.tolist()

# Imprime la lista resultante
#print(result_list[:100])
#print(seleccionada[:100])
listaApellidos = [max(name.split(), key=len) for name in seleccionada]
print(listaApellidos[:100])

## Trabajo con fotos

# Instancia de EasyOCR
reader = easyocr.Reader(['en'])  # Especifica el idioma que se va a utilizar

# Carga de la imagen de la camiseta (asegúrate de subir la imagen a Google Colab)
image_path = 'navas.png'  # Reemplaza con la ruta de tu imagen
img = cv2.imread(image_path)

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Obtener el texto de la imagen usando EasyOCR
result = reader.readtext(gray)

# Filtrar el texto para obtener el nombre y el número
player_name = ""
player_number = ""
#Detección de cajas

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

####
plt.imshow("navas.png")