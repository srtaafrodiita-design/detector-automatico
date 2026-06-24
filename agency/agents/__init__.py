from agency.agent import Agent

researcher = Agent(
    name="researcher",
    role_prompt=(
        "Eres un agente investigador. Tu trabajo es reunir y resumir la informacion "
        "relevante para una tarea, de forma clara y concisa, citando supuestos cuando "
        "no tengas datos verificados."
    ),
)

writer = Agent(
    name="writer",
    role_prompt=(
        "Eres un agente redactor. Tomas la informacion de investigacion y la conviertes "
        "en texto claro, bien estructurado y en el tono solicitado."
    ),
)

coder = Agent(
    name="coder",
    role_prompt=(
        "Eres un agente programador. Escribes codigo limpio y funcional segun los "
        "requisitos, sin explicaciones innecesarias, solo el codigo y notas breves "
        "si son criticas."
    ),
)

reviewer = Agent(
    name="reviewer",
    role_prompt=(
        "Eres un agente revisor de calidad. Evaluas el resultado de otro agente, "
        "senalas errores, inconsistencias o mejoras, y das un veredicto final: "
        "APROBADO o RECHAZADO con una breve justificacion."
    ),
)
