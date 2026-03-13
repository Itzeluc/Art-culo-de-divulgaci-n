import streamlit as st

# Configuración de la página
st.set_page_config(page_title="IA y Ansiedad - Artículo Completo", layout="centered")

# CSS para forzar Times New Roman, fondo blanco y eliminar textos de sistema
st.markdown("""
    <style>
    /* Forzar fuente en toda la aplicación */
    html, body, [class*="css"], .stApp, p, div, span, h1, h2, h3, h4, h5, h6, li, button {
        font-family: 'Times New Roman', Times, serif !important;
        background-color: #ffffff !important;
        color: #000000 !important;
    }

    /* Ocultar iconos y etiquetas automáticas de Streamlit para evitar "expand_more" */
    [data-testid="stPopover"] svg, 
    [data-testid="stWidgetLabel"] {
        display: none !important;
    }

    /* Estilo del título principal */
    .titulo-principal {
        font-size: 42px !important;
        font-weight: bold;
        text-align: center;
        margin: 30px 0;
        line-height: 1.2;
    }

    /* Frase motivadora alineada a la derecha */
    .frase-motivadora {
        font-style: italic !important;
        text-align: right;
        font-size: 20px !important;
        margin: 40px 0;
        color: #1a1a1a;
    }

    /* Cuerpo del texto con diseño elegante y tamaño mediano */
    .cuerpo-texto {
        font-size: 20px !important;
        text-align: justify;
        line-height: 1.7;
        margin-bottom: 25px;
    }

    /* Estilo de los subtítulos */
    .subtitulo {
        font-size: 26px !important;
        font-weight: bold;
        margin-top: 35px;
        margin-bottom: 15px;
    }

    /* Formato para las referencias bibliográficas */
    .referencia-apa {
        font-size: 17px !important;
        margin-top: 25px;
        margin-bottom: 5px;
        line-height: 1.4;
    }

    /* Estilo del botón "Ver resumen" para que sea elegante y sin iconos */
    [data-testid="stPopover"] > button {
        border: 1px solid #000000 !important;
        background-color: #ffffff !important;
        font-family: 'Times New Roman', Times, serif !important;
        font-size: 15px !important;
        padding: 5px 15px !important;
        border-radius: 0px !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Contenido interno del cuadro de resumen */
    [data-testid="stPopoverBody"] {
        border: 2px solid #000000 !important;
        padding: 20px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- INICIO DEL CONTENIDO DEL ARTÍCULO ---

# Título [cite: 3, 4]
st.markdown('<div class="titulo-principal">¿Un psicólogo en tu bolsillo? Luces y sombras de la IA generativa frente a la ansiedad</div>', unsafe_allow_html=True)

# Frase Motivadora [cite: 5, 6, 7]
st.markdown('<div class="frase-motivadora">Tu mente es el territorio y la innovación la herramienta; el verdadero poder de cambio siempre reside en la valentía de conocerte a ti mismo.</div>', unsafe_allow_html=True)

# Introducción [cite: 11, 12, 13, 14, 15]
st.markdown("""
<div class="cuerpo-texto">
    En la última década, la ansiedad ha dejado de ser una preocupación individual para convertirse en un desafío de salud pública global. 
    Se ha consolidado como una de las principales causas de discapacidad y pérdida de productividad en la población activa. 
    A pesar de que existen tratamientos efectivos, factores como el alto costo de la terapia, la falta de profesionales en zonas rurales y el estigma social impiden que muchas personas reciban ayuda oportuna. 
    En este escenario, la Inteligencia Artificial (IA) generativa surge como una herramienta disruptiva que promete democratizar el cuidado de la salud mental. 
    Pero, ¿qué tan sólida es esta promesa y cuáles son sus riesgos?
</div>
""", unsafe_allow_html=True)

# El potencial [cite: 16, 17, 18]
st.markdown('<div class="subtitulo">El potencial: ¿Por qué la IA funciona para la ansiedad?</div>', unsafe_allow_html=True)
st.markdown("""
<div class="cuerpo-texto">
    La mayoría de los chatbots actuales no operan al azar; su sustento teórico es la Terapia Cognitivo-Conductual (TCC). 
    Esta terapia se centra en identificar y reestructurar patrones de pensamiento catastróficos, algo que, por su naturaleza protocolizada, es ideal para ser traducido a algoritmos de respuesta.
</div>
""", unsafe_allow_html=True)

# Las ventajas [cite: 19, 20, 21, 22, 23, 24, 25, 26]
st.markdown('<div class="subtitulo">Las ventajas de un "entrenador de bolsillo"</div>', unsafe_allow_html=True)
st.markdown("""
<div class="cuerpo-texto">
    El uso de estos agentes conversacionales ofrece beneficios que el sistema tradicional difícilmente puede igualar: <br><br>
    <b>Disponibilidad 24/7 e inmediatez:</b> El apoyo está presente en el momento exacto de una crisis de pánico o estrés, sin importar el horario. <br>
    <b>Anonimato y reducción del estigma:</b> Al interactuar con una máquina, muchos pacientes se sienten libres del juicio social, lo que facilita una mayor apertura emocional. <br>
    <b>Alianza terapéutica digital:</b> Sorprendentemente, los estudios indican que los usuarios pueden desarrollar un vínculo de confianza con la IA, sintiéndose validados por sus respuestas empáticas. <br>
    <b>Personalización profunda:</b> A diferencia de los chatbots antiguos que eran rígidos, la IA generativa (como GPT-4) adapta su tono, metáforas y sugerencias a la historia específica del usuario. <br><br>
    Incluso se están explorando fronteras como la Realidad Virtual (RV) asistida por IA. Esta combinación permite que personas con ansiedad social practiquen interacciones en escenarios simulados y seguros, reduciendo la fobia social hasta en un 20% en periodos breves.
</div>
""", unsafe_allow_html=True)

# Riesgos [cite: 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
st.markdown('<div class="subtitulo">La otra cara de la moneda: Riesgos y desafíos éticos</div>', unsafe_allow_html=True)
st.markdown("""
<div class="cuerpo-texto">
    No todo es optimismo. La implementación de la IA en la salud mental plantea dilemas profundos que la comunidad científica analiza con cautela. <br><br>
    <b>El peligro de las "alucinaciones" y la seguridad clínica:</b> Uno de los mayores retos técnicos son las "alucinaciones" de la IA, donde el sistema genera información que parece coherente pero es incorrecta o peligrosa. En un contexto de salud mental, una instrucción errónea podría tener consecuencias graves. Además, existe el riesgo de que la IA no detecte señales sutiles de ideación suicida o autolesión, lo que hace imperativo contar con protocolos de derivación inmediata a profesionales humanos. <br><br>
    <b>Privacidad y persistencia:</b> La confidencialidad es la piedra angular de la psicología. El uso de datos sensibles por parte de empresas tecnológicas genera preocupaciones legítimas sobre la protección de la privacidad. Por otro lado, la evidencia científica actual es limitada en el tiempo. Aunque se observa una reducción de síntomas en las primeras semanas, aún no sabemos si estos efectos perduran una vez que el "efecto de novedad" tecnológica desaparece.
</div>
""", unsafe_allow_html=True)

# Modelo Híbrido [cite: 37, 38, 39, 40, 41]
st.markdown('<div class="subtitulo">El Modelo de Cuidado Escalonado: Una solución híbrida</div>', unsafe_allow_html=True)
st.markdown("""
<div class="cuerpo-texto">
    La ciencia actual no sugiere que la IA deba reemplazar a los psicólogos, sino que debe integrarse en un modelo de cuidado escalonado. En este esquema: <br><br>
    <b>Primera línea:</b> Los chatbots actúan como apoyo preventivo y de autogestión para personas con síntomas leves o moderados. <br>
    <b>Segunda línea:</b> Los profesionales humanos se concentran en los casos de mayor complejidad clínica y supervisan el uso de la tecnología.
</div>
""", unsafe_allow_html=True)

# Conclusión [cite: 42, 43, 44, 45]
st.markdown('<div class="subtitulo">Conclusión</div>', unsafe_allow_html=True)
st.markdown("""
<div class="cuerpo-texto">
    El impacto de la IA generativa en la sintomatología de la ansiedad es, hasta ahora, significativamente positivo. Representa un cambio de paradigma que ofrece una mano amiga a quienes históricamente han estado excluidos del sistema de salud. Sin embargo, para que esta herramienta sea realmente efectiva a largo plazo, debe avanzar bajo un marco de responsabilidad ética, garantizando que el bienestar del individuo siempre esté por encima de la eficiencia tecnológica.
</div>
""", unsafe_allow_html=True)

# --- SECCIÓN DE REFERENCIAS --- [cite: 48]
st.markdown("---")
st.markdown('<div class="subtitulo">Referencias</div>', unsafe_allow_html=True)

# Lista de referencias y resúmenes extraídos íntegramente del documento
referencias_data = [
    ("Camones, V., Cisneros, P. y Quevedo, D. (2025). Del miedo a la confianza: Realidad Virtual y ChatGPT-4 en el tratamiento de la ansiedad social.", 
     "El estudio aborda el impacto de los trastornos de ansiedad social en la calidad de vida y propone una solución tecnológica innovadora que integra la Realidad Virtual (RV) con la API de ChatGPT-4. El objetivo principal es ofrecer un sistema de simulaciones interactivas donde personas con diagnóstico clínico de ansiedad social puedan practicar habilidades en entornos controlados. Tras una intervención de tres semanas con 20 participantes, demostró una reducción promedio del 20% en los niveles de ansiedad."),
    
    ("Farzan, M., Ebrahimi, H., Pourali, M. y Sabeti, F. (2024). Artificial Intelligence-Powered Cognitive Behavioral Therapy Chatbots, a Systematic Review.", 
     "Esta revisión sistemática identifica las características distintivas y la eficacia terapéutica de chatbots basados en la Terapia Cognitivo-Conductual (TCC-IA), como Woebot, Wysa y Youper. Analiza diez investigaciones para determinar cómo impactan en los síntomas de depresión y ansiedad, destacando mejoras significativas y estableciendo estas herramientas como prometedoras para cerrar la brecha en el acceso a la atención psicológica."),
    
    ("Ferreira, D. S., et al. (2024). Uso do chatbot no enfrentamento da ansiedade: uma revisão integrativa.", 
     "Esta revisión integrativa explora cómo los chatbots auxilian en el manejo de la ansiedad, sintetizando hallazgos sobre soporte emocional 24/7 y ejercicios prácticos. Indica que son eficaces para reducir síntomas y mejorar la autoconciencia emocional, democratizando el acceso al apoyo en salud mental en contextos donde la atención presencial es limitada."),
    
    ("Heinz, M. V., et al. (2025). Randomized Trial of a Generative AI Chatbot for Mental Health Treatment.", 
     "Ensayo controlado aleatorio diseñado para evaluar Therabot, un chatbot de IA generativa ajustado por expertos. En un estudio con 210 adultos, reveló reducciones significativas en síntomas de depresión y ansiedad con un tamaño de efecto moderado tras cuatro semanas de uso, registrando altos niveles de compromiso."),
    
    ("Joshi, A. C., Ghogare, A. S. y Madavi, P. B. (2025). Systematic review of artificial intelligence enabled psychological interventions for depression and anxiety.", 
     "Revisión sistemática sobre el papel de los chatbots de IA para abordar la depresión y ansiedad. Destaca cómo la IA supera barreras como el alto costo y el estigma social. Demuestra que estas tecnologías facilitan la detección temprana y ofrecen apoyo personalizado, supeditado a la integración de algoritmos avanzados."),
    
    ("Klos, M. C., et al. (2021). Artificial Intelligence-Based Chatbot for Anxiety and Depression in University Students.", 
     "Ensayo piloto para evaluar el chatbot Tess en estudiantes universitarios. Aunque no hubo diferencias generales masivas frente al grupo de control, el grupo de Tess mostró una disminución estadísticamente significativa en sus propios niveles de ansiedad, sugiriendo que es una herramienta aceptada en la población estudiantil."),
    
    ("Lima Neto, J. G. F. y Castro, A. F. C. (2025). Eficácia de programas de inteligência artificial com aplicação de chatbots no auxílio ao cuidado a saúde mental.", 
     "Evalúa la efectividad de chatbots como Tess, TeO y AirHeart mediante una revisión sistemática. Concluye que son eficaces para reducir síntomas psicológicos y promover el bienestar, subrayando su capacidad para complementar el cuidado tradicional."),
    
    ("Manole, A., et al. (2024). An Exploratory Investigation of Chatbot Applications in Anxiety Management.", 
     "Investigación sobre cómo los chatbots LLM transforman el manejo de la ansiedad mediante intervenciones personalizadas. Destaca que la identificación de patrones emocionales mediante procesamiento de lenguaje natural reduce significativamente las barreras de costo y disponibilidad."),
    
    ("Pavlopoulos, A., Rachiotis, T. y Maglogiannis, I. (2024). An Overview of Tools and Technologies for Anxiety and Depression Management Using AI.", 
     "Revisión de la literatura de los últimos cinco años sobre IA en salud mental. Categoriza herramientas como wearables y LLMs, concluyendo que muestran una promesa significativa para complementar tratamientos tradicionales y reducir la carga de trabajo de los profesionales.")
]

# Renderizado de referencias con botón de resumen limpio [cite: 46, 47]
for apa, resumen in referencias_data:
    st.markdown(f'<div class="referencia-apa">{apa}</div>', unsafe_allow_html=True)
    with st.popover("Ver resumen"):
        st.markdown(f'<div style="font-family: \'Times New Roman\', serif; font-size: 18px; text-align: justify;">{resumen}</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
