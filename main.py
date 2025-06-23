from controllers.preprocesamiento import preprocesar_imagenes,get_cantidad_etiquetas
from funciones import print_colored
import os


opciones = [
    {
        "opcion": 0,
        "descripcion": "Salir",
        "funcion": None,
        "args": []
    },
    {
        "opcion": 1,
        "descripcion": "Convertir imágenes a RGB",
        "funcion": "convert_images_to_RGB",
    },
    {
        "opcion": 2,
        "descripcion": "Contar etiquetas en JSON",
        "funcion": "get_cantidad_etiquetas",
    }
]

def print_opciones():
    print("Seleccione una opción:")
    for opcion in opciones:
        print(f"{opcion['opcion']}. {opcion['descripcion']}")

def main():
    print_opciones()
    
    seleccion = int(input("Ingrese el número de la opción: "))

    while seleccion not in [op["opcion"] for op in opciones]:
        print_colored("Opción no válida. Intente nuevamente.",level="danger")
        print_opciones()
        seleccion = int(input("Ingrese el número de la opción: "))

    opcion_seleccionada = next((op for op in opciones if op["opcion"] == seleccion), None)
    if opcion_seleccionada:
        funcion = opcion_seleccionada["funcion"]
        match funcion:
            case "convert_images_to_RGB":
                preprocesar_imagenes()
            case "get_cantidad_etiquetas":
                get_cantidad_etiquetas()
            
                

                

if __name__ == "__main__":
    main()