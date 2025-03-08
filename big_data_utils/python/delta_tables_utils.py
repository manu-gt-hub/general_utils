def read_delta(input_dir_spark, name_pattern, date_col, raiseException=False):
  """
  Function to read a delta table from the datalake

  Args:
    input_dir_spark : path where de delta table is
    name_pattern : name of the delta table
    date_col : column to use and get the last partition

  Returns:
    Dataframe or None in case of error

  Raises:
    Exeception: if delta table was not able to be read and raiseException is True
  """
  try:
    all_files = os.listdir("/dbfs" + input_dir_spark)
    name_file = [input_dir_spark + f for f in all_files if name_pattern==f]
    if len(name_file) > 1:
      print('name_pattern is not unique!')
      return
    else:
      name_pattern_df = spark.read.format("delta").load(name_file[0])
      name_pattern_df2 = name_pattern_df.filter(F.col(str(date_col)) == name_pattern_df.selectExpr("max("+str(date_col)+") as max_load_date").collect()[0].max_load_date)

    return name_pattern_df2

  except Exception as ex:
    print("Error READING delta: {0}".format(ex))
    if raiseException:
      raise
    return None


def delete_delta(delta_path, predicate="", raiseException=False):
  """
  Function to delete a delta table from the datalake

  Args:
    delta_path : path where de delta table is
    predicate : predicate which indicates the filters to apply in deletion

  Returns:
    Bool (True if dropped and False if not)

  Raises:
    Exeception: if delta table was not able to be deleted and raiseException is True
  """
  
  try:
    deltaTable = DeltaTable.forPath(spark, delta_path)  
    # set retentionDurationCheck to false to execute the vacuum with 0 retention to 
    # properly execute the data deletion and then set retentionDurationCheck to
    # true again
    spark.conf.set("spark.databricks.delta.retentionDurationCheck.enabled", "false")
    if predicate != "":         
      deltaTable.delete(predicate)
      deltaTable.vacuum(0)    
    else : 
      deltaTable.delete()      
      deltaTable.vacuum(0)      
      
    spark.conf.set("spark.databricks.delta.retentionDurationCheck.enabled", "true")
    print("DELETED delta: "+delta_path)
    return True
  
  except Exception as ex:
    print("Error DELETING delta: {0}".format(ex))
    if raiseException:      
      raise   
    return False


def drop_delta(delta_path, raiseException=False):
  """
  Function to drop a delta table from the datalake

  Args:
    delta_path : path where de delta table is

  Returns:
    Bool (True if dropped and False if not)

  Raises:
    Exeception: if delta table was not able to be dropped and raiseException is True
  """
  
  try:
    
    deltaTable = DeltaTable.forPath(spark, delta_path)  
    
    deltaTable.delete()
    # set retentionDurationCheck to false to execute the vacuum with 0 retention to 
    # properly execute the data deletion and then set retentionDurationCheck to
    # true again
    spark.conf.set("spark.databricks.delta.retentionDurationCheck.enabled", "false")
    deltaTable.vacuum(0)      
    spark.conf.set("spark.databricks.delta.retentionDurationCheck.enabled", "true")
    dbutils.fs.rm(delta_path,True)
    
    print("DROPPED delta: "+delta_path)
    return True
  
  except Exception as ex:   
    print("Error DROPPING delta: {0}".format(ex))
    if raiseException:
      raise
    return False
