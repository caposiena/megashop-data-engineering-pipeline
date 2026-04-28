from pyspark.sql import SparkSession
from pyspark.sql.functions import sum
spark = SparkSession.builder \
    .appName("MegaShop Visualization") \
    .getOrCreate()

input_path = "data_local/processed_sales"

df = spark.read.parquet(input_path)

print("Dati caricati correttamente")

df.printSchema()
df.show(5)
from pyspark.sql.functions import sum

fatturato_categoria = df.groupBy("category") \
    .agg(sum("amount").alias("fatturato_totale")) \
    .orderBy("fatturato_totale", ascending=False)

print("Fatturato totale per categoria:")
fatturato_categoria.show()
# Conversione a Pandas (dataset piccolo → ok)
pdf = fatturato_categoria.toPandas()

import matplotlib.pyplot as plt
import seaborn as sns

# Grafico a barre
plt.figure()
sns.barplot(x="category", y="fatturato_totale", data=pdf)

plt.title("Fatturato per Categoria")
plt.xticks(rotation=45)

# Salvataggio immagine
plt.savefig("reports/fatturato_per_categoria.png")

print("Grafico salvato come fatturato_per_categoria.png")
spark.stop()