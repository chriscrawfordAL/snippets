#### Create SparkSession
```
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = SparkSession.builder.appName("Data Preparation").getOrCreate()
```

#### Reading a file with a defined Schema
#### Bringing in as all StringType first to clean the data
```
schema = StructType([
    StructField("Order ID", StringType(), True),
    StructField("Product", StringType(), True),
    StructField("Quantity Ordered", StringType(), True),
    StructField("Price Each", StringType(), True),
    StructField("Order Date", StringType(), True),
    StructField("Purchase Address", StringType(), True)
])

file_path = "./file/to/input.csv"
fire_df = (spark.read.format("csv")
           .option("header", True)
           .schema(schema)
           .load(file_path))
```

#### Writing to Parquet
```
output_path = ".file/to/output"  #directory, not a filename
fire_df.write.format("parquet").mode("overwrite").save(output_path)
```
