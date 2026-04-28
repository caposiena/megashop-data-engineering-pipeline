from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MegaShop ETL Pipeline") \
    .getOrCreate()

print("SparkSession avviata correttamente")

spark.stop()