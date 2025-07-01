# Streamlit UI (already created)
# multimedia_rag_app/app.py
import streamlit as st
from ingest import ingest_files
from retriever import answer_query
import os
from dotenv import load_dotenv
#
from utils.captioning import generate_caption

load_dotenv()

st.title("📚 Multimedia RAG AI App")

uploaded_files = st.file_uploader("Upload files (PDF, Image, Audio, Video, Text, JSON)",
                                   type=["pdf", "png", "jpg", "jpeg", "mp3", "wav", "mp4", "txt", "json"],
                                   accept_multiple_files=True)

if uploaded_files:
    with st.spinner("Processing files and updating vector store..."):
        texts = ingest_files(uploaded_files)
    st.success("Files processed and indexed!")
    st.markdown("**Uploaded files:**")
    for f in uploaded_files:
        st.markdown(f"- {f.name}")
        if f.type.startswith("image/"):
            st.image(f, caption=f.name)
            from utils.ocr import extract_text_from_image
            import tempfile
            from ultralytics import YOLO
            from PIL import Image as PILImage
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_img:
                tmp_img.write(f.read())
                tmp_img_path = tmp_img.name

            show_ocr = st.checkbox("Run OCR", value=True, key=f"ocr_{f.name}")
            show_captioning = st.checkbox("Generate Caption", value=True, key=f"caption_{f.name}")
            show_detection = st.checkbox("Detect Objects", value=True, key=f"detection_{f.name}")

            if show_ocr:
                text = extract_text_from_image(tmp_img_path)
                st.markdown("**OCR Extracted Text:**")
                st.markdown(text)

            if show_captioning:
                caption = generate_caption(tmp_img_path)
                st.markdown(f"**Image Caption:** {caption}")

            if show_detection:
                model = YOLO("yolov8n.pt")
                results = model(tmp_img_path)
                boxed_image = results[0].plot()
                st.image(boxed_image, caption="Detected Objects (with bounding boxes)")
                detected_objects = [model.names[int(cls)] for cls in results[0].boxes.cls]
                st.markdown("**Detected Objects:** " + ", ".join(map(str, detected_objects)))
        elif f.type.startswith("audio/") or f.type.startswith("video/"):
            import tempfile
            from utils.audio import transcribe_audio
            from pydub import AudioSegment

            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4" if f.type.endswith("mp4") else ".mp3") as tmp_media:
                f.seek(0)
                tmp_media.write(f.read())
                tmp_av_path = tmp_media.name

            if f.type.startswith("audio/"):
                st.audio(tmp_av_path, format="audio/mp3")
            else:
                st.video(tmp_av_path)

            st.markdown("**Transcription:**")
            try:
                transcription = transcribe_audio(tmp_av_path)
                st.markdown(transcription)
            except Exception as e:
                st.error(f"Transcription failed: {str(e)}")
        elif f.type.startswith("application/") or f.type.startswith("text/"):
            st.markdown("### Extracted Text Samples:")
            for i, text in enumerate(texts[:3]):
                st.text_area(f"Sample Chunk {i+1}", text[:1000], height=200, key=f"chunk_{f.name}_{i}")

            query = st.text_input("Ask a question based on uploaded content:")

            if query:
                with st.spinner("Searching and generating response..."):
                    try:
                        answer = answer_query(query)
                        st.markdown(answer)
                    except Exception as e:
                        st.error(f"Error: {str(e)}")


with st.sidebar:
    st.markdown("### About This App")
    st.info("Upload PDFs, images, videos, audio, JSON, or text files.\n\nAsk questions based on content.")
