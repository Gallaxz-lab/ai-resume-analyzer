# Resume Analyzer AI API

An API that reads a PDF resume and returns a score, strengths, weaknesses and suggestions as clean, structured JSON. It can give a general review or judge the resume against a specific job role.

Built with **FastAPI**, **Google Gemini** (through LiteLLM) and **Pydantic**.

---

## Features

- **Structured output:** the AI's answer is forced into a fixed JSON format (`schemas.py`), so the response is always machine-readable.
- **Two modes:** pass `target_role` to get a gap analysis for that job, or leave it out for a general technical review.
- **PDFs are read in memory:** `pypdf` with `io.BytesIO` extracts the text without saving the file to disk.
- **Async:** the file upload is read with FastAPI `async/await`, so one request does not block others.
- **Frontend-ready:** CORS is open to all origins so a web page can call the API. Restrict this to your own domain before any real deployment.

---

## Project structure

```
resume-analyzer-api/
├── .env.example     # Copy to .env and add your key
├── requirements.txt
├── schemas.py       # Pydantic models for the JSON response
├── prompts.py       # System instructions and prompt templates
├── pdf_reader.py    # PDF text extraction
├── analyzer.py      # Sends the text to the LLM and formats the result
└── main.py          # FastAPI app, CORS and endpoint
```

---

## API

### `POST /analyze`

| Part | Details |
|---|---|
| Body (form data) | `file`: the resume as a PDF (required) |
| Query parameter | `target_role`: job role to judge the resume against (optional) |

### Example: targeted mode

```bash
curl -X POST 'http://127.0.0.1:8000/analyze?target_role=AI%20Engineer' \
  -H 'accept: application/json' \
  -F 'file=@junior_developer_resume.pdf;type=application/pdf'
```

### Example: general mode

```bash
curl -X POST 'http://127.0.0.1:8000/analyze' \
  -H 'accept: application/json' \
  -F 'file=@junior_developer_resume.pdf;type=application/pdf'
```

### Example response

```json
{
  "mode": "targeted",
  "target_role": "AI Engineer",
  "filename": "junior_developer_resume.pdf",
  "score": 78,
  "strengths": [
    "Solid core Python foundations including asynchronous route design via FastAPI and Pydantic.",
    "Measurable database tuning history, reducing PostgreSQL lookup latencies by 12% via indexes."
  ],
  "weaknesses": [
    "No documented exposure to LLM orchestration tools such as LangChain or LlamaIndex.",
    "No visible experience with retrieval or semantic search pipelines."
  ],
  "suggestions": [
    "Extend your expense calculator project to read unstructured transaction logs using a vector store such as ChromaDB.",
    "Add a retrieval-augmented generation (RAG) pipeline to show modern AI backend skills."
  ]
}
```

---

## Run it locally

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Mac/Linux
# .venv\Scripts\activate         # Windows

# 2. Install packages
pip install -r requirements.txt

# 3. Add your key: copy .env.example to .env and set
#    GEMINI_API_KEY=your_key   (get one at https://aistudio.google.com)

# 4. Start the server
python main.py
```

Then open **http://127.0.0.1:8000/docs** and use the interactive page to upload a PDF and try `/analyze`.

---

## Status

Working prototype for learning and portfolio use. Scores are an AI opinion and should not be treated as a real hiring assessment.
