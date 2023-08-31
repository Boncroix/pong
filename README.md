# pong

Recreación del clásico videojuego PONG utilizando PyGame

## Cómo crear un entorno virtual

Supongamos que queremos crear un entorno virtual con el
nombre _env_.

```
python -m venv env

# En mac/linux si usáis python 3
python3 -m venv env
```

## Cómo activar el entorno virtual

```
# en Windows
.\env\Scripts\activate

# en Mac/Linux
source env/bin/activate
```

## Gestor de paquetes: pip

- Instalar un paquete nuevo: `pip install <nombre-del-paquete>`
- Ver los paquetes instalados (en el entorno): `pip freeze`

## Desactivar el entorno virtual

```
# Con el entorno virtual activo

deactivate
```

## Comandos típicos GIT

- Inicializar un repositorio local
  `git init`
- Clonar un repositorio remoto (por ejemplo, desde github) `git clone https://url-del-repositorio`
- Agregar TODOS los archivos modificados al staging (antes de guardarlos en el repo) `git add --all`
- Agregar los archivos modificados en el directorio actual (y sus subdirectorios) al staging (antes de guardarlos en el repo) `git add .`
- Guardar los cambios de la zona staging en el repositorio local `git commit -m mensaje del commit`
- Descargar cambios del repositorio remoto con el repositorio local `git pull`
- Enviar nuestros cambios (commits) al repositorio remoto `git push`
- Ver referencias de repositorios remotos (los nombres) `git remote`
- Ver la URL de una referencia remota (por ejemplo, _origin_) `git remote get-url origin`
- Cambiar la URL de una referencia remota (por ejemplo, origin) `git remote set-url origin https://nueva-url`
- Crear una nueva referencia remota `git remote add <nombre> <url>`
