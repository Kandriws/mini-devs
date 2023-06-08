import json
import os
import re

# Crea la carpeta "assets" si no existe
if not os.path.exists('assets'):
    os.makedirs('assets')

# Cargar el archivo JSON
with open('coverage.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Iterar sobre todos los objetos del JSON
for i, item in enumerate(data):
    # Obtener la URL y el texto completo del archivo
    url = item['url']
    css_text = item['text']
    if re.search(r'\.(css|js)[^/]*$', item['url'].lower()) is None:
        continue
    if 'https://fonts.googleapis.com/css' in url:
        continue
    # Obtener la extensión del archivo (CSS o JS)
    extension = os.path.splitext(url)[1]

    # Obtener los rangos cubiertos
    ranges = item['ranges']

    # Crear una lista de todas las partes del CSS cubiertas
    covered_parts = [css_text[range['start']:range['end']] for range in ranges]

    # Unir las partes cubiertas en un solo texto CSS
    covered_css = ''.join(covered_parts)

    # Obtener el nombre del archivo de salida a partir de la URL
    file_name = os.path.basename(url).replace(':', '-').replace('%', '')

    # Guardar el archivo en la carpeta "assets"
    file_path = os.path.join('assets', file_name)

    # Escribir el CSS cubierto en un archivo separado
    with open(file_path, 'w') as f:
        f.write(covered_css)
