from fastapi import APIRouter, UploadFile, File
from controllers.llm_controller import LLMController
from controllers.conversion_controller import PDFConverter
import json

llm = LLMController()
router = APIRouter()

@router.post("/pdf")
async def convert_pdf(file: UploadFile = File(...)):
  contents = await file.read()
  converter = PDFConverter(contents)
  text = converter.extract_text()
  response = llm.generate_response(text)
  data = json.loads(response)

  print(data)

  return {"status": "success"}
