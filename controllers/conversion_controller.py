import fitz

def convert_pdf_to_text(file):
  pdf_document = fitz.open(file)

  text = ""

  for page_num in range(len(pdf_document)):
    page = pdf_document[page_num]
    text += page.get_text()

  pdf_document.close()

  return text
