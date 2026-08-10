# Resume Analyzer AI API

A production-grade, asynchronous FastAPI service that parses raw binary PDF resumes and processes them through an engineered Large Language Model pipeline. Leveraging the `liteLLM` gateway and powered by Google Gemini, this API supports both general software engineering audits and hyper-targeted role-based assessments, guaranteeing output delivery inside strict, parseable JSON schema payloads.

---

## 🚀 Key Architectural Features

- **Pydantic Structural Enforcement (`schemas.py`):** Rejects erratic markdown or conversational string outputs from the AI by routing calls using rigid `response_format` constraint gates.
- **Dynamic Dual-Route Extraction:** Implements conditional parsing prompts. If a query parameter is passed, it executes a market-fit gap analysis; if omitted, it returns a general technical summary.
- **Memory-Safe PDF Stream Parsing:** Employs `pypdf` combined with memory-resident `io.BytesIO` byte wrappers to extract text on the fly without performing heavy, un-safe server hard-drive writes.
- **Asynchronous Multitasking Gateway:** Uses native FastAPI `async/await` mechanics to read multipart file packages streamingly without gridlocking upstream thread execution loops.
- **CORS Infrastructure Integration:** Configured with open cross-origin allowances to support seamless out-of-the-box integration with modern frontend single-page web applications.

---

## 📁 Repository Map

```text
resume-analyzer-api/
│
├── .env                  # Encrypted workspace developer credentials (git-ignored)
├── README.md             # Systems documentation and technical execution manuals
├── requirements.txt      # Decoupled project package application dependencies
├── schemas.py            # Strict Pydantic BaseModel validation gatekeepers
├── prompts.py            # Isolated System Instructions and structural User templates
├── pdf_reader.py         # Dedicated binary PDF data character stream extractor
├── analyzer.py           # Core business worker orchestrating model formatting blocks
└── main.py               # FastAPI router engine initialization, CORS, and endpoint paths
```

---

## 🌐 API Endpoint Specification

### `POST /analyze`

Accepts a multi-part file binary upload alongside an optional URL string modifier to calculate assessment metrics.

#### Request Components:
- **Headers:** `Content-Type: multipart/form-data`
- **Query Parameter:** `target_role` *(String | Optional)* — The technical career milestone role to judge the candidate qualifications against.
- **Body Payload (Form Data):** `file` *(Binary PDF | Mandatory)* — The physical resume document.

---

## 📝 Usage & Integration Examples

### 1. Example Request (Targeted Role Mode)

To hit the API using standard terminal tool chains like `curl`, reference your file binary using the `@` symbol and attach the query string suffix:

```bash
curl -X 'POST' \
  'http://127.0.0' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@junior_developer_resume.pdf;type=application/pdf'
```

---

### 2. Example Request (General Evaluation Mode)

If you omit the query parameter completely from your connection call, the API defaults to an organic general critique:

```bash
curl -X 'POST' \
  'http://127.0.0' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@junior_developer_resume.pdf;type=application/pdf'
```

---

### 3. Example JSON Response Payload

Regardless of the incoming configuration, the system sanitizes raw responses, providing metadata tracking parameters, and outputs clean numerical values and array structures:

```json
{
  "mode": "targeted",
  "target_role": "AI Engineer",
  "filename": "junior_developer_resume.pdf",
  "score": 78,
  "strengths": [
    "Solid core Python foundations including production-ready asynchronous route design via FastAPI and Pydantic.",
    "Measurable database tuning history, reducing relational PostgreSQL lookup latencies by 12% via declarative indexes."
  ],
  "weaknesses": [
    "Lacks documented field exposure to enterprise LLM orchestration layers such as LangChain, LlamaIndex, or native tool-calling maps.",
    "No visible application experience involving unstructured data retrieval mechanisms or semantic search indexing pipelines."
  ],
  "suggestions": [
    "Refactor your local expense calculator project to consume unstructured financial transaction logs via a vector store database like ChromaDB or Qdrant.",
    "Incorporate a dedicated retrieval-augmented generation (RAG) pipeline to demonstrate deep mastery of modern AI backend requirements."
  ]
}
```

---

## 🛠️ Local Installation & Activation Blueprint

To execute your API application server sandbox locally, initialize your isolated environment wrapper and boot the server using Uvicorn:

```bash
# 1. Spin up your local virtual environment
python -m venv .venv
source .venv/bin/activate  # On Mac/Linux
# .venv\Scripts\activate   # On Windows

# 2. Register required packages
pip install -r requirements.txt

# 3. Secure your Google AI Studio credentials in your .env file
# GEMINI_API_KEY=AIzaSy...

# 4. Fire up the hot-reloading web worker
python main.py
```

Once running, navigate your web browser directly to **`http://127.0.0`** or (http://localhost:8000/docs#/)** (Swagger UI) to access the interactive Swagger UI panel interface.
