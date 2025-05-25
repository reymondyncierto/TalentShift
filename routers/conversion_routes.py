from fastapi import APIRouter
from controllers.conversion_controller import convert_pdf_to_text

router = APIRouter()

@router.post("/pdf")
def convert_pdf_to_text(file: bytes):
    return convert_pdf_to_text(file)
