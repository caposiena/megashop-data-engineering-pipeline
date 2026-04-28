from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MegaShop ETL Pipeline") \
    .getOrCreate()

print("SparkSession avviata correttamente")

# Percorsi dei file parquet
transaction_files = [
    "data_local/parquet/transactions_batch_0000.parquet",
    "data_local/parquet/transactions_batch_0001.parquet",
    "data_local/parquet/transactions_batch_0002.parquet",
    "data_local/parquet/transactions_batch_0003.parquet",
    "data_local/parquet/transactions_batch_0004.parquet",
]

products_path = "data_local/parquet/products.parquet"
regions_path = "data_local/parquet/regions.parquet"

# Extract
transactions_df = spark.read.parquet(*transaction_files)
products_df = spark.read.parquet(products_path)
regions_df = spark.read.parquet(regions_path)

print("=== TRANSACTIONS ===")
transactions_df.show(5)

print("=== PRODUCTS ===")
products_df.show(5)

print("=== REGIONS ===")
regions_df.show(5)
# JOIN con prodotti (per ottenere category)
df_joined = transactions_df.join(products_df, on="product_id", how="inner")

# JOIN con regioni (per ottenere region_name)
df_joined = df_joined.join(regions_df, on="region_id", how="inner")

# Selezione colonne finali (DataFrame pulito)
final_df = df_joined.select(
    "transaction_id",
    "region_name",
    "category",
    "amount",
    "year"
)

print("=== DATAFRAME FINALE ===")
final_df.show(5)

output_path = "data_local/processed_sales"

final_df.coalesce(1).write \
    .mode("overwrite") \
    .option("mapreduce.fileoutputcommitter.marksuccessfuljobs", "false") \
    .partitionBy("year") \
    .parquet(output_path)

print(f"Dati salvati correttamente in: {output_path}")

spark.stop()