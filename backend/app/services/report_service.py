from app.repositories.report_repository import save_report, get_reports_by_user


def create_report(user_id, image_path, parts, total_cost):
    save_report(user_id, image_path, parts, total_cost)


def get_user_reports(user_id):
    reports = get_reports_by_user(user_id)
    return reports