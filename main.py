import argparse
import json
from pathlib import Path


def load_template(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_snippets(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def build_prompt(template: str, language: str, code: str) -> str:
    return (
        template.replace("{{LANGUAGE}}", language).replace("{{CODE_SNIPPET}}", code)
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build a final prompt for the Code Review Assistant challenge."
    )
    parser.add_argument(
        "--snippet",
        default="simple_python",
        help="Snippet key from sample_snippets.json",
    )
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent
    template_path = project_root / "code_review_assistant_prompt.md"
    snippets_path = project_root / "sample_snippets.json"

    template = load_template(template_path)
    snippets = load_snippets(snippets_path)

    if args.snippet not in snippets:
        available = ", ".join(sorted(snippets.keys()))
        raise SystemExit(
            f"Unknown snippet '{args.snippet}'. Available snippets: {available}"
        )

    item = snippets[args.snippet]
    final_prompt = build_prompt(template, item["language"], item["code"])
    print(final_prompt)


if __name__ == "__main__":
    main()
