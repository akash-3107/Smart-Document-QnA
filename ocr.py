import pytesseract
from pdf2image import convert_from_path

def extract_text_from_pdf(pdf_path):
    """
    Convert PDF pages to images, then run OCR on each page.
    Returns a list of (page_num, text).
    """
    pages = convert_from_path(pdf_path)
    extracted = []
    for i, page in enumerate(pages):
        text = pytesseract.image_to_string(page)
        extracted.append((i + 1, text))
    return extracted
