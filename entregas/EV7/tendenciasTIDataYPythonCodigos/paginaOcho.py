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
        if df.shape[0] != 13:
            raise ValueError(f"Se esperaban 13 filas, pero se encontraron {df.shape[0]} filas.")
        
        # Asignar los nombres a las columnas, los años (del 2018 al 2023)
        df.columns = ['Marcos móviles', '2019', '2020', '2021', '2022', '2023']
        
        # Establecer la columna "Sistema Operativo" como índice
        df.set_index('Marcos móviles', inplace=True)
        
        return df
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
        return None

# Función para graficar los datos del CSV
def graficar_datos(df):
    if df is not None:
        # Configuración del gráfico
        plt.figure(figsize=(10, 6))
         
        # Graficar cada sistema operativo
        for sistema in df.index:
            plt.plot(df.columns, df.loc[sistema], label=sistema, marker='o')
        
        # Agregar título y etiquetas
        plt.title('Marcos móviles multiplataforma utilizados por desarrolladores de software en todo el mundo entre 2019 y 2023', fontsize=16)
        plt.xlabel('Año', fontsize=12)
        plt.ylabel('Porcentaje (%)', fontsize=12)
        plt.xticks(df.columns, rotation=45)
        plt.yticks(range(0, 101, 10))
        
        # Agregar leyenda
        plt.legend(title='Marcos móviles')
        
        # Mostrar gráfico
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    else:
        print("No se pudo generar la gráfica debido a un error en la carga de los datos.")

# Ejemplo de uso
if __name__ == "__main__":
    archivo_csv = "C:/Users/MOMY/Documents/complementario-3125033/datos/datosExcel/paginaOcho.csv"  # Ruta del archivo CSV
    df = leer_csv(archivo_csv)
    graficar_datos(df)
