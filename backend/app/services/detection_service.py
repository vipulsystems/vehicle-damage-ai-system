from app.ai.predictor import run_detection
from app.ai.post_processor import process_results


def detect_damage(image_path):
    results = run_detection(image_path)
    parts = process_results(results)

    return parts, results