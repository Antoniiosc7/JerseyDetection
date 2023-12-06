#Calderon haz algo.
import cv2

def filtrado(filtro, imagen):
    if filtro==1:
        #Blanco y negro
        return cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    elif filtro==2:
        pass
    elif filtro==3:
        pass
    elif filtro==4:
        pass