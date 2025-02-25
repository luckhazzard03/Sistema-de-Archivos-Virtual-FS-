```markdown
# Sistema de Archivos Virtual (FS)
```


```markdown
## Descripción

Este proyecto implementa un sistema de archivos virtual en Python. Permite crear y administrar directorios y archivos, así como calcular el tamaño total de un directorio. El sistema de archivos soporta operaciones básicas como la creación de archivos, la creación de directorios y la eliminación de archivos. Es una herramienta ideal para simular cómo funcionan los sistemas de archivos reales, pero en un entorno controlado.
```



```markdown
## Características

- Crear directorios y archivos.
- Eliminar archivos.
- Calcular el tamaño total de un directorio.
- Mostrar la estructura completa del sistema de archivos.
```



```markdown
## Tecnologías

- Python 3
```


```markdown
## Instalación

Para usar este sistema de archivos virtual, sigue estos pasos:

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tuusuario/SistemaarchivosvirtualFS.git
   ```

2. Navega al directorio del proyecto:

   ```bash
   cd SistemaarchivosvirtualFS
   ```

3. Ejecuta el archivo `main.py`:

   ```bash
   python3 main.py
   ```

   Esto iniciará el sistema de archivos virtual y ejecutará algunos ejemplos básicos de operaciones.
```



```markdown
## Uso

Una vez que ejecute el programa, se crearán algunos directorios y archivos de ejemplo, y podrás ver la estructura del sistema de archivos impresa en la consola. Los directorios y archivos se crearán en la ruta raíz `/` y se pueden modificar con las siguientes operaciones:

- **Crear directorios**: Se crean subdirectorios dentro de otros directorios.
- **Crear archivos**: Se pueden crear archivos en cualquier directorio.
- **Eliminar archivos**: Los archivos pueden ser eliminados especificando la ruta completa.
- **Calcular el tamaño**: Puedes obtener el tamaño total de cualquier directorio.

### Ejemplo de ejecución:
```bash
$ python3 main.py
Directorio 'home' creado con éxito en /.
Directorio 'user' creado con éxito en /home.
Archivo 'file1.txt' creado con éxito en /home/user.
Archivo 'file2.txt' creado con éxito en /home/user.
Directorio 'documents' creado con éxito en /home/user.
Archivo 'doc1.pdf' creado con éxito en /home/user/documents.

Estructura del sistema de archivos: 
[/]
[home]
[user]
   - file1.txt (Archivo, tamaño: 200 bytes)
   - file2.txt (Archivo, tamaño: 300 bytes)
[documents]
    - doc1.pdf (Archivo, tamaño: 500 bytes)

Tamaño total de '/home': 1000 bytes

Eliminando archivo 'file1.txt':
Archivo 'file1.txt' ha sido eliminado.
```
```






