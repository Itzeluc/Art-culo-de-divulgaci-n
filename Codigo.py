import streamlit as st

# Configuración de la página
st.set_page_config(page_title="IA y Ansiedad - Artículo Completo", layout="centered")

# Inyección de CSS para diseño exacto
st.markdown("""
    <style>
    html, body, [class*="css"], .stApp {
        font-family: "Times New Roman", Times, serif !important;
        background-color: #ffffff;
        color: #000000;
    }
    .titulo-principal {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        margin: 30px 0;
        line-height: 1.2;
    }
    .frase-motivadora {
        font-style: italic;
        text-align: right;
        font-size: 19px;
        margin: 40px 0;
        color: #1a1a1a;
    }
    .cuerpo-texto {
        font-size: 19px;
        text-align: justify;
        line-height: 1.7;
        margin-bottom: 20px;
    }
    .subtitulo {
        font-size: 24px;
        font-weight: bold;
        margin-top: 35px;
        margin-bottom: 15px;
    }
    /* Estilo para los botones de referencia */
    .stButton>button {
        border: none;
        background: none;
        padding: 0;
        color: #0000EE;
        text-decoration: underline;
        font-family: "Times New Roman", Times, serif;
        font-size: 17px;
        text-align: left;
    }
    </style>
    """, unsafe_allow_html=True)

# --- INICIO DEL CONTENIDO ---

# Título [cite: 4]
st.markdown('<div class="titulo-principal">¿Un psicólogo en tu bolsillo? Luces y sombras de la IA generativa frente a la ansiedad</div>', unsafe_allow_html=True)

# Frase Motivadora [cite: 6, 7]
st.markdown('<div class="frase-motivadora">Tu mente es el territorio y la innovación la herramienta; el verdadero poder de cambio siempre reside en la valentía de conocerte a ti mismo.</div>', unsafe_allow_html=True)

# Introducción [cite: 11-15]
st.markdown("""
<div class="cuerpo-texto">
    En la última década, la ansiedad ha dejado de ser una preocupación individual para convertirse en un desafío de salud pública global. 
    Se ha consolidado como una de las principales causas de discapacidad y pérdida de productividad en la población activa. 
    A pesar de que existen tratamientos efectivos, factores como el alto costo de la terapia, la falta de profesionales en zonas rurales y el estigma social impiden que muchas personas reciban ayuda oportuna. 
    En este escenario, la Inteligencia Artificial (IA) generativa surge como una herramienta disruptiva que promete democratizar el cuidado de la salud mental. 
    Pero, ¿qué tan sólida es esta promesa y cuáles son sus riesgos?
</div>
""", unsafe_allow_html=True)

# El Potencial [cite: 16-18]
st.markdown('<div class="subtitulo">El potencial: ¿Por qué la IA funciona para la ansiedad?</div>', unsafe_allow_html=True)
st.markdown("""
<div class="cuerpo-texto">
    La mayoría de los chatbots actuales no operan al azar; su sustento teórico es la Terapia Cognitivo-Conductual (TCC). 
    Esta terapia se centra en identificar y reestructurar patrones de pensamiento catastróficos, algo que, por su naturaleza protocolizada, es ideal para ser traducido a algoritmos de respuesta.
</div>
""", unsafe_allow_html=True)

# Ventajas [cite: 19-26]
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

# Riesgos [cite: 27-36]
st.markdown('<div class="subtitulo">La otra cara de la moneda: Riesgos y desafíos éticos</div>', unsafe_allow_html=True)
st.markdown("""
<div class="cuerpo-texto">
    No todo es optimismo. La implementación de la IA en la salud mental plantea dilemas profundos que la comunidad científica analiza con cautela. <br><br>
    <b>El peligro de las "alucinaciones" y la seguridad clínica:</b> Uno de los mayores retos técnicos son las "alucinaciones" de la IA, donde el sistema genera información que parece coherente pero es incorrecta o peligrosa. En un contexto de salud mental, una instrucción errónea podría tener consecuencias graves. Además, existe el riesgo de que la IA no detecte señales sutiles de ideación suicida o autolesión, lo que hace imperativo contar con protocolos de derivación inmediata a profesionales humanos. <br><br>
    <b>Privacidad y persistencia:</b> La confidencialidad es la piedra angular de la psicología. El uso de datos sensibles por parte de empresas tecnológicas genera preocupaciones legítimas sobre la protección de la privacidad. Por otro lado, la evidencia científica actual es limitada en el tiempo. Aunque se observa una reducción de síntomas en las primeras semanas, aún no sabemos si estos efectos perduran una vez que el "efecto de novedad" tecnológica desaparece.
</div>
""", unsafe_allow_html=True)

# Modelo Escalonado [cite: 37-41]
st.markdown('<div class="subtitulo">El Modelo de Cuidado Escalonado: Una solución híbrida</div>', unsafe_allow_html=True)
st.markdown("""
<div class="cuerpo-texto">
    La ciencia actual no sugiere que la IA deba reemplazar a los psicólogos, sino que debe integrarse en un modelo de cuidado escalonado. En este esquema: <br><br>
    <b>Primera línea:</b> Los chatbots actúan como apoyo preventivo y de autogestión para personas con síntomas leves o moderados. <br>
    <b>Segunda línea:</b> Los profesionales humanos se concentran en los casos de mayor complejidad clínica y supervisan el uso de la tecnología.
</div>
""", unsafe_allow_html=True)

# Conclusión [cite: 42-45]
st.markdown('<div class="subtitulo">Conclusión</div>', unsafe_allow_html=True)
st.markdown("""
<div class="cuerpo-texto">
    El impacto de la IA generativa en la sintomatología de la ansiedad es, hasta ahora, significativamente positivo. Representa un cambio de paradigma que ofrece una mano amiga a quienes históricamente han estado excluidos del sistema de salud. Sin embargo, para que esta herramienta sea realmente efectiva a largo plazo, debe avanzar bajo un marco de responsabilidad ética, garantizando que el bienestar del individuo siempre esté por encima de la eficiencia tecnológica.
</div>
""", unsafe_allow_html=True)

# Referencias Interactivas [cite: 46-91]
st.markdown("---")
st.markdown('<div class="subtitulo">Referencias</div>', unsafe_allow_html=True)

# Función para generar el popover con el resumen completo del Word
def ref_popover(cita, resumen):
    with st.popover(cita):
        st.markdown(f"<div style='font-family: \"Times New Roman\", serif;'>{resumen}</div>", unsafe_allow_html=True)

# Datos extraídos íntegramente del documento
referencias = [
    ("Camones, V., Cisneros, P. y Quevedo, D. (2025). Del miedo a la confianza: Realidad Virtual y ChatGPT-4 en el tratamiento de la ansiedad social.", 
     "El estudio aborda el impacto de los trastornos de ansiedad social en la calidad de vida y propone una solución tecnológica innovadora que integra la Realidad Virtual (RV) con la API de ChatGPT-4. El objetivo principal es ofrecer un sistema de simulaciones interactivas donde personas con diagnóstico clínico de ansiedad social puedan practicar habilidades en entornos controlados, como reuniones sociales y entrevistas laborales. Tras una intervención de tres semanas con 20 participantes, la investigación demostró una reducción promedio del 20% en los niveles de ansiedad, validada mediante las escalas LSAS y SPIN. Además, el sistema mostró una alta fiabilidad técnica con un 90.58% de éxito en las interacciones y una recepción positiva en términos de usabilidad y calidad de interfaz."),
    
    ("Farzan, M., Ebrahimi, H., Pourali, M. y Sabeti, F. (2024). Artificial Intelligence-Powered Cognitive Behavioral Therapy Chatbots, a Systematic Review.", 
     "Esta revisión sistemática tiene como objetivo identificar las características distintivas y la eficacia terapéutica de los chatbots de inteligencia artificial basados en la Terapia Cognitivo-Conductual (TCC-IA), como Woebot, Wysa y Youper. El estudio analiza diez investigaciones empíricas publicadas entre 2017 y 2024 para determinar cómo estas herramientas impactan en los síntomas de depresión, ansiedad y otros trastornos de salud mental, además de evaluar el nivel de compromiso y satisfacción del usuario. Los resultados indican mejoras significativas en la reducción de síntomas, destacando a Woebot por su alta capacidad de vinculación y a Wysa por su eficacia en contextos de depresión severa y dolor crónico, estableciendo que estas herramientas son intervenciones digitales prometedoras para cerrar la brecha en el acceso a la atención psicológica."),
    
    ("Ferreira, D. S., et al. (2024). Uso do chatbot no enfrentamento da ansiedade: uma revisão integrativa.", 
     "Esta investigación consiste en una revisión integrativa de la literatura que explora cómo el uso de chatbots puede auxiliar en el manejo y enfrentamiento de la ansiedad. El estudio sintetiza hallazgos de diversas publicaciones científicas para identificar las principales funcionalidades de estos agentes conversacionales, como el soporte emocional 24/7 y la aplicación de ejercicios prácticos. Los resultados indican que los chatbots son herramientas eficaces para reducir los síntomas de ansiedad y mejorar la autoconciencia emocional de los usuarios, destacándose como una alternativa tecnológica viable para democratizar el acceso al apoyo en salud mental, especialmente en contextos donde la atención presencial es limitada o costosa."),
    
    ("Heinz, M. V., et al. (2025). Randomized Trial of a Generative AI Chatbot for Mental Health Treatment.", 
     "Este estudio presenta los resultados de un ensayo controlado aleatorio (RCT) a nivel nacional diseñado para evaluar la eficacia de Therabot, un chatbot de inteligencia artificial generativa (Gen-AI) ajustado por expertos para el tratamiento de la salud mental. La investigación se centró en 210 adultos con síntomas clínicamente significativos de trastorno depresivo mayor, trastorno de ansiedad generalizada o riesgo elevado de trastornos de la conducta alimentaria. Durante una intervención de cuatro semanas, los investigadores compararon a Therabot frente a un grupo de control en lista de espera. Los hallazgos principales revelaron que el uso del chatbot generó reducciones significativas y con un tamaño de efecto moderado en los síntomas de depresión, ansiedad y trastornos alimentarios, además de registrar niveles de compromiso y retención del usuario excepcionalmente altos en comparación con otras herramientas digitales."),
    
    ("Joshi, A. C., Ghogare, A. S. y Madavi, P. B. (2025). Systematic review of artificial intelligence enabled psychological interventions for depression and anxiety.", 
     "Esta revisión sistemática examina el papel de los chatbots impulsados por inteligencia artificial como herramientas de intervención psicológica para abordar la depresión y la ansiedad a nivel global. El estudio destaca cómo la IA ha emergido para superar barreras tradicionales en la salud mental, tales como el alto costo de los tratamientos, las limitaciones geográficas y el estigma social. Al analizar diversas plataformas conversacionales, la investigación demuestra que estas tecnologías facilitan la detección temprana y ofrecen apoyo terapéutico personalizado. Los hallazgos sugeridos indican que, aunque estas herramientas son altamente efectivas para reducir los síntomas y mejorar la accesibilidad, su éxito depende de la integración de algoritmos avanzados que permitan una interacción más humana y segura."),
    
    ("Klos, M. C., et al. (2021). Artificial Intelligence-Based Chatbot for Anxiety and Depression in University Students.", 
     "Este estudio consistió en un ensayo controlado aleatorio piloto diseñado para evaluar la viabilidad, aceptabilidad y el impacto potencial de un chatbot de inteligencia artificial llamado Tess en la salud mental de estudiantes universitarios argentinos. La investigación comparó el uso del chatbot frente a un grupo de control que utilizó un libro de psicoeducación sobre la depresión durante un periodo de ocho semanas. Aunque no se encontraron diferencias significativas entre ambos grupos en cuanto a la reducción general de síntomas de depresión y ansiedad, el grupo que utilizó a Tess mostró una disminución estadísticamente significativa en sus niveles de ansiedad dentro de su propio grupo. Los resultados sugieren que el chatbot es una herramienta usable y aceptada por la población estudiantil, ofreciendo una vía prometedora para expandir el acceso a cuidados psicológicos en América Latina."),
    
    ("Lima Neto, J. G. F. y Castro, A. F. C. (2025). Eficácia de programas de inteligencia artificial com aplicação de chatbots no auxílio ao cuidado a saúde mental.", 
     "La investigación analiza cómo los trastornos de salud mental, especialmente la ansiedad y la depresión, afectan de manera global la calidad de vida y el desempeño laboral. Ante el aumento en el uso de dispositivos móviles, el estudio evalúa la efectividad de los chatbots basados en Inteligencia Artificial (IA) como herramientas de apoyo emocional. Mediante una revisión sistemática, se examinaron seis intervenciones tecnológicas específicas (\"Tess\", \"XiaoE y Xiaoai\", \"XiaoNan\", \"TeO\", \"Dh\" y \"AirHeart\"), concluyendo que estas herramientas son eficaces para reducir síntomas psicológicos y promover el bienestar. No obstante, el estudio subraya que la relevancia de estas tecnologías reside en su capacidad para complementar el cuidado tradicional, aunque requieren más investigación para validar su impacto en poblaciones diversas."),
    
    ("Manole, A., et al. (2024). An Exploratory Investigation of Chatbot Applications in Anxiety Management.", 
     "Esta investigación realiza una exploración exhaustiva sobre cómo las aplicaciones de chatbots, impulsadas por inteligencia artificial avanzada, están transformando el manejo de la ansiedad a través de intervenciones personalizadas. El estudio examina la evolución de estos agentes conversacionales, desde sistemas basados en reglas simples hasta los actuales modelos de lenguaje de gran tamaño (LLM), analizando su capacidad para ofrecer soporte terapéutico accesible y adaptativo. Los autores destacan que, mediante la integración de técnicas como el procesamiento de lenguaje natural y el análisis de sentimientos, los chatbots pueden identificar patrones emocionales específicos en los usuarios, proporcionando herramientas de autoayuda que reducen significativamente las barreras tradicionales de costo, estigma y disponibilidad en la atención de la salud mental."),
    
    ("Pavlopoulos, A., Rachiotis, T. y Maglogiannis, I. (2024). An Overview of Tools and Technologies for Anxiety and Depression Management Using AI.", 
     "Este estudio consiste en una revisión exhaustiva de la literatura académica de los últimos cinco años para evaluar la efectividad y utilidad de las aplicaciones de Inteligencia Artificial (IA) en el manejo de la ansiedad y la depresión. El trabajo identifica y categoriza diversas herramientas como chatbots terapéuticos, aplicaciones móviles, dispositivos vestibles (wearables) y modelos de lenguaje de gran tamaño (LLMs), analizando sus beneficios en términos de accesibilidad y personalización del tratamiento. Los hallazgos principales sugieren que estas tecnologías muestran una promesa significativa para complementar los tratamientos tradicionales al ofrecer apoyo inmediato y reducir la carga de trabajo de los profesionales de la salud mental.")
]

for cita, resumen in referencias:
    ref_popover(cita, resumen)

st.markdown("<br><br>", unsafe_allow_html=True)
