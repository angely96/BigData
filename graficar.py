import pandas as pd
import matplotlib.pyplot as plt
import glob

# Leer los resultados que guardó Spark
archivo_ventas = glob.glob("resultado_ventas/*.csv")[0]
archivo_ganancias = glob.glob("resultado_ganancias/*.csv")[0]

df_ventas = pd.read_csv(archivo_ventas)
df_ganancias = pd.read_csv(archivo_ganancias)

# Crear figura con dos gráficos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Gráfico 1: Ventas por Categoría
ax1.bar(df_ventas['Category'], df_ventas['Total_Ventas'], color='skyblue')
ax1.set_title('Ventas Totales por Categoría')
ax1.set_ylabel('Ventas ($)')

# Gráfico 2: Ganancias por Región
ax2.bar(df_ganancias['Region'], df_ganancias['Total_Ganancias'], color='lightgreen')
ax2.set_title('Ganancias Totales por Región')
ax2.set_ylabel('Ganancias ($)')

plt.tight_layout()
plt.savefig("visualizacion_batch.png")
print("¡Gráfico guardado como 'visualizacion_batch.png'!")