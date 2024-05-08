pip install pyspark


from pyspark.sql import SparkSession
from pyspark.sql.functions import *
spark=SpearkSession.builder.appName("app").getOrCreate()

df=spark.createDataFrame([(1,101),(2,202)],['id','number'])
df.show()

