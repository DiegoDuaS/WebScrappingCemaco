import re
import csv

# Abrir archivo HTML
def cargar_html(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        return f.read()

# Buscar productos y URLs de imágenes
def extraer_productos(html):
    regex_item = r'"item":\s*({(?:[^{}]|\{.*?\})*})'
    matches = re.findall(regex_item, html, re.DOTALL)
    result = ""
    
    for match in matches:
        if match:
            # Extraer nombre e imagen con regex
            regex_name = r'"name"\s*:\s*"([^"]+)"'
            regex_image = r'"image"\s*:\s*"([^"]+)"'
            
            name_match = re.search(regex_name, match)
            image_match = re.search(regex_image, match)
            
            name = name_match.group(1) if name_match else None
            image = image_match.group(1) if image_match else None

            result += f"{name}, {image}\n"
        
    return result

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
