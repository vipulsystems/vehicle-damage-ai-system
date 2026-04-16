from flask import jsonify
from app.exceptions.custom_exceptions import AppException


def register_error_handlers(app):

    # Handle custom exceptions
    @app.errorhandler(AppException)
    def handle_app_exception(error):
        response = {
            "error": error.message
        }
        return jsonify(response), error.status_code


    # Handle generic exceptions
    @app.errorhandler(Exception)
    def handle_general_exception(error):
        response = {
            "error": "Internal Server Error",
            "details": str(error)
        }
        return jsonify(response), 500


    # 404 handler
    @app.errorhandler(404)
    def handle_not_found(error):
        return jsonify({"error": "Route not found"}), 404