import re
import sys
from pathlib import Path

from agency.orchestrator import run_pipeline, PIPELINES


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:60] or "libro"


def run_batch(ideas_file: str, pipeline_name: str, output_dir: str) -> None:
    ideas = [
        line.strip()
        for line in Path(ideas_file).read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

    out_root = Path(output_dir)
    out_root.mkdir(parents=True, exist_ok=True)

    for idea in ideas:
        slug = slugify(idea)
        book_dir = out_root / slug
        book_dir.mkdir(parents=True, exist_ok=True)
        print(f"\n=== Procesando: {idea} ===")

        history = run_pipeline(pipeline_name, idea)
        for agent_name, output in history.items():
            (book_dir / f"{agent_name}.md").write_text(output, encoding="utf-8")

        print(f"Resultados guardados en {book_dir}")


def main():
    if len(sys.argv) < 2:
        print("Uso: python batch.py <archivo_ideas.txt> [pipeline] [output_dir]")
        print(f"Pipelines disponibles: {list(PIPELINES)}")
        sys.exit(1)

    ideas_file = sys.argv[1]
    pipeline_name = sys.argv[2] if len(sys.argv) > 2 else "libro_kdp"
    output_dir = sys.argv[3] if len(sys.argv) > 3 else "output"

    run_batch(ideas_file, pipeline_name, output_dir)


if __name__ == "__main__":
    main()
