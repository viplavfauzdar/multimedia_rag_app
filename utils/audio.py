import whisper

def transcribe_audio(audio_path):
    try:
        model = whisper.load_model("base")
        result = model.transcribe(audio_path)
        return result.get("text", "")
    except Exception as e:
        print(f"Transcription error: {e}")
        return "[Transcription failed]"