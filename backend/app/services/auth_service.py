import bcrypt
from app.repositories.user_repository import create_user, get_user_by_email


def register_user(data):
    existing_user = get_user_by_email(data["email"])

    if existing_user:
        raise Exception("User already exists")

    hashed_password = bcrypt.hashpw(
        data["password"].encode(),
        bcrypt.gensalt()
    ).decode()

    user_data = {
        "name": data["name"],
        "email": data["email"],
        "password": hashed_password,
        "vehicle_id": data["vehicle_id"],
        "phone_number": data["phone_number"],
        "address": data["address"],
        "car_brand": data["car_brand"],
        "car_model": data["car_model"]
    }

    user_id = create_user(user_data)

    return {
        "message": "User registered successfully",
        "user_id": user_id
    }


def login_user(email, password):
    user = get_user_by_email(email)

    if not user:
        return None

    if not bcrypt.checkpw(password.encode(), user["password"].encode()):
        return None

    return {
        "message": "Login successful",
        "user_id": user["id"],
        "email": user["email"]
    }