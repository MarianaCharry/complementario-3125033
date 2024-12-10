import pandas as pd
import matplotlib.pyplot as plt

# Función para leer el archivo CSV y crear el DataFrame
def leer_csv(archivo_csv):
    try:
        # Leer el archivo CSV usando punto y coma como delimitador
        df = pd.read_csv(archivo_csv, delimiter=";")
        
        # Mostrar la estructura del DataFrame para verificar
        print("Estructura del DataFrame:")
        print(df.head())
        
        # Verificar que el número de filas es correcto
        if df.shape[0] != 25:
            raise ValueError(f"Se esperaban 25 filas, pero se encontraron {df.shape[0]} filas.")
        
        # Asignar los nombres a las columnas
        df.columns = ['Campos', 'Market Capitalization', 'Cambio', 'Fecha']
        
        # Establecer la columna "Campos" como índice
        df.set_index('Campos', inplace=True)
        
        return df
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
        return None

# Función para graficar los datos del CSV
def graficar_datos(df):
    if df is not None:
        # Configuración del gráfico
        plt.figure(figsize=(10, 6))
        
        # Graficar Market Capitalization y Cambio de cada empresa
        # Grafico de Market Capitalization
        plt.plot(df.index, df['Market Capitalization'], label='Market Capitalization', marker='o', linestyle='-', color='b')
        
        # Grafico de Cambio
        plt.plot(df.index, df['Cambio'], label='Cambio', marker='x', linestyle='--', color='r')
        
        # Agregar título y etiquetas
        plt.title('Market Capitalization y Cambio de Empresas', fontsize=16)
        plt.xlabel('Empresas', fontsize=12)
        plt.ylabel('Valores', fontsize=12)
        plt.xticks(rotation=90)  # Rotar las etiquetas del eje X para que sean legibles
        plt.yticks(range(0, 351, 50))  # Ajustar el rango de los valores en el eje Y
        
        # Agregar leyenda
        plt.legend(title='Indicadores')
        
        # Mostrar gráfico
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    else:
        print("No se pudo generar la gráfica debido a un error en la carga de los datos.")

# Ejemplo de uso
if __name__ == "__main__":
    archivo_csv = "C:/Users/MOMY/Documents/complementario-3125033/datos/datosExcel/paginaDos.csv"  # Ruta del archivo CSV
    df = leer_csv(archivo_csv)
    graficar_datos(df)
