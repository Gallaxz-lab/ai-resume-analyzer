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

# 1. Targeted Analysis Template
RESUME_ANALYZER_TARGETED_TEMPLATE = """
Analyze the following candidate resume specifically for the target job role of: {target_job}

<resume>
{resume_text}
</resume>
"""


# 2. General Analysis Prompt Layout
RESUME_ANALYZER_GENERAL_TEMPLATE = """
Perform a comprehensive general technical evaluation of the following resume. Identify core engineering proficiencies, baseline experience gaps, and universal resume improvement steps.

<resume>
{resume_text}
</resume>
"""