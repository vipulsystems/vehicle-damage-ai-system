from flask import request, jsonify
from app.services.auth_service import register_user, login_user

def signup_controller():
    data = request.get_json()

    required_fields = [
        "name", "email", "password",
        "vehicle_id", "phone_number",
        "address", "car_brand", "car_model"
    ]

    # Validate input
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        result = register_user(data)
        return jsonify(result), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def login_controller():
    data = request.get_json()

    if not data.get("email") or not data.get("password"):
        return jsonify({"error": "Email and password required"}), 400

    try:
        result = login_user(data["email"], data["password"])

        if not result:
            return jsonify({"error": "Invalid credentials"}), 401

        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500