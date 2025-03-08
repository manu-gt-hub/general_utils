# Spark config to optimize the joins with Databricks AQE
spark.conf.set("spark.sql.adaptive.enabled",True)
spark.conf.set('spark.sql.adaptive.skewJoin.enabled', True)
spark.conf.set('spark.sql.adaptive.localShuffleReader.enabled', True)
spark.conf.set('spark.sql.adaptive.coalescePartitions.enabled', True)
spark.conf.set('spark.databricks.adaptive.autoOptimizeShuffle.enabled', True)
