import uuid
import os


ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}


def generate_filename(original_filename):
    ext = original_filename.split(".")[-1].lower()
    return f"{uuid.uuid4()}.{ext}"


def is_allowed_file(filename):
    if "." not in filename:
        return False

    ext = filename.rsplit(".", 1)[1].lower()
    return ext in ALLOWED_EXTENSIONS


def get_file_extension(filename):
    return filename.rsplit(".", 1)[1].lower()


def build_file_path(upload_folder, filename):
    return os.path.join(upload_folder, filename)