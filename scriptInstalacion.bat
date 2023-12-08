@echo off
echo Instalando librerías de Python...

rem Instalar pandas
pip install pandas
if errorlevel 1 (
    echo Error al instalar pandas.
) else (
    echo Librería pandas instalada correctamente.
)

rem Instalar torch (solo en Windows)
if "%OS%"=="Windows_NT" (
    pip install torch
    if errorlevel 1 (
        echo Error al instalar torch.
    ) else (
        echo Librería torch instalada correctamente.
)
)

rem Instalar easyocr
pip install easyocr
if errorlevel 1 (
    echo Error al instalar easyocr.
) else (
    echo Librería easyocr instalada correctamente.
)

rem Instalar pillow
pip install pillow
if errorlevel 1 (
    echo Error al instalar pillow.
) else (
    echo Librería pillow instalada correctamente.
)

rem Instalar pytesseract
pip install pytesseract
if errorlevel 1 (
    echo Error al instalar pytesseract.
) else (
    echo Librería pytesseract instalada correctamente.
)

rem Instalar os-sys
pip install os-sys
if errorlevel 1 (
    echo Error al instalar os-sys.
) else (
    echo Librería os-sys instalada correctamente.
)


echo Instalación completa.
pause
