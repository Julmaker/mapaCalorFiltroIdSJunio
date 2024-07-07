"""Mapa de Calor de Indices de soporte Junio 2024 Con filtro"""

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from folium.plugins import HeatMap

# Título de la aplicación
st.title("Mapa de Calor Índices de Soporte Junio 2024 Interactivo")

# Ruta del archivo Excel
archivo_excel = "MapadeCalorJunio.xlsx"

# Cargar datos desde el archivo Excel
df = pd.read_excel(archivo_excel)

# Mostrar el DataFrame
st.write("Datos cargados:", df)

# Filtrar por semana
semanas = ['Todas'] + df['Semana'].unique().tolist()
semana_seleccionada = st.selectbox("Selecciona una semana", semanas)

if semana_seleccionada != 'Todas':
    df_filtrado = df[df['Semana'] == semana_seleccionada]
else:
    df_filtrado = df

# Centro del mapa en la República Mexicana
centro_mexico = [23.634501, -102.552784]

# Crear el mapa de calor
m = folium.Map(location=centro_mexico, zoom_start=5)

# Añadir puntos de calor
heat_data = [[row['Latitud'], row['Longitud']] for index, row in df_filtrado.iterrows()]
HeatMap(heat_data).add_to(m)

# Mostrar el mapa en Streamlit
folium_static(m)
