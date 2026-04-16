from flask import Blueprint, request, jsonify
from app.controllers.detection_controller import handle_detection
from app.repositories.user_repository import get_user_by_email

detection_bp = Blueprint("detection", __name__)


@detection_bp.route("/detect", methods=["POST"])
def detect():
    file = request.files.get("image")
    email = request.form.get("email")

    # Basic validation
    if not file:
        return jsonify({"error": "Image file is required"}), 400

    if not email:
        return jsonify({"error": "User email is required"}), 400

    # Get user
    user = get_user_by_email(email)

    if not user:
        return jsonify({"error": "User not found"}), 404

    try:
        result = handle_detection(file, user)
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500