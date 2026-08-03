import os
import sys
from dotenv import load_dotenv
from litellm import APIError,completion
from prompts import RESUME_ANALYZER_SYSTEM_PROMPT, RESUME_ANALYZER_USER_TEMPLATE

load_dotenv()
Model_Target = "gemini/gemini-3.6-flash"

if not os.getenv("GEMINI_API_KEY"):
    print("❌ GEMINI_API_KEY not found in environment variables.")
    sys.exit(1)


def main():
    print("\n" + "="*60)
    print("📋  AI RESUME ANALYZER ENGINE  |  VERSION 1.0  ")
    print("="*60)
    print(" -> Targeted Role Profiling: Active")
    print(" -> Strict Output Formatting Schema: Enforced")
    print("="*60 + "\n")

    #1: Capture target role parameters
    print("💼 Step 1: Specify your Target Job Role.")
    target_job = input("Target Job >> ").strip()
    if not target_job:
        print("❌ Error: Target Job role cannot be blank.")
        return
    #2: Capture resume text input (no file upload, just raw text)
    print("\n📄 Step 2: Paste the full raw text of the Resume.")
    print("(When finished pasting, press Enter, type 'SEND', and press Enter again to execute) \n" + "-"*60)
    resume_lines = []
    while True:
        line = input()
        if line.strip() == "SEND":
            break
        resume_lines.append(line)
    resume_text = "\n".join(resume_lines).strip()
    if not resume_text:
        print("❌ Error: Resume text cannot be blank.")
        return
    print ("\n✅ Input captured successfully. Processing analysis...\n")
    #3: Dynamic string composition compiling user context into the template
    formatted_user_prompt = RESUME_ANALYZER_USER_TEMPLATE.format(
        target_job=target_job,
        resume_text=resume_text
    )
    #4: Construct execution payload context
    messages = [
        {"role": "system", "content": RESUME_ANALYZER_SYSTEM_PROMPT},
        {"role": "user", "content": formatted_user_prompt}
    ]
    try:
        #5: Trigger network calculation over the free Gemini tier
        response = completion(
            model=Model_Target,
            messages=messages,
            temperature=0.1,  # Low temperature forces adherence to instructions
            custom_llm_provider="gemini"
        )

        ai_response = response.choices[0].message.content

        #6: Render the strictly formatted feedback payload
        print("\n📊 RECRUITER ASSESSMENT REPORT:")
        print("="*60)
        print(ai_response)
        print("="*60 + "\n")
    except APIError as e:
        if "503" in str(e) or "UNAVAILABLE" in str(e):
            print("\n⏳ Google's free servers are currently crowded. Retrying your request in 3 seconds...")
        else:
            print(f"\n❌ API Error: {e}\n")
    except APIError as e:
        print(f"\n❌ Pipeline Connection Error: {e}")
    except Exception as e:
        print(f"\n⚠️ Unexpected operational fault: {e}")

if __name__ == "__main__":
    main()