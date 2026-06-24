from agency.agents import (
    researcher,
    writer,
    coder,
    reviewer,
    niche_researcher,
    outliner,
    editor,
    cover_designer,
    kdp_metadata,
)

PIPELINES = {
    "investigacion_y_redaccion": [researcher, writer, reviewer],
    "codigo": [researcher, coder, reviewer],
    "redaccion_simple": [writer, reviewer],
    "libro_kdp": [
        niche_researcher,
        outliner,
        writer,
        editor,
        cover_designer,
        kdp_metadata,
    ],
}


def run_pipeline(pipeline_name: str, task: str) -> dict:
    """Ejecuta una secuencia de agentes pasando el resultado de uno como contexto del siguiente."""
    if pipeline_name not in PIPELINES:
        raise ValueError(
            f"Pipeline desconocido: {pipeline_name}. Opciones: {list(PIPELINES)}"
        )

    agents = PIPELINES[pipeline_name]
    history = {}
    context = ""

    for agent in agents:
        output = agent.run(task, context=context)
        history[agent.name] = output
        context = f"{context}\n\n[{agent.name}]:\n{output}".strip()

    return history


def run_task(task: str, pipeline_name: str = "investigacion_y_redaccion") -> str:
    history = run_pipeline(pipeline_name, task)
    last_agent = PIPELINES[pipeline_name][-1].name
    return history[last_agent]
