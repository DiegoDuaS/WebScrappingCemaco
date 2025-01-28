import re
import csv

# Abrir archivo HTML
def cargar_html(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        return f.read()

import re

def extraer_productos(html):
    # Regex para nombres de productos
    regex_nombre = r'<span class="vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body">([\s\S]*?)<\/span>'
    # Regex para imágenes 
    regex_imagen = r'<img[^>]*class="[^"]*vtex-product-summary-2-x-imageNormal[^"]*".*?src="([^"]+)".*?alt="([^"]+)"'
    
    # Extraer nombres de productos
    nombres = re.findall(regex_nombre, html)
    nombres = [nombre.strip() for nombre in nombres]  # Limpiar espacios extra

    # Extraer imágenes y el alt
    imagenes = re.findall(regex_imagen, html)
    
    productos = []
    
    # Asociar nombres con imágenes
    for nombre in nombres:
        encontrado = False
        for imagen_url, alt in imagenes:
            # Comparar los nombres y el alt directamente
            if nombre == alt:
                productos.append((nombre, imagen_url))
                encontrado = True
                break
        
        if not encontrado:
            continue
    
    return productos



# Exportar resultados a CSV
def exportar_csv(productos, archivo_salida):
    with open(archivo_salida, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Nombre del Producto", "URL de la Imagen"])
        writer.writerows(productos)

# Cargar el archivo HTML y extraer datos
archivo_html = "Cemaco _ Tienda en Línea_ Ferretería, Hogar, Blancos y Mascotas.html"
archivo_salida_csv = "productos.csv"

html = cargar_html(archivo_html)
productos = extraer_productos(html)

# Exportar a CSV
exportar_csv(productos, archivo_salida_csv)
print(f"Exportado a {archivo_salida_csv}")
