from app.ai.model_loader import get_model

def run_detection(image_path):
    model = get_model()
    results = model(image_path)
    return results