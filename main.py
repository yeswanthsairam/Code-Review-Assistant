import argparse
import json
import os
from pathlib import Path

from openai import OpenAI


def load_template(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_snippets(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def build_prompt(template: str, language: str, code: str) -> str:
    return (
        template.replace("{{LANGUAGE}}", language).replace("{{CODE_SNIPPET}}", code)
    )


def review_code_with_openai(prompt: str, model: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit(
            "OPENAI_API_KEY is not set. Export it before running this script."
        )

    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model=model,
        input=prompt,
        temperature=0.3,
    )
    return response.output_text.strip()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run a code review assistant using the OpenAI API."
    )
    parser.add_argument(
        "--snippet",
        default="simple_python",
        help="Snippet key from sample_snippets.json",
    )
    parser.add_argument(
        "--model",
        default="gpt-4o-mini",
        help="OpenAI model name to use",
    )
    parser.add_argument(
        "--print-prompt",
        action="store_true",
        help="Print the generated prompt before sending it",
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
    prompt = build_prompt(template, item["language"], item["code"])

    if args.print_prompt:
        print("=== Prompt Sent To Model ===")
        print(prompt)
        print("=== End Prompt ===\n")

    print("Running review with OpenAI...\n")
    review = review_code_with_openai(prompt, args.model)
    print(review)


if __name__ == "__main__":
    main()
