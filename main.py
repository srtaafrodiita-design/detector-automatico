import sys

from agency.orchestrator import run_pipeline, PIPELINES


def main():
    if len(sys.argv) < 2:
        print(f"Uso: python main.py <tarea> [pipeline]")
        print(f"Pipelines disponibles: {list(PIPELINES)}")
        sys.exit(1)

    task = sys.argv[1]
    pipeline_name = sys.argv[2] if len(sys.argv) > 2 else "investigacion_y_redaccion"

    history = run_pipeline(pipeline_name, task)
    for agent_name, output in history.items():
        print(f"\n=== {agent_name} ===\n{output}")


if __name__ == "__main__":
    main()
