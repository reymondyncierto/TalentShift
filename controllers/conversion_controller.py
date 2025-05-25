import fitz
from io import BytesIO

def convert_pdf_to_text(file_bytes):
	pdf_document = fitz.open(stream=BytesIO(file_bytes), filetype="pdf")
	text = ""
	for page_num in range(len(pdf_document)):
		page = pdf_document[page_num]
		text += page.get_text()
	pdf_document.close()
	return text
