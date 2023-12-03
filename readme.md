# Trabajo PID

## Resumen del Proyecto:
El proyecto se centra en el desarrollo de un sistema de reconocimiento de jugadores de fútbol utilizando imágenes de sus camisetas como entrada. La idea es aprovechar la información visual de las camisetas, que suelen estar marcadas con el nombre y el número del jugador, para identificar automáticamente a quién pertenece la camiseta. Una vez identificado el jugador, el sistema accederá a la base de datos del videojuego EA Sports FC 24 para extraer sus estadísticas.

## Objetivos del Proyecto:

 - Reconocimiento de Jugadores: El objetivo principal es desarrollar un algoritmo de reconocimiento de jugadores que sea capaz de identificar a quién pertenece una camiseta de fútbol a partir de una imagen de la misma. Esto implica la detección y extracción de texto, como el nombre y el número del jugador, de la imagen de la camiseta.

 - Integración con EA Sports FC 24: Una vez que se ha identificado al jugador a través de la camiseta, el sistema debe ser capaz de acceder a la base de datos del videojuego EA Sports FC 24. El objetivo es extraer automáticamente las estadísticas del jugador, como su posición, habilidades, historial de partidos, etc.

 - Interfaz de Usuario Amigable: Para hacer que la herramienta sea accesible y útil, se pretende desarrollar una interfaz de usuario utilizando la propia terminal que permita a los usuarios cargar imágenes de camisetas y obtener las estadísticas de los jugadores de forma sencilla.

## Instalacción

- pip install pandas
- pip install torch (Solo es necesario en windows)
- pip install easyocr 
- pip install pillow
- pip install pytesseract
- pip install os-sys
- pip install tensorflow
- pip install keras-ocr

## Breve descripcion de funcionamiento

El proyecto está dividido en 3 archivos. 
    - mainFile.py: Es el archivo que se debe ejecutar y en donde se encuentran la mayoria de funciones.
    - menus.py: Contiene todos los menu que van apareciendo por consola
    - filtros.py: En el están los filtros que se pueden aplicar a las imagenes para poder obtener una mejor lectura

Trabajo realizado por Javier Calderon Álvarez, Alberto Martín Martín y Antonio Saborido