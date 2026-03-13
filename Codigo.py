import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Dashboard de Análisis Comercial",
    page_icon="📈",
    layout="wide"
)

# --- GENERACIÓN DE DATOS (Simulando un archivo de ventas) ---
@st.cache_data # Esto hace que la app sea mucho más rápida
def cargar_datos():
    # Creamos datos ficticios para que el dashboard funcione de inmediato
    np.random.seed(42)
    fechas = pd.date_range(start="2025-01-01", periods=200)
    datos = pd.DataFrame({
        "Fecha": np.random.choice(fechas, 500),
        "Ventas": np.random.uniform(50, 1000, size=500),
        "Categoría": np.random.choice(['Electrónica', 'Hogar', 'Moda', 'Deportes'], 500),
        "Canal": np.random.choice(['Online', 'Tienda Física'], 500)
    })
    return datos.sort_values("Fecha")

df = cargar_datos()

# --- BARRA LATERAL (FILTROS) ---
st.sidebar.image("https://www.streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=200)
st.sidebar.title("Filtros de Control")

# Filtro por Categoría
categorias = st.sidebar.multiselect(
    "Selecciona Categorías:",
    options=df["Categoría"].unique(),
    default=df["Categoría"].unique()
)

# Filtro por Canal
canales = st.sidebar.radio("Canal de Venta:", ["Todos", "Online", "Tienda Física"])

# Aplicar filtros
df_filtrado = df[df["Categoría"].isin(categorias)]
if canales != "Todos":
    df_filtrado = df_filtrado[df_filtrado["Canal"] == canales]

# --- CUERPO PRINCIPAL ---
st.title("🚀 Panel de Control de Ventas 2026")
st.markdown("---")

# KPIs principales
m1, m2, m3 = st.columns(3)
m1.metric("Ventas Totales", f"${df_filtrado['Ventas'].sum():,.2f}", "+5.2%")
m2.metric("Ticket Promedio", f"${df_filtrado['Ventas'].mean():,.2f}")
m3.metric("N° Transacciones", len(df_filtrado))

st.markdown("### Visualización de Tendencias")

# Gráficos con Plotly
col_a, col_b = st.columns([2, 1])

with col_a:
    # Agrupar ventas por fecha para el gráfico de líneas
    ventas_diarias = df_filtrado.groupby("Fecha")["Ventas"].sum().reset_index()
    fig_line = px.line(
        ventas_diarias, x="Fecha", y="Ventas", 
        title="Evolución de Ventas Diarias",
        template="plotly_white",
        line_shape="spline"
    )
    st.plotly_chart(fig_line, use_container_width=True)

with col_b:
    # Gráfico de pastel por Categoría
    fig_pie = px.pie(
        df_filtrado, values="Ventas", names="Categoría", 
        title="Distribución por Categoría",
        hole=0.4
    )
    st.plotly_chart(fig_pie, use_container_width=True)

# Tabla de Datos inferior
st.markdown("### Detalle de Operaciones")
st.dataframe(df_filtrado.head(50), use_container_width=True)
