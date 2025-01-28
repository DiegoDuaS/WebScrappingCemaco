import re
import csv

# Abrir archivo HTML
def cargar_html(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        return f.read()

import re

def extraer_productos(html):
    regex_nombre = r'<span class="vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body">([\s\S]*?)<\/span>'
    regex_imagen = r'<img[^>]*class="[^"]*vtex-product-summary-2-x-imageNormal[^"]*".*?src="([^"]+)".*?alt="([^"]+)"'
    
    # Creación de índices 
    nombres = re.findall(regex_nombre, html)
    imagenes = re.findall(regex_imagen, html)

    nombres = [nombre.strip() for nombre in nombres]  # Limpiar espacios extra
    return zip(nombres, imagenes)



# Exportar resultados a CSV
def exportar_csv(productos, archivo_salida):
    with open(archivo_salida, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Nombre del Producto", "URL de la Imagen"])
        writer.writerows(productos)

# Cargar el archivo HTML y extraer datos
archivo_html = "./Cemaco _ Tienda en Línea_ Ferretería, Hogar, Blancos y Mascotas.html"

html = cargar_html(archivo_html)
productos = extraer_productos(html)

# Exportar a CSV
exportar_csv(productos, 'productos.csv')
print(f"Exportado a {'productos.csv'}")
