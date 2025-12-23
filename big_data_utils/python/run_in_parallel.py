# ================== REQUIRED IMPORTS ==================

from pyspark.sql import SparkSession, Row
from pyspark.sql.types import IntegerType
from pyspark.sql.functions import udf
from pyspark import AccumulatorParam
import pyspark.sql.functions as F

# ================== SPARK CONTEXT ==================
# (If spark and sc already exist in your environment, you can skip this)

spark = SparkSession.builder.getOrCreate()
sc = spark.sparkContext

# ================== ACCUMULATOR ==================

# Customized accumulator
class ListAcc(AccumulatorParam):
    # Function called when initialized
    def zero(self, v):
        return []

    # Function called when adding a new element
    def addInPlace(self, variable, value):
        # value is the new element
        # variable is the accumulator object (list)
        variable.append(value)
        return variable

parallel_acc = sc.accumulator([], ListAcc())

# ================== PARALLEL FUNCTION ==================

def run_in_parallel(rows, loop_func):
    # Create DataFrame from input rows
    df = spark.createDataFrame(rows)

    # Auxiliary function executed in parallel
    def aux_loop_func(row):
        # Access the global accumulator
        global parallel_acc
        # Call the provided function
        res = loop_func(row)
        # Add result to the accumulator
        parallel_acc.add(res)
        # Return required value for the UDF
        return 1

    # Define UDF
    loop_func_udf = udf(aux_loop_func, IntegerType())

    # Apply UDF passing the whole row as a struct
    _df = df.withColumn(
        "udf_val",
        loop_func_udf(F.struct([df[c] for c in df.columns]))
    )

    # Force execution
    _df.collect()

    # Process accumulator values
    list_items = []
    for i in range(len(parallel_acc.value)):
        # This filter determines if there is accumulated value or not
        if len(parallel_acc.value[i]) > 0:
            # Get the accumulated item
            item = parallel_acc.value[i]
            list_items.append(item)

    return list_items

# ================== USE ==================

# Create parameters as rows
model_parameters = [
    Row(a='x', b='y', c='z'),
    Row(a='x', b='y', c='z'),
    Row(a='x', b='y', c='z')
]

# Function containing model training code
# Function containing example "training" logic
def training_func(row):
    # Access Row values (Row is received as a struct)
    a_val = row['a']      # or row.a
    b_val = row['b']      # or row.b
    c_val = row['c']      # or row.c

    # Example logic (dummy processing)
    # Simulate some computation using row values
    result = f"processed_{a_val}_{b_val}_{c_val}"

    # Return a tuple (can be any object you want to accumulate)
    return (a_val, b_val, c_val, result)


# Run function in parallel
list_result = run_in_parallel(model_parameters, training_func)

# ================== END ==================
