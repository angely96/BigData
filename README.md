ste proyecto implementa una solución de Big Data utilizando Apache Spark y Apache Kafka para el análisis de un conjunto de datos de ventas de un supermercado (`samplesuperstore.csv`). El proyecto se divide en dos componentes principales:
1. **Procesamiento en Batch:** Limpieza, transformación y análisis exploratorio de datos (EDA) utilizando DataFrames de PySpark.
2. **Procesamiento en Tiempo Real:** Simulación de llegada de datos usando Kafka y procesamiento de flujos (Streaming) con Spark.

## Requisitos Previos
* Ubuntu 22.04 (Máquina Virtual)
* Java 11
* Apache Spark 3.5.3
* Apache Kafka 3.6.2
* Python 3
* Librerías de Python: `pyspark`, `kafka-python`, `pandas`, `matplotlib`

## Estructura del Repositorio
* `batch_superstore.py`: Script de PySpark para el procesamiento batch y EDA.
* `graficar.py`: Script de Python para generar gráficos a partir de los resultados del batch.
* `superstore_producer.py`: Script que actúa como generador de datos en tiempo real (envía datos a Kafka).
* `superstore_streaming.py`: Script de PySpark Streaming que consume los datos de Kafka y calcula estadísticas.
* `samplesuperstore.csv`: (Opcional) El dataset utilizado.

## Instrucciones de Ejecución

### 1. Iniciar ZooKeeper y Kafka
```bash
sudo /opt/Kafka/bin/zookeeper-server-start.sh /opt/Kafka/config/zookeeper.properties
# En otra terminal:
sudo /opt/Kafka/bin/kafka-server-start.sh /opt/Kafka/config/server.properties
