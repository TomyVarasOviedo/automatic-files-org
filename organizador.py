import os
import json
# Configurar la ruta de la carpeta a organizar
configFile = open(".config.json")
config=json.load(configFile)

ruta=config["ruta_raiz"]
# Organizacion segmentada por el usuario
user_dirs=config["clasificacion"]

carpetas=["PDFs", "Instaladores", "Imagenes","Comprimidos", "Otros"]
def mover_archivo(archivo:str, carpeta:str):
    """
    @param archivo: Nombre del archivo ha mover
    @param carpeta: Nombre de la carpeta donde quedara
    """
    src_path = os.path.join(ruta, archivo)
    destino_path = os.path.join(ruta+f"/{carpeta}", archivo)
    os.rename(src_path, destino_path)

def clasificar_archivos(archivo:str):
    """
    @param archivo: Nombre del archivo a clasificar
    """
    extension = os.path.splitext(archivo)[1]
    match extension:
        case ".pdf":
            mover_archivo(archivo,"PDFs")
        case ".exe":
            mover_archivo(archivo, "Instaladores")
        case ".jpg"| ".jpeg" | ".png" | ".web" :
            mover_archivo(archivo, "Imagenes")
        case ".zip" | ".tar" | ".deb" | ".rar":
            mover_archivo(archivo, "Comprimidos")
        case _:
            print(extension)
            mover_archivo(archivo,"Otros")
def main():
    archivos=os.listdir(ruta)
    print("Organizando archivos...")
    for archivo in archivos:
        if not(archivo in carpetas):
            "Si no corresponde a una carpeta clasifica el archivo"
            clasificar_archivos(archivo)
if __name__ == "__main__":
    main()