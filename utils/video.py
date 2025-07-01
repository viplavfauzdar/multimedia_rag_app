import cv2
import pytesseract

def extract_text_from_video(video_path, frame_interval=5):
    try:
        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = 0
        text = ""

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            if int(frame_count % (fps * frame_interval)) == 0:
                text += pytesseract.image_to_string(frame)
            frame_count += 1

        cap.release()
        return text
    except Exception as e:
        print(f"Video OCR error: {e}")
        return "[Video OCR failed]"