import re
import csv

# Abrir archivo HTML
def cargar_html(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        return f.read()

# Buscar productos y URLs de imágenes
def extraer_productos(html):
    regex_nombre = r'<span class="vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body">([\s\S]*?)<\/span>'
    regex_imagen = r'<img[^>]*src="([^"]+)"'
    
    nombres = re.findall(regex_nombre, html)
    imagenes = re.findall(regex_imagen, html)
    
    # Combinar resultados, asegurando que ambas listas tengan la misma longitud
    return list(zip(nombres, imagenes))

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
