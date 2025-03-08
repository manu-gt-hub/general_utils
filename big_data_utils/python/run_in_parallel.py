from pyspark import AccumulatorParam

#customized accumulator
class ListAcc(AccumulatorParam):
  #function called when initalized
  def zero(self, v):
      return []
  #function called when adding new element
  def addInPlace(self, variable, value):
      #value is the new element
      #variable is the acc object (list)
      variable.append(value)
      return variable

parallel_acc = sc.accumulator([], ListAcc())

def run_in_parallel(rows,loop_func):  
  df = spark.createDataFrame(rows)
  #loop function to call the parameter one but calling the accumulator
  #as global, to use it
  def aux_loop_func(row):
    #get the accumulator
    global parallel_acc  
    #call the parameter function
    res = loop_func(row)
    #add the result to the accumulator
    parallel_acc.add(res)
    #return required value for the UDF
    return 1

  #define UDF
  loop_func_udf = udf(aux_loop_func, IntegerType())
  #withcolumn sending the whole row to the UDF
  _df=df.withColumn("udf_val", loop_func_udf(F.struct([df[c] for c in df.columns])))
  #force the code to get executed
  _df.collect()  
  list_items = []
  #process accumulator to fit values in a list
  for i in range(0, len(parallel_acc.value)):
    # this filter determinates if there is value accumulated or not
    if len(parallel_acc.value[i]) > 0:
      # get the item
      item = parallel_acc.value[i]
      list_items.append(item)
  return list_items

# ***************USE************

#create parameters as rows
model_parameters = [
  Row(a='x',b='y',c=z),
  Row(a='x',b='y',c=z),
  Row(a='x',b='y',c=z)
]

#function containing training model's code
def training_func(row):  
  #trained = gradient.fit(X_train, Y_train)
  #return (_level,trained)

#run function in parallel
list_result = run_in_parallel(model_parameters,training_func)

#********************** END USE *************************
