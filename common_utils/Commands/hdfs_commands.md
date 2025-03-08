              
  **version**
```
  hadoop version
```
  **listar directorio**
```
  hdfs dfs -ls /
```
  **tamaño directorio**
```
  hdfs dfs -df hdfs:/
```
  **conteo directorios**
```
  hdfs dfs -count hdfs:/
```
  **crear directorio**
```
  hdfs dfs -mkdir /hadoop
```
  **crear fichero**
```
  hdfs dfs -put fichero_prueba /hadoop
```
  **eliminar fichero**
```
  hdfs dfs -rm /hadoop/fichero_prueba
```
  **eliminar directorio**
```
  hdfs dfs -rm -r /hadoop/directorio
```
  **cambiar permisos**
```
  hdfs dfs -chmod 777 /hadoop
```
  **copiar ficheros HDFS al filesystem normal**
```
  hdfs dfs -get /hadoop/test /home/ubuntu/Desktop/
```
  **ver fichero**
```
  hdfs dfs -cat /hadoop/fichero
```
  **mover fichero**
```
  hdfs dfs -mv /hadoop/sample /tmp
```
  **copiar fichero**
```
  hdfs dfs -cp /tmp/sample /usr
```
  **cambiar propietario**
```
  hdfs dfs -chown root:root /tmp
```