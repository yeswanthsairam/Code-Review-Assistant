# Code Review Assistant Prototype

This submission implements **Challenge 3: Code Review Assistant**.

## What this contains

- `main.py` - real code review assistant script that calls OpenAI API.
- `code_review_assistant_prompt.md` - reusable review prompt template.
- `sample_snippets.json` - self-created dummy snippets for testing.
- `requirements.txt` - Python dependency list.
- `SUBMISSION_SUMMARY.md` - 100-word summary of the idea and approach.

## How to use

1. Install dependencies:
   - `python3 -m pip install -r requirements.txt`
2. Set your OpenAI API key:
   - `export OPENAI_API_KEY="your_api_key_here"`
3. Run:
   - `python3 main.py --snippet simple_python`
4. Optional:
   - `python3 main.py --snippet javascript_loop --model gpt-4o-mini --print-prompt`
5. Capture output screenshots for submission.

## Submission checklist mapping

- Public link/document/screenshots:
  - Upload this folder to a public GitHub repo or Google Drive and attach screenshots.
- Public dataset link (if relevant):
  - Not required for this challenge. Dummy data is included in `sample_snippets.json`.
- Short 100-word summary:
  - Available in `SUBMISSION_SUMMARY.md`.
