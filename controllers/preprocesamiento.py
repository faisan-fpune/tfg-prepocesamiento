
from funciones import convert_images_to_RGB,print_colored,get_cantidad_etiquetas
import os

def preprocesar_imagenes():

    try:
        input_folder = str(input("Ingrese la ruta de la carpeta de entrada: "))
    
        if input_folder is None or input_folder.strip() == "":
            raise ValueError("La carpeta de entrada no puede estar vacía.")
        
        if not os.path.exists(input_folder):
            print_colored(f"❌ La carpeta de entrada {input_folder} no existe.", level="warning")
        
        convert_images_to_RGB(input_folder)
        print_colored("✅ Imágenes convertidas a RGB y renombradas correctamente.", level="success")
    
    except Exception as e:
        print_colored(f"❌ Error: {e}", level="danger")
