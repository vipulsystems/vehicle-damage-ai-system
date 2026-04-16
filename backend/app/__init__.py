from flask import Flask
from flask_cors import CORS
from app.config.dev_config import DevelopmentConfig
from app.config.prod_config import ProductionConfig
from app.exceptions.error_handler import register_error_handlers

from app.routes.auth_routes import auth_bp
from app.routes.detection_routes import detection_bp
from app.routes.report_routes import report_bp


def create_app():
    app = Flask(__name__)
    CORS(app)
    env = "dev"

    if env == "prod":
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(detection_bp, url_prefix="/api")
    app.register_blueprint(report_bp, url_prefix="/api")

    # Error handlers
    register_error_handlers(app)
    print(app.url_map)
    return app

