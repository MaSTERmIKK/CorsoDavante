from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, col

# Creazione della sessione Spark
spark = SparkSession.builder.appName("Vendite").getOrCreate()

# Dati delle vendite
vendite = [
    ("Mouse", "Informatica", 30),
    ("Tastiera", "Informatica", 70),
    ("Monitor", "Informatica", 200),
    ("Sedia", "Arredamento", 100),
    ("Scrivania", "Arredamento", 180),
    ("Lampada", "Arredamento", 40),
    ("Penna", "Cancelleria", 5),
    ("Quaderno", "Cancelleria", 15)
]

# Creazione del DataFrame
df = spark.createDataFrame(
    vendite,
    ["prodotto", "categoria", "importo"]
)

# Raggruppamento e somma delle vendite
df_totali = df.groupBy("categoria").agg(
    sum("importo").alias("totale_vendite")
)

# Ordinamento decrescente
df_ordinato = df_totali.orderBy(
    col("totale_vendite").desc()
)

# Visualizzazione
df_ordinato.show()

spark.stop()