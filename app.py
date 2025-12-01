import pandas as pd
import plotly.express as px
import streamlit as st

# Configuración de la página (opcional, pero se ve mejor)
st.set_page_config(page_title="Venta de Vehículos", layout="wide")

# 1. Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# 2. Crear el encabezado principal
st.header('Tablero de Análisis de Vehículos')
st.markdown("Utiliza las casillas de verificación a continuación para explorar los datos.")

# --- Lógica de Casillas de Verificación (Checkboxes) ---

# Casilla 1: Histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla está seleccionada
    st.write('Construyendo un histograma para la columna de odómetro (kilometraje)')
    
    # Crear histograma
    fig = px.histogram(car_data, x="odometer", title="Distribución del Kilometraje")
    
    # Mostrar gráfico
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter: # si la casilla está seleccionada
    st.write('Construyendo un gráfico de dispersión para evaluar Precio vs. Kilometraje')
    
    # CORRECCIÓN: Usamos 'opacity' en lugar de 'alpha'
    fig = px.scatter(car_data, x="odometer", y="price", title="Precio vs. Kilometraje", opacity=0.5)
    
    # Mostrar gráfico
    st.plotly_chart(fig, use_container_width=True)



