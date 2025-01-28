# Web Scraping de Cemaco

Este proyecto es una herramienta de web scraping desarrollada en Python que extrae información de productos (nombre y URL de la imagen) de un archivo HTML de la tienda en línea de Cemaco. Los datos extraídos se guardan en un archivo CSV para facilitar su análisis o uso posterior.

## Funcionalidades

- **Carga de HTML:** Lee un archivo HTML que contiene información de la tienda en línea.
- **Extracción de datos:** Utiliza expresiones regulares para extraer el nombre de los productos y las URLs de las imágenes.
- **Exportación a CSV:** Guarda los datos extraídos en un archivo CSV con un formato limpio y organizado.

## Requisitos

Para ejecutar este proyecto, asegúrate de tener instalado:

- Python 3.x
- Ninguna dependencia adicional es necesaria, ya que utiliza únicamente módulos estándar de Python (`re` y `csv`).

## Uso

1. **Copiar el Repositorio**  
   Copia el repositorio en tu maquina con este comando:
```bash
git clone https://github.com/DiegoDuaS/WebScrappingCemaco
```

2. Ejecuta el archivo `webScrapping.py` en tu terminal o entorno de desarrollo:
```bash
python webScrapping.py
``` 
Toma en cuenta que puedes descargar otro html de cemaco.com . Para poder utilizar el código con este nuevo archivo, lo debes de remplazar por "Cemaco _ Tienda en Línea_ Ferretería, Hogar, Blancos y Mascotas.html" y asegurarte que tenga el mismo nombre. 

## Notas importantes
- Este script utiliza expresiones regulares para extraer los datos. Asegúrate de que las clases y estructuras HTML coincidan con las expresiones utilizadas en el script.

## Contribución
Si deseas mejorar este proyecto o añadir nuevas funcionalidades, ¡siéntete libre de enviar un pull request!





