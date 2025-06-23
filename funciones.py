import os
import json
from collections import Counter
from PIL import Image
import uuid
import hashlib
import re


def json_data(path):
    """
    Esta función devuelve los datos del archivo JSON especificado.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"El archivo {path} no existe.")
    
    with open(path, "r") as file:
        return json.load(file)

def is_hash_valid(hash_string):
    """
    Verifica si el hash es válido (32 caracteres hexadecimales).

    """
    return bool(re.fullmatch(r'[a-f0-9]{32}', hash_string))

def convert_images_to_RGB(input_folder):
    if not os.path.exists(input_folder):
        raise FileNotFoundError(f"El directorio {input_folder} no existe.")
    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff", ".webp")):
            path = os.path.join(input_folder, filename)
            

            try:
                with Image.open(path) as img:
                    mode = img.mode
                    needs_conversion = mode in ("RGBA", "P")

                nuevo_nombre = f"{crear_uuid_hash()[0:12]}.jpg"
                nueva_ruta = os.path.join(input_folder, nuevo_nombre)

                if needs_conversion:
                    print_colored(f"🔁 Convirtiendo {filename} de {mode} a RGB...",level='warning')
                    with Image.open(path) as img:
                        rgb_img = img.convert("RGB")
                        rgb_img.save(nueva_ruta)
                    os.remove(path)
                else:
                    if not is_hash_valid(filename.split(".")[0]):
                        print_colored(f"🔁 Renombrando {filename} a {nuevo_nombre}...",level='warning')
                        
                        os.rename(path, nueva_ruta)
                    print(f"✅ {filename} ya está en modo {mode}")

            except Exception as e:
                print(f"❌ Error al procesar {filename}: {e}")

def get_cantidad_etiquetas():
    """
    Esta función devuelve la cantidad de etiquetas en los archivos JSON
    dentro del directorio especificado.
    """
    path = str(input("Ingrese la ruta del directorio que contiene los archivos JSON: "))

    if not os.path.exists(path):
        raise FileNotFoundError(f"El directorio {path} no existe.")
    
    etiquetas_counter = Counter()

    for filename in os.listdir(path):
        if filename.endswith(".json"):
            file_path = os.path.join(path, filename)
            data = json_data(file_path)
            etiquetas = [chapa.get("label") for chapa in data.get("shapes", [])]
            etiquetas_counter.update(etiquetas)
    print(f"Cantidad de chapas paraguayas: {etiquetas_counter['chapa_paraguaya']}")
    print(f"Cantidad de chapas mercosur: {etiquetas_counter['chapa_mercosur']}")


def print_colored(message, level="success"):

    
    """
    Imprime un mensaje en la consola con un color dependiendo del nivel.
    Niveles disponibles: success (verde), warning (amarillo), danger (rojo).
    """
    colors = {
        "success": "\033[92m",  # Verde
        "warning": "\033[93m",  # Amarillo
        "danger": "\033[91m",   # Rojo
        "reset": "\033[0m"      # Reset
    }
    color = colors.get(level, colors["reset"])
    print(f"{color}{message}{colors['reset']}")

def crear_uuid_hash():
    """
    Genera un UUID único y lo convierte a un hash SHA-256.
    """
    # Generar un UUID
    unique_id = str(uuid.uuid4())

    # Crear un hash SHA-256 del UUID
    sha256_hash = hashlib.sha256(unique_id.encode()).hexdigest()

    return sha256_hash
