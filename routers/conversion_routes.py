from fastapi import APIRouter, UploadFile, File
from controllers.llm_controller import LLMController
from controllers.conversion_controller import PDFConverter

llm = LLMController()
router = APIRouter()

@router.post("/pdf")
async def convert_pdf(file: UploadFile = File(...)):
  contents = await file.read()
  converter = PDFConverter(contents)
  text = converter.extract_text()
  response = llm.generate_response(text)
  return {"text": text, "response": response}
