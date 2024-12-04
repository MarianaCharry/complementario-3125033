# Importar las bibliotecas necesarias
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el archivo CSV
# Asegúrate de que el archivo CSV esté en el mismo directorio que tu script o proporciona la ruta completa.
df = pd.read_csv('paginaUno.csv')

# Verificar los datos cargados
print(df.head())

# Calcular la matriz de correlación
correlation_matrix = df.corr()

# Configurar el tamaño de la figura
plt.figure(figsize=(10, 8))

# Crear un mapa de calor (heatmap) para visualizar la correlación
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', cbar=True)

# Mostrar el gráfico
plt.title('Diagrama de Correlación')
plt.show()
