from PIL import Image
import os
import pytesseract
import cv2
import numpy as np

def preprocess_for_ocr(pil_image):
    image = np.array(pil_image)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    return Image.fromarray(thresh)

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        print(f"[DEBUG] Image format: {image.format}, size: {image.size}, mode: {image.mode}")
        if image.format == "MPO":
            temp_jpg = image_path + "_converted.jpg"
            image.convert("RGB").save(temp_jpg, format="JPEG", quality=95)
            image = Image.open(temp_jpg)
        image = preprocess_for_ocr(image)
        text = pytesseract.image_to_string(image)
        print(f"[DEBUG OCR] Extracted text: {text[:200]}")
        return text
    except Exception as e:
        print(f"[OCR ERROR] Failed to process {image_path}: {e}")
        return "The document cannot provide an answer as the Optical Character Recognition (OCR) has failed."