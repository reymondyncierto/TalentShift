from fastapi import APIRouter, UploadFile, File
from controllers.conversion_controller import convert_pdf_to_text

router = APIRouter()

@router.post("/pdf")
async def convert_pdf(file: UploadFile = File(...)):
  contents = await file.read()
  return {"text": convert_pdf_to_text(contents)}
