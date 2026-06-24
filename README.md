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

Para agregar un agente nuevo, define un `Agent` en `agency/agents/__init__.py`
con su `role_prompt`, y agrégalo a un pipeline en `agency/orchestrator.py`.