import os
from PIL import Image


# Este script convierte imágenes en un directorio a formato RGB si no lo están ya.
def convert_images_to_RGB(input_folder):


    # Recorre todos los archivos en el directorio
    for filename in os.listdir(input_dir):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff",'.webp')):
            path = os.path.join(input_dir, filename)

            try:
                with Image.open(path) as img:
                    if img.mode in ("RGBA", "P"):
                        print(f"🔁 Convirtiendo {filename} de {img.mode} a RGB...")
                        rgb_img = img.convert("RGB")
                        rgb_img.save(path)
                    else:
                        print(f"✅ {filename} ya está en modo {img.mode}")

            except Exception as e:
                print(f"❌ Error al procesar {filename}: {e}")



input_dir = "imagenes_renombradas"


convert_images_to_RGB(input_dir)

