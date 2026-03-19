# 📄 Research Paper Analyzer (CrewAI + Gemini)

Analyze research papers from PDF and generate a structured report using multi-agent workflows.

## Features

- PDF text extraction
- Multi-agent analysis with CrewAI:
  - Summary
  - Topic classification
  - Key insights
  - Citation extraction
- Streamlit web UI
- Markdown report export

## Tech Stack

- Python
- CrewAI
- Gemini (via CrewAI native Gemini provider)
- Streamlit
- PyPDF2

## Project Structure

- `ui/app.py` — Streamlit interface
- `main.py` — pipeline orchestration
- `agents/` — task-specific agents
- `pdf_reader.py` — PDF text extraction
- `exporter.py` — markdown export helper
- `gemini_client.py` — LLM setup

## Prerequisites

- Python 3.11 or 3.12 recommended
- A valid Gemini API key

## Setup

1. Create virtual environment:

   ```powershell
   py -3.11 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install dependencies:

   ```powershell
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

3. Create `.env` in project root:

   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

## Run the App

```powershell
python -m streamlit run ui/app.py
```

Then open: `http://localhost:8501`

## Common Issues

### 1) `streamlit` command not recognized
Use module invocation instead:

```powershell
python -m streamlit run ui/app.py
```

### 2) Gemini quota error (429 RESOURCE_EXHAUSTED)
Your API key/project has no available quota. Fix by:

- Enabling billing or quota for Gemini API
- Using another API key/project with available quota
- Retrying after the indicated cooldown time

## Notes

- `.env` is ignored by git for security.
- Generated files like `temp.pdf` and `analysis_report.md` are ignored by git.

## License

No license specified yet.
