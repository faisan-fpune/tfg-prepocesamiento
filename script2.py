""" import os
import zipfile
import shutil

def main():
    # Directorios
    imagenes_dir = "imagenes_renombradas"
    output_dir = "output"
    zip_name = "ruth.zip"

    # Verificar que las carpetas existen
    if not os.path.exists(imagenes_dir) or not os.path.exists(output_dir):
        print("Las carpetas 'imagenes_renombradas' y 'output' deben existir.")
        return

    # Obtener listas de imágenes y archivos JSON
    imagenes = set(f for f in os.listdir(imagenes_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg')))
    etiquetados = set(f.replace('.json', '') for f in os.listdir(output_dir) if f.lower().endswith('.json'))

    # Identificar imágenes faltantes por etiquetar
    faltantes = list(imagenes - etiquetados)
    etiquetadas = list(imagenes & etiquetados)

    # Calcular la mitad de las imágenes faltantes
    mitad = len(faltantes) // 2
    faltantes_para_zip = faltantes[:mitad]
    restantes = faltantes[mitad:]

    # Crear el archivo ZIP con las imágenes faltantes
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for img in faltantes_para_zip:
            img_path = os.path.join(imagenes_dir, img)
            zipf.write(img_path, img)

    # Mover las imágenes restantes a la carpeta de imágenes renombradas
    for img in restantes:
        src_path = os.path.join(imagenes_dir, img)
        dest_path = os.path.join(imagenes_dir, img)
        shutil.move(src_path, dest_path)

    print(f"Archivo ZIP '{zip_name}' creado con {len(faltantes_para_zip)} imágenes.")
    print(f"{len(restantes)} imágenes restantes en la carpeta 'imagenes_renombradas'.")
    print(f"{len(etiquetadas)} imágenes ya etiquetadas.")


main() """