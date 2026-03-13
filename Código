import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 1. Configuración de la página
st.set_page_config(page_title="Mi Dashboard Pro", layout="wide")

# 2. Generación de datos de ejemplo (Sustituye esto por tu CSV o Base de Datos)
def cargar_datos():
    fechas = pd.date_range(start="2025-01-01", periods=100)
    datos = pd.DataFrame({
        "Fecha": fechas,
        "Ventas": np.random.randint(100, 500, size=100),
        "Producto": np.random.choice(['Laptop', 'Tablet', 'Smartphone', 'Monitor'], 100),
        "Region": np.random.choice(['Norte', 'Sur', 'Este', 'Oeste'], 100)
    })
    return datos

df = cargar_datos()

# 3. Barra lateral (Sidebar) para filtros
st.sidebar.header("Filtros")
region_select = st.sidebar.multiselect(
    "Selecciona la Región:",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

df_filtrado = df[df["Region"].isin(region_select)]

# 4. Título Principal
st.title("📊 Dashboard de Rendimiento Comercial")
st.markdown("Bienvenido al panel de control. Aquí puedes ver el resumen de operaciones.")

# 5. Métricas Clave (KPIs)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Ventas Totales", f"${df_filtrado['Ventas'].sum():,}")
with col2:
    st.metric("Promedio de Venta", f"${df_filtrado['Ventas'].mean():.2f}")
with col3:
    st.metric("Registros", len(df_filtrado))

st.divider()

# 6. Visualizaciones
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.subheader("Tendencia Temporal")
    fig_linea = px.line(df_filtrado, x="Fecha", y="Ventas", color="Region", template="plotly_white")
    st.plotly_chart(fig_linea, use_container_width=True)

with col_graf2:
    st.subheader("Ventas por Producto")
    ventas_prod = df_filtrado.groupby("Producto")["Ventas"].sum().reset_index()
    fig_barra = px.bar(ventas_prod, x="Producto", y="Ventas", color="Producto")
    st.plotly_chart(fig_barra, use_container_width=True)

# 7. Tabla de datos
with st.expander("Ver base de datos completa"):
    st.dataframe(df_filtrado, use_container_width=True)
