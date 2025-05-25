import fitz
from io import BytesIO

class PDFConverter:
	def __init__(self, file_bytes):
		self.file_bytes = file_bytes
		self.pdf_document = fitz.open(stream=BytesIO(file_bytes), filetype="pdf")

	def extract_text(self):
		text = ""
		for page_num in range(len(self.pdf_document)):
			page = self.pdf_document[page_num]
			text += page.get_text()
		self.pdf_document.close()
		return text
