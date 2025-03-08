
#(todos los comandos se pueden ejecutar como super usuarios añadiendo sudo antes del comando)

  **listar directorio**
```
  ll 
```
  **entrar en directorio**
```
  cd [NOMBRE_DIRECTORIO]
```
  **subir un nivel en directorios **
```
  cd ..
```
  **ver fichero** 
```
  cat [NOMBRE_FICHERO]
```
  **cambiar permisos fichero**
```
  chmod [XXX] [NOMBRE_FICHERO]
```
  **dar permisos de ejecucion a fichero**
```
  chmod +x [NOMBRE FICHERO]
```
  **ver fichero y editarlo**
```
  vi [NOMBRE_FICHERO]

  paso 1: (estando dentro) pulsar i para editarlo

  paso 2: incluir cambios

  paso 3: presionar ESC para salir del moto edicion

  pulsar u para deshacer el ultimo cambio 
  
  pulsar :q para salir sin guardar los cambios

  pulsar :W para guardar cambios pero mantener abierto el fichero
  
  presionar Shift+zz para guardar y salir del fichero
  
  presionar :wq para guardar y salir del fichero
```
  **conectarse por ssh a una maquina remota**
```
  ssh [NOMBRE_MAQUINA/IP]
```
  **copiar ficheros/directorio a maquina remota**
```
  scp [FICHERO/DIRECTORIO] usuario@maquina_remote:/path/destino
```
  **descomprimir tar **
```
  tar xvf [NOMBRE_TAR]
```
  **copiar fichero a otra ubicacion**
```
  cp [NOMBRE_FICHERO] [RUTA DESTINO]
```
  **mover fichero a otra ubicacion**
```
  mv [NOMBRE_FICHERO] [RUTA DESTINO]
```
  **ejecutar script**
```
  ./script.sh 
  ./script.sh [PARAM1] [PARAM2]
```
  **mostrar valor variable**
```
  echo $variable
```
  **instalar aplicacion**
```
  sudo apt-get install [NOMBRE_APLICACION]
```
  **ver IPs**
```
  ifconfig
```