########### AYUDA WIDGETS

dbutils.widgets.help()

ejemplo
dbutils.widgets.dropdown("env", "dev", ["dev","int","prod"])

########### FILTRAR POR COLUMNAS CON VALOR NULL

display(dataframe.filter(col('COLUMN').isNull()))

########### ELIMINAR DIRECTORIO DE DELTA TABLE

dbutils.fs.rm("/mount/point/env/data/path/etc/DELTA_TABLE_NAME.delta/",True)

########### CONTEO % DE UN DF

print(dataframe.sample(0.01).count())

########### ELIMINAR DELTA TABLE Y METADATOS

from delta.tables import *

joined_data_path = "/mount/point/env/data/path/etc/DELTA_TABLE_NAME.delta/"

deltaTable = DeltaTable.forPath(spark, joined_data_path)  # path-based tables, or

deltaTable.vacuum() 
deltaTable.delete()
dbutils.fs.rm(joined_data_path,True)

########### ORDER BY VARIAS COLUMNAS Y ORDENACION 

display(mra_data.filter("COLUMN == 837294").orderBy(F.desc("COLUMN"), F.desc("COLUMN")))

########### RESTAURAR DELTA TABLE

df = spark.read.format("delta").load("/mount/point/env/data/path/etc/DELTA_TABLE_NAME.delta")
df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save("/mount/point/env/data/path/etc/DELTA_TABLE_NAME.delta")

########### LEER EL ESTADO ANTERIOR DE TABLA DELTA

from delta.tables import *

path = "/mount/point/env/data/path/etc/"
delta_name="DELTA_TABLE_NAME"

deltaTable = DeltaTable.forPath(spark, path + delta_name)
fullHistoryDF = deltaTable.history()
display(fullHistoryDF)

########## EXPLOTAR JSON EN COLUMNA

fullHistoryDF.withColumn("NOMBRE NUEVA COL.", F.col("VALOR JSON").getItem("NIVEL QUE QUEREMOS"))

########## REVISAR NUMERO DE FILAS POR CLAUSULA JOIN

df.groupBy("COLUMN NAME").count().filter('count > 1')

#########3 LISTAR PUNTOS DE MONTAJE ####

display(dbutils.fs.mounts())

######## SALTED JOIN ############

from pyspark.sql.types import IntegerType

li = []
for x in range(0, 8, 1):
li.append

list_df=spark.createDataFrame(li, IntegerType())

vdimproduct=vdimproduct.crossJoin(list_df).withColumn('salted_id', F.concat(F.col('ProductKey'),F.lit('_'), F.col('value'))).drop("value")

vfactselloutinvoice = vfactselloutinvoice.withColumn('salted_id', F.concat(F.col('ProductKey'),F.lit('_'), F.monotonically_increasing_id() % 8)).drop("value")

share_mra_joined = vfactselloutinvoice.join(vdimproduct, ["salted_id"], how = "inner")

print(share_mra_joined.count())
