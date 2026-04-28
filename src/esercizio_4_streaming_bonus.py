from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType, IntegerType, FloatType

spark = SparkSession.builder \
    .appName("MegaShop Streaming Bonus") \
    .getOrCreate()

schema = StructType() \
    .add("transaction_id", StringType()) \
    .add("customer_id", IntegerType()) \
    .add("product_id", IntegerType()) \
    .add("region_id", IntegerType()) \
    .add("quantity", IntegerType()) \
    .add("amount", FloatType()) \
    .add("ts", StringType()) \
    .add("year", IntegerType()) \
    .add("month", IntegerType())

streaming_df = spark.readStream \
    .schema(schema) \
    .json("data_local/json")

conteggio_regioni = streaming_df.groupBy("region_id").count()

query = conteggio_regioni.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

print("Streaming avviato. Aggiungi nuovi file JSON nella cartella data_local/json.")

query.awaitTermination()