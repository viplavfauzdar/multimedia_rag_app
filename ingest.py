import os
import tempfile
from utils.ocr import extract_text_from_image
from utils.audio import transcribe_audio
from utils.video import extract_text_from_video
from utils.embeddings import embed_and_store
import fitz  # PyMuPDF

def ingest_files(files):
    try:
        all_texts = []
        for file in files:
            suffix = file.name.split('.')[-1].lower()
            file_data = file.read()
            if not file_data:
                print(f"[WARNING] {file.name} is empty or unreadable.")
                continue
            with tempfile.NamedTemporaryFile(delete=False, suffix='.' + suffix) as tmp:
                tmp.write(file_data)
                tmp_path = tmp.name

            if suffix == 'pdf':
                doc = fitz.open(tmp_path)
                text = ''
                for page in doc:
                    text += page.get_text()
                all_texts.append(text)

            elif suffix in ['png', 'jpg', 'jpeg']:
                all_texts.append(extract_text_from_image(tmp_path))

            elif suffix in ['mp3', 'wav']:
                all_texts.append(transcribe_audio(tmp_path))

            elif suffix == 'mp4':
                all_texts.append(extract_text_from_video(tmp_path))

            elif suffix == 'txt':
                with open(tmp_path, 'r') as f:
                    all_texts.append(f.read())

            elif suffix == 'json':
                import json
                with open(tmp_path, 'r') as f:
                    data = json.load(f)
                    flat = json.dumps(data, indent=2)
                    all_texts.append(flat)

        metadatas = [{"source": file.name} for file in files]
        embed_and_store(all_texts, metadatas=metadatas)
        print(f"[DEBUG] Processed {len(all_texts)} text chunks.")
        return all_texts
    except Exception as e:
        print(f"[ERROR] Ingest failed: {e}")
        return []