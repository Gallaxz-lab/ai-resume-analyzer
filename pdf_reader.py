import io
from pypdf import PdfReader

def extract_text_from_pdf(file_bytes: bytes) -> str:
    try:
        pdf_stream = io.BytesIO(file_bytes)
        reader = PdfReader(pdf_stream)
        
        extracted_text = []
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                extracted_text.append(page_text)
                
        return "\n".join(extracted_text).strip()
    except Exception as e:
        raise ValueError(f"Failed to process binary PDF structure: {str(e)}")
