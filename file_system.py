# Definimos la clase "File"
class File:
    def __init__(self, name, size):
        self.name = name  # Nombre del archivo
        self.size = size  # Tamaño del archivo en bytes

    def __repr__(self):
        return f"File(name={self.name}, size={self.size})"


# Definimos la clase "Directory"
class Directory:
    def __init__(self, name):
        self.name = name  # Nombre del directorio
        self.contents = []  # Contenido del directorio (Archivos y subdirectorios)

    # Definimos la función Add_file
    def add_file(self, file):
        self.contents.append(file)  # Agregamos un archivo al directorio

    # Definimos la función agregar directorio "add_directory"
    def add_directory(self, directory):
        self.contents.append(directory)  # Agregamos un directorio al directorio
    
    # Definimos la función "get_size"
    def get_size(self):
        total_size = 0   
        for item in self.contents:
            if isinstance(item, File):
                total_size += item.size # Si es archivo, sumamos su tamaño
            elif isinstance(item, Directory):
                total_size += item.get_size() # Si es subdirectorio, recursivamente sumamos su tamaño
        return total_size
    
    
    def __repr__(self):
        return f"Directory(name={self.name}, contents={len(self.contents)} items)"
        
        
# Definimos la clase "FileSystem"
class FileSystem:
    def __init__(self):
        self.root = Directory("/") # El directorio raíz del sistema de archivos 
        
    # definimos la función crear directorio "Create_directory"
    def create_directory(self, path, name):
        # Buscar el directorio donde crear el nuevo subdirectorio 
        directory = self._get_directory(path)
        if directory:
            new_directory = Directory(name)
            directory.add_directory(new_directory)
            return f"Directorio '{name}' creado con éxito en {path}."
        return "Error: directorio no encontrado."
    
    # Definimos la función crear Archivo "create_file"
    def create_file(self, path, name , size):
        #Buscar directorio donde agregar el archivo 
        directory = self._get_directory(path)
        if directory:
            new_file = File(name, size)
            directory.add_file(new_file)
            return f"Archivo '{name}' credao con éxito en {path}."
        return "Error: directorio no encontrado."
    
    # Definimos la funcion borrar archivo "delete"
    def delete(self, path, name):
        # Buscar el directorio donde se encuentra el archivo o subdirectorio
        directory  = self._get_directory(path)
        if directory:
            # Intentar eliminar archivo o subdirectorio 
            for item in directory.contents:
                if item.name == name:
                    directory.contents.remove(item)
                    return f"'{name}' ha sido eliminado."
                return f"'{name}' no encontrado en {path}."
            return "Error: directorio no encontrado."
        
        
    # Definimos traer directorio "_get_directory"
    def _get_directory(self, path):
        # Si la ruta es vacía, se debe referir al directorio raíz
        if path == "/":
            return self.root
    
        # Separar la ruta en sus componentes
        parts = path.strip('/').split('/')
    
        # Empezar desde el directorio raíz
        current = self.root
        for part in parts:
            found = False
            for item in current.contents:
                if isinstance(item, Directory) and item.name == part:
                    current = item  # Cambiar al subdirectorio encontrado
                    found = True
                    break
            if not found:
                return None  # Si no se encuentra, devolver None
        return current


    
    # Definimos la función "display"
    def display(self):
        # Imprimir la estructura completa del sistema de archivos 
        self._print_directory(self.root)
        
    # Ddefinimos la función "_print_directory"
    def _print_directory(self, directory, indent=0):
        print("" * indent + f"[{directory.name}]")
        for item in directory.contents:
            if isinstance(item, Directory):
                self._print_directory(item, indent + 1)
            elif isinstance(item, File):
                print(" " * (indent + 1) + f"- {item.name} (Archivo, tamaño: {item.size} bytes)")