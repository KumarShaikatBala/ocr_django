import pytesseract
from pdf2image import convert_from_bytes
from PIL import Image
import io


def extract_text_from_image(image):
    return pytesseract.image_to_string(image)


def extract_text_from_pdf(pdf_file):
    text = ""
    images = convert_from_bytes(pdf_file.read())
    for i, image in enumerate(images):
        text += f"Page {i + 1}:\n{extract_text_from_image(image)}\n\n"
    return text


def process_document(document):
    try:
        document.status = 'processing'
        document.save()

        if document.file_type == 'pdf':
            text = extract_text_from_pdf(document.file)
        else:
            with Image.open(document.file) as img:
                text = extract_text_from_image(img)

        document.text = text
        document.status = 'completed'
    except Exception as e:
        document.status = 'failed'
        document.text = f"Error: {str(e)}"
    finally:
        document.save()