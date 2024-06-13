{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "bc204bed-2eed-4ebb-88bf-0dd0c3fbc341",
   "metadata": {},
   "source": [
    "# Práctica 7"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "935fe844-429f-4606-84f3-9d9be86e6866",
   "metadata": {},
   "source": [
    "## Extracción de los datos de deuda publica en la CDMX"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "18c6e872-064f-4908-b0f0-1e1caaaeaaef",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "12a48f4c-53fd-4154-8c28-166bbd70d03a",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "ruta_csv = r'C:\\Users\\ACER\\Documents\\Edgar\\URC\\PCD\\deuda_publica_2023_04.csv'\n",
    "\n",
    "data_df = pd.read_csv(ruta_csv, encoding='latin1')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "747115df-93d3-4bea-8905-a6cc25592d86",
   "metadata": {},
   "source": [
    "## Visualización de información general (info y tail)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "01880e94-9b31-4c87-a747-06b3abf26889",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "983\n"
     ]
    }
   ],
   "source": [
    "registros = data_df.shape[0]\n",
    "print(registros)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "6fc1aebb-61ba-4b62-9a09-7740d22cb387",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 983 entries, 0 to 982\n",
      "Data columns (total 22 columns):\n",
      " #   Column                       Non-Null Count  Dtype  \n",
      "---  ------                       --------------  -----  \n",
      " 0   anio                         983 non-null    int64  \n",
      " 1   trimestre                    983 non-null    object \n",
      " 2   mes                          983 non-null    object \n",
      " 3   no_registro                  983 non-null    object \n",
      " 4   tipo_deuda                   983 non-null    object \n",
      " 5   detalle_tipo_deuda           983 non-null    object \n",
      " 6   acreedor                     983 non-null    object \n",
      " 7   concepto                     983 non-null    object \n",
      " 8   inicio_credito               934 non-null    object \n",
      " 9   fin_credito                  934 non-null    object \n",
      " 10  dias_contrato                983 non-null    int64  \n",
      " 11  dias_restantes_contrato      983 non-null    int64  \n",
      " 12  disposicion_inicial_credito  983 non-null    float64\n",
      " 13  colocacion_periodo           983 non-null    float64\n",
      " 14  amortizaciones_periodo       964 non-null    float64\n",
      " 15  intereses_periodo            983 non-null    float64\n",
      " 16  pago_servicio_deuda          980 non-null    float64\n",
      " 17  saldo_periodo                983 non-null    float64\n",
      " 18  endeudamiento_periodo        983 non-null    float64\n",
      " 19  tasa                         983 non-null    object \n",
      " 20  sobretasa                    525 non-null    object \n",
      " 21  tasa_final                   966 non-null    object \n",
      "dtypes: float64(7), int64(3), object(12)\n",
      "memory usage: 169.1+ KB\n"
     ]
    }
   ],
   "source": [
    "data_df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "189a7cdb-926d-41b7-bd5b-56985b56908e",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>anio</th>\n",
       "      <th>trimestre</th>\n",
       "      <th>mes</th>\n",
       "      <th>no_registro</th>\n",
       "      <th>tipo_deuda</th>\n",
       "      <th>detalle_tipo_deuda</th>\n",
       "      <th>acreedor</th>\n",
       "      <th>concepto</th>\n",
       "      <th>inicio_credito</th>\n",
       "      <th>fin_credito</th>\n",
       "      <th>...</th>\n",
       "      <th>disposicion_inicial_credito</th>\n",
       "      <th>colocacion_periodo</th>\n",
       "      <th>amortizaciones_periodo</th>\n",
       "      <th>intereses_periodo</th>\n",
       "      <th>pago_servicio_deuda</th>\n",
       "      <th>saldo_periodo</th>\n",
       "      <th>endeudamiento_periodo</th>\n",
       "      <th>tasa</th>\n",
       "      <th>sobretasa</th>\n",
       "      <th>tasa_final</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>978</th>\n",
       "      <td>2023</td>\n",
       "      <td>Cuarto Trimestre</td>\n",
       "      <td>Diciembre</td>\n",
       "      <td>P09-1118104</td>\n",
       "      <td>Largo Plazo</td>\n",
       "      <td>Mercado de Capitales</td>\n",
       "      <td>CI BANCO</td>\n",
       "      <td>BONO GCDMXCB 18V</td>\n",
       "      <td>2018-11-21</td>\n",
       "      <td>2028-11-08</td>\n",
       "      <td>...</td>\n",
       "      <td>1.100000e+09</td>\n",
       "      <td>0.000000e+00</td>\n",
       "      <td>0.0</td>\n",
       "      <td>55221833.33</td>\n",
       "      <td>55221833.33</td>\n",
       "      <td>1.100000e+09</td>\n",
       "      <td>0.000000e+00</td>\n",
       "      <td>9.93</td>\n",
       "      <td>NaN</td>\n",
       "      <td>9.93</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>979</th>\n",
       "      <td>2023</td>\n",
       "      <td>Cuarto Trimestre</td>\n",
       "      <td>Diciembre</td>\n",
       "      <td>P09-1223078</td>\n",
       "      <td>Largo Plazo</td>\n",
       "      <td>Banca Comercial</td>\n",
       "      <td>SANTANDER</td>\n",
       "      <td>SANTANDER 2,169</td>\n",
       "      <td>2023-12-15</td>\n",
       "      <td>2033-12-14</td>\n",
       "      <td>...</td>\n",
       "      <td>2.169946e+09</td>\n",
       "      <td>2.169946e+09</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>2.169946e+09</td>\n",
       "      <td>2.169946e+09</td>\n",
       "      <td>9.1999999999999993</td>\n",
       "      <td>NaN</td>\n",
       "      <td>9.1999999999999993</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>980</th>\n",
       "      <td>2023</td>\n",
       "      <td>Cuarto Trimestre</td>\n",
       "      <td>Diciembre</td>\n",
       "      <td>P09-1223079</td>\n",
       "      <td>Largo Plazo</td>\n",
       "      <td>Banca de Desarrollo</td>\n",
       "      <td>BANOBRAS</td>\n",
       "      <td>BANOBRAS 2,500 23-1</td>\n",
       "      <td>2023-12-15</td>\n",
       "      <td>2043-12-15</td>\n",
       "      <td>...</td>\n",
       "      <td>2.500000e+09</td>\n",
       "      <td>2.500000e+09</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>2.500000e+09</td>\n",
       "      <td>2.500000e+09</td>\n",
       "      <td>8.83</td>\n",
       "      <td>NaN</td>\n",
       "      <td>8.83</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>981</th>\n",
       "      <td>2023</td>\n",
       "      <td>Cuarto Trimestre</td>\n",
       "      <td>Diciembre</td>\n",
       "      <td>P09-1223080</td>\n",
       "      <td>Largo Plazo</td>\n",
       "      <td>Banca de Desarrollo</td>\n",
       "      <td>BANOBRAS</td>\n",
       "      <td>BANOBRAS 2,500 23-2</td>\n",
       "      <td>2023-12-15</td>\n",
       "      <td>2043-12-15</td>\n",
       "      <td>...</td>\n",
       "      <td>2.500000e+09</td>\n",
       "      <td>2.500000e+09</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>2.500000e+09</td>\n",
       "      <td>2.500000e+09</td>\n",
       "      <td>8.93</td>\n",
       "      <td>NaN</td>\n",
       "      <td>8.93</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>982</th>\n",
       "      <td>2023</td>\n",
       "      <td>Cuarto Trimestre</td>\n",
       "      <td>Diciembre</td>\n",
       "      <td>P09-1223081</td>\n",
       "      <td>Largo Plazo</td>\n",
       "      <td>Banca de Desarrollo</td>\n",
       "      <td>BANOBRAS</td>\n",
       "      <td>BANOBRAS 5,276</td>\n",
       "      <td>2023-12-15</td>\n",
       "      <td>2043-12-15</td>\n",
       "      <td>...</td>\n",
       "      <td>4.974579e+09</td>\n",
       "      <td>4.974579e+09</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>4.974579e+09</td>\n",
       "      <td>4.974579e+09</td>\n",
       "      <td>TIIE Fondeo</td>\n",
       "      <td>0.44</td>\n",
       "      <td>TIIE Fondeo+0.44</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 22 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     anio         trimestre        mes  no_registro   tipo_deuda  \\\n",
       "978  2023  Cuarto Trimestre  Diciembre  P09-1118104  Largo Plazo   \n",
       "979  2023  Cuarto Trimestre  Diciembre  P09-1223078  Largo Plazo   \n",
       "980  2023  Cuarto Trimestre  Diciembre  P09-1223079  Largo Plazo   \n",
       "981  2023  Cuarto Trimestre  Diciembre  P09-1223080  Largo Plazo   \n",
       "982  2023  Cuarto Trimestre  Diciembre  P09-1223081  Largo Plazo   \n",
       "\n",
       "       detalle_tipo_deuda   acreedor             concepto inicio_credito  \\\n",
       "978  Mercado de Capitales   CI BANCO     BONO GCDMXCB 18V     2018-11-21   \n",
       "979       Banca Comercial  SANTANDER      SANTANDER 2,169     2023-12-15   \n",
       "980   Banca de Desarrollo   BANOBRAS  BANOBRAS 2,500 23-1     2023-12-15   \n",
       "981   Banca de Desarrollo   BANOBRAS  BANOBRAS 2,500 23-2     2023-12-15   \n",
       "982   Banca de Desarrollo   BANOBRAS       BANOBRAS 5,276     2023-12-15   \n",
       "\n",
       "    fin_credito  ...  disposicion_inicial_credito  colocacion_periodo  \\\n",
       "978  2028-11-08  ...                 1.100000e+09        0.000000e+00   \n",
       "979  2033-12-14  ...                 2.169946e+09        2.169946e+09   \n",
       "980  2043-12-15  ...                 2.500000e+09        2.500000e+09   \n",
       "981  2043-12-15  ...                 2.500000e+09        2.500000e+09   \n",
       "982  2043-12-15  ...                 4.974579e+09        4.974579e+09   \n",
       "\n",
       "     amortizaciones_periodo  intereses_periodo  pago_servicio_deuda  \\\n",
       "978                     0.0        55221833.33          55221833.33   \n",
       "979                     0.0               0.00                 0.00   \n",
       "980                     0.0               0.00                 0.00   \n",
       "981                     0.0               0.00                 0.00   \n",
       "982                     0.0               0.00                 0.00   \n",
       "\n",
       "     saldo_periodo  endeudamiento_periodo                tasa  sobretasa  \\\n",
       "978   1.100000e+09           0.000000e+00                9.93        NaN   \n",
       "979   2.169946e+09           2.169946e+09  9.1999999999999993        NaN   \n",
       "980   2.500000e+09           2.500000e+09                8.83        NaN   \n",
       "981   2.500000e+09           2.500000e+09                8.93        NaN   \n",
       "982   4.974579e+09           4.974579e+09         TIIE Fondeo       0.44   \n",
       "\n",
       "             tasa_final  \n",
       "978                9.93  \n",
       "979  9.1999999999999993  \n",
       "980                8.83  \n",
       "981                8.93  \n",
       "982    TIIE Fondeo+0.44  \n",
       "\n",
       "[5 rows x 22 columns]"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_df.tail()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "17153a3e-2069-4ff1-be41-c1c21d61245b",
   "metadata": {},
   "source": [
    "## Rango de fechas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "9c9f6d0a-b395-4a90-9efc-b9a5a68b9f80",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "data_df['inicio_credito'] = pd.to_datetime(data_df['inicio_credito'], format=\"%Y/%m/%d\")\n",
    "fecha_i = data_df['inicio_credito'].min()\n",
    "fecha_f = data_df['inicio_credito'].max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "65209916-64db-4a8a-9dc6-630492e0bc6b",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "El rango de fechas va desde 2007-08-30 00:00:00 hasta 2023-12-15 00:00:00\n"
     ]
    }
   ],
   "source": [
    "print(f\"El rango de fechas va desde {fecha_i} hasta {fecha_f}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fdebbf0b-5541-4dbf-8d42-6e05ae24ad43",
   "metadata": {},
   "source": [
    "## Calculo de media y moda de montos iniciales de crédito y banco acreedor"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "9a01102a-e4da-4efb-bfcc-c9297b5fc202",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "data_df['disposicion_inicial_credito'] = data_df['disposicion_inicial_credito'].astype(float)\n",
    "pd.options.display.float_format = '{:.2f}'.format"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "5514441f-cd64-4bc4-b02f-b24c07516c3c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "El promedio de disposición por crédito es de 2378323279.5784636\n"
     ]
    }
   ],
   "source": [
    "media = data_df['disposicion_inicial_credito'].mean()\n",
    "print(f\"El promedio de disposición por crédito es de {media}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "60ecdc6d-141f-49f7-a7eb-b3f9aad5f8f7",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "El Banco acreedor de la deuda más presente es: 0    BANOBRAS\n",
      "Name: acreedor, dtype: object\n"
     ]
    }
   ],
   "source": [
    "moda = data_df['acreedor'].mode()\n",
    "print(f\"El Banco acreedor de la deuda más presente es: {moda}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "fa6cd767-876a-467d-a3dc-1232e9fc45d1",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (2238935765.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[47], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    jupyter nbconvert --to script practica_7.ipynb\u001b[0m\n\u001b[1;37m            ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "jupyter nbconvert --to script practica_7.ipynb"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "680d662d-eba4-4176-bace-9e8816ce6053",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
