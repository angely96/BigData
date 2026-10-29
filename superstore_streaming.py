from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, window
from pyspark.sql.types import StructType, StructField, StringType, FloatType, IntegerType, TimestampType

# Configurar Spark
spark = SparkSession.builder.appName("SuperstoreStreaming").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

# Esquema de los datos JSON
schema = StructType([
    StructField("Order_ID", StringType()),
    StructField("Category", StringType()),
    StructField("Sales", FloatType()),
    StructField("Quantity", IntegerType()),
    StructField("Profit", FloatType()),
    StructField("timestamp", TimestampType())
])

# Leer el stream desde Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "superstore_stream") \
    .load()

# Parsear el JSON
parsed_df = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

# Calcular ventas y cantidades por categoría en ventanas de 1 minuto
windowed_stats = parsed_df \
    .groupBy(window(col("timestamp"), "1 minute"), "Category") \
    .agg({"Sales": "sum", "Quantity": "sum"})

# Escribir los resultados en la consola
query = windowed_stats.writeStream \
    .outputMode("complete") \
    .format("console") \
    .option("truncate", "false") \
    .start()

query.awaitTermination()