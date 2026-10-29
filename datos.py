
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, desc

# Crear la sesión de Spark
spark = SparkSession.builder \
    .appName("BatchSuperstoreAnalysis") \
    .getOrCreate()

# 1. Cargar el dataset
print("Cargando datos...")
df = spark.read.csv("samplesuperstore.csv", header=True, inferSchema=True)

# 2. Limpieza (Eliminar nulos en columnas clave)
df_clean = df.dropna(subset=["Sales", "Profit", "Category", "Region"])

# 3. Análisis Exploratorio (EDA)
print("\n--- Ventas Totales por Categoría ---")
ventas_categoria = df_clean.groupBy("Category") \
    .agg(_sum("Sales").alias("Total_Ventas")) \
    .orderBy(desc("Total_Ventas"))
ventas_categoria.show()

print("\n--- Ganancias Totales por Región ---")
ganancias_region = df_clean.groupBy("Region") \
    .agg(_sum("Profit").alias("Total_Ganancias")) \
    .orderBy(desc("Total_Ganancias"))
ganancias_region.show()

# 4. Guardar resultados para graficar posteriormente
ventas_categoria.coalesce(1).write.csv("resultado_ventas", header=True, mode="overwrite")
ganancias_region.coalesce(1).write.csv("resultado_ganancias", header=True, mode="overwrite")

print("\nProceso batch finalizado y resultados guardados.")
spark.stop()