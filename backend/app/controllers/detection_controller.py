import os
import uuid
from flask import current_app
from app.services.detection_service import detect_damage
from app.services.cost_service import calculate_cost
from app.services.report_service import create_report

def handle_detection(file, user):
    filename = f"{uuid.uuid4()}.jpg"
    path = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)

    file.save(path)

    parts, _ = detect_damage(path)

    brand = user["car_brand"]
    model = user["car_model"]

    total_cost, breakdown = calculate_cost(parts, brand, model)

    create_report(user["id"], path, parts, total_cost)

    return {
        "image": filename,
        "parts": breakdown,
        "total_cost": total_cost
    }