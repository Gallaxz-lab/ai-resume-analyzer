import os
from litellm import completion
from pdf_reader import extract_text_from_pdf
from prompts import (
    RESUME_ANALYZER_SYSTEM_PROMPT, 
    RESUME_ANALYZER_TARGETED_TEMPLATE, 
    RESUME_ANALYZER_GENERAL_TEMPLATE
)
from schemas import ResumeAnalysisResponse

MODEL_TARGET = "gemini/gemini-3.6-flash"

def analyze_resume_with_ai(file_bytes: bytes, target_job: str) -> str:
    resume_text = extract_text_from_pdf(file_bytes)
    if not resume_text:
        raise ValueError("The uploaded PDF file contains no parseable text layers.")

    if target_job:
        formatted_user_prompt = RESUME_ANALYZER_TARGETED_TEMPLATE.format(
            target_job=target_job,
            resume_text=resume_text
        )
    else:
        formatted_user_prompt = RESUME_ANALYZER_GENERAL_TEMPLATE.format(
            resume_text=resume_text
        )
    messages = [
        {"role": "system", "content": RESUME_ANALYZER_SYSTEM_PROMPT},
        {"role": "user", "content": formatted_user_prompt}
    ]

    response = completion(
        model=MODEL_TARGET,
        messages=messages,
        temperature=0.1,                
        custom_llm_provider="gemini",    
        api_key=os.getenv("GEMINI_API_KEY"),
        response_format=ResumeAnalysisResponse
    )

    json_string_output = response.choices[0].message.content
    import json
    try:
        parsed_output = json.loads(json_string_output)
        return parsed_output
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse AI response into JSON: {str(e)}")
    
    
