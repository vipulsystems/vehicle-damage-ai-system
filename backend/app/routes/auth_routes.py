from flask import Blueprint
from app.controllers.auth_controller import signup_controller, login_controller

auth_bp = Blueprint("auth", __name__)

# Signup
@auth_bp.route("/signup", methods=["POST"])
def signup():
    return signup_controller()


# Login
@auth_bp.route("/login", methods=["POST"])
def login():
    return login_controller()