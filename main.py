# Importamos el archivo "file_system"
from file_system import FileSystem


# Definimos la función main
def main():
    # Crear una instancia del sistema de archivos
    fs = FileSystem()
    
    
    #crear directorios y archivos 
    print(fs.create_directory("/", "home"))
    print(fs.create_directory("/home", "user"))
    print(fs.create_file("/home/user", "file1.txt", 200))
    print(fs.create_file("/home/user", "file2.txt", 300))
    print(fs.create_directory("/home/user", "documents"))
    print(fs.create_file("/home/user/documents", "doc1.pdf", 500))
    
    # Mostrar la estructura 
    print("\nEstructura del sistema de archivos: ")
    fs.display()
    
    # Obtener el tamaño de un directorio
    home_dir = fs._get_directory("/home")
    if home_dir:
        print(f"\nTamaño total de '/home': {home_dir.get_size()} bytes")
    else:
        print("El directorio '/home' no fue encontrado.")
    
    #Eliminar un archivo
    print("\nEliminando archivo 'file1.txt':")
    print(fs.delete("/home/user", "file1.txt"))
    
    #Mostrar la estructura después de la eliminación 
    print("\nEstructura del sistema de archivos después de la eliminación:")
    fs.display()
    
    
if __name__ == "__main__":
    main()
