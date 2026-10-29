import time
import json
import csv
from kafka import KafkaProducer

# Configurar el productor de Kafka
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

# Leer el dataset
with open('samplesuperstore.csv', mode='r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    data = list(reader)

print("Iniciando simulación de datos en tiempo real...")
while True:
    for row in data:
        try:
            # Extraer datos clave y formatearlos como JSON
            order_data = {
                "Order_ID": row["Order ID"],
                "Category": row["Category"],
                "Sales": float(row["Sales"]),
                "Quantity": int(row["Quantity"]),
                "Profit": float(row["Profit"]),
                "timestamp": int(time.time())
            }
            
            # Enviar a Kafka
            producer.send('superstore_stream', value=order_data)
            print(f"Enviado: {order_data['Order_ID']} - {order_data['Category']} - ${order_data['Sales']}")
            
            # Pausa de 1 segundo para simular tiempo real
            time.sleep(1) 
        except Exception as e:
            pass # Ignorar filas con errores