from flask import request, jsonify
from app.services.report_service import get_user_reports

def get_reports_controller():
    user_id = request.args.get("user_id")

    if not user_id:
        return jsonify({"error": "user_id is required"}), 400

    try:
        reports = get_user_reports(user_id)

        return jsonify({
            "reports": reports
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500