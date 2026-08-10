import os
from fastapi import FastAPI, UploadFile, File, HTTPException, status, Query
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from analyzer import analyze_resume_with_ai
from litellm.exceptions import APIError

load_dotenv()
app = FastAPI(title="Resume Analyzer AI API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze", status_code=status.HTTP_200_OK)
async def analyze_resume_endpoint(
    file: UploadFile = File(...),
    target_job: str | None = Query(None, description="The optional target engineering role to filter by.")
):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Unsupported File Type. Only standard PDF (.pdf) documents are accepted."
        )
        
    try:
        file_bytes = await file.read() 
        structured_report = analyze_resume_with_ai(file_bytes, target_job)
        return {
            "target_job": target_job,
            "filename": file.filename,
            **structured_report        }
        
    except ValueError as val_err:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
            detail=str(val_err)
        )
    except APIError as api_err:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Upstream AI Provider authentication or rate limit fault: {str(api_err)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected web server exception occurred: {str(e)}"
        )
    finally:
        await file.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
