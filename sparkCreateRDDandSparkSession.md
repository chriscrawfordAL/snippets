#### Create a Spark RDD
```
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("myAppName").getOrCreate()

rdd1 = spark.sparkContext.parallelize(some_list)

# OR

sc = spark.sparkContext()
myfile = "/path/to/some/file.csv"
rdd2 = sc.textFile(myfile)
rdd2.take(5)
```

### Using SparkSession vs sparkContext
```
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("myAppName").getOrCreate()

myfile = "/path/to/some/file.csv"
df1 = spark.read.csv(myfile, sep = ",", inferSchema = True, header = True)
df1.show(5)
df1.printSchema()
```
