# detector-automatico

Agencia de agentes de IA en Python: un orquestador reparte tareas entre agentes
especializados (investigador, redactor, programador, revisor), encadenando
el resultado de cada uno como contexto del siguiente.

## Uso

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=tu_api_key
python main.py "Escribe un resumen sobre energias renovables" investigacion_y_redaccion
```

Pipelines disponibles en `agency/orchestrator.py`:
- `investigacion_y_redaccion`: researcher -> writer -> reviewer
- `codigo`: researcher -> coder -> reviewer
- `redaccion_simple`: writer -> reviewer
- `libro_kdp`: niche_researcher -> competitor_analyst -> outliner -> writer -> editor -> cover_designer -> kdp_metadata

El pipeline `libro_kdp` cubre el flujo de una editorial en Amazon KDP: nicho y
keywords, analisis de competencia y precios, estructura del libro, manuscrito,
edicion, prompt de portada y ficha de venta optimizada (titulo, descripcion,
keywords, categorias, precio).

```bash
python main.py "Libro de no ficcion sobre habitos de productividad para freelancers" libro_kdp
```

## Procesar varios libros en lote

Crea un archivo de texto con una idea de libro por linea (ver
`ideas_ejemplo.txt`) y ejecuta:

```bash
python batch.py ideas_ejemplo.txt libro_kdp output
```

Esto genera, por cada idea, una carpeta dentro de `output/` con un archivo
`.md` por cada agente del pipeline (investigacion, competencia, indice,
manuscrito, edicion, portada y ficha de KDP).

Para agregar un agente nuevo, define un `Agent` en `agency/agents/__init__.py`
con su `role_prompt`, y agrégalo a un pipeline en `agency/orchestrator.py`.