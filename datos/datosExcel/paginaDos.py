import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Función para leer el archivo CSV y crear el DataFrame
def leer_csv(archivo_csv):
    # Leer el archivo CSV
    df = pd.read_csv(archivo_csv)
    
    # Mostrar las primeras filas del DataFrame para verificar
    print("Primeras filas del DataFrame:")
    print(df.head())
    
    return df

# Función para generar el diagrama de dispersión
def graficar_correlacion_lineal(df):
    # Eliminar las columnas no numéricas
    df_numerico = df.select_dtypes(include=['number'])
    
    # Configurar el estilo de seaborn
    sns.set(style="ticks")
    
    # Crear la matriz de gráficos de dispersión (scatterplot matrix)
    pairplot = sns.pairplot(df_numerico, diag_kind="kde", plot_kws={'alpha': 0.6})
    
    # Ajustar título y mostrar el gráfico
    plt.suptitle('Matriz de Gráficos de Dispersión', y=1.02, fontsize=16)
    plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    archivo_csv = "C:/Users/MOMY/Documents/complementario-3125033/datos/datosExcel/paginaDos.csv"  # Usando barras diagonales
    df = leer_csv(archivo_csv)
    graficar_correlacion_lineal(df)