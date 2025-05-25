from fastapi import APIRouter, UploadFile, File
from controllers.llm_controller import LLMController
from controllers.conversion_controller import PDFConverter
from services.database_service import DatabaseService
import json

llm = LLMController()
router = APIRouter()
db = DatabaseService()

@router.post("/pdf")
async def convert_pdf(file: UploadFile = File(...)):
  contents = await file.read()
  converter = PDFConverter(contents)
  text = converter.extract_text()
  response = llm.generate_response(text)
  try:
    data = json.loads(response)
  except json.JSONDecodeError:
    return {"status": "error", "message": "Invalid JSON from LLM"}

  try:
    db.insert_resume(data)
  except Exception as e:
    return {"status": "error", "message": str(e)}

  return {
    "status": "success",
    "message": "Resume processed and stored.",
  }
