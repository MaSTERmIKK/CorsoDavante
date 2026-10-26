from pyspark.sql import SparkSession

# Creazione della sessione Spark
spark = SparkSession.builder.appName("Studenti").getOrCreate()

# Dati degli studenti
studenti = [
    ("Mario", 20, 8),
    ("Luca", 22, 6),
    ("Anna", 19, 9),
    ("Sara", 21, 7),
    ("Paolo", 23, 5)
]

# Creazione del DataFrame
df = spark.createDataFrame(
    studenti,
    ["nome", "eta", "voto"]
)

# Visualizzazione completa
df.show()

# Selezione delle colonne
df.select("nome", "voto").show()

# Chiusura della sessione
spark.stop()