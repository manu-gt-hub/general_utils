
  **descargar proyecto a local**
```
  git clone [URL]
```
  **ver cambios**
```
  git status
```
  **traer cambios de la rama donde estoy trabajando**
```
  git pull
  git pull origin [RAMA]
  git pull upstream [RAMA]
```
  **crear rama nueva**
```
  git branch [NOMBRE_RAMA]
```
  **apuntar en una rama para trabajar en ella**
```
  git checkout [NOMBRE_RAMA]
```
  **añadir cambios**
```
  (añadir todos los cambios a partir de la carpeta actual) git add .
  (añadir un fichero concrato) git add [fichero]
```
  **confirmar cambios**
```
  git commit  -m "MENSAJE" (idealmente cada tarea será un commit)
```
  **confirmar cambios sobre el último commit**
```
  git commit  --amend [--no-edit]
```
  **ver la lista de commits**
```
  git log
```
  **subir cambios al repositorio**
```
  git push 
  git push origin [RAMA]
  git push upstream [RAMA]
```
  **subir cambios al repositorio forzando**
```
  git push  -f
```
  **sincronizar cambios con el repositorio**
```
  git fetch  --all
```
  **ver todos los espacios de trabajo **
```
  git remote  -v 
```
  **añadir espacios de trabajo remotos**
```
  git remote add upstream [URL]
```
  **crear etiqueta en una rama **
```
  git tag [ETIQUETA]
```
  **revertir commit**
```
  git log (para ver los commits)
  git revert [CODIGO DEL COMMIT]
```
  **revertir cambios**

   ** descartar cambios en un fichero**
```
    git checkout  --[FICHERO]
```
   ** descartar todos los cambios en todos los ficheros**
```
    git reset  --hard
```
  ** agrupar varios commits en uno (squash)**
```
Pasos para hacer squash con git rebase -i

Ejecuta rebase interactivo con la cantidad de commits que quieres combinar. Por ejemplo, para los últimos 3 commits:

git rebase -i HEAD~3

Se abrirá un editor con algo así:

pick abc123 Añade función A
pick def456 Corrige bug en función A
pick ghi789 Mejora documentación


Cambia la palabra pick en los commits que quieres combinar por squash o s (normalmente, deja el primero como pick y los siguientes como squash):

pick abc123 Añade función A
squash def456 Corrige bug en función A
squash ghi789 Mejora documentación


Guarda y cierra el editor. Luego se abrirá otro editor para que edites el mensaje del nuevo commit combinado. Puedes dejar solo uno o combinar los mensajes.

Guarda y cierra.
```
