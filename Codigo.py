import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Artículo: IA y Ansiedad", layout="centered")

# Inyección de CSS para forzar el estilo elegante y la fuente Times New Roman
st.markdown("""
    <style>
    /* Importar o definir la fuente global */
    html, body, [class*="css"] {
        font-family: "Times New Roman", Times, serif;
        background-color: #ffffff;
    }
    
    /* Fondo blanco para la aplicación principal */
    .stApp {
        background-color: #ffffff;
    }

    /* Estilo para el Título (Grande y en Times New Roman) */
    .titulo-principal {
        font-family: "Times New Roman", Times, serif;
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        color: #000000;
        line-height: 1.2;
        padding-top: 20px;
    }

    /* Frase Motivadora (Derecha, Cursiva, Times New Roman) */
    .frase-motivadora {
        font-family: "Times New Roman", Times, serif;
        font-style: italic;
        text-align: right;
        font-size: 20px;
        color: #444444;
        margin: 40px 0;
        border-right: 4px solid #000;
        padding-right: 15px;
    }

    /* Cuerpo del Artículo (Mediano, Elegante) */
    .cuerpo-texto {
        font-family: "Times New Roman", Times, serif;
        font-size: 20px;
        text-align: justify;
        color: #1a1a1a;
        line-height: 1.6;
    }

    /* Subtítulos */
    .subtitulo {
        font-family: "Times New Roman", Times, serif;
        font-size: 26px;
        font-weight: bold;
        margin-top: 30px;
        color: #000000;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONTENIDO DEL DASHBOARD ---

# Título del artículo
st.markdown('<div class="titulo-principal">¿Un psicólogo en tu bolsillo? Luces y sombras de la IA generativa frente a la ansiedad</div>', unsafe_allow_html=True)

# Frase motivadora
st.markdown('<div class="frase-motivadora">Tu mente es el territorio y la innovación la herramienta; el verdadero poder de cambio siempre reside en la valentía de conocerte a ti mismo.</div>', unsafe_allow_html=True)

# Cuerpo del artículo
st.markdown("""
<div class="cuerpo-texto">
    En la última década, la ansiedad ha dejado de ser una preocupación individual para convertirse en un desafío de salud pública global. 
    Se ha consolidado como una de las principales causas de discapacidad y pérdida de productividad en la población activa. 
    A pesar de que existen tratamientos efectivos, factores como el alto costo de la terapia, la falta de profesionales en zonas rurales 
    y el estigma social impiden que muchas personas reciban ayuda oportuna. En este escenario, la Inteligencia Artificial (IA) generativa 
    surge como una herramienta disruptiva que promete democratizar el cuidado de la salud mental. Pero, ¿qué tan sólida es esta promesa y 
    cuáles son sus riesgos?
</div>
""", unsafe_allow_html=True)

# Subtítulo y continuación
st.markdown('<div class="subtitulo">El potencial: ¿Por qué la IA funciona para la ansiedad?</div>', unsafe_allow_html=True)

st.markdown("""
<div class="cuerpo-texto">
    La mayoría de los chatbots actuales no operan al azar; su sustento teórico es la <b>Terapia Cognitivo-Conductual (TCC)</b>. 
    Esta terapia se centra en identificar y reestructurar patrones de pensamiento catastróficos, algo que, por su naturaleza protocolizada, 
    es ideal para ser traducido a algoritmos de respuesta.
</div>
""", unsafe_allow_html=True)

# Pie de página elegante
st.markdown("---")
st.caption("Dashboard de Divulgación Científica | Creado con Streamlit")
