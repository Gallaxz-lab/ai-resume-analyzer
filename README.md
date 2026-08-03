# AI Resume Analyzer

A high-utility, structured AI data pipeline that evaluates raw technical resumes against specific target job descriptions. Engineered using the `liteLLM` abstraction gateway and powered by the Google Gemini free developer tier, this application leverages strategic system prompt engineering and few-shot formatting rules to transform unstructured text inputs into strict, predictable recruiter metric reports.

---

## 🚀 Key Features

- **Decoupled Prompt Layer Engineering (`prompts.py`):** Separates systemic behavior instructions and prompt text layouts from the main application loop execution code for maximum clarity.
- **Role-Targeted Profiling:** Rejects generic, open-ended evaluations by forcing the model to run analysis through the lens of an elite technical recruiter seeking a specific target role (e.g., *Junior AI Engineer*).
- **Enforced Output Schema:** Uses a low temperature setting (`0.1`) combined with negative constraints to completely strip conversational filler and guarantee a consistent, predictable markdown report layout every single time.
- **Single-Shot Data Pipeline Architecture:** Bypasses conversational context memory lists since evaluations are independent utility actions, optimizing network payload performance and costs.
- **Multi-Line Terminal Input Engine:** Implements a robust string collection matrix using a dedicated terminal capture loop so users can copy-and-paste multi-page documents seamlessly.

---

## 📁 Repository Blueprint

```text
ai-resume-analyzer/
│
├── .env                  # Private workspace developer credentials (git-ignored)
├── .env.example          # Public documentation blueprint for local environment configurations
├── .gitignore            # Explicitly bars venv, cache folders, and secrets from version tracking
├── README.md             # Systems documentation and engineering usage manuals
├── requirements.txt      # Decoupled project package software dependencies
├── prompts.py            # The Prompt Layer containing hardcoded system rules and user templates
└── main.py               # Main application entry point running inputs, composition, and API loops
```

---

## 🔑 Configuration & API Key Registration

The application uses standard local environment variables isolated from git tracking. Follow these steps to secure and register your developer credentials:

1. **Acquire a Developer Key:**
   Log into the [Google AI Studio Console](https://google.com) and generate a free API key for prototyping.

2. **Establish the Environment File:**
   Duplicate the provided configuration boilerplate inside your repository root folder:
   ```bash
   cp .env.example .env
   ```

3. **Populate Your Token Syntax Exactly:**
   Open your newly created `.env` file and insert your cryptographic developer key. Avoid using quote marks `""` or trailing spaces around your key string:
   ```ini
   GEMINI_API_KEY=AIzaSyYourActualSecureGoogleStudioKeyHere
   ```

*Note: If your API key is invalid, corrupted, or has un-vetted permissions, the application will catch a `401 UNAUTHENTICATED` runtime exception and exit safely.*

---

## 🛠️ Local Execution Blueprint

To boot the interactive script locally, initialize your isolated virtual environment wrapper and trigger the system entry point:

```bash
# 1. Activate your isolated environment wrapper
source .venv/bin/activate  # On Mac/Linux
# .venv\Scripts\activate   # On Windows

# 2. Verify dependencies are fully registered
pip install -r requirements.txt

# 3. Boot the application execution loop
python main.py
```

---

## 📊 Standard Output Schema Structure

When execution completes successfully, the application will always return a perfectly aligned report matching this precise schema taxonomy:

```text
============================================================
📊 RECRUITER ASSESSMENT REPORT:
============================================================
Overall Score: [Numerical evaluation, e.g., 85]/100

Strengths
- [Targeted skill or project alignment point 1]
- [Targeted skill or project alignment point 2]

Weaknesses
- [Identified gap relative to the target role 1]
- [Identified gap relative to the target role 2]

Missing Skills
- [Missing core industry tool keyword 1]
- [Missing core industry tool keyword 2]

Suggestions
- [Actionable metric-driven advice to improve the content]

Interview Readiness
- [Brief predictive breakdown of their technical round preparation level]
============================================================
```