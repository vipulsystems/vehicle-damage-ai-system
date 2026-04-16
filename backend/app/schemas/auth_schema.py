def validate_signup(data):
    required_fields = [
        "name", "email", "password",
        "vehicle_id", "phone_number",
        "address", "car_brand", "car_model"
    ]

    errors = []

    for field in required_fields:
        if field not in data or not data[field]:
            errors.append(f"{field} is required")

    if "email" in data and "@" not in data["email"]:
        errors.append("Invalid email format")

    if "password" in data and len(data["password"]) < 6:
        errors.append("Password must be at least 6 characters")

    return errors


def validate_login(data):
    errors = []

    if not data.get("email"):
        errors.append("Email is required")

    if not data.get("password"):
        errors.append("Password is required")

    return errors