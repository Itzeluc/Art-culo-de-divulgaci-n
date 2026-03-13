import streamlit as st

# Configuración de la página
st.set_page_config(page_title="IA y Ansiedad", layout="centered")

# Inyección de CSS para estilo y fuente Times New Roman
st.markdown("""
    <style>
    /* Estilo Global y Fondo Blanco */
    html, body, [class*="css"], .stApp {
        font-family: "Times New Roman", Times, serif !important;
        background-color: #ffffff;
        color: #000000;
    }

    /* Título del artículo (Letra grande) */
    .titulo-principal {
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 30px;
        line-height: 1.2;
    }

    /* Frase motivadora (Derecha y Cursiva) */
    .frase-motivadora {
        font-style: italic;
        text-align: right;
        font-size: 18px;
        margin: 40px 0;
        color: #333333;
    }

    /* Cuerpo del artículo (Tamaño mediano, diseño moderno) */
    .cuerpo-texto {
        font-size: 19px;
        text-align: justify;
        line-height: 1.6;
        margin-bottom: 20px;
    }

    /* Subtítulos */
    .subtitulo {
        font-size: 24px;
        font-weight: bold;
        margin-top: 35px;
        margin-bottom: 15px;
        border-left: 5px solid #000;
        padding-left: 15px;
    }

    /* Estilo para las Referencias */
    .referencia-item {
        font-size: 16px;
        margin-bottom: 10px;
        color: #000000;
        text-decoration: underline;
        cursor: pointer;
    }
    
    /* Ajuste para que los botones de Streamlit parezcan texto de referencia */
    .stButton>button {
        border: none;
        background: none;
        padding: 0;
        color: #0000EE;
        text-decoration: underline;
        font-family: "Times New Roman", Times, serif;
        font-size: 16px;
        text-align: left;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONTENIDO DEL ARTÍCULO ---

# Título [cite: 3, 4]
st.markdown('<div class="titulo-principal">¿Un psicólogo en tu bolsillo? Luces y sombras de la IA generativa frente a la ansiedad</div>', unsafe_allow_html=True)

# Frase Motivadora [cite: 5, 6, 7]
st.markdown('<div class="frase-motivadora">Tu mente es el territorio y la innovación la herramienta;<br>el verdadero poder de cambio siempre reside en la valentía de conocerte a ti mismo.</div>', unsafe_allow_html=True)

# Cuerpo del artículo - Introducción [cite: 11-15]
st.markdown(f"""
<div class="cuerpo-texto">
    En la última década, la ansiedad ha dejado de ser una preocupación individual para convertirse en un desafío de salud pública global[cite: 11]. 
    Se ha consolidado como una de las principales causas de discapacidad y pérdida de productividad en la población activa[cite: 12]. 
    A pesar de que existen tratamientos efectivos, factores como el alto costo de la terapia, la falta de profesionales en zonas rurales y el estigma social impiden que muchas personas reciban ayuda oportuna[cite: 13]. 
    En este escenario, la Inteligencia Artificial (IA) generativa surge como una herramienta disruptiva que promete democratizar el cuidado de la salud mental[cite: 14]. 
    Pero, ¿qué tan sólida es esta promesa y cuáles son sus riesgos? [cite: 15]
</div>
""", unsafe_allow_html=True)

# El Potencial [cite: 16-18]
st.markdown('<div class="subtitulo">El potencial: ¿Por qué la IA funciona para la ansiedad?</div>', unsafe_allow_html=True)
st.markdown("""
<div class="cuerpo-texto">
    La mayoría de los chatbots actuales no operan al azar; su sustento teórico es la <b>Terapia Cognitivo-Conductual (TCC)</b>[cite: 17]. 
    Esta terapia se centra en identificar y reestructurar patrones de pensamiento catastróficos, algo que, por su naturaleza protocolizada, es ideal para ser traducido a algoritmos de respuesta[cite: 18].
</div>
""", unsafe_allow_html=True)

# Ventajas [cite: 19-26]
st.markdown('<div class="subtitulo">Las ventajas de un "entrenador de bolsillo"</div>', unsafe_allow_html=True)
st.markdown("""
<div class="cuerpo-texto">
    El uso de estos agentes conversacionales ofrece beneficios que el sistema tradicional difícilmente puede igualar[cite: 20]:
    <ul>
        <li><b>Disponibilidad 24/7 e inmediatez:</b> El apoyo está presente en el momento exacto de una crisis de pánico o estrés[cite: 21].</li>
        <li><b>Anonimato y reducción del estigma:</b> Al interactuar con una máquina, muchos pacientes se sienten libres del juicio social[cite: 22].</li>
        <li><b>Alianza terapéutica digital:</b> Los usuarios pueden desarrollar un vínculo de confianza con la IA, sintiéndose validados[cite: 23].</li>
        <li><b>Personalización profunda:</b> La IA generativa adapta su tono y sugerencias a la historia específica del usuario[cite: 24].</li>
    </ul>
    Incluso se están explorando fronteras como la <b>Realidad Virtual (RV)</b> asistida por IA, que permite practicar interacciones en escenarios seguros, reduciendo la fobia social hasta en un 20%[cite: 25, 26].
</div>
""", unsafe_allow_html=True)

# Riesgos [cite: 27-36]
st.markdown('<div class="subtitulo">La otra cara de la moneda: Riesgos y desafíos éticos</div>', unsafe_allow_html=True)
st.markdown("""
<div class="cuerpo-texto">
    No todo es optimismo. La implementación de la IA plantea dilemas profundos[cite: 28]. Uno de los mayores retos son las <b>"alucinaciones"</b>, donde el sistema genera información incorrecta o peligrosa[cite: 29, 30]. Además, existe el riesgo de que la IA no detecte señales sutiles de ideación suicida[cite: 32]. 
    La confidencialidad es otra piedra angular; el uso de datos sensibles genera preocupaciones sobre la privacidad[cite: 34]. Finalmente, aún no sabemos si estos efectos perduran una vez que el "efecto de novedad" desaparece[cite: 36].
</div>
""", unsafe_allow_html=True)

# Modelo Híbrido y Conclusión [cite: 37-45]
st.markdown('<div class="subtitulo">El Modelo de Cuidado Escalonado: Una solución híbrida</div>', unsafe_allow_html=True)
st.markdown("""
<div class="cuerpo-texto">
    La ciencia no sugiere reemplazar a los psicólogos, sino integrar la IA en un <b>modelo de cuidado escalonado</b>[cite: 38]. Los chatbots actúan como primera línea para síntomas leves, mientras los profesionales humanos supervisan los casos complejos[cite: 40, 41].
</div>
<div class="subtitulo">Conclusión</div>
<div class="cuerpo-texto">
    El impacto de la IA generativa es, hasta ahora, significativamente positivo y representa un cambio de paradigma[cite: 43, 44]. Sin embargo, debe avanzar bajo un marco de responsabilidad ética, priorizando el bienestar del individuo sobre la eficiencia[cite: 45].
</div>
""", unsafe_allow_html=True)

# --- SECCIÓN DE REFERENCIAS INTERACTIVAS [cite: 46, 47, 48] ---
st.markdown("---")
st.markdown('<div class="subtitulo">Referencias</div>', unsafe_allow_html=True)

def crear_referencia(cita, resumen):
    with st.popover(cita):
        st.markdown(f"**Resumen:** {resumen}")
        # El componente popover de Streamlit ya incluye una "X" o se cierra al hacer clic fuera/re-click.

# Lista de referencias según el documento [cite: 49-91]
referencias_data = [
    (
        "Camones, V., Cisneros, P. y Quevedo, D. (2025). Del miedo a la confianza: Realidad Virtual y ChatGPT-4 en el tratamiento de la ansiedad social.",
        "El estudio aborda la integración de RV con ChatGPT-4 para simulaciones interactivas. Demostró una reducción del 20% en niveles de ansiedad social tras tres semanas de uso. [cite: 50, 52]"
    ),
    (
        "Farzan, M., Ebrahimi, H., Pourali, M. y Sabeti, F. (2024). Artificial Intelligence-Powered Cognitive Behavioral Therapy Chatbots, a Systematic Review.",
        "Revisión sistemática de chatbots como Woebot y Wysa. Indica mejoras significativas en síntomas de depresión y ansiedad, destacando su capacidad de vinculación. [cite: 55, 57]"
    ),
    (
        "Ferreira, D. S., et al. (2024). Uso do chatbot no enfrentamento da ansiedade: uma revisão integrativa.",
        "Explora cómo los chatbots ofrecen soporte emocional 24/7 y ejercicios prácticos, mejorando la autoconciencia emocional y democratizando el acceso. [cite: 59, 61]"
    ),
    (
        "Heinz, M. V., et al. (2025). Randomized Trial of a Generative AI Chatbot for Mental Health Treatment.",
        "Ensayo controlado con Therabot en 210 adultos. Reveló reducciones moderadas en síntomas de ansiedad y depresión con alta retención de usuarios. [cite: 63, 66]"
    ),
    (
        "Joshi, A. C., Ghogare, A. S. y Madavi, P. B. (2025). Systematic review of artificial intelligence enabled psychological interventions for depression and anxiety.",
        "Examina el papel de la IA para superar barreras de costo y estigma, subrayando que su éxito depende de algoritmos avanzados para interacciones seguras. [cite: 69, 72]"
    ),
    (
        "Klos, M. C., et al. (2021). Artificial Intelligence-Based Chatbot for Anxiety and Depression in University Students.",
        "Estudio con el chatbot Tess en estudiantes argentinos. Mostró una disminución estadísticamente significativa de la ansiedad intragrupo. [cite: 74, 76]"
    ),
    (
        "Lima Neto, J. G. F. y Castro, A. F. C. (2025). Eficácia de programas de inteligência artificial com aplicação de chatbots no auxílio ao cuidado a saúde mental.",
        "Analiza herramientas como 'Tess' y 'TeO', concluyendo que son eficaces para promover el bienestar, aunque deben complementar el cuidado tradicional. [cite: 78, 82, 83]"
    ),
    (
        "Manole, A., et al. (2024). An Exploratory Investigation of Chatbot Applications in Anxiety Management.",
        "Investiga la transición de sistemas rígidos a LLMs, destacando el procesamiento de lenguaje natural para identificar patrones emocionales. [cite: 84, 87]"
    ),
    (
        "Pavlopoulos, A., Rachiotis, T. y Maglogiannis, I. (2024). An Overview of Tools and Technologies for Anxiety and Depression Management Using AI.",
        "Revisión de los últimos cinco años sobre wearables y LLMs, sugiriendo que complementan tratamientos tradicionales y reducen la carga profesional. [cite: 88, 91]"
    )
]

for cita, resumen in referencias_data:
    crear_referencia(cita, resumen)

st.markdown("<br><br>", unsafe_allow_html=True)
