from flask import Blueprint, request, jsonify
from app.controllers.report_controller import get_reports_controller

report_bp = Blueprint("report", __name__)


@report_bp.route("/reports", methods=["GET"])
def get_reports():
    return get_reports_controller()