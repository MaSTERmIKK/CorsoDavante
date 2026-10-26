from pyspark.sql import SparkSession
from pyspark.sql.functions import col  

# Creazione della sessione Spark
spark = SparkSession.builder.appName("Prodotti").getOrCreate()

# Dati dei prodotti
prodotti = [
    ("Mouse", "Informatica", 25),
    ("Tastiera", "Informatica", 60),
    ("Monitor", "Informatica", 180),
    ("Scrivania", "Arredamento", 150),
    ("Lampada", "Arredamento", 35),
    ("Sedia", "Arredamento", 90)
]

# Creazione del DataFrame
df = spark.createDataFrame(
    prodotti,
    ["nome", "categoria", "prezzo"]
)

# Filtro dei prodotti superiori a 50 euro
df_filtrato = df.filter(col("prezzo") > 50)

df_filtrato.show()

# Creazione della colonna con lo sconto
df_scontato = df_filtrato.withColumn(
    "prezzo_scontato",
    col("prezzo") * 0.90
)

# Visualizzazione
df_scontato.show()

spark.stop()