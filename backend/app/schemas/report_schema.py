def validate_report_request(user_id):
    errors = []

    if not user_id:
        errors.append("user_id is required")

    try:
        int(user_id)
    except:
        errors.append("user_id must be an integer")

    return errors