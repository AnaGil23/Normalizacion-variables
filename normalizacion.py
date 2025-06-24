
import geopandas as gpd
import pandas as pd
from sklearn.preprocessing import StandardScaler

gdf = gpd.read_file(r'C:\Users\ana_g\Desktop\tfm2\parcelas_disueltas_pct2.gpkg')

# Definir las variables a normalizar
variables = [
    'pob_menor5_pct', 'pob_mayor65_pct', 'extran_vulner_pct', 'mujeres_pct',
    'ocup_elementales_pct', 'cuenta_propia_pct', 'parados_pct', 'estudios_primaria_pct',
    'densidad_poblacion', 'renta_total_estim_parcela', 'antiguedad', 'usos_cod',
    'planta_baja_vulnerable', 'elemento_sensible', 'centro_educativo',
    'centro_inclusivo', 'centro_salud', 'farmacia'
]

# Seleccionar solo esas columnas
X = gdf[variables].copy()

# Aplicar normalización z-score
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Añadir las columnas normalizadas al GeoDataFrame con sufijo "_zscore"
for i, col in enumerate(variables):
    gdf[col + "_zscore"] = X_scaled[:, i]
for col in ['elemento_sensible', 'centro_educativo', 'farmacia', 'centro_salud']:
    print(col, gdf[col].unique())

# Guardar el GeoDataFrame con variables normalizadas
#gdf.to_file(r"C:\Users\ana_g\Desktop\tfm2\parcelas_disueltas_pct2_normalizado_prueba.gpkg", driver="GPKG")