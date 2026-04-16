from ultralytics import YOLO
from app.config.config import Config

model = None

def get_model():
    global model
    if model is None:
        model = YOLO(Config.MODEL_PATH)
    return model