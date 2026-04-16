def validate_detection_request(file, email):
    errors = []

    if not file:
        errors.append("Image file is required")

    if file:
        filename = file.filename.lower()
        if not filename.endswith((".jpg", ".jpeg", ".png")):
            errors.append("Invalid file type (only jpg, jpeg, png allowed)")

    if not email:
        errors.append("User email is required")

    return errors