# -*- coding: utf-8 -*-
import pandas as pd
import sys
import fitz
import pytesseract
import io
from PIL import Image

def extract_text_from_pdf(pdf_file):
    text = ""
    doc = fitz.open(pdf_file)
    data_list = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        image_list = page.get_images(full=True)
        pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract.exe'
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(io.BytesIO(image_bytes))
            text += pytesseract.image_to_string(image)
        text +="\n______________________________________\n\n" 
    return text

def process_pdf_text_with_pytesseract(text):
    with open("inv_text.txt", "w") as file:
        file.write(text)
    print("txt file generated successfully.")

pdf_path = sys.argv[1]
pdf_text = extract_text_from_pdf(pdf_path)
result = process_pdf_text_with_pytesseract(pdf_text)
