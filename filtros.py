import cv2, numpy as np, matplotlib.pyplot as plt
import menus

def filtrado(filtro, imagen):
    if imagen is None or imagen.size == 0:
        # La imagen es nula o vacía
        print("\n Error: La imagen es nula o vacía.")
        print("Volviendo al menú inicial... \n")
        return menus.main()
    elif filtro==1:
        #Blanco y negro
        return cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    elif filtro==2:
        # Filtro de contorno
        contorno = cv2.Canny(imagen, 100, 200)
        return contorno
    elif filtro==3:
         # Mejora del contraste
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        contraste = clahe.apply(gris)
        return contraste
    elif filtro==4:
        # Filtro de suavizado (Gaussiano)
        suavizado = cv2.GaussianBlur(imagen, (5, 5), 0)
        return suavizado
    elif filtro == 5:
        # Filtro de mejora de nitidez (Laplaciano)
        laplaciano = cv2.Laplacian(imagen, cv2.CV_64F) # type: ignore
        mejora_nitidez = np.uint8(np.abs(laplaciano))
        return mejora_nitidez