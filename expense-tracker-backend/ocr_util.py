import pytesseract
from PIL import Image #image scanning and parse tool
import re 

#extracts text from file
#para: image_path : str
def extract_text(image_path : str) -> str:
    return pytesseract.image_to_string(Image.open(image_path)) #opens file at image_path, then pytesseract extracts all visible text from it using OCR


def parse_receipt(text : str):
    vendor=text.splitlines()[0].strip() #The vendor/company is usually at the top, we grab that text directly
    total=re.search(r"(?:TOTAL\s*)?[\$£€]?\s*(\d+(?:,\d{3})*\.\d{2})", text, re.IGNORECASE) #
    date=re.search(r"\b\d{1,2}/\d{1,2}/(?:\d{2}|\d{4})\b", text) #searches for exactly either 00/00/00 or 00/00/0000
    return{
        "vendor" : vendor,
        "amount" : float(total.group(1).replace(",", "")) if total else 0.0, #if the amount is valid, turn to 000,00
        "date" : date.group() if date else "unknown"
    }

