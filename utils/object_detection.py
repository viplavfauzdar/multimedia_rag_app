from ultralytics import YOLO
from PIL import Image

model = YOLO("yolov8n.pt")

def detect_objects(image_path):
    results = model(image_path)
    detections = results[0].names
    return detections