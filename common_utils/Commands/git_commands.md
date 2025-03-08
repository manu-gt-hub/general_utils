
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
  git commit  --amend
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
