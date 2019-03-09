from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *
import pandas as pd

if __name__ == "__main__":
  sc = SparkContext(appName="CSV2Parquet")
  sqlContext = SQLContext(sc)

  schema = StructType([
          StructField("VendorID", StringType(), True),
          StructField("tpep_pickup_datetime", StringType(), True),
          StructField("tpep_dropoff_datetime", StringType(), True),
          StructField("passenger_count", StringType(), True),
          StructField("trip_distance", StringType(), True),
          StructField("pickup_longitude", StringType(), True),
          StructField("pickup_latitude", StringType(), True),
          StructField("RatecodeID", StringType(), True),
          StructField("store_and_fwd_flag", StringType(), True),
          StructField("dropoff_longitude", StringType(), True),
          StructField("dropoff_latitude", StringType(), True),
          StructField("payment_type", StringType(), True),
          StructField("fare_amount", StringType(), True),
          StructField("extra", StringType(), True),
          StructField("mta_tax", StringType(), True),
          StructField("tip_amount", StringType(), True),
          StructField("tolls_amount", StringType(), True),
          StructField("improvement_surcharge", StringType(), True),
          StructField("total_amount", StringType(), True),
          StructField("PULocationID", StringType(), True),
          StructField("DOLocationID", StringType(), True)])

rdd = sc.textFile("maprfs:///datasets/nyctaxi/yellow_tripdata_2016-12.csv").map(lambda line: line.split(","))
df = sqlContext.createDataFrame(rdd, schema)
#df.write.parquet('maprfs:///datasets/nyctaxi/yellow_tripdata_2016-combined.parquet')
df.write.parquet('maprfs:///datasets/nyctaxi/yellow_tripdata_2016-12.parquet')
