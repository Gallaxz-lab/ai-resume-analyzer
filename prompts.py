"""
Prompts Layer for AI Resume Analyzer.
"""

RESUME_ANALYZER_SYSTEM_PROMPT = (
    "You are an expert technical recruiter, executive resume writer, and elite AI talent scout.\n" # Ask the model to take on a specific persona
    "Your task is to analyze candidate resumes strictly against their desired target job role.\n\n" 
    "CRITICAL COMPLIANCE RULE:\n"
    "You must evaluate the input text comprehensively and format your response exactly using the structure provided below.\n"
    "Do not include introductory words, pleasantries, wrapping code blocks, or conversational notes.\n" # Negative Prompting
    "Begin your response immediately with 'Overall Score:' and follow the template line-by-line." #An Output Indicator specifies the expected format.
)

# Template forcing structural context and few-shot formatting constraint boundaries
RESUME_ANALYZER_USER_TEMPLATE = """
Analyze the following candidate resume specifically for the target job role of: {target_job}

### EXAMPLES OF EXPECTED ANALYSIS OUTCOMES ###

---
EXAMPLE 1:
Target Job: Python Backend Engineer
<resume>
John Doe. Experience: 2 years writing scripts in Flask. Built a scraper. Knows basic SQL. No FastAPI or Docker experience.
</resume>

OUTPUT:
Overall Score: 65/100

Strengths
- 2 years of practical experience working with Python web frameworks like Flask.
- Demonstrated ability to extract data independently by building web scrapers.

Weaknesses
- Complete lack of exposure to modern async frameworks like FastAPI or continuous integration.
- Relies heavily on basic scripting rather than production-grade scalable systems.

Missing Skills
- FastAPI, asynchronous programming.
- Docker, containerization.

Suggestions
- Rebuild your existing Flask scraper application using asynchronous FastAPI to demonstrate performance optimization.
- Containerize your local python backend with a multi-stage Dockerfile and add it to your GitHub portfolio.

Interview Readiness
- Candidate is currently underprepared for an advanced backend round. They need to study asynchronous execution and container deployment before interviewing.
---

### YOUR ACTUAL CURRENT TASK ###

Target Job: {target_job}

<resume>
{resume_text}
</resume>

You must return your output precisely in this exact markdown template structure:

Overall Score: [Insert numerical score here, e.g., 75]/100

Strengths
- [Point 1 regarding target job]
- [Point 2 regarding target job]

Weaknesses
- [Point 1 regarding gaps for target job]
- [Point 2 regarding gaps for target job]

Missing Skills
- [Skill keyword 1 missing from target job requirements]
- [Skill keyword 2 missing from target job requirements]

Suggestions
- [Actionable metric-driven improvement advice 1]
- [Actionable metric-driven improvement advice 2]

Interview Readiness
- [Brief 1-2 sentence analysis of how prepared they are for a technical round for this job]
"""