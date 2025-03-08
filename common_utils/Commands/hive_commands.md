
  **crear tabla**
```
  CREATE [TEMPORARY ] [EXTERNAL] TABLE [IF NOT EXISTS] db_name table_name;

  CREATE TABLE IF NOT EXISTS test(col1 char(10),col2 char(20));
```
  **describir tabla**
```  
  DESCRIBE FORMATTED table_name;
```
  **drop table** 
```  
  DROP TABLE [IF EXISTS] table_name;
```
  **insert** 
```  
  INSERT INTO TABLE students
  VALUES ('fred flintstone', 35, 1.28), ('barney rubble', 32, 2.32);
```
  **refrescar tabla**
```  
  REFRESH [db_name.]table_name
```
  **invalidar metadatos**
```  
  INVALIDATE METADATA db_from_hive.table_from_hive;
```
  **cuando hemos hechos cambios en HDFS por debajo para que HIve se entere**
```  
  msck repair
```