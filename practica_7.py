# EXTRACIÓN DE INFORMACIÓN DE DATOS ABIERTOS SOBRE DEUDA PUBLICA EN CDMX E IMPORTACIÓN DE LIBRERÍAS
import pandas as pd
import matplotlib.pyplot as plt

ruta_csv = r'C:\Users\ACER\Documents\Edgar\URC\PCD\deuda_publica_2023_04.csv'

data_df = pd.read_csv(ruta_csv, encoding='latin1')


# 1.- REVISIÓN GENERAL DE INFORMACIÓN

registros = data_df.shape[0]
print(registros)

data_df.info()

# 2. FUNCIÓN TAIL()

data_df.tail()

# 3. RANGO DE FECHAS

data_df['inicio_credito'] = pd.to_datetime(data_df['inicio_credito'], format="%Y/%m/%d")
fecha_i = data_df['inicio_credito'].min()
fecha_f = data_df['inicio_credito'].max()

print(f"El rango de fechas va desde {fecha_i} hasta {fecha_f}")

# 4- CALCULO DE MEDIA DE DISPOSICIÓN DE CREDITOS

data_df['disposicion_inicial_credito'] = data_df['disposicion_inicial_credito'].astype(float)
pd.options.display.float_format = '{:.2f}'.format

media = data_df['disposicion_inicial_credito'].mean()
print(f"El promedio de disposición por crédito es de {media}")

# 5. MODA DE BANCOS ACREEDORES A LA DEUDA

moda = data_df['acreedor'].mode()
print(f"El Banco acreedor de la deuda más presente es: {moda}")
